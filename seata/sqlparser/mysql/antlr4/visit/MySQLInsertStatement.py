#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.mysql.antlr4.MySqlParser import MySqlParser
from seata.sqlparser.mysql.antlr4.value.MySQLValue import DefaultValue, InsertNotSupportValue


class MySQLInsertStatement:

    def __init__(self, ctx: MySqlParser.InsertStatementContext):
        self.table_name = None
        self.insert_columns = []
        self.insert_rows = []
        self.__ctx = ctx
        self.parse()

    def parse(self):
        self.__parse_table_name()
        self.__parse_insert_columns()
        self.__parse_insert_rows()

    def __parse_table_name(self):
        self.table_name = self.__ctx.tableName().getText()

    def __parse_insert_columns(self):
        columns = self.__ctx.columns
        if columns is None:
            return None
        uids = columns.uid()
        columns_list = []
        for i in range(len(uids)):
            columns_list.append(uids[i].getText())
        self.insert_columns = columns_list

    def __parse_insert_rows(self):
        ewds = self.__ctx.insertStatementValue().expressionsWithDefaults()
        rows = []
        for i in range(len(ewds)):
            ewd = ewds[i]
            row = []
            eds = ewd.expressionOrDefault()
            for j in range(len(eds)):
                ed = eds[i]
                expr = ed.expression()
                if expr.DEFAULT() is not None:
                    row.append(DefaultValue(expr.DEFAULT().getText()))
                elif isinstance(expr, MySqlParser.NotExpressionContext) or \
                        isinstance(expr, MySqlParser.LogicalExpressionContext) or \
                        isinstance(expr, MySqlParser.IsExpressionContext):
                    row.append(InsertNotSupportValue())
                elif isinstance(expr, MySqlParser.PredicateExpressionContext):
                    p = expr.predicate()
                    if isinstance(p, MySqlParser.InPredicateContext) or \
                            isinstance(p, MySqlParser.IsNullPredicateContext) or \
                            isinstance(p, MySqlParser.BinaryComparisonPredicateContext) or \
                            isinstance(p, MySqlParser.SubqueryComparisonPredicateContext) or \
                            isinstance(p, MySqlParser.BetweenPredicateContext) or \
                            isinstance(p, MySqlParser.SoundsLikePredicateContext) or \
                            isinstance(p, MySqlParser.LikePredicateContext) or \
                            isinstance(p, MySqlParser.RegexpPredicateContext) or \
                            isinstance(p, MySqlParser.JsonMemberOfPredicateContext):
                        row.append(InsertNotSupportValue())
                    else:
                        ea = p.expressionAtom()
                        if isinstance(ea, MySqlParser.ConstantExpressionAtomContext):
                            row.append(ea.getText())
                        elif isinstance(ea, MySqlParser.FullColumnNameExpressionAtomContext):
                            fcn = ea.fullColumnName()
                            if fcn.uid() is not None:
                                uid = fcn.uid()
                                if uid.simpleId() is not None:
                                    si = uid.simpleId()
                                    if isinstance(si, MySqlParser.ParameterMarkerContext):
                                        row.append(si.QUESTION_().getText())
                                    elif isinstance(si, MySqlParser.FunctionNameBaseContext):
                                        row.append(si.getText())
                                    else:
                                        row.append(InsertNotSupportValue())
                                elif isinstance(uid, MySqlParser.REVERSE_QUOTE_ID) or \
                                        isinstance(uid, MySqlParser.CHARSET_REVERSE_QOUTE_STRING):
                                    row.append(InsertNotSupportValue())
                        elif isinstance(ea, MySqlParser.FunctionCallContext):
                            print('TODO')

        self.insert_rows = rows
