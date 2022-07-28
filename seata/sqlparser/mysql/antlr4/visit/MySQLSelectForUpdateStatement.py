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

from am.mysql_base import SelectStatement


class MySQLSelectForUpdateStatement:

    def __init__(self, ctx: SelectStatement):
        if not isinstance(ctx, SelectStatement):
            raise TypeError('ctx type error.' + type(ctx).__name__)
        self.select_elements = None
        self.table_name = None
        self.table_alias = None
        self.where = None
        self.order_by = None
        self.limit = None
        self.lock = None
        self.__ctx = ctx
        self.__parse()

    def __parse(self):
        self.__parse_select_elements()
        self.__parse_table_name()
        self.__parse_table_alias()
        self.__parse_where()
        self.__parse_order_by()
        self.__parse_limit()
        self.__parse_lock()

    def __parse_select_elements(self):
        self.select_elements = self.__ctx.selectElements

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

    def __parse_lock(self):
        self.lock = self.__ctx.lock
