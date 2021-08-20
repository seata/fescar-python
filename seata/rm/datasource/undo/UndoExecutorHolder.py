#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


class UndoExecutorHolder:
    def get_insert_executor(self, sql_undo_log):
        from seata.exception.NeedSubclassImplemented import NeedSubclassImplemented
        raise NeedSubclassImplemented()

    def get_update_executor(self, sql_undo_log):
        from seata.exception.NeedSubclassImplemented import NeedSubclassImplemented
        raise NeedSubclassImplemented()

    def get_delete_executor(self, sql_undo_log):
        from seata.exception.NeedSubclassImplemented import NeedSubclassImplemented
        raise NeedSubclassImplemented()
