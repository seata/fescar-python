# -*- coding: utf-8 -*-

"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

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
