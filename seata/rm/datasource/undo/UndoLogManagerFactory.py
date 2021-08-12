#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.NotSupportYetException import NotSupportYetException
from seata.rm.datasource.undo.mysql.MySQLUndoLogManager import MySQLUndoLogManager
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class UndoLogManagerFactory(object):

    @staticmethod
    def get_undo_log_manager(db_type):
        if db_type == JdbcConstants.MYSQL:
            return MySQLUndoLogManager()
        raise NotSupportYetException("not support db type : [{}]".format(db_type))
