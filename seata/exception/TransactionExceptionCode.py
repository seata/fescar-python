# -*- coding: utf-8 -*-

"""
 Licensed to the Apache Software Foundation (ASF) under one or more
 contributor license agreements.  See the NOTICE file distributed with
 this work for additional information regarding copyright ownership.
 The ASF licenses this file to You under the Apache License, Version 2.0
 (the "License"); you may not use this file except in compliance with
 the License.  You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

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
