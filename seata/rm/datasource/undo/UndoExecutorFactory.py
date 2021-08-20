#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException

from seata.sqlparser.SQLType import SQLType


class UndoExecutorFactory:
    @classmethod
    def get_undo_executor(cls, db_type, sql_undo_log):
        from seata.rm.datasource.undo.UndoExecutorHolderFactory import UndoExecutorHolderFactory
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
