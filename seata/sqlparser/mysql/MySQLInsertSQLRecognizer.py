#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import sql_metadata

from seata.sqlparser.SQLRecognizer import SQLRecognizer


class MySQLInsertSQLRecognizer(SQLRecognizer):

    def __int__(self, original_sql=None, sql_type=None, tokens=None):
        self.original_sql = original_sql
        self.sql_type = sql_type
        self.tokens = tokens

    def get_sql_type(self):
        return self.sql_type

    def get_table_name(self):
        return sql_metadata.get_query_tables(self.original_sql)[0]

    def get_table_alias(self):
        aliases = sql_metadata.get_query_table_aliases(self.original_sql)
        if aliases is None or len(aliases) <= 0:
            return None
        return next(iter(aliases))[0]

    def get_original_sql(self):
        return self.original_sql
