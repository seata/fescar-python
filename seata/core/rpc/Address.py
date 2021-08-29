#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


class Address:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def to_string(self):
        return self.host + ":" + str(self.port)
