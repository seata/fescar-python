#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from exception.NotSupportYetException import NotSupportYetException
from rm.datasource.undo.mysql.MySQLUndoLogManager import MySQLUndoLogManager


class UndoLogManagerFactory(object):

    @staticmethod
    def get_undo_log_manager(db_type):
        if db_type == "mysql":
            return MySQLUndoLogManager()
        raise NotSupportYetException("not support db type : [{}]".format(db_type))