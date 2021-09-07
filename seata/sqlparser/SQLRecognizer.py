#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


class SQLRecognizer(object):

    def get_sql_type(self):
        raise NotImplemented("need subclass implemented")

    def get_table_alias(self):
        raise NotImplemented("need subclass implemented")

    def get_table_name(self):
        raise NotImplemented("need subclass implemented")

    def get_original_sql(self):
        raise NotImplemented("need subclass implemented")

    def get_where_condition(self, parameters_map=None, param_list=None):
        raise NotImplemented("need subclass implemented")
