#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import time

from loguru import logger

from seata.config.Config import ConfigFactory
from seata.core.context.RootContext import RootContext
from seata.exception.NotSupportYetException import NotSupportYetException
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.ColumnUtils import ColumnUtils
from seata.rm.datasource.exception.SQLException import SQLException
from seata.rm.datasource.executor.LockConflictException import LockConflictException
from seata.rm.datasource.executor.LockWaitTimeoutException import LockWaitTimeoutException
from seata.rm.datasource.sql.TableMetaCacheFactory import TableMetaCacheFactory
from seata.rm.datasource.sql.struct.TableRecords import TableRecords
from seata.rm.datasource.undo.SQLUndoLog import SQLUndoLog
from seata.sqlparser.SQLType import SQLType
from seata.sqlparser.util.SQLUtil import SQLUtil


class Executor:
    def execute(self, args):
        raise NotImplemented("need subclass implemented")


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
        raise NotImplemented("need subclass implemented")

    def get_table_meta(self, table_name: str = None):
        if table_name is None:
            table_name = self.sql_recognizer.get_table_name()
        if self.table_meta is not None:
            return self.table_meta
        cp = self.cursor_proxy.connection_proxy
        self.table_meta = TableMetaCacheFactory.get_table_meta_cache(cp.get_db_type()) \
            .get_table_meta(cp.target_connection, table_name, cp.data_source_proxy.get_resource_id())
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
            cp.append_lock_key(lock_keys)
            sql_undo_log = self.build_undo_item(before_image, after_image)
            cp.append_undo_log(sql_undo_log)

    def build_lock_key(self, lock_key_records):
        if lock_key_records.size() == 0:
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
                string += str(pk_row.get(pk_name).value)
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

    def get_standard_pk_column_name(self, column_name):
        new_column_name = ColumnUtils.del_escape_by_col_dbtype(column_name, self.get_db_type())
        pks = self.get_table_meta().get_primary_key_only_name()
        for i in range(len(pks)):
            cn = pks[i]
            if cn.lower() == new_column_name.lower():
                return cn
        return None

    def get_db_type(self):
        return self.cursor_proxy.connection_proxy.get_db_type()

    def get_from_table_in_sql(self):
        table_name = self.sql_recognizer.get_table_name()
        table_alias = self.sql_recognizer.get_table_alias()
        if table_alias is None:
            return table_name
        else:
            return table_name + " " + table_alias

    def build_where_condition(self, recognizer, param_list):
        where_condition = None
        if self.cursor_proxy.parameters is not None:
            where_condition = recognizer.get_where_condition(self.deal_parameters(self.cursor_proxy.parameters),
                                                             param_list)
        else:
            where_condition = recognizer.get_where_condition()
        if where_condition is not None and param_list is not None and len(param_list) > 1:
            where_str = " ( " + where_condition.replace(" WHERE", "") + " ) "
            for i in range(len(param_list)):
                if i > 0:
                    where_str += (" or ( " + where_condition.replace(" WHERE", "") + " ) ")
            where_condition = " WHERE" + where_str
        return where_condition

    def build_order_by_condition(self, recognizer, param_list):
        # TODO
        return ""

    def build_limit_condition(self, recognizer, param_list):
        # TODO
        return ""

    def deal_parameters(self, parameters):
        if isinstance(parameters, tuple):
            params = {}
            for index, p in enumerate(parameters):
                params[index] = [p]
            return params
        elif isinstance(parameters, list):
            params = {}
            for i in range(len(parameters)):
                parameter = parameters[i]
                if isinstance(parameter, tuple):
                    for index, p in enumerate(parameter):
                        if params.get(index, None) is None:
                            params[index] = [p]
                        else:
                            params[index].append(p)
                elif isinstance(parameter, dict):
                    for index, p in enumerate(parameter.items()):
                        if params.get(index, None) is None:
                            params[index] = [p[1]]
                        else:
                            params[index].append(p[1])
                else:
                    raise NotSupportYetException('parameter type error. ' + type(parameter).__name__)
            return params
        elif isinstance(parameters, dict):
            params = {}
            for index, kv in enumerate(parameters.items()):
                params[index] = [kv[1]]
            return params
        else:
            raise NotSupportYetException('not support parameters type : {}'.format(type(parameters)))

    def contains_pk(self, columns):
        if columns is None or len(columns) == 0:
            return False
        new_columns = ColumnUtils.del_escape_by_cols_dbtype(columns, self.get_db_type())
        return self.get_table_meta().contains_pk(new_columns)

    def get_column_names_in_sql(self, column_name_list):
        if column_name_list is None or len(column_name_list) == 0:
            return None
        column_str = ""
        for col_idx, column in enumerate(column_name_list):
            if col_idx > 0:
                column_str += ","
            column_str += self.get_column_name_in_sql(column)
        return column_str

    def get_column_name_in_sql(self, column):
        table_alias = self.sql_recognizer.get_table_alias()
        if table_alias is None:
            return column
        else:
            return table_alias + "." + column

    def build_table_records(self, tm, select_sql, param_list):
        cursor = None
        try:
            con = self.cursor_proxy.get_connection()
            cursor = con.cursor()
            params = []
            if param_list is not None and len(param_list) > 0:
                for pl_idx, param in enumerate(param_list):
                    for p_idx, p in enumerate(param):
                        params.append(p)
            cursor.execute(select_sql, tuple(params))
            rs_all = cursor.fetchall()

            description = cursor.description
            return TableRecords.build_records(tm, rs_all, description)
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass


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
            logger.error('rollback', e)
            cp.rollback()
        finally:
            cp.context.reset()
            cp.autocommit(True)

    def execute_autocommit_false(self, args):
        before_image = self.before_image()
        result = self.cursor_callback.execute(self.cursor_proxy.target_cursor, self.cursor_proxy.target_sql, args)
        after_image = self.after_image(before_image)
        self.prepare_undo_log(before_image, after_image)
        return result

    def before_image(self):
        raise NotImplemented("need subclass implemented")

    def after_image(self, before_image: TableRecords):
        raise NotImplemented("need subclass implemented")


