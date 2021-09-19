#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import os

from seata.log.LogConfiguration import LogConfiguration


class Configuration:

    def __init__(self, path):
        LogConfiguration()
        os.environ['config.name'] = path
        # 1. 读取client.yml
        # 2. 从client.yml中读取config节点配置
        # 3. 从client.yml中读取registry节点配置
        pass
