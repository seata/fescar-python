#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import threading

core = None
lock = threading.RLock()


class ContextCore(object):
    threadLocal = threading.local()

    @staticmethod
    def get():
        global core, lock
        if core is None:
            with lock:
                if core is None:
                    core = ContextCore()
        return core

    def put(self, key, value):
        ContextCore.threadLocal.__setattr__(key, value)

    def get(self, key):
        return ContextCore.threadLocal.__getattribute__(key)

    def remove(self, key):
        ContextCore.threadLocal.__delattr__(key, None)

    def entries(self):
        return ContextCore.threadLocal.__dict__


