#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class IndexMeta(object):

    def __init__(self):
        self.values = []
        self.non_unique = False
        self.index_qualifier = None
        self.index_name = None
        self.type = 0
        self.index_type = None
        self.asc_or_desc = None
        self.cardinality = 0
        self.ordinal_position = 0
