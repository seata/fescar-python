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

from seata.rm.datasource.undo.UndoExecutorHolder import UndoExecutorHolder
from seata.rm.datasource.undo.mysql.MySQLUndoDeleteExecutor import MySQLUndoDeleteExecutor
from seata.rm.datasource.undo.mysql.MySQLUndoInsertExecutor import MySQLUndoInsertExecutor
from seata.rm.datasource.undo.mysql.MySQLUndoUpdateExecutor import MySQLUndoUpdateExecutor


class MySQLUndoExecutorHolder(UndoExecutorHolder):
    def get_insert_executor(self, sql_undo_log):
        return MySQLUndoInsertExecutor(sql_undo_log)

    def get_update_executor(self, sql_undo_log):
        return MySQLUndoUpdateExecutor(sql_undo_log)

    def get_delete_executor(self, sql_undo_log):
        return MySQLUndoDeleteExecutor(sql_undo_log)