#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.model.BranchStatus import BranchStatus
from core.model.BranchType import BranchType
from exception.TransactionException import TransactionException
from exception.TransactionExceptionCode import TransactionExceptionCode
from rm.ATResourceManager import ATResourceManager
from rm.datasource.ConnectionContext import ConnectionContext
from rm.datasource.CursorProxy import CursorProxy
from rm.datasource.PooledDBProxy import PooledDBProxy
from rm.datasource.undo.UndoLogManagerFactory import UndoLogManagerFactory
from rm.datasource.exec.LockConflictException import LockConflictException


class ConnectionProxy(object):

    def __init__(self, pooled_db_proxy, target_connection):
        if not isinstance(pooled_db_proxy, PooledDBProxy):
            raise TypeError("Only support PooledDBProxy")

        self.pooled_db_proxy = pooled_db_proxy
        self.target_connection = target_connection
        self.context = ConnectionContext()

    def get_db_type(self):
        self.target_connection

    def bind(self, xid):
        self.context.bind(xid)
        pass

    def set_global_lock_require(self, is_lock):
        self.context.is_global_lock_require = is_lock

    def is_global_lock_require(self):
        return self.context.is_global_lock_require

    def check_lock(self, lock_keys):
        if lock_keys is None or len(lock_keys) <= 0:
            return
        # Just check lock without requiring lock by now.
        try:
            lockable = ATResourceManager.get().lock_query(BranchType.AT, self.pooled_db_proxy.get_resource_id(),
                                                          self.context.xid, lock_keys)
            if not lockable:
                raise LockConflictException()
        except TransactionException as e:
            self._recognize_lock_key_conflict_exception(e, lock_keys)

    def append_undo_log(self, sql_undo_log):
        self.context.append_undo_item(sql_undo_log)

    def append_lock_key(self, lock_key):
        self.context.append_lock_key(lock_key)

    # override Connection close
    def close(self):
        self.target_connection.close()

    # override Connection commit
    def commit(self):
        try:
            self.do_commit()
            return None
        except RuntimeError as e:
            if self.target_connection is not None and not self.target_connection.autocommit:
                self.rollback()
            raise e
        except Exception as e:
            raise RuntimeError(e)

    # override Connection rollback
    def rollback(self):
        self.target_connection.rollback()
        if self.context.in_global_transaction() and self.context.is_branch_registered():
            self.report(False)
        self.context.reset()

    # override Connection cursor
    def cursor(self):
        cursor = self.target_connection.cursor()
        return CursorProxy(cursor)

    def autocommit(self, on):
        if (self.context.in_global_transaction() or self.context.is_global_lock_require) \
                and on and not self.target_connection.autocommit:
            self.do_commit()
        self.target_connection.autocommit = on

    def do_commit(self):
        if self.context.in_global_transaction():
            self.process_global_transaction_commit()
        elif self.context.is_global_lock_require:
            self.process_local_commit_with_global_locks()
        else:
            self.target_connection.commit()

    def process_global_transaction_commit(self):
        try:
            self.register()
        except TransactionException as e:
            self.recognize_lock_key_conflict_exception(e, self.context.build_lock_keys())

        try:
            if self.context.has_undo_log():
                UndoLogManagerFactory.get_undo_log_manager(self.get_db_type()).flush_undo_log(self)
        except Exception as ex:
            print("process connectionProxy commit error: {}, {}".format(ex.getMessage(), ex))
            self.report(False)
            raise ex

        self.report(True)
        self.context.reset()

    def process_local_commit_with_global_locks(self):
        self.check_lock(self.context.build_lock_keys())
        try:
            self.target_connection.commit()
        except Exception as e:
            raise RuntimeError(e)
        self.context.reset()

    def register(self):
        if not self.context.has_undo_log() or len(self.context.lock_keys_buffer) == 0:
            return
        branch_id = ATResourceManager.get().branch_register(BranchType.AT, self.pooled_db_proxy.get_resource_id(),
                                                            None, self.context.xid, None,
                                                            self.context.build_lock_keys())
        self.context.branch_id = branch_id

    def report(self, commit_done):
        if self.context.branch_id is None:
            return
        retry = 5
        while retry > 0:
            try:
                status = BranchStatus.PhaseOne_Done
                if not commit_done:
                    status = BranchStatus.PhaseOne_Failed
                ATResourceManager.get().branch_report(BranchType.AT, self.context.xid, self.context.branch_id, status,
                                                      None)
            except Exception as e:
                print("Failed to report [{}/{}]  commit done [{}] Retry Countdown: {}".format(self.context.branch_id,
                                                                                              self.context.xid,
                                                                                              commit_done, retry))
                retry -= 1
                if retry == 0:
                    raise RuntimeError("Failed to report branch status  {}".format(commit_done), e)

    def _recognize_lock_key_conflict_exception(self, e, lock_keys):
        if e.value == TransactionExceptionCode.LockKeyConflict:
            reason = "get global lock fail, xid:" + self.context.xid
            if lock_keys is not None and len(lock_keys) > 0:
                reason += ", lock_keys:" + lock_keys
            raise LockConflictException(reason)
        else:
            raise RuntimeError(e)
