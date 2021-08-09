#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from enum import Enum


class BranchStatus(Enum):
    """
    The Unknown.
    description: Unknown branch status.
    """
    Unknown = 0,

    """
    The Registered.
    description: Registered to TC.
    """
    Registered = 1,

    """
    The Phase one done.
    description: Branch logic is successfully done at phase one.
    """
    PhaseOne_Done = 2,

    """
    The Phase one failed.
    description: Branch logic is failed at phase one.
    """
    PhaseOne_Failed = 3,

    """
    The Phase one timeout.
    description: Branch logic is NOT reported for a timeout.
    """
    PhaseOne_Timeout = 4,

    """
    The Phase two committed.
    description: Commit logic is successfully done at phase two.
    """
    PhaseTwo_Committed = 5,

    """
    The Phase two commit failed retryable.
    description: Commit logic is failed but retryable.
    """
    PhaseTwo_CommitFailed_Retryable = 6,

    """
    The Phase two commit failed unretryable.
    description: Commit logic is failed and NOT retryable.
    """
    PhaseTwo_CommitFailed_Unretryable = 7,

    """
    The Phase two rollbacked.
    description: Rollback logic is successfully done at phase two.
    """
    PhaseTwo_Rollbacked = 8,

    """
    The Phase two rollback failed retryable.
    description: Rollback logic is failed but retryable.
    """
    PhaseTwo_RollbackFailed_Retryable = 9,

    """
    The Phase two rollback failed unretryable.
    description: Rollback logic is failed but NOT retryable.
    """
    PhaseTwo_RollbackFailed_Unretryable = 10