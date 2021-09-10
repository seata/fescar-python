#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.model.BranchStatus import BranchStatus
from seata.core.protocol.transaction.AbstractTransactionRequestResponseCodec import AbstractTransactionResponseCodec
from seata.core.ByteBuffer import ByteBuffer
from seata.core.model.BranchType import BranchType


class AbstractBranchEndRequestCodec(object):

    @staticmethod
    def encode(t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        xid = t.xid
        branch_id = t.branch_id
        branch_type = t.branch_type
        resource_id = t.resource_id
        application_data = t.application_data
        if xid is not None:
            xid_ba = bytearray(xid)
            out_buffer.put_int16(len(xid_ba))
            if len(xid_ba) > 0:
                out_buffer.put(xid_ba)
        else:
            out_buffer.put_int16(0)

        out_buffer.put_int64(branch_id)
        out_buffer.put_int8(branch_type.value)
        if resource_id is not None:
            resource_id_ba = bytearray(resource_id.encode(encoding="utf-8"))
            out_buffer.put_int16(len(resource_id_ba))
            if len(resource_id_ba) > 0:
                out_buffer.put(resource_id_ba)
        else:
            out_buffer.put_int16(0)

        if application_data is not None:
            application_data_ba = bytearray(application_data.encode(encoding="utf-8"))
            out_buffer.put_int32(len(application_data_ba))
            if len(application_data_ba) > 0:
                out_buffer.put(application_data_ba)
        else:
            out_buffer.put_int32(0)

    @staticmethod
    def decode(t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        xid_len = 0
        if in_buffer.readable_bytes() > 2:
            xid_len = in_buffer.get_int16()
        if xid_len <= 0:
            return
        if in_buffer.readable_bytes() < xid_len:
            return
        xid_ba = bytearray(xid_len)
        in_buffer.get(xid_ba)
        t.xid = xid_ba.decode(encoding="utf-8")

        if in_buffer.readable_bytes() < 8:
            return
        t.branch_id = in_buffer.get_int64()

        if in_buffer.readable_bytes() < 1:
            return
        t.branch_type = BranchType(in_buffer.get_int8())

        if in_buffer.readable_bytes() < 2:
            return
        resource_id_len = in_buffer.get_int16()
        if resource_id_len <= 0:
            return
        if in_buffer.readable_bytes() < resource_id_len:
            return
        resource_id_ba = bytearray(resource_id_len)
        in_buffer.get(resource_id_ba)
        t.resource_id = resource_id_ba.decode(encoding="utf-8")

        application_data_len = 0
        if in_buffer.readable_bytes() < 4:
            return
        application_data_len = in_buffer.get_int32()
        if application_data_len > 0:
            if in_buffer.readable_bytes() < application_data_len:
                return
            application_data_da = bytearray(application_data_len)
            in_buffer.get(application_data_da)
            t.application_data = application_data_da.decode(encoding="utf-8")


class AbstractBranchEndResponseCodec(object):

    @staticmethod
    def encode(t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        AbstractTransactionResponseCodec.encode(t, out_buffer)
        xid = t.xid
        branch_id = t.branch_id
        branch_status = t.branch_status
        if xid is not None:
            xid_ba = bytearray(xid.encode(encoding="utf-8"))
            out_buffer.put_int16(len(xid_ba))
            if len(xid_ba) > 0:
                out_buffer.put(xid_ba)
        else:
            out_buffer.put_int16(0)

        out_buffer.put_int64(branch_id)
        out_buffer.put_int8(branch_status.value[0])

    @staticmethod
    def decode(t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        AbstractTransactionResponseCodec.decode(t, in_buffer)
        xid_len = in_buffer.get_int16()
        if xid_len > 0:
            xid_ba = bytearray(xid_len)
            in_buffer.get(xid_ba)
            t.xid = xid_ba.decode(encoding="utf-8")
        t.branch_id = in_buffer.get_int64()
        bs = in_buffer.get_int8()
        t.branch_status = BranchStatus(bs)
