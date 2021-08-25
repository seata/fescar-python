#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class UndoLogParser:
    def get_name(self):
        raise NotImplemented("need subclass implemented")

    def get_default_content(self):
        raise NotImplemented("need subclass implemented")

    def encode(self, branch_undo_log):
        raise NotImplemented("need subclass implemented")

    def decode(self, bytes_):
        raise NotImplemented("need subclass implemented")
