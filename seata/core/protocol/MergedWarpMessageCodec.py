#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from loguru import logger

from seata.core.ByteBuffer import ByteBuffer


class MergedWarpMessageCodec(object):

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer class")
        msgs = t.msgs
        buffer = ByteBuffer()
        for i in range(len(msgs)):
            msg = msgs[i]
            bb = ByteBuffer()
            type_code = msg.get_type_code()
            from seata.core.serializer.seata.MessageCodecFactory import MessageCodecFactory
            message_codec = MessageCodecFactory.get_message_codec(type_code)
            message_codec.encode(msg, bb)
            buffer.put_int16(type_code)
            buffer.put(bb.array())

        out_buffer.put_int32(buffer.readable_bytes() + 2)
        out_buffer.put_int16(len(msgs))
        content = buffer.array()
        out_buffer.put(content)
        if len(msgs) > 20:
            logger.info("msg in one packet:[{}], buffer size:[{}]".format(len(msgs), len(content)))

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer class")
        if in_buffer.readable_bytes() < 4:
            return
        length = in_buffer.get_int32()
        if in_buffer.readable_bytes() < length:
            return
        buffer_ba = bytearray(length)
        in_buffer.get(buffer_ba)
        byte_buffer = ByteBuffer.wrap(buffer_ba)
        self._do_decode(t, byte_buffer)

    def _do_decode(self, t, byte_buffer):
        msg_num = byte_buffer.get_int16()
        msgs = []
        for i in range(msg_num):
            type_code = byte_buffer.get_int16()
            from seata.core.serializer.seata.MessageCodecFactory import MessageCodecFactory
            message = MessageCodecFactory.get_message(type_code)
            message_codec = MessageCodecFactory.get_message_codec(type_code)
            message_codec.encode(message, byte_buffer)
            msgs.append(message)
        t.msgs = msgs
