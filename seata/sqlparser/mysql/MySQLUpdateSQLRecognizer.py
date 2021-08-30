#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


from seata.sqlparser.SQLRecognizer import SQLRecognizer
from seata.sqlparser.mysql.antlr4.visit.MySQLUpdateStatement import MySQLUpdateStatement


class MySQLUpdateSQLRecognizer(SQLRecognizer):

    def __int__(self, original_sql=None, sql_type=None, stmt=None):
        self.original_sql = original_sql
        self.sql_type = sql_type
        self.dml_stmt = stmt
        self.statement = None

    def init(self):
        self.statement = MySQLUpdateStatement(self.dml_stmt.updateStatement())

    def get_sql_type(self):
        return self.sql_type

    def get_table_name(self):
        # TODO
        pass

    def get_table_alias(self):
        # TODO
        pass

    def get_original_sql(self):
        # TODO
        pass

    def get_where_condition(self, parameters_map, param_list):
        pass

    def get_update_columns(self):
        pass

    def get_update_values(self):
        pass