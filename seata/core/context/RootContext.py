#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from loguru import logger

from seata.core.context.ContextCore import ContextCore
from seata.core.model.BranchType import BranchType
from seata.exception.ShouldNeverHappenException import ShouldNeverHappenException


class RootContext(object):
    KEY_XID = "KEY_XID"
    KEY_BRANCH_TYPE = "TX_BRANCH_TYPE"
    KEY_GLOBAL_LOCK_FLAG = "TX_LOCK"
    VALUE_GLOBAL_LOCK_FLAG = True
    DEFAULT_BRANCH_TYPE = None

    CONTEXT_HOLDER = ContextCore.get_instance()

    @classmethod
    def set_default_branch_type(cls, default_branch_type):
        if default_branch_type != BranchType.AT and default_branch_type != BranchType.XA:
            raise TypeError("The default branch type must be [{}] or [{}]. the value of the argument is: [{}]"
                            .format(BranchType.AT, BranchType.XA, default_branch_type))
        if cls.DEFAULT_BRANCH_TYPE is not None and cls.DEFAULT_BRANCH_TYPE != default_branch_type:
            logger.warning(
                "The `RootContext.DEFAULT_BRANCH_TYPE` has been set repeatedly. The value changes from [{}] to [{}]"
                .format(cls.DEFAULT_BRANCH_TYPE, default_branch_type))
        cls.DEFAULT_BRANCH_TYPE = default_branch_type

    @classmethod
    def get_xid(cls):
        return cls.CONTEXT_HOLDER.get(cls.KEY_XID)

    @classmethod
    def bind(cls, xid=None):
        if xid is None or len(xid) == 0:
            xid = None
        logger.info("bind xid [{}]".format(xid))
        cls.CONTEXT_HOLDER.put(cls.KEY_XID, xid)

    @classmethod
    def bind_global_lock_flag(cls):
        cls.CONTEXT_HOLDER.put(cls.KEY_GLOBAL_LOCK_FLAG, cls.VALUE_GLOBAL_LOCK_FLAG)

    @classmethod
    def unbind(cls):
        xid = cls.CONTEXT_HOLDER.get(cls.KEY_XID)
        logger.info("unbind xid [{}]".format(xid))
        return xid

    @classmethod
    def unbind_global_lock_flag(cls):
        flag = cls.CONTEXT_HOLDER.get(cls.KEY_GLOBAL_LOCK_FLAG)
        logger.info("unbind global lock flag [{}]".format(flag))
        cls.CONTEXT_HOLDER.remove(cls.KEY_GLOBAL_LOCK_FLAG)

    @classmethod
    def in_global_transaction(cls):
        if cls.CONTEXT_HOLDER.get(cls.KEY_XID) is not None:
            return True
        return False

    @classmethod
    def in_tcc_branch(cls):
        return BranchType.TCC == RootContext.get_branch_type()

    @classmethod
    def in_saga_branch(cls):
        return BranchType.SAGA == RootContext.get_branch_type()

    @classmethod
    def get_branch_type(cls):
        if cls.in_global_transaction():
            branch_type = cls.CONTEXT_HOLDER.get(cls.KEY_BRANCH_TYPE)
            if branch_type is not None:
                return branch_type
            if cls.DEFAULT_BRANCH_TYPE is not None:
                return cls.DEFAULT_BRANCH_TYPE
            else:
                return BranchType.AT
        return None

    @classmethod
    def bind_branch_type(cls, branch_type):
        if branch_type is None:
            raise ValueError("branch_type is None")
        cls.CONTEXT_HOLDER.put(cls.KEY_BRANCH_TYPE, branch_type)

    @classmethod
    def unbind_branch_type(cls):
        branch_type = cls.CONTEXT_HOLDER.get(cls.KEY_BRANCH_TYPE)
        logger.info("unbind branch type [{}]".format(branch_type))
        cls.CONTEXT_HOLDER.remove(cls.KEY_BRANCH_TYPE)
        return branch_type

    @classmethod
    def require_global_lock(cls):
        global_lock_flag = cls.CONTEXT_HOLDER.get(cls.KEY_GLOBAL_LOCK_FLAG)
        if global_lock_flag is not None:
            return True
        return False

    @classmethod
    def assert_not_in_global_transaction(cls):
        if cls.in_global_transaction():
            raise ShouldNeverHappenException()
