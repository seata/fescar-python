#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.model.GlobalStatus import GlobalStatus

if __name__ == '__main__':
    val = GlobalStatus.UnKnown.value
    print(val)
    e = GlobalStatus(val)
    print(e)
