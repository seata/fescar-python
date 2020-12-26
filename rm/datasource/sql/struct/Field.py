#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from rm.datasource.sql.struct.KeyType import KeyType


class Field(object):

    def __init__(self):
        self.name = None
        self.key_type = KeyType.NULL
        self.type = 0
        self.value = None