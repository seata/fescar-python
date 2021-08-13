#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from seata.core.compressor.CompressorType import CompressorType
from seata.exception.TransactionException import BranchTransactionException
from seata.exception.TransactionExceptionCode import TransactionExceptionCode
from seata.rm.datasource.sql.TableMetaCacheFactory import TableMetaCacheFactory
from seata.rm.datasource.undo.BranchUndoLog import BranchUndoLog
from seata.rm.datasource.undo.State import State
from seata.rm.datasource.undo.UndoExecutorFactory import UndoExecutorFactory
from seata.rm.datasource.undo.UndoLogParserFactory import UndoLogParserFactory
from seata.sqlparser.util.CollectionUtil import CollectionUtil


class UndoLogManager(object):
    UNDO_LOG_TABLE_NAME = "undo_log"
    DELETE_UNDO_LOG_SQL = "DELETE FROM " + UNDO_LOG_TABLE_NAME + " WHERE branch_id = ? AND xid = ?"
    SELECT_UNDO_LOG_SQL = "SELECT * FROM " + UNDO_LOG_TABLE_NAME + " WHERE branch_id = ? AND xid = ? FOR UPDATE"

    CONTEXT_SERIALIZER = "serializer"
    CONTEXT_COMPRESSOR_TYPE = "compressorType"

    def get_db_type(self):
        pass

    def build_context(self, parse_name, compressor_type):
        context_map = {self.CONTEXT_SERIALIZER: parse_name, self.CONTEXT_COMPRESSOR_TYPE: compressor_type.name}
        return CollectionUtil.encode_map(context_map)

    def parse_context(self, context_string):
        return CollectionUtil.decode_map(context_string)

    def flush_undo_logs(self, connection_proxy):
        context = connection_proxy.context
        if not context.has_undo_log():
            return
        xid = context.xid
        branch_id = context.branch_id
        branch_undo_log = BranchUndoLog()
        branch_undo_log.xid = xid
        branch_undo_log.branch_id = branch_id
        branch_undo_log.sql_undo_logs = context.get_undo_items()

        parser = UndoLogParserFactory.get_instance()
        undo_log_content = parser.encode(branch_undo_log)
        compress_type = CompressorType.NONE

        self.insert_undo_log_with_normal(xid, branch_id, self.build_context(parser.get_name(), compress_type),
                                         undo_log_content, connection_proxy.target_connection)

    def can_undo(self, state):
        return state == State.Normal.value

    def undo(self, pooled_db_proxy, xid, branch_id):
        con = None
        cursor = None
        original_auto_commit = True
        while True:
            try:
                con = pooled_db_proxy.get_origin_connection()
                if con.autocommit == original_auto_commit:
                    con.autocommit = False

                cursor = con.cursor()
                """
                CREATE TABLE IF NOT EXISTS `undo_log`
                (
                    `branch_id`     BIGINT       NOT NULL COMMENT 'branch transaction id',
                    `xid`           VARCHAR(128) NOT NULL COMMENT 'global transaction id',
                    `context`       VARCHAR(128) NOT NULL COMMENT 'undo_log context,such as serialization',
                    `rollback_info` LONGBLOB     NOT NULL COMMENT 'rollback info',
                    `log_status`    INT(11)      NOT NULL COMMENT '0:normal status,1:defense status',
                    `log_created`   DATETIME(6)  NOT NULL COMMENT 'create datetime',
                    `log_modified`  DATETIME(6)  NOT NULL COMMENT 'modify datetime',
                    UNIQUE KEY `ux_undo_log` (`xid`, `branch_id`)
                ) ENGINE = InnoDB AUTO_INCREMENT = 1 DEFAULT CHARSET = utf8 COMMENT ='AT transaction mode undo table';
                """
                cursor.execute(self.SELECT_UNDO_LOG_SQL, (branch_id, xid))
                rs = cursor.fetchall()
                exists = False
                for i in range(len(rs)):
                    exists = True
                    state = rs[4]
                    if not self.can_undo(state):
                        print("xid {} branch {}, ignore {} undo_log".format(xid, branch_id, state))
                        return
                    context_string = rs[2]
                    context_map = self.parse_context(context_string)
                    rollback_info = self.get_rollback_info(rs[3])
                    serializer = None
                    if context_map is None:
                        serializer = context_map[self.CONTEXT_SERIALIZER]

                    if serializer is None:
                        parser = UndoLogParserFactory.get_instance()
                    else:
                        parser = UndoLogParserFactory.get_instance(serializer)
                    branch_undo_log = parser.decode(rollback_info)

                    sql_undo_logs = branch_undo_log.sql_undo_logs
                    if len(sql_undo_logs) > 1:
                        sql_undo_logs.reverse()
                    for i in range(len(sql_undo_logs)):
                        sql_undo_log = sql_undo_logs[i]
                        table_meta = TableMetaCacheFactory.get_table_meta_cache(pooled_db_proxy.db_type) \
                            .get_table_meta(con, sql_undo_log.table_name, pooled_db_proxy.resource_id)
                        sql_undo_log.set_table_meta(table_meta)
                        undo_executor = UndoExecutorFactory.get_undo_executor(pooled_db_proxy.db_type, sql_undo_log)
                        undo_executor.execute_on(con)

                    if exists:
                        self.delete_undo_log(xid, branch_id, con)
                        con.commit()
                        print('xid {} branch {}, undo_log deleted with {}'.format(xid, branch_id,
                                                                                  State.GlobalFinished.name))
                    else:
                        self.insert_undo_log_with_global_finished(xid, branch_id, UndoLogParserFactory.get_instance(),
                                                                  con)
                        con.commit()
                        print('xid {} branch {}, undo_log added with {}'.format(xid, branch_id,
                                                                                State.GlobalFinished.name))
                    return
            except Exception as e:
                error_name = e.__class__.__name__
                if error_name == 'IntegrityError':
                    print('xid {} branch {}, undo_log inserted, retry rollback'.format(xid, branch_id))
                else:
                    if con is not None:
                        try:
                            con.rollback()
                        except Exception as e:
                            print("close connection while undo", e)
                    raise BranchTransactionException(TransactionExceptionCode.BranchRollbackFailed_Retriable)
            finally:
                if cursor is not None:
                    try:
                        cursor.close()
                    except Exception as ignored:
                        pass
                if con is not None:
                    if original_auto_commit:
                        con.autocommit = True
                    try:
                        con.close()
                    except Exception as ignored:
                        pass

    def delete_undo_log(self, xid, branch_id, connection):
        try:
            cursor = connection.cursor()
            cursor.execute(self.DELETE_UNDO_LOG_SQL, (branch_id, xid))
            cursor.commit()
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception as ignored:
                    pass

    def batch_delete_undo_log(self, xids, branch_ids, connection):
        pass

    def delete_undo_log_by_log_created(self, log_created, limit_rows, connection):
        pass

    def insert_undo_log_with_global_finished(self, xid, branch_id, undo_log_parser, connection):
        pass

    def insert_undo_log_with_normal(self, xid, branch_id, rollback_context, undo_log_content, connection):
        pass
