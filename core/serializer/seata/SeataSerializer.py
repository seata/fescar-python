#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.protocol.MessageType import MessageType
from core.protocol.MessageTypeAware import MessageTypeAware
from core.serializer.seata.MessageCodecFactory import MessageCodecFactory


class SeataSerializer(object):

    def __init__(self):
        pass

    def serialize(self, t):
        if t is None or not isinstance(t, MessageTypeAware):
            raise ValueError("message isn't available.")
        type_code = t.get_type_code()
        msg_codec = MessageCodecFactory.get_message_codec(type_code)



        return None

    def deserialize(self, v):
        return None