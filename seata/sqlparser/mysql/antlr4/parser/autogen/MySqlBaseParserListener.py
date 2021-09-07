# Generated from MySqlBaseParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MySqlBaseParser import MySqlBaseParser
else:
    from MySqlBaseParser import MySqlBaseParser

# This class defines a complete listener for a parse tree produced by MySqlBaseParser.
class MySqlBaseParserListener(ParseTreeListener):

    # Enter a parse tree produced by MySqlBaseParser#root.
    def enterRoot(self, ctx:MySqlBaseParser.RootContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#root.
    def exitRoot(self, ctx:MySqlBaseParser.RootContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#sqlStatements.
    def enterSqlStatements(self, ctx:MySqlBaseParser.SqlStatementsContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#sqlStatements.
    def exitSqlStatements(self, ctx:MySqlBaseParser.SqlStatementsContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#sqlStatement.
    def enterSqlStatement(self, ctx:MySqlBaseParser.SqlStatementContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#sqlStatement.
    def exitSqlStatement(self, ctx:MySqlBaseParser.SqlStatementContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#emptyStatement.
    def enterEmptyStatement(self, ctx:MySqlBaseParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#emptyStatement.
    def exitEmptyStatement(self, ctx:MySqlBaseParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#dmlStatement.
    def enterDmlStatement(self, ctx:MySqlBaseParser.DmlStatementContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#dmlStatement.
    def exitDmlStatement(self, ctx:MySqlBaseParser.DmlStatementContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#selectStatement.
    def enterSelectStatement(self, ctx:MySqlBaseParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#selectStatement.
    def exitSelectStatement(self, ctx:MySqlBaseParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#insertStatement.
    def enterInsertStatement(self, ctx:MySqlBaseParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#insertStatement.
    def exitInsertStatement(self, ctx:MySqlBaseParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#updateStatement.
    def enterUpdateStatement(self, ctx:MySqlBaseParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#updateStatement.
    def exitUpdateStatement(self, ctx:MySqlBaseParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#deleteStatement.
    def enterDeleteStatement(self, ctx:MySqlBaseParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#deleteStatement.
    def exitDeleteStatement(self, ctx:MySqlBaseParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#insertStatementValue.
    def enterInsertStatementValue(self, ctx:MySqlBaseParser.InsertStatementValueContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#insertStatementValue.
    def exitInsertStatementValue(self, ctx:MySqlBaseParser.InsertStatementValueContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#selectElements.
    def enterSelectElements(self, ctx:MySqlBaseParser.SelectElementsContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#selectElements.
    def exitSelectElements(self, ctx:MySqlBaseParser.SelectElementsContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#selectStarElement.
    def enterSelectStarElement(self, ctx:MySqlBaseParser.SelectStarElementContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#selectStarElement.
    def exitSelectStarElement(self, ctx:MySqlBaseParser.SelectStarElementContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#selectColumnElement.
    def enterSelectColumnElement(self, ctx:MySqlBaseParser.SelectColumnElementContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#selectColumnElement.
    def exitSelectColumnElement(self, ctx:MySqlBaseParser.SelectColumnElementContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#tableSource.
    def enterTableSource(self, ctx:MySqlBaseParser.TableSourceContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#tableSource.
    def exitTableSource(self, ctx:MySqlBaseParser.TableSourceContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#tableName.
    def enterTableName(self, ctx:MySqlBaseParser.TableNameContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#tableName.
    def exitTableName(self, ctx:MySqlBaseParser.TableNameContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#tableAlias.
    def enterTableAlias(self, ctx:MySqlBaseParser.TableAliasContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#tableAlias.
    def exitTableAlias(self, ctx:MySqlBaseParser.TableAliasContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#fullId.
    def enterFullId(self, ctx:MySqlBaseParser.FullIdContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#fullId.
    def exitFullId(self, ctx:MySqlBaseParser.FullIdContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#fullColumnName.
    def enterFullColumnName(self, ctx:MySqlBaseParser.FullColumnNameContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#fullColumnName.
    def exitFullColumnName(self, ctx:MySqlBaseParser.FullColumnNameContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#dottedId.
    def enterDottedId(self, ctx:MySqlBaseParser.DottedIdContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#dottedId.
    def exitDottedId(self, ctx:MySqlBaseParser.DottedIdContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#uidList.
    def enterUidList(self, ctx:MySqlBaseParser.UidListContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#uidList.
    def exitUidList(self, ctx:MySqlBaseParser.UidListContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#uid.
    def enterUid(self, ctx:MySqlBaseParser.UidContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#uid.
    def exitUid(self, ctx:MySqlBaseParser.UidContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#updatedElement.
    def enterUpdatedElement(self, ctx:MySqlBaseParser.UpdatedElementContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#updatedElement.
    def exitUpdatedElement(self, ctx:MySqlBaseParser.UpdatedElementContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#whereClause.
    def enterWhereClause(self, ctx:MySqlBaseParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#whereClause.
    def exitWhereClause(self, ctx:MySqlBaseParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#expressions.
    def enterExpressions(self, ctx:MySqlBaseParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#expressions.
    def exitExpressions(self, ctx:MySqlBaseParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#comparisonPredicate.
    def enterComparisonPredicate(self, ctx:MySqlBaseParser.ComparisonPredicateContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#comparisonPredicate.
    def exitComparisonPredicate(self, ctx:MySqlBaseParser.ComparisonPredicateContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#expressionAtomPredicate.
    def enterExpressionAtomPredicate(self, ctx:MySqlBaseParser.ExpressionAtomPredicateContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#expressionAtomPredicate.
    def exitExpressionAtomPredicate(self, ctx:MySqlBaseParser.ExpressionAtomPredicateContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#inPredicate.
    def enterInPredicate(self, ctx:MySqlBaseParser.InPredicateContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#inPredicate.
    def exitInPredicate(self, ctx:MySqlBaseParser.InPredicateContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#betweenPredicate.
    def enterBetweenPredicate(self, ctx:MySqlBaseParser.BetweenPredicateContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#betweenPredicate.
    def exitBetweenPredicate(self, ctx:MySqlBaseParser.BetweenPredicateContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#notExpression.
    def enterNotExpression(self, ctx:MySqlBaseParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#notExpression.
    def exitNotExpression(self, ctx:MySqlBaseParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#likePredicate.
    def enterLikePredicate(self, ctx:MySqlBaseParser.LikePredicateContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#likePredicate.
    def exitLikePredicate(self, ctx:MySqlBaseParser.LikePredicateContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#nullPredicate.
    def enterNullPredicate(self, ctx:MySqlBaseParser.NullPredicateContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#nullPredicate.
    def exitNullPredicate(self, ctx:MySqlBaseParser.NullPredicateContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#logicalExpression.
    def enterLogicalExpression(self, ctx:MySqlBaseParser.LogicalExpressionContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#logicalExpression.
    def exitLogicalExpression(self, ctx:MySqlBaseParser.LogicalExpressionContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#predicate.
    def enterPredicate(self, ctx:MySqlBaseParser.PredicateContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#predicate.
    def exitPredicate(self, ctx:MySqlBaseParser.PredicateContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#specificFunctionCall.
    def enterSpecificFunctionCall(self, ctx:MySqlBaseParser.SpecificFunctionCallContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#specificFunctionCall.
    def exitSpecificFunctionCall(self, ctx:MySqlBaseParser.SpecificFunctionCallContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#scalarFunctionCall.
    def enterScalarFunctionCall(self, ctx:MySqlBaseParser.ScalarFunctionCallContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#scalarFunctionCall.
    def exitScalarFunctionCall(self, ctx:MySqlBaseParser.ScalarFunctionCallContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#scalarFunctionName.
    def enterScalarFunctionName(self, ctx:MySqlBaseParser.ScalarFunctionNameContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#scalarFunctionName.
    def exitScalarFunctionName(self, ctx:MySqlBaseParser.ScalarFunctionNameContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#simpleFunctionCall.
    def enterSimpleFunctionCall(self, ctx:MySqlBaseParser.SimpleFunctionCallContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#simpleFunctionCall.
    def exitSimpleFunctionCall(self, ctx:MySqlBaseParser.SimpleFunctionCallContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#functionArgs.
    def enterFunctionArgs(self, ctx:MySqlBaseParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#functionArgs.
    def exitFunctionArgs(self, ctx:MySqlBaseParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#functionArg.
    def enterFunctionArg(self, ctx:MySqlBaseParser.FunctionArgContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#functionArg.
    def exitFunctionArg(self, ctx:MySqlBaseParser.FunctionArgContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#functionNameBase.
    def enterFunctionNameBase(self, ctx:MySqlBaseParser.FunctionNameBaseContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#functionNameBase.
    def exitFunctionNameBase(self, ctx:MySqlBaseParser.FunctionNameBaseContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:MySqlBaseParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:MySqlBaseParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#logicalOperator.
    def enterLogicalOperator(self, ctx:MySqlBaseParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#logicalOperator.
    def exitLogicalOperator(self, ctx:MySqlBaseParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#keywordsCanBeId.
    def enterKeywordsCanBeId(self, ctx:MySqlBaseParser.KeywordsCanBeIdContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#keywordsCanBeId.
    def exitKeywordsCanBeId(self, ctx:MySqlBaseParser.KeywordsCanBeIdContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#constant.
    def enterConstant(self, ctx:MySqlBaseParser.ConstantContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#constant.
    def exitConstant(self, ctx:MySqlBaseParser.ConstantContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#nullLiteral.
    def enterNullLiteral(self, ctx:MySqlBaseParser.NullLiteralContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#nullLiteral.
    def exitNullLiteral(self, ctx:MySqlBaseParser.NullLiteralContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#realLiteral.
    def enterRealLiteral(self, ctx:MySqlBaseParser.RealLiteralContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#realLiteral.
    def exitRealLiteral(self, ctx:MySqlBaseParser.RealLiteralContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#bitString.
    def enterBitString(self, ctx:MySqlBaseParser.BitStringContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#bitString.
    def exitBitString(self, ctx:MySqlBaseParser.BitStringContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#booleanLiteral.
    def enterBooleanLiteral(self, ctx:MySqlBaseParser.BooleanLiteralContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#booleanLiteral.
    def exitBooleanLiteral(self, ctx:MySqlBaseParser.BooleanLiteralContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#stringLiteral.
    def enterStringLiteral(self, ctx:MySqlBaseParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#stringLiteral.
    def exitStringLiteral(self, ctx:MySqlBaseParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:MySqlBaseParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:MySqlBaseParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#hexadecimalLiteral.
    def enterHexadecimalLiteral(self, ctx:MySqlBaseParser.HexadecimalLiteralContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#hexadecimalLiteral.
    def exitHexadecimalLiteral(self, ctx:MySqlBaseParser.HexadecimalLiteralContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#orderByClause.
    def enterOrderByClause(self, ctx:MySqlBaseParser.OrderByClauseContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#orderByClause.
    def exitOrderByClause(self, ctx:MySqlBaseParser.OrderByClauseContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#orderByExpression.
    def enterOrderByExpression(self, ctx:MySqlBaseParser.OrderByExpressionContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#orderByExpression.
    def exitOrderByExpression(self, ctx:MySqlBaseParser.OrderByExpressionContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#limitClause.
    def enterLimitClause(self, ctx:MySqlBaseParser.LimitClauseContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#limitClause.
    def exitLimitClause(self, ctx:MySqlBaseParser.LimitClauseContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#lockClause.
    def enterLockClause(self, ctx:MySqlBaseParser.LockClauseContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#lockClause.
    def exitLockClause(self, ctx:MySqlBaseParser.LockClauseContext):
        pass


    # Enter a parse tree produced by MySqlBaseParser#parameterMarker.
    def enterParameterMarker(self, ctx:MySqlBaseParser.ParameterMarkerContext):
        pass

    # Exit a parse tree produced by MySqlBaseParser#parameterMarker.
    def exitParameterMarker(self, ctx:MySqlBaseParser.ParameterMarkerContext):
        pass



del MySqlBaseParser