#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import threading

atom = 0
lock = threading.RLock()


class RpcMessage(object):
    # int
    id = 0
    # byte
    message_type = 0
    # byte
    codec = 0
    # byte
    compressor = 0
    # map string, string
    head_map = dict()
    # Object
    body = None

    @staticmethod
    def get_id():
        global atom, lock
        with lock:
            atom = (atom + 1) & 0x7FFFFFFF
        return atom

    @staticmethod
    def build_request_message(msg, message_type):
        rpc_message = RpcMessage()
        rpc_message.id = RpcMessage.get_id()
        rpc_message.message_type = message_type
        rpc_message.codec = 0x1
        rpc_message.compressor = 0x0
        rpc_message.body = msg
        return rpc_message

