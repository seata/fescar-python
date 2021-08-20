#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.context.RootContext import RootContext
from seata.core.model.GlobalStatus import GlobalStatus
from seata.tm.api.DefaultGlobalTransaction import DefaultGlobalTransaction
from seata.tm.api.GlobalTransactionRole import GlobalTransactionRole


class GlobalTransactionContext:

    @classmethod
    def create_new(cls):
        return DefaultGlobalTransaction()

    @classmethod
    def get_current(cls):
        xid = RootContext.get_xid()
        if xid is None:
            return None
        return DefaultGlobalTransaction(xid, GlobalStatus.Begin, GlobalTransactionRole.Participant)

    @classmethod
    def get_current_or_create(cls):
        tx = cls.get_current()
        if tx is None:
            return cls.create_new()
        return tx

    @classmethod
    def reload(cls, xid):
        tx = DefaultGlobalTransaction(xid, GlobalStatus.UnKnown, GlobalTransactionRole.Launcher)
        tx.begin = lambda timeout, name: (_ for _ in ()).throw(Exception('never begin on a reload global transaction.'))
        return tx
