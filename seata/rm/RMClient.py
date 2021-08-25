#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import threading

from seata.core.rpc.v1.RmRemotingClient import RmRemotingClient


class RMClient(object):
    client = None
    lock = threading.RLock()

    @classmethod
    def get(cls, application_id=None, transaction_service_group=None):
        if cls.client is None:
            try:
                cls.lock.acquire()
                if cls.client is None:
                    cls.client = RMClient(application_id, transaction_service_group)
            finally:
                cls.lock.release()
        return cls.client

    def __init__(self, application_id=None, transaction_service_group=None):
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        self.remote_client = None
        from seata.rm.DefaultResourceManager import DefaultResourceManager
        self.resource_manager = DefaultResourceManager.get()

    def init_client(self):
        from seata.rm.RMHandlerAT import RMHandlerAT
        message_handler = RMHandlerAT()
        self.remote_client = RmRemotingClient.get_client(self.application_id, self.transaction_service_group,
                                                         message_handler)
