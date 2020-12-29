#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import sql_metadata

if __name__ == '__main__':
    sql = "insert into test(id, name) values(?, ?)"
    tables = sql_metadata.get_query_tables(sql)
    print(tables)
    columns = sql_metadata.get_query_columns(sql)
    print(columns)

    sql = "insert into test values(?, ?)"
    columns = sql_metadata.get_query_columns(sql)
    print(columns)
