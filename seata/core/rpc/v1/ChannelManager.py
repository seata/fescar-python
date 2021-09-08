#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import sys
import queue
import selectors
import socket
import threading
import time
from concurrent.futures import ThreadPoolExecutor

from seata.core.ByteBuffer import ByteBuffer
from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.protocol.ProtocolConstants import ProtocolConstants
from seata.core.protocol.RpcMessage import RpcMessage
from seata.core.rpc.v1.ProtocolV1 import ProtocolV1
from seata.core.util.ClassUtil import ClassUtil
from seata.registry.Registry import RegistryFactory

debug = False


class Channel:
    def __init__(self, sock):
        self.sock = sock
        self.in_data = bytes()
        self.out_data = queue.Queue()
        self.cond = threading.Condition()

    def write(self, rpc_message):
        self.out_data.put_nowait(rpc_message)


class ChannelManager:
    def __init__(self, remote_client):
        self.remote_client = remote_client
        self.channels = {}
        self.sel = selectors.DefaultSelector()
        self.boot = False
        self.__cond = threading.Condition()
        self.protocol = ProtocolV1()
        # TODO
        self.executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix="cm")
        self.init()

    def init(self):
        threading.Thread(target=self.do_events, args=()).start()
        threading.Thread(target=self.do_heart, args=()).start()

    def acquire_channel(self, server_address):
        if self.channels.get(server_address.to_string(), None) is not None:
            return self.channels.get(server_address.to_string())
        server_addr = (server_address.host, server_address.port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        channel = Channel(socket)
        self.sel.register(sock, events, data=channel)
        self.channels[server_address.to_string()] = channel
        return channel

    def do_events(self):
        try:
            if sys.platform == 'win32' and not self.boot:
                try:
                    self.__cond.acquire()
                    self.__cond.wait()
                finally:
                    self.__cond.release()
            while True:
                events = self.sel.select()
                if events:
                    for key, mask in events:
                        self.service_connection(key, mask)
        except KeyboardInterrupt:
            print("caught keyboard interrupt, exiting")
        finally:
            self.sel.close()

    def service_connection(self, key, mask):
        sock = key.fileobj
        channel = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(4096)
            if len(recv_data) > 0:
                channel.in_data += recv_data
                if len(recv_data) < 7:
                    return
                t_bb = ByteBuffer.wrap(bytearray(channel.in_data))
                magic = bytearray(len(ProtocolConstants.MAGIC_CODE_BYTES))
                t_bb.get(magic)
                if magic != ProtocolConstants.MAGIC_CODE_BYTES:
                    print("magic not 0xdada", magic)
                    return
                t_bb.get_int8()
                full_length = t_bb.get_int32()
                if len(channel.in_data) >= full_length:
                    buf = channel.in_data[0:full_length]
                    channel.in_data = channel.in_data[full_length:]
                    in_message = self.protocol.decode(ByteBuffer.wrap(bytearray(buf)))
                    if not isinstance(in_message.body, HeartbeatMessage) or debug:
                        print('in message : <{}> request_id : {} sock : {}'.format(
                            ClassUtil.get_simple_name(in_message.body), in_message.id, sock.getpeername()))
                    self.executor.submit(self.remote_client.message_handler.process, in_message)
            else:
                print('sock unregister...', sock.getpeername())
                self.sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            while not channel.out_data.empty():
                out_message = channel.out_data.get_nowait()
                if not isinstance(out_message.body, HeartbeatMessage) or debug:
                    print(
                        'out message : <{}> request_id : {} sock : {}'.format(
                            ClassUtil.get_simple_name(out_message.body), out_message.id, sock.getpeername()))
                try:
                    sock.send(self.protocol.encode(out_message))
                except ConnectionAbortedError as e:
                    print(e)

    def get_avail_list(self, tx_service_group):
        avail_list = RegistryFactory.get_registry().lookup(tx_service_group)
        return avail_list

    def reconnect(self, tx_service_group):
        avail_list = self.get_avail_list(tx_service_group)
        if avail_list is None or len(avail_list) == 0:
            registry = RegistryFactory.get_registry()
            cluster_name = registry.get_service_group(tx_service_group)
            if cluster_name is None or len(cluster_name.strip()) == 0:
                print(
                    'can not get cluster name in registry config [{}{}], please make sure registry config correct'.format(
                        'service.vgroupMapping.', tx_service_group))
                return

            from seata.registry.FileRegistry import FileRegistry
            if not isinstance(registry, FileRegistry):
                print(
                    'no available service found in cluster [{}], please make sure registry config correct and keep your seata server running'.format(
                        cluster_name))
            return
        for address in avail_list:
            self.acquire_channel(address)

        if not self.boot:
            try:
                self.__cond.acquire()
                self.boot = True
                self.__cond.notify_all()
            finally:
                self.__cond.release()

    def do_heart(self):
        while True:
            try:
                if debug:
                    print('do heart channel size : [{}]'.format(len(self.channels.values())))
                for idx, channel in enumerate(self.channels.values()):
                    hb = HeartbeatMessage(True)
                    rpc_message = RpcMessage.build_request_message(hb, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
                    channel.write(rpc_message)
            except Exception as e:
                print('heart error', e)
            finally:
                try:
                    time.sleep(5)
                except Exception:
                    pass

    def get_channels(self):
        if not self.boot:
            try:
                self.__cond.acquire()
                self.__cond.wait(15)
            finally:
                self.__cond.release()
        return self.channels.values()
