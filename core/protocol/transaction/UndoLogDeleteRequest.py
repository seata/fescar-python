#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.model.BranchType import BranchType
from core.protocol.MessageType import MessageType
from core.protocol.MessageTypeAware import MessageTypeAware


class UndoLogDeleteRequest(MessageTypeAware):

    def __init__(self):
        self.resource_id = None
        self.save_days = 7
        self.branch_type = BranchType.AT

    def get_type_code(self):
        return MessageType.TYPE_RM_DELETE_UNDOLOG
