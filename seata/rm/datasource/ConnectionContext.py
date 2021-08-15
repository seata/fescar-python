#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException


class ConnectionContext(object):
    P = "default"

    def __init__(self):
        self.xid = None
        self.branch_id = None
        self.is_global_lock_require = False
        self.lock_keys_buffer = set()
        self.sql_undo_items_buffer = {self.P: []}
        self.autocommit_changed = False

    def append_lock_key(self, lock_key):
        self.lock_keys_buffer.add(lock_key)

    def append_undo_item(self, sql_undo_log):
        self.sql_undo_items_buffer.get(self.P).append(sql_undo_log)

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
        return len(self.sql_undo_items_buffer.get(self.P)) > 0

    def reset(self, xid=None):
        self.xid = xid
        self.branch_id = None
        self.is_global_lock_require = False
        self.lock_keys_buffer.clear()
        self.sql_undo_items_buffer.get(self.P).clear()

    def build_lock_keys(self):
        if len(self.lock_keys_buffer) == 0:
            return None
        appender = ""
        for idx, key_buffer in enumerate(self.lock_keys_buffer):
            appender += key_buffer
            if idx != len(self.lock_keys_buffer) - 1:
                appender += ";"
        return appender

    def get_undo_items(self):
        undo_items = []
        us = self.sql_undo_items_buffer.get(self.P)
        for i in range(len(us)):
            undo_items.append(us[i])
        return undo_items
