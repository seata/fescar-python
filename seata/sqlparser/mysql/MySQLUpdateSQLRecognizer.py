#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from am.mysql_base import UpdateStatement

from seata.sqlparser.mysql.MySQLDmlRecognizer import MySQLUpdateRecognizer
from seata.sqlparser.mysql.antlr4.value import MySQLValue
from seata.sqlparser.mysql.antlr4.visit.MySQLUpdateStatement import MySQLUpdateStatement


class MySQLUpdateSQLRecognizer(MySQLUpdateRecognizer):

    def __int__(self, original_sql=None, sql_type=None, stmt=None):
        self.original_sql = original_sql
        self.sql_type = sql_type
        self.stmt = stmt
        self.statement = None

    def init(self):
        if not isinstance(self.stmt, UpdateStatement):
            raise TypeError('stmt type error.' + type(self.stmt).__name__)
        self.statement = MySQLUpdateStatement(self.stmt)

    def get_sql_type(self):
        return self.sql_type

    def get_table_name(self):
        return self.statement.table_name

    def get_table_alias(self):
        return self.statement.table_alias

    def get_original_sql(self):
        return self.original_sql

    def get_update_columns(self):
        items = self.statement.items
        table_alias = self.get_table_alias()
        columns = []
        for item in items:
            if item.owner is not None:
                column = item.owner + item.column
            else:
                if table_alias is not None:
                    column = table_alias + item.column
                else:
                    column = item.column
            columns.append(column)
        return columns

    def get_update_values(self):
        items = self.statement.items
        values = []
        for item in items:
            if isinstance(item.value, MySQLValue.ValueExpr):
                values.append(item.value.get_value())
            elif isinstance(item.value, MySQLValue.OtherValue):
                values.append(item.value.value)
            elif isinstance(item.value, MySQLValue.NotSupportValue):
                raise ValueError('not support value type.' + item.value.origin_type.__name__)
        return values
