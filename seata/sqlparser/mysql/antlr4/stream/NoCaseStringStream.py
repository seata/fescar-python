#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from antlr4 import *


class NoCaseStringStream(InputStream):

    def __init__(self, value: str):
        super(NoCaseStringStream, self).__init__(value)

    def LA(self, offset: int):
        la = super(NoCaseStringStream, self).LA(offset)
        if la == 0 or la == -1:
            return la
        else:
            return ord(chr(la).upper())
