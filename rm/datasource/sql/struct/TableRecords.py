#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from exception.ShouldNeverHappenException import ShouldNeverHappenException


class TableRecords(object):

    def __init__(self):
        self.table_meta = None
        self.table_name = None
        self.rows = []

    def __init__(self, table_meta):
        self.table_meta = table_meta

    def set_table_meta(self, table_meta):
        if self.table_meta is not None:
            raise ShouldNeverHappenException("table meta is not null")
        self.table_meta = table_meta
        self.table_name = table_meta.table_name
