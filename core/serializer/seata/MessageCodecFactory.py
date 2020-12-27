#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.protocol.MessageType import MessageType


class MessageCodecFactory(object):

    @staticmethod
    def get_message_codec(type_code):
        msg_codec = None
        if type_code == MessageType.TYPE_SEATA_MERGE:
            pass
        elif type_code == MessageType.TYPE_SEATA_MERGE_RESULT:
            pass
        elif type_code == MessageType.TYPE_REG_CLT:
            pass
        elif type_code == MessageType.TYPE_REG_CLT_RESULT:
            pass
        elif type_code == MessageType.TYPE_REG_RM:
            pass
        elif type_code == MessageType.TYPE_REG_RM_RESULT:
            pass
        elif type_code == MessageType.TYPE_BRANCH_COMMIT:
            pass
        elif type_code == MessageType.TYPE_BRANCH_ROLLBACK:
            pass
        elif type_code == MessageType.TYPE_GLOBAL_REPORT:
            pass

        if msg_codec is not None:
            return msg_codec
        try:
            msg_codec = MessageCodecFactory.get_merge_request_message_seata_codec(type_code)
        except Exception as e:
            pass

        if msg_codec is not None:
            return msg_codec

        msg_codec = MessageCodecFactory.get_merge_response_message_seata_codec(type_code)

        return msg_codec

    @staticmethod
    def get_merge_request_message_seata_codec(type_code):
        if type_code == MessageType.TYPE_GLOBAL_BEGIN:
            pass
        elif type_code == MessageType.TYPE_GLOBAL_COMMIT:
            pass
        elif type_code == MessageType.TYPE_GLOBAL_ROLLBACK:
            pass
        elif type_code == MessageType.TYPE_GLOBAL_STATUS:
            pass
        elif type_code == MessageType.TYPE_GLOBAL_LOCK_QUERY:
            pass
        elif type_code == MessageType.TYPE_BRANCH_REGISTER:
            pass
        elif type_code == MessageType.TYPE_BRANCH_STATUS_REPORT:
            pass
        elif type_code == MessageType.TYPE_GLOBAL_REPORT:
            pass
        return None

    @staticmethod
    def get_merge_response_message_seata_codec(type_code):
        pass