#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class MessageTypeAware(object):

    def get_type_code(self):
        raise NotImplemented("need subclass implemented")

class ResultMessage:

    def __init__(self):
        self.result_code = None
        self.msg = None

    pass
