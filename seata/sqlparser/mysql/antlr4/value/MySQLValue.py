#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


class DefaultValue:
    def __init__(self, value: str):
        self.value = value


class InsertNotSupportValue:
    def __init__(self):
        self.value = "NOT SUPPORT"


class FunctionNameValue:
    def __init__(self, function_name, args_):
        self.function_name = function_name
        self.args_ = args_


class ParameterMarkerValue:
    def __init__(self, value: str):
        self.value = value


class ValueExpr:
    def get_value(self):
        pass


class StringValue(ValueExpr):
    def __init__(self, value: str):
        self.value = value

    def get_value(self):
        return self.value


class NullValue:
    def __init__(self):
        self.value = None


class BoolValue(ValueExpr):
    def __init__(self, value: str):
        self.value = bool(value)

    def get_value(self):
        return self.value


class NumberValue(ValueExpr):
    def __init__(self, value: str):
        try:
            self.value = int(value)
        except Exception as e:
            self.value - float(value)

    def get_value(self):
        return self.value


class OtherValue:
    def __init__(self, value: str):
        self.value = value


class NotPlaceholderValue:
    pass
