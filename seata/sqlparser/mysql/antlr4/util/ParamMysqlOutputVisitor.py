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

from am.mysql_base import MysqlOutputVisitor


class ParamMysqlOutputVisitor(MysqlOutputVisitor):

    def __init__(self, parameters_map, param_list):
        self.parameters_map = parameters_map
        self.param_list = param_list

    def visitParameterMarker(self, parameter_marker, output):
        param_values = self.parameters_map[parameter_marker.index]
        if self.param_list is None or len(self.param_list) == 0:
            for i in range(len(param_values)):
                self.param_list.append([])
        for i in range(len(param_values)):
            val = param_values[i]
            self.param_list[i].append(val)
        output.append("%s")
