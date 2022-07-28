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
