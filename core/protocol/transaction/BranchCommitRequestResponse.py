#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.model.BranchType import BranchType
from core.protocol.MessageType import MessageType
from core.protocol.MessageTypeAware import MessageTypeAware


class BranchCommitRequest(MessageTypeAware):

    def __init__(self):
        self.xid = None
        self.branch_id = 0
        self.branch_type = BranchType.AT
        self.resource_id = None
        self.application_data = None

    def get_type_code(self):
        return MessageType.TYPE_BRANCH_COMMIT


class BranchCommitResponse(MessageTypeAware):

    def __init__(self):
        self.xid = None
        self.branch_id = 0
        self.branch_status = None

        self.result_code = None
        self.msg = None

    def get_type_code(self):
        return MessageType.TYPE_BRANCH_COMMIT_RESULT
