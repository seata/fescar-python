#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.context.RootContext import RootContext
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.ColumnUtils import ColumnUtils
from seata.rm.datasource.exception.SQLException import SQLException
from seata.rm.datasource.sql.TableMetaCacheFactory import TableMetaCacheFactory
from seata.rm.datasource.sql.struct.TableRecords import TableRecords
from seata.rm.datasource.undo.SQLUndoLog import SQLUndoLog
from seata.sqlparser.SQLType import SQLType
from seata.sqlparser.mysql.MySQLInsertSQLRecognizer import MySQLInsertRecognizer


class Executor:
    def execute(self, args):
        pass


class BaseTransactionalExecutor(Executor):
    def __init__(self, cursor_proxy, cursor_callback, sql_recognizer):
        self.cursor_proxy = cursor_proxy
        self.cursor_callback = cursor_callback
        if isinstance(sql_recognizer, list):
            self.sql_recognizer = sql_recognizer[0]
            self.sql_recognizers = sql_recognizer
        else:
            self.sql_recognizer = sql_recognizer
        self.table_meta = None

    def execute(self, args):
        xid = RootContext.get_xid()
        if xid is not None:
            self.cursor_proxy.connection_proxy.bind(xid)
        self.cursor_proxy.connection_proxy.set_global_lock_require(RootContext.require_global_lock())
        self.do_execute(args)

    def do_execute(self, args):
        pass

    def get_table_meta(self, table_name: str = None):
        if table_name is None:
            table_name = self.sql_recognizer.get_table_name()
        if self.table_meta is not None:
            return self.table_meta
        cp = self.cursor_proxy.connection_proxy
        self.table_meta = TableMetaCacheFactory.get_table_meta_cache(cp.get_db_type()) \
            .get_table_meta(cp.target_connection, table_name, cp.pooled_db_proxy.get_resource_id())
        return self.table_meta

    def prepare_undo_log(self, before_image, after_image):
        if len(before_image.rows) == 0 and len(after_image.rows) == 0:
            return
        if SQLType.UPDATE == self.sql_recognizer.get_sql_type():
            if len(before_image.rows) != len(after_image.rows):
                raise ShouldNeverHappenException("before image size not equals after image size")
        cp = self.cursor_proxy.connection_proxy
        if self.sql_recognizer.get_sql_type() == SQLType.DELETE:
            lock_key_records = before_image
        else:
            lock_key_records = after_image
        lock_keys = self.build_lock_key(lock_key_records)
        if lock_keys is not None:
            cp.appendLockKey(lock_keys)
            sql_undo_log = self.build_undo_item(before_image, after_image)
            cp.append_undo_log(sql_undo_log)

    def build_lock_key(self, lock_key_records):
        if len(lock_key_records) == 0:
            return None

        string = lock_key_records.table_meta.table_name + ":"
        field_seq = 0
        pk_rows = lock_key_records.pk_rows()
        for i in range(len(pk_rows)):
            pk_row = pk_rows[i]
            pk_list = self.get_table_meta().get_primary_key_only_name()
            for j in range(len(pk_list)):
                pk_name = pk_list[j]
                if j > 0:
                    string += "_"
                string += pk_row[pk_name].value
            field_seq += 1
            if field_seq < len(pk_rows):
                string += ","
        return string

    def build_undo_item(self, before_image, after_image):
        sql_type = self.sql_recognizer.get_sql_type()
        table_name = self.sql_recognizer.get_table_name()
        sql_undo_log = SQLUndoLog()
        sql_undo_log.sql_type = sql_type
        sql_undo_log.table_name = table_name
        sql_undo_log.before_image = before_image
        sql_undo_log.after_image = after_image
        return sql_undo_log


