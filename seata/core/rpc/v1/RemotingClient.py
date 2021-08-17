#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import select
import threading
import time

from gevent import monkey

from seata.core.ByteBuffer import ByteBuffer

monkey.patch_socket()

from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.protocol.ProtocolConstants import ProtocolConstants
from seata.core.protocol.RpcMessage import RpcMessage

from seata.core.rpc.v1.ProtocolV1 import ProtocolV1

import socket

class NoneMessage:
    pass


class RemotingClient:
    dataBuffer = bytes()

    def __init__(self, host, port, message_handler):
        # key: rpc_message.id value: rpc_message.body
        self.req_msg_map = {}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        try:
            self.sock.connect((host, port))
        except BlockingIOError:
            pass
        self.message_handler = message_handler
        self.message_handler.set_remote_client(self)
        self.protocol = ProtocolV1()
        self.outputs = []

    def start(self):
        threading.Thread(target=self.do_start, args=()).start()

    def do_start(self):
        socket_list = [self.sock]
        while True:
            read_sockets, write_sockets, error_sockets = select.select(socket_list, [self.sock], [])
            for sock in read_sockets:
                if sock == self.sock:
                    recv_data = sock.recv(4096)
                    if len(recv_data) <= 0:
                        print('\ndisconnected from server')
                        break
                    else:
                        self.dataBuffer += recv_data
                        if len(self.dataBuffer) < 7:
                            break
                        bb = ByteBuffer.wrap(bytearray(self.dataBuffer))
                        magic = bytearray(len(ProtocolConstants.MAGIC_CODE_BYTES))
                        bb.get(magic)
                        if magic != ProtocolConstants.MAGIC_CODE_BYTES:
                            print("magic not 0xdada", magic)
                            break
                        bb.get_int8()
                        full_length = bb.get_int32()
                        if len(self.dataBuffer) >= full_length:
                            buf = self.dataBuffer[0:full_length]
                            self.dataBuffer = self.dataBuffer[full_length:]
                            rpc_message = self.protocol.decode(ByteBuffer.wrap(bytearray(buf)))
                            self.message_handler.process(rpc_message)
                else:
                    pass

            for sock in write_sockets:
                if sock == self.sock:
                    ops = self.outputs.copy()
                    for rpc_message in ops:
                        sock.send(self.protocol.encode(rpc_message))
                    self.outputs.clear()

    def send_sync_request(self, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)

        self.outputs.append(rpc_message)

        self.req_msg_map[rpc_message.id] = NoneMessage()
        timeout = 0
        while isinstance(self.req_msg_map.get(rpc_message.id), NoneMessage) and timeout <= 30:
            timeout += 0.01
            time.sleep(0.01)
        response = self.req_msg_map[rpc_message.id]
        if isinstance(response, NoneMessage) and timeout > 30:
            raise TimeoutError()
        del self.req_msg_map[rpc_message.id]
        return response

    def send_async_request(self, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)

        self.outputs.append(rpc_message)

    def send_async_response(self, rpc_message, msg):
        rpc_msg = self.__build_response_message(rpc_message, msg, ProtocolConstants.MSGTYPE_RESPONSE)
        self.outputs.append(rpc_msg)

    def __build_response_message(self, rpc_message, msg, message_type):
        rpc_msg = RpcMessage()
        rpc_msg.message_type = message_type
        rpc_msg.codec = rpc_message.codec
        rpc_msg.compressor = rpc_message.compressor
        rpc_msg.body = msg
        rpc_msg.id = rpc_message.id
        return rpc_msg