class InsertExecutor(Executor):
    def get_pk_values(self):
        raise NotImplemented("need subclass implemented")

    def get_pk_values_by_column(self):
        raise NotImplemented("need subclass implemented")


class BaseInsertExecutor(DMLBaseExecutor, InsertExecutor):
    def __init__(self, cursor_proxy, cursor_callback, sql_recognizer):
        super(BaseInsertExecutor, self).__init__(cursor_proxy, cursor_callback, sql_recognizer)

    def before_image(self):
        return TableRecords.empty(self.get_table_meta())

    def after_image(self, before_image: TableRecords):
        pk_values = self.get_pk_values()
        after_image = self.build_table_records_by_pk_values(pk_values)
        if after_image is None:
            raise SQLException("build table records error for insert")
        return after_image

    def contains_pk(self, insert_columns: list = None):
        if insert_columns is not None and not isinstance(insert_columns, list):
            raise ValueError('insert columns is not list type')
        if insert_columns is None:
            recognizer = self.sql_recognizer
            insert_columns = recognizer.get_insert_columns()
            if insert_columns is None or len(insert_columns) <= 0:
                return False
        if len(insert_columns) <= 0:
            return False
        new_columns = ColumnUtils.del_escape_by_cols_dbtype(insert_columns, self.get_db_type())
        return self.get_table_meta().contains_pk(new_columns)

    def build_table_records_by_pk_values(self, pk_values_map):
        pk_column_name_list = self.get_table_meta().get_primary_key_only_name()
        sql = " SELECT * FROM "
        sql += self.get_from_table_in_sql()
        sql += " WHERE "
        first_key = next(iter(pk_values_map))
        row_size = len(pk_values_map[first_key])
        sql += SQLUtil.build_where_condition_by_pks(pk_column_name_list, row_size, self.get_db_type())
        cursor = None
        try:
            cursor = self.cursor_proxy.get_connection().cursor()
            params = []
            for r in range(row_size):
                for c in range(len(pk_column_name_list)):
                    pk_column_value_list = pk_values_map[pk_column_name_list[c]]
                    params.append(pk_column_value_list[r])
            cursor.execute(sql, tuple(params))
            result = cursor.fetchall()
            description = cursor.description
            return TableRecords.build_records(self.get_table_meta(), result, description)
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass


