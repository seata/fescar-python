#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from loguru import logger

from seata.core.ByteBuffer import ByteBuffer
from seata.core.compressor.CompressorFactory import CompressorFactory
from seata.core.protocol.HeartbeatMessage import HeartbeatMessage
from seata.core.protocol.ProtocolConstants import ProtocolConstants
from seata.core.protocol.RpcMessage import RpcMessage
from seata.core.rpc.v1.HeadMapSerializer import HeadMapSerializer
from seata.core.serializer.SerializerFactory import SerializerFactory

"""
0     1     2     3     4     5     6     7     8     9    10     11    12    13    14    15    16
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
|   magic   |Proto|     Full length       |    Head   | Msg |Seria|Compr|     RequestId         |
|   code    |colVer|    (head+body)       |   Length  |Type |lizer|ess  |                       |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|                                                                                               |
|                                   Head Map [Optional]                                         |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
|                                                                                               |
|                                         body                                                  |
|                                                                                               |
|                                        ... ...                                                |
+-----------------------------------------------------------------------------------------------+
"""


class ProtocolV1:
    def decode(self, bb):
        magic = bytearray(len(ProtocolConstants.MAGIC_CODE_BYTES))
        bb.get(magic)
        if magic != ProtocolConstants.MAGIC_CODE_BYTES:
            logger.error("magic not 0xdada", magic)
            return
        # get version
        bb.get_int8()
        full_length = bb.get_int32()
        head_length = bb.get_int16()
        message_type = bb.get_int8()
        codec_type = bb.get_int8()
        compressor_type = bb.get_int8()
        request_id = bb.get_int32()

        rpc_message = RpcMessage()
        rpc_message.codec = codec_type
        rpc_message.id = request_id
        rpc_message.compressor = compressor_type
        rpc_message.message_type = message_type

        head_map_length = head_length - ProtocolConstants.V1_HEAD_LENGTH
        if head_map_length > 0:
            if bb.readable_bytes() > 0:
                head_bytearray = bytearray(head_map_length)
                bb.get(head_bytearray)
                head_bytebuffer = ByteBuffer.wrap(head_bytearray)

                head_map_serializer = HeadMapSerializer()
                head_map = head_map_serializer.decode(head_bytebuffer, head_map_length)
                rpc_message.head_map.update(head_map)
        if message_type == ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST:
            rpc_message.body = HeartbeatMessage(True)
        elif message_type == ProtocolConstants.MSGTYPE_HEARTBEAT_RESPONSE:
            rpc_message.body = HeartbeatMessage(False)
        else:
            body_length = full_length - head_length
            if body_length > 0:
                body_bytearray = bytearray(body_length)
                bb.get(body_bytearray)
                body_bytearray = CompressorFactory.get(compressor_type).decompress(body_bytearray)
                body = SerializerFactory.get(codec_type).deserialize(body_bytearray)
                rpc_message.body = body
        return rpc_message

    def encode(self, rpc_message):
        full_length = 16
        head_length = 16
        bb = ByteBuffer()

        message_type = rpc_message.message_type

        if len(rpc_message.head_map) > 0:
            head_map_serializer = HeadMapSerializer()
            head_map_length = head_map_serializer.encode(rpc_message.head_map, bb)
            head_length = head_length + head_map_length
            full_length = full_length + head_map_length

        body_array = None
        if message_type is not ProtocolConstants.MSGTYPE_HEARTBEAT_REQUEST and \
                message_type is not ProtocolConstants.MSGTYPE_HEARTBEAT_RESPONSE:
            body_array = SerializerFactory.get(rpc_message.codec).serialize(rpc_message.body)
            body_array = CompressorFactory.get(rpc_message.compressor).compress(body_array)
            full_length += len(body_array)

        if body_array is not None:
            bb.put(body_array)

        result = ByteBuffer()
        # magic
        result.put(ProtocolConstants.MAGIC_CODE_BYTES)
        # version
        result.put_int8(ProtocolConstants.VERSION)
        result.put_int32(full_length)
        result.put_int16(head_length)
        result.put_int8(rpc_message.message_type)
        result.put_int8(rpc_message.codec)
        result.put_int8(rpc_message.compressor)
        result.put_int32(rpc_message.id)
        result.put(bb.array())
        return bytes(result.array())
