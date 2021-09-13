#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.NotSupportYetException import NotSupportYetException
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.ColumnUtils import ColumnUtils
from seata.rm.datasource.executor.Executor import BaseInsertExecutor
from seata.sqlparser.mysql.antlr4.value import MySQLValue
from seata.sqlparser.mysql.antlr4.value.MySQLValue import ParameterMarkerValue


class MySQLInsertExecutor(BaseInsertExecutor):
    RESOURCE_STEP_CACHE = {}

    def __int__(self, cursor_proxy, cursor_callback, sql_recognizer):
        self.cursor_proxy = cursor_proxy
        self.cursor_callback = cursor_callback
        self.sql_recognizer = sql_recognizer

    def get_pk_values(self):
        pk_values_map = None
        pk_column_name_list = self.get_table_meta().get_primary_key_only_name()
        is_contains_pk = self.contains_pk()
        if len(self.get_table_meta().get_primary_key_only_name()) == 1:
            if is_contains_pk:
                pk_values_map = self.get_pk_values_by_column()
            elif self.contains_columns():
                pk_values_map = self.get_pk_values_by_auto()
            else:
                pk_values_map = self.get_pk_values_by_column()
        else:
            pk_values_map = self.get_pk_values_by_column()
            for i in range(len(pk_column_name_list)):
                column_name = pk_column_name_list[i]
                if pk_values_map[column_name] is None:
                    pk_column_meta = self.get_table_meta().get_column_meta(column_name)
                    if pk_column_meta is not None and pk_column_meta.is_auto_increment():
                        pk_values_map.update(self.get_pk_values_by_auto())
        return pk_values_map

    def contains_columns(self):
        return self.sql_recognizer.insert_columns_is_empty()

    def get_pk_values_by_column(self):
        pk_values_map = self.parse_pk_values_from_cursor()
        key_set = list(pk_values_map.keys())
        for i in range(len(key_set)):
            key = key_set[i]
            pk_values = pk_values_map[key]
            if len(pk_values) == 1 and isinstance(pk_values[0], MySQLValue.FunctionNameValue):
                auto_pk_map = self.get_pk_values_by_auto()
                pk_values_map.update(auto_pk_map)
            elif len(pk_values) > 0 and isinstance(pk_values[0], MySQLValue.NullValue):
                auto_pk_map = self.get_pk_values_by_auto()
                pk_values_map.update(auto_pk_map)
            elif len(pk_values) > 0 and pk_values[0] is None:
                auto_pk_map = self.get_pk_values_by_auto()
                pk_values_map.update(auto_pk_map)
        return pk_values_map

    def parse_pk_values_from_cursor(self):
        recognizer = self.sql_recognizer
        pk_index_map = self.get_pk_index()
        if len(pk_index_map) == 0:
            raise ShouldNeverHappenException('pk index is not found')
        pk_values_map = {}
        ps = True
        if self.cursor_proxy.parameters is not None:
            insert_rows = recognizer.get_insert_rows(pk_index_map.values())
            if insert_rows is not None and len(insert_rows) > 0:
                parameters = self.deal_parameters(self.cursor_proxy.parameters)
                total_placeholder_num = -1
                for row in insert_rows:
                    if len(row) == 0:
                        continue
                    current_row_placeholder_num = -1
                    for r in row:
                        if isinstance(r, ParameterMarkerValue):
                            total_placeholder_num += 1
                            current_row_placeholder_num += 1
                    pk_key = None
                    pk_index = 0
                    pk_values = None
                    for pk_key, pk_index in pk_index_map.items():
                        pk_values = pk_values_map.get(pk_key, None)
                        if pk_values is None:
                            pk_values = []
                        pk_value = row[pk_index]
                        if isinstance(pk_value, ParameterMarkerValue):
                            current_row_not_placeholder_num_before_pk_index = 0
                            for n in range(len(row)):
                                r = row[n]
                                if n < pk_index and not isinstance(r, ParameterMarkerValue):
                                    current_row_not_placeholder_num_before_pk_index += 1
                            idx = total_placeholder_num - current_row_placeholder_num + pk_index - current_row_not_placeholder_num_before_pk_index
                            parameter = parameters[idx]
                            pk_values.extend(parameter)
                        else:
                            pk_values.append(pk_value)

                        pk_key_escape = ColumnUtils.del_escape_by_col_dbtype(pk_key, self.get_db_type())
                        if pk_values_map.get(pk_key_escape, None) is None:
                            pk_values_map[pk_key_escape] = pk_values
        else:
            ps = False
            insert_rows = self.sql_recognizer.get_insert_rows(pk_index_map.values())
            for i in range(len(insert_rows)):
                row = insert_rows[i]
                for pk, index in pk_index_map:
                    pk_values = pk_values_map[pk]
                    if pk_values is None:
                        pk_values_map[ColumnUtils.del_escape_by_col_dbtype(pk, self.get_db_type())] = [row[index]]
                    else:
                        pk_values.append(row[index])

        if pk_values_map is None or len(pk_values_map) <= 0:
            raise ShouldNeverHappenException('pk values map is empty')
        b = self.__check_pk_values(pk_values_map, ps)
        if not b:
            raise NotSupportYetException('not support sql [{}]'.format(self.sql_recognizer.original_sql))
        return pk_values_map

    def __check_pk_values(self, pk_values_map, ps):
        pk_names = pk_values_map.keys()
        if len(pk_names) == 1:
            return self.check_pk_values_for_single_pk(next(iter(pk_values_map)), ps)
        else:
            return self.check_pk_values_for_multi_pk(pk_values_map)

    def check_pk_values_for_single_pk(self, pk_values, ps):
        n = 0
        v = 0
        m = 0
        s = 0
        d = 0
        for i in range(len(pk_values)):
            pk_value = pk_values[i]
            if isinstance(pk_value, MySQLValue.NullValue):
                n += 1
                continue
            if isinstance(pk_value, MySQLValue.FunctionNameValue):
                m += 1
                continue
            if isinstance(pk_value, MySQLValue.DefaultValue):
                d += 1
                continue
            v += 1
        if not ps:
            if m > 0:
                return False
            if n == 1 and v == 0 and m == 0 and s == 0 and d == 0:
                return True
            if n == 0 and v > 0 and m == 0 and s == 0 and d == 0:
                return True
            if n == 0 and v == 0 and m == 0 and s == 1 and d == 0:
                return True
            if n == 0 and v == 0 and m == 0 and s == 0 and d == 1:
                return True
            return False
        if n > 0 and v == 0 and m == 0 and s == 0 and d == 0:
            return True
        if n == 0 and v > 0 and m == 0 and s == 0 and d == 0:
            return True
        if n == 0 and v == 0 and m > 0 and s == 0 and d == 0:
            return True
        if n == 0 and v == 0 and m == 0 and s > 0 and d == 0:
            return True
        if n == 0 and v == 0 and m == 0 and s == 0 and d > 0:
            return True
        return False

    def check_pk_values_for_multi_pk(self, pk_values_map):
        pk_names = pk_values_map.keys()
        if len(pk_names) == 0:
            raise ShouldNeverHappenException()
        row_size = len(pk_values_map.get(next(iter(pk_names))))
        for i in range(row_size):
            n = 0
            m = 0
            for k in pk_names:
                pk_value = pk_values_map[k][i]
                if isinstance(pk_value, MySQLValue.NullValue):
                    n += 1
                if isinstance(pk_value, MySQLValue.FunctionNameValue):
                    m += 1
            if n > 1:
                return False
            if m > 0:
                return False
        return True

    def get_pk_index(self):
        pk_index_map = {}
        recognizer = self.sql_recognizer
        insert_columns = recognizer.get_insert_columns()
        if insert_columns is not None and len(insert_columns) > 0:
            insert_columns_size = len(insert_columns)
            for param_idx in range(insert_columns_size):
                sql_column_name = insert_columns[param_idx]
                if self.contains_pk([sql_column_name]):
                    pk_index_map[self.get_standard_pk_column_name(sql_column_name)] = param_idx
            return pk_index_map
        pk_index = -1
        all_columns = self.get_table_meta().all_columns
        for cn, column_meta in all_columns:
            pk_index += 1
            if self.contains_pk([column_meta.column_name]):
                pk_index_map[
                    ColumnUtils.del_escape_by_col_dbtype(column_meta.column_name, self.get_db_type())] = pk_index
        return pk_index_map

    def get_pk_values_by_auto(self):
        pk_values_map = {}
        pk_meta_map = self.get_table_meta().get_primary_key_map()
        auto_column_name = None
        for k, v in pk_meta_map.items():
            if v.is_auto_increment():
                auto_column_name = k
                break
        if auto_column_name is None or auto_column_name.strip() == "":
            raise ShouldNeverHappenException()

        rowid = self.cursor_proxy.lastrowid
        values = []
        rowcount = self.cursor_proxy.rowcount
        if rowcount > 1 and self.can_auto_increment(pk_meta_map):
            return self.auto_generate_pks(rowid, auto_column_name, rowcount)
        else:
            values.append(rowid)

        pk_values_map[auto_column_name] = values
        return pk_values_map

    def can_auto_increment(self, pk_meta_map):
        if len(pk_meta_map) > 1:
            return False
        for k, v in pk_meta_map.items():
            return v.is_auto_increment()
        return False

    def auto_generate_pks(self, rowid, auto_column_name, rowcount):
        step = 1
        resource_id = self.cursor_proxy.connection_proxy.data_source_proxy.get_resource_id()
        if self.RESOURCE_STEP_CACHE.get(resource_id, None) is not None:
            step = self.RESOURCE_STEP_CACHE[resource_id]
        else:
            self.cursor_proxy.target_cursor.execute("SHOW VARIABLES LIKE 'auto_increment_increment'")
            one = self.cursor_proxy.target_cursor.fetchone()
            step = int(one[1])
            self.RESOURCE_STEP_CACHE[resource_id] = step

        pk_values = []
        for i in range(rowcount):
            pk_values.append(rowid)
            rowid += step

        pk_values_map = {auto_column_name: pk_values}
        return pk_values_map
