#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
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

    @staticmethod
    def set_default_branch_type(default_branch_type):
        if default_branch_type != BranchType.AT and default_branch_type != BranchType.XA:
            raise TypeError("The default branch type must be {} or {}. the value of the argument is: {}"
                            .format(BranchType.AT, BranchType.XA, default_branch_type))
        if RootContext.DEFAULT_BRANCH_TYPE is not None and RootContext.DEFAULT_BRANCH_TYPE != default_branch_type:
            print("The `RootContext.DEFAULT_BRANCH_TYPE` has been set repeatedly. The value changes from {} to {}"
                  .format(RootContext.DEFAULT_BRANCH_TYPE, default_branch_type))
        RootContext.DEFAULT_BRANCH_TYPE = default_branch_type

    @staticmethod
    def get_xid():
        return RootContext.CONTEXT_HOLDER.get(RootContext.KEY_XID)

    @staticmethod
    def bind(xid=None):
        if xid is None or len(xid) == 0:
            xid = None
        print("bind xid [{}]".format(xid))
        RootContext.CONTEXT_HOLDER.put(RootContext.KEY_XID, xid)

    @staticmethod
    def bind_global_lock_flag():
        RootContext.CONTEXT_HOLDER.put(RootContext.KEY_GLOBAL_LOCK_FLAG, RootContext.VALUE_GLOBAL_LOCK_FLAG)

    @staticmethod
    def unbind():
        xid = RootContext.CONTEXT_HOLDER.get(RootContext.KEY_XID)
        print("unbind xid [{}]".format(xid))
        return xid

    @staticmethod
    def unbind_global_lock_flag():
        flag = RootContext.CONTEXT_HOLDER.get(RootContext.KEY_GLOBAL_LOCK_FLAG)
        print("unbind global lock flag [{}]".format(flag))
        RootContext.CONTEXT_HOLDER.remove(RootContext.KEY_GLOBAL_LOCK_FLAG)

    @staticmethod
    def in_global_transaction():
        if RootContext.CONTEXT_HOLDER.get(RootContext.KEY_XID) is not None:
            return True
        return False

    @staticmethod
    def in_tcc_branch():
        return BranchType.TCC == RootContext.get_branch_type()

    @staticmethod
    def in_saga_branch():
        return BranchType.SAGA == RootContext.get_branch_type()

    @staticmethod
    def get_branch_type():
        if RootContext.in_global_transaction():
            branch_type = RootContext.CONTEXT_HOLDER.get(RootContext.KEY_BRANCH_TYPE)
            if branch_type is not None:
                return branch_type
            if RootContext.DEFAULT_BRANCH_TYPE is not None:
                return RootContext.DEFAULT_BRANCH_TYPE
            else:
                return BranchType.AT
        return None

    @staticmethod
    def bind_branch_type(branch_type):
        if branch_type is None:
            raise ValueError("branch_type is None")
        RootContext.CONTEXT_HOLDER.put(RootContext.KEY_BRANCH_TYPE, branch_type)

    @staticmethod
    def unbind_branch_type():
        branch_type = RootContext.CONTEXT_HOLDER.get(RootContext.KEY_BRANCH_TYPE)
        print("unbind branch type {}".format(branch_type))
        RootContext.CONTEXT_HOLDER.remove(RootContext.KEY_BRANCH_TYPE)
        return branch_type

    @staticmethod
    def require_global_lock():
        global_lock_flag = RootContext.CONTEXT_HOLDER.get(RootContext.KEY_GLOBAL_LOCK_FLAG)
        if global_lock_flag is not None:
            return True
        return False

    @staticmethod
    def assert_not_in_global_transaction():
        if RootContext.in_global_transaction():
            raise ShouldNeverHappenException()
