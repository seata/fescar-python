# -*- coding: utf-8 -*-

"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

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
