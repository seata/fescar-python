#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
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
