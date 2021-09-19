#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
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
