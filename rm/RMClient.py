#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from twisted.internet import reactor
import threading
import time

from core.protocol.HeartbeatMessage import HeartbeatMessage
from core.rpc.v1.ProtocolV1Factory import ProtocolV1Factory

bStop = False
factory = None


def do_heart(factory):  # 每隔 5秒 向服务器发送消息
    while not bStop:
        # 判断连接状态（factory.protocol.connected），决定是否向服务器发送消息
        if factory.protocol and factory.protocol.connected:
            hb = HeartbeatMessage(True)
            factory.protocol.encode(hb)
            time.sleep(5)


class RMClient(object):

    def __init__(self, application_id, transaction_service_group):
        self.appliction_id = application_id
        self.transaction_service_group = transaction_service_group

    def init_client(self, host="localhost", port=8091):
        # 程序启动
        global factory
        factory = ProtocolV1Factory()  # 实例化通信类
        reactor.connectTCP(host, port, factory)  # 指定需要连接的服务器地址和端口
        threading.Thread(target=do_heart, args=(factory,)).start()
        reactor.run()  # 挂起运行
        global bStop
        bStop = True

    @staticmethod
    def send_request(msg):
        if factory.protocol and factory.protocol.connected:
            factory.protocol.encode(msg)
        else:
            print("rm client connection lost...")
