#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.protocol.MessageType import MessageType
from seata.core.protocol.MessageTypeAware import MessageTypeAware, ResultMessage
from seata.exception.TransactionExceptionCode import TransactionExceptionCode


class GlobalBeginRequest(MessageTypeAware):

    def __int__(self):
        self.timeout = 60000
        self.transaction_name = None

    def get_type_code(self):
        return MessageType.TYPE_GLOBAL_BEGIN


class GlobalBeginResponse(ResultMessage, MessageTypeAware):

    def __init__(self):
        super(GlobalBeginResponse, self).__init__()
        self.xid = None
        self.extra_data = None

        self.transaction_exception_code = TransactionExceptionCode.Unknown
        self.result_code = None
        self.msg = None

    def get_type_code(self):
        return MessageType.TYPE_GLOBAL_BEGIN_RESULT
