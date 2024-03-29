# -*- coding: utf-8 -*-

"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from loguru import logger

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
            logger.warning('warn message type : [{}]'.format(msg_type))
            pass
        # RegisterTMResponse
        elif msg_type == MessageType.TYPE_REG_CLT_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('RegisterTMResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalBeginResponse
        elif msg_type == MessageType.TYPE_GLOBAL_BEGIN_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('GlobalBeginResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalCommitResponse
        elif msg_type == MessageType.TYPE_GLOBAL_COMMIT_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('GlobalCommitResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalReportResponse
        elif msg_type == MessageType.TYPE_GLOBAL_REPORT_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('GlobalReportResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalRollbackResponse
        elif msg_type == MessageType.TYPE_GLOBAL_ROLLBACK_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('GlobalRollbackResponse', self.futures.get(rpc_message.id))
                pass
        # GlobalStatusResponse
        elif msg_type == MessageType.TYPE_GLOBAL_STATUS_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('GlobalStatusResponse', self.futures.get(rpc_message.id))
                pass
        # RegisterTMResponse
        elif msg_type == MessageType.TYPE_REG_CLT_RESULT:
            if self.futures.get(rpc_message.id, None) is not None:
                self.futures[rpc_message.id].set(msg)
            else:
                logger.info('RegisterTMResponse', self.futures.get(rpc_message.id))
                pass
