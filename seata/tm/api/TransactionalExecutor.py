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

import enum


class TransactionalExecutor:
    class ExecutionException(Exception):

        def __init__(self, tx, cause, code, origin_exception):
            self.tx = tx
            self.cause = cause
            self.code = code
            self.origin_exception = origin_exception

        def __str__(self):
            return 'globalStatus={}, cause={}, code={}, origin_exception={}'.format(
                self.tx.status, self.cause, self.code, self.origin_exception)

        def __repr__(self):
            return self.__str__()

    class Code(enum.Enum):
        BeginFailure = 0
        CommitFailure = 1
        RollbackFailure = 2
        RollbackDone = 3
        ReportFailure = 4
        RollbackRetrying = 5
