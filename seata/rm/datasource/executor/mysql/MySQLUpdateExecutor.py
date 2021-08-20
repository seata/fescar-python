#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


class MySQLUpdateExecutor(object):

    def __int__(self, cursor_proxy, cursor_callback, sql_recognizer):
        self.cursor_proxy = cursor_proxy
        self.cursor_callback = cursor_callback
        self.sql_recognizer = sql_recognizer

    def before_image(self):
        raise NotImplemented()

    def after_image(self, before_image):
        raise NotImplemented()

    def execute(self, args):
        raise NotImplemented()

    def get_table_meta(self):
        raise NotImplemented()