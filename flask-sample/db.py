# -- coding: utf-8 --

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

import pymysql
from dbutils.pooled_db import PooledDB
from seata.rm.datasource.DataSourceProxy import DataSourceProxy
from seata.sqlparser.util.JdbcConstants import JdbcConstants

import pool_config


def get_pool():
    host = pool_config.host
    port = pool_config.port
    user = pool_config.user
    password = pool_config.password
    database = pool_config.database
    return PooledDB(creator=pymysql, host=host, port=port, user=user, password=password, database=database)


class DB:
    pool = None
    data_source_proxy = None

    @classmethod
    def init(cls):
        if cls.pool is None:
            cls.pool = get_pool()
        if cls.data_source_proxy is None:
            cls.data_source_proxy = DataSourceProxy(cls.pool, JdbcConstants.MYSQL)

    @classmethod
    def get_data_source(cls):
        return cls.data_source_proxy
