#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from gevent import monkey

monkey.patch_socket()

from seata.core.rpc.v1.ProtocolV1 import ProtocolV1

import socket


class DefaultHandler:
    def on_response(self, result_message):
        pass


class RemotingClient:
    def __init__(self, host, port):
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.skt.connect((host, port))
        self.result_message_handler = DefaultHandler()
        self.protocol = ProtocolV1(self.skt, self.result_message_handler)
        self.req_id_map = {}

    def get_socket(self):
        return self.skt

    def send_sync(self, rpc_message):
        self.protocol.encode(rpc_message)

        self.req_id_map[rpc_message.id] = None
        timeout = 0
        while self.req_id_map[rpc_message.id] is None and timeout <= 30:
            timeout += 0.01
            gevent.sleep(0.01)
        response = self.req_id_map[rpc_message.id]
        if response is None and timeout > 30:
            raise TimeoutError()
        self.req_id_map.pop(rpc_message.id, None)
        return response
