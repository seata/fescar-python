#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from seata.core.protocol.MergeResultMessage import MergeResultMessage
from seata.core.protocol.MergeResultMessageCodec import MergeResultMessageCodec
from seata.core.protocol.MergedWarpMessage import MergedWarpMessage
from seata.core.protocol.MergedWarpMessageCodec import MergedWarpMessageCodec
from seata.core.protocol.MessageType import MessageType
from seata.core.protocol.RegisterRMRequestResponse import RegisterRMRequest, RegisterRMResponse
from seata.core.protocol.RegisterRMRequestResponseCodec import RegisterRMRequestCodec, RegisterRMResponseCodec
from seata.core.protocol.RegisterTMRequestResponse import RegisterTMResponse, RegisterTMRequest
from seata.core.protocol.RegisterTMRequestResponseCodec import RegisterTMRequestCodec, RegisterTMResponseCodec
from seata.core.protocol.transaction.BranchCommitRequestResponse import BranchCommitResponse, BranchCommitRequest
from seata.core.protocol.transaction.BranchCommitRequestResponseCodec import BranchCommitResponseCodec, \
    BranchCommitRequestCodec
from seata.core.protocol.transaction.BranchRegisterRequestResponseCodec import BranchRegisterRequestCodec, \
    BranchRegisterResponseCodec
from seata.core.protocol.transaction.BranchRegisterRequestResponse import BranchRegisterResponse, BranchRegisterRequest
from seata.core.protocol.transaction.BranchReportRequestResponseCodec import BranchReportRequestCodec, \
    BranchReportResponseCodec
from seata.core.protocol.transaction.BranchReportRequestResponse import BranchReportResponse, BranchReportRequest
from seata.core.protocol.transaction.BranchRollbackRequestResponse import BranchRollbackResponse, BranchRollbackRequest
from seata.core.protocol.transaction.BranchRollbackRequestResponseCodec import BranchRollbackResponseCodec, \
    BranchRollbackRequestCodec
from seata.core.protocol.transaction.GlobalBeginRequestResponseCodec import GlobalBeginRequestCodec, \
    GlobalBeginResponseCodec
from seata.core.protocol.transaction.GlobalBeginRequestResponse import GlobalBeginResponse, GlobalBeginRequest
from seata.core.protocol.transaction.GlobalCommitRequestResponseCodec import GlobalCommitRequestCodec, \
    GlobalCommitResponseCodec
from seata.core.protocol.transaction.GlobalCommitRequestResponse import GlobalCommitResponse, GlobalCommitRequest
from seata.core.protocol.transaction.GlobalLockQueryRequestResponseCodec import GlobalLockQueryRequestCodec, \
    GlobalLockQueryResponseCodec
from seata.core.protocol.transaction.GlobalLockQueryRequestResponse import GlobalLockQueryResponse, \
    GlobalLockQueryRequest
from seata.core.protocol.transaction.GlobalReportRequestResponseCodec import GlobalReportRequestCodec, \
    GlobalReportResponseCodec
from seata.core.protocol.transaction.GlobalReportRequestResponse import GlobalReportResponse, GlobalReportRequest
from seata.core.protocol.transaction.GlobalRollbackRequestResponseCodec import GlobalRollbackRequestCodec, \
    GlobalRollbackResponseCodec
from seata.core.protocol.transaction.GlobalRollbackRequestResponse import GlobalRollbackResponse, GlobalRollbackRequest
from seata.core.protocol.transaction.GlobalStatusRequestResponseCodec import GlobalStatusRequestCodec, \
    GlobalStatusResponseCodec
from seata.core.protocol.transaction.GlobalStatusRequestResponse import GlobalStatusResponse, GlobalStatusRequest
from seata.core.protocol.transaction.UndoLogDeleteRequest import UndoLogDeleteRequest
from seata.core.protocol.transaction.UndoLogDeleteRequestCodec import UndoLogDeleteRequestCodec


