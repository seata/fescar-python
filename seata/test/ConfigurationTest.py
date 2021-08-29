#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import os

from seata.config.Config import ConfigFactory
from seata.config.Configuration import Configuration

BASEDIR = os.path.dirname(os.path.dirname(__file__))

if __name__ == '__main__':
    Configuration(BASEDIR + '/script/client.yml')
    config = ConfigFactory.get_config()
    print(config)
