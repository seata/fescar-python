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
from seata.core.Number import Number
from seata.core.protocol.ResultCode import ResultCode


class AbstractResultMessageCodec(object):

    @staticmethod
    def encode(t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer class")
        result_code = t.result_code
        result_msg = t.msg
        out_buffer.put_int8(result_code.value)
        if result_code == ResultCode.Failed:
            if result_msg is not None and len(result_msg) > 0:
                if len(result_msg) > Number.SHORT_MAX_VALUE:
                    msg = result_msg[0:Number.SHORT_MAX_VALUE]
                else:
                    msg = result_msg
                msg_ba = bytearray(msg.encode(encoding="utf-8"))
                out_buffer.put_int16(len(msg_ba))
                out_buffer.put(msg_ba)
            else:
                out_buffer.put_int16(0)

    @staticmethod
    def decode(t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer class")
        result_code = ResultCode(in_buffer.get_int8())
        t.result_code = result_code
        if result_code == ResultCode.Failed:
            msg_len = in_buffer.get_int16()
            if msg_len > 0:
                msg = bytearray(msg_len)
                in_buffer.get(msg)
                t.msg = msg.decode(encoding="utf-8")
