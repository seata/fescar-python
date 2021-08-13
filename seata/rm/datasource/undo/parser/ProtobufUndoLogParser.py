#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.rm.datasource.undo.BranchUndoLog import BranchUndoLog
from seata.rm.datasource.undo.UndoLogParserFactory import UndoLogParser
import json


class ProtobufUndoLogParser(UndoLogParser):

    def get_name(self):
        return "protobuf"

    def get_default_content(self):
        return self.encode(BranchUndoLog())

    def encode(self, branch_undo_log):
        return json.dumps(branch_undo_log).encode('utf-8')

    def decode(self, bytes_):
        pass
