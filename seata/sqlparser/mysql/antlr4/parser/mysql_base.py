#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

# https://github.com/jsbxyyx/antlr4-mysql

from antlr4 import *

from .autogen.MySqlBaseLexer import MySqlBaseLexer
from .autogen.MySqlBaseParser import MySqlBaseParser
from .autogen.MySqlBaseParserVisitor import MySqlBaseParserVisitor

debug = False


def log(value, args=None):
    if debug:
        print(value, args)


class MySqlBase:

    @classmethod
    def parser(cls, sql):
        lexer = MySqlBaseLexer(InputStream(sql))
        stream = CommonTokenStream(lexer)
        parser = MySqlBaseParser(stream)
        return parser

    @classmethod
    def parserSQLStatement(cls, sql):
        parser = cls.parser(sql)
        return parser.sqlStatements().sqlStatement()


class LockClause:
    def __init__(self):
        self.forUpdate = None
        pass


class NullPredicate:
    def __init__(self):
        self.predicate = None
        self.NOT = None
        pass


class LikePredicate:
    def __init__(self):
        self.predicate1 = None
        self.NOT = None
        self.predicate2 = None
        pass


class LogicalExpression:
    def __init__(self):
        self.expression1 = None
        self.logicalOperator = None
        self.expression2 = None


class NotExpression:
    def __init__(self):
        self.expression = None


class BetweenPredicate:
    def __init__(self):
        self.predicate1 = None
        self.NOT = None
        self.predicate2 = None
        self.predicate3 = None
        pass


class UpdateElement:
    def __init__(self):
        self.column = None
        self.value = None
        pass


class WhereClause:
    def __init__(self):
        self.expression = None


class Expression:
    def __init__(self):
        pass


class InPredicate:
    def __init__(self):
        self.predicate = None
        self.NOT = None
        self.expressions = list()


class ComparisonPredicate:
    def __init__(self):
        self.predicate1 = None
        self.comparisonOperator = None
        self.predicate2 = None


class PredicateAtom:
    def __init__(self):
        pass


class FullColumnName(PredicateAtom):
    def __init__(self):
        super(FullColumnName, self).__init__()
        self.owner = None
        self.value = None


class Constant(PredicateAtom):
    def __init__(self):
        super(Constant, self).__init__()


class FunctionCall(PredicateAtom):
    def __init__(self):
        super(FunctionCall, self).__init__()
        self.function_name = None
        self.args_list = None


class ParameterMarker(Constant):
    def __init__(self, index, name, value):
        self.index = index
        self.name = name
        self.value = value


class StringLiteral(Constant):
    def __init__(self, value):
        self.value = value[1:-1]


class DecimalLiteral(Constant):
    def __init__(self, value):
        self.value = int(value)


class HexadecimalLiteral(Constant):
    def __init__(self, value):
        self.value = value


class BooleanLiteral(Constant):
    def __init__(self, value):
        self.value = bool(value)


class RealLiteral(Constant):
    def __init__(self, value):
        self.value = float(value)


class NullLiteral(Constant):
    def __init__(self):
        self.value = None


class BitString(Constant):
    def __init__(self, value):
        self.value = value


class Default:
    def __init__(self):
        self.value = 'DEFAULT'


class SelectStatement:
    def __init__(self):
        self.selectElements = None
        self.tableSource = None
        self.where = None
        self.orderBy = None
        self.limit = None
        self.lock = None
        pass


class InsertStatement:
    def __init__(self):
        self.ignore = None
        self.tableSource = None
        self.columns = None
        self.value_list = None


class UpdateStatement:
    def __init__(self):
        self.tableSource = None
        self.updatedElement = None
        self.where = None
        self.orderBy = None
        self.limit = None


class DeleteStatement:
    def __init__(self):
        self.tableAlias = None
        self.tableSource = None
        self.where = None
        self.orderBy = None
        self.limit = None


