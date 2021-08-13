#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class TransactionException(Exception):

    def __init__(self, code, message=None, cause=None):
        self.code = code
        self.message = message
        self.cause = cause


class BranchTransactionException(TransactionException):

    def __init__(self, code, message=None, cause=None):
        super(BranchTransactionException, self).__init__(code, message, cause)
