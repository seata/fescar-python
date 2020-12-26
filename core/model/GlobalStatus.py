#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from enum import Enum


class GlobalStatus(Enum):
    """
    Un known global status.
    """
    UnKnown = 0

    """
    The Begin.
    PHASE 1: can accept new branch registering.
    """
    Begin = 1

    """
    PHASE 2: Running Status: may be changed any time.
    """
    Committing = 2

    """
    The Commit retrying.
    Retrying commit after a recoverable failure.
    """
    CommitRetrying = 3

    """
    Rollbacking global status.
    """
    Rollbacking = 4

    """
    The Rollback retrying.
    Retrying rollback after a recoverable failure.
    """
    RollbackRetrying = 5

    """
    The Timeout rollbacking.
    """
    TimeoutRollbacking = 6

    """
    The Timeout rollback retrying.
    Retrying rollback (since timeout) after a recoverable failure.
    """
    TimeoutRollbackRetrying = 7

    """
    All branches can be async committed. The committing is NOT done yet, but it can be seen as committed for TM/RM
    client.
    """
    AsyncCommitting = 8

    """
    PHASE 2: Final Status: will NOT change any more.
    Finally: global transaction is successfully committed.
    """
    Committed = 9

    """
    The Commit failed.
    Finally: failed to commit
    """
    CommitFailed = 10

    """
    The Rollbacked.
    Finally: global transaction is successfully rollbacked.
    """
    Rollbacked = 11

    """
    The Rollback failed.
    Finally: failed to rollback
    """
    RollbackFailed = 12

    """
    The Timeout rollbacked.
    Finally: global transaction is successfully rollbacked since timeout.
    """
    TimeoutRollbacked = 13

    """
    The Timeout rollback failed.
    Finally: failed to rollback since timeout
    """
    TimeoutRollbackFailed = 14

    """
    The Finished.
    Not managed in session MAP any more
    """
    Finished = 15
