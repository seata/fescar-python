#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from twisted.internet import reactor
import threading
import time

from core.protocol.HeartbeatMessage import HeartbeatMessage
from core.protocol.RegisterTMRequestResponse import RegisterTMRequest
from core.rpc.v1.ProtocolV1Factory import ProtocolV1Factory

factory = None


def do_heart(factory):  # 每隔 5秒 向服务器发送消息
    while True:
        try:
            # 判断连接状态（factory.protocol.connected），决定是否向服务器发送消息
            if factory.protocol and factory.protocol.connected:
                hb = HeartbeatMessage(True)
                factory.protocol.encode(hb)
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


class TMClient(object):

    def __init__(self, application_id=None, transaction_service_group=None):
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group

    def init_client(self, host="localhost", port=8091):
        # 程序启动
        global factory
        factory = ProtocolV1Factory()  # 实例化通信类
        reactor.connectTCP(host, port, factory)  # 指定需要连接的服务器地址和端口
        threading.Thread(target=do_heart, args=(factory,)).start()
        threading.Thread(target=do_init, args=(self,)).start()
        threading.Thread(target=reactor.run, args=()).start()


    def reg(self):
        request = RegisterTMRequest(self.application_id, self.transaction_service_group)
        TMClient.send_request(request)

    @staticmethod
    def send_request(msg):
        wait_connected()
        if factory.protocol and factory.protocol.connected:
            return factory.protocol.encode(msg)
        else:
            print("tm client not connected...")
            return None
