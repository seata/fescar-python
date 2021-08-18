#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.rm.datasource.ColumnUtils import ColumnUtils
from seata.sqlparser.util.JdbcConstants import JdbcConstants


class SQLUtil:
    __quote = "[]`'\""

    @classmethod
    def remove_quota(cls, value):
        for i in range(len(cls.__quote)):
            value = value.replace(cls.__quote[i], "")
        return value

    @classmethod
    def get_db_type(cls, connection):
        server_info = connection._con._con.get_server_info().lower()
        if JdbcConstants.MARIADB in server_info or JdbcConstants.MYSQL in server_info:
            return JdbcConstants.MYSQL
        return None

    @classmethod
    def build_where_condition_by_pks(cls, pk_column_name_list, row_size, db_type):
        max_in_size = 1000
        where_str = ""
        if row_size % max_in_size == 0:
            batch_size = row_size // max_in_size
        else:
            batch_size = row_size // max_in_size + 1
        for batch in range(batch_size):
            if batch > 0:
                where_str += " or "
            where_str += "("
            for i in range(len(pk_column_name_list)):
                if i > 0:
                    where_str += ","
                where_str += ColumnUtils.add_by_dbtype(pk_column_name_list[i], db_type)
            where_str += ") in ( "
            if batch == batch_size - 1:
                if row_size % max_in_size == 0:
                    each_size = max_in_size
                else:
                    each_size = row_size % max_in_size
            else:
                each_size = max_in_size
            for i in range(each_size):
                if i > 0:
                    where_str += ","
                where_str += "("
                for x in range(len(pk_column_name_list)):
                    if x > 0:
                        where_str += ","
                    where_str += "%s"
                where_str += ")"
            where_str += ")"
        return where_str

    @classmethod
    def build_where_condition_by_pks_single(cls, pk_name_list, db_type):
        where_str = ""
        for i in range(len(pk_name_list)):
            if i > 0:
                where_str += " and "
            pk_name = pk_name_list[i]
            where_str += ColumnUtils.add_by_dbtype(pk_name, db_type)
            where_str += " = %s "
        return where_str
