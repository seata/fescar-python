#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from seata.exception import NotSupportYetException
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.sqlparser.SQLType import SQLType
from seata.sqlparser.mysql.MySQLDeleteSQLRecognizer import MySQLDeleteSQLRecognizer
from seata.sqlparser.mysql.MySQLInsertSQLRecognizer import MySQLInsertRecognizer
from seata.sqlparser.mysql.MySQLSelectSQLRecognizer import MySQLSelectSQLRecognizer
from seata.sqlparser.mysql.MySQLUpdateSQLRecognizer import MySQLUpdateSQLRecognizer
from seata.sqlparser.mysql.antlr4.gen.MySqlLexer import MySqlLexer, CommonTokenStream
from seata.sqlparser.mysql.antlr4.gen.MySqlParser import MySqlParser
from seata.sqlparser.mysql.antlr4.stream.NoCaseStringStream import NoCaseStringStream
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class SQLVisitorFactory(object):

    @classmethod
    def get(cls, target_sql, db_type):
        if db_type != JdbcConstants.MYSQL:
            raise NotSupportYetException()

        lexer = MySqlLexer(NoCaseStringStream(target_sql))
        stream = CommonTokenStream(lexer)
        parser = MySqlParser(stream)
        stmts = parser.sqlStatements().sqlStatement()

        if stmts is None or len(stmts) <= 0:
            raise ShouldNeverHappenException()

        sql_recognizers = cls.get_sql_recognizer(target_sql, stmts)
        if sql_recognizers is None or len(sql_recognizers) <= 0:
            return None
        else:
            return sql_recognizers[0]

    @classmethod
    def get_sql_recognizer(cls, target_sql, stmts):
        sql_recognizers = []
        for i in range(len(stmts)):
            dml_stmt = stmts[i].dmlStatement()
            if dml_stmt.insertStatement() is not None:
                sql_recognizer = MySQLInsertRecognizer()
                sql_recognizer.sql_type = SQLType.INSERT
                if dml_stmt.insertStatement().IGNORE() is not None:
                    sql_recognizer.sql_type = SQLType.INSERT_IGNORE
                if dml_stmt.insertStatement().DUPLICATE() is not None:
                    sql_recognizer.sql_type = SQLType.INSERT_ON_DUPLICATE_UPDATE
                sql_recognizer.stmt = dml_stmt
                sql_recognizer.original_sql = target_sql
                sql_recognizer.init()
                sql_recognizers.append(sql_recognizer)
            elif dml_stmt.deleteStatement() is not None:
                sql_recognizer = MySQLDeleteSQLRecognizer()
                sql_recognizer.sql_type = SQLType.DELETE
                sql_recognizer.stmt = dml_stmt
                sql_recognizer.original_sql = target_sql
                sql_recognizer.init()
                sql_recognizers.append(sql_recognizer)
            elif dml_stmt.updateStatement() is not None:
                sql_recognizer = MySQLUpdateSQLRecognizer()
                sql_recognizer.sql_type = SQLType.UPDATE
                sql_recognizer.stmt = dml_stmt
                sql_recognizer.original_sql = target_sql
                sql_recognizer.init()
                sql_recognizers.append(sql_recognizer)
            elif dml_stmt.selectStatement() is not None:
                sql_recognizer = MySQLSelectSQLRecognizer()
                sql_recognizer.sql_type = SQLType.SELECT
                if dml_stmt.selectStatement().lockClause() is not None:
                    sql_recognizer.sql_type = SQLType.SELECT_FOR_UPDATE
                sql_recognizer.stmt = dml_stmt
                sql_recognizer.original_sql = target_sql
                sql_recognizer.init()
                sql_recognizers.append(sql_recognizer)

        return sql_recognizers
