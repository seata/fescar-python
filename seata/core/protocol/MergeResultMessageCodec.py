#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from loguru import logger

from seata.core.ByteBuffer import ByteBuffer


class MergeResultMessageCodec(object):

    def encode(self, t, out_buffer):
        if not isinstance(out_buffer, ByteBuffer):
            raise TypeError("out_buffer is not ByteBuffer class")
        msgs = t.msgs

        msg_bb = ByteBuffer()
        for i in range(len(msgs)):
            msg = msgs[i]
            type_code = msg.get_type_code()
            msg_bb.put_int16(type_code)
            from seata.core.serializer.seata.MessageCodecFactory import MessageCodecFactory
            message_codec = MessageCodecFactory.get_message_codec(type_code)
            message_codec.encode(msg, msg_bb)
        length = msg_bb.readable_bytes() + 2
        out_buffer.put_int32(length)
        out_buffer.put_int16(len(msgs))
        out_buffer.put(msg_bb.array())
        if len(msgs) > 20:
            logger.info("msg in one services merge packet:[{}],buffer size:[{}]".format(len(msgs), length))

    def decode(self, t, in_buffer):
        if not isinstance(in_buffer, ByteBuffer):
            raise TypeError("in_buffer is not ByteBuffer class")
        if in_buffer.readable_bytes() < 4:
            return
        length = in_buffer.get_int32()
        if in_buffer.readable_bytes() < length:
            return
        ba = bytearray(length)
        in_buffer.get(ba)
        byte_buffer = ByteBuffer.wrap(ba)
        self._do_decode(t, byte_buffer)

    def _do_decode(self, t, byte_buffer):
        msg_num = byte_buffer.get_int16()
        msgs = []
        for i in range(msg_num):
            type_code = byte_buffer.get_int16()
            from seata.core.serializer.seata.MessageCodecFactory import MessageCodecFactory
            message = MessageCodecFactory.get_message(type_code)
            message_codec = MessageCodecFactory.get_message_codec(type_code)
            message_codec.decode(message, byte_buffer)
            msgs.append(message)
        t.msgs = msgs
