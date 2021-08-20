#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class UndoLogParserFactory:
    DEFAULT_SERIALIZER = "protobuf"

    @classmethod
    def get_instance(cls, serializer=None):
        if serializer is None:
            serializer = cls.DEFAULT_SERIALIZER
        if serializer == cls.DEFAULT_SERIALIZER:
            from seata.rm.datasource.undo.parser.ProtobufUndoLogParser import ProtobufUndoLogParser
            return ProtobufUndoLogParser()
        raise NotImplemented()

