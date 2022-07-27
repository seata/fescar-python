# -*- coding: utf-8 -*-

"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

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
