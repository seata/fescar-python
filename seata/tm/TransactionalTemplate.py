#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from functools import wraps

from seata.core.model.GlobalStatus import GlobalStatus
from seata.exception.TransactionException import TransactionException
from seata.tm.api.GlobalTransactionContext import GlobalTransactionContext
from seata.tm.api.TransactionalExecutor import TransactionalExecutor


def GlobalTransactional(timeout=60000, name=""):
    def c(func):
        @wraps(func)
        def b(*args, **kwargs):
            tx_info = TransactionInfo()
            tx_info.timeout = timeout
            tx_info.name = name
            return TransactionalTemplate.execute(tx_info, func, *args, **kwargs)

        return b

    return c


class TransactionInfo:
    def __init__(self, timeout=None, name=None):
        self.timeout = timeout
        self.name = name


class TransactionalTemplate:

    @classmethod
    def execute(cls, tx_info, func, *args, **kwargs):
        # get current transaction, if null, the tx role is GlobalTransactionRole.Participant
        tx = GlobalTransactionContext.get_current()
        # if tx is null, create new transaction with role GlobalTransactionRole.Launcher
        if tx is None:
            tx = GlobalTransactionContext.create_new()
        try:
            # if role is GlobalTransactionRole.Launcher begin
            cls.begin_transaction(tx_info, tx)
            result = None
            try:
                # execute business
                result = func(*args, **kwargs)
            except Exception as e:
                # need business throw exception rollback
                cls.complete_transaction_after_throwing(tx_info, tx, e)
                raise e
            # commit
            cls.commit_transaction(tx)
            return result
        finally:
            pass

    @classmethod
    def begin_transaction(cls, tx_info, tx):
        try:
            tx.begin(tx_info.timeout, tx_info.name)
        except TransactionException as e:
            raise TransactionalExecutor.ExecutionException(tx, e, TransactionalExecutor.Code.BeginFailure, None)

    @classmethod
    def complete_transaction_after_throwing(cls, tx_info, tx, exception):
        if isinstance(exception, RuntimeError):
            try:
                cls.rollback_transaction(tx, exception)
            except TransactionException as e:
                raise TransactionalExecutor.ExecutionException(tx, e, TransactionalExecutor.Code.RollbackFailure,
                                                               exception)
        else:
            cls.commit_transaction(tx)

    @classmethod
    def rollback_transaction(cls, tx, exception):
        tx.rollback()
        if GlobalStatus.RollbackRetrying == tx.status:
            raise TransactionalExecutor.ExecutionException(tx, None, TransactionalExecutor.Code.RollbackRetrying,
                                                           exception)
        else:
            raise TransactionalExecutor.ExecutionException(tx, None, TransactionalExecutor.Code.RollbackDone,
                                                           exception)

    @classmethod
    def commit_transaction(cls, tx):
        try:
            tx.commit()
        except TransactionException as e:
            raise TransactionalExecutor.ExecutionException(tx, e, TransactionalExecutor.Code.CommitFailure, None)
