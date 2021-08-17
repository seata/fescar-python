#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

import threading
import time

from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.protocol.RegisterTMRequestResponse import RegisterTMRequest
from seata.core.rpc.v1.RemotingClient import RemotingClient


def do_heart(remote_client):  # 每隔 5秒 向服务器发送消息
    while True:
        try:
            hb = HeartbeatMessage(True)
            remote_client.send_async_request(hb)
            print("tm client do heart...")
            time.sleep(5)
        except Exception:
            pass


client = None
lock = threading.RLock()


class TMClient(object):
    @staticmethod
    def get():
        global client, lock
        if client is None:
            with lock:
                if client is None:
                    client = TMClient(None, None)
        return client

    def __init__(self, application_id=None, transaction_service_group=None):
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        self.remote_client = None

    def init_client(self, host="localhost", port=8091):
        # 程序启动
        from seata.rm.DefaultHandler import DefaultHandler
        message_handler = DefaultHandler()
        self.remote_client = RemotingClient(host, port, message_handler)
        threading.Thread(target=do_heart, args=(self.remote_client,)).start()
        self.reg()

    def reg(self):
        request = RegisterTMRequest(self.application_id, self.transaction_service_group, None)
        self.send_sync_request(request)
        print("tm register...")

    def send_sync_request(self, msg):
        self.remote_client.send_sync_request(msg)
