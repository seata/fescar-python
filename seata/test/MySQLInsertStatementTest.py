#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from seata.sqlparser.mysql.antlr4.parser.mysql_base import MySqlBase, MysqlStatementVisitor
from seata.sqlparser.mysql.antlr4.visit.MySQLInsertStatement import MySQLInsertStatement


def get_stmts(sql):
    ss = MySqlBase.parserSQLStatement(sql)
    return ss


def test_insert_sql():
    stmt = get_stmts("insert into test (id, name) values (?,?)")[0]
    s = MysqlStatementVisitor().visit(stmt)
    mis = MySQLInsertStatement(s)
    assert mis.table_name == "test"
    assert mis.columns == ["id", "name"]

    rows = mis.values_list
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            assert row[j].value == "?"


if __name__ == '__main__':
    test_insert_sql()
    print()
