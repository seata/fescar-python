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

from seata.rm.RMClient import RMClient
from seata.tm.TMClient import TMClient
from seata.config.Config import ConfigFactory


class GlobalTransactionScanner:
    _init = False

    def __init__(self):
        config = ConfigFactory.get_config()
        self.application_id = config.get('application-id')
        self.transaction_service_group = config.get('tx-service-group')
        if not self._init:
            self._init = True
            self._init_client()

    def _init_client(self):
        tm = TMClient.get(self.application_id, self.transaction_service_group)
        tm.init_client()

        rm = RMClient.get(self.application_id, self.transaction_service_group)
        rm.init_client()
