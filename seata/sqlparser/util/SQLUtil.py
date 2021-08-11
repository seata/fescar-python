#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class SQLUtil:

    __quote = "[]`'\""

    @classmethod
    def remove_quota(cls, value):
        for i in range(len(cls.__quote)):
            value = value.replace(cls.__quote[i], "")
        return value