class OrderByClause:
    def __init__(self):
        self.orderByExpressions = None


class OrderByExpression:
    def __init__(self):
        self.expression = None
        self.ASC = None


class LimitClause:
    def __init__(self):
        self.offset = None
        self.limit = None


class TableSource:
    def __init__(self):
        self.tableName = None
        self.tableAlias = None


class MysqlStatementVisitor(MySqlBaseParserVisitor):
    def __init__(self):
        self.parameter_marker_index = -1

    def visitSelectStatement(self, ctx: MySqlBaseParser.SelectStatementContext):
        log('visitSelectStatement')
        ss = SelectStatement()
        ss.selectElements = self.visit(ctx.selectElements())
        ss.tableSource = self.visit(ctx.tableSource())
        if ctx.whereClause() is not None:
            ss.where = self.visit(ctx.whereClause())
        if ctx.limitClause() is not None:
            ss.limit = self.visit(ctx.limitClause())
        if ctx.orderByClause() is not None:
            ss.orderBy = self.visit(ctx.orderByClause())
        if ctx.lockClause() is not None:
            ss.lock = self.visit(ctx.lockClause())
        return ss

    def visitInsertStatement(self, ctx: MySqlBaseParser.InsertStatementContext):
        log('visitInsertStatement')
        ins = InsertStatement()
        ins.ignore = ctx.IGNORE() is not None
        ins.tableSource = self.visit(ctx.tableSource())
        if ctx.uidList() is not None:
            ins.columns = self.visit(ctx.uidList())
        ins.value_list = self.visit(ctx.insertStatementValue())
        return ins

    def visitUpdateStatement(self, ctx: MySqlBaseParser.UpdateStatementContext):
        log('visitUpdateStatement')
        us = UpdateStatement()
        us.tableSource = self.visit(ctx.tableSource())
        elements = []
        ues = ctx.updatedElement()
        for i in range(len(ues)):
            elements.append(self.visit(ues[i]))
        us.updatedElement = elements
        if ctx.whereClause() is not None:
            us.where = self.visit(ctx.whereClause())
        if ctx.orderByClause() is not None:
            us.orderBy = self.visit(ctx.orderByClause())
        if ctx.limitClause() is not None:
            us.limit = self.visit(ctx.limitClause())
        return us

    def visitDeleteStatement(self, ctx: MySqlBaseParser.DeleteStatementContext):
        log('visitDeleteStatement')
        ds = DeleteStatement()
        if ctx.tableAlias() is not None:
            ds.tableAlias = self.visit(ctx.tableAlias())
        ds.tableSource = self.visit(ctx.tableSource())
        ds.where = self.visit(ctx.whereClause())
        if ctx.orderByClause() is not None:
            ds.orderBy = self.visit(ctx.orderByClause())
        if ctx.LIMIT() is not None:
            ds.limit = self.visit(ctx.decimalLiteral())
        return ds

    def visitInsertStatementValue(self, ctx: MySqlBaseParser.InsertStatementValueContext):
        log('visitInsertStatementValue')
        values = []
        eps = ctx.expressions()
        for i in range(len(eps)):
            values.append(self.visit(eps[i]))
        return values

    def visitSelectElements(self, ctx: MySqlBaseParser.SelectElementsContext):
        log('visitSelectElements')
        elements = []
        ses = ctx.selectElement()
        for i in range(len(ses)):
            elements.append(self.visit(ses[i]))
        return elements

    def visitSelectStarElement(self, ctx: MySqlBaseParser.SelectStarElementContext):
        log('visitSelectStarElement')
        return ctx.getText()

    def visitSelectColumnElement(self, ctx: MySqlBaseParser.SelectColumnElementContext):
        log('visitSelectColumnElement')
        return self.visit(ctx.fullColumnName())

    def visitTableSource(self, ctx: MySqlBaseParser.TableSourceContext):
        log('visitTableSource')
        ts = TableSource()
        ts.tableName = self.visit(ctx.tableName())
        if ctx.tableAlias() is not None:
            ts.tableAlias = self.visit(ctx.tableAlias())
        return ts

    def visitTableName(self, ctx: MySqlBaseParser.TableNameContext):
        log('visitTableName')
        return ctx.getText()

    def visitTableAlias(self, ctx: MySqlBaseParser.TableAliasContext):
        log('visitTableAlias')
        return ctx.getText()

    def visitFullId(self, ctx: MySqlBaseParser.FullIdContext):
        log('visitFullId')
        return ctx.getText()

    def visitFullColumnName(self, ctx: MySqlBaseParser.FullColumnNameContext):
        log('visitFullColumnName')
        fcn = FullColumnName()
        fcn.value = self.visit(ctx.uid())
        if len(ctx.dottedId()) > 0:
            fcn.owner = self.visit(ctx.uid())
            fcn.value = self.visit(ctx.dottedId(len(ctx.dottedId()) - 1))
        return fcn

    def visitDottedId(self, ctx: MySqlBaseParser.DottedIdContext):
        log('visitDottedId')
        return ctx.getText()

    def visitUidList(self, ctx: MySqlBaseParser.UidListContext):
        log('visitUidList')
        uid_list = []
        uids = ctx.uid()
        for i in range(len(uids)):
            uid_list.append(self.visit(uids[i]))
        return uid_list

    def visitUid(self, ctx: MySqlBaseParser.UidContext):
        log('visitUid')
        return ctx.getText()

    def visitUpdatedElement(self, ctx: MySqlBaseParser.UpdatedElementContext):
        log('visitUpdatedElement')
        ue = UpdateElement()
        ue.column = self.visit(ctx.fullColumnName())
        if ctx.DEFAULT() is not None:
            ue.value = Default()
        else:
            ue.value = self.visit(ctx.expression())
        return ue

    def visitWhereClause(self, ctx: MySqlBaseParser.WhereClauseContext):
        log('visitWhereClause')
        wc = WhereClause()
        wc.expression = self.visit(ctx.expression())
        return wc

    def visitExpressions(self, ctx: MySqlBaseParser.ExpressionsContext):
        log('visitExpressions')
        expressions = []
        eps = ctx.expression()
        for i in range(len(eps)):
            expressions.append(self.visit(eps[i]))
        return expressions

    def visitComparisonPredicate(self, ctx: MySqlBaseParser.ComparisonPredicateContext):
        log('visitComparisonPredicate')
        cp = ComparisonPredicate()
        cp.predicate1 = self.visit(ctx.predicate(0))
        cp.comparisonOperator = self.visit(ctx.comparisonOperator())
        cp.predicate2 = self.visit(ctx.predicate(1))
        return cp

    def visitInPredicate(self, ctx: MySqlBaseParser.InPredicateContext):
        log('visitInPredicate')
        ip = InPredicate()
        ip.predicate = self.visit(ctx.predicate())
        ip.NOT = ctx.NOT() is not None
        ip.expressions = self.visit(ctx.expressions())
        return ip

    def visitExpressionAtomPredicate(self, ctx: MySqlBaseParser.ExpressionAtomPredicateContext):
        return self.visit(ctx.predicate())

    def visitBetweenPredicate(self, ctx: MySqlBaseParser.BetweenPredicateContext):
        log('visitBetweenPredicate')
        bp = BetweenPredicate()
        bp.predicate1 = self.visit(ctx.predicate(0))
        bp.NOT = ctx.NOT() is not None
        bp.predicate2 = self.visit(ctx.predicate(1))
        bp.predicate3 = self.visit(ctx.predicate(2))
        return bp

    def visitNotExpression(self, ctx: MySqlBaseParser.NotExpressionContext):
        log('visitNotExpression')
        np = NotExpression()
        np.expression = self.visit(ctx.expression())
        return np

    def visitLogicalExpression(self, ctx: MySqlBaseParser.LogicalExpressionContext):
        log('visitLogicalExpression')
        lp = LogicalExpression()
        lp.expression1 = self.visit(ctx.expression(0))
        lp.logicalOperator = self.visit(ctx.logicalOperator())
        lp.expression2 = self.visit(ctx.expression(1))
        return lp

    def visitLikePredicate(self, ctx: MySqlBaseParser.LikePredicateContext):
        log('visitLikePredicate')
        lp = LikePredicate()
        lp.predicate1 = self.visit(ctx.predicate(0))
        lp.NOT = ctx.NOT() is not None
        lp.predicate2 = self.visit(ctx.predicate(1))
        return lp

    def visitNullPredicate(self, ctx: MySqlBaseParser.NullPredicateContext):
        log('visitNullPredicate')
        np = NullPredicate()
        np.predicate = self.visit(ctx.predicate())
        np.NOT = ctx.NOT() is not None
        return np

    def visitPredicate(self, ctx: MySqlBaseParser.PredicateContext):
        log('visitPredicate')
        if ctx.fullColumnName() is not None:
            return self.visit(ctx.fullColumnName())
        elif ctx.constant() is not None:
            return self.visit(ctx.constant())
        elif ctx.functionCall() is not None:
            return self.visit(ctx.functionCall())

    def visitSpecificFunctionCall(self, ctx: MySqlBaseParser.SpecificFunctionCallContext):
        log('visitSpecificFunctionCall')
        return self.visit(ctx.specificFunction())

    def visitSimpleFunctionCall(self, ctx: MySqlBaseParser.SimpleFunctionCallContext):
        log('visitSpecificFunctionCall')
        fc = FunctionCall()
        fc.function_name = ctx.getText().replace('(', '').replace(')')
        return fc

    def visitScalarFunctionCall(self, ctx: MySqlBaseParser.ScalarFunctionCallContext):
        log('visitScalarFunctionCall')
        fc = FunctionCall()
        fc.function_name = self.visit(ctx.scalarFunctionName())
        if ctx.functionArgs() is not None:
            fc.args_list = self.visit(ctx.functionArgs())
        return fc

    def visitScalarFunctionName(self, ctx: MySqlBaseParser.ScalarFunctionNameContext):
        log('visitScalarFunctionCall')
        return ctx.getText()

    def visitFunctionArgs(self, ctx: MySqlBaseParser.FunctionArgsContext):
        log('visitFunctionArgs')
        fas = ctx.functionArg()
        args_list = []
        for fa in fas:
            args_list.append(self.visit(fa))
        return args_list

    def visitFunctionArg(self, ctx: MySqlBaseParser.FunctionArgContext):
        log('visitFunctionArg')
        if ctx.constant() is not None:
            return self.visit(ctx.constant())
        elif ctx.fullColumnName() is not None:
            return self.visit(ctx.fullColumnName())
        elif ctx.functionCall() is not None:
            return self.visit(ctx.functionCall())

    def visitComparisonOperator(self, ctx: MySqlBaseParser.ComparisonOperatorContext):
        log('visitComparisonOperator')
        return ctx.getText()

    def visitLogicalOperator(self, ctx: MySqlBaseParser.LogicalOperatorContext):
        log('visitLogicalOperator')
        return ctx.getText()

    def visitKeywordsCanBeId(self, ctx: MySqlBaseParser.KeywordsCanBeIdContext):
        log('visitKeywordsCanBeId')
        return ctx.getText()

    def visitConstant(self, ctx: MySqlBaseParser.ConstantContext):
        log('visitConstant')
        if ctx.bitString() is not None:
            return self.visit(ctx.bitString())
        elif ctx.realLiteral() is not None:
            return self.visit(ctx.realLiteral())
        elif ctx.decimalLiteral() is not None:
            return self.visit(ctx.decimalLiteral())
        elif ctx.stringLiteral() is not None:
            return self.visit(ctx.stringLiteral())
        elif ctx.booleanLiteral() is not None:
            return self.visit(ctx.booleanLiteral())
        elif ctx.parameterMarker() is not None:
            return self.visit(ctx.parameterMarker())
        elif ctx.hexadecimalLiteral() is not None:
            return self.visit(ctx.hexadecimalLiteral())
        elif ctx.nullLiteral() is not None:
            return self.visit(ctx.nullLiteral())
        else:
            print('constant unknown')

    def visitBitString(self, ctx: MySqlBaseParser.BitStringContext):
        log('visitBitString')
        return BitString(ctx.getText())

    def visitRealLiteral(self, ctx: MySqlBaseParser.RealLiteralContext):
        log('visitRealLiteral')
        return RealLiteral(ctx.getText())

    def visitBooleanLiteral(self, ctx: MySqlBaseParser.BooleanLiteralContext):
        log('visitBooleanLiteral')
        return BooleanLiteral(ctx.getText())

    def visitStringLiteral(self, ctx: MySqlBaseParser.StringLiteralContext):
        log('visitStringLiteral')
        return StringLiteral(ctx.getText())

    def visitDecimalLiteral(self, ctx: MySqlBaseParser.DecimalLiteralContext):
        log('visitDecimalLiteral')
        return DecimalLiteral(ctx.getText())

    def visitHexadecimalLiteral(self, ctx: MySqlBaseParser.HexadecimalLiteralContext):
        log('visitHexadecimalLiteral')
        return HexadecimalLiteral(ctx.getText())

    def visitNullLiteral(self, ctx: MySqlBaseParser.NullLiteralContext):
        log('visitNullLiteral')
        return NullLiteral()

    def visitOrderByClause(self, ctx: MySqlBaseParser.OrderByClauseContext):
        log('visitOrderByClause')
        obc = OrderByClause()
        order_by_exprs = []
        obes = ctx.orderByExpression()
        for i in range(len(obes)):
            order_by_exprs.append(self.visitOrderByExpression(obes[i]))
        obc.orderByExpressions = order_by_exprs
        return obc

    def visitOrderByExpression(self, ctx: MySqlBaseParser.OrderByExpressionContext):
        log('visitOrderByExpression')
        obe = OrderByExpression()
        obe.expression = self.visit(ctx.expression())
        if ctx.ASC() is None and ctx.DESC() is None:
            obe.ASC = True
        elif ctx.ASC() is not None:
            obe.ASC = True
        elif ctx.DESC() is not None:
            obe.ASC = False
        return obe

    def visitLimitClause(self, ctx: MySqlBaseParser.LimitClauseContext):
        log('visitLimitClause')
        lc = LimitClause()
        if ctx.COMMA() is not None:
            lc.offset = self.visitDecimalLiteral(ctx.decimalLiteral(0))
            lc.limit = self.visitDecimalLiteral(ctx.decimalLiteral(1))
        else:
            lc.limit = self.visitDecimalLiteral(ctx.decimalLiteral(0))
        return lc

    def visitLockClause(self, ctx: MySqlBaseParser.LockClauseContext):
        log('visitLockClause')
        lc = LockClause()
        if ctx.UPDATE() is not None:
            lc.forUpdate = True
        else:
            lc.forUpdate = False
        return lc

    def visitParameterMarker(self, ctx: MySqlBaseParser.ParameterMarkerContext):
        log('visitParameterMarker')
        self.parameter_marker_index += 1
        name = None
        if ctx.PERCENT_NAME_() is not None:
            name = ctx.PERCENT_NAME_().getText()[2:-2]
        pm = ParameterMarker(self.parameter_marker_index, name, ctx.getText())
        return pm


