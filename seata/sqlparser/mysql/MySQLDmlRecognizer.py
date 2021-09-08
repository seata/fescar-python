#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.sqlparser.SQLDMLRecognizer import SQLInsertRecognizer, SQLUpdateRecognizer
from seata.sqlparser.mysql.MySQLWhereSQLRecognizer import MySQLWhereSQLRecognizer


class MySQLInsertRecognizer(SQLInsertRecognizer, MySQLWhereSQLRecognizer):
    pass


class MySQLUpdateRecognizer(SQLUpdateRecognizer, MySQLWhereSQLRecognizer):
    pass
