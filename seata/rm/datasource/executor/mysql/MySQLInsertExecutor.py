#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.executor.Executor import BaseInsertExecutor
from seata.sqlparser.mysql.antlr4.value import MySQLValue


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
        return pk_values_map

    def get_pk_values_by_auto(self):
        pk_values_map = {}
        pk_meta_map = self.get_table_meta().get_primary_key_map()
        auto_column_name = None
        for k, v in pk_meta_map:
            if v.is_auto_increment():
                auto_column_name = k
                break
        if auto_column_name is None or auto_column_name.strip() == "":
            raise ShouldNeverHappenException()

        rowid = self.cursor_proxy.lastrowid
        values = []
        rowcount = self.cursor_proxy.rowcount
        if rowcount > 1 and self.can_auto_increment(pk_meta_map):
            self.auto_generate_pks(rowid, auto_column_name, rowcount)
        else:
            values.append(rowid)

        pk_values_map[auto_column_name] = values
        return pk_values_map

    def can_auto_increment(self, pk_meta_map):
        if len(pk_meta_map) > 1:
            return False
        for k, v in pk_meta_map:
            return v.is_auto_increment()
        return False

    def auto_generate_pks(self, rowid, auto_column_name, rowcount):
        step = 1
        resource_id = self.cursor_proxy.connection_proxy.pooled_db_proxy.get_resource_id()
        if self.RESOURCE_STEP_CACHE[resource_id] is not None:
            step = self.RESOURCE_STEP_CACHE[resource_id]
        else:
            self.cursor_proxy.target_cursor.execute("SHOW VARIABLES LIKE 'auto_increment_increment'")
            one = self.cursor_proxy.target_cursor.fetchone()
            step = one[1]
            self.RESOURCE_STEP_CACHE[resource_id] = step

        pk_values = []
        for i in range(rowcount):
            pk_values.append(rowid)
            rowid += step

        pk_values_map = {auto_column_name: pk_values}
        return pk_values_map
