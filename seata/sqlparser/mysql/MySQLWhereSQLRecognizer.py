#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from am.mysql_base import MysqlOutputVisitor

from seata.sqlparser.SQLRecognizer import SQLRecognizer
from seata.sqlparser.mysql.antlr4.util.ParamMysqlOutputVisitor import ParamMysqlOutputVisitor


class MySQLWhereSQLRecognizer(SQLRecognizer):

    def get_where_condition(self, parameters_map=None, param_list=None):
        where = self.statement.where
        if where is None:
            return ""
        if parameters_map is not None:
            output = list()
            ParamMysqlOutputVisitor(parameters_map, param_list).visitWhere(where, output)
            return ''.join(output)
        else:
            output = list()
            MysqlOutputVisitor().visitWhere(where, output)
            return ''.join(output)
