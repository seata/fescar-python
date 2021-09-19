#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from loguru import logger

from seata.config.Config import ConfigFactory
from seata.rm.datasource.ColumnUtils import ColumnUtils
from seata.rm.datasource.DataCompareUtil import DataCompareUtil
from seata.rm.datasource.exception.SQLException import SQLException
from seata.rm.datasource.sql.struct.KeyType import KeyType
from seata.rm.datasource.sql.struct.TableRecords import TableRecords
from seata.sqlparser.util.SQLUtil import SQLUtil


class UndoExecutor:
    IS_UNDO_DATA_VALIDATION_ENABLE = None
    CHECK_SQL_TEMPLATE = "SELECT * FROM {} WHERE {} FOR UPDATE"

    def __init__(self, sql_undo_log):
        self.sql_undo_log = sql_undo_log

        if self.IS_UNDO_DATA_VALIDATION_ENABLE is None:
            self.IS_UNDO_DATA_VALIDATION_ENABLE = ConfigFactory.get_config().get_bool('client.undo.data-validation')

    def build_undo_sql(self):
        raise NotImplemented("need subclass implemented")

    def get_undo_rows(self):
        raise NotImplemented("need subclass implemented")

    def execute_on(self, connection):
        if self.IS_UNDO_DATA_VALIDATION_ENABLE and not self.data_validation_and_go_on(connection):
            return
        try:
            undo_sql = self.build_undo_sql()
            cursor = connection.cursor()
            undo_records = self.get_undo_rows()
            for undo_row in undo_records.rows:
                undo_values = []
                pk_value_list = self.get_ordered_pk_list(undo_records, undo_row, self.get_db_type(connection))
                for field in undo_row.fields:
                    if field.key_type != KeyType.PRIMARY_KEY:
                        undo_values.append(field)
                params = self.undo_prepare(cursor, undo_values, pk_value_list)
                cursor.execute(undo_sql, tuple(params))
        except Exception as e:
            raise e

    def get_ordered_pk_list(self, table_records, row, db_type):
        pk_fields = []
        pk_column_name_list_by_order = table_records.table_meta.get_primary_key_only_name()
        pk_column_name_list_no_order = [ColumnUtils.del_escape_by_col_dbtype(x.name, db_type) for x in
                                        row.primary_keys()]
        for pk_name in pk_column_name_list_by_order:
            pk_index = pk_column_name_list_no_order.index(pk_name)
            if pk_index != -1:
                pk_fields.append(row.primary_keys()[pk_index])
        return pk_fields

    def undo_prepare(self, cursor, undo_values, pk_value_list):
        params = []
        for undo_value in undo_values:
            params.append(undo_value.get_value())

        for pk_field in pk_value_list:
            params.append(pk_field.get_value())
        return params

    def data_validation_and_go_on(self, connection):
        before_image = self.sql_undo_log.before_image
        after_image = self.sql_undo_log.after_image

        before_eq_after_result = DataCompareUtil.is_records_equals(before_image, after_image)
        if before_eq_after_result[0]:
            logger.error("stop rollback because there is no data change. before and after snapshot")
            return False
        current_image = self.query_current_records(connection)
        after_eq_current_result = DataCompareUtil.is_records_equals(after_image, current_image)
        if not after_eq_current_result[0]:
            before_eq_current_result = DataCompareUtil.is_records_equals(before_image, current_image)
            if before_eq_current_result[0]:
                logger.error("stop rollback because there is not data change. before and current snapshot")
                return False
            else:
                if after_eq_current_result[1] is not None:
                    logger.error(after_eq_current_result[1], after_eq_current_result[2])
                raise SQLException('Has dirty records when undo.')
        return True

    def query_current_records(self, connection):
        undo_records = self.get_undo_rows()
        tm = undo_records.table_meta
        pk_name_list = tm.get_primary_key_only_name()
        pk_row_values = self.parse_pk_values(undo_records.rows, pk_name_list)
        if len(pk_row_values) == 0:
            return TableRecords.empty(tm)
        first_key = next(iter(pk_row_values.keys()))
        pk_row_size = len(pk_row_values[first_key])
        check_sql = self.CHECK_SQL_TEMPLATE.format(self.sql_undo_log.table_name,
                                                   SQLUtil.build_where_condition_by_pks(pk_name_list, pk_row_size,
                                                                                        self.get_db_type(connection)))
        params = []
        row_size = len(pk_row_values.get(pk_name_list[0]))
        for r in range(row_size):
            for c in range(len(pk_name_list)):
                pk_column_value_list = pk_row_values.get(pk_name_list[c])
                field = pk_column_value_list[r]
                params.append(field.value)
        cursor = None
        current_records = None
        try:
            cursor = connection.cursor()
            cursor.execute(check_sql, tuple(params))
            rs_all = cursor.fetchall()
            description = cursor.description
            current_records = TableRecords.build_records(tm, rs_all, description)
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass
        return current_records

    def parse_pk_values(self, rows, pk_name_list):
        pk_field_list = []
        l_pk_name_list = [x.lower() for x in pk_name_list]
        for i in range(len(rows)):
            fields = rows[i].fields
            if fields is not None:
                for field in fields:
                    if field.name.lower() in l_pk_name_list:
                        pk_field_list.append(field)

        pk_value_map = {}
        for field in pk_field_list:
            if pk_value_map.get(field.name, None) is not None:
                pk_value_map.get(field.name).append(field)
            else:
                pk_value_map[field.name] = []
                pk_value_map.get(field.name).append(field)
        return pk_value_map

    def get_db_type(self, connection):
        return SQLUtil.get_db_type(connection)
