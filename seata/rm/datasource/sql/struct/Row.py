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

from seata.rm.datasource.sql.struct.KeyType import KeyType


class Row(object):

    def __init__(self):
        # Field
        self.fields = []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def add(self, field):
        self.fields.append(field)

    def primary_keys(self):
        keys = []
        for i in range(len(self.fields)):
            f = self.fields[i]
            if f.key_type == KeyType.PRIMARY_KEY:
                keys.append(f)
        return keys

    def non_primary_keys(self):
        keys = []
        for i in range(len(self.fields)):
            f = self.fields[i]
            if f.key_type != KeyType.PRIMARY_KEY:
                keys.append(f)
        return keys
