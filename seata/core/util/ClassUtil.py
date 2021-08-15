#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

import enum


class ClassUtil:
    @classmethod
    def obj_to_dic(cls, obj):
        pr = {}
        for name in dir(obj):
            value = getattr(obj, name)
            if not name.startswith('__') and not callable(value):
                # print(str(value) + ":" + str(type(value)))
                if isinstance(value, list) or isinstance(value, set):
                    value_array = []
                    for o in value:
                        value_array.append(cls.obj_to_dic(o))
                    pr[name] = value_array
                elif isinstance(value, float) or \
                        isinstance(value, bool) or \
                        isinstance(value, int) or \
                        isinstance(value, str):
                    pr[name] = value
                elif isinstance(value, enum.Enum):
                    pr[name] = value.value
                else:
                    pr[name] = cls.obj_to_dic(value)
        return pr

    @classmethod
    def dic_to_obj(cls, obj, data):
        obj.__dict__.update(data)
