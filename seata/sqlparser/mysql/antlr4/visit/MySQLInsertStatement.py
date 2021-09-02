#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.mysql.antlr4.gen.MySqlParser import MySqlParser
from seata.sqlparser.mysql.antlr4.util.MySQLStatementUtil import MySQLStatementUtil
from seata.sqlparser.mysql.antlr4.value.MySQLValue import DefaultValue, ParameterMarkerValue, NotSupportValue, FunctionNameValue



class MySQLInsertStatement:

    def __init__(self, ctx: MySqlParser.InsertStatementContext):
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
        self.table_name = self.__ctx.tableName().getText()

    def __parse_columns(self):
        columns = self.__ctx.columns
        if columns is None:
            return
        uids = columns.uid()
        columns_list = []
        for i in range(len(uids)):
            columns_list.append(uids[i].getText())
        self.columns = columns_list

    def __parse_value_list(self):
        ewds = self.__ctx.insertStatementValue().expressionsWithDefaults()
        rows = []
        for i in range(len(ewds)):
            ewd = ewds[i]
            row = []
            eds = ewd.expressionOrDefault()
            for j in range(len(eds)):
                ed = eds[j]
                if ed.DEFAULT() is not None:
                    row.append(DefaultValue(ed.DEFAULT().getText()))
                else:
                    # MySqlParser.ExpressionContext
                    expr = ed.expression()
                    row.append(self.__parse_value_expression(expr))
            rows.append(row)
        self.values_list = rows


    def __parse_value_expression(self, expr):
        if isinstance(expr, MySqlParser.PredicateExpressionContext):
            p = expr.predicate()
            if isinstance(p, MySqlParser.ExpressionAtomPredicateContext):
                ea = p.expressionAtom()
                if isinstance(ea, MySqlParser.ConstantExpressionAtomContext):
                    return MySQLStatementUtil.parse_constant(ea.constant())
                elif isinstance(ea, MySqlParser.FullColumnNameExpressionAtomContext):
                    fcn = ea.fullColumnName()
                    if fcn.uid() is not None:
                        uid = fcn.uid()
                        if uid.simpleId() is not None:
                            si = uid.simpleId()
                            if si.parameterMarker() is not None:
                                return ParameterMarkerValue(si.parameterMarker().getText())
                            elif si.functionNameBase() is not None:
                                return FunctionNameValue(si.functionNameBase().getText(), None)
                            else:
                                # see MySqlParser.SimpleIdContext other
                                return NotSupportValue()
                        else:
                            # MySqlParser.REVERSE_QUOTE_ID
                            # MySqlParser.CHARSET_REVERSE_QOUTE_STRING
                            return NotSupportValue()
                    else:
                        # MySqlParser.DottedIdContext
                        return NotSupportValue()
                elif isinstance(ea, MySqlParser.FunctionCallExpressionAtomContext):
                    fc = ea.functionCall()
                    function_name = fc.getChild(0).getText()
                    args_ = fc.getChild(2).getText()
                    return FunctionNameValue(function_name, args_)
            else:
                # MySqlParser.InPredicateContex
                # MySqlParser.IsNullPredicateContext
                # MySqlParser.BinaryComparisonPredicateContext
                # MySqlParser.SubqueryComparisonPredicateContext
                # MySqlParser.BetweenPredicateContext
                # MySqlParser.SoundsLikePredicateContext
                # MySqlParser.LikePredicateContext
                # MySqlParser.RegexpPredicateContext
                # MySqlParser.JsonMemberOfPredicateContext
                return NotSupportValue()
        else:
            # MySqlParser.NotExpressionContext,
            # MySqlParser.LogicalExpressionContext,
            # MySqlParser.IsExpressionContext
            return NotSupportValue()
