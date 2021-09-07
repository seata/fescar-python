# Generated from MySqlBaseParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MySqlBaseParser import MySqlBaseParser
else:
    from MySqlBaseParser import MySqlBaseParser

# This class defines a complete generic visitor for a parse tree produced by MySqlBaseParser.

class MySqlBaseParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MySqlBaseParser#root.
    def visitRoot(self, ctx:MySqlBaseParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#sqlStatements.
    def visitSqlStatements(self, ctx:MySqlBaseParser.SqlStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#sqlStatement.
    def visitSqlStatement(self, ctx:MySqlBaseParser.SqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#emptyStatement.
    def visitEmptyStatement(self, ctx:MySqlBaseParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#dmlStatement.
    def visitDmlStatement(self, ctx:MySqlBaseParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#selectStatement.
    def visitSelectStatement(self, ctx:MySqlBaseParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#insertStatement.
    def visitInsertStatement(self, ctx:MySqlBaseParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#updateStatement.
    def visitUpdateStatement(self, ctx:MySqlBaseParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#deleteStatement.
    def visitDeleteStatement(self, ctx:MySqlBaseParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#insertStatementValue.
    def visitInsertStatementValue(self, ctx:MySqlBaseParser.InsertStatementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#selectElements.
    def visitSelectElements(self, ctx:MySqlBaseParser.SelectElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#selectStarElement.
    def visitSelectStarElement(self, ctx:MySqlBaseParser.SelectStarElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#selectColumnElement.
    def visitSelectColumnElement(self, ctx:MySqlBaseParser.SelectColumnElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#tableSource.
    def visitTableSource(self, ctx:MySqlBaseParser.TableSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#tableName.
    def visitTableName(self, ctx:MySqlBaseParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#tableAlias.
    def visitTableAlias(self, ctx:MySqlBaseParser.TableAliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#fullId.
    def visitFullId(self, ctx:MySqlBaseParser.FullIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#fullColumnName.
    def visitFullColumnName(self, ctx:MySqlBaseParser.FullColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#dottedId.
    def visitDottedId(self, ctx:MySqlBaseParser.DottedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#uidList.
    def visitUidList(self, ctx:MySqlBaseParser.UidListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#uid.
    def visitUid(self, ctx:MySqlBaseParser.UidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#updatedElement.
    def visitUpdatedElement(self, ctx:MySqlBaseParser.UpdatedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#whereClause.
    def visitWhereClause(self, ctx:MySqlBaseParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#expressions.
    def visitExpressions(self, ctx:MySqlBaseParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#comparisonPredicate.
    def visitComparisonPredicate(self, ctx:MySqlBaseParser.ComparisonPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#expressionAtomPredicate.
    def visitExpressionAtomPredicate(self, ctx:MySqlBaseParser.ExpressionAtomPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#inPredicate.
    def visitInPredicate(self, ctx:MySqlBaseParser.InPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#betweenPredicate.
    def visitBetweenPredicate(self, ctx:MySqlBaseParser.BetweenPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#notExpression.
    def visitNotExpression(self, ctx:MySqlBaseParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#likePredicate.
    def visitLikePredicate(self, ctx:MySqlBaseParser.LikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#nullPredicate.
    def visitNullPredicate(self, ctx:MySqlBaseParser.NullPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#logicalExpression.
    def visitLogicalExpression(self, ctx:MySqlBaseParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#predicate.
    def visitPredicate(self, ctx:MySqlBaseParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#specificFunctionCall.
    def visitSpecificFunctionCall(self, ctx:MySqlBaseParser.SpecificFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#scalarFunctionCall.
    def visitScalarFunctionCall(self, ctx:MySqlBaseParser.ScalarFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#scalarFunctionName.
    def visitScalarFunctionName(self, ctx:MySqlBaseParser.ScalarFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#simpleFunctionCall.
    def visitSimpleFunctionCall(self, ctx:MySqlBaseParser.SimpleFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#functionArgs.
    def visitFunctionArgs(self, ctx:MySqlBaseParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#functionArg.
    def visitFunctionArg(self, ctx:MySqlBaseParser.FunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#functionNameBase.
    def visitFunctionNameBase(self, ctx:MySqlBaseParser.FunctionNameBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:MySqlBaseParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#logicalOperator.
    def visitLogicalOperator(self, ctx:MySqlBaseParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#keywordsCanBeId.
    def visitKeywordsCanBeId(self, ctx:MySqlBaseParser.KeywordsCanBeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#constant.
    def visitConstant(self, ctx:MySqlBaseParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#nullLiteral.
    def visitNullLiteral(self, ctx:MySqlBaseParser.NullLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#realLiteral.
    def visitRealLiteral(self, ctx:MySqlBaseParser.RealLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#bitString.
    def visitBitString(self, ctx:MySqlBaseParser.BitStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:MySqlBaseParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#stringLiteral.
    def visitStringLiteral(self, ctx:MySqlBaseParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:MySqlBaseParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#hexadecimalLiteral.
    def visitHexadecimalLiteral(self, ctx:MySqlBaseParser.HexadecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#orderByClause.
    def visitOrderByClause(self, ctx:MySqlBaseParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#orderByExpression.
    def visitOrderByExpression(self, ctx:MySqlBaseParser.OrderByExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#limitClause.
    def visitLimitClause(self, ctx:MySqlBaseParser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#lockClause.
    def visitLockClause(self, ctx:MySqlBaseParser.LockClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlBaseParser#parameterMarker.
    def visitParameterMarker(self, ctx:MySqlBaseParser.ParameterMarkerContext):
        return self.visitChildren(ctx)



del MySqlBaseParser