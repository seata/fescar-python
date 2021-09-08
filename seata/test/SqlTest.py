#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
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


