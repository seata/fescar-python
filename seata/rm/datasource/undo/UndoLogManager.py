#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from loguru import logger

from seata.config.Config import ConfigFactory
from seata.core.compressor.CompressorType import CompressorType
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.exception.TransactionException import BranchTransactionException
from seata.exception.TransactionExceptionCode import TransactionExceptionCode
from seata.rm.datasource.sql.TableMetaCacheFactory import TableMetaCacheFactory
from seata.rm.datasource.undo.BranchUndoLog import BranchUndoLog
from seata.rm.datasource.undo.State import State
from seata.rm.datasource.undo.UndoExecutorFactory import UndoExecutorFactory
from seata.rm.datasource.undo.UndoLogParserFactory import UndoLogParserFactory
from seata.sqlparser.util.CollectionUtil import CollectionUtil


# CREATE TABLE IF NOT EXISTS `undo_log` (
#     `branch_id`     BIGINT       NOT NULL COMMENT 'branch transaction id',
#     `xid`           VARCHAR(128) NOT NULL COMMENT 'global transaction id',
#     `context`       VARCHAR(128) NOT NULL COMMENT 'undo_log context,such as serialization',
#     `rollback_info` LONGBLOB     NOT NULL COMMENT 'rollback info',
#     `log_status`    INT(11)      NOT NULL COMMENT '0:normal status,1:defense status',
#     `log_created`   DATETIME(6)  NOT NULL COMMENT 'create datetime',
#     `log_modified`  DATETIME(6)  NOT NULL COMMENT 'modify datetime',
#     UNIQUE KEY `ux_undo_log` (`xid`, `branch_id`)
# ) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT ='AT transaction mode undo table';


class UndoLogManager(object):
    UNDO_LOG_TABLE_NAME = ConfigFactory.get_config().get("client.undo.log-table")
    DELETE_UNDO_LOG_SQL = "DELETE FROM " + UNDO_LOG_TABLE_NAME + " WHERE branch_id = %s AND xid = %s"
    SELECT_UNDO_LOG_SQL = "SELECT * FROM " + UNDO_LOG_TABLE_NAME + " WHERE branch_id = %s AND xid = %s FOR UPDATE"

    CONTEXT_SERIALIZER = "serializer"
    CONTEXT_COMPRESSOR_TYPE = "compressorType"

    def get_db_type(self):
        raise NotImplemented('need subclass implemented')

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

    def undo(self, data_source_proxy, xid, branch_id):
        cp = None
        con = None
        cursor = None
        original_auto_commit = True
        while True:
            try:
                cp = data_source_proxy.connection()
                con = cp.target_connection
                if cp.get_autocommit() == original_auto_commit:
                    cp.set_origin_autocommit(False)

                cursor = con.cursor()
                cursor.execute(self.SELECT_UNDO_LOG_SQL, (branch_id, xid))
                rs_all = cursor.fetchall()
                exists = False

                description = cursor.description
                col_map = {}
                for idx, d in enumerate(description):
                    # 0 name 1 type_code
                    col_map[d[0]] = idx
                if len(col_map) == 0:
                    raise ShouldNeverHappenException()
                # ********** execute on begin **********
                for i in range(len(rs_all)):
                    rs = rs_all[i]
                    exists = True
                    state = rs[col_map['log_status']]
                    if not self.can_undo(state):
                        logger.warning("xid [{}] branch [{}], ignore [{}] undo_log".format(xid, branch_id, State(state)))
                        return
                    context_string = rs[col_map['context']]
                    context_map = self.parse_context(context_string)
                    rollback_info = self.get_rollback_info(rs[col_map['rollback_info']])
                    serializer = None
                    if context_map is not None:
                        serializer = context_map[self.CONTEXT_SERIALIZER]

                    if serializer is None:
                        parser = UndoLogParserFactory.get_instance()
                    else:
                        parser = UndoLogParserFactory.get_instance(serializer)
                    branch_undo_log = parser.decode(rollback_info)

                    sql_undo_logs = branch_undo_log.sql_undo_logs
                    if len(sql_undo_logs) > 1:
                        sql_undo_logs.reverse()
                    for j in range(len(sql_undo_logs)):
                        sql_undo_log = sql_undo_logs[j]
                        table_meta = TableMetaCacheFactory.get_table_meta_cache(data_source_proxy.db_type) \
                            .get_table_meta(con, sql_undo_log.table_name, data_source_proxy.get_resource_id())
                        sql_undo_log.set_table_meta(table_meta)
                        undo_executor = UndoExecutorFactory.get_undo_executor(data_source_proxy.db_type, sql_undo_log)
                        undo_executor.execute_on(con)
                # ********** execute on end **********

                if exists:
                    self.delete_undo_log(xid, branch_id, con)
                    con.commit()
                    logger.info('xid [{}] branch [{}], undo_log deleted with [{}]'.format(xid, branch_id,
                                                                                    State.GlobalFinished.name))
                else:
                    self.insert_undo_log_with_global_finished(xid, branch_id, UndoLogParserFactory.get_instance(),
                                                              con)
                    con.commit()
                    logger.info('xid [{}] branch [{}], undo_log added with [{}]'.format(xid, branch_id,
                                                                                  State.GlobalFinished.name))
                return
            except Exception as e:
                error_name = e.__class__.__name__
                if error_name == 'IntegrityError':
                    logger.info('xid [{}] branch [{}], undo_log inserted, retry rollback'.format(xid, branch_id))
                else:
                    logger.error(e)
                    if cp is not None:
                        try:
                            con.rollback()
                        except Exception as e:
                            logger.error("close connection while undo", e)
                    raise BranchTransactionException(TransactionExceptionCode.BranchRollbackFailed_Retriable)
            finally:
                if cursor is not None:
                    try:
                        cursor.close()
                    except Exception:
                        pass
                if cp is not None:
                    if original_auto_commit:
                        cp.set_origin_autocommit(True)
                    try:
                        cp.close()
                    except Exception:
                        pass

    def delete_undo_log(self, xid, branch_id, connection):
        cursor = None
        try:
            cursor = connection.cursor()
            cursor.execute(self.DELETE_UNDO_LOG_SQL, (branch_id, xid))
            connection.commit()
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass

    def get_rollback_info(self, rollback_info):
        return rollback_info

    def batch_delete_undo_log(self, xids, branch_ids, connection):
        raise NotImplemented('need subclass implemented')

    def delete_undo_log_by_log_created(self, log_created, limit_rows, connection):
        raise NotImplemented('need subclass implemented')

    def insert_undo_log_with_global_finished(self, xid, branch_id, undo_log_parser, connection):
        raise NotImplemented('need subclass implemented')

    def insert_undo_log_with_normal(self, xid, branch_id, rollback_context, undo_log_content, connection):
        raise NotImplemented('need subclass implemented')
