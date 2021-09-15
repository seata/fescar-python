#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import os

from loguru import logger


class LogConfiguration:

    def __init__(self):
        home = os.path.expanduser('~')
        log_file_path = os.path.join(home, 'logs/seata/info.log')
        err_log_file_path = os.path.join(home, 'logs/seata/error.log')
        logger.add(log_file_path, rotation="500 MB", encoding='utf-8',
                   format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}", filter="", level="INFO", enqueue=True)
        logger.add(err_log_file_path, rotation="500 MB", encoding='utf-8',
                   format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}", filter="", level="ERROR", enqueue=True)
        logger.info("init logger...")
