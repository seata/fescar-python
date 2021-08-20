#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.rm.datasource.undo.UndoExecutor import UndoExecutor


class MySQLUndoDeleteExecutor(UndoExecutor):
    def __init__(self, sql_undo_log):
        super(MySQLUndoDeleteExecutor, self).__init__(sql_undo_log)