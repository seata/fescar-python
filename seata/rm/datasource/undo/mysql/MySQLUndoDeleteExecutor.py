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
from seata.rm.datasource.ColumnUtils import ColumnUtils
from seata.rm.datasource.undo.UndoExecutor import UndoExecutor
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class MySQLUndoDeleteExecutor(UndoExecutor):
    INSERT_SQL_TEMPLATE = "INSERT INTO {} ({}) VALUES ({})"

    def __init__(self, sql_undo_log):
        super(MySQLUndoDeleteExecutor, self).__init__(sql_undo_log)

    def build_undo_sql(self):
        before_image = self.sql_undo_log.before_image
        rows = before_image.rows
        if rows is None or len(rows) == 0:
            raise ShouldNeverHappenException('Invalid undo log')
        row = rows[0]
        fields = []
        fields.extend(row.non_primary_keys())
        fields.extend(self.get_ordered_pk_list(before_image, row, JdbcConstants.MYSQL))

        columns = ', '.join([ColumnUtils.add_by_col_dbtype(f.name, JdbcConstants.MYSQL) for f in fields])
        values = ', '.join(["%s" for f in fields])
        return self.INSERT_SQL_TEMPLATE.format(self.sql_undo_log.table_name, columns, values)

    def get_undo_rows(self):
        return self.sql_undo_log.before_image
