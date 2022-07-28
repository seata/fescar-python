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


class ColumnMeta(object):

    def __init__(self):
        self.table_cat = None
        self.table_schema_name = None
        self.table_name = None
        self.column_name = None
        self.data_type = None
        self.data_type_name = None
        self.column_size = None
        self.decimal_digits = None
        self.num_prec_radix = None
        self.null_able = None
        self.remarks = None
        self.column_def = None
        self.sql_data_type = None
        self.sql_datetime_sub = None
        self.char_octet_length = None
        self.ordinal_position = None
        self.is_nullable = None
        self.is_autoincrement = None

    def is_auto_increment(self):
        return self.is_autoincrement == "YES"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
