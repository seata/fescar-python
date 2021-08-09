#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from enum import Enum


class Escape(Enum):
    STANDARD = '"'
    MYSQL = '`'


class ColumnUtils(object):
    DOT = "."

    @staticmethod
    def del_escape_by_cols_dbtype(cols, db_type):
        new_cols = ColumnUtils.del_escape_by_cols_escape(cols, Escape.STANDARD)
        if ColumnUtils.is_mysql_series(db_type):
            new_cols = ColumnUtils.del_escape_by_cols_escape(cols, Escape.STANDARD)
        return new_cols

    @staticmethod
    def del_escape_by_cols_escape(cols, escape):
        if cols is None or len(cols) == 0:
            return cols
        new_cols = []
        for col in cols:
            new_cols.append(ColumnUtils.del_escape_by_colname_escape(col, escape))
        return new_cols

    @staticmethod
    def del_escape_by_colname_dbtype(col_name, db_type):
        new_col_name = ColumnUtils.del_escape_by_colname_escape(col_name, Escape.STANDARD)
        if ColumnUtils.is_mysql_series(db_type):
            new_col_name = ColumnUtils.del_escape_by_colname_escape(new_col_name, Escape.MYSQL)
        return new_col_name

    @staticmethod
    def del_escape_by_colname_escape(col_name, escape):
        if col_name is None or len(col_name) == 0:
            return col_name
        if col_name[0] == escape.value and col_name[len(col_name) - 1] == escape.value:
            # like "scheme"."id" `scheme`.`id`
            s = escape.value + ColumnUtils.DOT + escape.value
            index = col_name.find(s)
            if index > -1:
                return col_name[1: index] + ColumnUtils.DOT + col_name[index + len(s): len(col_name) - 1]
            return col_name[1:len(col_name) - 1]
        else:
            # like "scheme".id `scheme`.id
            s = escape.value + ColumnUtils.DOT
            index = col_name.find(s)
            if index > -1 and col_name[0] == escape.value:
                return col_name[1: index] + ColumnUtils.DOT + col_name[index + len(s):]
            # like scheme."id" scheme.`id`
            s = ColumnUtils.DOT + escape.value
            index = col_name.find(s)
            if index > -1 and col_name[len(col_name) - 1] == escape.value:
                return col_name[0: index] + ColumnUtils.DOT + col_name[index + len(s):]
        return col_name

    @staticmethod
    def add_escape_by_cols_dbtype(cols, db_type):
        if cols is None or len(cols) == 0:
            return cols
        new_cols = []
        for col in cols:
            new_cols.append(ColumnUtils.add_by_dbtype(col, db_type))
        return new_cols

    @staticmethod
    def add_by_dbtype(col_name, db_type):
        if ColumnUtils.is_mysql_series(db_type):
            return ColumnUtils.add_by_dbtype_escape(col_name, db_type, Escape.MYSQL)
        return ColumnUtils.add_by_dbtype_escape(col_name, db_type, Escape.STANDARD)

    @staticmethod
    def add_by_dbtype_escape(col_name, db_type, escape):
        if col_name is None or col_name == "":
            return col_name
        if col_name[0] == escape.value and col_name[len(col_name) - 1] == escape.value:
            return col_name

        # TODO
        """
        KeywordChecker keywordChecker = KeywordCheckerFactory.getKeywordChecker(dbType);
        if (keywordChecker != null) {
            boolean check = keywordChecker.checkEscape(colName);
            if (!check) {
                return colName;
            }
        }"""

        if col_name.find(ColumnUtils.DOT) > -1:
            # like "scheme".id `scheme`.id
            s = escape.value + ColumnUtils.DOT
            dot_index = col_name.find(s)
            if dot_index > -1:
                return col_name[0:dot_index + len(s)] + escape.value + col_name[dot_index + len(s):] + escape.value
            # like scheme."id" scheme.`id`
            s = ColumnUtils.DOT + escape.value
            dot_index = col_name.find(s)
            if dot_index > -1:
                return escape.value + col_name[0: dot_index] + escape.value + col_name[dot_index]

            s = ColumnUtils.DOT
            dot_index = col_name.find(s)
            if dot_index > -1:
                return escape.value + col_name[0: dot_index] + escape.value + ColumnUtils.DOT + \
                       escape.value + col_name[dot_index + len(s)] + escape.value
        return escape.value + col_name + escape.value

    @staticmethod
    def is_mysql_series(db_type):
        return db_type == 'mysql' or db_type == 'h2' or db_type == 'mariadb'
