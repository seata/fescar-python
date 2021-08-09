#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.protocol.MessageType import MessageType
from seata.core.protocol.MessageTypeAware import MessageTypeAware


class GlobalRollbackRequest(MessageTypeAware):

    def __int__(self):
        self.xid = None
        self.extra_data = None

    def get_type_code(self):
        return MessageType.TYPE_GLOBAL_ROLLBACK


class GlobalRollbackResponse(MessageTypeAware):

    def __init__(self):
        self.global_status = None

        self.transaction_exception_code = None
        self.result_code = None
        self.msg = None

    def get_type_code(self):
        return MessageType.TYPE_GLOBAL_ROLLBACK_RESULT
