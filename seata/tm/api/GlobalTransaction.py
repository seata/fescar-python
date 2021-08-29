#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class GlobalTransaction:
    def begin(self, timeout=None, name="default"):
        raise NotImplemented("need subclass implemented")

    def commit(self):
        raise NotImplemented("need subclass implemented")

    def rollback(self):
        raise NotImplemented("need subclass implemented")

    def suspend(self):
        raise NotImplemented("need subclass implemented")

    def resume(self, suspend_resource_holder):
        raise NotImplemented("need subclass implemented")

    def get_status(self):
        raise NotImplemented("need subclass implemented")

    def get_xid(self):
        raise NotImplemented("need subclass implemented")

    def global_report(self, global_status):
        raise NotImplemented("need subclass implemented")

    def get_local_status(self):
        raise NotImplemented("need subclass implemented")
