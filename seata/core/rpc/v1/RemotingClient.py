#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import time

from loguru import logger

from seata.core.c.Future import Future
from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.protocol.ProtocolConstants import ProtocolConstants
from seata.core.protocol.RpcMessage import RpcMessage
from seata.registry.Registry import RegistryFactory


class RemotingClient:
    RPC_TIMEOUT = 30

    def __init__(self, channel_manager, futures, transaction_service_group):
        self.channel_manager = channel_manager
        self.futures = futures
        self.transaction_service_group = transaction_service_group

    def do_reconnect(self):
        while True:
            try:
                self.channel_manager.reconnect(self.transaction_service_group)
            except Exception as e:
                logger.error('reconnect error', e)
            finally:
                try:
                    time.sleep(5)
                except Exception:
                    pass

    def send_sync_request(self, msg):
        server_address = self.load_balance(self.transaction_service_group, msg)
        channel = self.channel_manager.acquire_channel(server_address)
        return self.send_sync_request_channel(channel, msg)

    def send_sync_request_channel(self, channel, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)

        channel.write(rpc_message)

        f = Future()
        self.futures[rpc_message.id] = f
        try:
            response = f.get(self.RPC_TIMEOUT)
        except TimeoutError as e:
            raise e
        finally:
            del self.futures[rpc_message.id]
        return response

    def send_async_request(self, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_ONEWAY)

        server_address = self.load_balance(self.transaction_service_group, msg)
        channel = self.channel_manager.acquire_channel(server_address)

        channel.write(rpc_message)

    def send_async_response(self, rpc_message, msg):
        rpc_msg = RpcMessage.build_response_message(rpc_message, msg, ProtocolConstants.MSGTYPE_RESPONSE)
        server_address = self.load_balance(self.transaction_service_group, msg)
        channel = self.channel_manager.acquire_channel(server_address)
        channel.write(rpc_msg)

    def load_balance(self, transaction_service_group, msg):
        # TODO
        address_list = RegistryFactory.get_registry().lookup(transaction_service_group)
        import random
        return address_list[random.randint(0, len(address_list) - 1)]
