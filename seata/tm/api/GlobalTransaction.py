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
