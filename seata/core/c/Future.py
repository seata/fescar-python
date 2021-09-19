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
        self.completed = False
        self.result = None

    def set(self, result):
        try:
            self.lock.acquire()
            if self.completed:
                return False
            self.completed = True
            self.result = result
            self.lock.notifyAll()
        finally:
            self.lock.release()
        return True

    def get(self, timeout=3):
        """
        get result
        :param timeout: unit seconds
        :return:
        """
        try:
            self.lock.acquire()
            seconds = timeout
            wait_time = seconds
            if self.completed:
                return self.result
            elif wait_time <= 0:
                raise TimeoutError()
            else:
                while True:
                    self.lock.wait(wait_time)
                    if self.completed:
                        return self.result
                    else:
                        wait_time = seconds - (int(round(time.time())) - self.start / 1000)
                        if wait_time <= 0:
                            raise TimeoutError("timeout cost " + str(int(round(time.time())) - self.start / 1000) + "s")
        finally:
            self.lock.release()
