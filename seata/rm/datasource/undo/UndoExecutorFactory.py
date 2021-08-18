#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.ColumnUtils import ColumnUtils
from seata.rm.datasource.DataCompareUtil import DataCompareUtil
from seata.rm.datasource.exception.SQLException import SQLException
from seata.rm.datasource.sql.struct.KeyType import KeyType
from seata.rm.datasource.sql.struct.TableRecords import TableRecords
from seata.sqlparser.SQLType import SQLType
from seata.sqlparser.util.JdbcConstants import JdbcConstants
from seata.sqlparser.util.SQLUtil import SQLUtil


class UndoExecutorFactory:
    @classmethod
    def get_undo_executor(cls, db_type, sql_undo_log):
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


class UndoExecutorHolder:
    def get_insert_executor(self, sql_undo_log):
        pass

    def get_update_executor(self, sql_undo_log):
        pass

    def get_delete_executor(self, sql_undo_log):
        pass


class MySQLUndoExecutorHolder(UndoExecutorHolder):
    def get_insert_executor(self, sql_undo_log):
        return MySQLUndoInsertExecutor(sql_undo_log)

    def get_update_executor(self, sql_undo_log):
        return MySQLUndoUpdateExecutor(sql_undo_log)

    def get_delete_executor(self, sql_undo_log):
        return MySQLUndoDeleteExecutor(sql_undo_log)


class UndoExecutor:
    IS_UNDO_DATA_VALIDATION_ENABLE = True
    CHECK_SQL_TEMPLATE = "SELECT * FROM {} WHERE {} FOR UPDATE"

    def __init__(self, sql_undo_log):
        self.sql_undo_log = sql_undo_log

    def build_undo_sql(self):
        pass

    def get_undo_rows(self):
        pass

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
        pk_column_name_list_no_order = [ColumnUtils.del_escape_by_colname_dbtype(x.name, db_type) for x in
                                        row.primary_keys()]
        for pk_name in pk_column_name_list_by_order:
            pk_index = pk_column_name_list_no_order.index(pk_name)
            if pk_index != -1:
                pk_fields.append(row.primary_keys()[pk_index])
        return pk_fields

    def undo_prepare(self, cursor, undo_values, pk_value_list):
        params = []
        for undo_value in undo_values:
            params.append(undo_value.value)

        for pk_field in pk_value_list:
            params.append(pk_field.value)
        return params

    def data_validation_and_go_on(self, connection):
        before_image = self.sql_undo_log.before_image
        after_image = self.sql_undo_log.after_image

        before_eq_after_result = DataCompareUtil.is_records_equals(before_image, after_image)
        if before_eq_after_result[0]:
            print("stop rollback because there is no data change. before and after snapshot")
            return False
        current_image = self.query_current_records(connection)
        after_eq_current_result = DataCompareUtil.is_records_equals(after_image, current_image)
        if not after_eq_current_result[0]:
            before_eq_current_result = DataCompareUtil.is_records_equals(before_image, current_image)
            if before_eq_current_result[0]:
                print("stop rollback because there is not data change. before and current snapshot")
                return False
            else:
                if after_eq_current_result[1] is not None:
                    print(after_eq_current_result[1], after_eq_current_result[2])
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
            current_records = TableRecords.build_records(tm, rs_all)
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


class MySQLUndoUpdateExecutor(UndoExecutor):
    def __init__(self, sql_undo_log):
        super(MySQLUndoUpdateExecutor, self).__init__(sql_undo_log)


class MySQLUndoDeleteExecutor(UndoExecutor):
    def __init__(self, sql_undo_log):
        super(MySQLUndoDeleteExecutor, self).__init__(sql_undo_log)


class UndoExecutorHolderFactory:
    _HOLDER_MAP = {}

    @classmethod
    def get_undo_executor_holder(cls, db_type):
        if cls._HOLDER_MAP.get(db_type, None) is not None:
            return cls._HOLDER_MAP[db_type]
        if db_type == JdbcConstants.MYSQL:
            cls._HOLDER_MAP[db_type] = MySQLUndoExecutorHolder()
            return cls._HOLDER_MAP[db_type]
        raise NotImplemented("db type : " + db_type)
