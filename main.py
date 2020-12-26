#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from tm.TMClient import TmClient

if __name__ == '__main__':
    tm_client = TmClient()
    tm_client.init_client(host="192.168.1.9", port=8091)
