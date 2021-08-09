#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.protocol.MessageType import MessageType
from seata.core.protocol.MessageTypeAware import MessageTypeAware


class HeartbeatMessage(MessageTypeAware):
    ping = True

    def __init__(self, ping):
        self.ping = ping

    def set_ping(self, ping):
        self.ping = ping

    def get_ping(self):
        return self.ping

    def get_type_code(self):
        return MessageType.TYPE_HEARTBEAT_MSG

