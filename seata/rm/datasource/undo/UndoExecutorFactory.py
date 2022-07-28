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

from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException

from seata.sqlparser.SQLType import SQLType


class UndoExecutorFactory:
    @classmethod
    def get_undo_executor(cls, db_type, sql_undo_log):
        from seata.rm.datasource.undo.UndoExecutorHolderFactory import UndoExecutorHolderFactory
        holder = UndoExecutorHolderFactory.get_undo_executor_holder(db_type.lower())
        result = None
        sql_type = sql_undo_log.sql_type
        if sql_type == SQLType.INSERT:
            result = holder.get_insert_executor(sql_undo_log)
        elif sql_type == SQLType.UPDATE:
            result = holder.get_update_executor(sql_undo_log)
        elif sql_type == SQLType.DELETE:
            result = holder.get_delete_executor(sql_undo_log)
        else:
            raise ShouldNeverHappenException()
        return result
