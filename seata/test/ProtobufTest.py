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
from seata.rm.datasource.sql.struct.ColumnMeta import ColumnMeta
from seata.rm.datasource.sql.struct.IndexMeta import IndexMeta
from seata.rm.datasource.sql.struct.TableMeta import TableMeta
from seata.rm.datasource.sql.struct.TableRecords import TableRecords
from seata.rm.datasource.undo.BranchUndoLog import BranchUndoLog
from seata.rm.datasource.undo.SQLUndoLog import SQLUndoLog
from seata.rm.datasource.undo.parser.proto import branch_undolog_pb2
from seata.sqlparser.SQLType import SQLType


def test_protobuf():
    # dic_obj = {}
    # request = json_format.ParseDict(dic_obj, branch_undolog_pb2.BranchUndoLog())
    # dic_result = json_format.MessageToDict(request)

    b = branch_undolog_pb2.BranchUndoLog()
    b.xid = "1"
    c = b.SerializeToString()
    print(c)


def test_vars():
    table_name = "test"
    bul = BranchUndoLog()
    bul.xid = "1"
    bul.branch_id = "1"
    sul = SQLUndoLog()
    sul.sql_type = SQLType.INSERT
    sul.table_name = table_name
    tm = TableMeta()
    tm.table_name = table_name
    cm = ColumnMeta()
    cm.table_name = table_name
    cm.column_name = "id"
    cm.data_type_name = "int"
    cm.is_autoincrement = "YES"
    cm1 = ColumnMeta()
    cm1.table_name = table_name
    cm1.column_name = "name"
    cm1.data_type_name = "varchar"
    cm1.is_autoincrement = "NO"
    tm.all_columns = {"id": cm, "name": cm1}
    im = IndexMeta()
    im.values = [cm]
    im.non_unique = False
    im.index_name = "PRIMARY"
    tm.all_indexs = {"PRIMARY": im}
    sul.before_image = TableRecords.empty(tm)
    sul.after_image = TableRecords.empty(tm)
    bul.sql_undo_logs = [sul]
    a = ClassUtil.obj_to_dic(bul)
    bul1 = BranchUndoLog()
    pb_bul = json_format.ParseDict(a, branch_undolog_pb2.BranchUndoLog())
    print(pb_bul)


if __name__ == '__main__':
    # test_protobuf()
    test_vars()
    print()
