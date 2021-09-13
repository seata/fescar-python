#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import datetime
import os
import time

import pymysql
from dbutils.pooled_db import PooledDB

from seata.boot.GlobalTransactionScanner import GlobalTransactionScanner
from seata.config.Configuration import Configuration
from seata.rm.datasource.DataSourceProxy import DataSourceProxy
from seata.sqlparser.util.JdbcConstants import JdbcConstants
from seata.test import pool_config
from seata.tm.TransactionalTemplate import GlobalTransactional

pool = None
data_source_proxy = None


def get_pool():
    host = pool_config.host
    port = pool_config.port
    user = pool_config.user
    password = pool_config.password
    database = pool_config.database
    return PooledDB(creator=pymysql, host=host, port=port, user=user, password=password, database=database)


def init():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    Configuration(base_dir + '/script/client.yml')

    GlobalTransactionScanner()

    global pool
    pool = get_pool()
    global data_source_proxy
    data_source_proxy = DataSourceProxy(pool, JdbcConstants.MYSQL)


@GlobalTransactional()
def test_insert():
    insert_business()

    throw = True
    if throw:
        raise RuntimeError('trigger rollback')

    time.sleep(30)
    print('success')


def insert_business():
    cp = data_source_proxy.connection()

    cursor = cp.cursor()
    cursor.execute("insert into test(id, name, created) values(%s, %s, %s)",
                   (None, "name1", datetime.datetime.now()))

    cursor.execute("insert into test values(null, '1', '2021-08-30 12:01:01.001')")
    cp.commit()


@GlobalTransactional()
def test_update():
    update_business()

    throw = True
    if throw:
        raise RuntimeError('trigger rollback')

    time.sleep(30)
    print('success')


def update_business():
    cp = data_source_proxy.connection()
    cursor = cp.cursor()
    cursor.execute("update test t set t.name = %s, t.created = now() where t.id = %s",
                   ('name2', 1))
    cp.commit()


@GlobalTransactional()
def test_delete():
    delete_business(1)

    throw = False
    if throw:
        raise RuntimeError('trigger rollback')

    time.sleep(30)
    print('success')


def delete_business(a=None):
    cp = data_source_proxy.connection()

    cursor = cp.cursor()
    cursor.execute("delete t from test t where t.id = %s", (23,))

    cp.commit()


def select_for_update():
    cp = data_source_proxy.connection()

    cursor = cp.cursor()
    cursor.execute("select * from test t where t.id = %s for update", (18,))

    cp.commit()


@GlobalTransactional()
def test_select_for_update():
    select_for_update()

    delete_business(1)

    throw = True
    if throw:
        raise RuntimeError('trigger rollback')


def test_non_tx_insert():
    cp = data_source_proxy.connection()

    cursor = cp.cursor()
    cursor.execute("insert into test values (null, '1', now())")
    cp.commit()

    print('success')


@GlobalTransactional()
def test_var_name_insert():
    cp = data_source_proxy.connection()
    cursor = cp.cursor()
    # cursor.executemany("insert into test(id, name, created) values(null, %(name)s, %(created)s)",
    #                [{"name": "11", "created": datetime.datetime.now()},
    #                 {"name": "12", "created": datetime.datetime.now()}])
    # cursor.execute("insert into test(id, name, created) values(null, %(name)s, %(created)s)",
    #                ({"name": "11", "created": datetime.datetime.now()}))

    # cursor.execute("delete from test where id = %(id)s", ({"id": 33}))
    # cursor.executemany("delete from test where id = %(id)s", [{"id": 33}, {"id": 34}])

    # cursor.execute("update test set name = %(name)s, created = %(created)s where id = %(id)s",
    #                ({"name": "11", "created": datetime.datetime.now(), "id": 34}))
    cursor.executemany("update test set name = %(name)s, created = %(created)s where id = %(id)s",
                       [{"name": "34", "created": datetime.datetime.now(), "id": 34},
                        {"name": "35", "created": datetime.datetime.now(), "id": 35}])

    cp.commit()
    print('success')
    raise RuntimeError()


def test_get_table_meta():
    con = pool.connection()
    cursor = con.cursor()
    schema = con._pool._kwargs['database']
    sql = 'select * from information_schema.columns where table_name = %s and table_schema = %s'
    cursor.execute(sql, ('test', schema))
    rs_all = cursor.fetchall()
    for i in range(len(rs_all)):
        r = rs_all[i]
        print(r)
    pass


def test_get_low_case():
    con = pool.connection()
    cursor = con.cursor()
    sql = "select * from information_schema.global_variables WHERE variable_name = 'LOWER_CASE_TABLE_NAMES'"
    cursor.execute(sql)
    one = cursor.fetchone()
    print(one)
    pass


def test_insert_lastrowid():
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
    con = pool.connection()
    try:
        cursor = con.cursor()
        sql = "insert into test (id, name) values(1, 1)"
        cursor.execute(sql)
        con.commit()
    except Exception as e:
        print(e.__class__.mro())


@GlobalTransactional()
def test_dml():
    cp = data_source_proxy.connection()
    cursor = cp.cursor()
    cursor.execute("insert into test values(999, %s, %s)", ("11", datetime.datetime.now()))
    cp.commit()
    cursor.close()
    cp.close()

    cp = data_source_proxy.connection()
    cursor = cp.cursor()
    cursor.execute("update test set name = %(name)s, created = %(created)s where id = %(id)s",
                   {"name": "999", "created": datetime.datetime.now(), "id": 999})
    cp.commit()
    cursor.close()
    cp.close()

    cp = data_source_proxy.connection()
    cursor = cp.cursor()
    cursor.execute("delete from test where id = %s", (999,))
    cp.commit()
    cursor.close()
    cp.close()

    print("success")
    raise RuntimeError('rollback')


if __name__ == '__main__':
    init()
    # test_insert()
    # test_update()
    # test_delete()
    # test_select_for_update()
    # test_non_tx_insert()
    # test_var_name_insert()
    # test_dml()
    # test_get_table_meta()
    # test_get_low_case()
    # test_insert_lastrowid()
    # test_IntegrityError()
    print()
