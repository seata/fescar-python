#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import threading
import time


class Future:

    def __init__(self):
        self.lock = threading.Condition()
        self.start = int(round(time.time() * 1000))
        self.obj = None

    def set(self, obj):
        self.lock.acquire()
        try:
            self.obj = obj
            self.lock.notifyAll()
        finally:
            self.lock.release()

    def get(self, timeout=1):
        self.lock.acquire()
        try:
            w = self.lock.wait(timeout)
            if not w:
                raise TimeoutError()
        finally:
            self.lock.release()
        return self.obj
