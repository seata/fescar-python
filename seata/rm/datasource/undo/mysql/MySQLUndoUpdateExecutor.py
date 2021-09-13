#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.ColumnUtils import ColumnUtils
from seata.rm.datasource.undo.UndoExecutor import UndoExecutor
from seata.sqlparser.util.JdbcConstants import JdbcConstants
from seata.sqlparser.util.SQLUtil import SQLUtil


class MySQLUndoUpdateExecutor(UndoExecutor):
    UPDATE_SQL_TEMPLATE = "UPDATE {} SET {} WHERE {}"

    def __init__(self, sql_undo_log):
        super(MySQLUndoUpdateExecutor, self).__init__(sql_undo_log)

    def build_undo_sql(self):
        before_image = self.sql_undo_log.before_image
        before_image_rows = before_image.rows
        if before_image_rows is None or len(before_image_rows) == 0:
            raise ShouldNeverHappenException('Invalid undo log')
        row = before_image_rows[0]
        non_pk_fields = row.non_primary_keys()
        update_columns = ""
        for non_pk_idx, non_pk in enumerate(non_pk_fields):
            if non_pk_idx > 0:
                update_columns += ","
            update_columns += (ColumnUtils.add_by_col_dbtype(non_pk.name, JdbcConstants.MYSQL) + " = %s")
        pk_list = self.get_ordered_pk_list(before_image, row, JdbcConstants.MYSQL)
        pk_name_list = []
        for pk_idx, pk in enumerate(pk_list):
            pk_name_list.append(pk.name)
        where_sql = SQLUtil.build_where_condition_by_pks_single(pk_name_list, JdbcConstants.MYSQL)
        return self.UPDATE_SQL_TEMPLATE.format(self.sql_undo_log.table_name, update_columns, where_sql)

    def get_undo_rows(self):
        return self.sql_undo_log.before_image
