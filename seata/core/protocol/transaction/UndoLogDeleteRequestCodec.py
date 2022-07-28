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

from seata.core.ByteBuffer import ByteBuffer
from seata.core.model.BranchType import BranchType
from seata.core.util.ClassUtil import ClassUtil


class UndoLogDeleteRequestCodec(object):

    def __init__(self):
        pass

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        save_days = ClassUtil.get_attr(t, 'save_days')
        branch_type = ClassUtil.get_attr(t, 'branch_type')
        resource_id = ClassUtil.get_attr(t, 'resource_id')
        out_buffer.put_int8(branch_type.value)
        if resource_id is not None:
            resource_id_ba = bytearray(resource_id.encode(encoding="utf-8"))
            out_buffer.put_int16(len(resource_id_ba))
            if len(resource_id_ba) > 0:
                out_buffer.put(resource_id_ba)
        else:
            out_buffer.put_int16(0)
        out_buffer.put_int16(save_days)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        if in_buffer.readable_bytes() < 1:
            return
        t.branch_type = BranchType(in_buffer.get_int8())
        if in_buffer.readable_bytes() < 2:
            return
        resource_id_len = in_buffer.get_int16()
        if resource_id_len <= 0 or in_buffer.readable_bytes() < resource_id_len:
            return
        resource_id_ba = bytearray(resource_id_len)
        in_buffer.get(resource_id_ba)
        t.resource_id = resource_id_ba.decode(encoding="utf-8")
        if in_buffer.readable_bytes() < 2:
            return
        t.save_days = in_buffer.get_int16()
