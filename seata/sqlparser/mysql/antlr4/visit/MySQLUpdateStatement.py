#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.mysql.antlr4.gen.MySqlParser import MySqlParser
from seata.sqlparser.mysql.antlr4.util.MySQLStatementUtil import MySQLStatementUtil


class UpdateSetItem(object):
    def __init__(self, column=None, value=None):
        self.column = column
        self.value = value


class MySQLUpdateStatement:

    def __init__(self, ctx: MySqlParser.UpdateStatementContext):
        self.table_name = None
        self.table_alias = None
        self.items = []
        self.where = None
        self.order_by = None
        self.limit = None
        self.__ctx = ctx
        self.parse()

    def parse(self):
        self.__parse_table_name()
        self.__parse_table_alias()
        self.__parse_items()
        self.__parse_where()
        self.__parse_order_by()

    def __parse_table_alias(self):
        sus = self.__ctx.singleUpdateStatement()
        if sus.uid() is not None:
            self.table_alias = sus.uid().getText()

    def __parse_table_name(self):
        sus = self.__ctx.singleUpdateStatement()
        table_name = sus.tableName().getText()
        self.table_name = table_name

    def __parse_items(self):
        sus = self.__ctx.singleUpdateStatement()
        ues = sus.updatedElement()
        for i in range(len(ues)):
            ue = ues[i]
            # like t.id or id
            column = ue.fullColumnName().getText()
            # TODO ignore value
            value = None
            self.items.append(UpdateSetItem(column, value))

    def __parse_where(self):
        sus = self.__ctx.singleUpdateStatement()
        where = sus.expression()
        if isinstance(where, MySqlParser.NotExpressionContext):
            pass
        elif isinstance(where, MySqlParser.LogicalExpressionContext):
            pass
        elif isinstance(where, MySqlParser.IsExpressionContext):
            pass
        elif isinstance(where, MySqlParser.PredicateExpressionContext):
            pc = where.predicate()

            pass

    def __parse_order_by(self):
        sus = self.__ctx.singleUpdateStatement()
        self.order_by = sus.orderByClause()
    
    def __parse_limit(self):
        sus = self.__ctx.singleUpdateStatement()
        self.limit = sus.limitClause()
