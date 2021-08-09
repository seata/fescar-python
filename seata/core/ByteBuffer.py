#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
import struct


class ByteBuffer(object):

    def __init__(self):
        self._array = bytearray(1024)
        self._write_index = 0
        self._read_index = 0

    @staticmethod
    def wrap(array):
        if not isinstance(array, bytearray):
            raise TypeError('Can wrap only to bytearray')
        bb = ByteBuffer()
        bb.put(array)
        return bb

    def put_int8(self, value):
        dst_offset = self._write_index
        self._write_index += 1
        struct.pack_into('!b', self._array, dst_offset, value)

    def get_int8(self):
        if self._read_index > self._write_index - 1:
            raise IndexError('Not enough data to get')
        src_offset = self._read_index
        self._read_index += 1
        return struct.unpack_from('!b', self._array, src_offset)[0]

    def put_int16(self, value):
        dst_offset = self._write_index
        self._write_index += 2
        struct.pack_into('!h', self._array, dst_offset, value)

    def get_int16(self):
        if self._read_index > self._write_index - 2:
            raise IndexError('Not enough data to get')
        src_offset = self._read_index
        self._read_index += 2
        return struct.unpack_from('!h', self._array, src_offset)[0]

    def put_int32(self, value):
        dst_offset = self._write_index
        self._write_index += 4
        struct.pack_into('!i', self._array, dst_offset, value)

    def get_int32(self):
        if self._read_index > self._write_index - 4:
            raise IndexError('Not enough data to get')
        src_offset = self._read_index
        self._read_index += 4
        return struct.unpack_from('!i', self._array, src_offset)[0]

    def put_int64(self, value):
        dst_offset = self._write_index
        self._write_index += 8
        struct.pack_into('!q', self._array, dst_offset, value)

    def get_int64(self):
        if self._read_index > self._write_index - 8:
            raise IndexError('Not enough data to get')

        src_offset = self._read_index
        self._read_index += 8
        return struct.unpack_from('!q', self._array, src_offset)[0]

    def put_float64(self, value):
        dst_offset = self._write_index
        self._write_index += 8
        struct.pack_into('!d', self._array, dst_offset, value)

    def get_float64(self):
        if self._read_index > self._write_index - 8:
            raise IndexError('Not enough data to get')

        src_offset = self._read_index
        self._read_index += 8
        return struct.unpack_from('!d', self._array, src_offset)[0]

    def put_bool(self, value):
        if value:
            self.put_int8(1)
        else:
            self.put_int8(0)

    def get_bool(self):
        if self.get_int8():
            return True
        else:
            return False

    def put(self, array, offset=0, length=None):
        if not isinstance(array, bytearray):
            raise TypeError('Can put only bytearray')

        array_len = len(array)

        if length is None:
            length = array_len - offset
        else:
            if not (0 <= length <= array_len - offset):
                raise ValueError('Length out of range')

        dst_offset = self._write_index
        self._write_index += length
        self._array[dst_offset:dst_offset + length] = array[offset:offset + length]

        return length

    def get(self, array, offset=0, length=None):
        if not isinstance(array, bytearray):
            raise TypeError('Can get only to bytearray')

        array_len = len(array)

        if not (0 <= offset <= array_len):
            raise ValueError('Offset out of range')

        if length is None:
            length = array_len - offset
        else:
            if not (0 <= length <= array_len - offset):
                raise ValueError('Length out of range')

        src_offset = self._read_index
        self._read_index += length
        array[offset:offset + length] = self._array[src_offset:src_offset + length]

        return length

    def array(self):
        return bytearray(self._array[0:self._write_index])

    def readable_bytes(self):
        return self._write_index - self._read_index

    def read_index(self):
        return self._read_index

    def write_index(self):
        return self._write_index

