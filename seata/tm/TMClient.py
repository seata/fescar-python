#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import threading
import time

from seata.core.protocol.RegisterTMRequestResponse import RegisterTMRequest
from seata.core.rpc.v1.TmRemotingClient import TmRemotingClient


class TMClient(object):
    client = None
    lock = threading.RLock()

    @classmethod
    def get(cls, application_id=None, transaction_service_group=None):
        if cls.client is None:
            try:
                cls.lock.acquire()
                if cls.client is None:
                    cls.client = TMClient(application_id, transaction_service_group)
            finally:
                cls.lock.release()
        return cls.client

    def __init__(self, application_id=None, transaction_service_group=None):
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        self.remote_client = None

    def init_client(self):
        # 程序启动
        from seata.tm.TMHandler import TMHandler
        message_handler = TMHandler()
        self.remote_client = TmRemotingClient.get_client(self.application_id, self.transaction_service_group,
                                                         message_handler)
