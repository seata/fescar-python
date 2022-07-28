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
