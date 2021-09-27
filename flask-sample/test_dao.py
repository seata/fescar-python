#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
import datetime

from db import DB


class TestDao:

    @classmethod
    def insert(cls):
        con = None
        try:
            con = DB.get_data_source().connection()
            cursor = con.cursor()
            cursor.execute("insert into test values(%s, %s, %s)", (None, 'namexx', datetime.datetime.now()))
            con.commit()
        except Exception:
            con.rollback()
        finally:
            if con is not None:
                try:
                    con.close()
                except Exception:
                    pass
