#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from am.mysql_base import MySqlBase, MysqlStatementVisitor, MysqlOutputVisitor

from seata.sqlparser.mysql.antlr4.visit.MySQLDeleteStatement import MySQLDeleteStatement
from seata.sqlparser.mysql.antlr4.visit.MySQLInsertStatement import MySQLInsertStatement
from seata.sqlparser.mysql.antlr4.visit.MySQLUpdateStatement import MySQLUpdateStatement


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


def test_update_sql():
    stmt = get_stmts("update test t set t.id = ?, t.name = ? where t.name like '%1%'")[0]
    s = MysqlStatementVisitor().visit(stmt)
    us = MySQLUpdateStatement(s)
    assert us.table_name == 'test'
    assert us.table_alias == 't'
    assert us.items[0].column == '.id'
    assert us.items[1].column == '.name'

    output = list()
    MysqlOutputVisitor().visitWhere(us.where, output)
    where_str = ''.join(output)
    assert where_str == " WHERE t.name LIKE '%1%'"

    stmt = get_stmts("update test set id = ?, name = ? where name like '%1%'")[0]
    s = MysqlStatementVisitor().visit(stmt)
    us = MySQLUpdateStatement(s)
    assert us.table_name == 'test'
    assert us.table_alias is None
    assert us.items[0].column == 'id'
    assert us.items[1].column == 'name'

    output = list()
    MysqlOutputVisitor().visitWhere(us.where, output)
    where_str = ''.join(output)
    assert where_str == " WHERE name LIKE '%1%'"


def test_delete_sql():
    stmt = get_stmts("delete t from test t where t.id = ?")[0]
    s = MysqlStatementVisitor().visit(stmt)
    ds = MySQLDeleteStatement(s)
    assert ds.table_name == 'test'
    assert ds.table_alias == 't'

    output = list()
    MysqlOutputVisitor().visitWhere(ds.where, output)
    where_str = ''.join(output)
    assert where_str == " WHERE t.id = ?"

    stmt = get_stmts("delete from test where id = ?")[0]
    s = MysqlStatementVisitor().visit(stmt)
    ds = MySQLDeleteStatement(s)
    assert ds.table_name == 'test'
    assert ds.table_alias is None

    output = list()
    MysqlOutputVisitor().visitWhere(ds.where, output)
    where_str = ''.join(output)
    assert where_str == " WHERE id = ?"


if __name__ == '__main__':
    test_insert_sql()
    test_update_sql()
    test_delete_sql()
    print()