class UpdateExecutor(DMLBaseExecutor):
    ONLY_CARE_UPDATE_COLUMNS = None

    def __init__(self, cursor_proxy, cursor_callback, sql_recognizer):
        super(UpdateExecutor, self).__init__(cursor_proxy, cursor_callback, sql_recognizer)

        if self.ONLY_CARE_UPDATE_COLUMNS is None:
            self.ONLY_CARE_UPDATE_COLUMNS = ConfigFactory.get_config().get_bool('client.undo.only-care-update-columns')

    def before_image(self):
        param_list = []
        tm = self.get_table_meta()
        select_sql = self.__build_before_image_sql(tm, param_list)
        return self.build_table_records(tm, select_sql, param_list)

    def __build_before_image_sql(self, tm, param_list):
        recognizer = self.sql_recognizer
        update_columns = recognizer.get_update_columns()
        prefix = "SELECT "
        suffix = " FROM " + self.get_from_table_in_sql()
        where_condition = self.build_where_condition(recognizer, param_list)
        if len(where_condition.strip()) > 0:
            suffix += where_condition

        order_by_condition = self.build_order_by_condition(recognizer, param_list)
        if len(order_by_condition.strip()) > 0:
            suffix += order_by_condition
        limit_condition = self.build_limit_condition(recognizer, param_list)
        if len(limit_condition.strip()) > 0:
            suffix += limit_condition
        suffix += " FOR UPDATE"

        column_str = ""
        if self.ONLY_CARE_UPDATE_COLUMNS:
            if not self.contains_pk(update_columns):
                column_str += self.get_column_names_in_sql(tm.get_escape_pk_name_list(self.get_db_type())) + ","
            for col_idx, column in enumerate(update_columns):
                if col_idx > 0:
                    column_str += ","
                column_str += column
        else:
            for col_idx, column in enumerate(tm.all_columns.keys()):
                if col_idx > 0:
                    column_str += ","
                column_str += ColumnUtils.add_by_col_dbtype(column, self.get_db_type())

        return prefix + column_str + suffix

    def after_image(self, before_image: TableRecords):
        tm = self.get_table_meta()
        if before_image is None or before_image.size() == 0:
            return TableRecords.empty(tm)
        select_sql = self.__build_after_image_sql(tm, before_image)

        cursor = None
        try:
            con = self.cursor_proxy.get_connection()
            cursor = con.cursor()
            params = SQLUtil.set_param_for_pk(before_image.pk_rows(), tm.get_primary_key_only_name())
            cursor.execute(select_sql, tuple(params))
            rs_all = cursor.fetchall()
            description = cursor.description
            return TableRecords.build_records(tm, rs_all, description)
        finally:
            if cursor is not None:
                try:
                    cursor.close()
                except Exception:
                    pass

    def __build_after_image_sql(self, tm, before_image):
        prefix = "SELECT "
        where_sql = SQLUtil.build_where_condition_by_pks(tm.get_primary_key_only_name(), len(before_image.rows),
                                                         self.get_db_type())
        suffix = " FROM " + self.get_from_table_in_sql() + " WHERE " + where_sql
        column_str = ""
        if self.ONLY_CARE_UPDATE_COLUMNS:
            update_columns = self.sql_recognizer.get_update_columns()
            if not self.contains_pk(update_columns):
                column_str += self.get_column_names_in_sql(tm.get_escape_pk_name_list(self.get_db_type())) + ","
            for col_idx, column in enumerate(update_columns):
                if col_idx > 0:
                    column_str += ","
                column_str += column
        else:
            for col_idx, column in enumerate(tm.all_columns.keys()):
                if col_idx > 0:
                    column_str += ","
                column_str += ColumnUtils.add_by_col_dbtype(column, self.get_db_type())

        return prefix + column_str + suffix


