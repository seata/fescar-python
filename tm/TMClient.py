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


def get_factory():
    return factory


def routine(factory):  # 每隔 5秒 向服务器发送消息
    while not bStop:
        # 判断连接状态（factory.protocol.connected），决定是否向服务器发送消息
        if factory.protocol and factory.protocol.connected:
            hb = HeartbeatMessage(True)
            factory.protocol.encode(hb)
            time.sleep(5)


class TmClient(object):

    def __init__(self):
        pass

    def init_client(self, host="localhost", port=8091):
        # 程序启动
        global factory
        factory = ProtocolV1Factory()  # 实例化通信类
        reactor.connectTCP(host, port, factory)  # 指定需要连接的服务器地址和端口
        threading.Thread(target=routine, args=(factory,)).start()  # 启动线程运行routine()函数
        reactor.run()  # 挂起运行
        global bStop
        bStop = True