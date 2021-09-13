#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
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
