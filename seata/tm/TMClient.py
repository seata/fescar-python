#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

import threading
import time

from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.protocol.ProtocolConstants import ProtocolConstants
from seata.core.protocol.RegisterTMRequestResponse import RegisterTMRequest
from seata.core.protocol.RpcMessage import RpcMessage
from seata.core.rpc.v1.RemotingClient import RemotingClient


def do_heart():  # 每隔 5秒 向服务器发送消息
    while True:
        try:
            hb = HeartbeatMessage(True)
            TMClient.get().send_sync_request(hb)
            print("tm client do heart...")
            time.sleep(5)
        except Exception as e:
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
        self.remote_client = RemotingClient(host, port)
        threading.Thread(target=do_heart, args=()).start()
        self.reg()

    def reg(self):
        request = RegisterTMRequest(self.application_id, self.transaction_service_group, None)
        self.send_sync_request(request)
        print("tm register...")

    def send_sync_request(self, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)
        return self.remote_client.protocol.encode(rpc_message)
