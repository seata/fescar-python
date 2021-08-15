#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


class CursorCallback:

    def __init__(self, func_name):
        self.func_name = func_name

    def execute(self, target, sql, parameters):
        """
        :param target: cursor
        :param sql: sql
        :param parameters: parameters
        :return:
        """
        return getattr(target, self.func_name)(sql, parameters)
