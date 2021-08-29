#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.SQLRecognizer import SQLRecognizer


class SQLInsertRecognizer(SQLRecognizer):

    def insert_columns_is_empty(self):
        raise NotImplemented("need subclass implemented")

    def get_insert_columns(self):
        raise NotImplemented("need subclass implemented")

    def get_insert_rows(self, pk_index: list):
        raise NotImplemented("need subclass implemented")


class SQLUpdateRecognizer(SQLRecognizer):

    def get_update_columns(self):
        raise NotImplemented("need subclass implemented")

    def get_update_values(self):
        raise NotImplemented("need subclass implemented")
