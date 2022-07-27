# -*- coding: utf-8 -*-

"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from am.mysql_base import InsertStatement, Constant, FunctionCall

from seata.sqlparser.mysql.antlr4.util.MySQLStatementUtil import MySQLStatementUtil
from seata.sqlparser.mysql.antlr4.value import MySQLValue


class MySQLInsertStatement:

    def __init__(self, ctx: InsertStatement):
        self.table_name = None
        self.table_alias = None
        self.columns = None
        self.values_list = []
        self.__ctx = ctx
        self.parse()

    def parse(self):
        self.__parse_table_name()
        self.__parse_columns()
        self.__parse_value_list()

    def __parse_table_name(self):
        self.table_name = self.__ctx.tableSource.tableName

    def __parse_columns(self):
        columns = self.__ctx.columns
        if columns is None:
            return
        columns_list = []
        for i in range(len(columns)):
            columns_list.append(columns[i])
        self.columns = columns_list

    def __parse_value_list(self):
        values = self.__ctx.value_list
        rows = []
        for i in range(len(values)):
            vals = values[i]
            row = []
            for j in range(len(vals)):
                val = vals[j]
                if isinstance(val, Constant):
                    row.append(MySQLStatementUtil.parse_constant(val))
                elif isinstance(val, FunctionCall):
                    row.append(MySQLValue.FunctionNameValue(val.function_name, val.args_list))
                else:
                    row.append(MySQLValue.NotSupportValue(type(val)))
            rows.append(row)
        self.values_list = rows
