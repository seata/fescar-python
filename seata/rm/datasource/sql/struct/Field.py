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

import datetime
import time

from seata.rm.datasource.sql.struct.KeyType import KeyType
from seata.rm.datasource.Types import Types


class Field(object):

    def __init__(self):
        self.name = None
        self.key_type = KeyType.NULL
        self.type = 0
        # any
        self.value = None

    def set_value(self, value):
        result = None
        if self.type == Types.BIT or \
                self.type == Types.BLOB:
            result = str(self.value)
        elif self.type == Types.TINYINT or \
                self.type == Types.SMALLINT or \
                self.type == Types.INTEGER or \
                self.type == Types.INT or \
                self.type == Types.BIGINT or \
                self.type == Types.FLOAT or \
                self.type == Types.REAL or \
                self.type == Types.DOUBLE or \
                self.type == Types.NUMERIC or \
                self.type == Types.DECIMAL or \
                self.type == Types.CHAR or \
                self.type == Types.VARCHAR or \
                self.type == Types.LONGVARCHAR or \
                self.type == Types.TINYTEXT or \
                self.type == Types.TEXT or \
                self.type == Types.MEDIUMTEXT or \
                self.type == Types.LONGTEXT or \
                self.type == Types.JSON:
            result = str(value)
        elif self.type == Types.DATE:
            if isinstance(value, str):
                result = value
            else:
                # datetime.date
                result = value.strftime('%Y-%m-%d')
        elif self.type == Types.TIME:
            if isinstance(value, str):
                result = value
            else:
                # time.timedelta
                result = value.strftime('%H:%M:%S.%f')
        elif self.type == Types.DATETIME:
            if isinstance(value, str):
                result = value
            else:
                # datetime.datetime
                result = value.strftime('%Y-%m-%d %H:%M:%S.%f')
        else:
            result = str(self.value)
        self.value = result

    def get_value(self):
        val_str = self.value
        if self.type == Types.TINYINT or \
                self.type == Types.SMALLINT or \
                self.type == Types.INTEGER or \
                self.type == Types.INT or \
                self.type == Types.BIGINT or \
                self.type == Types.NUMERIC:
            return int(val_str)
        elif self.type == Types.FLOAT or \
                self.type == Types.REAL or \
                self.type == Types.DOUBLE or \
                self.type == Types.DECIMAL:
            return float(val_str)
        elif self.type == Types.CHAR or \
                self.type == Types.VARCHAR or \
                self.type == Types.LONGVARCHAR or \
                self.type == Types.TINYTEXT or \
                self.type == Types.TEXT or \
                self.type == Types.MEDIUMTEXT or \
                self.type == Types.LONGTEXT or \
                self.type == Types.JSON:
            return val_str
        elif self.type == Types.DATE:
            string = val_str
            return datetime.datetime.strptime(string, "%Y-%m-%d").date()
        elif self.type == Types.TIME:
            string = val_str
            return datetime.datetime.strptime(string, "%H:%M:%S.%f").time()
        elif self.type == Types.DATETIME:
            string = val_str
            return datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S.%f")
        elif self.type == Types.BIT or \
                self.type == Types.BLOB:
            return val_str.decode('utf-8')
        else:
            return val_str

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
