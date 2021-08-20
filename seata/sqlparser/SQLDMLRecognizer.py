#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.NeedSubclassImplemented import NeedSubclassImplemented
from seata.sqlparser.SQLRecognizer import SQLRecognizer


class SQLInsertRecognizer(SQLRecognizer):

    def insert_columns_is_empty(self):
        raise NeedSubclassImplemented()

    def get_insert_columns(self):
        raise NeedSubclassImplemented()

    def get_insert_rows(self, pk_index: list):
        raise NeedSubclassImplemented()


class SQLUpdateRecognizer(SQLRecognizer):

    def get_update_columns(self):
        raise NeedSubclassImplemented()

    def get_update_values(self):
        raise NeedSubclassImplemented()
