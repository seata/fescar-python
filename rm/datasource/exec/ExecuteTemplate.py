#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.context.RootContext import RootContext
from core.model.BranchType import BranchType
from rm.datasource.sql.SQLVisitorFactory import SQLVisitorFactory
from rm.datasource.exec.mysql.MySQLInsertExecutor import MySQLInsertExecutor
from sqlparser.SQLType import SQLType


class ExecuteTemplate(object):

    @staticmethod
    def execute(cursor_proxy, cursor_callback, args):
        if not RootContext.in_global_transaction() and BranchType.AT != RootContext.get_branch_type():
            return cursor_callback(args)
        db_type = cursor_proxy.connection.get_db_type()
        sql_recoginzer = SQLVisitorFactory.get(cursor_proxy.target_sql, db_type)
        sql_type = sql_recoginzer.get_sql_type()
        executor = None
        if sql_type == SQLType.INSERT:
            executor = MySQLInsertExecutor(cursor_proxy, cursor_callback, sql_recoginzer)
        elif sql_type == SQLType.UPDATE:
            executor = MySQLInsertExecutor(cursor_proxy, cursor_callback, sql_recoginzer)
        elif sql_type == SQLType.DELETE:
            executor = MySQLInsertExecutor(cursor_proxy, cursor_callback, sql_recoginzer)
        elif sql_type == SQLType.SELECT_FOR_UPDATE:
            executor = MySQLInsertExecutor(cursor_proxy, cursor_callback, sql_recoginzer)
        else:
            return cursor_callback(args)

        return executor.execute(args)
