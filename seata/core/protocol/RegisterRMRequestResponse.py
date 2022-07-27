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

from seata.core.protocol import Version
from seata.core.protocol.MessageType import MessageType
from seata.core.protocol.MessageTypeAware import MessageTypeAware, ResultMessage


class RegisterRMRequest(MessageTypeAware):

    def __init__(self, application_id=None, transaction_service_group=None, extra_data=None):
        self.version = Version.CURRENT
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        self.extra_data = extra_data

        self.resource_ids = None

    def get_type_code(self):
        return MessageType.TYPE_REG_RM


class RegisterRMResponse(ResultMessage, MessageTypeAware):

    def __init__(self, result=True):
        super(RegisterRMResponse, self).__init__()
        self.result = result

        self.version = Version.CURRENT
        self.identified = result
        self.extra_data = None

    def get_type_code(self):
        return MessageType.TYPE_REG_RM_RESULT
