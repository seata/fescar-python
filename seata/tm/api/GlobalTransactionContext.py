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

from seata.core.context.RootContext import RootContext
from seata.core.model.GlobalStatus import GlobalStatus
from seata.tm.api.DefaultGlobalTransaction import DefaultGlobalTransaction
from seata.tm.api.GlobalTransactionRole import GlobalTransactionRole


class GlobalTransactionContext:

    @classmethod
    def create_new(cls):
        return DefaultGlobalTransaction()

    @classmethod
    def get_current(cls):
        xid = RootContext.get_xid()
        if xid is None:
            return None
        return DefaultGlobalTransaction(xid, GlobalStatus.Begin, GlobalTransactionRole.Participant)

    @classmethod
    def get_current_or_create(cls):
        tx = cls.get_current()
        if tx is None:
            return cls.create_new()
        return tx

    @classmethod
    def reload(cls, xid):
        tx = DefaultGlobalTransaction(xid, GlobalStatus.UnKnown, GlobalTransactionRole.Launcher)
        tx.begin = lambda timeout, name: (_ for _ in ()).throw(Exception('never begin on a reload global transaction.'))
        return tx
