#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import os
import time
import datetime

import pymysql
from dbutils.pooled_db import PooledDB

from seata.boot.GlobalTransactionScanner import GlobalTransactionScanner
from seata.config.Config import ConfigFactory
from seata.config.Configuration import Configuration
from seata.rm.datasource.DataSourceProxy import DataSourceProxy
from seata.sqlparser.util.JdbcConstants import JdbcConstants
from seata.test import pool_config
from seata.tm.api.GlobalTransactionContext import GlobalTransactionContext


def get_pool():
    host = pool_config.host
    port = pool_config.port
    user = pool_config.user
    password = pool_config.password
    database = pool_config.database
    return PooledDB(creator=pymysql, host=host, port=port, user=user, password=password, database=database)


def test_insert():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    Configuration(base_dir + '/script/client.yml')
    GlobalTransactionScanner()

    pool = get_pool()
    data_source_proxy = DataSourceProxy(pool, JdbcConstants.MYSQL)

    cp = data_source_proxy.connection()

    tx = GlobalTransactionContext.get_current_or_create()
    tx.begin()

    cursor = cp.cursor()
    cursor.execute("insert into test(id, name, created) values(%s, %s, %s)",
                   (None, "name1", datetime.datetime.now()))
    cp.commit()

    cursor2 = cp.cursor()
    cursor2.execute("insert into test values(null, '1', '2021-08-30 12:01:01.001')")
    cp.commit()

    tx.commit()
    # tx.rollback()
    time.sleep(30)
    print('success')


def test_update():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    Configuration(base_dir + '/script/client.yml')
    GlobalTransactionScanner()

    pool = get_pool()
    data_source_proxy = DataSourceProxy(pool, JdbcConstants.MYSQL)

    cp = data_source_proxy.connection()

    tx = GlobalTransactionContext.get_current_or_create()
    tx.begin()

    cursor = cp.cursor()
    cursor.execute("update test t set t.name = %s, t.created = now() where t.id = %s",
                   ('name2', 1))
    cp.commit()

    # tx.commit()
    tx.rollback()
    time.sleep(30)
    print('success')


def test_get_table_meta():
    pool = get_pool()
    con = pool.connection()
    cursor = con.cursor()
    schema = con._pool._kwargs['database']
    sql = 'select * from information_schema.columns where table_name = %s and table_schema = %s'
    cursor.execute(sql, ('test', schema))
    all = cursor.fetchall()
    for i in range(len(all)):
        r = all[i]
        print(r)
    pass


def test_get_low_case():
    pool = get_pool()
    con = pool.connection()
    cursor = con.cursor()
    sql = "select * from information_schema.global_variables WHERE variable_name = 'LOWER_CASE_TABLE_NAMES'"
    cursor.execute(sql)
    one = cursor.fetchone()
    print(one)
    pass


def test_insert_lastrowid():
    pool = get_pool()
    con = pool.connection()
    cursor = con.cursor()
    sql = "insert into test (id, name) values(null, 1), (null, 2)"
    cursor.execute(sql)
    con.commit()
    print(cursor.lastrowid)
    print(cursor.lastrowid)
    print(cursor.rowcount)
    print()


def test_IntegrityError():
    pool = get_pool()
    con = pool.connection()
    try:
        cursor = con.cursor()
        sql = "insert into test (id, name) values(1, 1)"
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        print(e.__class__.mro())


if __name__ == '__main__':
    # test_insert()
    test_update()
    # test_get_table_meta()
    # test_get_low_case()
    # test_insert_lastrowid()
    # test_IntegrityError()
    print()
