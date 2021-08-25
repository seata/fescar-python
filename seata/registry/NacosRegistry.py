#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.registry.Registry import Registry


class NacosRegistry(Registry):

    def __init__(self):
        pass

    def register(self, address):
        pass

    def unregister(self, address):
        pass

    def subscribe(self, cluster, listener):
        pass

    def unsubscribe(self, cluster, listener):
        pass

    def lookup(self, key):
        pass

    def close(self):
        pass
