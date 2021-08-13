#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.sql.struct.Field import Field
from seata.rm.datasource.sql.struct.KeyType import KeyType
from seata.rm.datasource.sql.struct.Row import Row


class TableRecords(object):

    def __init__(self, table_meta=None):
        # TableMeta
        self.table_meta = table_meta
        self.table_name = None
        # Row
        self.rows = []

    def set_table_meta(self, table_meta):
        if self.table_meta is not None:
            raise ShouldNeverHappenException("table meta is not null")
        self.table_meta = table_meta
        self.table_name = table_meta.table_name

    @staticmethod
    def empty(table_meta):
        tr = TableRecords()
        tr.set_table_meta(table_meta)
        return tr

    def pk_rows(self):
        primary_key_map = self.table_meta.get_primary_key_map()
        pk_rows = []
        for i in range(len(self.rows)):
            row = self.rows[i]
            fields = row.fields
            row_map = {}
            for j in range(len(fields)):
                field = fields[j]
                if primary_key_map[field.name] is not None:
                    row_map[field.name] = field
            pk_rows.append(row_map)
        return pk_rows

    @classmethod
    def build_records(cls, table_meta, result):
        records = TableRecords(table_meta)
        fields = []
        for i in range(len(result)):
            res = result[i]
            column_name_list = list(table_meta.all_columns.keys())
            column_count = len(column_name_list)
            for j in range(column_count):
                column_name = column_name_list[i]
                col = table_meta.get_column_meta(column_name)
                field = Field()
                field.name = column_name
                if table_meta.get_primary_key_map[column_name] is not None:
                    field.key_type = KeyType.PRIMARY_KEY
                field.type = col.data_type
                field.value = res[j]
                fields.append(field)
            row = Row()
            row.fields = fields
            records.rows.append(row)
        return records
