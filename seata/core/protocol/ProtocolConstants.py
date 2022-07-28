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


class ProtocolConstants(object):
    # Magic code
    MAGIC_CODE_BYTES = bytearray([0xda, 0xda])
    # Protocol version
    VERSION = 1
    # Max frame length
    MAX_FRAME_LENGTH = 8 * 1024 * 1024
    # HEAD_LENGTH of protocol v1
    V1_HEAD_LENGTH = 16
    # Message type: Request
    MSGTYPE_RESQUEST_SYNC = 0
    # Message type: Response
    MSGTYPE_RESPONSE = 1
    # Message type: Request which no need response
    MSGTYPE_RESQUEST_ONEWAY = 2
    #  Message type: Heartbeat Request
    MSGTYPE_HEARTBEAT_REQUEST = 3
    # Message type: Heartbeat Response
    MSGTYPE_HEARTBEAT_RESPONSE = 4
