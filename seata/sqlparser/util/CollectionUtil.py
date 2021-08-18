#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class CollectionUtil:

    @classmethod
    def encode_map(cls, map_):
        if map_ is None:
            return None
        if len(map_) == 0:
            return ""
        result = ""
        for k, v in map_.items():
            result += (k + "=" + v + "&")
        return result

    @classmethod
    def decode_map(cls, string):
        if string is None:
            return None
        map_ = {}
        cs = string.split("&")
        for i in range(len(cs)):
            c = cs[i]
            if c.strip() != '':
                kv = c.split("=")
                map_[kv[0]] = kv[1]
        return map_