class DMLBaseExecutor(BaseTransactionalExecutor):
    def __init__(self, cursor_proxy, cursor_callback, sql_recognizer):
        super(DMLBaseExecutor, self).__init__(cursor_proxy, cursor_callback, sql_recognizer)

    def do_execute(self, args):
        cp = self.cursor_proxy.connection_proxy
        if cp.get_autocommit():
            self.execute_autocommit_true(args)
        else:
            self.execute_autocommit_false(args)

    def execute_autocommit_true(self, args):
        cp = self.cursor_proxy.connection_proxy
        try:
            cp.change_autocommit()
            # TODO retry
            result = self.execute_autocommit_false(args)
            cp.commit()
            return result
        except Exception as e:
            print('rollback', e)
            cp.rollback()
        finally:
            cp.context.reset()
            cp.autocommit(True)

    def execute_autocommit_false(self, args):
        before_image = self.before_image()
        result = self.cursor_proxy.execute(self.cursor_proxy.target_cursor, args)
        after_image = self.after_image(before_image)
        self.prepare_undo_log(before_image, after_image)
        return result

    def before_image(self):
        pass

    def after_image(self, before_image: TableRecords):
        pass


class InsertExecutor(Executor):
    def get_pk_values(self):
        pass

    def get_pk_values_by_column(self):
        pass


class BaseInsertExecutor(DMLBaseExecutor, InsertExecutor):
    def __init__(self, cursor_proxy, cursor_callback, sql_recognizer):
        super(BaseInsertExecutor, self).__init__(cursor_proxy, cursor_callback, sql_recognizer)

    def before_image(self):
        return TableRecords.empty(self.get_table_meta())

    def after_image(self, before_image: TableRecords):
        pk_values = self.get_pk_values()
        after_image = self.build_table_records(pk_values)
        if after_image is None:
            raise SQLException("build table records error for insert")
        return after_image

    def contains_pk(self, insert_columns=None):
        if insert_columns is None:
            recognizer: MySQLInsertRecognizer = self.sql_recognizer
            insert_columns = recognizer.get_insert_columns()
            if insert_columns is None or len(insert_columns) <= 0:
                return False
        if len(insert_columns) <= 0:
            return False
        new_columns = ColumnUtils.del_escape(insert_columns, self.get_db_type())
        return self.get_table_meta().contains_pk(new_columns)

    def build_table_records(self, pk_values_map):
        pk_column_name_list = self.get_table_meta().get_primary_key_only_name()
        sql = " SELECT * FROM "
        sql += self.get_from_table_in_sql()
        sql += " WHERE "
        first_key = next(iter(pk_values_map))
        row_size = len(pk_values_map[first_key])
        sql += self.build_where_condition_by_pks(pk_column_name_list, row_size, self.get_db_type())
        with self.cursor_proxy.get_connection().cursor() as cursor:
            params = []
            for r in range(row_size):
                for c in range(len(pk_column_name_list)):
                    pk_column_value_list = pk_values_map[pk_column_name_list[c]]
                    params.append(pk_column_value_list[r])
            cursor.execute(sql, tuple(params))
            result = cursor.fetchall()
            return TableRecords.build_records(self.get_table_meta(), result)

    def build_where_condition_by_pks(self, pk_column_name_list, row_size, db_type):
        max_in_size = 1000
        where_str = ""
        if row_size % max_in_size == 0:
            batch_size = row_size // max_in_size
        else:
            batch_size = row_size // max_in_size + 1
        for batch in range(batch_size):
            if batch > 0:
                where_str += " or "
            where_str += "("
            for i in range(len(pk_column_name_list)):
                if i > 0:
                    where_str += ","
                where_str += ColumnUtils.add_escape_by_cols_dbtype(pk_column_name_list[i], db_type)
            where_str += ") in ( "
            if batch == batch_size - 1:
                if row_size % max_in_size == 0:
                    each_size = max_in_size
                else:
                    each_size = row_size % max_in_size
            else:
                each_size = max_in_size
            for i in range(each_size):
                if i > 0:
                    where_str += ","
                where_str += "("
                for x in range(len(pk_column_name_list)):
                    if x > 0:
                        where_str += ","
                    where_str += "?"
                where_str += ")"
            where_str += ")"
        return where_str

    def get_db_type(self):
        return self.cursor_proxy.connection_proxy.get_db_type()
