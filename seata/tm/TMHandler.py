#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.protocol.MessageType import MessageType


class TMHandler:
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
        # tc response tm message
        # MergeResultMessage
        elif msg_type == MessageType.TYPE_SEATA_MERGE_RESULT:
            print('warn message type : [{}]'.format(msg_type))
            pass
        # RegisterTMResponse
        elif msg_type == MessageType.TYPE_REG_CLT_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                print('RegisterTMResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalBeginResponse
        elif msg_type == MessageType.TYPE_GLOBAL_BEGIN_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                print('GlobalBeginResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalCommitResponse
        elif msg_type == MessageType.TYPE_GLOBAL_COMMIT_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                print('GlobalCommitResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalReportResponse
        elif msg_type == MessageType.TYPE_GLOBAL_REPORT_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                print('GlobalReportResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalRollbackResponse
        elif msg_type == MessageType.TYPE_GLOBAL_ROLLBACK_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                print('GlobalRollbackResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalStatusResponse
        elif msg_type == MessageType.TYPE_GLOBAL_STATUS_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                print('GlobalStatusResponse', self.futures.get(rpc_message.id))
                pass
        # RegisterTMResponse
        elif msg_type == MessageType.TYPE_REG_CLT_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                print('RegisterTMResponse', self.futures.get(rpc_message.id))
                pass
