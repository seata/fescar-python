#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.ByteBuffer import ByteBuffer
from seata.core.protocol.transaction.AbstractTransactionRequestResponseCodec import AbstractTransactionResponseCodec
from seata.core.util.ClassUtil import ClassUtil


class GlobalBeginRequestCodec(object):

    def __init__(self):
        pass

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        timeout = ClassUtil.get_attr(t, 'timeout')
        transaction_name = ClassUtil.get_attr(t, 'transaction_name')
        out_buffer.put_int32(timeout)
        if transaction_name is not None:
            transaction_name_ba = bytearray(transaction_name.encode(encoding="utf-8"))
            out_buffer.put_int16(len(transaction_name_ba))
            if len(transaction_name_ba) > 0:
                out_buffer.put(transaction_name_ba)
        else:
            out_buffer.put_int16(0)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        t.timeout = in_buffer.get_int32()
        transaction_name_len = in_buffer.getint16()
        if transaction_name_len > 0:
            transaction_name_ba = bytearray(transaction_name_len)
            in_buffer.get(transaction_name_ba)
            t.transaction_name = transaction_name_ba.decode(encoding="utf-8")


class GlobalBeginResponseCodec(object):

    def __init__(self):
        pass

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        AbstractTransactionResponseCodec.encode(t, out_buffer)
        xid = ClassUtil.get_attr(t, 'xid')
        extra_data = ClassUtil.get_attr(t, 'extra_data')
        if xid is not None:
            xid_ba = bytearray(xid.encode(encoding="utf-8"))
            out_buffer.put_int16(len(xid_ba))
            if len(xid_ba) > 0:
                out_buffer.put(xid_ba)
        else:
            out_buffer.put_int16(0)
        if extra_data is not None:
            extra_data_ba = bytearray(extra_data)
            out_buffer.put_int16(len(extra_data_ba))
            if len(extra_data_ba) > 0:
                out_buffer.put(extra_data_ba)
        else:
            out_buffer.put_int16(0)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        AbstractTransactionResponseCodec.decode(t, in_buffer)
        xid_len = in_buffer.get_int16()
        if xid_len > 0:
            xid_ba = bytearray(xid_len)
            in_buffer.get(xid_ba)
            t.xid = xid_ba.decode(encoding="utf-8")
        extra_data_len = in_buffer.get_int16()
        if extra_data_len > 0:
            extra_data_ba = bytearray(extra_data_len)
            in_buffer.get(extra_data_ba)
            t.extra_data = extra_data_ba.decode(encoding="utf-8")
