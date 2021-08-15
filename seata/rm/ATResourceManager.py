#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.context.RootContext import RootContext
from seata.core.model.BranchStatus import BranchStatus
from seata.core.protocol.RegisterRMRequestResponse import RegisterRMRequest
from seata.core.protocol.ResultCode import ResultCode
from seata.core.protocol.transaction.BranchRegisterRequestResponse import BranchRegisterRequest
from seata.core.protocol.transaction.BranchReportRequestResponse import BranchReportRequest
from seata.core.protocol.transaction.GlobalLockQueryRequestResponse import GlobalLockQueryRequest
from seata.exception.RmTransactionException import RmTransactionException
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.exception.TransactionException import TransactionException
from seata.exception.TransactionExceptionCode import TransactionExceptionCode
from seata.rm.RMClient import RMClient
from seata.rm.datasource.undo.UndoLogManagerFactory import UndoLogManagerFactory

manager = None


class ATResourceManager(object):

    def __init__(self):
        self.pool_db_proxy_cache = dict()
        pass

    @staticmethod
    def get():
        global manager
        if manager is None:
            manager = ATResourceManager()
        return manager

    def register_resource(self, pooled_db_proxy):
        from seata.rm.datasource.PooledDBProxy import PooledDBProxy
        if not isinstance(pooled_db_proxy, PooledDBProxy):
            raise TypeError("Register resource type error.")
        self.pool_db_proxy_cache[pooled_db_proxy.get_resource_id()] = pooled_db_proxy
        request = RegisterRMRequest()
        request.transaction_service_group = RMClient.get().transaction_service_group
        request.application_id = RMClient.get().application_id
        RMClient.get().send_sync_request(request)

    def lock_query(self, branch_type, resource_id, xid, lock_keys):
        try:
            request = GlobalLockQueryRequest()
            request.xid = xid
            request.lock_key = lock_keys
            request.resource_id = resource_id
            if RootContext.in_global_transaction() or RootContext.require_global_lock():
                response = RMClient.get().send_sync_request(request)
            else:
                raise RuntimeError("unknow situation!")
            if response.result_code == ResultCode.Failed:
                raise TransactionException(response.transaction_exception_code, "Response[{}]".format(response.msg))
            return response.lockable
        except TimeoutError as e:
            raise RmTransactionException(TransactionExceptionCode.IO, "RPC Timeout", e)
        except RuntimeError as e:
            raise RmTransactionException(TransactionExceptionCode.BranchReportFailed, "Runtime", e)

    def branch_register(self, branch_type, resource_id, client_id, xid, application_data, lock_keys):
        try:
            request = BranchRegisterRequest()
            request.xid = xid
            request.branch_type = branch_type
            request.resource_id = resource_id
            request.lock_key = lock_keys
            request.application_data = application_data
            response = RMClient.get().send_sync_request(request)
            if response.result_code == ResultCode.Failed:
                raise RmTransactionException("response {} {}".format(response.transaction_exception_code, response.msg))
            return response.branch_id
        except TimeoutError as e:
            raise RmTransactionException(TransactionExceptionCode.IO, "RPC Timeout", e)
        except RuntimeError as e:
            raise RmTransactionException(TransactionExceptionCode.BranchReportFailed, "Runtime", e)

    def branch_report(self, branch_type, xid, branch_id, status, application_data):
        try:
            request = BranchReportRequest()
            request.xid = xid
            request.branch_id = branch_id
            request.branch_type = branch_type
            request.status = status
            request.application_data = application_data
            response = RMClient.get().send_sync_request(request)
            if response.result_code == ResultCode.Failed:
                raise RmTransactionException(response.transaction_exception_code, "response [{}]".format(response.msg))
        except TimeoutError as e:
            raise RmTransactionException(TransactionExceptionCode.IO, "RPC Timeout", e)
        except RuntimeError as e:
            raise RmTransactionException(TransactionExceptionCode.BranchReportFailed, "Runtime", e)

    def branch_rollback(self, branch_type, xid, branch_id, resource_id, application_data):
        pool_db_proxy = self.pool_db_proxy_cache.get(resource_id)
        if pool_db_proxy is None:
            raise ShouldNeverHappenException()
        try:
            UndoLogManagerFactory.get_undo_log_manager(pool_db_proxy.get_db_type()).undo(pool_db_proxy, xid, branch_id)
        except TransactionException as e:
            print("branchRollback failed. branch_type:[{}], xid:[{}], branch_id:[{}], resource_id:[{}], "
                  "application_data:[{}], reason:[{}]".format(branch_type, xid, branch_id, resource_id,
                                                              application_data, e.message))
            if e.code == TransactionExceptionCode.BranchRollbackFailed_Unretriable:
                return BranchStatus.PhaseTwo_RollbackFailed_Unretryable
            else:
                return BranchStatus.PhaseTwo_RollbackFailed_Retryable
        return BranchStatus.PhaseTwo_Rollbacked
