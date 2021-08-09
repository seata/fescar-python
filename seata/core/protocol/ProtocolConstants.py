#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class ProtocolConstants(object):
    # Magic code
    MAGIC_CODE_BYTES = bytearray([0xda, 0xda])
    # Protocol version
    VERSION = 1
    # Max frame length
    MAX_FRAME_LENGTH = 8 * 1024 * 1024
    # HEAD_LENGTH of protocol v1
    V1_HEAD_LENGTH = 16
    # Message type: Request
    MSGTYPE_RESQUEST_SYNC = 0
    # Message type: Response
    MSGTYPE_RESPONSE = 1
    # Message type: Request which no need response
    MSGTYPE_RESQUEST_ONEWAY = 2
    #  Message type: Heartbeat Request
    MSGTYPE_HEARTBEAT_REQUEST = 3
    # Message type: Heartbeat Response
    MSGTYPE_HEARTBEAT_RESPONSE = 4
