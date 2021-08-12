#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from dbutils.pooled_db import PooledDB
from seata.rm.datasource.ConnectionProxy import ConnectionProxy


class PooledDBProxy(object):

    def __init__(self, pool, db_type, resource_group_id="DEFAULT"):
        if not isinstance(pool, PooledDB):
            raise TypeError("Only support dbutils.pooled_db.PooledDB")

        self.pool = pool
        self.resource_group_id = resource_group_id
        kwargs = pool._kwargs
        port = 3306
        if kwargs['port'] is not None:
            port = kwargs['port']
        self.jdbc_url = "{}:{}:{}/{}".format(db_type, kwargs['host'], port, kwargs['database'])
        self.db_type = db_type
        self.username = kwargs['user']
        self.database = kwargs['database']

        from seata.rm.ATResourceManager import ATResourceManager
        ATResourceManager.get().register_resource(self)

    def get_resource_id(self):
        return self.jdbc_url

    def connection(self):
        return ConnectionProxy(self, self.pool.connection())

    def get_origin_connection(self):
        return self.pool.connection()

    def steady_connection(self):
        return ConnectionProxy(self, self.pool.steady_connection())

    def dedicated_connection(self):
        return ConnectionProxy(self, self.pool.dedicated_connection())

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
