#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import threading
import time

from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.rpc.v1.RemotingClient import RemotingClient


def do_heart(remote_client):
    # 每隔 5秒 向服务器发送消息
    while True:
        try:
            hb = HeartbeatMessage(True)
            remote_client.send_async_request(hb)
            # print("rm client do heart...")
            time.sleep(5)
        except Exception as e:
            pass


client = None
lock = threading.RLock()


class RMClient(object):
    @staticmethod
    def get():
        global client, lock
        if client is None:
            with lock:
                if client is None:
                    client = RMClient(None, None)
        return client

    def __init__(self, application_id, transaction_service_group):
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        self.remote_client = None
        from seata.rm.DefaultResourceManager import DefaultResourceManager
        self.resource_manager = DefaultResourceManager.get()

    def set_transaction_service_group(self, transaction_service_group):
        self.transaction_service_group = transaction_service_group

    def set_application_id(self, application_id):
        self.application_id = application_id

    def init_client(self, host="localhost", port=8091):
        from seata.rm.RMHandlerAT import RMHandlerAT
        message_handler = RMHandlerAT()
        self.remote_client = RemotingClient(host, port, message_handler)
        self.remote_client.start()
        threading.Thread(target=do_heart, args=(self.remote_client,)).start()

    def send_sync_request(self, msg):
        return self.remote_client.send_sync_request(msg)
