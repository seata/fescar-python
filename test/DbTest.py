#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

import mariadb
from dbutils.pooled_db import PooledDB

if __name__ == '__main__':
    host = "mariadb.host"
    port = 3306
    user = "root"
    password = "mariadb123!"
    database = "istock"

    pool = PooledDB(creator=mariadb, host=host, port=port, user=user, password=password, database=database)
    conn = pool.connection()
    print(conn)

