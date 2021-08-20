#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.NeedSubclassImplemented import NeedSubclassImplemented


class UndoLogParser:
    def get_name(self):
        raise NeedSubclassImplemented()

    def get_default_content(self):
        raise NeedSubclassImplemented()

    def encode(self, branch_undo_log):
        raise NeedSubclassImplemented()

    def decode(self, bytes_):
        raise NeedSubclassImplemented()
