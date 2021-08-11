# Generated from MySqlParser.g4- by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MySqlParser import MySqlParser
else:
    from MySqlParser import MySqlParser

# This class defines a complete generic visitor for a parse tree produced by MySqlParser.

class MySqlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MySqlParser#root.
    def visitRoot(self, ctx:MySqlParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#sqlStatements.
    def visitSqlStatements(self, ctx:MySqlParser.SqlStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#sqlStatement.
    def visitSqlStatement(self, ctx:MySqlParser.SqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#emptyStatement.
    def visitEmptyStatement(self, ctx:MySqlParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ddlStatement.
    def visitDdlStatement(self, ctx:MySqlParser.DdlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dmlStatement.
    def visitDmlStatement(self, ctx:MySqlParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#transactionStatement.
    def visitTransactionStatement(self, ctx:MySqlParser.TransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#replicationStatement.
    def visitReplicationStatement(self, ctx:MySqlParser.ReplicationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#preparedStatement.
    def visitPreparedStatement(self, ctx:MySqlParser.PreparedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#compoundStatement.
    def visitCompoundStatement(self, ctx:MySqlParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#administrationStatement.
    def visitAdministrationStatement(self, ctx:MySqlParser.AdministrationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#utilityStatement.
    def visitUtilityStatement(self, ctx:MySqlParser.UtilityStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createDatabase.
    def visitCreateDatabase(self, ctx:MySqlParser.CreateDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createEvent.
    def visitCreateEvent(self, ctx:MySqlParser.CreateEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createIndex.
    def visitCreateIndex(self, ctx:MySqlParser.CreateIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createLogfileGroup.
    def visitCreateLogfileGroup(self, ctx:MySqlParser.CreateLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createProcedure.
    def visitCreateProcedure(self, ctx:MySqlParser.CreateProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createFunction.
    def visitCreateFunction(self, ctx:MySqlParser.CreateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createServer.
    def visitCreateServer(self, ctx:MySqlParser.CreateServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#copyCreateTable.
    def visitCopyCreateTable(self, ctx:MySqlParser.CopyCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#queryCreateTable.
    def visitQueryCreateTable(self, ctx:MySqlParser.QueryCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#columnCreateTable.
    def visitColumnCreateTable(self, ctx:MySqlParser.ColumnCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createTablespaceInnodb.
    def visitCreateTablespaceInnodb(self, ctx:MySqlParser.CreateTablespaceInnodbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createTablespaceNdb.
    def visitCreateTablespaceNdb(self, ctx:MySqlParser.CreateTablespaceNdbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createTrigger.
    def visitCreateTrigger(self, ctx:MySqlParser.CreateTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createView.
    def visitCreateView(self, ctx:MySqlParser.CreateViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createDatabaseOption.
    def visitCreateDatabaseOption(self, ctx:MySqlParser.CreateDatabaseOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ownerStatement.
    def visitOwnerStatement(self, ctx:MySqlParser.OwnerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#preciseSchedule.
    def visitPreciseSchedule(self, ctx:MySqlParser.PreciseScheduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#intervalSchedule.
    def visitIntervalSchedule(self, ctx:MySqlParser.IntervalScheduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#timestampValue.
    def visitTimestampValue(self, ctx:MySqlParser.TimestampValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#intervalExpr.
    def visitIntervalExpr(self, ctx:MySqlParser.IntervalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#intervalType.
    def visitIntervalType(self, ctx:MySqlParser.IntervalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#enableType.
    def visitEnableType(self, ctx:MySqlParser.EnableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexType.
    def visitIndexType(self, ctx:MySqlParser.IndexTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexOption.
    def visitIndexOption(self, ctx:MySqlParser.IndexOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#procedureParameter.
    def visitProcedureParameter(self, ctx:MySqlParser.ProcedureParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionParameter.
    def visitFunctionParameter(self, ctx:MySqlParser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineComment.
    def visitRoutineComment(self, ctx:MySqlParser.RoutineCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineLanguage.
    def visitRoutineLanguage(self, ctx:MySqlParser.RoutineLanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineBehavior.
    def visitRoutineBehavior(self, ctx:MySqlParser.RoutineBehaviorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineData.
    def visitRoutineData(self, ctx:MySqlParser.RoutineDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineSecurity.
    def visitRoutineSecurity(self, ctx:MySqlParser.RoutineSecurityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#serverOption.
    def visitServerOption(self, ctx:MySqlParser.ServerOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createDefinitions.
    def visitCreateDefinitions(self, ctx:MySqlParser.CreateDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#columnDeclaration.
    def visitColumnDeclaration(self, ctx:MySqlParser.ColumnDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#constraintDeclaration.
    def visitConstraintDeclaration(self, ctx:MySqlParser.ConstraintDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexDeclaration.
    def visitIndexDeclaration(self, ctx:MySqlParser.IndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#columnDefinition.
    def visitColumnDefinition(self, ctx:MySqlParser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nullColumnConstraint.
    def visitNullColumnConstraint(self, ctx:MySqlParser.NullColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#defaultColumnConstraint.
    def visitDefaultColumnConstraint(self, ctx:MySqlParser.DefaultColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#visibilityColumnConstraint.
    def visitVisibilityColumnConstraint(self, ctx:MySqlParser.VisibilityColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#autoIncrementColumnConstraint.
    def visitAutoIncrementColumnConstraint(self, ctx:MySqlParser.AutoIncrementColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#primaryKeyColumnConstraint.
    def visitPrimaryKeyColumnConstraint(self, ctx:MySqlParser.PrimaryKeyColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uniqueKeyColumnConstraint.
    def visitUniqueKeyColumnConstraint(self, ctx:MySqlParser.UniqueKeyColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#commentColumnConstraint.
    def visitCommentColumnConstraint(self, ctx:MySqlParser.CommentColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#formatColumnConstraint.
    def visitFormatColumnConstraint(self, ctx:MySqlParser.FormatColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#storageColumnConstraint.
    def visitStorageColumnConstraint(self, ctx:MySqlParser.StorageColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#referenceColumnConstraint.
    def visitReferenceColumnConstraint(self, ctx:MySqlParser.ReferenceColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#collateColumnConstraint.
    def visitCollateColumnConstraint(self, ctx:MySqlParser.CollateColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#generatedColumnConstraint.
    def visitGeneratedColumnConstraint(self, ctx:MySqlParser.GeneratedColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#serialDefaultColumnConstraint.
    def visitSerialDefaultColumnConstraint(self, ctx:MySqlParser.SerialDefaultColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#checkColumnConstraint.
    def visitCheckColumnConstraint(self, ctx:MySqlParser.CheckColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#primaryKeyTableConstraint.
    def visitPrimaryKeyTableConstraint(self, ctx:MySqlParser.PrimaryKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uniqueKeyTableConstraint.
    def visitUniqueKeyTableConstraint(self, ctx:MySqlParser.UniqueKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#foreignKeyTableConstraint.
    def visitForeignKeyTableConstraint(self, ctx:MySqlParser.ForeignKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#checkTableConstraint.
    def visitCheckTableConstraint(self, ctx:MySqlParser.CheckTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#referenceDefinition.
    def visitReferenceDefinition(self, ctx:MySqlParser.ReferenceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#referenceAction.
    def visitReferenceAction(self, ctx:MySqlParser.ReferenceActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#referenceControlType.
    def visitReferenceControlType(self, ctx:MySqlParser.ReferenceControlTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleIndexDeclaration.
    def visitSimpleIndexDeclaration(self, ctx:MySqlParser.SimpleIndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#specialIndexDeclaration.
    def visitSpecialIndexDeclaration(self, ctx:MySqlParser.SpecialIndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionEngine.
    def visitTableOptionEngine(self, ctx:MySqlParser.TableOptionEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionAutoIncrement.
    def visitTableOptionAutoIncrement(self, ctx:MySqlParser.TableOptionAutoIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionAverage.
    def visitTableOptionAverage(self, ctx:MySqlParser.TableOptionAverageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionCharset.
    def visitTableOptionCharset(self, ctx:MySqlParser.TableOptionCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionChecksum.
    def visitTableOptionChecksum(self, ctx:MySqlParser.TableOptionChecksumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionCollate.
    def visitTableOptionCollate(self, ctx:MySqlParser.TableOptionCollateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionComment.
    def visitTableOptionComment(self, ctx:MySqlParser.TableOptionCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionCompression.
    def visitTableOptionCompression(self, ctx:MySqlParser.TableOptionCompressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionConnection.
    def visitTableOptionConnection(self, ctx:MySqlParser.TableOptionConnectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionDataDirectory.
    def visitTableOptionDataDirectory(self, ctx:MySqlParser.TableOptionDataDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionDelay.
    def visitTableOptionDelay(self, ctx:MySqlParser.TableOptionDelayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionEncryption.
    def visitTableOptionEncryption(self, ctx:MySqlParser.TableOptionEncryptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionIndexDirectory.
    def visitTableOptionIndexDirectory(self, ctx:MySqlParser.TableOptionIndexDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionInsertMethod.
    def visitTableOptionInsertMethod(self, ctx:MySqlParser.TableOptionInsertMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionKeyBlockSize.
    def visitTableOptionKeyBlockSize(self, ctx:MySqlParser.TableOptionKeyBlockSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionMaxRows.
    def visitTableOptionMaxRows(self, ctx:MySqlParser.TableOptionMaxRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionMinRows.
    def visitTableOptionMinRows(self, ctx:MySqlParser.TableOptionMinRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionPackKeys.
    def visitTableOptionPackKeys(self, ctx:MySqlParser.TableOptionPackKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionPassword.
    def visitTableOptionPassword(self, ctx:MySqlParser.TableOptionPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionRowFormat.
    def visitTableOptionRowFormat(self, ctx:MySqlParser.TableOptionRowFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionRecalculation.
    def visitTableOptionRecalculation(self, ctx:MySqlParser.TableOptionRecalculationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionPersistent.
    def visitTableOptionPersistent(self, ctx:MySqlParser.TableOptionPersistentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionSamplePage.
    def visitTableOptionSamplePage(self, ctx:MySqlParser.TableOptionSamplePageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionTablespace.
    def visitTableOptionTablespace(self, ctx:MySqlParser.TableOptionTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionTableType.
    def visitTableOptionTableType(self, ctx:MySqlParser.TableOptionTableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableOptionUnion.
    def visitTableOptionUnion(self, ctx:MySqlParser.TableOptionUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableType.
    def visitTableType(self, ctx:MySqlParser.TableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tablespaceStorage.
    def visitTablespaceStorage(self, ctx:MySqlParser.TablespaceStorageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionDefinitions.
    def visitPartitionDefinitions(self, ctx:MySqlParser.PartitionDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionFunctionHash.
    def visitPartitionFunctionHash(self, ctx:MySqlParser.PartitionFunctionHashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionFunctionKey.
    def visitPartitionFunctionKey(self, ctx:MySqlParser.PartitionFunctionKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionFunctionRange.
    def visitPartitionFunctionRange(self, ctx:MySqlParser.PartitionFunctionRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionFunctionList.
    def visitPartitionFunctionList(self, ctx:MySqlParser.PartitionFunctionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subPartitionFunctionHash.
    def visitSubPartitionFunctionHash(self, ctx:MySqlParser.SubPartitionFunctionHashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subPartitionFunctionKey.
    def visitSubPartitionFunctionKey(self, ctx:MySqlParser.SubPartitionFunctionKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionComparison.
    def visitPartitionComparison(self, ctx:MySqlParser.PartitionComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionListAtom.
    def visitPartitionListAtom(self, ctx:MySqlParser.PartitionListAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionListVector.
    def visitPartitionListVector(self, ctx:MySqlParser.PartitionListVectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionSimple.
    def visitPartitionSimple(self, ctx:MySqlParser.PartitionSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionDefinerAtom.
    def visitPartitionDefinerAtom(self, ctx:MySqlParser.PartitionDefinerAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionDefinerVector.
    def visitPartitionDefinerVector(self, ctx:MySqlParser.PartitionDefinerVectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subpartitionDefinition.
    def visitSubpartitionDefinition(self, ctx:MySqlParser.SubpartitionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionEngine.
    def visitPartitionOptionEngine(self, ctx:MySqlParser.PartitionOptionEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionComment.
    def visitPartitionOptionComment(self, ctx:MySqlParser.PartitionOptionCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionDataDirectory.
    def visitPartitionOptionDataDirectory(self, ctx:MySqlParser.PartitionOptionDataDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionIndexDirectory.
    def visitPartitionOptionIndexDirectory(self, ctx:MySqlParser.PartitionOptionIndexDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionMaxRows.
    def visitPartitionOptionMaxRows(self, ctx:MySqlParser.PartitionOptionMaxRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionMinRows.
    def visitPartitionOptionMinRows(self, ctx:MySqlParser.PartitionOptionMinRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionTablespace.
    def visitPartitionOptionTablespace(self, ctx:MySqlParser.PartitionOptionTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#partitionOptionNodeGroup.
    def visitPartitionOptionNodeGroup(self, ctx:MySqlParser.PartitionOptionNodeGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterSimpleDatabase.
    def visitAlterSimpleDatabase(self, ctx:MySqlParser.AlterSimpleDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterUpgradeName.
    def visitAlterUpgradeName(self, ctx:MySqlParser.AlterUpgradeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterEvent.
    def visitAlterEvent(self, ctx:MySqlParser.AlterEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterFunction.
    def visitAlterFunction(self, ctx:MySqlParser.AlterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterInstance.
    def visitAlterInstance(self, ctx:MySqlParser.AlterInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterLogfileGroup.
    def visitAlterLogfileGroup(self, ctx:MySqlParser.AlterLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterProcedure.
    def visitAlterProcedure(self, ctx:MySqlParser.AlterProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterServer.
    def visitAlterServer(self, ctx:MySqlParser.AlterServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterTable.
    def visitAlterTable(self, ctx:MySqlParser.AlterTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterTablespace.
    def visitAlterTablespace(self, ctx:MySqlParser.AlterTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterView.
    def visitAlterView(self, ctx:MySqlParser.AlterViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByTableOption.
    def visitAlterByTableOption(self, ctx:MySqlParser.AlterByTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddColumn.
    def visitAlterByAddColumn(self, ctx:MySqlParser.AlterByAddColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddColumns.
    def visitAlterByAddColumns(self, ctx:MySqlParser.AlterByAddColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddIndex.
    def visitAlterByAddIndex(self, ctx:MySqlParser.AlterByAddIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddPrimaryKey.
    def visitAlterByAddPrimaryKey(self, ctx:MySqlParser.AlterByAddPrimaryKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddUniqueKey.
    def visitAlterByAddUniqueKey(self, ctx:MySqlParser.AlterByAddUniqueKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddSpecialIndex.
    def visitAlterByAddSpecialIndex(self, ctx:MySqlParser.AlterByAddSpecialIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddForeignKey.
    def visitAlterByAddForeignKey(self, ctx:MySqlParser.AlterByAddForeignKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddCheckTableConstraint.
    def visitAlterByAddCheckTableConstraint(self, ctx:MySqlParser.AlterByAddCheckTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterBySetAlgorithm.
    def visitAlterBySetAlgorithm(self, ctx:MySqlParser.AlterBySetAlgorithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByChangeDefault.
    def visitAlterByChangeDefault(self, ctx:MySqlParser.AlterByChangeDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByChangeColumn.
    def visitAlterByChangeColumn(self, ctx:MySqlParser.AlterByChangeColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByRenameColumn.
    def visitAlterByRenameColumn(self, ctx:MySqlParser.AlterByRenameColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByLock.
    def visitAlterByLock(self, ctx:MySqlParser.AlterByLockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByModifyColumn.
    def visitAlterByModifyColumn(self, ctx:MySqlParser.AlterByModifyColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropColumn.
    def visitAlterByDropColumn(self, ctx:MySqlParser.AlterByDropColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropConstraintCheck.
    def visitAlterByDropConstraintCheck(self, ctx:MySqlParser.AlterByDropConstraintCheckContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropPrimaryKey.
    def visitAlterByDropPrimaryKey(self, ctx:MySqlParser.AlterByDropPrimaryKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByRenameIndex.
    def visitAlterByRenameIndex(self, ctx:MySqlParser.AlterByRenameIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAlterIndexVisibility.
    def visitAlterByAlterIndexVisibility(self, ctx:MySqlParser.AlterByAlterIndexVisibilityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropIndex.
    def visitAlterByDropIndex(self, ctx:MySqlParser.AlterByDropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropForeignKey.
    def visitAlterByDropForeignKey(self, ctx:MySqlParser.AlterByDropForeignKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDisableKeys.
    def visitAlterByDisableKeys(self, ctx:MySqlParser.AlterByDisableKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByEnableKeys.
    def visitAlterByEnableKeys(self, ctx:MySqlParser.AlterByEnableKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByRename.
    def visitAlterByRename(self, ctx:MySqlParser.AlterByRenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByOrder.
    def visitAlterByOrder(self, ctx:MySqlParser.AlterByOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByConvertCharset.
    def visitAlterByConvertCharset(self, ctx:MySqlParser.AlterByConvertCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDefaultCharset.
    def visitAlterByDefaultCharset(self, ctx:MySqlParser.AlterByDefaultCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDiscardTablespace.
    def visitAlterByDiscardTablespace(self, ctx:MySqlParser.AlterByDiscardTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByImportTablespace.
    def visitAlterByImportTablespace(self, ctx:MySqlParser.AlterByImportTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByForce.
    def visitAlterByForce(self, ctx:MySqlParser.AlterByForceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByValidate.
    def visitAlterByValidate(self, ctx:MySqlParser.AlterByValidateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAddPartition.
    def visitAlterByAddPartition(self, ctx:MySqlParser.AlterByAddPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDropPartition.
    def visitAlterByDropPartition(self, ctx:MySqlParser.AlterByDropPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByDiscardPartition.
    def visitAlterByDiscardPartition(self, ctx:MySqlParser.AlterByDiscardPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByImportPartition.
    def visitAlterByImportPartition(self, ctx:MySqlParser.AlterByImportPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByTruncatePartition.
    def visitAlterByTruncatePartition(self, ctx:MySqlParser.AlterByTruncatePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByCoalescePartition.
    def visitAlterByCoalescePartition(self, ctx:MySqlParser.AlterByCoalescePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByReorganizePartition.
    def visitAlterByReorganizePartition(self, ctx:MySqlParser.AlterByReorganizePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByExchangePartition.
    def visitAlterByExchangePartition(self, ctx:MySqlParser.AlterByExchangePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByAnalyzePartition.
    def visitAlterByAnalyzePartition(self, ctx:MySqlParser.AlterByAnalyzePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByCheckPartition.
    def visitAlterByCheckPartition(self, ctx:MySqlParser.AlterByCheckPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByOptimizePartition.
    def visitAlterByOptimizePartition(self, ctx:MySqlParser.AlterByOptimizePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByRebuildPartition.
    def visitAlterByRebuildPartition(self, ctx:MySqlParser.AlterByRebuildPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByRepairPartition.
    def visitAlterByRepairPartition(self, ctx:MySqlParser.AlterByRepairPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByRemovePartitioning.
    def visitAlterByRemovePartitioning(self, ctx:MySqlParser.AlterByRemovePartitioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterByUpgradePartitioning.
    def visitAlterByUpgradePartitioning(self, ctx:MySqlParser.AlterByUpgradePartitioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropDatabase.
    def visitDropDatabase(self, ctx:MySqlParser.DropDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropEvent.
    def visitDropEvent(self, ctx:MySqlParser.DropEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropIndex.
    def visitDropIndex(self, ctx:MySqlParser.DropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropLogfileGroup.
    def visitDropLogfileGroup(self, ctx:MySqlParser.DropLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropProcedure.
    def visitDropProcedure(self, ctx:MySqlParser.DropProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropFunction.
    def visitDropFunction(self, ctx:MySqlParser.DropFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropServer.
    def visitDropServer(self, ctx:MySqlParser.DropServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropTable.
    def visitDropTable(self, ctx:MySqlParser.DropTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropTablespace.
    def visitDropTablespace(self, ctx:MySqlParser.DropTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropTrigger.
    def visitDropTrigger(self, ctx:MySqlParser.DropTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropView.
    def visitDropView(self, ctx:MySqlParser.DropViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#renameTable.
    def visitRenameTable(self, ctx:MySqlParser.RenameTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#renameTableClause.
    def visitRenameTableClause(self, ctx:MySqlParser.RenameTableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#truncateTable.
    def visitTruncateTable(self, ctx:MySqlParser.TruncateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#callStatement.
    def visitCallStatement(self, ctx:MySqlParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#deleteStatement.
    def visitDeleteStatement(self, ctx:MySqlParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#doStatement.
    def visitDoStatement(self, ctx:MySqlParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerStatement.
    def visitHandlerStatement(self, ctx:MySqlParser.HandlerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#insertStatement.
    def visitInsertStatement(self, ctx:MySqlParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#loadDataStatement.
    def visitLoadDataStatement(self, ctx:MySqlParser.LoadDataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#loadXmlStatement.
    def visitLoadXmlStatement(self, ctx:MySqlParser.LoadXmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#replaceStatement.
    def visitReplaceStatement(self, ctx:MySqlParser.ReplaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleSelect.
    def visitSimpleSelect(self, ctx:MySqlParser.SimpleSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#parenthesisSelect.
    def visitParenthesisSelect(self, ctx:MySqlParser.ParenthesisSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unionSelect.
    def visitUnionSelect(self, ctx:MySqlParser.UnionSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unionParenthesisSelect.
    def visitUnionParenthesisSelect(self, ctx:MySqlParser.UnionParenthesisSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#updateStatement.
    def visitUpdateStatement(self, ctx:MySqlParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#insertStatementValue.
    def visitInsertStatementValue(self, ctx:MySqlParser.InsertStatementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#updatedElement.
    def visitUpdatedElement(self, ctx:MySqlParser.UpdatedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#assignmentField.
    def visitAssignmentField(self, ctx:MySqlParser.AssignmentFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lockClause.
    def visitLockClause(self, ctx:MySqlParser.LockClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#singleDeleteStatement.
    def visitSingleDeleteStatement(self, ctx:MySqlParser.SingleDeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#multipleDeleteStatement.
    def visitMultipleDeleteStatement(self, ctx:MySqlParser.MultipleDeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerOpenStatement.
    def visitHandlerOpenStatement(self, ctx:MySqlParser.HandlerOpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerReadIndexStatement.
    def visitHandlerReadIndexStatement(self, ctx:MySqlParser.HandlerReadIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerReadStatement.
    def visitHandlerReadStatement(self, ctx:MySqlParser.HandlerReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerCloseStatement.
    def visitHandlerCloseStatement(self, ctx:MySqlParser.HandlerCloseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#singleUpdateStatement.
    def visitSingleUpdateStatement(self, ctx:MySqlParser.SingleUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#multipleUpdateStatement.
    def visitMultipleUpdateStatement(self, ctx:MySqlParser.MultipleUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#orderByClause.
    def visitOrderByClause(self, ctx:MySqlParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#orderByExpression.
    def visitOrderByExpression(self, ctx:MySqlParser.OrderByExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSources.
    def visitTableSources(self, ctx:MySqlParser.TableSourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSourceBase.
    def visitTableSourceBase(self, ctx:MySqlParser.TableSourceBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSourceNested.
    def visitTableSourceNested(self, ctx:MySqlParser.TableSourceNestedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#atomTableItem.
    def visitAtomTableItem(self, ctx:MySqlParser.AtomTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subqueryTableItem.
    def visitSubqueryTableItem(self, ctx:MySqlParser.SubqueryTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableSourcesItem.
    def visitTableSourcesItem(self, ctx:MySqlParser.TableSourcesItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexHint.
    def visitIndexHint(self, ctx:MySqlParser.IndexHintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexHintType.
    def visitIndexHintType(self, ctx:MySqlParser.IndexHintTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#innerJoin.
    def visitInnerJoin(self, ctx:MySqlParser.InnerJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#straightJoin.
    def visitStraightJoin(self, ctx:MySqlParser.StraightJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#outerJoin.
    def visitOuterJoin(self, ctx:MySqlParser.OuterJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#naturalJoin.
    def visitNaturalJoin(self, ctx:MySqlParser.NaturalJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#queryExpression.
    def visitQueryExpression(self, ctx:MySqlParser.QueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#queryExpressionNointo.
    def visitQueryExpressionNointo(self, ctx:MySqlParser.QueryExpressionNointoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#querySpecification.
    def visitQuerySpecification(self, ctx:MySqlParser.QuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#querySpecificationNointo.
    def visitQuerySpecificationNointo(self, ctx:MySqlParser.QuerySpecificationNointoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unionParenthesis.
    def visitUnionParenthesis(self, ctx:MySqlParser.UnionParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unionStatement.
    def visitUnionStatement(self, ctx:MySqlParser.UnionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectSpec.
    def visitSelectSpec(self, ctx:MySqlParser.SelectSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectElements.
    def visitSelectElements(self, ctx:MySqlParser.SelectElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectStarElement.
    def visitSelectStarElement(self, ctx:MySqlParser.SelectStarElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectColumnElement.
    def visitSelectColumnElement(self, ctx:MySqlParser.SelectColumnElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectFunctionElement.
    def visitSelectFunctionElement(self, ctx:MySqlParser.SelectFunctionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectExpressionElement.
    def visitSelectExpressionElement(self, ctx:MySqlParser.SelectExpressionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectIntoVariables.
    def visitSelectIntoVariables(self, ctx:MySqlParser.SelectIntoVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectIntoDumpFile.
    def visitSelectIntoDumpFile(self, ctx:MySqlParser.SelectIntoDumpFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectIntoTextFile.
    def visitSelectIntoTextFile(self, ctx:MySqlParser.SelectIntoTextFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectFieldsInto.
    def visitSelectFieldsInto(self, ctx:MySqlParser.SelectFieldsIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#selectLinesInto.
    def visitSelectLinesInto(self, ctx:MySqlParser.SelectLinesIntoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fromClause.
    def visitFromClause(self, ctx:MySqlParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#groupByClause.
    def visitGroupByClause(self, ctx:MySqlParser.GroupByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#havingClause.
    def visitHavingClause(self, ctx:MySqlParser.HavingClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#groupByItem.
    def visitGroupByItem(self, ctx:MySqlParser.GroupByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#limitClause.
    def visitLimitClause(self, ctx:MySqlParser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#limitClauseAtom.
    def visitLimitClauseAtom(self, ctx:MySqlParser.LimitClauseAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#startTransaction.
    def visitStartTransaction(self, ctx:MySqlParser.StartTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#beginWork.
    def visitBeginWork(self, ctx:MySqlParser.BeginWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#commitWork.
    def visitCommitWork(self, ctx:MySqlParser.CommitWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#rollbackWork.
    def visitRollbackWork(self, ctx:MySqlParser.RollbackWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#savepointStatement.
    def visitSavepointStatement(self, ctx:MySqlParser.SavepointStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#rollbackStatement.
    def visitRollbackStatement(self, ctx:MySqlParser.RollbackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#releaseStatement.
    def visitReleaseStatement(self, ctx:MySqlParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lockTables.
    def visitLockTables(self, ctx:MySqlParser.LockTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unlockTables.
    def visitUnlockTables(self, ctx:MySqlParser.UnlockTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setAutocommitStatement.
    def visitSetAutocommitStatement(self, ctx:MySqlParser.SetAutocommitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setTransactionStatement.
    def visitSetTransactionStatement(self, ctx:MySqlParser.SetTransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#transactionMode.
    def visitTransactionMode(self, ctx:MySqlParser.TransactionModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lockTableElement.
    def visitLockTableElement(self, ctx:MySqlParser.LockTableElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lockAction.
    def visitLockAction(self, ctx:MySqlParser.LockActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#transactionOption.
    def visitTransactionOption(self, ctx:MySqlParser.TransactionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#transactionLevel.
    def visitTransactionLevel(self, ctx:MySqlParser.TransactionLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#changeMaster.
    def visitChangeMaster(self, ctx:MySqlParser.ChangeMasterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#changeReplicationFilter.
    def visitChangeReplicationFilter(self, ctx:MySqlParser.ChangeReplicationFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#purgeBinaryLogs.
    def visitPurgeBinaryLogs(self, ctx:MySqlParser.PurgeBinaryLogsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#resetMaster.
    def visitResetMaster(self, ctx:MySqlParser.ResetMasterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#resetSlave.
    def visitResetSlave(self, ctx:MySqlParser.ResetSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#startSlave.
    def visitStartSlave(self, ctx:MySqlParser.StartSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stopSlave.
    def visitStopSlave(self, ctx:MySqlParser.StopSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#startGroupReplication.
    def visitStartGroupReplication(self, ctx:MySqlParser.StartGroupReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stopGroupReplication.
    def visitStopGroupReplication(self, ctx:MySqlParser.StopGroupReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterStringOption.
    def visitMasterStringOption(self, ctx:MySqlParser.MasterStringOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterDecimalOption.
    def visitMasterDecimalOption(self, ctx:MySqlParser.MasterDecimalOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterBoolOption.
    def visitMasterBoolOption(self, ctx:MySqlParser.MasterBoolOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterRealOption.
    def visitMasterRealOption(self, ctx:MySqlParser.MasterRealOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterUidListOption.
    def visitMasterUidListOption(self, ctx:MySqlParser.MasterUidListOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stringMasterOption.
    def visitStringMasterOption(self, ctx:MySqlParser.StringMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#decimalMasterOption.
    def visitDecimalMasterOption(self, ctx:MySqlParser.DecimalMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#boolMasterOption.
    def visitBoolMasterOption(self, ctx:MySqlParser.BoolMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#channelOption.
    def visitChannelOption(self, ctx:MySqlParser.ChannelOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#doDbReplication.
    def visitDoDbReplication(self, ctx:MySqlParser.DoDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ignoreDbReplication.
    def visitIgnoreDbReplication(self, ctx:MySqlParser.IgnoreDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#doTableReplication.
    def visitDoTableReplication(self, ctx:MySqlParser.DoTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ignoreTableReplication.
    def visitIgnoreTableReplication(self, ctx:MySqlParser.IgnoreTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#wildDoTableReplication.
    def visitWildDoTableReplication(self, ctx:MySqlParser.WildDoTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#wildIgnoreTableReplication.
    def visitWildIgnoreTableReplication(self, ctx:MySqlParser.WildIgnoreTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#rewriteDbReplication.
    def visitRewriteDbReplication(self, ctx:MySqlParser.RewriteDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tablePair.
    def visitTablePair(self, ctx:MySqlParser.TablePairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#threadType.
    def visitThreadType(self, ctx:MySqlParser.ThreadTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#gtidsUntilOption.
    def visitGtidsUntilOption(self, ctx:MySqlParser.GtidsUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#masterLogUntilOption.
    def visitMasterLogUntilOption(self, ctx:MySqlParser.MasterLogUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#relayLogUntilOption.
    def visitRelayLogUntilOption(self, ctx:MySqlParser.RelayLogUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#sqlGapsUntilOption.
    def visitSqlGapsUntilOption(self, ctx:MySqlParser.SqlGapsUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userConnectionOption.
    def visitUserConnectionOption(self, ctx:MySqlParser.UserConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#passwordConnectionOption.
    def visitPasswordConnectionOption(self, ctx:MySqlParser.PasswordConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#defaultAuthConnectionOption.
    def visitDefaultAuthConnectionOption(self, ctx:MySqlParser.DefaultAuthConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#pluginDirConnectionOption.
    def visitPluginDirConnectionOption(self, ctx:MySqlParser.PluginDirConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#gtuidSet.
    def visitGtuidSet(self, ctx:MySqlParser.GtuidSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaStartTransaction.
    def visitXaStartTransaction(self, ctx:MySqlParser.XaStartTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaEndTransaction.
    def visitXaEndTransaction(self, ctx:MySqlParser.XaEndTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaPrepareStatement.
    def visitXaPrepareStatement(self, ctx:MySqlParser.XaPrepareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaCommitWork.
    def visitXaCommitWork(self, ctx:MySqlParser.XaCommitWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaRollbackWork.
    def visitXaRollbackWork(self, ctx:MySqlParser.XaRollbackWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xaRecoverWork.
    def visitXaRecoverWork(self, ctx:MySqlParser.XaRecoverWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#prepareStatement.
    def visitPrepareStatement(self, ctx:MySqlParser.PrepareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#executeStatement.
    def visitExecuteStatement(self, ctx:MySqlParser.ExecuteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#deallocatePrepare.
    def visitDeallocatePrepare(self, ctx:MySqlParser.DeallocatePrepareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#routineBody.
    def visitRoutineBody(self, ctx:MySqlParser.RoutineBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#blockStatement.
    def visitBlockStatement(self, ctx:MySqlParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseStatement.
    def visitCaseStatement(self, ctx:MySqlParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ifStatement.
    def visitIfStatement(self, ctx:MySqlParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#iterateStatement.
    def visitIterateStatement(self, ctx:MySqlParser.IterateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#leaveStatement.
    def visitLeaveStatement(self, ctx:MySqlParser.LeaveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#loopStatement.
    def visitLoopStatement(self, ctx:MySqlParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#repeatStatement.
    def visitRepeatStatement(self, ctx:MySqlParser.RepeatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#returnStatement.
    def visitReturnStatement(self, ctx:MySqlParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#whileStatement.
    def visitWhileStatement(self, ctx:MySqlParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#CloseCursor.
    def visitCloseCursor(self, ctx:MySqlParser.CloseCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#FetchCursor.
    def visitFetchCursor(self, ctx:MySqlParser.FetchCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#OpenCursor.
    def visitOpenCursor(self, ctx:MySqlParser.OpenCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#declareVariable.
    def visitDeclareVariable(self, ctx:MySqlParser.DeclareVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#declareCondition.
    def visitDeclareCondition(self, ctx:MySqlParser.DeclareConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#declareCursor.
    def visitDeclareCursor(self, ctx:MySqlParser.DeclareCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#declareHandler.
    def visitDeclareHandler(self, ctx:MySqlParser.DeclareHandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionCode.
    def visitHandlerConditionCode(self, ctx:MySqlParser.HandlerConditionCodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionState.
    def visitHandlerConditionState(self, ctx:MySqlParser.HandlerConditionStateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionName.
    def visitHandlerConditionName(self, ctx:MySqlParser.HandlerConditionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionWarning.
    def visitHandlerConditionWarning(self, ctx:MySqlParser.HandlerConditionWarningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionNotfound.
    def visitHandlerConditionNotfound(self, ctx:MySqlParser.HandlerConditionNotfoundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#handlerConditionException.
    def visitHandlerConditionException(self, ctx:MySqlParser.HandlerConditionExceptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#procedureSqlStatement.
    def visitProcedureSqlStatement(self, ctx:MySqlParser.ProcedureSqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseAlternative.
    def visitCaseAlternative(self, ctx:MySqlParser.CaseAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#elifAlternative.
    def visitElifAlternative(self, ctx:MySqlParser.ElifAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterUserMysqlV56.
    def visitAlterUserMysqlV56(self, ctx:MySqlParser.AlterUserMysqlV56Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#alterUserMysqlV57.
    def visitAlterUserMysqlV57(self, ctx:MySqlParser.AlterUserMysqlV57Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createUserMysqlV56.
    def visitCreateUserMysqlV56(self, ctx:MySqlParser.CreateUserMysqlV56Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createUserMysqlV57.
    def visitCreateUserMysqlV57(self, ctx:MySqlParser.CreateUserMysqlV57Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dropUser.
    def visitDropUser(self, ctx:MySqlParser.DropUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#grantStatement.
    def visitGrantStatement(self, ctx:MySqlParser.GrantStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#grantProxy.
    def visitGrantProxy(self, ctx:MySqlParser.GrantProxyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#renameUser.
    def visitRenameUser(self, ctx:MySqlParser.RenameUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#detailRevoke.
    def visitDetailRevoke(self, ctx:MySqlParser.DetailRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#shortRevoke.
    def visitShortRevoke(self, ctx:MySqlParser.ShortRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#roleRevoke.
    def visitRoleRevoke(self, ctx:MySqlParser.RoleRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#revokeProxy.
    def visitRevokeProxy(self, ctx:MySqlParser.RevokeProxyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setPasswordStatement.
    def visitSetPasswordStatement(self, ctx:MySqlParser.SetPasswordStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userSpecification.
    def visitUserSpecification(self, ctx:MySqlParser.UserSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#passwordAuthOption.
    def visitPasswordAuthOption(self, ctx:MySqlParser.PasswordAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stringAuthOption.
    def visitStringAuthOption(self, ctx:MySqlParser.StringAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#hashAuthOption.
    def visitHashAuthOption(self, ctx:MySqlParser.HashAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleAuthOption.
    def visitSimpleAuthOption(self, ctx:MySqlParser.SimpleAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tlsOption.
    def visitTlsOption(self, ctx:MySqlParser.TlsOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userResourceOption.
    def visitUserResourceOption(self, ctx:MySqlParser.UserResourceOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userPasswordOption.
    def visitUserPasswordOption(self, ctx:MySqlParser.UserPasswordOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userLockOption.
    def visitUserLockOption(self, ctx:MySqlParser.UserLockOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#privelegeClause.
    def visitPrivelegeClause(self, ctx:MySqlParser.PrivelegeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#privilege.
    def visitPrivilege(self, ctx:MySqlParser.PrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#currentSchemaPriviLevel.
    def visitCurrentSchemaPriviLevel(self, ctx:MySqlParser.CurrentSchemaPriviLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#globalPrivLevel.
    def visitGlobalPrivLevel(self, ctx:MySqlParser.GlobalPrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#definiteSchemaPrivLevel.
    def visitDefiniteSchemaPrivLevel(self, ctx:MySqlParser.DefiniteSchemaPrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#definiteFullTablePrivLevel.
    def visitDefiniteFullTablePrivLevel(self, ctx:MySqlParser.DefiniteFullTablePrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#definiteFullTablePrivLevel2.
    def visitDefiniteFullTablePrivLevel2(self, ctx:MySqlParser.DefiniteFullTablePrivLevel2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#definiteTablePrivLevel.
    def visitDefiniteTablePrivLevel(self, ctx:MySqlParser.DefiniteTablePrivLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#renameUserClause.
    def visitRenameUserClause(self, ctx:MySqlParser.RenameUserClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#analyzeTable.
    def visitAnalyzeTable(self, ctx:MySqlParser.AnalyzeTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#checkTable.
    def visitCheckTable(self, ctx:MySqlParser.CheckTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#checksumTable.
    def visitChecksumTable(self, ctx:MySqlParser.ChecksumTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#optimizeTable.
    def visitOptimizeTable(self, ctx:MySqlParser.OptimizeTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#repairTable.
    def visitRepairTable(self, ctx:MySqlParser.RepairTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#checkTableOption.
    def visitCheckTableOption(self, ctx:MySqlParser.CheckTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#createUdfunction.
    def visitCreateUdfunction(self, ctx:MySqlParser.CreateUdfunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#installPlugin.
    def visitInstallPlugin(self, ctx:MySqlParser.InstallPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uninstallPlugin.
    def visitUninstallPlugin(self, ctx:MySqlParser.UninstallPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setVariable.
    def visitSetVariable(self, ctx:MySqlParser.SetVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setCharset.
    def visitSetCharset(self, ctx:MySqlParser.SetCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setNames.
    def visitSetNames(self, ctx:MySqlParser.SetNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setPassword.
    def visitSetPassword(self, ctx:MySqlParser.SetPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setTransaction.
    def visitSetTransaction(self, ctx:MySqlParser.SetTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setAutocommit.
    def visitSetAutocommit(self, ctx:MySqlParser.SetAutocommitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#setNewValueInsideTrigger.
    def visitSetNewValueInsideTrigger(self, ctx:MySqlParser.SetNewValueInsideTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showMasterLogs.
    def visitShowMasterLogs(self, ctx:MySqlParser.ShowMasterLogsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showLogEvents.
    def visitShowLogEvents(self, ctx:MySqlParser.ShowLogEventsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showObjectFilter.
    def visitShowObjectFilter(self, ctx:MySqlParser.ShowObjectFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showColumns.
    def visitShowColumns(self, ctx:MySqlParser.ShowColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showCreateDb.
    def visitShowCreateDb(self, ctx:MySqlParser.ShowCreateDbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showCreateFullIdObject.
    def visitShowCreateFullIdObject(self, ctx:MySqlParser.ShowCreateFullIdObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showCreateUser.
    def visitShowCreateUser(self, ctx:MySqlParser.ShowCreateUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showEngine.
    def visitShowEngine(self, ctx:MySqlParser.ShowEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showGlobalInfo.
    def visitShowGlobalInfo(self, ctx:MySqlParser.ShowGlobalInfoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showErrors.
    def visitShowErrors(self, ctx:MySqlParser.ShowErrorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showCountErrors.
    def visitShowCountErrors(self, ctx:MySqlParser.ShowCountErrorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showSchemaFilter.
    def visitShowSchemaFilter(self, ctx:MySqlParser.ShowSchemaFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showRoutine.
    def visitShowRoutine(self, ctx:MySqlParser.ShowRoutineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showGrants.
    def visitShowGrants(self, ctx:MySqlParser.ShowGrantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showIndexes.
    def visitShowIndexes(self, ctx:MySqlParser.ShowIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showOpenTables.
    def visitShowOpenTables(self, ctx:MySqlParser.ShowOpenTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showProfile.
    def visitShowProfile(self, ctx:MySqlParser.ShowProfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showSlaveStatus.
    def visitShowSlaveStatus(self, ctx:MySqlParser.ShowSlaveStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#variableClause.
    def visitVariableClause(self, ctx:MySqlParser.VariableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showCommonEntity.
    def visitShowCommonEntity(self, ctx:MySqlParser.ShowCommonEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showFilter.
    def visitShowFilter(self, ctx:MySqlParser.ShowFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showGlobalInfoClause.
    def visitShowGlobalInfoClause(self, ctx:MySqlParser.ShowGlobalInfoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showSchemaEntity.
    def visitShowSchemaEntity(self, ctx:MySqlParser.ShowSchemaEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#showProfileType.
    def visitShowProfileType(self, ctx:MySqlParser.ShowProfileTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#binlogStatement.
    def visitBinlogStatement(self, ctx:MySqlParser.BinlogStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#cacheIndexStatement.
    def visitCacheIndexStatement(self, ctx:MySqlParser.CacheIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#flushStatement.
    def visitFlushStatement(self, ctx:MySqlParser.FlushStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#killStatement.
    def visitKillStatement(self, ctx:MySqlParser.KillStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#loadIndexIntoCache.
    def visitLoadIndexIntoCache(self, ctx:MySqlParser.LoadIndexIntoCacheContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#resetStatement.
    def visitResetStatement(self, ctx:MySqlParser.ResetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#shutdownStatement.
    def visitShutdownStatement(self, ctx:MySqlParser.ShutdownStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableIndexes.
    def visitTableIndexes(self, ctx:MySqlParser.TableIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleFlushOption.
    def visitSimpleFlushOption(self, ctx:MySqlParser.SimpleFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#channelFlushOption.
    def visitChannelFlushOption(self, ctx:MySqlParser.ChannelFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableFlushOption.
    def visitTableFlushOption(self, ctx:MySqlParser.TableFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#flushTableOption.
    def visitFlushTableOption(self, ctx:MySqlParser.FlushTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#loadedTableIndexes.
    def visitLoadedTableIndexes(self, ctx:MySqlParser.LoadedTableIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleDescribeStatement.
    def visitSimpleDescribeStatement(self, ctx:MySqlParser.SimpleDescribeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullDescribeStatement.
    def visitFullDescribeStatement(self, ctx:MySqlParser.FullDescribeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#helpStatement.
    def visitHelpStatement(self, ctx:MySqlParser.HelpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#useStatement.
    def visitUseStatement(self, ctx:MySqlParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#signalStatement.
    def visitSignalStatement(self, ctx:MySqlParser.SignalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#resignalStatement.
    def visitResignalStatement(self, ctx:MySqlParser.ResignalStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#signalConditionInformation.
    def visitSignalConditionInformation(self, ctx:MySqlParser.SignalConditionInformationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#diagnosticsStatement.
    def visitDiagnosticsStatement(self, ctx:MySqlParser.DiagnosticsStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#diagnosticsConditionInformationName.
    def visitDiagnosticsConditionInformationName(self, ctx:MySqlParser.DiagnosticsConditionInformationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#describeStatements.
    def visitDescribeStatements(self, ctx:MySqlParser.DescribeStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#describeConnection.
    def visitDescribeConnection(self, ctx:MySqlParser.DescribeConnectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullId.
    def visitFullId(self, ctx:MySqlParser.FullIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tableName.
    def visitTableName(self, ctx:MySqlParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullColumnName.
    def visitFullColumnName(self, ctx:MySqlParser.FullColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexColumnName.
    def visitIndexColumnName(self, ctx:MySqlParser.IndexColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userName.
    def visitUserName(self, ctx:MySqlParser.UserNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#mysqlVariable.
    def visitMysqlVariable(self, ctx:MySqlParser.MysqlVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#charsetName.
    def visitCharsetName(self, ctx:MySqlParser.CharsetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#collationName.
    def visitCollationName(self, ctx:MySqlParser.CollationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#engineName.
    def visitEngineName(self, ctx:MySqlParser.EngineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uuidSet.
    def visitUuidSet(self, ctx:MySqlParser.UuidSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xid.
    def visitXid(self, ctx:MySqlParser.XidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#xuidStringId.
    def visitXuidStringId(self, ctx:MySqlParser.XuidStringIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#authPlugin.
    def visitAuthPlugin(self, ctx:MySqlParser.AuthPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uid.
    def visitUid(self, ctx:MySqlParser.UidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleId.
    def visitSimpleId(self, ctx:MySqlParser.SimpleIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dottedId.
    def visitDottedId(self, ctx:MySqlParser.DottedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:MySqlParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fileSizeLiteral.
    def visitFileSizeLiteral(self, ctx:MySqlParser.FileSizeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stringLiteral.
    def visitStringLiteral(self, ctx:MySqlParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:MySqlParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#hexadecimalLiteral.
    def visitHexadecimalLiteral(self, ctx:MySqlParser.HexadecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nullNotnull.
    def visitNullNotnull(self, ctx:MySqlParser.NullNotnullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#constant.
    def visitConstant(self, ctx:MySqlParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#stringDataType.
    def visitStringDataType(self, ctx:MySqlParser.StringDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nationalStringDataType.
    def visitNationalStringDataType(self, ctx:MySqlParser.NationalStringDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nationalVaryingStringDataType.
    def visitNationalVaryingStringDataType(self, ctx:MySqlParser.NationalVaryingStringDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dimensionDataType.
    def visitDimensionDataType(self, ctx:MySqlParser.DimensionDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleDataType.
    def visitSimpleDataType(self, ctx:MySqlParser.SimpleDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#collectionDataType.
    def visitCollectionDataType(self, ctx:MySqlParser.CollectionDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#spatialDataType.
    def visitSpatialDataType(self, ctx:MySqlParser.SpatialDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#longVarcharDataType.
    def visitLongVarcharDataType(self, ctx:MySqlParser.LongVarcharDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#longVarbinaryDataType.
    def visitLongVarbinaryDataType(self, ctx:MySqlParser.LongVarbinaryDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#collectionOptions.
    def visitCollectionOptions(self, ctx:MySqlParser.CollectionOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#convertedDataType.
    def visitConvertedDataType(self, ctx:MySqlParser.ConvertedDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lengthOneDimension.
    def visitLengthOneDimension(self, ctx:MySqlParser.LengthOneDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lengthTwoDimension.
    def visitLengthTwoDimension(self, ctx:MySqlParser.LengthTwoDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#lengthTwoOptionalDimension.
    def visitLengthTwoOptionalDimension(self, ctx:MySqlParser.LengthTwoOptionalDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#uidList.
    def visitUidList(self, ctx:MySqlParser.UidListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#tables.
    def visitTables(self, ctx:MySqlParser.TablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#indexColumnNames.
    def visitIndexColumnNames(self, ctx:MySqlParser.IndexColumnNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#expressions.
    def visitExpressions(self, ctx:MySqlParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#expressionsWithDefaults.
    def visitExpressionsWithDefaults(self, ctx:MySqlParser.ExpressionsWithDefaultsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#constants.
    def visitConstants(self, ctx:MySqlParser.ConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleStrings.
    def visitSimpleStrings(self, ctx:MySqlParser.SimpleStringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#userVariables.
    def visitUserVariables(self, ctx:MySqlParser.UserVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#defaultValue.
    def visitDefaultValue(self, ctx:MySqlParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#currentTimestamp.
    def visitCurrentTimestamp(self, ctx:MySqlParser.CurrentTimestampContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#expressionOrDefault.
    def visitExpressionOrDefault(self, ctx:MySqlParser.ExpressionOrDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ifExists.
    def visitIfExists(self, ctx:MySqlParser.IfExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#ifNotExists.
    def visitIfNotExists(self, ctx:MySqlParser.IfNotExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#specificFunctionCall.
    def visitSpecificFunctionCall(self, ctx:MySqlParser.SpecificFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#aggregateFunctionCall.
    def visitAggregateFunctionCall(self, ctx:MySqlParser.AggregateFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#scalarFunctionCall.
    def visitScalarFunctionCall(self, ctx:MySqlParser.ScalarFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#udfFunctionCall.
    def visitUdfFunctionCall(self, ctx:MySqlParser.UdfFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#passwordFunctionCall.
    def visitPasswordFunctionCall(self, ctx:MySqlParser.PasswordFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#simpleFunctionCall.
    def visitSimpleFunctionCall(self, ctx:MySqlParser.SimpleFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dataTypeFunctionCall.
    def visitDataTypeFunctionCall(self, ctx:MySqlParser.DataTypeFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#valuesFunctionCall.
    def visitValuesFunctionCall(self, ctx:MySqlParser.ValuesFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseExpressionFunctionCall.
    def visitCaseExpressionFunctionCall(self, ctx:MySqlParser.CaseExpressionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseFunctionCall.
    def visitCaseFunctionCall(self, ctx:MySqlParser.CaseFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#charFunctionCall.
    def visitCharFunctionCall(self, ctx:MySqlParser.CharFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#positionFunctionCall.
    def visitPositionFunctionCall(self, ctx:MySqlParser.PositionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#substrFunctionCall.
    def visitSubstrFunctionCall(self, ctx:MySqlParser.SubstrFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#trimFunctionCall.
    def visitTrimFunctionCall(self, ctx:MySqlParser.TrimFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#weightFunctionCall.
    def visitWeightFunctionCall(self, ctx:MySqlParser.WeightFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#extractFunctionCall.
    def visitExtractFunctionCall(self, ctx:MySqlParser.ExtractFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#getFormatFunctionCall.
    def visitGetFormatFunctionCall(self, ctx:MySqlParser.GetFormatFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#jsonValueFunctionCall.
    def visitJsonValueFunctionCall(self, ctx:MySqlParser.JsonValueFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#caseFuncAlternative.
    def visitCaseFuncAlternative(self, ctx:MySqlParser.CaseFuncAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#levelWeightList.
    def visitLevelWeightList(self, ctx:MySqlParser.LevelWeightListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#levelWeightRange.
    def visitLevelWeightRange(self, ctx:MySqlParser.LevelWeightRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#levelInWeightListElement.
    def visitLevelInWeightListElement(self, ctx:MySqlParser.LevelInWeightListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#aggregateWindowedFunction.
    def visitAggregateWindowedFunction(self, ctx:MySqlParser.AggregateWindowedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#scalarFunctionName.
    def visitScalarFunctionName(self, ctx:MySqlParser.ScalarFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#passwordFunctionClause.
    def visitPasswordFunctionClause(self, ctx:MySqlParser.PasswordFunctionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionArgs.
    def visitFunctionArgs(self, ctx:MySqlParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionArg.
    def visitFunctionArg(self, ctx:MySqlParser.FunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#isExpression.
    def visitIsExpression(self, ctx:MySqlParser.IsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#notExpression.
    def visitNotExpression(self, ctx:MySqlParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#logicalExpression.
    def visitLogicalExpression(self, ctx:MySqlParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#predicateExpression.
    def visitPredicateExpression(self, ctx:MySqlParser.PredicateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#soundsLikePredicate.
    def visitSoundsLikePredicate(self, ctx:MySqlParser.SoundsLikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#expressionAtomPredicate.
    def visitExpressionAtomPredicate(self, ctx:MySqlParser.ExpressionAtomPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subqueryComparisonPredicate.
    def visitSubqueryComparisonPredicate(self, ctx:MySqlParser.SubqueryComparisonPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#jsonMemberOfPredicate.
    def visitJsonMemberOfPredicate(self, ctx:MySqlParser.JsonMemberOfPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#binaryComparisonPredicate.
    def visitBinaryComparisonPredicate(self, ctx:MySqlParser.BinaryComparisonPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#inPredicate.
    def visitInPredicate(self, ctx:MySqlParser.InPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#betweenPredicate.
    def visitBetweenPredicate(self, ctx:MySqlParser.BetweenPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#isNullPredicate.
    def visitIsNullPredicate(self, ctx:MySqlParser.IsNullPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#likePredicate.
    def visitLikePredicate(self, ctx:MySqlParser.LikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#regexpPredicate.
    def visitRegexpPredicate(self, ctx:MySqlParser.RegexpPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unaryExpressionAtom.
    def visitUnaryExpressionAtom(self, ctx:MySqlParser.UnaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#collateExpressionAtom.
    def visitCollateExpressionAtom(self, ctx:MySqlParser.CollateExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#mysqlVariableExpressionAtom.
    def visitMysqlVariableExpressionAtom(self, ctx:MySqlParser.MysqlVariableExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nestedExpressionAtom.
    def visitNestedExpressionAtom(self, ctx:MySqlParser.NestedExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#nestedRowExpressionAtom.
    def visitNestedRowExpressionAtom(self, ctx:MySqlParser.NestedRowExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#mathExpressionAtom.
    def visitMathExpressionAtom(self, ctx:MySqlParser.MathExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#existsExpressionAtom.
    def visitExistsExpressionAtom(self, ctx:MySqlParser.ExistsExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#intervalExpressionAtom.
    def visitIntervalExpressionAtom(self, ctx:MySqlParser.IntervalExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#jsonExpressionAtom.
    def visitJsonExpressionAtom(self, ctx:MySqlParser.JsonExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#subqueryExpressionAtom.
    def visitSubqueryExpressionAtom(self, ctx:MySqlParser.SubqueryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#constantExpressionAtom.
    def visitConstantExpressionAtom(self, ctx:MySqlParser.ConstantExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionCallExpressionAtom.
    def visitFunctionCallExpressionAtom(self, ctx:MySqlParser.FunctionCallExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#binaryExpressionAtom.
    def visitBinaryExpressionAtom(self, ctx:MySqlParser.BinaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#fullColumnNameExpressionAtom.
    def visitFullColumnNameExpressionAtom(self, ctx:MySqlParser.FullColumnNameExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#bitExpressionAtom.
    def visitBitExpressionAtom(self, ctx:MySqlParser.BitExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#unaryOperator.
    def visitUnaryOperator(self, ctx:MySqlParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:MySqlParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#logicalOperator.
    def visitLogicalOperator(self, ctx:MySqlParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#bitOperator.
    def visitBitOperator(self, ctx:MySqlParser.BitOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#mathOperator.
    def visitMathOperator(self, ctx:MySqlParser.MathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#jsonOperator.
    def visitJsonOperator(self, ctx:MySqlParser.JsonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#charsetNameBase.
    def visitCharsetNameBase(self, ctx:MySqlParser.CharsetNameBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#transactionLevelBase.
    def visitTransactionLevelBase(self, ctx:MySqlParser.TransactionLevelBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#privilegesBase.
    def visitPrivilegesBase(self, ctx:MySqlParser.PrivilegesBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#intervalTypeBase.
    def visitIntervalTypeBase(self, ctx:MySqlParser.IntervalTypeBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#dataTypeBase.
    def visitDataTypeBase(self, ctx:MySqlParser.DataTypeBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#keywordsCanBeId.
    def visitKeywordsCanBeId(self, ctx:MySqlParser.KeywordsCanBeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#functionNameBase.
    def visitFunctionNameBase(self, ctx:MySqlParser.FunctionNameBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MySqlParser#parameterMarker.
    def visitParameterMarker(self, ctx:MySqlParser.ParameterMarkerContext):
        return self.visitChildren(ctx)



del MySqlParser