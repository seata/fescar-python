#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.mysql.antlr4.gen.MySqlParser import MySqlParser


class MySQLUpdateStatement:

    def __init__(self, ctx: MySqlParser.UpdateStatementContext):
        self.table_name = None
        self.alias = None
        self.items = []
        self.where = None
        self.order_by = None
        self.__ctx = ctx
        self.parse()

    def parse(self):
        self.__parse_table_name()
        self.__parse_items()
        self.__parse_where()
        self.__parse_order_by()

    def __parse_table_name(self):
        sus = self.__ctx.singleUpdateStatement()
        table_name = sus.tableName().getText()
        self.table_name = table_name

    def __parse_items(self):
        sus = self.__ctx.singleUpdateStatement()
        ues = sus.updatedElement()


    def __parse_where(self):
        pass

    def __parse_order_by(self):
        pass