class SelectForUpdateExecutor(BaseTransactionalExecutor):
    # TODO
    RETRY_TIMES = None
    RETRY_INTERNAL = None

    def __init__(self, cursor_proxy, cursor_callback, sql_recognizer):
        super(SelectForUpdateExecutor, self).__init__(cursor_proxy, cursor_callback, sql_recognizer)

        if self.RETRY_TIMES is None:
            self.RETRY_TIMES = ConfigFactory.get_config().get_int('client.rm.lock.retry-times')

        if self.RETRY_INTERNAL is None:
            self.RETRY_INTERNAL = ConfigFactory.get_config().get_float('client.rm.lock.retry-interval')

    def do_execute(self, args):
        try:
            param_list = []
            select_pk_sql = self.__build_select_sql(param_list)
            while True:
                try:
                    self.cursor_callback.execute(self.cursor_proxy.target_cursor, self.cursor_proxy.target_sql, args)
                    pk_rows = self.build_table_records(self.get_table_meta(), select_pk_sql, param_list)
                    lock_keys = self.build_lock_key(pk_rows)
                    if lock_keys is None or len(lock_keys.strip()) == 0:
                        break
                    if RootContext.in_global_transaction() or RootContext.require_global_lock():
                        self.cursor_proxy.connection_proxy.check_lock(lock_keys)
                    else:
                        raise RuntimeError('Unknown situation')
                    break
                except LockConflictException as e:
                    retry_times = self.RETRY_TIMES
                    retry_times -= 1
                    if retry_times < 0:
                        raise LockWaitTimeoutException('Global lock wait timeout', e)
                    try:
                        time.sleep(self.RETRY_INTERNAL)
                    except Exception:
                        pass
        finally:
            pass

    def __build_select_sql(self, param_list):
        recognizer = self.sql_recognizer
        select_sql = "SELECT "
        select_sql += self.get_column_names_in_sql(self.get_table_meta().get_escape_pk_name_list(self.get_db_type()))
        select_sql += (" FROM " + self.get_from_table_in_sql())
        where_condition = self.build_where_condition(recognizer, param_list)
        if where_condition is not None and len(where_condition.strip()) > 0:
            select_sql += where_condition
        select_sql += " FOR UPDATE"
        return select_sql


class DeleteExecutor(DMLBaseExecutor):

    def before_image(self):
        recognizer = self.sql_recognizer
        tm = self.get_table_meta(recognizer.get_table_name())
        param_list = []
        select_sql = self.__build_before_image_sql(recognizer, tm, param_list)
        return self.build_table_records(tm, select_sql, param_list)

    def __build_before_image_sql(self, recognizer, tm, param_list):
        where_condition = self.build_where_condition(recognizer, param_list)
        suffix = (" FROM " + self.get_from_table_in_sql())
        if where_condition is not None and len(where_condition.strip()) > 0:
            suffix += where_condition
        order_by = self.build_order_by_condition(recognizer, param_list)
        if order_by is not None and len(order_by.strip()) > 0:
            suffix += order_by
        limit = self.build_limit_condition(recognizer, param_list)
        if limit is not None and len(limit.strip()) > 0:
            suffix += limit
        suffix += " FOR UPDATE"
        columns = []
        for col_idx, column in enumerate(tm.all_columns.keys()):
            columns.append(self.get_column_name_in_sql(ColumnUtils.add_by_col_dbtype(column, self.get_db_type())))
        return "SELECT " + (', '.join(columns)) + suffix

    def after_image(self, before_image: TableRecords):
        return TableRecords.empty(self.get_table_meta())
