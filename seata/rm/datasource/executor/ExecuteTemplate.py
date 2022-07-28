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
from seata.core.model.BranchType import BranchType
from seata.rm.datasource.executor.PlainExecutor import PlainExecutor
from seata.rm.datasource.sql.SQLVisitorFactory import SQLVisitorFactory
from seata.rm.datasource.executor.mysql.MySQLInsertExecutor import MySQLInsertExecutor
from seata.rm.datasource.executor.mysql.MySQLDeleteExecutor import MySQLDeleteExecutor
from seata.rm.datasource.executor.mysql.MySQLUpdateExecutor import MySQLUpdateExecutor
from seata.rm.datasource.executor.mysql.MySQLSelectForUpdateExecutor import MySQLSelectForUpdateExecutor
from seata.sqlparser.SQLType import SQLType


class ExecuteTemplate(object):

    @staticmethod
    def execute(cursor_proxy, cursor_callback, args):
        if not RootContext.in_global_transaction() and BranchType.AT != RootContext.get_branch_type():
            return cursor_callback.execute(cursor_proxy.target_cursor, cursor_proxy.target_sql, args)
        db_type = cursor_proxy.connection.get_db_type()
        sql_recognizer = SQLVisitorFactory.get(cursor_proxy.target_sql, db_type)
        executor = None
        if sql_recognizer is not None:
            sql_type = sql_recognizer.get_sql_type()
            if sql_type == SQLType.INSERT:
                executor = MySQLInsertExecutor(cursor_proxy, cursor_callback, sql_recognizer)
            elif sql_type == SQLType.UPDATE:
                executor = MySQLUpdateExecutor(cursor_proxy, cursor_callback, sql_recognizer)
            elif sql_type == SQLType.DELETE:
                executor = MySQLDeleteExecutor(cursor_proxy, cursor_callback, sql_recognizer)
            elif sql_type == SQLType.SELECT_FOR_UPDATE:
                executor = MySQLSelectForUpdateExecutor(cursor_proxy, cursor_callback, sql_recognizer)
            else:
                executor = PlainExecutor(cursor_proxy, cursor_callback, sql_recognizer)
        else:
            executor = PlainExecutor(cursor_proxy, cursor_callback, sql_recognizer)

        return executor.execute(args)
