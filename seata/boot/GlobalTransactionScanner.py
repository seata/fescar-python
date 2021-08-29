#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.rm.RMClient import RMClient
from seata.tm.TMClient import TMClient


class GlobalTransactionScanner:
    _init = False

    def __init__(self, application_id, transaction_service_group):
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        if not self._init:
            self._init = True
            self._init_client()

    def _init_client(self):
        tm = TMClient.get(self.application_id, self.transaction_service_group)
        tm.init_client()

        rm = RMClient.get(self.application_id, self.transaction_service_group)
        rm.init_client()
