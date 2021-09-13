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
        self.table_meta = None
        self.table_name = None
        # Row
        self.rows = []
        if table_meta is not None:
            self.set_table_meta(table_meta)

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

    def size(self):
        return len(self.rows)

    def pk_rows(self):
        primary_key_map = self.table_meta.get_primary_key_map()
        pk_rows = []
        for i in range(len(self.rows)):
            row = self.rows[i]
            fields = row.fields
            row_map = {}
            for j in range(len(fields)):
                field = fields[j]
                if primary_key_map.get(field.name, None) is not None:
                    row_map[field.name] = field
            pk_rows.append(row_map)
        return pk_rows

    @classmethod
    def build_records(cls, table_meta, result, description):
        records = TableRecords(table_meta)
        for idx in range(len(result)):
            res = result[idx]
            column_count = len(res)
            fields = []
            for j in range(column_count):
                column_name = description[j][0]
                col = table_meta.get_column_meta(column_name)
                field = Field()
                field.name = column_name
                if table_meta.get_primary_key_map().get(column_name, None) is not None:
                    field.key_type = KeyType.PRIMARY_KEY
                field.type = col.data_type
                field.set_value(res[j])
                fields.append(field)
            row = Row()
            row.fields = fields
            records.rows.append(row)
        return records
