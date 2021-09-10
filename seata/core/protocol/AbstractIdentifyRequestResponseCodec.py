#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.ByteBuffer import ByteBuffer


class AbstractIdentifyRequestCodec(object):

    @staticmethod
    def encode(t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer class")
        version = t.version
        application_id = t.application_id
        transaction_service_group = t.transaction_service_group
        extra_data = t.extra_data
        if version is not None:
            version_ba = bytearray(version.encode(encoding="utf-8"))
            out_buffer.put_int16(len(version_ba))
            if len(version_ba) > 0:
                out_buffer.put(version_ba)
        else:
            out_buffer.put_int16(0)

        if application_id is not None:
            application_id_ba = bytearray(application_id.encode(encoding="utf-8"))
            out_buffer.put_int16(len(application_id_ba))
            if len(application_id_ba) > 0:
                out_buffer.put(application_id_ba)
        else:
            out_buffer.put_int16(0)

        if transaction_service_group is not None:
            transaction_service_group_ba = bytearray(transaction_service_group.encode(encoding="utf-8"))
            out_buffer.put_int16(len(transaction_service_group_ba))
            if len(transaction_service_group_ba) > 0:
                out_buffer.put(transaction_service_group_ba)
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
            raise TypeError("in_buffer is not ByteBuffer class")
        if in_buffer.readable_bytes() < 2:
            return
        version_len = in_buffer.get_int16()
        if in_buffer.readable_bytes() < version_len:
            return
        version_ba = bytearray(version_len)
        in_buffer.get(version_ba)
        t.version = version_ba.decode(encoding="utf-8")

        if in_buffer.readable_bytes() < 2:
            return
        application_id_len = in_buffer.get_int16()
        if in_buffer.readable_bytes() < application_id_len:
            return
        application_id_ba = bytearray(application_id_len)
        in_buffer.get(application_id_ba)
        t.application_id = application_id_ba.decode(encoding="utf-8")

        if in_buffer.readable_bytes() < 2:
            return
        transaction_service_group_len = in_buffer.get_int16()
        if in_buffer.readable_bytes() < transaction_service_group_len:
            return
        transaction_service_group_ba = bytearray(transaction_service_group_len)
        in_buffer.get(transaction_service_group_ba)
        t.transaction_service_group = transaction_service_group_ba.decode(encoding="utf-8")

        if in_buffer.readable_bytes() < 2:
            return
        extra_data_len = in_buffer.get_int16()
        if in_buffer.readable_bytes() < extra_data_len:
            return
        extra_data_ba = bytearray(extra_data_len)
        in_buffer.get(extra_data_ba)
        t.extra_data = extra_data_ba.decode(encoding="utf-8")


class AbstractIdentifyResponseCodec(object):

    @staticmethod
    def encode(t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer class")
        identified = t.identified
        version = t.version
        if identified:
            out_buffer.put_int8(1)
        else:
            out_buffer.put_int8(0)
        if version is not None:
            version_ba = bytearray(version)
            out_buffer.put_int16(len(version_ba))
            if len(version_ba) > 0:
                out_buffer.put(version_ba)
        else:
            out_buffer.put_int16(0)

    @staticmethod
    def decode(t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer class")
        t.identified = in_buffer.get_int8() == 1
        version_len = in_buffer.get_int16()
        if version_len <= 0:
            return
        if in_buffer.readable_bytes() < version_len:
            return
        version_ba = bytearray(version_len)
        in_buffer.get(version_ba)
        t.version = version_ba.decode(encoding="utf-8")

