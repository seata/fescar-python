#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
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
