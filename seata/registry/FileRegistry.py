#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.config.Config import ConfigFactory
from seata.core.rpc.Address import Address
from seata.registry.Registry import Registry


class FileRegistry(Registry):
    config = ConfigFactory.get_config()

    def __init__(self):
        pass

    def register(self, address):
        pass

    def unregister(self, address):
        pass

    def subscribe(self, cluster, listener):
        pass

    def unsubscribe(self, cluster, listener):
        pass

    def lookup(self, key):
        cluster_name = super(FileRegistry, self).get_service_group(key)
        if cluster_name is None:
            return None
        endpoint_str = self.config.get('service.grouplist.' + cluster_name)
        endpoints = endpoint_str.split(';')
        addresses = []
        for endpoint in endpoints:
            if endpoint is None or len(endpoint.strip()) == 0:
                continue
            ip_port_arr = endpoint.split(':')
            if len(ip_port_arr) != 2:
                raise ValueError('endpoint format should like ip:port')
            addresses.append(Address(ip_port_arr[0], int(ip_port_arr[1])))
        return addresses

    def close(self):
        pass
