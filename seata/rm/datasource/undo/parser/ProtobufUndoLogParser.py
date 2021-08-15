#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.util.ClassUtil import ClassUtil
from seata.rm.datasource.undo.BranchUndoLog import BranchUndoLog
from seata.rm.datasource.undo.UndoLogParserFactory import UndoLogParser

from seata.rm.datasource.undo.parser.proto import branch_undolog_pb2

from google.protobuf import json_format


class ProtobufUndoLogParser(UndoLogParser):
    def get_name(self):
        return "protobuf"

    def get_default_content(self):
        return self.encode(BranchUndoLog())

    def encode(self, branch_undo_log):
        dic = ClassUtil.obj_to_dic(branch_undo_log)
        return json_format.ParseDict(branch_undolog_pb2.BranchUndoLog, dic)

    def decode(self, bytes_):
        dic = json_format.MessageToDict(bytes_)
        return BranchUndoLog(dic)
