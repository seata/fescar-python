#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import yaml

from seata.config.Config import Config


class FileConfig(Config):

    def __init__(self, path):
        yml_data = None
        with open(path, 'r') as stream:
            try:
                yml_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
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
