#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
"""
from seata.sqlparser.mysql.antlr4.MySQLStatementParser import MySQLStatementParser
from seata.sqlparser.mysql.antlr4.MySQLStatementVisitor import MySQLStatementVisitor
from seata.sqlparser.mysql.antlr4.value.table import SimpleTableSegment, TableNameSegment, OwnerSegment, ColumnSegment, \
    IndexSegment, Interval, BinaryOperationExpression, LiteralExpressionSegment, SubqueryExpressionSegment, \
    SubquerySegment, ListExpression, InExpression, BetweenExpression, ExistsSubqueryExpression, \
    ParameterMarkerExpressionSegment, CommonExpressionSegment, NotExpression, LockSegment
from seata.sqlparser.mysql.antlr4.value.value import ParameterMarkerValue, StringLiteralValue, NumberLiteralValue, \
    OtherLiteralValue, BooleanLiteralValue, IdentifierValue, MySQLIdentifierValue


class MySQLStatementSQLVisitor(MySQLStatementVisitor):

    def __init__(self):
        self.currentParameterIndex = 0

    def visitParameterMarker(self, ctx: MySQLStatementParser.ParameterMarkerContext):
        self.currentParameterIndex += 1
        return ParameterMarkerValue(self.currentParameterIndex)

    def visitLiterals(self, ctx: MySQLStatementParser.LiteralsContext):
        if ctx.stringLiterals() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.stringLiterals())
        if ctx.numberLiterals() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.numberLiterals())
        if ctx.temporalLiterals() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.temporalLiterals())
        if ctx.hexadecimalLiterals() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.hexadecimalLiterals())
        if ctx.bitValueLiterals() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.bitValueLiterals())
        if ctx.booleanLiterals() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.booleanLiterals())
        if ctx.nullValueLiterals() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.nullValueLiterals())
        raise ValueError("Literals must have string, number, dateTime, hex, bit, boolean or null.")

    def visitStringLiterals(self, ctx: MySQLStatementParser.StringLiteralsContext):
        return StringLiteralValue(ctx.getText())

    def visitNumberLiterals(self, ctx: MySQLStatementParser.NumberLiteralsContext):
        return NumberLiteralValue(ctx.getText())

    def visitTemporalLiterals(self, ctx: MySQLStatementParser.TemporalLiteralsContext):
        return OtherLiteralValue(ctx.getText())

    def visitHexadecimalLiterals(self, ctx: MySQLStatementParser.HexadecimalLiteralsContext):
        return OtherLiteralValue(ctx.getText())

    def visitBitValueLiterals(self, ctx: MySQLStatementParser.BitValueLiteralsContext):
        return OtherLiteralValue(ctx.getText())

    def visitBooleanLiterals(self, ctx: MySQLStatementParser.BooleanLiteralsContext):
        return BooleanLiteralValue(ctx.getText())

    def visitNullValueLiterals(self, ctx: MySQLStatementParser.NullValueLiteralsContext):
        return OtherLiteralValue(ctx.getText())

    def visitIdentifier(self, ctx: MySQLStatementParser.IdentifierContext):
        return MySQLIdentifierValue(ctx.getText())

    def visitSchemaName(self, ctx: MySQLStatementParser.SchemaNameContext):
        return super(MySQLStatementSQLVisitor, self).visit(ctx.identifier())

    def visitTableName(self, ctx: MySQLStatementParser.TableNameContext):
        result = SimpleTableSegment(TableNameSegment(ctx.name().getStart().getStartIndex(),
                                                     ctx.name().getStop().getStopIndex(),
                                                     IdentifierValue(ctx.name().identifier().getText())))
        owner = ctx.owner()
        if owner is not None:
            result.owner = OwnerSegment(owner.getStart().getStartIndex(),
                                        owner.getStop().getStopIndex(),
                                        super(MySQLStatementSQLVisitor, self).visit(owner.identifier()))
        return result

    def visitViewName(self, ctx: MySQLStatementParser.ViewNameContext):
        result = SimpleTableSegment(TableNameSegment(ctx.name().getStart().getStartIndex(),
                                                     ctx.name().getStop().getStopIndex(),
                                                     IdentifierValue(ctx.name().identifier().getText())))
        owner = ctx.owner()
        if owner is not None:
            result.owner = OwnerSegment(owner.getStart().getStartIndex(),
                                        owner.getStop().getStopIndex(),
                                        super(MySQLStatementSQLVisitor, self).visit(owner.identifier()))
        return result

    def visitColumnName(self, ctx: MySQLStatementParser.ColumnNameContext):
        return ColumnSegment(ctx.getStart().getStartIndex(),
                             ctx.getStop().getStopIndex(),
                             super(MySQLStatementSQLVisitor, self).visit(ctx.identifier()))

    def visitIndexName(self, ctx: MySQLStatementParser.IndexNameContext):
        return IndexSegment(ctx.getStart().getStartIndex(),
                            ctx.getStop().getStopIndex(),
                            super(MySQLStatementSQLVisitor, self).visit(ctx.identifier()))

    def visitTableList(self, ctx: MySQLStatementParser.TableListContext):
        result = []
        tns = ctx.tableName()
        for i in range(len(tns)):
            tnc = tns[i]
            result.append(self.visitTableName(tnc))

        return result

    def visitExpr(self, ctx: MySQLStatementParser.ExprContext):
        if ctx.booleanPrimary() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.booleanPrimary())

        if ctx.XOR() is not None:
            left = super(MySQLStatementSQLVisitor, self).visit(ctx.expr(0))
            right = super(MySQLStatementSQLVisitor, self).visit(ctx.expr(1))
            operator = "XOR"
            text = ctx.start.getInputStream().getText(Interval(ctx.start.getStartIndex(), ctx.stop.getStopIndex()))
            return BinaryOperationExpression(ctx.start.getStartIndex(),
                                             ctx.stop.getStopIndex(),
                                             left, right, operator, text)

    def visitBooleanPrimary(self, ctx: MySQLStatementParser.BooleanPrimaryContext):
        if ctx.IS() is not None:
            left = super(MySQLStatementSQLVisitor, self).visit(ctx.booleanPrimary())
            right = LiteralExpressionSegment(ctx.IS().getSymbol().getStopIndex() + 1,
                                             ctx.stop.getStopIndex(),
                                             Interval(ctx.IS().getSymbol().getStopIndex() + 1, ctx.stop.getStopIndex()))
            operator = "IS"
            text = ctx.start.getInputStream().getText(Interval(ctx.start.getStartIndex(), ctx.stop.getStopIndex()))
            return BinaryOperationExpression(ctx.start.getStartIndex(),
                                             ctx.stop.getStopIndex(),
                                             left, right, operator, text)
        if ctx.comparisonOperator() is not None or ctx.SAFE_EQ_() is not None:
            return self.__create_compare_segment(ctx)

        if ctx.assignmentOperator() is not None:
            return self.__create_assignment_segment(ctx)

        return super(MySQLStatementSQLVisitor, self).visit(ctx.predicate())

    def __create_compare_segment(self, ctx: MySQLStatementParser.BooleanPrimaryContext):
        left = super(MySQLStatementSQLVisitor, self).visit(ctx.booleanPrimary())
        if ctx.predicate() is not None:
            right = super(MySQLStatementSQLVisitor, self).visit(ctx.predicate())
        else:
            right = SubqueryExpressionSegment(SubquerySegment(ctx.subquery().start.getStartIndex(),
                                                              ctx.subquery().stop.getStopIndex(),
                                                              super(MySQLStatementSQLVisitor, self).visit(
                                                                  ctx.subquery())))
        if ctx.SAFE_EQ_() is not None:
            operator = ctx.SAFE_EQ_().getText()
        else:
            operator = ctx.comparisonOperator().getText()
        text = ctx.start.getInputStream().getText(Interval(ctx.start.getStartIndex(), ctx.stop.getStopIndex()))
        return BinaryOperationExpression(ctx.start.getStartIndex(), ctx.stop.getStopIndex(), left, right, operator,
                                         text)

    def __create_assignment_segment(self, ctx: MySQLStatementParser.BooleanPrimaryContext):
        left = super(MySQLStatementSQLVisitor, self).visit(ctx.booleanPrimary())
        right = super(MySQLStatementSQLVisitor, self).visit(ctx.predicate())
        operator = ctx.assignmentOperator().getText()
        text = ctx.start.getInputStream().getText(Interval(ctx.start.getStartIndex(), ctx.stop.getStopIndex()))
        return BinaryOperationExpression(ctx.start.getStartIndex(), ctx.stop.getStopIndex(), left, right, operator,
                                         text)

    def visitPredicate(self, ctx: MySQLStatementParser.PredicateContext):
        if ctx.IN() is not None:
            return self.__create_in_segment(ctx)
        if ctx.BETWEEN() is not None:
            return self.__create_between_segment(ctx)
        if ctx.LIKE() is not None:
            return self.__create_binary_operation_expression_from_like(ctx)
        if ctx.REGEXP() is not None:
            return self.__create_binary_operation_expression_from_regexp(ctx)
        return super(MySQLStatementSQLVisitor, self).visit(ctx.bitExpr(0))

    def __create_in_segment(self, ctx: MySQLStatementParser.PredicateContext):
        b = ctx.NOT() is not None
        left = super(MySQLStatementSQLVisitor, self).visit(ctx.bitExpr(0))
        if ctx.subquery() is not None:
            right = SubqueryExpressionSegment(SubquerySegment(ctx.subquery().start.getStartIndex(),
                                                              ctx.subquery().stop.getStopIndex(),
                                                              super(MySQLStatementSQLVisitor, self).visit(
                                                                  ctx.subquery())))
        else:
            right = ListExpression(ctx.LP_().getSymbol().getStartIndex(), ctx.RP_().getSymbol().getStopIndex())
            eps = ctx.expr()
            for i in range(len(eps)):
                right.getItems().add(super(MySQLStatementSQLVisitor, self).visit(eps[i]))
        return InExpression(ctx.start.getStartIndex(), ctx.stop.getStopIndex(), left, right, b)

    def __create_between_segment(self, ctx: MySQLStatementParser.PredicateContext):
        left = super(MySQLStatementSQLVisitor, self).visit(ctx.bitExpr(0))
        between = super(MySQLStatementSQLVisitor, self).visit(ctx.bitExpr(1))
        and_ = super(MySQLStatementSQLVisitor, self).visit(ctx.predicate())
        not_ = ctx.NOT() is not None
        return BetweenExpression(ctx.start.getStartIndex(), ctx.stop.getStopIndex(), left, between, and_, not_)

    def __create_binary_operation_expression_from_like(self, ctx: MySQLStatementParser.PredicateContext):

        left = super(MySQLStatementSQLVisitor, self).visit(ctx.bitExpr(0))
        if ctx.SOUNDS() is not None:
            right = super(MySQLStatementSQLVisitor, self).visit(ctx.bitExpr(1))
            operator = "SOUNDS LIKE"
        else:
            list_expression = ListExpression(ctx.simpleExpr(0).start.getStartIndex(),
                                             ctx.simpleExpr().get(ctx.simpleExpr().size() - 1).stop.getStopIndex())
            ses = ctx.simpleExpr()
            for i in range(len(ses)):
                list_expression.getItems().add(super(MySQLStatementSQLVisitor, self).visit(ses[i]))
            right = list_expression
            if ctx.NOT() is not None:
                operator = "NOT LIKE"
            else:
                operator = "LIKE"
        text = ctx.start.getInputStream().getText(Interval(ctx.start.getStartIndex(), ctx.stop.getStopIndex()))
        return BinaryOperationExpression(ctx.start.getStartIndex(), ctx.stop.getStopIndex(), left, right, operator,
                                         text)

    def __create_binary_operation_expression_from_regexp(self, ctx: MySQLStatementParser.PredicateContext):
        left = super(MySQLStatementSQLVisitor, self).visit(ctx.bitExpr(0))
        right = super(MySQLStatementSQLVisitor, self).visit(ctx.bitExpr(1))
        if ctx.NOT() is not None:
            operator = "NOT REGEXP"
        else:
            operator = "REGEXP"
        text = ctx.start.getInputStream().getText(Interval(ctx.start.getStartIndex(), ctx.stop.getStopIndex()))
        return BinaryOperationExpression(ctx.start.getStartIndex(), ctx.stop.getStopIndex(), left, right, operator,
                                         text)

    def visitBitExpr(self, ctx: MySQLStatementParser.BitExprContext):
        if ctx.simpleExpr() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.simpleExpr())
        left = super(MySQLStatementSQLVisitor, self).visit(ctx.getChild(0))
        right = super(MySQLStatementSQLVisitor, self).visit(ctx.getChild(2))
        operator = ctx.getChild(1).getText()
        text = ctx.start.getInputStream().getText(Interval(ctx.start.getStartIndex(), ctx.stop.getStopIndex()))
        return BinaryOperationExpression(ctx.start.getStartIndex(), ctx.stop.getStopIndex(), left, right, operator,
                                         text)

    def visitSimpleExpr(self, ctx: MySQLStatementParser.SimpleExprContext):
        start_index = ctx.start.getStartIndex()
        stop_index = ctx.stop.getStopIndex()
        if ctx.subquery() is not None:
            subquery_segment = SubquerySegment(ctx.subquery().getStart().getStartIndex(),
                                               ctx.subquery().getStop().getStopIndex(),
                                               super(MySQLStatementSQLVisitor, self).visit(ctx.subquery()))
            if ctx.EXISTS() is not None:
                return ExistsSubqueryExpression(start_index, stop_index, subquery_segment)
            return SubqueryExpressionSegment(subquery_segment)
        if ctx.parameterMarker() is not None:
            return ParameterMarkerExpressionSegment(start_index, stop_index,
                                                    super(MySQLStatementSQLVisitor, self).visit(
                                                        ctx.parameterMarker().value))

        if ctx.literals() is not None:
            return self.__create_literal_express(
                super(MySQLStatementSQLVisitor, self).visit(ctx.literals()),
                start_index, stop_index,
                ctx.literals().start.getInputStream().getText(Interval(start_index, stop_index))
            )

        if ctx.intervalExpression() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.intervalExpression())

        if ctx.functionCall() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.functionCall())

        if ctx.columnRef() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.columnRef())

        if ctx.matchExpression() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.matchExpression())

        if ctx.notOperator() is not None:
            expression = super(MySQLStatementSQLVisitor, self).visit(ctx.simpleExpr())
            if isinstance(expression, ExistsSubqueryExpression):
                expression.not_ = True
                return expression
            return NotExpression(start_index, stop_index, expression)

        if ctx.LP_() is not None and ctx.expr().size() == 1:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.expr(0))
        return self.__visit_remain_simple_expr(ctx)

    def __create_literal_express(self, ast, start_index, stop_index, text):
        if isinstance(ast, StringLiteralValue):
            return LiteralExpressionSegment(start_index, stop_index, ast.value)
        if isinstance(ast, NumberLiteralValue):
            return LiteralExpressionSegment(start_index, stop_index, ast.value)
        if isinstance(ast, BooleanLiteralValue):
            return LiteralExpressionSegment(start_index, stop_index, ast.value)
        if isinstance(ast, OtherLiteralValue):
            return LiteralExpressionSegment(start_index, stop_index, ast.value)
        return CommonExpressionSegment(start_index, stop_index, text)

    def __visit_remain_simple_expr(self, ctx: MySQLStatementParser.SimpleExprContext):
        if ctx.caseExpression() is not None:
            super(MySQLStatementSQLVisitor, self).visit(ctx.caseExpression())
            text = ctx.start.getInputStream().getText(Interval(ctx.start.getStartIndex(), ctx.stop.getStopIndex()))
            return CommonExpressionSegment(ctx.getStart().getStartIndex(), ctx.getStop().getStopIndex(), text)

        es = ctx.expr()
        for i in range(len(es)):
            super(MySQLStatementSQLVisitor, self).visit(es[i])
        ses = ctx.simpleExpr()
        for i in range(len(ses)):
            super(MySQLStatementSQLVisitor, self).visit(ses[i])
        text = ctx.start.getInputStream().getText(Interval(ctx.start.getStartIndex(), ctx.stop.getStopIndex()))
        return CommonExpressionSegment(ctx.getStart().getStartIndex(), ctx.getStop().getStopIndex(), text)

    def visitColumnRef(self, ctx: MySQLStatementParser.ColumnRefContext):
        identifier_count = ctx.identifier().size()
        if 1 == identifier_count:
            result = ColumnSegment(ctx.getStart().getStartIndex(), ctx.getStop().getStopIndex(),
                                   super(MySQLStatementSQLVisitor, self).visit(ctx.identifier(0)))
        elif 2 == identifier_count:
            result = ColumnSegment(ctx.getStart().getStartIndex(), ctx.getStop().getStopIndex(),
                                   super(MySQLStatementSQLVisitor, self).visit(ctx.identifier(1)))
            result.setOwner(OwnerSegment(ctx.identifier(0).start.getStartIndex(), ctx.identifier(0).stop.getStopIndex(),
                                         super(MySQLStatementSQLVisitor, self).visit(ctx.identifier(0))))
        else:
            result = ColumnSegment(ctx.getStart().getStartIndex(), ctx.getStop().getStopIndex(),
                                   super(MySQLStatementSQLVisitor, self).visit(ctx.identifier(2)))
            result.setOwner(OwnerSegment(ctx.identifier(1).start.getStartIndex(), ctx.identifier(1).stop.getStopIndex(),
                                         super(MySQLStatementSQLVisitor, self).visit(ctx.identifier(1))))
        return result

    def visitSubquery(self, ctx: MySQLStatementParser.SubqueryContext):
        return super(MySQLStatementSQLVisitor, self).visit(ctx.queryExpressionParens())

    def visitQueryExpressionParens(self, ctx: MySQLStatementParser.QueryExpressionParensContext):
        if ctx.queryExpressionParens() is not None:
            return super(MySQLStatementSQLVisitor, self).visit(ctx.queryExpressionParens())
        result = super(MySQLStatementSQLVisitor, self).visit(ctx.queryExpression())
        if ctx.lockClauseList() is not None:
            result.lock = super(MySQLStatementSQLVisitor, self).visit(ctx.lockClauseList())
        result.parameter_count = self.current_parameter_index
        return result

    def visitLockClauseList(self, ctx:MySQLStatementParser.LockClauseListContext):
        result = LockSegment(ctx.getStart().getStartIndex(), ctx.getStop().getStopIndex())
        lcs = ctx.lockClause()
        for i in range(len(lcs)):
            if lcs[i].tableLockList() is not None:
                result.table.append(
                    self.__generate_tables_from_table_alias_ref_list(lcs[i].tableLockingList().tableAliasRefList()))
        return result

    def visitQueryExpression(self, ctx:MySQLStatementParser.QueryExpressionContext):
        if ctx.queryExpressionBody() is not None:
            result = super(MySQLStatementSQLVisitor, self).visit(ctx.queryExpressionBody())
        else:
            result = super(MySQLStatementSQLVisitor, self).visit(ctx.queryExpressionParens())

        if ctx.orderByClause() is not None:
            result.order_by = super(MySQLStatementSQLVisitor, self).visit(ctx.orderByClause())

        if ctx.limitClause() is not None:
            result.limit = super(MySQLStatementSQLVisitor, self).visit(ctx.limitClause())

        return result

    def visitSelectWithInto(self, ctx:MySQLStatementParser.SelectWithIntoContext):
        # TODO
        pass

    def __generate_tables_from_table_alias_ref_list(self, ctx: MySQLStatementParser.TableAliasRefListContext):
        result = []
        tiows = ctx.tableIdentOptWild()
        for i in range(len(tiows)):
            result.append(super(MySQLStatementSQLVisitor, self).visit(tiows[i].tableName()))
        return result
"""