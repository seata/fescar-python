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
from seata.core.model.GlobalStatus import GlobalStatus
from seata.core.protocol.transaction.AbstractGlobalEndRequestResponseCodec import AbstractGlobalEndRequestCodec, \
    AbstractGlobalEndResponseCodec


class GlobalReportRequestCodec(object):

    def __init__(self):
        pass

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        AbstractGlobalEndRequestCodec.encode(t, out_buffer)
        global_status = t.global_status
        if global_status is not None:
            out_buffer.put_int8(global_status.value[0])
        else:
            out_buffer.put_int8(-1)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        AbstractGlobalEndRequestCodec.decode(t, in_buffer)
        global_status = in_buffer.get_int8()
        if global_status > -1:
            t.global_status = GlobalStatus(global_status)


class GlobalReportResponseCodec(object):

    def __init__(self):
        pass

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        AbstractGlobalEndResponseCodec.encode(t, out_buffer)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        AbstractGlobalEndResponseCodec.decode(t, in_buffer)
