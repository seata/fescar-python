#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import enum

from seata.core.context.RootContext import RootContext
from seata.core.model.GlobalStatus import GlobalStatus
from seata.core.protocol.ResultCode import ResultCode
from seata.core.protocol.transaction.GlobalBeginRequestResponse import GlobalBeginRequest
from seata.core.protocol.transaction.GlobalCommitRequestResponse import GlobalCommitRequest
from seata.core.protocol.transaction.GlobalReportRequestResponse import GlobalReportRequest
from seata.core.protocol.transaction.GlobalRollbackRequestResponse import GlobalRollbackRequest
from seata.core.protocol.transaction.GlobalStatusRequestResponse import GlobalStatusRequest
from seata.exception.TmTransactionException import TmTransactionException
from seata.exception.TransactionExceptionCode import TransactionExceptionCode
from seata.tm.TMClient import TMClient


class GlobalTransactionRole(enum.Enum):
    Launcher = 0
    Participant = 1


class GlobalTransaction:
    def begin(self, timeout=None, name="default"):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    def suspend(self):
        pass

    def resume(self, suspend_resource_holder):
        pass

    def get_status(self):
        pass

    def get_xid(self):
        pass

    def global_report(self, global_status):
        pass

    def get_local_status(self):
        pass


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


class DefaultTransactionManager:
    def begin(self, application_id, transaction_service_group, name, timeout):
        req = GlobalBeginRequest()
        req.transaction_name = name
        req.timeout = timeout
        response = self.__sync_call(req)
        if response.result_code == ResultCode.Failed:
            raise TmTransactionException(TransactionExceptionCode.BeginFailed, response.msg)
        return response.xid

    def commit(self, xid):
        req = GlobalCommitRequest()
        req.xid = xid
        response = self.__sync_call(req)
        return response.global_status

    def rollback(self, xid):
        req = GlobalRollbackRequest()
        req.xid = xid
        response = self.__sync_call(req)
        return response.global_status

    def get_status(self, xid):
        request = GlobalStatusRequest()
        request.xid = xid
        response = self.__sync_call(request)
        return response.global_status

    def global_report(self, xid, global_status):
        req = GlobalReportRequest()
        req.xid = xid
        req.global_status = global_status
        response = self.__sync_call(req)
        return response.global_status

    def __sync_call(self, request):
        return TMClient.get().send_sync_request(request)
