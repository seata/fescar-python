#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.compressor.CompressorType import CompressorType
from seata.rm.datasource.undo.State import State
from seata.rm.datasource.undo.UndoLogManager import UndoLogManager
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class MySQLUndoLogManager(UndoLogManager):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_insert_undo_log_sql(cls):
        return "INSERT INTO " + \
               cls.UNDO_LOG_TABLE_NAME + \
               " (branch_id, xid, context, rollback_info, log_status, log_created, log_modified) " + \
               "values (%s,%s,%s,%s,%s,now(6),now(6))"

    def get_db_type(self):
        return JdbcConstants.MYSQL

    def batch_delete_undo_log(self, xids, branch_ids, connection):
        if (xids is None or len(xids) == 0) or (branch_ids is None or len(branch_ids) == 0):
            return
        batch_delete_sql = self.to_batch_delete_undo_log_sql(len(xids), len(branch_ids))
        cursor = connection.cursor()
        params = []
        params.extend(branch_ids)
        params.extend(xids)
        cursor.execute(batch_delete_sql, tuple(params))

    def to_batch_delete_undo_log_sql(self, xid_size, branch_id_size):
        sql = "DELETE FROM " + self.UNDO_LOG_TABLE_NAME + " WHERE branch_id IN "
        sql += self.append_in_param(branch_id_size)
        sql += " AND xid IN "
        sql += self.append_in_param(xid_size)
        return sql

    def append_in_param(self, size):
        sql = " ("
        for i in range(size):
            sql += "%s"
            if i < size - 1:
                sql += ","
        sql += ") "
        return sql


    def delete_undo_log_by_log_created(self, log_created, limit_rows, connection):
        # TODO
        return 1

    def insert_undo_log_with_global_finished(self, xid, branch_id, undo_log_parser, connection):
        self.insert_undo_log(xid, branch_id, self.build_context(undo_log_parser.get_name(), CompressorType.NONE),
                             undo_log_parser.get_default_content(), State.GlobalFinished, connection)

    def insert_undo_log_with_normal(self, xid, branch_id, rollback_context, undo_log_content, connection):
        self.insert_undo_log(xid, branch_id, rollback_context, undo_log_content, State.Normal, connection)

    def insert_undo_log(self, xid, branch_id, rollback_context, undo_log_content, state, connection):
        try:
            cursor = connection.cursor()
            cursor.execute(self.get_insert_undo_log_sql(),
                           (branch_id, xid, rollback_context, undo_log_content, state.value))
            connection.commit()
        except Exception as e:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception as ignored:
                    pass
