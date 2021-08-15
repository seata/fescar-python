#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.TransactionException import TransactionException


class TmTransactionException(TransactionException):

    def __init__(self, code, message=None, cause=None):
        self.code = code
        self.message = message
        self.cause = cause