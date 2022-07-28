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
from seata.core.protocol.AbstractResultMessageCodec import AbstractResultMessageCodec
from seata.exception.TransactionExceptionCode import TransactionExceptionCode


class AbstractTransactionResponseCodec(object):

    @staticmethod
    def encode(t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer class")
        AbstractResultMessageCodec.encode(t, out_buffer)
        transaction_exception_code = t.transaction_exception_code
        out_buffer.put_int8(transaction_exception_code.value)

    @staticmethod
    def decode(t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer class")
        AbstractResultMessageCodec.decode(t, in_buffer)
        tec = in_buffer.get_int8()
        t.transaction_exception_code = TransactionExceptionCode(tec)
