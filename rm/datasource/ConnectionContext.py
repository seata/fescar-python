#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class ConnectionContext(object):

    def __init__(self):
        self.xid = None
        self.branch_id = None
        self.is_global_lock_require = False
        self.lock_keys_buffer = set()
        self.sql_undo_items_buffer = []

    def append_lock_key(self, lock_key):
        self.lock_keys_buffer.add(lock_key)

    def append_undo_item(self):
        # TODO
        pass