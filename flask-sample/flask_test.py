#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
import sys

from flask import Flask, request
from loguru import logger
from seata.boot.GlobalTransactionScanner import GlobalTransactionScanner
from seata.config.Configuration import Configuration
from seata.core.context.RootContext import RootContext

from db import DB
from test_service import TestService

app = Flask(__name__)


@app.before_request
def xid_before():
    xid = RootContext.get_xid()
    rpc_xid = request.headers.get(RootContext.KEY_XID, None)
    logger.debug("xid {} rpc_xid {}".format(xid, rpc_xid))
    if xid is None and rpc_xid is not None:
        logger.debug('bind xid {} to root context'.format(rpc_xid))
        RootContext.bind(rpc_xid)


@app.after_request
def xid_after(response):
    if RootContext.in_global_transaction():
        xid = RootContext.get_xid()
        if xid is not None:
            un_xid = RootContext.unbind()
            rpc_xid = request.headers.get(RootContext.KEY_XID, None)
            if un_xid != rpc_xid:
                logger.warning('rpc_xid not equal unbind xid {} {}'.format(rpc_xid, un_xid))
                if un_xid is not None:
                    logger.warning('bind xid {} back to root context '.format(un_xid))
                    RootContext.bind(un_xid)
    return response


@app.route("/hello")
def hello():
    e = request.args.get('e')
    TestService.save(e)
    return "1"


if __name__ == '__main__':
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    # 1. init config
    Configuration('./client.yml')
    # 2. init remote client
    GlobalTransactionScanner()
    # 3. init datasource
    DB.init()
    app.run(host="0.0.0.0", port=8000)
