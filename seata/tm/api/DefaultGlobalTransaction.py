#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.context.RootContext import RootContext
from seata.core.model.GlobalStatus import GlobalStatus
from seata.tm.DefaultTransactionManager import DefaultTransactionManager
from seata.tm.api.GlobalTransaction import GlobalTransaction
from seata.tm.api.GlobalTransactionRole import GlobalTransactionRole


class DefaultGlobalTransaction(GlobalTransaction):
    def __init__(self, xid=None, status=GlobalStatus.UnKnown, role=GlobalTransactionRole.Launcher):
        self.transaction_manager = DefaultTransactionManager()
        self.xid = xid
        self.status = status
        self.role = role

    def begin(self, timeout=60000, name="default"):
        if self.role != GlobalTransactionRole.Launcher:
            self.__assert_xid_not_null()
            print('ignore begin, involved in global transaction xid : [{}]'.format(self.xid))
            return
        self.__assert_xid_null()
        current_xid = RootContext.get_xid()
        if current_xid is not None:
            raise ValueError("Global transaction already exists, "
                             "can't begin a new global transaction, currentXid = {}".format(self.xid))
        self.xid = self.transaction_manager.begin(None, None, name, timeout)
        self.status = GlobalStatus.Begin
        RootContext.bind(self.xid)
        print('begin new global transaction [{}]'.format(self.xid))

    def commit(self):
        if self.role == GlobalTransactionRole.Participant:
            print('ignore commit, involved in global transaction xid : [{}]'.format(self.xid))
            return
        self.__assert_xid_not_null()
        self.status = self.transaction_manager.commit(self.xid)
        print('commit global transaction [{}] [{}]'.format(self.xid, self.status))

    def rollback(self):
        if self.role == GlobalTransactionRole.Participant:
            print('ignore rollback, involved in global transaction xid : [{}]'.format(self.xid))
            return
        self.__assert_xid_not_null()
        self.status = self.transaction_manager.rollback(self.xid)
        print('rollback global transaction [{}] [{}]'.format(self.xid, self.status))

    def get_status(self):
        if self.xid is None:
            return GlobalStatus.UnKnown
        return self.transaction_manager.get_status(self.xid)

    def get_xid(self):
        return self.xid

    def global_report(self, global_status):
        self.__assert_xid_not_null()
        if global_status is None:
            raise ValueError('global status is null')
        self.status = self.transaction_manager.global_report(self.xid, global_status)
        print('report global transaction [{}] [{}]'.format(self.xid, global_status))

    def __assert_xid_null(self):
        if self.xid is not None:
            raise ValueError('xid is not null [{}]'.format(self.xid))

    def __assert_xid_not_null(self):
        if self.xid is None:
            raise ValueError('xid is null')