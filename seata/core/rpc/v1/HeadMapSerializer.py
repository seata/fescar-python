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



class HeadMapSerializer(object):

    def __init__(self):
        pass

    def encode(self, head_map, bytebuffer):
        head_map_length = 0
        if len(head_map) > 0:
            for k in head_map:
                head_map_length += self._write_string(bytebuffer, k)
                head_map_length += self._write_string(bytebuffer, head_map[k])
        return head_map_length

    def decode(self, bytebuffer, head_map_length):
        head_map = dict()
        if bytebuffer is None or bytebuffer.readable_bytes() == 0 or head_map_length == 0:
            return head_map
        start = bytebuffer.read_index()
        while bytebuffer.read_index() - start < head_map_length:
            key = self._read_string(bytebuffer)
            value = self._read_string(bytebuffer)
            head_map[key] = value
        return head_map

    def _write_string(self, bytebuffer, v):
        if v is None:
            bytebuffer.put_int16(-1)
            return 2
        elif len(v) == 0:
            bytebuffer.put_int16(0)
            return 2
        else:
            v_len = len(v)
            v_bb = bytearray(v.encode(encoding="utf-8"))
            bytebuffer.put_int16(v_len)
            bytebuffer.put(v_bb)
            return 2 + len(v_bb)

    def _read_string(self, bytebuffer):
        length = bytebuffer.get_int16()
        if length < 0:
            return None
        elif length == 0:
            return ""
        else:
            value = bytearray(length)
            bytebuffer.get(value)
            return value.decode(encoding="utf-8")


