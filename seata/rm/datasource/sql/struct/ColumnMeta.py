#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class ColumnMeta(object):

    def __init__(self):
        self.table_cat = None
        self.table_schema_name = None
        self.table_name = None
        self.column_name = None
        self.data_type = None
        self.data_type_name = None
        self.column_size = None
        self.decimal_digits = None
        self.num_prec_radix = None
        self.null_able = None
        self.remarks = None
        self.column_def = None
        self.sql_data_type = None
        self.sql_datetime_sub = None
        self.char_octet_length = None
        self.ordinal_position = None
        self.is_nullable = None
        self.is_autoincrement = None

    def is_auto_increment(self):
        return self.is_autoincrement == "YES"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
