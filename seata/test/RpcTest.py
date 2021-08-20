#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.boot.GlobalTransactionScanner import GlobalTransactionScanner
from seata.tm.api.DefaultGlobalTransaction import DefaultGlobalTransaction
from seata.tm.api.GlobalTransactionRole import GlobalTransactionRole

if __name__ == '__main__':

    GlobalTransactionScanner("test", "my_test_tx_group")

    gt = DefaultGlobalTransaction(None, None, GlobalTransactionRole.Launcher)
    gt.begin(60000, "xxx")
    print("xid = [{}]".format(gt.xid))


