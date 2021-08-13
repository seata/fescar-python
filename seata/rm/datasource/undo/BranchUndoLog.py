#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0

class BranchUndoLog:

    def __init__(self):
        self.xid = None
        self.branch_id = 0
        # SQLUndoLog list
        self.sql_undo_logs = None
