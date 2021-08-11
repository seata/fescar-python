#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from antlr4 import *

# from seata.sqlparser.mysql.antlr4.MySQLStatementLexer import MySQLStatementLexer
# from seata.sqlparser.mysql.antlr4.MySQLStatementParser import MySQLStatementParser
# from seata.sqlparser.mysql.antlr4.MySQLStatementVisitor import MySQLStatementVisitor
# from seata.sqlparser.mysql.antlr4.MySQLStatementListener import MySQLStatementListener
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
    stmt_ctx = parser.sqlStatements()
    stmt_ctxs = stmt_ctx.sqlStatement()
    for i in range(len(stmt_ctxs)):
        stmt = stmt_ctxs[i]
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
    # sql = "SELECT * FROM test t WHERE id = ? FOR UPDATE"
    sql = "insert into test (id, name) values (?, ?)"
    # sql = "select a from tb_test where name = ?"
    # test1(sql)
    test2(sql)
