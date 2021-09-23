#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.NotSupportYetException import NotSupportYetException
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.sqlparser.SQLType import SQLType
from seata.sqlparser.mysql.MySQLDeleteSQLRecognizer import MySQLDeleteSQLRecognizer
from seata.sqlparser.mysql.MySQLInsertSQLRecognizer import MySQLInsertRecognizer
from seata.sqlparser.mysql.MySQLSelectSQLRecognizer import MySQLSelectSQLRecognizer
from seata.sqlparser.mysql.MySQLUpdateSQLRecognizer import MySQLUpdateSQLRecognizer

from am.mysql_base import MySqlBase, MysqlStatementVisitor, InsertStatement, \
    DeleteStatement, UpdateStatement, SelectStatement
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class SQLVisitorFactory(object):

    @classmethod
    def get(cls, target_sql, db_type):
        if db_type != JdbcConstants.MYSQL:
            raise NotSupportYetException()

        stmts = MySqlBase.parserSQLStatement(target_sql)

        if stmts is None or len(stmts) <= 0:
            raise ShouldNeverHappenException()

        sql_recognizers = cls.get_sql_recognizer(target_sql, stmts)
        if sql_recognizers is None or len(sql_recognizers) <= 0:
            return None

        if len(sql_recognizers) > 1:
            raise NotSupportYetException()

        return sql_recognizers[0]

    @classmethod
    def get_sql_recognizer(cls, target_sql, stmts):
        sql_recognizers = []
        for i in range(len(stmts)):
            dml_stmt = stmts[i]
            if dml_stmt is None:
                continue

            stmt = MysqlStatementVisitor().visit(dml_stmt)

            if isinstance(stmt, InsertStatement):
                sql_recognizer = MySQLInsertRecognizer()
                sql_recognizer.sql_type = SQLType.INSERT
                if stmt.ignore:
                    sql_recognizer.sql_type = SQLType.INSERT_IGNORE
                sql_recognizer.stmt = stmt
                sql_recognizer.original_sql = target_sql
                sql_recognizers.append(sql_recognizer)
            elif isinstance(stmt, DeleteStatement):
                sql_recognizer = MySQLDeleteSQLRecognizer()
                sql_recognizer.sql_type = SQLType.DELETE
                sql_recognizer.stmt = stmt
                sql_recognizer.original_sql = target_sql
                sql_recognizers.append(sql_recognizer)
            elif isinstance(stmt, UpdateStatement):
                sql_recognizer = MySQLUpdateSQLRecognizer()
                sql_recognizer.sql_type = SQLType.UPDATE
                sql_recognizer.stmt = stmt
                sql_recognizer.original_sql = target_sql
                sql_recognizers.append(sql_recognizer)
            elif isinstance(stmt, SelectStatement):
                sql_recognizer = MySQLSelectSQLRecognizer()
                sql_recognizer.sql_type = SQLType.SELECT
                if stmt.lock is not None:
                    sql_recognizer.sql_type = SQLType.SELECT_FOR_UPDATE
                sql_recognizer.stmt = stmt
                sql_recognizer.original_sql = target_sql
                sql_recognizers.append(sql_recognizer)

            sql_recognizer.init()

        return sql_recognizers
