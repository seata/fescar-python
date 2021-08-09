#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.ByteBuffer import ByteBuffer
from seata.core.protocol.AbstractIdentifyRequestResponseCodec import AbstractIdentifyRequestCodec, \
    AbstractIdentifyResponseCodec


class RegisterRMRequestCodec(object):

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer class")
        AbstractIdentifyRequestCodec.encode(t, out_buffer)
        resource_ids = t.resource_ids
        if resource_ids is not None:
            resource_ids_ba = bytearray(resource_ids.encode(encoding="utf-8"))
            out_buffer.put_int32(len(resource_ids_ba))
            if len(resource_ids_ba) > 0:
                out_buffer.put(resource_ids_ba)
        else:
            out_buffer.put_int32(0)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer class")
        if in_buffer.readable_bytes() < 2:
            return
        len = in_buffer.get_int16()
        if len > 0:
            if in_buffer.readable_bytes() < len:
                return
            ba = bytearray(len)
            in_buffer.get(ba)
            version = str(ba)
        else:
            return
        if in_buffer.readable_bytes() < 2:
            return
        len = in_buffer.get_int16()
        if len > 0:
            if in_buffer.readable_bytes() < len:
                return
            ba = bytearray(len)
            in_buffer.get(ba)
            t.application_id = str(ba)
        if in_buffer.readable_bytes() < 2:
            return
        len = in_buffer.get_int16()
        if in_buffer.readable_bytes() < len:
            return
        ba = bytearray(len)
        in_buffer.get(ba)
        t.transaction_service_group = str(ba)

        if in_buffer.readable_bytes() < 2:
            return
        len = in_buffer.get_int16()
        if len > 0:
            if in_buffer.readable_bytes() < len:
                return
            ba = bytearray(len)
            in_buffer.get(ba)
            t.extra_data = str(ba)
        if in_buffer.readable_bytes() < 4:
            return
        len = in_buffer.get_int32()
        if len > 0:
            if in_buffer.readable_bytes() < len:
                return
            ba = bytearray(len)
            in_buffer.get(ba)
            t.resource_ids = str(ba)


class RegisterRMResponseCodec(object):

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer class")
        AbstractIdentifyResponseCodec.encode(t, out_buffer)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer class")
        AbstractIdentifyResponseCodec.decode(t, in_buffer)
