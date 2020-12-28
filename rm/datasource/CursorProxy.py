#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class CursorProxy(object):

    def __init__(self, target_cursor):
        self.target_cursor = target_cursor

    @property
    def description(self):
        """
        * name
        * type_code
        display_size
        internal_size
        precision
        scale
        null_ok
        """
        return self.target_cursor.description

    @property
    def rowcount(self):
        return self.target_cursor.rowcount

    # override Cursor callproc
    def callproc(self, procname, parameters=None):
        return self.target_cursor.callproc(procname, parameters)

    # override Cursor close
    def close(self):
        return self.target_cursor.close()

    # override Cursor exec
    def execute(self, operation, parameters=None):
        pass

    # override Cursor executemany
    def executemany(self, operation, seq_of_parameters=None):
        pass

    # override Cursor fetchone
    def fetchone(self):
        pass

    # override Cursor fetchmany
    def fetchmany(self, size=None):
        pass

    # override Cursor fetchall
    def fetchall(self):
        pass

    # override Cursor nextset
    def nextset(self):
        pass

    # override Cursor arraysize
    @property
    def arraysize(self):
        return self.target_cursor.arraysize

    # override Cursor setinputsizes
    def setinputsizes(self, sizes):
        return self.target_cursor.setinputsizes(sizes)

    # override Cursor setoutputsize
    def setoutputsize(self, size, column=None):
        return self.target_cursor.setinputsize(size, column)
