#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.ByteBuffer import ByteBuffer
from seata.core.protocol.MessageTypeAware import MessageTypeAware
from seata.core.serializer.seata.MessageCodecFactory import MessageCodecFactory


class SeataSerializer(object):

    def __init__(self):
        pass

    def serialize(self, t):
        if t is None or not isinstance(t, MessageTypeAware):
            raise ValueError("message isn't available.")
        type_code = t.get_type_code()
        msg_codec = MessageCodecFactory.get_message_codec(type_code)
        bb = ByteBuffer()
        msg_codec.encode(t, bb)

        content_bb = ByteBuffer()
        content_bb.put_int16(type_code)
        content_bb.put(bb.array())

        return content_bb.array()

    def deserialize(self, byte_array):
        if byte_array is None or len(byte_array) == 0:
            raise ValueError("Nothing to decode.")
        if len(byte_array) < 2:
            raise ValueError("byte array isn't available for decode.")
        bb = ByteBuffer.wrap(byte_array)
        type_code = bb.get_int16()
        body = bytearray(bb.readable_bytes())
        bb.get(body)

        new_bb = ByteBuffer.wrap(body)
        message = MessageCodecFactory.get_message(type_code)
        message_codec = MessageCodecFactory.get_message_codec(type_code)
        message_codec.decode(message, new_bb)
        return message
