#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.protocol.MessageType import MessageType
from core.protocol.MessageTypeAware import MessageTypeAware


class GlobalReportRequest(MessageTypeAware):

    def __int__(self):
        self.xid = None
        self.extra_data = None
        self.global_status = None

    def get_type_code(self):
        return MessageType.TYPE_GLOBAL_REPORT


class GlobalReportResponse(MessageTypeAware):

    def __init__(self):
        self.global_status = None

        self.transaction_exception_code = None
        self.result_code = None
        self.msg = None

    def get_type_code(self):
        return MessageType.TYPE_GLOBAL_REPORT_RESULT
