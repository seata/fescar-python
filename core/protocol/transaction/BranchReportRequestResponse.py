#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.model.BranchType import BranchType
from core.protocol.MessageType import MessageType
from core.protocol.MessageTypeAware import MessageTypeAware


class BranchReportRequest(MessageTypeAware):

    def __int__(self):
        self.xid = None
        self.branch_id = 0
        self.resource_id = None
        self.status = None
        self.application_data = None
        self.branch_type = BranchType.AT

    def get_type_code(self):
        return MessageType.TYPE_BRANCH_STATUS_REPORT


class BranchReportResponse(MessageTypeAware):

    def __init__(self):
        self.branch_id = 0

        self.transaction_exception_code = None
        self.result_code = None
        self.msg = None

    def get_type_code(self):
        return MessageType.TYPE_BRANCH_STATUS_REPORT_RESULT
