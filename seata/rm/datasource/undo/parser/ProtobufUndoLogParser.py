# -*- coding: utf-8 -*-

"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from google.protobuf import json_format

from seata.core.util.ClassUtil import ClassUtil
from seata.rm.datasource.undo.BranchUndoLog import BranchUndoLog
from seata.rm.datasource.undo.UndoLogParser import UndoLogParser
from seata.rm.datasource.undo.parser.proto import branch_undolog_pb2


class ProtobufUndoLogParser(UndoLogParser):
    def get_name(self):
        return "protobuf"

    def get_default_content(self):
        return self.encode(BranchUndoLog())

    def encode(self, branch_undo_log):
        dic = ClassUtil.obj_to_dic(branch_undo_log, ignore_names=['table_meta'])
        bul_pb = json_format.ParseDict(dic, branch_undolog_pb2.BranchUndoLog(), ignore_unknown_fields=True)
        bs = bul_pb.SerializeToString()
        return bs

    def decode(self, bytes_):
        bul_pb = branch_undolog_pb2.BranchUndoLog()
        bul_pb.ParseFromString(bytes_)
        dic = json_format.MessageToDict(bul_pb, including_default_value_fields=True, preserving_proto_field_name=True)
        bul = BranchUndoLog(dic)
        return bul
