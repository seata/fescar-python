#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
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
