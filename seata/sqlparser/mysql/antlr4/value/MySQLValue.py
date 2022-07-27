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



class DefaultValue:
    def __init__(self, value: str):
        self.value = value


class NotSupportValue:
    def __init__(self, origin_type):
        self.origin_type = origin_type
        self.value = "NOT SUPPORT"


class FunctionNameValue:
    def __init__(self, function_name, args_list):
        self.function_name = function_name
        self.args_list = args_list


class ParameterMarkerValue:
    def __init__(self, name, value: str):
        self.name = name
        self.value = value


class ValueExpr:
    def get_value(self):
        pass


class StringValue(ValueExpr):
    def __init__(self, value: str):
        self.value = value

    def get_value(self):
        return self.value


class BoolValue(ValueExpr):
    def __init__(self, value: str):
        self.value = value

    def get_value(self):
        return self.value


class IntValue(ValueExpr):
    def __init__(self, value: str):
        self.value = value

    def get_value(self):
        return self.value


class DoubleValue(ValueExpr):
    def __init__(self, value: str):
        self.value = value

    def get_value(self):
        return self.value


class NullValue(ValueExpr):
    def __init__(self):
        self.value = None

    def get_value(self):
        return self.value


class OtherValue:
    def __init__(self, value: str):
        self.value = value


class NotPlaceholderValue:
    pass
