# -*- coding: utf-8 -*-

"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""


import enum


class ClassUtil:
    @classmethod
    def obj_to_dic(cls, obj, ignore_names=[]):
        pr = {}
        for name in dir(obj):
            value = getattr(obj, name)
            if name in ignore_names:
                continue
            if not name.startswith('__') and not callable(value):
                # print(str(value) + ":" + str(type(value)))
                if value is None:
                    pr[name] = value
                elif isinstance(value, list) or isinstance(value, set):
                    value_array = []
                    for o in value:
                        value_array.append(cls.obj_to_dic(o, ignore_names))
                    pr[name] = value_array
                elif isinstance(value, float) or \
                        isinstance(value, bool) or \
                        isinstance(value, int) or \
                        isinstance(value, str):
                    pr[name] = value
                elif isinstance(value, bytes):
                    pr[name] = value
                elif isinstance(value, enum.Enum):
                    pr[name] = value.value
                else:
                    pr[name] = cls.obj_to_dic(value, ignore_names)
        return pr

    @classmethod
    def get_attr(cls, obj, name, default_value=None):
        try:
            return getattr(obj, name)
        except AttributeError:
            if default_value is not None:
                return default_value
            return None

    @classmethod
    def get_simple_name(cls, obj):
        return type(obj).__name__
