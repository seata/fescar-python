#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

from seata.rm.RMClient import RMClient
from seata.tm.TMClient import TMClient
from seata.tm.api.GlobalTransaction import DefaultGlobalTransaction, GlobalTransactionRole

if __name__ == '__main__':

    host = "127.0.0.1"
    port = 8091
    rm_client = RMClient.get()
    rm_client.set_application_id("test")
    rm_client.set_transaction_service_group("my_test_tx_group")
    rm_client.init_client(host, port)

    tm_client = TMClient.get()
    tm_client.application_id = "xxx"
    tm_client.transaction_service_group = "my_test_tx_group"
    tm_client.init_client(host, port)

    gt = DefaultGlobalTransaction(None, None, GlobalTransactionRole.Launcher)
    gt.begin(60000, "xxx")
    print("xid = {}".format(gt.xid))


