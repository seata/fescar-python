#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.mysql.antlr4.value.value import IdentifierValue


class OwnerSegment:

    def __init__(self, start_index: int, stop_index: int, identifier: IdentifierValue):
        self.start_index = start_index
        self.stop_index = stop_index
        self.identifier = identifier


class AliasSegment:

    def __init__(self, start_index: int, stop_index: int, identifier: IdentifierValue):
        self.start_index = start_index
        self.stop_index = stop_index
        self.identifier = identifier


class TableNameSegment:

    def __init__(self, start_index: int, stop_index: int, identifier: IdentifierValue):
        self.start_index = start_index
        self.stop_index = stop_index
        self.identifier = identifier


class SimpleTableSegment:

    def __init__(self, table_name: TableNameSegment, owner: OwnerSegment = None, alias: AliasSegment = None):
        self.table_name = table_name
        self.owner = owner
        self.alias = alias

    def get_start_index(self):
        if self.owner is None:
            return self.table_name.start_index
        else:
            return self.owner.stop_index

    def get_stop_index(self):
        if self.alias is None:
            return self.table_name.stop_index
        else:
            return self.alias.stop_index

    def get_alias(self):
        if self.alias is None:
            return ""
        else:
            self.alias.identifier.value


class ColumnSegment:

    def __init__(self, start_index: int, stop_index: int, identifier: IdentifierValue, owner: OwnerSegment = None):
        self.start_index = start_index
        self.stop_index = stop_index
        self.identifier = identifier
        self.owner = owner


class IndexSegment:

    def __init__(self, start_index: int, stop_index: int, identifier: IdentifierValue, owner: OwnerSegment = None):
        self.start_index = start_index
        self.stop_index = stop_index
        self.identifier = identifier
        self.owner = owner


class Interval:

    def __init__(self, start_index: int, stop_index: int):
        self.start_index = start_index
        self.stop_index = stop_index


class ExpressionSegment:
    pass


class SubquerySegment:
    pass


class MySQLSelectStatement:
    def __init__(self):
        self.order_by = None
        self.limit = None


class ListExpression:
    pass


class InExpression:

    def __init__(self, start_index: int, stop_index: int, left: ExpressionSegment, right: ListExpression, not_):
        self.start_index = start_index
        self.stop_index = stop_index
        self.left = left
        self.right = right
        self.not_ = not_


class BetweenExpression:
    def __init__(self, start_index: int, stop_index: int, left: ExpressionSegment, between: ExpressionSegment, and_,
                 not_):
        self.start_index = start_index
        self.stop_index = stop_index
        self.left = left
        self.between = between
        self.and_ = and_
        self.not_ = not_


class ExistsSubqueryExpression:
    def __init__(self, start_index: int, stop_index: int, subquery_segment: SubquerySegment):
        self.start_index = start_index
        self.stop_index = stop_index
        self.subquery_segment = subquery_segment


class ParameterMarkerExpressionSegment:
    def __init__(self, start_index: int, stop_index: int, value: str):
        self.start_index = start_index
        self.stop_index = stop_index
        self.value = value


class CommonExpressionSegment:

    def __init__(self, start_index: int, stop_index: int, text: str):
        self.start_index = start_index
        self.stop_index = stop_index
        self.text = text


class LiteralExpressionSegment:
    def __init__(self, start_index: int, stop_index: int, value: str):
        self.start_index = start_index
        self.stop_index = stop_index
        self.value = value


class SubqueryExpressionSegment:
    pass


class LockSegment:
    def __init__(self, start_index: int, stop_index: int):
        self.start_index = start_index
        self.stop_index = stop_index
        self.table = []


class NotExpression:
    def __init__(self, start_index: int, stop_index: int, expression: ExpressionSegment):
        self.start_index = start_index
        self.stop_index = stop_index
        self.expression = expression


class BinaryOperationExpression:

    def __init__(self, start_index: int, stop_index: int,
                 left: ExpressionSegment, right: ExpressionSegment,
                 operator: str, text: str):
        self.start_index = start_index
        self.stop_index = stop_index
        self.left = left
        self.right = right
        self.operator = operator
        self.text = text