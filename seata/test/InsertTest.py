#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import mariadb
from dbutils.pooled_db import PooledDB

from seata.Boostrap import Bootstrap
from seata.rm.RMClient import RMClient
from seata.rm.datasource.PooledDBProxy import PooledDBProxy
from seata.sqlparser.util.JdbcConstants import JdbcConstants
from seata.tm.TMClient import TMClient

if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8091

    tm_client = TMClient.get()
    tm_client.application_id = "test"
    tm_client.transaction_service_group = "my_test_tx_group"
    tm_client.init_client(host, port)

    rm_client = RMClient.get()
    rm_client.application_id = tm_client.application_id
    rm_client.transaction_service_group = tm_client.transaction_service_group
    rm_client.init_client(host, port)

    Bootstrap.start()

    pool = PooledDB(creator=mariadb, host="mariadb.dev", port=3306, user="root", password="root", database="test")

    pool_proxy = PooledDBProxy(pool, JdbcConstants.MYSQL)

    cp = pool_proxy.connection()

    cursor = cp.cursor()
    cursor.execute("insert into test(id, name) values(?, ?)", (None, "name1"))
    cp.commit()
    print("success")
