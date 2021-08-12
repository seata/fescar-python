#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from antlr4 import *

from seata.sqlparser.mysql.antlr4.MySqlLexer import MySqlLexer
from seata.sqlparser.mysql.antlr4.MySqlParser import MySqlParser
from seata.sqlparser.mysql.antlr4.MySqlParserVisitor import MySqlParserVisitor
from seata.sqlparser.mysql.antlr4.MySqlParserListener import MySqlParserListener
from seata.sqlparser.mysql.antlr4.stream.NoCaseStringStream import NoCaseStringStream


class PrintListener(MySqlParserListener):
    def enterRoot(self, ctx):
        print("root", ctx.getText())

    def enterSqlStatements(self, ctx):
        print("sqls", ctx.getText())

    def enterSqlStatement(self, ctx):
        print("sql", ctx.getText(), type(ctx))
        for child in ctx.getChildren():
            if isinstance(child, MySqlParser.DmlStatementContext):
                print("dml", child)
                self.printContent(child, 0)
        # print ctx.getChild(0).getText()

    def _enterFromClause(self, ctx):
        print(ctx.getText())

    def printContent(self, ctx, i):
        print("print context: %s" % i, type(ctx), ctx.getText())
        if isinstance(ctx, tree.Tree.TerminalNodeImpl):
            return
        for child in ctx.getChildren():
            self.printContent(child, i + 1)


def test1(sql):
    in_ = NoCaseStringStream(sql)
    # in_ = InputStream(sql)
    lexer = MySqlLexer(in_)
    stream = CommonTokenStream(lexer)
    parser = MySqlParser(stream)
    tree = parser.root()
    printer = PrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    pass


def test2(sql):
    lexer = MySqlLexer(NoCaseStringStream(sql))
    stream = CommonTokenStream(lexer)
    parser = MySqlParser(stream)
    stmts = parser.sqlStatements().sqlStatement()
    for i in range(len(stmts)):
        stmt = stmts[i]
        if stmt.dmlStatement().insertStatement() is not None:
            print("insert")
        elif stmt.dmlStatement().updateStatement() is not None:
            print("update")
        elif stmt.dmlStatement().deleteStatement() is not None:
            print("delete")
        elif stmt.dmlStatement().selectStatement() is not None:
            print("select")
    pass


if __name__ == '__main__':
    sql = """
    insert ignore into test values(?,?);
    insert into test (id, name) values (?,?);
    insert into test value (default, 'null', null, true, '1', 1, 1.0, now(6), format(250500.5634, 2));
    insert into test (a, b, c) values (1, 2, 3) on duplicate key update c = c + 1;
    """
    sql2 = """
    delete from test where id = ?;
    delete from test where id = 1;
    delete t from test t where t.id = ?;
    delete t from test t where t.id = 1;
    """
    sql3 = """
    update test set id = ?, name = ? where id = ?;
    update test set id = 1, name = ? where id = 1;
    update test set id = 1, name = '1' where id = 1;
    update test t set id = ?, name = ? where t.id = ?;
    """
    sql4 = """
    select * from test t where t.id = ?;
    select id, name from test where id = ?;
    select id, name from test where id = 1;
    """
    # test1(sql)
    test2(sql)
