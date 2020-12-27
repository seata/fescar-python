#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from exception.ShouldNeverHappenException import ShouldNeverHappenException


class ConnectionContext(object):

    def __init__(self):
        self.xid = None
        self.branch_id = None
        self.is_global_lock_require = False
        self.lock_keys_buffer = set()
        self.sql_undo_items_buffer = []

    def append_lock_key(self, lock_key):
        self.lock_keys_buffer.add(lock_key)

    def append_undo_item(self, sql_undo_log):
        self.sql_undo_items_buffer.append(sql_undo_log)

    def in_global_transaction(self):
        if self.xid is not None:
            return True
        return False

    def is_branch_registered(self):
        if self.branch_id is not None:
            return True
        return False

    def bind(self, xid):
        if xid is None:
            raise ValueError("xid is null")
        if not self.in_global_transaction():
            self.xid = xid
        else:
            if self.xid != xid:
                raise ShouldNeverHappenException("self.xid.[{}] != xid.[{}]".format(self.xid, xid))

    def has_undo_log(self):
        return len(self.sql_undo_items_buffer) > 0

    def reset(self, xid=None):
        self.xid = xid
        self.branch_id = None
        self.is_global_lock_require = False
        self.lock_keys_buffer.clear()
        self.sql_undo_items_buffer.clear()

    def build_lock_keys(self):
        if len(self.lock_keys_buffer) == 0:
            return None
        appender = ""
        for i in range(len(self.lock_keys_buffer)):
            appender += self.lock_keys_buffer[i]
            if i != len(self.lock_keys_buffer) - 1:
                appender += ";"
        return appender
