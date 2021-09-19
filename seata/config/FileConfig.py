#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import yaml
from loguru import logger

from seata.config.Config import Config


class FileConfig(Config):

    def __init__(self, path):
        yml_data = None
        with open(path, 'r') as stream:
            try:
                yml_data = yaml.safe_load(stream)
            except yaml.YAMLError as ex:
                logger.error('path : [' + path + '] parse error', ex)
                raise ValueError('path : [' + path + '] parse error')
        self.data = yml_data

    def get(self, data_id):
        ds = data_id.split(".")
        value = None
        for idx, d in enumerate(ds):
            if idx == 0:
                value = self.data.get(d, None)
            else:
                value = value.get(d, None)
            if value is None:
                return value
        return value

    def get_bool(self, data_id):
        val = self.get(data_id)
        if val is None:
            return val
        if not isinstance(val, bool):
            return bool(val)
        return val

    def get_int(self, data_id):
        val = self.get(data_id)
        if val is None:
            return val
        if not isinstance(val, int):
            return int(val)
        return val

    def get_float(self, data_id):
        val = self.get(data_id)
        if val is None:
            return val
        if not isinstance(val, float):
            return float(val)
        return val
