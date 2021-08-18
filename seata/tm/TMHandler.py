#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.protocol.MessageType import MessageType


class TMHandler:

    def __init__(self):
        self.remote_client = None
        self.req_msg_map = None

    def set_remote_client(self, remote_client):
        self.remote_client = remote_client
        self.req_msg_map = self.remote_client.req_msg_map

    def process(self, rpc_message):
        msg = rpc_message.body
        msg_type = msg.get_type_code()
        # HeartbeatMessage
        if msg_type == MessageType.TYPE_HEARTBEAT_MSG:
            if not msg.ping:
                # print("received PONG")
                pass
        # tc response tm message
        # MergeResultMessage
        elif msg_type == MessageType.TYPE_SEATA_MERGE_RESULT:
            print('warn message type : [{}]'.format(msg_type))
            pass

        # RegisterTMResponse
        elif msg_type == MessageType.TYPE_REG_CLT_RESULT:
            if self.req_msg_map.get(rpc_message.id, None) == -1:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass

        # GlobalBeginResponse
        elif msg_type == MessageType.TYPE_GLOBAL_BEGIN_RESULT:
            if self.req_msg_map.get(rpc_message.id, None) == -1:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # GlobalCommitResponse
        elif msg_type == MessageType.TYPE_GLOBAL_COMMIT_RESULT:
            if self.req_msg_map.get(rpc_message.id, None) == -1:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # GlobalReportResponse
        elif msg_type == MessageType.TYPE_GLOBAL_REPORT_RESULT:
            if self.req_msg_map.get(rpc_message.id, None) == -1:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # GlobalRollbackResponse
        elif msg_type == MessageType.TYPE_GLOBAL_ROLLBACK_RESULT:
            if self.req_msg_map.get(rpc_message.id, None) == -1:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # GlobalStatusResponse
        elif msg_type == MessageType.TYPE_GLOBAL_STATUS_RESULT:
            if self.req_msg_map.get(rpc_message.id, None) == -1:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
        # RegisterTMResponse
        elif msg_type == MessageType.TYPE_REG_CLT_RESULT:
            if self.req_msg_map.get(rpc_message.id, None) == -1:
                self.req_msg_map[rpc_message.id] = msg
            else:
                pass
