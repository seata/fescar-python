#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import enum


class TransactionalExecutor:
    class ExecutionException(Exception):

        def __init__(self, tx, cause, code, origin_exception):
            self.tx = tx
            self.cause = cause
            self.code = code
            self.origin_exception = origin_exception

        def __str__(self):
            return 'globalStatus={}, cause={}, code={}, origin_exception={}'.format(
                self.tx.status, self.cause, self.code, self.origin_exception)

        def __repr__(self):
            return self.__str__()

    class Code(enum.Enum):
        BeginFailure = 0
        CommitFailure = 1
        RollbackFailure = 2
        RollbackDone = 3
        ReportFailure = 4
        RollbackRetrying = 5
