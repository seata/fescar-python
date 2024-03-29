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

from dbutils.pooled_db import PooledDB

from seata.core.model.BranchType import BranchType
from seata.rm.datasource.ConnectionProxy import ConnectionProxy


class DataSourceProxy(object):

    def __init__(self, pool, db_type, resource_group_id="DEFAULT"):
        if not isinstance(pool, PooledDB):
            raise TypeError("Only support dbutils.pooled_db.PooledDB")

        self.pool = pool
        self.resource_group_id = resource_group_id
        kwargs = pool._kwargs
        port = 3306
        if kwargs['port'] is not None:
            port = kwargs['port']
        self.jdbc_url = "{}://{}:{}/{}".format(db_type, kwargs['host'], port, kwargs['database'])
        self.db_type = db_type
        self.username = kwargs['user']
        self.database = kwargs['database']

        self.init()

    def init(self):
        from seata.rm.DefaultResourceManager import DefaultResourceManager
        DefaultResourceManager.get().register_resource(self)

    def get_resource_id(self):
        return self.jdbc_url

    def get_branch_type(self):
        return BranchType.AT

    def connection(self):
        connection = self.get_origin_connection()
        return ConnectionProxy(self, connection)

    def get_origin_connection(self):
        connection = self.pool.connection()
        self.__set_dbtype_database(connection)
        return connection

    def steady_connection(self):
        steady_connection = self.pool.steady_connection()
        self.__set_dbtype_database(steady_connection)
        return ConnectionProxy(self, steady_connection)

    def dedicated_connection(self):
        dedicated_connection = self.pool.dedicated_connection()
        self.__set_dbtype_database(dedicated_connection)
        return ConnectionProxy(self, dedicated_connection)

    def unshare(self, con):
        self.pool.unshare(con)

    def cache(self, con):
        self.pool.cache(con)

    def close(self):
        self.pool.close()

    def __del__(self):
        self.pool.__del__()

    def _wait_lock(self):
        self.pool._wait_lock()

    def __set_dbtype_database(self, connection):
        connection.db_type = self.db_type
        connection.database = self.database
