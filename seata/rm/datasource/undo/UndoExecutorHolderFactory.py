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

from seata.sqlparser.util.JdbcConstants import JdbcConstants


class UndoExecutorHolderFactory:
    _HOLDER_MAP = {}

    @classmethod
    def get_undo_executor_holder(cls, db_type):
        if cls._HOLDER_MAP.get(db_type, None) is not None:
            return cls._HOLDER_MAP[db_type]
        if db_type == JdbcConstants.MYSQL:
            from seata.rm.datasource.undo.mysql.MySQLUndoExecutorHolder import MySQLUndoExecutorHolder
            cls._HOLDER_MAP[db_type] = MySQLUndoExecutorHolder()
            return cls._HOLDER_MAP[db_type]
        raise NotImplemented("db type : " + db_type)
