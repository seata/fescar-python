#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


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
