#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.mysql.antlr4.gen.MySqlParser import MySqlParser
from seata.sqlparser.mysql.antlr4.value.MySQLValue import NullValue, StringValue, BoolValue, IntValue, \
    DoubleValue, ParameterMarkerValue
from seata.sqlparser.mysql.antlr4.value.value import OtherLiteralValue


class MySQLStatementUtil:

    @classmethod
    def parse_constant(cls, ctx: MySqlParser.ConstantContext):
        if ctx.NULL_LITERAL() is not None:
            return NullValue()
        elif ctx.stringLiteral() is not None:
            return StringValue(ctx.stringLiteral().getText())
        elif ctx.decimalLiteral() is not None:
            return IntValue(ctx.decimalLiteral().getText())
        elif ctx.REAL_LITERAL() is not None:
            return DoubleValue(ctx.REAL_LITERAL().getText())
        elif ctx.booleanLiteral() is not None:
            return BoolValue(ctx.booleanLiteral().getText())
        elif ctx.parameterMarker() is not None:
            return ParameterMarkerValue(ctx.parameterMarker().getText())
        else:
            return OtherLiteralValue(ctx.getText())
