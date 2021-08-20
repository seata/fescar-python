#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class UndoExecutorHolderFactory:
    _HOLDER_MAP = {}

    @classmethod
    def get_undo_executor_holder(cls, db_type):
        if cls._HOLDER_MAP.get(db_type, None) is not None:
            return cls._HOLDER_MAP[db_type]
        if db_type == JdbcConstants.MYSQL:
            from seata.rm.datasource.undo.mysql.MySQLUndoExecutorHolder import MySQLUndoExecutorHolder
            cls._HOLDER_MAP[db_type] = MySQLUndoExecutorHolder()
            return cls._HOLDER_MAP[db_type]
        raise NotImplemented("db type : " + db_type)
