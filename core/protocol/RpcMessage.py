#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0


atom = 0


class RpcMessage(object):
    # int
    id = 0
    # byte
    message_type = 0
    # byte
    codec = 0
    # byte
    compressor = 0
    # map string, string
    head_map = dict()
    # Object
    body = None

    @staticmethod
    def get_id():
        global atom
        atom = (atom + 1) & 0x7FFFFFFF
        return atom

