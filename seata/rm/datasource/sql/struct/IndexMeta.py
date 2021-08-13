#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class IndexMeta(object):

    def __init__(self):
        # ColumnMeta list
        self.values = []
        self.non_unique = False
        self.index_qualifier = None
        self.index_name = None
        self.type = 0
        # IndexType
        self.index_type = None
        self.asc_or_desc = None
        self.cardinality = 0
        self.ordinal_position = 0

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
