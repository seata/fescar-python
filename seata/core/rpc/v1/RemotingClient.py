#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import datetime
import time

from gevent import monkey

monkey.patch_socket()

from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.protocol.ProtocolConstants import ProtocolConstants
from seata.core.protocol.RpcMessage import RpcMessage
from seata.core.protocol.transaction.BranchCommitRequestResponse import BranchCommitResponse
from seata.core.protocol.transaction.BranchRollbackRequestResponse import BranchRollbackResponse
from seata.rm.ATResourceManager import ATResourceManager
from seata.rm.datasource.undo.UndoLogManagerFactory import UndoLogManagerFactory

from seata.core.protocol.MessageType import MessageType

from seata.core.rpc.v1.ProtocolV1 import ProtocolV1

import gevent
import socket


class DefaultHandler:
    LIMIT_ROWS = 3000

    def __init__(self, remote_client):
        self.remote_client = remote_client
        self.req_msg_map = self.remote_client.req_msg_map

    def process(self, rpc_message):
        msg = rpc_message.body
        msg_type = msg.get_type_code()
        print('msg type :', msg_type)
        # tc response tm message
        # HeartbeatMessage
        if msg_type == MessageType.TYPE_HEARTBEAT_MSG:
            if not msg.ping:
                print("received PONG")
        # MergeResultMessage
        elif msg_type == MessageType.TYPE_SEATA_MERGE_RESULT:
            print('warn message type : [{}]'.format(msg_type))
            pass
        # RegisterTMResponse
        elif msg_type == MessageType.TYPE_REG_CLT_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # GlobalBeginResponse
        elif msg_type == MessageType.TYPE_GLOBAL_BEGIN_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # GlobalCommitResponse
        elif msg_type == MessageType.TYPE_GLOBAL_COMMIT_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # GlobalReportResponse
        elif msg_type == MessageType.TYPE_GLOBAL_REPORT_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # GlobalRollbackResponse
        elif msg_type == MessageType.TYPE_GLOBAL_ROLLBACK_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # GlobalStatusResponse
        elif msg_type == MessageType.TYPE_GLOBAL_STATUS_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # RegisterTMResponse
        elif msg_type == MessageType.TYPE_REG_CLT_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # tc response rm message
        # BranchCommitRequest
        elif msg_type == MessageType.TYPE_BRANCH_COMMIT:
            response = BranchCommitResponse()
            self.__do_branch_commit(msg, response)
            self.remote_client.send_async_response(rpc_message, response)
            pass
        # BranchRollbackRequest
        elif msg_type == MessageType.TYPE_BRANCH_ROLLBACK:
            response = BranchRollbackResponse()
            self.__do_branch_rollback(msg, response)
            self.remote_client.send_async_response(rpc_message, response)
            pass
        # UndoLogDeleteRequest
        elif msg_type == MessageType.TYPE_RM_DELETE_UNDOLOG:
            self.__do_undo_log_delete(msg)
            pass
        # BranchRegisterResponse
        elif msg_type == MessageType.TYPE_BRANCH_REGISTER_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # BranchReportResponse
        elif msg_type == MessageType.TYPE_BRANCH_STATUS_REPORT_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # GlobalLockQueryResponse
        elif msg_type == MessageType.TYPE_GLOBAL_LOCK_QUERY_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # RegisterRMResponse
        elif msg_type == MessageType.TYPE_REG_RM_RESULT:
            if self.req_msg_map.get(msg_type, None) is not None:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass

    def __do_branch_commit(self, msg, response):
        xid = msg.xid
        branch_id = msg.branch_id
        resource_id = msg.resource_id
        application_data = msg.application_data
        print('branch committing : xid={} branch_id={} resource_id={} application_data={}'.format(xid, branch_id,
                                                                                                  resource_id,
                                                                                                  application_data))

        status = self.get_resource_manager().branch_commit(xid, branch_id, resource_id)
        response.xid = xid
        response.branch_id = branch_id
        response.branch_status = status

    def __do_branch_rollback(self, msg, response):
        xid = msg.xid
        branch_id = msg.branch_id
        resource_id = msg.resource_id
        application_data = msg.application_data
        status = self.get_resource_manager().branch_rollback(msg.branch_type, xid, branch_id, resource_id,
                                                             application_data)
        response.xid = xid
        response.branch_id = branch_id
        response.branch_status = status

    def __do_undo_log_delete(self, msg):
        resource_manager = self.get_resource_manager()
        pooled_db_proxy = resource_manager.get(msg.resource_id)
        if pooled_db_proxy is None:
            print('failed get pooled db proxy for delete undolog on {}', msg.resource_id)
            return
        log_created = (datetime.datetime.now() + datetime.timedelta(days=-msg.save_days)).strftime('%Y-%m-%d')
        delete_rows = 0
        cp = None
        con = None
        try:
            while True:
                try:
                    cp = pooled_db_proxy.connection()
                    con = cp.target_connection
                    delete_rows = UndoLogManagerFactory.get_undo_log_manager(
                        pooled_db_proxy.db_type).delete_undo_log_by_log_created(log_created, self.LIMIT_ROWS, con)
                    if delete_rows > 0 and not cp.get_autocommit():
                        con.commit()
                except Exception as e:
                    if delete_rows > 0 and not cp.get_autocommit():
                        con.rollback()
                    raise e
                if delete_rows != self.LIMIT_ROWS:
                    break
        except Exception as e:
            print('do_undo_log_delete error', e)
        finally:
            if cp is not None:
                try:
                    cp.close()
                except Exception:
                    pass

    @classmethod
    def get_resource_manager(cls):
        return ATResourceManager.get()


class RemotingClient:
    def __init__(self, host, port):
        # key: rpc_message.id value: rpc_message.body
        self.req_msg_map = {}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        self.sock.connect((host, port))
        self.message_handler = DefaultHandler(self)
        self.protocol = ProtocolV1(self.sock, self.message_handler)

    def get_socket(self):
        return self.sock

    def send_sync_request(self, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)

        self.protocol.encode(rpc_message)

        self.req_msg_map[rpc_message.id] = None
        timeout = 0
        while self.req_msg_map[rpc_message.id] is None and timeout <= 30:
            timeout += 0.01
            time.sleep(0.01)
        response = self.req_msg_map[rpc_message.id]
        if response is None and timeout > 30:
            raise TimeoutError()
        self.req_msg_map.pop(rpc_message.id, None)
        return response

    def send_async_request(self, msg):
        if isinstance(msg, HeartbeatMessage):
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST)
        else:
            rpc_message = RpcMessage.build_request_message(msg, ProtocolConstants.MSGTYPE_RESQUEST_SYNC)

        self.protocol.encode(rpc_message)

    def send_async_response(self, rpc_message, msg):
        rpc_msg = self.__build_response_message(rpc_message, msg, ProtocolConstants.MSGTYPE_RESPONSE)
        self.protocol.encode(rpc_msg)

    def __build_response_message(self, rpc_message, msg, message_type):
        rpc_msg = RpcMessage()
        rpc_msg.message_type = message_type
        rpc_msg.codec = rpc_message.codec
        rpc_msg.compressor = rpc_message.compressor
        rpc_msg.body = msg
        rpc_msg.id = rpc_message.id
        return rpc_msg
