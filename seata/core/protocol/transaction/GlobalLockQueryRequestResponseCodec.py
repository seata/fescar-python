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
from seata.core.protocol.transaction.AbstractTransactionRequestResponseCodec import AbstractTransactionResponseCodec
from seata.core.util.ClassUtil import ClassUtil


class GlobalLockQueryRequestCodec(object):

    def __init__(self):
        pass

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        xid = ClassUtil.get_attr(t, 'xid')
        branch_type = ClassUtil.get_attr(t, 'branch_type')
        resource_id = ClassUtil.get_attr(t, 'resource_id')
        lock_key = ClassUtil.get_attr(t, 'lock_key')
        application_data = ClassUtil.get_attr(t, 'application_data')

        if xid is not None:
            xid_ba = bytearray(xid.encode(encoding="utf-8"))
            out_buffer.put_int16(len(xid_ba))
            if len(xid_ba) > 0:
                out_buffer.put(xid_ba)
        else:
            out_buffer.put_int16(0)
        out_buffer.put_int8(branch_type.value)
        if resource_id is not None:
            resource_id_ba = bytearray(resource_id.encode(encoding="utf-8"))
            out_buffer.put_int16(len(resource_id_ba))
            if len(resource_id_ba) > 0:
                out_buffer.put(resource_id_ba)
        else:
            out_buffer.put_int16(0)

        if lock_key is not None:
            lock_key_ba = bytearray(lock_key.encode(encoding="utf-8"))
            out_buffer.put_int32(len(lock_key_ba))
            if len(lock_key_ba) > 0:
                out_buffer.put(lock_key_ba)
        else:
            out_buffer.put_int32(0)

        if application_data is not None:
            application_data_ba = bytearray(application_data.encode(encoding="utf-8"))
            out_buffer.put_int32(len(application_data_ba))
            if len(application_data_ba) > 0:
                out_buffer.put(application_data_ba)
        else:
            out_buffer.put_int32(0)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        xid_len = in_buffer.get_int16()
        if xid_len > 0:
            xid_ba = bytearray(xid_len)
            in_buffer.get(xid_ba)
            t.xid = xid_ba.decode(encoding="utf-8")
        t.branch_type = BranchType(in_buffer.get_int8())
        resource_id_len = in_buffer.get_int16()
        if resource_id_len > 0:
            resource_id_ba = bytearray(resource_id_len)
            in_buffer.get(resource_id_ba)
            t.resource_id = resource_id_ba.decode(encoding="utf-8")
        lock_key_len = in_buffer.get_int32()
        if lock_key_len > 0:
            lock_key_ba = bytearray(lock_key_len)
            in_buffer.get(lock_key_ba)
            t.lock_key = lock_key_ba.decode(encoding="utf-8")
        application_data_len = in_buffer.get_int32()
        if application_data_len > 0:
            application_data_ba = bytearray(application_data_len)
            in_buffer.get(application_data_ba)
            t.application_data = application_data_ba.decode(encoding="utf-8")


class GlobalLockQueryResponseCodec(object):

    def __init__(self):
        pass

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        AbstractTransactionResponseCodec.encode(t, out_buffer)
        lockable = t.lockable
        if lockable:
            out_buffer.put_int16(1)
        else:
            out_buffer.put_int16(0)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        AbstractTransactionResponseCodec.decode(t, in_buffer)
        lockable_n = in_buffer.get_int16()
        if lockable_n == 1:
            t.lockable = True
        else:
            t.lockable = False
