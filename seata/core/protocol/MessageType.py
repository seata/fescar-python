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


class MessageType(object):

    TYPE_GLOBAL_BEGIN = 1

    TYPE_GLOBAL_BEGIN_RESULT = 2

    TYPE_GLOBAL_COMMIT = 7

    TYPE_GLOBAL_COMMIT_RESULT = 8

    TYPE_GLOBAL_ROLLBACK = 9

    TYPE_GLOBAL_ROLLBACK_RESULT = 10

    TYPE_GLOBAL_STATUS = 15

    TYPE_GLOBAL_STATUS_RESULT = 16

    TYPE_GLOBAL_REPORT = 17

    TYPE_GLOBAL_REPORT_RESULT = 18

    TYPE_GLOBAL_LOCK_QUERY = 21

    TYPE_GLOBAL_LOCK_QUERY_RESULT = 22

    TYPE_BRANCH_COMMIT = 3

    TYPE_BRANCH_COMMIT_RESULT = 4

    TYPE_BRANCH_ROLLBACK = 5

    TYPE_BRANCH_ROLLBACK_RESULT = 6

    TYPE_BRANCH_REGISTER = 11

    TYPE_BRANCH_REGISTER_RESULT = 12

    TYPE_BRANCH_STATUS_REPORT = 13

    TYPE_BRANCH_STATUS_REPORT_RESULT = 14

    TYPE_SEATA_MERGE = 59

    TYPE_SEATA_MERGE_RESULT = 60

    TYPE_REG_CLT = 101

    TYPE_REG_CLT_RESULT = 102

    TYPE_REG_RM = 103

    TYPE_REG_RM_RESULT = 104

    TYPE_RM_DELETE_UNDOLOG = 111

    TYPE_HEARTBEAT_MSG = 120

    def __init__(self):
        pass
