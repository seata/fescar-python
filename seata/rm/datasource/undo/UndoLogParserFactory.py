#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


class UndoLogParserFactory:

    DEFAULT_SERIALIZER = "json"

    @classmethod
    def get_instance(cls, serializer=None):
        if serializer is None:
            serializer = cls.DEFAULT_SERIALIZER
        if serializer == cls.DEFAULT_SERIALIZER:
            return JsonUndoLogParser()
        raise NotImplemented()


class UndoLogParser:

    def get_name(self):
        pass

    def get_default_content(self):
        pass

    def encode(self, branch_undo_log):
        pass

    def decode(self, bytes_):
        pass


class JsonUndoLogParser(UndoLogParser):

    def get_name(self):
        pass

    def get_default_content(self):
        pass

    def encode(self, branch_undo_log):
        pass

    def decode(self, bytes_):
        pass