class MessageCodecFactory(object):

    @staticmethod
    def get_message_codec(type_code):
        msg_codec = None
        if type_code == MessageType.TYPE_SEATA_MERGE:
            msg_codec = MergedWarpMessageCodec()
        elif type_code == MessageType.TYPE_SEATA_MERGE_RESULT:
            msg_codec = MergeResultMessageCodec()
        elif type_code == MessageType.TYPE_REG_CLT:
            msg_codec = RegisterTMRequestCodec()
        elif type_code == MessageType.TYPE_REG_CLT_RESULT:
            msg_codec = RegisterTMResponseCodec()
        elif type_code == MessageType.TYPE_REG_RM:
            msg_codec = RegisterRMRequestCodec()
        elif type_code == MessageType.TYPE_REG_RM_RESULT:
            msg_codec = RegisterRMResponseCodec()
        elif type_code == MessageType.TYPE_BRANCH_COMMIT:
            msg_codec = BranchCommitRequestCodec()
        elif type_code == MessageType.TYPE_BRANCH_ROLLBACK:
            msg_codec = BranchRollbackRequestCodec()
        elif type_code == MessageType.TYPE_GLOBAL_REPORT:
            msg_codec = GlobalReportRequestCodec()

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
            return GlobalBeginRequestCodec()
        elif type_code == MessageType.TYPE_GLOBAL_COMMIT:
            return GlobalCommitRequestCodec()
        elif type_code == MessageType.TYPE_GLOBAL_ROLLBACK:
            return GlobalRollbackRequestCodec()
        elif type_code == MessageType.TYPE_GLOBAL_STATUS:
            return GlobalStatusRequestCodec()
        elif type_code == MessageType.TYPE_GLOBAL_LOCK_QUERY:
            return GlobalLockQueryRequestCodec()
        elif type_code == MessageType.TYPE_BRANCH_REGISTER:
            return BranchRegisterRequestCodec()
        elif type_code == MessageType.TYPE_BRANCH_STATUS_REPORT:
            return BranchReportRequestCodec()
        elif type_code == MessageType.TYPE_GLOBAL_REPORT:
            return GlobalReportRequestCodec()
        else:
            raise ValueError("not support typeCode {}".format(type_code))

    @staticmethod
    def get_merge_response_message_seata_codec(type_code):
        if type_code == MessageType.TYPE_GLOBAL_BEGIN_RESULT:
            return GlobalBeginResponseCodec()
        elif type_code == MessageType.TYPE_GLOBAL_COMMIT_RESULT:
            return GlobalCommitResponseCodec()
        elif type_code == MessageType.TYPE_GLOBAL_ROLLBACK_RESULT:
            return GlobalRollbackResponseCodec()
        elif type_code == MessageType.TYPE_GLOBAL_STATUS_RESULT:
            return GlobalStatusResponseCodec()
        elif type_code == MessageType.TYPE_GLOBAL_LOCK_QUERY_RESULT:
            return GlobalLockQueryResponseCodec()
        elif type_code == MessageType.TYPE_BRANCH_REGISTER_RESULT:
            return BranchRegisterResponseCodec()
        elif type_code == MessageType.TYPE_BRANCH_STATUS_REPORT_RESULT:
            return BranchReportResponseCodec()
        elif type_code == MessageType.TYPE_BRANCH_COMMIT_RESULT:
            return BranchCommitResponseCodec()
        elif type_code == MessageType.TYPE_BRANCH_ROLLBACK_RESULT:
            return BranchRollbackResponseCodec()
        elif type_code == MessageType.TYPE_RM_DELETE_UNDOLOG:
            return UndoLogDeleteRequestCodec()
        elif type_code == MessageType.TYPE_GLOBAL_REPORT_RESULT:
            return GlobalReportResponseCodec()
        else:
            raise ValueError("not support typeCode {}".format(type_code))

    @staticmethod
    def get_message(type_code):
        message = None
        if type_code == MessageType.TYPE_SEATA_MERGE:
            message = MergedWarpMessage()
        elif type_code == MessageType.TYPE_SEATA_MERGE_RESULT:
            message = MergeResultMessage()
        elif type_code == MessageType.TYPE_REG_CLT:
            message = RegisterTMRequest()
        elif type_code == MessageType.TYPE_REG_CLT_RESULT:
            message = RegisterTMResponse()
        elif type_code == MessageType.TYPE_REG_RM:
            message = RegisterRMRequest()
        elif type_code == MessageType.TYPE_REG_RM_RESULT:
            message = RegisterRMResponse()
        elif type_code == MessageType.TYPE_BRANCH_COMMIT:
            message = BranchCommitRequest()
        elif type_code == MessageType.TYPE_BRANCH_ROLLBACK:
            message = BranchRollbackRequest()
        elif type_code == MessageType.TYPE_RM_DELETE_UNDOLOG:
            message = UndoLogDeleteRequest()
        elif type_code == MessageType.TYPE_GLOBAL_REPORT:
            message = GlobalReportRequest()
        elif type_code == MessageType.TYPE_GLOBAL_REPORT_RESULT:
            message = GlobalReportResponse()

        if message is not None:
            return message

        try:
            message = MessageCodecFactory.get_merge_request_instance_by_code(type_code)
        except Exception as e:
            pass

        if message is not None:
            return message

        return MessageCodecFactory.get_merge_response_instance_by_code(type_code)

    @staticmethod
    def get_merge_request_instance_by_code(type_code):
        if type_code == MessageType.TYPE_GLOBAL_BEGIN:
            return GlobalBeginRequest()
        elif type_code == MessageType.TYPE_GLOBAL_COMMIT:
            return GlobalCommitRequest()
        elif type_code == MessageType.TYPE_GLOBAL_ROLLBACK:
            return GlobalRollbackRequest()
        elif type_code == MessageType.TYPE_GLOBAL_STATUS:
            return GlobalStatusRequest()
        elif type_code == MessageType.TYPE_GLOBAL_LOCK_QUERY:
            return GlobalLockQueryRequest()
        elif type_code == MessageType.TYPE_BRANCH_REGISTER:
            return BranchRegisterRequest()
        elif type_code == MessageType.TYPE_BRANCH_STATUS_REPORT:
            return BranchReportRequest()
        elif type_code == MessageType.TYPE_GLOBAL_REPORT:
            return GlobalReportRequest()
        else:
            raise ValueError("not support typeCode {}".format(type_code))

    @staticmethod
    def get_merge_response_instance_by_code(type_code):
        if type_code == MessageType.TYPE_GLOBAL_BEGIN_RESULT:
            return GlobalBeginResponse()
        elif type_code == MessageType.TYPE_GLOBAL_COMMIT_RESULT:
            return GlobalCommitResponse()
        elif type_code == MessageType.TYPE_GLOBAL_ROLLBACK_RESULT:
            return GlobalRollbackResponse()
        elif type_code == MessageType.TYPE_GLOBAL_STATUS_RESULT:
            return GlobalStatusResponse()
        elif type_code == MessageType.TYPE_GLOBAL_LOCK_QUERY_RESULT:
            return GlobalLockQueryResponse()
        elif type_code == MessageType.TYPE_BRANCH_REGISTER_RESULT:
            return BranchRegisterResponse()
        elif type_code == MessageType.TYPE_BRANCH_STATUS_REPORT_RESULT:
            return BranchReportResponse()
        elif type_code == MessageType.TYPE_BRANCH_COMMIT_RESULT:
            return BranchCommitResponse()
        elif type_code == MessageType.TYPE_BRANCH_ROLLBACK_RESULT:
            return BranchRollbackResponse()
        elif type_code == MessageType.TYPE_GLOBAL_REPORT_RESULT:
            return GlobalReportResponse()
        else:
            raise ValueError("not support typeCode {}".format(type_code))
