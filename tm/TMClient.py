#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from twisted.internet import reactor
import threading
import time

from core.protocol.HeartbeatMessage import HeartbeatMessage
from core.protocol.ProtocolConstants import ProtocolConstants
from core.protocol.RegisterTMRequestResponse import RegisterTMRequest
from core.protocol.RpcMessage import RpcMessage
from core.rpc.v1.ProtocolV1Factory import ProtocolV1Factory

factory = None


def do_heart():  # 每隔 5秒 向服务器发送消息
    while True:
        try:
            wait_connected()
            hb = HeartbeatMessage(True)
            TMClient.get().send_sync_request(hb)
            time.sleep(5)
        except Exception as e:
            pass


def wait_connected(seconds=1):
    while not (factory.protocol and factory.protocol.connected):
        print("wait connected...")
        time.sleep(seconds)


def do_init(client):
    wait_connected()
    client.reg()


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

    def init_client(self, host="localhost", port=8091):
        # 程序启动
        global factory
        factory = ProtocolV1Factory()  # 实例化通信类
        reactor.connectTCP(host, port, factory)  # 指定需要连接的服务器地址和端口
        threading.Thread(target=do_heart, args=()).start()
        threading.Thread(target=do_init, args=(self,)).start()
        if not reactor.running:
            threading.Thread(target=reactor.run, args=(False,)).start()

    def reg(self):
        request = RegisterTMRequest(self.application_id, self.transaction_service_group, None)
        self.send_sync_request(request)
        print("tm register...")

    def send_sync_request(self, msg):
        wait_connected()
        if factory.protocol and factory.protocol.connected:
            if isinstance(msg, HeartbeatMessage):
                rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
            else:
                rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)
            return factory.protocol.encode(rpc_message)
        else:
            print("tm client not connected...")
            return None

