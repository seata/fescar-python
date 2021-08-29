#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import os


class Configuration:

    def __init__(self, path):
        os.environ['config.name'] = path
        # 1. 读取client.yml
        # 2. 从client.yml中读取config节点配置
        # 3. 从client.yml中读取registry节点配置

        # 获取可用tc列表
        # 1. 获取service.vgroup-mapping.${tx-service-group}对应的value
        # 2. 获取service.${value}.grouplist对应tc节点ip:port信息
        pass
