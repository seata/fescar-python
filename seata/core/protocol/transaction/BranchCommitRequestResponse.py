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

from seata.core.model.BranchType import BranchType
from seata.core.protocol.MessageType import MessageType
from seata.core.protocol.MessageTypeAware import MessageTypeAware, ResultMessage
from seata.exception.TransactionExceptionCode import TransactionExceptionCode


class BranchCommitRequest(MessageTypeAware):

    def __init__(self):
        self.xid = None
        self.branch_id = 0
        self.branch_type = BranchType.AT
        self.resource_id = None
        self.application_data = None

    def get_type_code(self):
        return MessageType.TYPE_BRANCH_COMMIT


class BranchCommitResponse(ResultMessage, MessageTypeAware):

    def __init__(self):
        super(BranchCommitResponse, self).__init__()
        self.xid = None
        self.branch_id = 0
        self.branch_status = None

        self.transaction_exception_code = TransactionExceptionCode.Unknown
        self.result_code = None
        self.msg = None

    def get_type_code(self):
        return MessageType.TYPE_BRANCH_COMMIT_RESULT
