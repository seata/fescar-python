#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class SQLUndoLog(object):
    def __int__(self):
        # SQLType
        self.sql_type = None
        self.table_name = None
        # TableRecords
        self.before_image = None
        self.after_image = None

    def set_table_meta(self, table_meta):
        if self.before_image is not None:
            self.before_image.set_table_meta(table_meta)
        if self.after_image is not None:
            self.after_image.set_table_meta(table_meta)
