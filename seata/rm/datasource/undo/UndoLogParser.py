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


class UndoLogParser:
    def get_name(self):
        raise NotImplemented("need subclass implemented")

    def get_default_content(self):
        raise NotImplemented("need subclass implemented")

    def encode(self, branch_undo_log):
        raise NotImplemented("need subclass implemented")

    def decode(self, bytes_):
        raise NotImplemented("need subclass implemented")
