#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.SQLRecognizer import SQLRecognizer


class MySQLSelectSQLRecognizer(SQLRecognizer):

    def __int__(self, original_sql=None, sql_type=None, tokens=None):
        self.original_sql = original_sql
        self.sql_type = sql_type
        self.tokens = tokens

    def get_sql_type(self):
        return self.sql_type

    def get_table_name(self):
        pass

    def get_table_alias(self):
        pass

    def get_original_sql(self):
        pass
