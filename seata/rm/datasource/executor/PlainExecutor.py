#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


class PlainExecutor(object):

    def __int__(self, cursor_proxy, cursor_callback, sql_recognizer):
        self.cursor_proxy = cursor_proxy
        self.cursor_callback = cursor_callback
        self.sql_recognizer = sql_recognizer

    def execute(self, args):
        self.cursor_callback.execute(self.cursor_proxy.target_cursor, self.cursor_proxy.target_sql, args)
