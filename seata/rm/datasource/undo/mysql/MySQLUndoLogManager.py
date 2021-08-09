#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.rm.datasource.undo.UndoLogManager import UndoLogManager
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class MySQLUndoLogManager(UndoLogManager):

    def get_db_type(self):
        return JdbcConstants.MYSQL
