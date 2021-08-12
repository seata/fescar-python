#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from twisted.internet import reactor
import threading
import time

from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.protocol.ProtocolConstants import ProtocolConstants
from seata.core.protocol.RegisterRMRequestResponse import RegisterRMRequest
from seata.core.protocol.RpcMessage import RpcMessage
from seata.core.rpc.v1.ProtocolV1Factory import ProtocolV1Factory

factory = None


def do_heart(factory):  # 每隔 5秒 向服务器发送消息
    while True:
        try:
            # 判断连接状态（factory.protocol.connected），决定是否向服务器发送消息
            wait_connected(factory)
            hb = HeartbeatMessage(True)
            RMClient.get().send_sync_request(hb)
            print("rm client do heart...")
            time.sleep(1)
        except Exception as e:
            pass


def do_init(client, factory):
    wait_connected(factory)
    client.reg()


def wait_connected(factory, seconds=1):
    while not (factory.protocol and factory.protocol.connected):
        print("wait connected...")
        time.sleep(seconds)


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

    def set_transaction_service_group(self, transaction_service_group):
        self.transaction_service_group = transaction_service_group

    def set_application_id(self, application_id):
        self.application_id = application_id

    def init_client(self, host="localhost", port=8091):
        # 程序启动
        global factory
        factory = ProtocolV1Factory()  # 实例化通信类
        reactor.connectTCP(host, port, factory)  # 指定需要连接的服务器地址和端口
        threading.Thread(target=do_heart, args=(factory,)).start()
        threading.Thread(target=do_init, args=(self, factory,)).start()

    def reg(self):
        request = RegisterRMRequest(self.application_id, self.transaction_service_group)
        self.send_sync_request(request)
        print("rm register...")

    def send_sync_request(self, msg):
        wait_connected(factory)
        if factory.protocol and factory.protocol.connected:
            if isinstance(msg, HeartbeatMessage):
                rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
            else:
                rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)
            return factory.protocol.encode(rpc_message)
        else:
            print("rm client not connected...")
            return None
