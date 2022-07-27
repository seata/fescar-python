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

import threading

from seata.exception.NotSupportYetException import NotSupportYetException

registry_type_file = "file"
registry_type_nacos = "nacos"


class RegistryFactory:
    registry = None
    lock = threading.RLock()

    @classmethod
    def get_registry(cls):
        if cls.registry is None:
            cls.lock.acquire()
            try:
                if cls.registry is None:
                    cls.registry = cls.__build_registry()
            finally:
                cls.lock.release()
        return cls.registry

    @classmethod
    def __build_registry(cls):
        from seata.config.Config import ConfigFactory
        registry_type = ConfigFactory.get_config().get('registry.type')
        if registry_type == registry_type_file:
            from seata.registry.FileRegistry import FileRegistry
            return FileRegistry()
        elif registry_type == registry_type_nacos:
            from seata.registry.NacosRegistry import NacosRegistry
            return NacosRegistry()
        else:
            raise NotSupportYetException("not support registry type : [{}]".format(registry_type))


class Registry:

    def register(self, address):
        raise NotImplemented("need subclass implemented")

    def unregister(self, address):
        raise NotImplemented("need subclass implemented")

    def subscribe(self, cluster, listener):
        raise NotImplemented("need subclass implemented")

    def unsubscribe(self, cluster, listener):
        raise NotImplemented("need subclass implemented")

    def lookup(self, key):
        raise NotImplemented("need subclass implemented")

    def close(self):
        raise NotImplemented("need subclass implemented")

    def get_service_group(self, tx_service_group):
        from seata.config.Config import ConfigFactory
        # TODO cache
        return ConfigFactory.get_config().get('service.vgroupMapping.' + tx_service_group)
