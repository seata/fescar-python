#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.context.RootContext import RootContext
from seata.core.model.BranchType import BranchType
from seata.rm.datasource.executor.PlainExecutor import PlainExecutor
from seata.rm.datasource.sql.SQLVisitorFactory import SQLVisitorFactory
from seata.rm.datasource.executor.mysql.MySQLInsertExecutor import MySQLInsertExecutor
from seata.rm.datasource.executor.mysql.MySQLDeleteExecutor import MySQLDeleteExecutor
from seata.rm.datasource.executor.mysql.MySQLUpdateExecutor import MySQLUpdateExecutor
from seata.rm.datasource.executor.mysql.MySQLSelectForUpdateExecutor import MySQLSelectForUpdateExecutor
from seata.sqlparser.SQLType import SQLType


class ExecuteTemplate(object):

    @staticmethod
    def execute(cursor_proxy, cursor_callback, args):
        if not RootContext.in_global_transaction() and BranchType.AT != RootContext.get_branch_type():
            return cursor_callback.execute(cursor_proxy.target_cursor, cursor_proxy.target_sql, args)
        db_type = cursor_proxy.connection.get_db_type()
        sql_recognizer = SQLVisitorFactory.get(cursor_proxy.target_sql, db_type)
        executor = None
        if sql_recognizer is not None:
            sql_type = sql_recognizer.get_sql_type()
            if sql_type == SQLType.INSERT:
                executor = MySQLInsertExecutor(cursor_proxy, cursor_callback, sql_recognizer)
            elif sql_type == SQLType.UPDATE:
                executor = MySQLUpdateExecutor(cursor_proxy, cursor_callback, sql_recognizer)
            elif sql_type == SQLType.DELETE:
                executor = MySQLDeleteExecutor(cursor_proxy, cursor_callback, sql_recognizer)
            elif sql_type == SQLType.SELECT_FOR_UPDATE:
                executor = MySQLSelectForUpdateExecutor(cursor_proxy, cursor_callback, sql_recognizer)
            else:
                executor = PlainExecutor(cursor_proxy, cursor_callback, sql_recognizer)
        else:
            executor = PlainExecutor(cursor_proxy, cursor_callback, sql_recognizer)

        return executor.execute(args)
