#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.context.RootContext import RootContext
from core.model.BranchType import BranchType
from rm.datasource.executor.PlainExecutor import PlainExecutor
from rm.datasource.sql.SQLVisitorFactory import SQLVisitorFactory
from rm.datasource.executor.mysql.MySQLInsertExecutor import MySQLInsertExecutor
from rm.datasource.executor.mysql.MySQLDeleteExecutor import MySQLDeleteExecutor
from rm.datasource.executor.mysql.MySQLUpdateExecutor import MySQLUpdateExecutor
from rm.datasource.executor.mysql.MySQLSelectForUpdateExecutor import MySQLSelectForUpdateExecutor
from sqlparser.SQLType import SQLType


class ExecuteTemplate(object):

    @staticmethod
    def execute(cursor_proxy, cursor_callback, args):
        if not RootContext.in_global_transaction() and BranchType.AT != RootContext.get_branch_type():
            return cursor_callback(args)
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
