#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.ByteBuffer import ByteBuffer
from seata.core.model.GlobalStatus import GlobalStatus
from seata.core.protocol.transaction.AbstractTransactionRequestResponseCodec import AbstractTransactionResponseCodec


class AbstractGlobalEndRequestCodec(object):

    @staticmethod
    def encode(t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        xid = t.xid
        extra_data = None
        try:
            extra_data = getattr(t, 'extra_data')
        except AttributeError:
            pass
        if xid is not None:
            xid_ba = bytearray(xid.encode(encoding="utf-8"))
            out_buffer.put_int16(len(xid_ba))
            if len(xid_ba) > 0:
                out_buffer.put(xid_ba)
        else:
            out_buffer.put_int16(0)
        if extra_data is not None:
            extra_data_ba = bytearray(extra_data.encode(encoding="utf-8"))
            out_buffer.put_int16(len(extra_data_ba))
            if len(extra_data_ba) > 0:
                out_buffer.put(extra_data_ba)
        else:
            out_buffer.put_int16(0)

    @staticmethod
    def decode(t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        xid_len = in_buffer.get_int16()
        if xid_len > 0:
            xid_ba = bytearray(xid_len)
            in_buffer.get(xid_ba)
            t.xid = xid_ba.decode(encoding="utf-8")
        extra_data_len = in_buffer.get_int16()
        if xid_len > 0:
            extra_data_ba = bytearray(extra_data_len)
            in_buffer.get(extra_data_ba)
            t.extra_data = extra_data_ba.decode(encoding="utf-8")


class AbstractGlobalEndResponseCodec(object):

    @staticmethod
    def encode(t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        AbstractTransactionResponseCodec.encode(t, out_buffer)
        global_status = t.global_status
        out_buffer.put_int8(global_status.value[0])

    @staticmethod
    def decode(t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        AbstractTransactionResponseCodec.decode(t, in_buffer)
        gs = in_buffer.get_int8()
        t.global_status = GlobalStatus(gs)
