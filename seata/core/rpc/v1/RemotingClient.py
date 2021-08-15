#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from gevent import monkey;

from seata.core.rpc.v1.ProtocolV1 import ProtocolV1

monkey.patch_socket()
import gevent
import socket

class RemotingClient:

    def __init__(self, host, port):
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.skt.connect((host, port))
        self.protocol = ProtocolV1(self.skt)

    def get_socket(self):
        return self.skt
