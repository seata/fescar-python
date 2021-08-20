#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.exception.NeedSubclassImplemented import NeedSubclassImplemented


class GlobalTransaction:
    def begin(self, timeout=None, name="default"):
        raise NeedSubclassImplemented()

    def commit(self):
        raise NeedSubclassImplemented()

    def rollback(self):
        raise NeedSubclassImplemented()

    def suspend(self):
        raise NeedSubclassImplemented()

    def resume(self, suspend_resource_holder):
        raise NeedSubclassImplemented()

    def get_status(self):
        raise NeedSubclassImplemented()

    def get_xid(self):
        raise NeedSubclassImplemented()

    def global_report(self, global_status):
        raise NeedSubclassImplemented()

    def get_local_status(self):
        raise NeedSubclassImplemented()
