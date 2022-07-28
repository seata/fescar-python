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


class SQLUndoLog(object):
    def __int__(self):
        # SQLType
        self.sql_type = None
        self.table_name = None
        # TableRecords
        self.before_image = None
        self.after_image = None

    def set_table_meta(self, table_meta):
        if self.before_image is not None:
            self.before_image.set_table_meta(table_meta)
        if self.after_image is not None:
            self.after_image.set_table_meta(table_meta)
