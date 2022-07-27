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

from collections import OrderedDict

from seata.exception.NotSupportYetException import NotSupportYetException
from seata.rm.datasource.ColumnUtils import ColumnUtils
from seata.rm.datasource.sql.struct.IndexType import IndexType


class TableMeta(object):

    def __init__(self):
        self.table_name = None
        # key: column_name value: ColumnMeta
        self.all_columns = OrderedDict()
        # key: index_name value: IndexMeta
        self.all_indexs = OrderedDict()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_column_meta(self, col_name):
        return self.all_columns.get(col_name, None)

    def get_auto_increase_column(self):
        for k in self.all_columns:
            col = self.all_columns[k]
            if 'YES' == col.is_auto_increment():
                return col
        return None

    def get_primary_key_map(self):
        pk = dict()
        for k in self.all_indexs:
            index = self.all_indexs[k]
            if index.index_type.value == IndexType.PRIMARY.value:
                for col in index.values:
                    pk[col.column_name] = col
        if len(pk) < 1:
            raise NotSupportYetException('{} needs to contain the primary key'.format(self.table_name))
        return pk

    def get_primary_key_only_name(self):
        name_list = []
        key_map = self.get_primary_key_map()
        for k in key_map:
            name_list.append(k)
        return name_list

    def get_escape_pk_name_list(self, db_type):
        return ColumnUtils.add_escape_by_cols_dbtype(self.get_primary_key_only_name(), db_type)

    def contains_pk(self, cols):
        if cols is None:
            return False
        pk = self.get_primary_key_only_name()
        if len(pk) == 0:
            return False

        big = cols
        small = pk
        result = all(elem in big for elem in small)
        if result:
            return True
        else:
            big_a = [each.upper() for each in big]
            small_a = [each.upper() for each in small]
            return all(elem in big_a for elem in small_a)
