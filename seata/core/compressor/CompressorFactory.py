#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
from seata.exception.NotSupportYetException import NotSupportYetException


class CompressorFactory(object):

    @staticmethod
    def get(compressor_type=0):
        if compressor_type == 0:
            from seata.core.compressor.DefaultCompressor import DefaultCompressor
            return DefaultCompressor()
        else:
            raise NotSupportYetException('not support compress type {}'.format(compressor_type))
