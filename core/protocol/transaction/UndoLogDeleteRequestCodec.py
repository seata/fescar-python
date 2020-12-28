#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.ByteBuffer import ByteBuffer
from core.model.BranchType import BranchType


class UndoLogDeleteRequestCodec(object):

    def __init__(self):
        pass

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer")
        save_days = t.save_days
        branch_type = t.branch_type
        resource_id = t.resource_id
        out_buffer.put_int8(branch_type.value)
        if resource_id is not None:
            resource_id_ba = bytearray(resource_id)
            out_buffer.put_int16(len(resource_id_ba))
            if len(resource_id_ba) > 0:
                out_buffer.put(resource_id_ba)
        else:
            out_buffer.put_int16(0)
        out_buffer.put_int16(save_days)

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer")
        if in_buffer.readable_bytes() < 1:
            return
        t.branch_type = BranchType(in_buffer.get_int8())
        if in_buffer.readable_bytes() < 2:
            return
        resource_id_len = in_buffer.get_int16()
        if resource_id_len <= 0 or in_buffer.readable_bytes() < resource_id_len:
            return
        resource_id_ba = bytearray(resource_id_len)
        in_buffer.get(resource_id_ba)
        t.resource_id = str(resource_id_ba)
        if in_buffer.readable_bytes() < 2:
            return
        t.save_days = in_buffer.get_int16()
