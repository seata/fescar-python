#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.undo.UndoExecutor import UndoExecutor
from seata.sqlparser.util.JdbcConstants import JdbcConstants
from seata.sqlparser.util.SQLUtil import SQLUtil


class MySQLUndoInsertExecutor(UndoExecutor):
    DELETE_SQL_TEMPLATE = "DELETE FROM {} WHERE {}"

    def __init__(self, sql_undo_log):
        super(MySQLUndoInsertExecutor, self).__init__(sql_undo_log)

    def get_undo_rows(self):
        return self.sql_undo_log.after_image

    def build_undo_sql(self):
        after_image = self.sql_undo_log.after_image
        rows = after_image.rows
        if rows is None or len(rows) <= 0:
            raise ShouldNeverHappenException('invalid undo log')
        return self.generate_delete_sql(rows, after_image)

    def undo_prepare(self, cursor, undo_values, pk_value_list):
        params = [x.value for x in pk_value_list]
        return params

    def generate_delete_sql(self, rows, after_image):
        pk_name_list = [x.name for x in self.get_ordered_pk_list(after_image, rows[0], JdbcConstants.MYSQL)]
        where_sql = SQLUtil.build_where_condition_by_pks_single(pk_name_list, JdbcConstants.MYSQL)
        return self.DELETE_SQL_TEMPLATE.format(self.sql_undo_log.table_name, where_sql)
