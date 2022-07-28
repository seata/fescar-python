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
import time

from seata.core.protocol.RegisterTMRequestResponse import RegisterTMRequest
from seata.core.rpc.v1.TmRemotingClient import TmRemotingClient


class TMClient(object):
    client = None
    lock = threading.RLock()

    @classmethod
    def get(cls, application_id=None, transaction_service_group=None):
        if cls.client is None:
            try:
                cls.lock.acquire()
                if cls.client is None:
                    cls.client = TMClient(application_id, transaction_service_group)
            finally:
                cls.lock.release()
        return cls.client

    def __init__(self, application_id=None, transaction_service_group=None):
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        self.remote_client = None

    def init_client(self):
        # 程序启动
        from seata.tm.TMHandler import TMHandler
        message_handler = TMHandler()
        self.remote_client = TmRemotingClient.get_client(self.application_id, self.transaction_service_group,
                                                         message_handler)
