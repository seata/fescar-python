#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import time
from core.protocol.transaction.GlobalBeginRequestResponse import GlobalBeginRequest
from rm.RMClient import RMClient

if __name__ == '__main__':
    client = RMClient.get()
    client.set_application_id("test")
    client.set_transaction_service_group("my_test_tx_group")
    client.init_client(host="192.168.1.9", port=8091)

    time.sleep(2)
    msg = GlobalBeginRequest()
    msg.transaction_name = "xxx"
    msg.timeout = 60000
    rpc_message = client.send_sync_request(msg)
    print(rpc_message.body)

