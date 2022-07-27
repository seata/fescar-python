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

from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException
from seata.rm.datasource.sql.SQLVisitorFactory import SQLVisitorFactory
from seata.sqlparser.util.JdbcConstants import JdbcConstants

if __name__ == '__main__':
    sql = "insert into test values(?, ?)"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print(1)

    sql = "insert ignore into test values(?, ?)"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print(2)

    sql = "delete from test where a = ?"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print(3)

    sql = "update test set a = ? where b = ?"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print(4)

    sql = "select * from test"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print(5)

    sql = "select * from test for update"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print(6)

    try:
        sql = "show create table test"
        sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    except ShouldNeverHappenException:
        print(7)


