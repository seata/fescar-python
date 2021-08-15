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
    def get_instance():
        global core, lock
        if core is None:
            with lock:
                if core is None:
                    core = ContextCore()
        return core

    def put(self, key, value):
        setattr(self.threadLocal, key, value)

    def get(self, key):
        try:
            return getattr(self.threadLocal, key)
        except AttributeError:
            return None

    def remove(self, key):
        delattr(self.threadLocal, key)

    def entries(self):
        return vars(self.threadLocal)
