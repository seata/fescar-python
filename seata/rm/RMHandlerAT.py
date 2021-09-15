#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import datetime

from loguru import logger

from seata.core.model.BranchType import BranchType
from seata.core.protocol.MessageType import MessageType
from seata.core.protocol.ResultCode import ResultCode
from seata.core.protocol.transaction.BranchCommitRequestResponse import BranchCommitResponse
from seata.core.protocol.transaction.BranchRollbackRequestResponse import BranchRollbackResponse
from seata.core.util.ClassUtil import ClassUtil
from seata.exception.TransactionException import TransactionException
from seata.rm.DefaultResourceManager import DefaultResourceManager
from seata.rm.datasource.undo.UndoLogManagerFactory import UndoLogManagerFactory


class RMHandlerAT:
    LIMIT_ROWS = 3000

    def __init__(self):
        self.remote_client = None
        self.futures = None

    def set_remote_client(self, remote_client, futures):
        self.remote_client = remote_client
        self.futures = futures

    def process(self, rpc_message):
        msg = rpc_message.body
        msg_type = msg.get_type_code()
        # HeartbeatMessage
        if msg_type == MessageType.TYPE_HEARTBEAT_MSG:
            if not msg.ping:
                # print("received PONG")
                pass
        # tc response rm message
        # BranchCommitRequest
        elif msg_type == MessageType.TYPE_BRANCH_COMMIT:
            response = BranchCommitResponse()
            try:
                self.__do_branch_commit(msg, response)
                response.result_code = ResultCode.Success
                logger.info('commit branch xid : [{}] branch_id : [{}] branch_status : [{}]'.format(response.xid,
                                                                                                    response.branch_id,
                                                                                                    response.branch_status))
            except TransactionException as e:
                logger.error('do branch commit transaction exception error', e)
                response.result_code = ResultCode.Failed
                response.transaction_exception_code = e.code
                response.msg = str(e)
            except Exception as e:
                logger.error('do branch commit error', e)
                response.result_code = ResultCode.Failed
                response.msg = str(e)
            self.remote_client.send_async_response(rpc_message, response)
            pass
        # BranchRollbackRequest
        elif msg_type == MessageType.TYPE_BRANCH_ROLLBACK:
            response = BranchRollbackResponse()
            try:
                self.__do_branch_rollback(msg, response)
                response.result_code = ResultCode.Success
                logger.info('rollback branch xid : [{}] branch_id : [{}] : branch_status : [{}]'.format(response.xid,
                                                                                                        response.branch_id,
                                                                                                        response.branch_status))
            except TransactionException as e:
                logger.error('do branch rollback transaction exception error', e)
                response.result_code = ResultCode.Failed
                response.transaction_exception_code = e.code
                response.msg = str(e)
            except Exception as e:
                logger.error('do branch rollback error', e)
                response.result_code = ResultCode.Failed
                response.msg = str(e)
            self.remote_client.send_async_response(rpc_message, response)
            pass
        # UndoLogDeleteRequest
        elif msg_type == MessageType.TYPE_RM_DELETE_UNDOLOG:
            self.__do_undo_log_delete(msg)
            pass
        # BranchRegisterResponse
        elif msg_type == MessageType.TYPE_BRANCH_REGISTER_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('BranchRegisterResponse', self.futures.get(rpc_message.id))
                pass
        # BranchReportResponse
        elif msg_type == MessageType.TYPE_BRANCH_STATUS_REPORT_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('BranchReportResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalLockQueryResponse
        elif msg_type == MessageType.TYPE_GLOBAL_LOCK_QUERY_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('GlobalLockQueryResponse', self.futures.get(rpc_message.id))
                pass
        # RegisterRMResponse
        elif msg_type == MessageType.TYPE_REG_RM_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('RegisterRMResponse', self.futures.get(rpc_message.id))
                pass

    def __do_branch_commit(self, msg, response):
        xid = msg.xid
        branch_id = msg.branch_id
        resource_id = msg.resource_id
        application_data = msg.application_data
        logger.info(
            'branch committing : xid=[{}] branch_id=[{}] resource_id=[{}] application_data=[{}]'.format(xid, branch_id,
                                                                                                        resource_id,
                                                                                                        application_data))

        status = self.get_resource_manager().branch_commit(BranchType.AT, xid, branch_id, resource_id)
        response.xid = xid
        response.branch_id = branch_id
        response.branch_status = status

    def __do_branch_rollback(self, msg, response):
        xid = msg.xid
        branch_id = msg.branch_id
        resource_id = msg.resource_id
        application_data = ClassUtil.get_attr(msg, 'application_data')
        status = self.get_resource_manager().branch_rollback(msg.branch_type, xid, branch_id, resource_id,
                                                             application_data)
        response.xid = xid
        response.branch_id = branch_id
        response.branch_status = status

    def __do_undo_log_delete(self, msg):
        resource_manager = self.get_resource_manager()
        data_source_proxy = resource_manager.get_resource(msg.resource_id)
        if data_source_proxy is None:
            logger.error('failed get data source proxy for delete undo log on [{}]'.format(msg.resource_id))
            return
        log_created = (datetime.datetime.now() + datetime.timedelta(days=-msg.save_days)).strftime('%Y-%m-%d')
        delete_rows = 0
        cp = None
        con = None
        try:
            while True:
                try:
                    cp = data_source_proxy.connection()
                    con = cp.target_connection
                    delete_rows = UndoLogManagerFactory.get_undo_log_manager(
                        data_source_proxy.db_type).delete_undo_log_by_log_created(log_created, self.LIMIT_ROWS, con)
                    if delete_rows > 0 and not cp.get_autocommit():
                        con.commit()
                except Exception as e:
                    if delete_rows > 0 and not cp.get_autocommit():
                        con.rollback()
                    raise e
                if delete_rows != self.LIMIT_ROWS:
                    break
        except Exception as e:
            logger.error('do_undo_log_delete error', e)
        finally:
            if cp is not None:
                try:
                    cp.close()
                except Exception:
                    pass

    @classmethod
    def get_resource_manager(cls):
        return DefaultResourceManager.get().get_manager_resource(BranchType.AT)
