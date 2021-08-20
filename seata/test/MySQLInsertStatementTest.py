#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from antlr4 import *

from seata.sqlparser.mysql.antlr4.visit.MySQLInsertStatement import MySQLInsertStatement
from seata.sqlparser.mysql.antlr4.gen.MySqlLexer import MySqlLexer
from seata.sqlparser.mysql.antlr4.gen.MySqlParser import MySqlParser
from seata.sqlparser.mysql.antlr4.stream.NoCaseStringStream import NoCaseStringStream


def get_stmts(sql):
    lexer = MySqlLexer(NoCaseStringStream(sql))
    stream = CommonTokenStream(lexer)
    parser = MySqlParser(stream)
    stmts = parser.sqlStatements().sqlStatement()
    return stmts


def test_insert_sql():
    stmt = get_stmts("insert into test (id, name) values (?,?)")[0].dmlStatement().insertStatement()
    mis = MySQLInsertStatement(stmt)
    assert mis.table_name == "test"
    assert mis.insert_columns == ["id", "name"]

    rows = mis.values_list
    for i in range(len(rows)):
        row = rows[i]
        for j in range(len(row)):
            assert row[j].value == "?"


def test_insert_values():
    stmt = get_stmts("insert into test (id, name) values (?,?), (?,?)")[0].dmlStatement().insertStatement()
    mis = MySQLInsertStatement(stmt)
    pass


if __name__ == '__main__':
    test_insert_sql()
    # test_insert_values()
    print()
