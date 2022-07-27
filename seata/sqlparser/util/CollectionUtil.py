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
