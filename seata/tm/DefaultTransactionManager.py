#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.protocol.ResultCode import ResultCode
from seata.core.protocol.transaction.GlobalBeginRequestResponse import GlobalBeginRequest
from seata.core.protocol.transaction.GlobalCommitRequestResponse import GlobalCommitRequest
from seata.core.protocol.transaction.GlobalReportRequestResponse import GlobalReportRequest
from seata.core.protocol.transaction.GlobalRollbackRequestResponse import GlobalRollbackRequest
from seata.core.protocol.transaction.GlobalStatusRequestResponse import GlobalStatusRequest
from seata.exception.TmTransactionException import TmTransactionException
from seata.exception.TransactionExceptionCode import TransactionExceptionCode


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
        from seata.core.rpc.v1.TmRemotingClient import TmRemotingClient
        return TmRemotingClient.get_client().send_sync_request(request)
