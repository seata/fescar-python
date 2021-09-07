#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.mysql.antlr4.parser.mysql_base import MySqlBase, MysqlStatementVisitor, UpdateStatement
from seata.sqlparser.mysql.antlr4.visit.MySQLUpdateStatement import MySQLUpdateStatement


def get_stmts(sql):
    parser = MySqlBase.parser(sql)
    ss = parser.sqlStatements().sqlStatement()
    return ss


if __name__ == '__main__':
    stmt = get_stmts("update test t set t.id = ?, t.name = ? where t.name like '%1%'")[0]
    s = MysqlStatementVisitor().visit(stmt)
    us = MySQLUpdateStatement(s)
    assert us.table_name == 'test'
    assert us.table_alias == 't'
    assert us.items[0].column == 't.id'
    assert us.items[1].column == 't.name'
