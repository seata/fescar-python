#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import time
from core.protocol.transaction.GlobalBeginRequestResponse import GlobalBeginRequest
from rm.RMClient import RMClient

if __name__ == '__main__':
    client = RMClient(application_id="test", transaction_service_group="my_test_tx_group")
    client.init_client(host="192.168.1.9", port=8091)

    time.sleep(5)
    msg = GlobalBeginRequest()
    msg.transaction_name = "xxx"
    msg.timeout = 60000
    response = RMClient.send_request(msg)
    print(response)
