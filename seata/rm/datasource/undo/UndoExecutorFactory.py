#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.DataCompareUtil import DataCompareUtil
from seata.rm.datasource.exception.SQLException import SQLException
from seata.sqlparser.SQLType import SQLType
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class UndoExecutorFactory:
    @classmethod
    def get_undo_executor(cls, db_type, sql_undo_log, connection):
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

    def __init__(self, sql_undo_log):
        self.sql_undo_log = sql_undo_log

    def build_undo_sql(self):
        pass

    def get_undo_rows(self):
        pass

    def execute_on(self, connection):
        if self.IS_UNDO_DATA_VALIDATION_ENABLE and not self.data_validation_and_go_on(connection):
            return

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
        pass


class MySQLUndoInsertExecutor(UndoExecutor):
    def __init__(self, sql_undo_log):
        super(MySQLUndoInsertExecutor, self).__init__(sql_undo_log)


class MySQLUndoUpdateExecutor(UndoExecutor):
    def __init__(self, sql_undo_log):
        super(MySQLUndoUpdateExecutor, self).__init__(sql_undo_log)


class MySQLUndoDeleteExecutor(UndoExecutor):
    def __init__(self, sql_undo_log):
        super(MySQLUndoDeleteExecutor, self).__init__(sql_undo_log)


class UndoExecutorHolderFactory:
    __HOLDER_MAP = {}

    @classmethod
    def get_undo_executor_holder(cls, db_type):
        if cls.__HOLDER_MAP[db_type] is not None:
            return cls.__HOLDER_MAP[db_type]
        if db_type == JdbcConstants.MYSQL:
            cls.__HOLDER_MAP[db_type] = MySQLUndoExecutorHolder()
            return cls.__HOLDER_MAP[db_type]
        raise NotImplemented("db type : " + db_type)
