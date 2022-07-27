# -*- coding: utf-8 -*-

"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import threading

from loguru import logger

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
            logger.info("rm register success. [{}] [{}]".format(request.transaction_service_group, request.resource_ids))
        else:
            logger.error("rm register failed. [{}] [{}]".format(request.transaction_service_group, request.resource_ids))
