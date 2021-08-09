#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from enum import Enum


class TransactionExceptionCode(Enum):
    # Unknown transaction exception code.
    Unknown = 0

    # BeginFailed
    BeginFailed = 1

    # Lock key conflict transaction exception code.
    LockKeyConflict = 2

    # Io transaction exception code.
    IO = 3

    # Branch rollback failed retriable transaction exception code.
    BranchRollbackFailed_Retriable = 4

    # Branch rollback failed unretriable transaction exception code.
    BranchRollbackFailed_Unretriable = 5

    # Branch register failed transaction exception code.
    BranchRegisterFailed = 6

    # Branch report failed transaction exception code.
    BranchReportFailed = 7

    # Lockable check failed transaction exception code.
    LockableCheckFailed = 8

    # Branch transaction not exist transaction exception code.
    BranchTransactionNotExist = 9

    # Global transaction not exist transaction exception code.
    GlobalTransactionNotExist = 10

    # Global transaction not active transaction exception code.
    GlobalTransactionNotActive = 11

    # Global transaction status invalid transaction exception code.
    GlobalTransactionStatusInvalid = 12

    # Failed to send branch commit request transaction exception code.
    FailedToSendBranchCommitRequest = 13

    # Failed to send branch rollback request transaction exception code.
    FailedToSendBranchRollbackRequest = 14

    # Failed to add branch transaction exception code.
    FailedToAddBranch = 15

    # Failed to lock global transaction exception code.
    FailedLockGlobalTranscation = 16

    # FailedWriteSession
    FailedWriteSession = 17

    # Failed to store exception code
    FailedStore = 18
