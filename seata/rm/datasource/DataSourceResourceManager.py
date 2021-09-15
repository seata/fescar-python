#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from loguru import logger

from seata.core.context.RootContext import RootContext
from seata.core.model.BranchStatus import BranchStatus
from seata.core.model.BranchType import BranchType
from seata.core.protocol.ResultCode import ResultCode
from seata.core.protocol.transaction.BranchRegisterRequestResponse import BranchRegisterRequest
from seata.core.protocol.transaction.BranchReportRequestResponse import BranchReportRequest
from seata.core.protocol.transaction.GlobalLockQueryRequestResponse import GlobalLockQueryRequest
from seata.exception.RmTransactionException import RmTransactionException
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.exception.TransactionException import TransactionException
from seata.exception.TransactionExceptionCode import TransactionExceptionCode
from seata.rm.datasource.AsyncWorker import AsyncWorker, Phase2Context
from seata.rm.datasource.undo.UndoLogManagerFactory import UndoLogManagerFactory


class DataSourceResourceManager(object):
    manager = None

    def __init__(self):
        self.data_source_proxy_cache = dict()
        self.async_work = AsyncWorker(self)
        pass

    @classmethod
    def get(cls):
        if cls.manager is None:
            cls.manager = DataSourceResourceManager()
        return cls.manager

    def register_resource(self, data_source_proxy):
        from seata.rm.datasource.DataSourceProxy import DataSourceProxy
        if not isinstance(data_source_proxy, DataSourceProxy):
            raise TypeError("Register resource type error.")
        self.data_source_proxy_cache[data_source_proxy.get_resource_id()] = data_source_proxy

        from seata.core.rpc.v1.RmRemotingClient import RmRemotingClient
        RmRemotingClient.get_client().register_resource(data_source_proxy.resource_group_id,
                                                        data_source_proxy.get_resource_id())

    def get_resource(self, resource_id):
        return self.data_source_proxy_cache.get(resource_id, None)

    def get_manager_resources(self):
        return self.data_source_proxy_cache

    def get_branch_type(self):
        return BranchType.AT

    def lock_query(self, branch_type, resource_id, xid, lock_keys):
        try:
            request = GlobalLockQueryRequest()
            request.xid = xid
            request.branch_type = branch_type
            request.lock_key = lock_keys
            request.resource_id = resource_id

            from seata.core.rpc.v1.RmRemotingClient import RmRemotingClient
            if RootContext.in_global_transaction() or RootContext.require_global_lock():
                response = RmRemotingClient.get_client().send_sync_request(request)
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
            from seata.core.rpc.v1.RmRemotingClient import RmRemotingClient
            response = RmRemotingClient.get_client().send_sync_request(request)
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
            from seata.core.rpc.v1.RmRemotingClient import RmRemotingClient
            response = RmRemotingClient.get_client().send_sync_request(request)
            if response.result_code == ResultCode.Failed:
                raise RmTransactionException(response.transaction_exception_code, "response [{}]".format(response.msg))
        except TimeoutError as e:
            raise RmTransactionException(TransactionExceptionCode.IO, "RPC Timeout", e)
        except RuntimeError as e:
            raise RmTransactionException(TransactionExceptionCode.BranchReportFailed, "Runtime", e)

    def branch_rollback(self, branch_type, xid, branch_id, resource_id, application_data):
        data_source_proxy = self.data_source_proxy_cache.get(resource_id)
        if data_source_proxy is None:
            raise ShouldNeverHappenException()
        try:
            UndoLogManagerFactory.get_undo_log_manager(data_source_proxy.db_type).undo(data_source_proxy, xid,
                                                                                       branch_id)
        except TransactionException as e:
            logger.error("branchRollback failed. branch_type:[{}], xid:[{}], branch_id:[{}], resource_id:[{}], "
                         "application_data:[{}], reason:[{}]".format(branch_type, xid, branch_id, resource_id,
                                                                     application_data, e.message))
            if e.code == TransactionExceptionCode.BranchRollbackFailed_Unretriable:
                return BranchStatus.PhaseTwo_RollbackFailed_Unretryable
            else:
                return BranchStatus.PhaseTwo_RollbackFailed_Retryable
        return BranchStatus.PhaseTwo_Rollbacked

    def branch_commit(self, branch_type, xid, branch_id, resource_id):
        context = Phase2Context(xid, branch_id, resource_id)
        self.async_work.add_context(context)
        return BranchStatus.PhaseTwo_Committed
