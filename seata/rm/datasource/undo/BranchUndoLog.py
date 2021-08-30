#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from collections import OrderedDict

from seata.rm.datasource.sql.struct.ColumnMeta import ColumnMeta
from seata.rm.datasource.sql.struct.Field import Field
from seata.rm.datasource.sql.struct.IndexMeta import IndexMeta
from seata.rm.datasource.sql.struct.IndexType import IndexType
from seata.rm.datasource.sql.struct.KeyType import KeyType
from seata.rm.datasource.sql.struct.Row import Row
from seata.rm.datasource.sql.struct.TableMeta import TableMeta
from seata.rm.datasource.sql.struct.TableRecords import TableRecords
from seata.rm.datasource.undo.SQLUndoLog import SQLUndoLog
from seata.sqlparser.SQLType import SQLType


class BranchUndoLog:
    def __init__(self, dic=None):
        self.xid = None
        self.branch_id = 0
        # SQLUndoLog list
        self.sql_undo_logs = None
        if dic is not None:
            self.__dic_to_branch_undo_log(dic)

    def __dic_to_branch_undo_log(self, bul_dic):
        self.xid = bul_dic.get('xid', None)
        self.branch_id = bul_dic.get('branch_id', None)
        self.sql_undo_logs = []
        sql_undo_logs = bul_dic.get('sql_undo_logs', None)
        if sql_undo_logs is not None and len(sql_undo_logs) > 0:
            for sql_undo_log in sql_undo_logs:
                sul = SQLUndoLog()
                sul.sql_type = SQLType(sql_undo_log.get('sql_type', None))
                sul.table_name = sql_undo_log.get('table_name', None)

                before_image = sql_undo_log.get('before_image', None)
                if before_image is not None:
                    sul.before_image = self.__dic_to_table_records(before_image)

                after_image = sql_undo_log.get('after_image', None)
                if after_image is not None:
                    sul.after_image = self.__dic_to_table_records(after_image)

                self.sql_undo_logs.append(sul)

    def __dic_to_table_records(self, tr_dic):
        tr = TableRecords()
        table_meta = tr_dic.get('table_meta', None)
        tr.table_meta = self.__dic_to_table_meta(table_meta)
        tr.table_name = tr_dic.get('table_name', None)
        rows_dic = tr_dic.get('rows', None)
        tr.rows = self.__dic_to_rows(rows_dic)
        return tr

    def __dic_to_rows(self, rows_dic):
        rows = []
        if rows_dic is not None and len(rows_dic) > 0:
            for i in range(len(rows_dic)):
                row_dic = rows_dic[i]
                row = Row()
                fields_dic = row_dic.get('fields', None)
                if fields_dic is not None and len(fields_dic) > 0:
                    for j in range(len(fields_dic)):
                        f_dic = fields_dic[j]
                        f = self.__dic_to_field(f_dic)
                        row.fields.append(f)
                rows.append(row)
        return rows

    def __dic_to_field(self, f_dic):
        if f_dic is None:
            return None
        f = Field()
        f.name = f_dic.get('name', None)
        f.key_type = KeyType(f_dic.get('key_type', None))
        f.type = f_dic.get('type', None)
        f.value = f_dic.get('value', None)
        return f

    def __dic_to_table_meta(self, tm_dic):
        if tm_dic is None:
            return None
        tm = TableMeta()
        tm.table_name = tm_dic.get('table_name', None)
        all_columns = tm_dic.get('all_columns', None)
        if all_columns is not None and len(all_columns) > 0:
            tm.all_columns = OrderedDict()
            for column_name, cm_dic in all_columns.items():
                cm = self.__dic_to_column_meta(cm_dic)
                tm.all_columns[column_name] = cm
        all_indexs = tm_dic.get('all_indexs', None)
        if all_indexs is not None and len(all_indexs) > 0:
            tm.all_indexs = OrderedDict()
            for index_name, im_dic in all_indexs.items():
                cm = self.__dic_to_index_meta(im_dic)
                tm.all_indexs[index_name] = cm
        return tm

    def __dic_to_column_meta(self, cm_dic):
        if cm_dic is None:
            return None
        cm = ColumnMeta()
        cm.table_cat = cm_dic.get('table_cat', None)
        cm.table_schema_name = cm_dic.get('table_schema_name', None)
        cm.table_name = cm_dic.get('table_name', None)
        cm.column_name = cm_dic.get('column_name', None)
        cm.data_type = cm_dic.get('data_type', None)
        cm.data_type_name = cm_dic.get('data_type_name', None)
        cm.column_size = cm_dic.get('column_size', None)
        cm.decimal_digits = cm_dic.get('decimal_digits', None)
        cm.num_prec_radix = cm_dic.get('num_prec_radix', None)
        cm.null_able = cm_dic.get('null_able', None)
        cm.remarks = cm_dic.get('remarks', None)
        cm.column_def = cm_dic.get('column_def', None)
        cm.sql_data_type = cm_dic.get('sql_data_type', None)
        cm.sql_datetime_sub = cm_dic.get('sql_datetime_sub', None)
        cm.char_octet_length = cm_dic.get('char_octet_length', None)
        cm.ordinal_position = cm_dic.get('ordinal_position', None)
        cm.is_nullable = cm_dic.get('is_nullable', None)
        cm.is_autoincrement = cm_dic.get('is_autoincrement', None)
        return cm

    def __dic_to_index_meta(self, im_dic):
        if im_dic is None:
            return None
        im = IndexMeta()
        values = im_dic.get('values', None)
        if values is not None and len(values) > 0:
            im.values = []
            for value in values:
                im.values.append(self.__dic_to_column_meta(value))
        im.non_unique = im_dic.get('non_unique', None)
        im.index_qualifier = im_dic.get('index_qualifier', None)
        im.index_name = im_dic.get('index_name', None)
        im.type = im_dic.get('type', None)
        im.index_type = IndexType(im_dic.get('index_type', None))
        im.asc_or_desc = im_dic.get('asc_or_desc', None)
        im.cardinality = im_dic.get('cardinality', None)
        im.ordinal_position = im_dic.get('ordinal_position', None)
        return im
