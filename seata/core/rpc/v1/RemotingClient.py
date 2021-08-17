#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import datetime
import time

from gevent import monkey

monkey.patch_socket()

from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.protocol.ProtocolConstants import ProtocolConstants
from seata.core.protocol.RpcMessage import RpcMessage
from seata.core.protocol.transaction.BranchCommitRequestResponse import BranchCommitResponse
from seata.core.protocol.transaction.BranchRollbackRequestResponse import BranchRollbackResponse
from seata.rm.datasource.undo.UndoLogManagerFactory import UndoLogManagerFactory

from seata.core.protocol.MessageType import MessageType

from seata.core.rpc.v1.ProtocolV1 import ProtocolV1

import gevent

import socket


class RemotingClient:
    def __init__(self, host, port, message_handler):
        # key: rpc_message.id value: rpc_message.body
        self.req_msg_map = {}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        self.sock.connect((host, port))
        self.message_handler = message_handler
        self.message_handler.set_remote_client(self)
        self.protocol = ProtocolV1(self.sock, self.message_handler)

    def get_socket(self):
        return self.sock

    def send_sync_request(self, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)

        self.protocol.encode(rpc_message)

        self.req_msg_map[rpc_message.id] = None
        timeout = 0
        while self.req_msg_map[rpc_message.id] is None and timeout <= 30:
            timeout += 0.01
            time.sleep(0.01)
        response = self.req_msg_map[rpc_message.id]
        if response is None and timeout > 30:
            raise TimeoutError()
        self.req_msg_map.pop(rpc_message.id, None)
        return response

    def send_async_request(self, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)

        self.protocol.encode(rpc_message)

    def send_async_response(self, rpc_message, msg):
        rpc_msg = self.__build_response_message(rpc_message, msg, ProtocolConstants.MSGTYPE_RESPONSE)
        self.protocol.encode(rpc_msg)

    def __build_response_message(self, rpc_message, msg, message_type):
        rpc_msg = RpcMessage()
        rpc_msg.message_type = message_type
        rpc_msg.codec = rpc_message.codec
        rpc_msg.compressor = rpc_message.compressor
        rpc_msg.body = msg
        rpc_msg.id = rpc_message.id
        return rpc_msg
