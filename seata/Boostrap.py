#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import threading

from twisted.internet import reactor


class Bootstrap(object):

    @staticmethod
    def start():
        if not reactor.running:
            threading.Thread(target=reactor.run, args=(False,)).start()
