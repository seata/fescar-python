#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import os

from seata.boot.GlobalTransactionScanner import GlobalTransactionScanner
from seata.config.Configuration import Configuration
from seata.tm.api.DefaultGlobalTransaction import DefaultGlobalTransaction
from seata.tm.api.GlobalTransactionRole import GlobalTransactionRole

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(__file__))
    Configuration(base_dir + '/script/client.yml')
    GlobalTransactionScanner()

    gt = DefaultGlobalTransaction(None, None, GlobalTransactionRole.Launcher)
    gt.begin(60000, "xxx")
    print("xid = [{}]".format(gt.xid))
