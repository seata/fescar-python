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

    @classmethod
    def del_escape_by_cols_dbtype(cls, cols, db_type):
        new_cols = cls.del_escape_by_cols_escape(cols, Escape.STANDARD)
        if cls.is_mysql_series(db_type):
            new_cols = cls.del_escape_by_cols_escape(cols, Escape.STANDARD)
        return new_cols

    @classmethod
    def del_escape_by_cols_escape(cls, cols, escape):
        if cols is None or len(cols) == 0:
            return cols
        new_cols = []
        for col in cols:
            new_cols.append(cls.del_escape_by_col_escape(col, escape))
        return new_cols

    @classmethod
    def del_escape_by_col_dbtype(cls, col_name, db_type):
        new_col_name = cls.del_escape_by_col_escape(col_name, Escape.STANDARD)
        if cls.is_mysql_series(db_type):
            new_col_name = cls.del_escape_by_col_escape(new_col_name, Escape.MYSQL)
        return new_col_name

    @classmethod
    def del_escape_by_col_escape(cls, col_name, escape):
        if col_name is None or len(col_name.strip()) == 0:
            return col_name
        if col_name[0] == escape.value and col_name[len(col_name) - 1] == escape.value:
            # like "scheme"."id" `scheme`.`id`
            s = escape.value + cls.DOT + escape.value
            index = col_name.find(s)
            if index > -1:
                return col_name[1: index] + cls.DOT + col_name[index + len(s): len(col_name) - 1]
            return col_name[1:len(col_name) - 1]
        else:
            # like "scheme".id `scheme`.id
            s = escape.value + cls.DOT
            index = col_name.find(s)
            if index > -1 and col_name[0] == escape.value:
                return col_name[1: index] + cls.DOT + col_name[index + len(s):]
            # like scheme."id" scheme.`id`
            s = cls.DOT + escape.value
            index = col_name.find(s)
            if index > -1 and col_name[len(col_name) - 1] == escape.value:
                return col_name[0: index] + cls.DOT + col_name[index + len(s):]
        return col_name

    @classmethod
    def add_escape_by_cols_dbtype(cls, cols, db_type):
        if cols is None or len(cols) == 0:
            return cols
        new_cols = []
        for col in cols:
            new_cols.append(cls.add_by_col_dbtype(col, db_type))
        return new_cols

    @classmethod
    def add_by_col_dbtype(cls, col_name, db_type):
        if cls.is_mysql_series(db_type):
            return cls.add_by_col_dbtype_escape(col_name, db_type, Escape.MYSQL)
        return cls.add_by_col_dbtype_escape(col_name, db_type, Escape.STANDARD)

    @classmethod
    def add_by_col_dbtype_escape(cls, col_name, db_type, escape):
        if col_name is None or col_name == "":
            return col_name
        if col_name[0] == escape.value and col_name[len(col_name) - 1] == escape.value:
            return col_name

        # TODO check keyword by dbtype

        if col_name.find(cls.DOT) > -1:
            # like "scheme".id `scheme`.id
            s = escape.value + cls.DOT
            dot_index = col_name.find(s)
            if dot_index > -1:
                return col_name[0:dot_index + len(s)] + escape.value + col_name[dot_index + len(s):] + escape.value
            # like scheme."id" scheme.`id`
            s = cls.DOT + escape.value
            dot_index = col_name.find(s)
            if dot_index > -1:
                return escape.value + col_name[0: dot_index] + escape.value + col_name[dot_index]

            s = cls.DOT
            dot_index = col_name.find(s)
            if dot_index > -1:
                return escape.value + col_name[0: dot_index] + escape.value + cls.DOT + \
                       escape.value + col_name[dot_index + len(s)] + escape.value
        return escape.value + col_name + escape.value

    @classmethod
    def is_mysql_series(cls, db_type):
        up = db_type.lower()
        return up == 'mysql' or up == 'h2' or up == 'mariadb'
