#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
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
