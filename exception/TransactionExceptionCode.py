#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from enum import Enum


class TransactionExceptionCode(Enum):
    # Unknown transaction exception code.
    Unknown = 1

    # BeginFailed
    BeginFailed = 2

    # Lock key conflict transaction exception code.
    LockKeyConflict = 3

    # Io transaction exception code.
    IO = 4

    # Branch rollback failed retriable transaction exception code.
    BranchRollbackFailed_Retriable = 5

    # Branch rollback failed unretriable transaction exception code.
    BranchRollbackFailed_Unretriable = 6

    # Branch register failed transaction exception code.
    BranchRegisterFailed = 7

    # Branch report failed transaction exception code.
    BranchReportFailed = 8

    # Lockable check failed transaction exception code.
    LockableCheckFailed = 9

    # Branch transaction not exist transaction exception code.
    BranchTransactionNotExist = 10

    # Global transaction not exist transaction exception code.
    GlobalTransactionNotExist = 11

    # Global transaction not active transaction exception code.
    GlobalTransactionNotActive = 12

    # Global transaction status invalid transaction exception code.
    GlobalTransactionStatusInvalid = 13

    # Failed to send branch commit request transaction exception code.
    FailedToSendBranchCommitRequest = 14

    # Failed to send branch rollback request transaction exception code.
    FailedToSendBranchRollbackRequest = 15

    # Failed to add branch transaction exception code.
    FailedToAddBranch = 16

    # Failed to lock global transaction exception code.
    FailedLockGlobalTranscation = 17

    # FailedWriteSession
    FailedWriteSession = 18

    # Failed to store exception code
    FailedStore = 19
