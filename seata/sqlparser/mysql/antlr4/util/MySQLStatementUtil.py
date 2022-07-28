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

from am.mysql_base import BitString, RealLiteral, DecimalLiteral, BooleanLiteral, \
    ParameterMarker, StringLiteral, HexadecimalLiteral, NullLiteral
from seata.sqlparser.mysql.antlr4.value import MySQLValue


class MySQLStatementUtil:

    @classmethod
    def parse_constant(cls, val):
        if isinstance(val, BitString):
            return MySQLValue.OtherValue(val.value)
        elif isinstance(val, RealLiteral):
            return MySQLValue.IntValue(val.value)
        elif isinstance(val, DecimalLiteral):
            return MySQLValue.DoubleValue(val.value)
        elif isinstance(val, BooleanLiteral):
            return MySQLValue.BoolValue(val.value)
        elif isinstance(val, ParameterMarker):
            return MySQLValue.ParameterMarkerValue(val.name, val.value)
        elif isinstance(val, StringLiteral):
            return MySQLValue.StringValue(val.value)
        elif isinstance(val, HexadecimalLiteral):
            return MySQLValue.OtherValue(val.value)
        elif isinstance(val, NullLiteral):
            return MySQLValue.NullValue()
