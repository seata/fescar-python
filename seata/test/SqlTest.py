#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.rm.datasource.sql.SQLVisitorFactory import SQLVisitorFactory
from seata.sqlparser.util.JdbcConstants import JdbcConstants

if __name__ == '__main__':
    sql = "insert into test values(?, ?)"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print()

    sql = "insert ignore into test values(?, ?)"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print()

    sql = "delete from test where a = ?"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print()

    sql = "update test set a = ? where b = ?"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print()

    sql = "select * from test"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print()

    sql = "select * from test for update"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print()

    sql = "show create table test"
    sql_recognizer = SQLVisitorFactory.get(sql, JdbcConstants.MYSQL)
    print()


