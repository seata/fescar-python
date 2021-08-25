#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import os
from seata.boot.GlobalTransactionScanner import GlobalTransactionScanner
from seata.config.Config import ConfigFactory
from seata.config.Configuration import Configuration
from seata.tm.api.DefaultGlobalTransaction import DefaultGlobalTransaction
from seata.tm.api.GlobalTransactionRole import GlobalTransactionRole

if __name__ == '__main__':
    BASEDIR = os.path.dirname(os.path.dirname(__file__))
    Configuration(BASEDIR + '/script/client.yml')
    config = ConfigFactory.get_config()
    application_id = config.get('application-id')
    tx_service_group = config.get('tx-service-group')
    GlobalTransactionScanner(application_id, tx_service_group)

    gt = DefaultGlobalTransaction(None, None, GlobalTransactionRole.Launcher)
    gt.begin(60000, "xxx")
    print("xid = [{}]".format(gt.xid))
