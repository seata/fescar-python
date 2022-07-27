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

import os
import threading

from seata.exception.NotSupportYetException import NotSupportYetException

config_type_file = "file"
config_type_nacos = "nacos"
config_name_key = 'config.name'


class ConfigFactory:
    lock = threading.RLock()
    config = None
    current_config = None
    path = None

    @classmethod
    def get_config(cls):
        if cls.config is None:
            cls.lock.acquire()
            try:
                if cls.config is None:
                    cls.__load()
                    cls.config = cls.__build_config()
            finally:
                cls.lock.release()
        return cls.config

    @classmethod
    def __load(cls):
        cls.path = os.getenv(config_name_key)
        from seata.config.FileConfig import FileConfig
        cls.current_config = FileConfig(cls.path)

    @classmethod
    def __build_config(cls):
        config_type = cls.current_config.get('config.type')
        if config_type == config_type_file:
            from seata.config.FileConfig import FileConfig
            return FileConfig(cls.path)
        elif config_type == config_type_nacos:
            from seata.config.NacosConfig import NacosConfig
            return NacosConfig()
        else:
            raise NotSupportYetException("not support config type : [{}]".format(config_type))


class Config:

    def get(self, data_id):
        raise NotImplemented("need subclass implemented")

    def get_bool(self, data_id):
        raise NotImplemented("need subclass implemented")

    def get_int(self, data_id):
        raise NotImplemented("need subclass implemented")

    def get_float(self, data_id):
        raise NotImplemented("need subclass implemented")
