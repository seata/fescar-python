#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import threading

from seata.core.protocol.RegisterRMRequestResponse import RegisterRMRequest
from seata.core.rpc.v1.ChannelManager import ChannelManager
from seata.core.rpc.v1.RemotingClient import RemotingClient


class RmRemotingClient(RemotingClient):
    lock = threading.RLock()
    client = None

    @classmethod
    def get_client(cls, application_id=None, transaction_service_group=None, message_handler=None):
        if cls.client is None:
            try:
                cls.lock.acquire()
                if cls.client is None:
                    cls.client = RmRemotingClient(application_id, transaction_service_group, message_handler)
            finally:
                cls.lock.release()
        return cls.client

    def __init__(self, application_id, transaction_service_group, message_handler):
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        self.futures = {}
        self.channel_manager = ChannelManager(self)

        super(RmRemotingClient, self).__init__(self.channel_manager, self.futures, self.transaction_service_group)

        self.message_handler = message_handler
        self.message_handler.set_remote_client(self, self.futures)

        self.init()

    def init(self):
        threading.Thread(target=self.do_reconnect, args=()).start()

    def register_resource(self, resource_group_id, resource_id):
        request = RegisterRMRequest(self.application_id, self.transaction_service_group)
        request.resource_ids = resource_id

        channels = self.channel_manager.get_channels()
        for channel in channels:
            response = self.send_sync_request_channel(channel, request)
            self.on_reg_response(request, response)

    def on_reg_response(self, request, response):
        if response.result:
            print("rm register success. [{}] [{}]".format(request.transaction_service_group, request.resource_ids))
        else:
            print("rm register failed. [{}] [{}]".format(request.transaction_service_group, request.resource_ids))