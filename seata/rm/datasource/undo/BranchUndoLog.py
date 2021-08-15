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
        self.xid = bul_dic['xid']
        self.branch_id = bul_dic['branch_id']
        self.sql_undo_logs = []
        sql_undo_logs = bul_dic['sql_undo_logs']
        if sql_undo_logs is not None and len(sql_undo_logs) > 0:
            for i in sql_undo_logs:
                sql_undo_log = sql_undo_logs[i]
                sul = SQLUndoLog()
                sul.sql_type = SQLType(sql_undo_log['sql_type'])
                sul.table_name = sql_undo_log['table_name']
                before_image = sql_undo_log['before_image']

                if before_image is not None:
                    sul.before_image = self.__dic_to_table_records(before_image)

                after_image = sql_undo_log['after_image']
                if after_image is not None:
                    sul.after_image = self.__dic_to_table_records(after_image)

    def __dic_to_table_records(self, tr_dic):
        tr = TableRecords()
        table_meta = tr_dic['table_meta']
        tr.table_meta = self.__dic_to_table_meta(table_meta)
        tr.table_name = tr_dic['table_name']
        rows_dic = tr_dic['rows']
        tr.rows = self.__dic_to_rows(rows_dic)
        return tr

    def __dic_to_rows(self, rows_dic):
        rows = []
        if rows_dic is not None and len(rows_dic) > 0:
            for i in range(len(rows_dic)):
                row_dic = rows_dic[i]
                row = Row()
                fields_dic = row_dic['fields']
                if fields_dic is not None and len(fields_dic) > 0:
                    for j in range(len(fields_dic)):
                        field_dic = fields_dic[j]
                        f = Field()
                        f.name = field_dic['name']
                        f.key_type = KeyType(field_dic['key_type'])
                        f.value = field_dic['value']
                        row.fields.append(f)
                rows.append(row)
        return rows

    def __dic_to_table_meta(self, tm_dic):
        tm = TableMeta()
        tm.table_name = tm_dic['table_name']
        all_columns = tm_dic['all_columns']
        if all_columns is not None and len(all_columns) > 0:
            tm.all_columns = OrderedDict()
            for column_name, cm_dic in all_columns:
                cm = self.__dic_to_column_meta(cm_dic)
                tm.all_columns[column_name] = cm
        all_indexs = tm_dic['all_indexs']
        if all_indexs is not None and len(all_indexs) > 0:
            tm.all_indexs = OrderedDict()
            for index_name, im_dic in all_indexs:
                cm = self.__dic_to_index_meta(im_dic)
                tm.all_indexs[index_name] = cm
        return tm

    def __dic_to_column_meta(self, cm_dic):
        cm = ColumnMeta()
        cm.table_cat = cm_dic['table_cat']
        cm.table_schema_name = cm_dic['table_schema_name']
        cm.table_name = cm_dic['table_name']
        cm.column_name = cm_dic['column_name']
        cm.data_type = cm_dic['data_type']
        cm.data_type_name = cm_dic['data_type_name']
        cm.column_size = cm_dic['column_size']
        cm.decimal_digits = cm_dic['decimal_digits']
        cm.num_prec_radix = cm_dic['num_prec_radix']
        cm.null_able = cm_dic['null_able']
        cm.remarks = cm_dic['remarks']
        cm.column_def = cm_dic['column_def']
        cm.sql_data_type = cm_dic['sql_data_type']
        cm.sql_datetime_sub = cm_dic['sql_datetime_sub']
        cm.char_octet_length = cm_dic['char_octet_length']
        cm.ordinal_position = cm_dic['ordinal_position']
        cm.is_nullable = cm_dic['is_nullable']
        cm.is_autoincrement = cm_dic['is_autoincrement']
        return cm

    def __dic_to_index_meta(self, im_dic):
        im = IndexMeta()
        values = im_dic['values']
        if values is not None and len(values) > 0:
            im.values = []
            for i in range(len(values)):
                value = values[i]
                im.values.append(self.__dic_to_column_meta(value))
        im.non_unique = im_dic['non_unique']
        im.index_qualifier = im_dic['index_qualifier']
        im.index_name = im_dic['index_name']
        im.type = im_dic['type']
        im.index_type = IndexType(im_dic['index_type'])
        im.asc_or_desc = im_dic['asc_or_desc']
        im.cardinality = im_dic['cardinality']
        im.ordinal_position = im_dic['ordinal_position']
        return im
