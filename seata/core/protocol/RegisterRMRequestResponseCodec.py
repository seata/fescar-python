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
        version_len = in_buffer.get_int16()
        if version_len > 0:
            if in_buffer.readable_bytes() < version_len:
                return
            version_ba = bytearray(version_len)
            in_buffer.get(version_ba)
            t.version = version_ba.decode(encoding="utf-8")
        else:
            return
        if in_buffer.readable_bytes() < 2:
            return
        application_id_len = in_buffer.get_int16()
        if application_id_len > 0:
            if in_buffer.readable_bytes() < application_id_len:
                return
            application_id_ba = bytearray(application_id_len)
            in_buffer.get(application_id_ba)
            t.application_id = application_id_ba.decode(encoding="utf-8")
        if in_buffer.readable_bytes() < 2:
            return
        tx_service_group_len = in_buffer.get_int16()
        if in_buffer.readable_bytes() < tx_service_group_len:
            return
        tx_service_group_ba = bytearray(tx_service_group_len)
        in_buffer.get(tx_service_group_ba)
        t.transaction_service_group = tx_service_group_ba.decode(encoding="utf-8")

        if in_buffer.readable_bytes() < 2:
            return
        extra_data_len = in_buffer.get_int16()
        if extra_data_len > 0:
            if in_buffer.readable_bytes() < extra_data_len:
                return
            extra_data_ba = bytearray(extra_data_len)
            in_buffer.get(extra_data_ba)
            t.extra_data = extra_data_ba.decode(encoding="utf-8")
        if in_buffer.readable_bytes() < 4:
            return
        resource_ids_len = in_buffer.get_int32()
        if resource_ids_len > 0:
            if in_buffer.readable_bytes() < resource_ids_len:
                return
            resource_ids_ba = bytearray(resource_ids_len)
            in_buffer.get(resource_ids_ba)
            t.resource_ids = resource_ids_ba.decode(encoding="utf-8")


class RegisterRMResponseCodec(object):

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer class")
        AbstractIdentifyResponseCodec.encode(t, out_buffer)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer class")
        AbstractIdentifyResponseCodec.decode(t, in_buffer)
