#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import threading

from loguru import logger

from seata.core.protocol.RegisterTMRequestResponse import RegisterTMRequest
from seata.core.rpc.v1.ChannelManager import ChannelManager
from seata.core.rpc.v1.RemotingClient import RemotingClient


class TmRemotingClient(RemotingClient):
    lock = threading.RLock()
    client = None

    @classmethod
    def get_client(cls, application_id=None, transaction_service_group=None, message_handler=None):
        if cls.client is None:
            try:
                cls.lock.acquire()
                if cls.client is None:
                    cls.client = TmRemotingClient(application_id, transaction_service_group, message_handler)
            finally:
                cls.lock.release()
        return cls.client

    def __init__(self, application_id, transaction_service_group, message_handler):
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        self.futures = {}
        self.channel_manager = ChannelManager(self)

        super(TmRemotingClient, self).__init__(self.channel_manager, self.futures, self.transaction_service_group)

        self.message_handler = message_handler
        self.message_handler.set_remote_client(self, self.futures)

        self.init()

    def init(self):
        threading.Thread(target=self.do_reconnect, args=()).start()
        self.reg_tm()

    def reg_tm(self):
        channels = self.channel_manager.get_channels()
        for channel in channels:
            request = RegisterTMRequest(self.application_id, self.transaction_service_group, None)
            response = self.send_sync_request_channel(channel, request)
            self.on_reg_response(request, response)

    def on_reg_response(self, request, response):
        if response.result:
            logger.info("tm register success. [{}]".format(request.transaction_service_group))
        else:
            logger.error("tm register failed. [{}]".format(request.transaction_service_group))
