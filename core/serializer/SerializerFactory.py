#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.serializer.seata import SeataSerializer
from exception.NotSupportYetException import NotSupportYetException


class SerializerFactory(object):

    @staticmethod
    def get(codec_type=1):
        if codec_type == 1:
            return SeataSerializer()
        else:
            raise NotSupportYetException('not support serialize type {}'.format(codec_type))
