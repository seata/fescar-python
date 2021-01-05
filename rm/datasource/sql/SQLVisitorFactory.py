#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from exception.NotSupportYetException import NotSupportYetException
from exception.ShouldNeverHappenException import ShouldNeverHappenException
from sqlparser.SQLType import SQLType
from sqlparser.mysql.MySQLDeleteSQLRecognizer import MySQLDeleteSQLRecognizer
from sqlparser.mysql.MySQLInsertSQLRecognizer import MySQLInsertSQLRecognizer
from sqlparser.mysql.MySQLSelectSQLRecognizer import MySQLSelectSQLRecognizer
from sqlparser.mysql.MySQLUpdateSQLRecognizer import MySQLUpdateSQLRecognizer
from sqlparser.util.JdbcConstants import JdbcConstants
import sqlparse


class SQLVisitorFactory(object):

    @classmethod
    def get(cls, target_sql, db_type):
        if db_type != JdbcConstants.MYSQL:
            raise NotSupportYetException()

        parsed = sqlparse.parse(target_sql)
        if parsed is None or len(parsed) <= 0:
            raise ShouldNeverHappenException()

        sql_recognizers = cls.get_sql_recognizer(target_sql, parsed)
        if sql_recognizers is None or len(sql_recognizers) <= 0:
            return None
        else:
            return sql_recognizers[0]

    @classmethod
    def get_sql_recognizer(cls, target_sql, parsed):
        p = parsed[0]
        token_list = p.tokens
        kw = None
        for i in range(len(token_list)):
            token = token_list[i]
            if token.is_keyword:
                kw = token
                break

        if kw is None:
            raise ShouldNeverHappenException()

        sql_recognizers = []

        if kw.normalized == "INSERT":
            sql_type = SQLType.INSERT
            for i in range(len(token_list)):
                token = token_list[i]
                if token.is_keyword and token.normalized == "IGNORE":
                    sql_type = SQLType.INSERT_IGNORE
                    break
            sql_recognizer = MySQLInsertSQLRecognizer()
            sql_recognizer.sql_type = sql_type
            sql_recognizer.tokens = token_list
            sql_recognizer.original_sql = target_sql
            sql_recognizers.append(sql_recognizer)
        elif kw.normalized == "DELETE":
            sql_recognizer = MySQLDeleteSQLRecognizer()
            sql_recognizer.sql_type = SQLType.DELETE
            sql_recognizer.tokens = token_list
            sql_recognizer.original_sql = target_sql
            sql_recognizers.append(sql_recognizer)
        elif kw.normalized == "UPDATE":
            sql_recognizer = MySQLUpdateSQLRecognizer()
            sql_recognizer.sql_type = SQLType.UPDATE
            sql_recognizer.tokens = token_list
            sql_recognizer.original_sql = target_sql
            sql_recognizers.append(sql_recognizer)
        elif kw.normalized == "SELECT":
            sql_type = SQLType.SELECT
            for i in range(len(token_list)):
                token = token_list[i]
                if token.is_keyword and token.normalized == "FOR":
                    sql_type = SQLType.SELECT_FOR_UPDATE
                    break
            sql_recognizer = MySQLSelectSQLRecognizer()
            sql_recognizer.sql_type = sql_type
            sql_recognizer.tokens = token_list
            sql_recognizer.original_sql = target_sql
            sql_recognizers.append(sql_recognizer)

        return sql_recognizers
