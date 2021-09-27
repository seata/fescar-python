#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
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
