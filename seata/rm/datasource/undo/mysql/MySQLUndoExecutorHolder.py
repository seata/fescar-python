#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.rm.datasource.undo.UndoExecutorHolder import UndoExecutorHolder
from seata.rm.datasource.undo.mysql.MySQLUndoDeleteExecutor import MySQLUndoDeleteExecutor
from seata.rm.datasource.undo.mysql.MySQLUndoInsertExecutor import MySQLUndoInsertExecutor
from seata.rm.datasource.undo.mysql.MySQLUndoUpdateExecutor import MySQLUndoUpdateExecutor


class MySQLUndoExecutorHolder(UndoExecutorHolder):
    def get_insert_executor(self, sql_undo_log):
        return MySQLUndoInsertExecutor(sql_undo_log)

    def get_update_executor(self, sql_undo_log):
        return MySQLUndoUpdateExecutor(sql_undo_log)

    def get_delete_executor(self, sql_undo_log):
        return MySQLUndoDeleteExecutor(sql_undo_log)