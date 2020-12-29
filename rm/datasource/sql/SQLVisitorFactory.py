#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import sql_metadata

from exception.NotSupportYetException import NotSupportYetException
from sqlparser.util.JdbcConstants import JdbcConstants


class SQLVisitorFactory(object):

    @staticmethod
    def get(target_sql, db_type):
        if db_type != JdbcConstants.MYSQL:
            raise NotSupportYetException()

