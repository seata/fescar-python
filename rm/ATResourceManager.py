#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.model.BranchType import BranchType
from core.protocol.ResultCode import ResultCode
from core.protocol.transaction.BranchRegisterRequestResponse import BranchRegisterRequest
from core.protocol.transaction.BranchReportRequestResponse import BranchReportRequest
from exception.RmTransactionException import RmTransactionException
from exception.TransactionException import TransactionException
from exception.TransactionExceptionCode import TransactionExceptionCode
from rm.RMClient import RMClient
from rm.datasource.PooledDBProxy import PooledDBProxy

manager = None


class ATResourceManager(object):

    def __init__(self):
        self.pool_db_cache = dict()
        pass

    @staticmethod
    def get():
        global manager
        if manager is None:
            manager = ATResourceManager()
        return manager

    def register_resource(self, pooled_db_proxy):
        if not isinstance(pooled_db_proxy, PooledDBProxy):
            raise ValueError("Register resource type error.")
        self.pool_db_cache.put(pooled_db_proxy.get_resource_id(), pooled_db_proxy)
        RMClient.send_request()

    def branch_register(self, branch_type, resource_id, client_id, xid, application_data, lock_keys):
        try:
            request = BranchRegisterRequest()
            request.xid = xid
            request.branch_type = branch_type
            request.resource_id = resource_id
            request.lock_key = lock_keys
            request.application_data = application_data
            response = RMClient.send_request(request)
            if response.result_code == ResultCode.Failed:
                raise RmTransactionException("response {} {}".format(response.transaction_exception_code, response.msg))
        except TimeoutError as e:
            raise RmTransactionException(TransactionExceptionCode.IO, "RPC Timeout", e)
        except RuntimeError as e:
            raise RmTransactionException(TransactionExceptionCode.BranchReportFailed, "Runtime", e)

    def branch_report(self, branch_type, xid, branch_id, status, application_data):
        try:
            request = BranchReportRequest()
            request.xid = xid
            request.branch_id = branch_id
            request.status = status
            request.application_data = application_data
            response = RMClient.send_request(request)
            if response.result_code == ResultCode.Failed:
                raise RmTransactionException(response.transaction_exception_code, "response [{}]".format(response.msg))
        except TimeoutError as e:
            raise RmTransactionException(TransactionExceptionCode.IO, "RPC Timeout", e)
        except RuntimeError as e:
            raise RmTransactionException(TransactionExceptionCode.BranchReportFailed, "Runtime", e)
