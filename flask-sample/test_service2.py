#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
import requests
from seata.core.context.RootContext import RootContext
from seata.tm.TransactionalTemplate import GlobalTransactional

from test_dao import TestDao


class TestService:

    @classmethod
    @GlobalTransactional()
    def save(cls, e):
        TestDao.insert()
        # http request pass `KEY_XID`
        headers = {
            RootContext.KEY_XID: RootContext.get_xid()
        }
        r = requests.get('http://127.0.0.1:8000/hello?e=' + e, headers=headers)
        if r.status_code > 299:
            raise RuntimeError('rollback')
