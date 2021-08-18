#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import queue
import select
import socket
import threading
import time

from seata.core.ByteBuffer import ByteBuffer
from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.protocol.ProtocolConstants import ProtocolConstants
from seata.core.protocol.RpcMessage import RpcMessage
from seata.core.rpc.v1.ProtocolV1 import ProtocolV1
from seata.core.util.ClassUtil import ClassUtil


class RemotingClient:
    RPC_TIMEOUT = 120

    def __init__(self, host, port, message_handler):
        # key: rpc_message.id value: rpc_message.body
        self.req_msg_map = {}
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        try:
            self.sock.connect((host, port))
        except BlockingIOError:
            pass
        self.message_handler = message_handler
        self.message_handler.set_remote_client(self)
        self.protocol = ProtocolV1()
        self.out_data = {}
        self.in_data = {}

    def start(self):
        threading.Thread(target=self.do_start, args=()).start()

    def do_start(self):
        self.out_data[self.sock] = queue.Queue()
        self.in_data[self.sock] = bytes()
        while True:
            read_sockets, write_sockets, error_sockets = select.select([self.sock], [self.sock], [self.sock])
            for r_sock in read_sockets:
                if r_sock == self.sock:
                    recv_data = r_sock.recv(4096)
                    if len(recv_data) <= 0:
                        print('\ndisconnected from server')
                        break
                    else:
                        self.__append_in_data(r_sock, recv_data)
                        data_buf = self.__get_in_data(r_sock)
                        if len(data_buf) < 7:
                            break
                        t_bb = ByteBuffer.wrap(bytearray(data_buf))
                        magic = bytearray(len(ProtocolConstants.MAGIC_CODE_BYTES))
                        t_bb.get(magic)
                        if magic != ProtocolConstants.MAGIC_CODE_BYTES:
                            print("magic not 0xdada", magic)
                            break
                        t_bb.get_int8()
                        full_length = t_bb.get_int32()
                        if len(data_buf) >= full_length:
                            buf = data_buf[0:full_length]
                            self.__set_in_data(r_sock, data_buf[full_length:])
                            in_message = self.protocol.decode(ByteBuffer.wrap(bytearray(buf)))
                            if not isinstance(in_message.body, HeartbeatMessage):
                                print('in message : <{}> request_id : {}'.format(
                                    ClassUtil.get_simple_name(in_message.body),
                                    in_message.id))
                            self.message_handler.process(in_message)
                else:
                    pass

            for w_sock in write_sockets:
                if w_sock == self.sock:
                    while not self.out_data.get(w_sock).empty():
                        out_message = self.out_data.get(w_sock).get_nowait()
                        if not isinstance(out_message.body, HeartbeatMessage):
                            print(
                                'out message : <{}> request_id : {}'.format(ClassUtil.get_simple_name(out_message.body),
                                                                            out_message.id))
                        try:
                            w_sock.send(self.protocol.encode(out_message))
                        except ConnectionAbortedError as e:
                            print(e)

            for e_sock in error_sockets:
                if e_sock == self.sock:
                    print('sock error', e_sock)
                    pass

    def send_sync_request(self, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)

        self.__append_out_data(rpc_message)

        self.req_msg_map[rpc_message.id] = -1
        timeout = 0
        while self.req_msg_map.get(rpc_message.id) == -1 and timeout <= self.RPC_TIMEOUT:
            timeout += 0.01
            time.sleep(0.01)
        response = self.req_msg_map.get(rpc_message.id)
        if response == -1 and timeout > 30:
            raise TimeoutError()
        del self.req_msg_map[rpc_message.id]
        return response

    def send_async_request(self, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)

        self.__append_out_data(rpc_message)

    def send_async_response(self, rpc_message, msg):
        rpc_msg = self.__build_response_message(rpc_message, msg, ProtocolConstants.MSGTYPE_RESPONSE)
        self.__append_out_data(rpc_msg)

    def __append_out_data(self, rpc_message):
        self.out_data.get(self.sock).put_nowait(rpc_message)

    def __append_in_data(self, sock, in_buf):
        buf = self.in_data.get(sock)
        buf += in_buf
        self.in_data[sock] = buf

    def __get_in_data(self, sock):
        return self.in_data.get(sock)

    def __set_in_data(self, sock, in_buf):
        self.in_data[sock] = in_buf

    def __build_response_message(self, rpc_message, msg, message_type):
        rpc_msg = RpcMessage()
        rpc_msg.message_type = message_type
        rpc_msg.codec = rpc_message.codec
        rpc_msg.compressor = rpc_message.compressor
        rpc_msg.body = msg
        rpc_msg.id = rpc_message.id
        return rpc_msg
