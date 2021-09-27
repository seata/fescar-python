#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
from seata.tm.TransactionalTemplate import GlobalTransactional

from test_dao import TestDao


class TestService:

    @classmethod
    @GlobalTransactional()
    def save(cls, e):
        TestDao.insert()
        if e.lower() == 'true':
            raise RuntimeError('rollback')
