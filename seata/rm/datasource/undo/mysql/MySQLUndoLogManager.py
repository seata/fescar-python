#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.rm.datasource.undo.UndoLogManager import UndoLogManager
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class MySQLUndoLogManager(UndoLogManager):

    def get_db_type(self):
        return JdbcConstants.MYSQL

    def flush_undo_logs(self, cp):
        pass

    def delete_undo_log(self, xid, branch_id, connection):
        pass

    def batch_delete_undo_log(self, xids, branch_ids, connection):
        pass

    def delete_undo_log_by_log_created(self, log_created, limit_rows, connection):
        pass
