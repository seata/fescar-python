#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from am.mysql_base import DeleteStatement


class MySQLDeleteStatement:

    def __init__(self, ctx: DeleteStatement):
        self.table_name = None
        self.table_alias = None
        self.where = None
        self.order_by = None
        self.limit = None
        self.__ctx = ctx
        self.__parse()

    def __parse(self):
        self.__parse_table_name()
        self.__parse_table_alias()
        self.__parse_where()
        self.__parse_order_by()
        self.__parse_limit()

    def __parse_table_name(self):
        self.table_name = self.__ctx.tableSource.tableName

    def __parse_table_alias(self):
        self.table_alias = self.__ctx.tableSource.tableAlias

    def __parse_where(self):
        self.where = self.__ctx.where

    def __parse_order_by(self):
        self.order_by = self.__ctx.orderBy

    def __parse_limit(self):
        self.limit = self.__ctx.limit
