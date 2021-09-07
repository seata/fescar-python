#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


from seata.sqlparser.SQLRecognizer import SQLRecognizer
from seata.sqlparser.mysql.antlr4.parser.mysql_base import MysqlOutputVisitor, UpdateStatement
from seata.sqlparser.mysql.antlr4.value import MySQLValue
from seata.sqlparser.mysql.antlr4.visit.MySQLUpdateStatement import MySQLUpdateStatement


class CustomMysqlOutputVisitor(MysqlOutputVisitor):

    def __init__(self, parameters_map, param_list):
        self.parameters_map = parameters_map
        self.param_list = param_list

    def visitParameterMarker(self, parameter_marker, output):
        param_values = self.parameters_map[parameter_marker.index]
        if self.param_list is None or len(self.param_list) == 0:
            for i in range(len(param_values)):
                self.param_list.append([])
        for i in range(len(param_values)):
            val = param_values[i]
            self.param_list[i].append(val)
        super(CustomMysqlOutputVisitor, self).visitParameterMarker(parameter_marker, output)


class MySQLUpdateSQLRecognizer(SQLRecognizer):

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

    def get_where_condition(self, parameters_map=None, param_list=None):
        where = self.statement.where
        if where is None:
            return ""
        if parameters_map is not None:
            output = list()
            CustomMysqlOutputVisitor(parameters_map, param_list).visitWhere(where, output)
            return ''.join(output)
        else:
            output = list()
            MysqlOutputVisitor().visitWhere(where, output)
            return ''.join(output)

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