class MysqlOutputVisitor:

    def visitSelectStatement(self, statement, output):
        if not isinstance(statement, SelectStatement):
            raise TypeError('select statement type error. ' + type(statement).__name__)
        if not isinstance(output, list):
            raise TypeError('select statement output type error. ' + type(output).__name__)

        output.append("SELECT")
        if len(statement.selectElements) == 0:
            output.append(" ")
            output.append("*")
        else:
            for selectElement in statement.selectElements:
                self.visitSelectElement(selectElement, output)
        output.append(" ")
        output.append("FROM")
        self.visitTableSource(statement.tableSource, output)

        if statement.where is not None:
            self.visitWhere(statement.where, output)
        if statement.orderBy is not None:
            self.visitOrderBy(statement.orderBy, output)
        if statement.limit is not None:
            self.visitLimit(statement.limit, output)
        if statement.lock is not None:
            self.visitLock(statement.lock, output)

    def visitSelectElement(self, select_element, output):
        if not isinstance(output, list):
            raise TypeError('select_element output type error. ' + type(output).__name__)
        if isinstance(select_element, FullColumnName):
            self.visitFullColumnName(select_element, output)
        else:
            output.append(" ")
            output.append(select_element)

    def visitWhere(self, where, output):
        if not isinstance(where, WhereClause):
            raise TypeError("where type error. " + type(where).__name__)
        if not isinstance(output, list):
            raise TypeError('where output type error. ' + type(output).__name__)
        output.append(" ")
        output.append("WHERE")
        self.visitExpression(where.expression, output)

    def visitOrderBy(self, order_by, output):
        if not isinstance(order_by, OrderByClause):
            raise TypeError("order_by type error. " + type(order_by).__name__)
        if not isinstance(output, list):
            raise TypeError('order_by output type error. ' + type(output).__name__)
        output.append(" ")
        output.append("ORDER")
        output.append(" ")
        output.append("BY")
        for obe_idx, obe in enumerate(order_by.orderByExpressions):
            if obe_idx > 0:
                output.append(",")
            self.visitOrderByExpression(obe, output)

    def visitOrderByExpression(self, order_by_expression, output):
        if not isinstance(order_by_expression, OrderByExpression):
            raise TypeError("order_by_expression type error. " + type(order_by_expression).__name__)
        if not isinstance(output, list):
            raise TypeError('order_by_expression output type error. ' + type(output).__name__)
        self.visitExpression(order_by_expression.expression, output)
        output.append(" ")
        if order_by_expression.ASC:
            output.append("ASC")
        else:
            output.append("DESC")

    def visitLimit(self, limit, output):
        if not isinstance(limit, LimitClause):
            raise TypeError("limit type error. " + type(limit).__name__)
        if not isinstance(output, list):
            raise TypeError('limit output type error. ' + type(output).__name__)
        output.append(" ")
        output.append("LIMIT")
        if limit.offset is not None:
            self.visitConstant(limit.offset, output)
            output.append(",")
        self.visitConstant(limit.limit, output)

    def visitLock(self, lock, output):
        if not isinstance(lock, LockClause):
            raise TypeError("lock type error. " + type(lock).__name__)
        if not isinstance(output, list):
            raise TypeError('lock output type error. ' + type(output).__name__)

        output.append(" ")
        if lock.forUpdate:
            output.append("FOR UPDATE")
        else:
            output.append("LOCK IN SHARE MODE")

    def visitInsertStatement(self, statement, output):
        if not isinstance(statement, InsertStatement):
            raise TypeError('insert statement type error. ' + type(statement).__name__)
        if not isinstance(output, list):
            raise TypeError('insert statement output type error. ' + type(output).__name__)
        output.append('INSERT')
        if statement.ignore:
            output.append(" ")
            output.append('IGNORE')
        output.append(" ")
        output.append('INTO')
        self.visitTableSource(statement.tableSource, output)
        self.visitColumns(statement.columns, output)
        self.visitValueList(statement.value_list, output)

    def visitUpdateStatement(self, statement, output):
        if not isinstance(statement, UpdateStatement):
            raise TypeError('update statement type error. ' + type(statement).__name__)
        if not isinstance(output, list):
            raise TypeError('update statement output type error. ' + type(output).__name__)

        output.append("UPDATE")
        self.visitTableSource(statement.tableSource, output)
        output.append(" ")
        output.append("SET")
        for ele_idx, ele in enumerate(statement.updatedElement):
            if ele_idx > 0:
                output.append(",")
            self.visitUpdatedElement(ele, output)
        if statement.where is not None:
            self.visitWhere(statement.where, output)
        if statement.orderBy is not None:
            self.visitOrderBy(statement.orderBy, output)
        if statement.limit is not None:
            self.visitLimit(statement.limit, output)

    def visitUpdatedElement(self, updated_element, output):
        if not isinstance(updated_element, UpdateElement):
            raise TypeError("updated_element type error. " + type(updated_element).__name__)
        if not isinstance(output, list):
            raise TypeError('updated_element output type error. ' + type(output).__name__)
        self.visitFullColumnName(updated_element.column, output)
        output.append(" ")
        output.append("=")
        if isinstance(updated_element.value, str):
            output.append(" ")
            output.append(updated_element.value)
        else:
            self.visitExpression(updated_element.value, output)

    def visitDeleteStatement(self, statement, output):
        if not isinstance(statement, DeleteStatement):
            raise TypeError('delete statement type error. ' + type(statement).__name__)
        if not isinstance(output, list):
            raise TypeError('delete statement output type error. ' + type(output).__name__)
        output.append("DELETE")
        if statement.tableAlias is not None:
            output.append(" ")
            output.append(statement.tableAlias)
        output.append(" ")
        output.append("FROM")
        self.visitTableSource(statement.tableSource, output)
        if statement.where is not None:
            self.visitWhere(statement.where, output)
        if statement.orderBy is not None:
            self.visitOrderBy(statement.orderBy, output)
        if statement.limit is not None:
            output.append(" ")
            output.append("LIMIT")
            self.visitConstant(statement.limit, output)

    def visitTableSource(self, table_source, output):
        if not isinstance(table_source, TableSource):
            raise TypeError('table_source type error. ' + type(table_source).__name__)
        if not isinstance(output, list):
            raise TypeError('table_source output type error. ' + type(output).__name__)
        output.append(" ")
        output.append(table_source.tableName)
        if table_source.tableAlias is not None:
            output.append(" ")
            output.append(table_source.tableAlias)

    def visitColumns(self, columns, output):
        if not isinstance(output, list):
            raise TypeError('columns output type error. ' + type(output).__name__)
        if columns is not None and len(columns) > 0:
            output.append(" ")
            output.append("(")
            for col_idx, col in enumerate(columns):
                if col_idx > 0:
                    output.append(',')
                output.append(" ")
                output.append(col)
            output.append(")")

    def visitValueList(self, value_list, output):
        if not isinstance(output, list):
            raise TypeError('value_list output type error. ' + type(output).__name__)
        output.append(" ")
        output.append('VALUES')
        for exprs_idx, expressions in enumerate(value_list):
            if exprs_idx > 0:
                output.append(",")
            output.append(" ")
            output.append("(")
            for expr_idx, expression in enumerate(expressions):
                if expr_idx > 0:
                    output.append(",")
                self.visitExpression(expression, output)
            output.append(")")

    def visitExpression(self, expression, output):
        self.visitPredicate(expression, output)

    def visitPredicate(self, predicate, output):
        if isinstance(predicate, InPredicate):
            self.visitPredicate(predicate.predicate, output)
            if predicate.NOT:
                output.append(" ")
                output.append('NOT')
            output.append(" ")
            output.append("IN")
            output.append(" ")
            output.append('(')
            self.visitExpressions(predicate.expressions, output)
            output.append(" ")
            output.append(")")
        elif isinstance(predicate, ComparisonPredicate):
            self.visitPredicate(predicate.predicate1, output)
            output.append(" ")
            output.append(predicate.comparisonOperator)
            self.visitPredicate(predicate.predicate2, output)
        elif isinstance(predicate, NullPredicate):
            self.visitPredicate(predicate.predicate, output)
            output.append(" ")
            output.append("IS")
            if predicate.NOT:
                output.append(" ")
                output.append("NOT")
            output.append(" ")
            output.append("NULL")
        elif isinstance(predicate, BetweenPredicate):
            self.visitPredicate(predicate.predicate1, output)
            if predicate.NOT:
                output.append(" ")
                output.append("NOT")
            output.append(" ")
            output.append("BETWEEN")
            self.visitPredicate(predicate.predicate2, output)
            output.append(" ")
            output.append("AND")
            self.visitPredicate(predicate.predicate3, output)
        elif isinstance(predicate, LikePredicate):
            self.visitPredicate(predicate.predicate1, output)
            if predicate.NOT:
                output.append(" ")
                output.append("NOT")
            output.append(" ")
            output.append("LIKE")
            self.visitPredicate(predicate.predicate2, output)
        elif isinstance(predicate, NotExpression):
            output.append(" ")
            output.append("NOT")
            self.visitExpression(predicate.expression, output)
        elif isinstance(predicate, LogicalExpression):
            self.visitExpression(predicate.expression1, output)
            output.append(" ")
            output.append(predicate.logicalOperator.upper())
            self.visitExpression(predicate.expression2, output)
        elif isinstance(predicate, PredicateAtom):
            if isinstance(predicate, FullColumnName):
                self.visitFullColumnName(predicate, output)
            elif isinstance(predicate, Constant):
                self.visitConstant(predicate, output)
            elif isinstance(predicate, FunctionCall):
                self.visitFunctionCall(predicate, output)
            else:
                print('predicate atom unknown')
        else:
            print('predicate unknown')

    def visitExpressions(self, expressions, output):
        for expr_idx, expression in enumerate(expressions):
            if expr_idx > 0:
                output.append(",")
            self.visitExpression(expression, output)

    def visitFullColumnName(self, predicate, output):
        output.append(" ")
        if predicate.owner is not None:
            output.append(predicate.owner + predicate.value)
        else:
            output.append(predicate.value)

    def visitConstant(self, val, output):
        output.append(" ")
        if isinstance(val, BitString):
            output.append(str(val.value))
        elif isinstance(val, RealLiteral):
            output.append(str(val.value))
        elif isinstance(val, DecimalLiteral):
            output.append(str(val.value))
        elif isinstance(val, BooleanLiteral):
            output.append(str(val.value).upper())
        elif isinstance(val, ParameterMarker):
            self.visitParameterMarker(val, output)
        elif isinstance(val, StringLiteral):
            output.append('\'' + val.value + '\'')
        elif isinstance(val, HexadecimalLiteral):
            output.append(str(val.value))
        elif isinstance(val, NullLiteral):
            output.append('NULL')
        else:
            print('constant unknown, ' + type(val).__name__)

    def visitParameterMarker(self, parameter_marker, output):
        output.append(parameter_marker.value)

    def visitFunctionCall(self, function_call, output):
        if not isinstance(function_call, FunctionCall):
            raise TypeError('function_call type error. ' + type(function_call).__name__)
        if not isinstance(output, list):
            raise TypeError('function_call output type error. ' + type(output).__name__)
        output.append(" ")
        output.append(function_call.function_name)
        output.append("(")
        if function_call.args_list is not None:
            for arg_idx, arg in enumerate(function_call.args_list):
                if arg_idx > 0:
                    output.append(",")
                if isinstance(arg, Constant):
                    self.visitConstant(arg, output)
                elif isinstance(arg, FullColumnName):
                    self.visitConstant(arg, output)
                elif isinstance(arg, FunctionCall):
                    self.visitFunctionCall(arg, output)
        output.append(")")
