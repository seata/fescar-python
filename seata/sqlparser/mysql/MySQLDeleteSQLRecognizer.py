#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from am.mysql_base import DeleteStatement

from seata.sqlparser.mysql.MySQLWhereSQLRecognizer import MySQLWhereSQLRecognizer
from seata.sqlparser.mysql.antlr4.visit.MySQLDeleteStatement import MySQLDeleteStatement


class MySQLDeleteSQLRecognizer(MySQLWhereSQLRecognizer):

    def __int__(self, original_sql=None, sql_type=None, stmt=None):
        self.original_sql = original_sql
        self.sql_type = sql_type
        self.stmt = stmt
        self.statement = None

    def init(self):
        if not isinstance(self.stmt, DeleteStatement):
            raise TypeError('stmt type error.' + type(self.stmt).__name__)
        self.statement = MySQLDeleteStatement(self.stmt)

    def get_sql_type(self):
        return self.sql_type

    def get_table_name(self):
        return self.statement.table_name

    def get_table_alias(self):
        return self.statement.table_alias

    def get_original_sql(self):
        return self.original_sql
