#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import queue
import threading
import time

from loguru import logger

from seata.rm.datasource.undo.UndoLogManagerFactory import UndoLogManagerFactory


class AsyncWorker:
    ASYNC_COMMIT_BUFFER_LIMIT = 10000

    def __init__(self, data_source_manager):
        self.data_source_manager = data_source_manager
        self.commit_queue = queue.Queue(self.ASYNC_COMMIT_BUFFER_LIMIT)
        threading.Thread(target=self.do_branch_commit_safely, args=()).start()

    def add_context(self, context):
        self.commit_queue.put_nowait(context)

    def do_branch_commit_safely(self):
        while True:
            try:
                i = 0
                items = []
                while not self.commit_queue.empty():
                    items.append(self.commit_queue.get_nowait())
                    i += 1
                    if i >= 1000:
                        break

                if len(items) > 0:
                    grouped_contexts = {}
                    for context in items:
                        if grouped_contexts.get(context.resource_id, None) is None:
                            grouped_contexts[context.resource_id] = []
                        grouped_contexts[context.resource_id].append(context)

                    for resource_id, contexts in grouped_contexts.items():
                        self.deal_with_grouped_contexts(resource_id, contexts)

                time.sleep(1)
            except Exception:
                pass

    def deal_with_grouped_contexts(self, resource_id, contexts):
        data_source_proxy = self.data_source_manager.get_resource(resource_id)
        if data_source_proxy is None:
            logger.error('failed to find resource for [{}]'.format(resource_id))
            return

        cp = None
        try:
            cp = data_source_proxy.connection()
        except Exception as e:
            logger.error('failed to get connection for async committing on [{}] [{}]'.format(resource_id, e))
            return
        undo_log_manager = UndoLogManagerFactory.get_undo_log_manager(data_source_proxy.db_type)
        self.delete_undo_log(cp.target_connection, undo_log_manager, contexts)

    def delete_undo_log(self, connection, undo_log_manager, contexts):
        xids = set()
        branch_ids = set()
        for context in contexts:
            xids.add(context.xid)
            branch_ids.add(context.branch_id)

        try:
            undo_log_manager.batch_delete_undo_log(xids, branch_ids, connection)
            connection.commit()
        except Exception as e:
            logger.error('failed to batch delete undo log', e)
            try:
                connection.rollback()
            except Exception as e:
                logger.error('failed to rollback resource after deleting undo log failed', e)
        finally:
            try:
                connection.close()
            except Exception:
                pass


class Phase2Context:

    def __init__(self, xid, branch_id, resource_id):
        self.xid = xid
        self.branch_id = branch_id
        self.resource_id = resource_id
