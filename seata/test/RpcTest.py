#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import time

from seata.Boostrap import Bootstrap
from seata.core.protocol.transaction.GlobalBeginRequestResponse import GlobalBeginRequest
from seata.rm.RMClient import RMClient

if __name__ == '__main__':
    client = RMClient.get()
    client.set_application_id("test")
    client.set_transaction_service_group("my_test_tx_group")
    client.init_client(host="127.0.0.1", port=8091)
    Bootstrap.start()

    time.sleep(2)
    msg = GlobalBeginRequest()
    msg.transaction_name = "xxx"
    msg.timeout = 60000
    rpc_message = client.send_sync_request(msg)
    print(rpc_message.body.xid)

