# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: branch_undolog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='branch_undolog.proto',
  package='seata.rm.datasource.undo.parser.proto',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x62ranch_undolog.proto\x12%seata.rm.datasource.undo.parser.proto\x1a\x19google/protobuf/any.proto\"\x99\x01\n\rBranchUndoLog\x12\x10\n\x03xid\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tbranch_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12H\n\rsql_undo_logs\x18\x03 \x03(\x0b\x32\x31.seata.rm.datasource.undo.parser.proto.SQLUndoLogB\x06\n\x04_xidB\x0c\n\n_branch_id\"\xc7\x01\n\nSQLUndoLog\x12\x10\n\x08sql_type\x18\x01 \x01(\x05\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12I\n\x0c\x62\x65\x66ore_image\x18\x03 \x01(\x0b\x32\x33.seata.rm.datasource.undo.parser.proto.TableRecords\x12H\n\x0b\x61\x66ter_image\x18\x04 \x01(\x0b\x32\x33.seata.rm.datasource.undo.parser.proto.TableRecords\"\xa2\x01\n\x0cTableRecords\x12\x44\n\ntable_meta\x18\x01 \x01(\x0b\x32\x30.seata.rm.datasource.undo.parser.proto.TableMeta\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12\x38\n\x04rows\x18\x03 \x03(\x0b\x32*.seata.rm.datasource.undo.parser.proto.Row\"\x95\x03\n\tTableMeta\x12\x12\n\ntable_name\x18\x01 \x01(\t\x12U\n\x0b\x61ll_columns\x18\x02 \x03(\x0b\x32@.seata.rm.datasource.undo.parser.proto.TableMeta.AllColumnsEntry\x12S\n\nall_indexs\x18\x03 \x03(\x0b\x32?.seata.rm.datasource.undo.parser.proto.TableMeta.AllIndexsEntry\x1a\x64\n\x0f\x41llColumnsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b\x32\x31.seata.rm.datasource.undo.parser.proto.ColumnMeta:\x02\x38\x01\x1a\x62\n\x0e\x41llIndexsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12?\n\x05value\x18\x02 \x01(\x0b\x32\x30.seata.rm.datasource.undo.parser.proto.IndexMeta:\x02\x38\x01\"\xb6\x03\n\nColumnMeta\x12\x11\n\ttable_cat\x18\x01 \x01(\t\x12\x19\n\x11table_schema_name\x18\x02 \x01(\t\x12\x12\n\ntable_name\x18\x03 \x01(\t\x12\x13\n\x0b\x63olumn_name\x18\x04 \x01(\t\x12\x11\n\tdata_type\x18\x05 \x01(\x05\x12\x16\n\x0e\x64\x61ta_type_name\x18\x06 \x01(\t\x12\x13\n\x0b\x63olumn_size\x18\x07 \x01(\x05\x12\x16\n\x0e\x64\x65\x63imal_digits\x18\x08 \x01(\x05\x12\x16\n\x0enum_prec_radix\x18\t \x01(\x05\x12\x11\n\tnull_able\x18\n \x01(\x05\x12\x0f\n\x07remarks\x18\x0b \x01(\t\x12\x12\n\ncolumn_def\x18\x0c \x01(\t\x12\x15\n\rsql_data_type\x18\r \x01(\x05\x12\x18\n\x10sql_datetime_sub\x18\x0e \x01(\x05\x12/\n\x11\x63har_octet_length\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\x12\x18\n\x10ordinal_position\x18\x10 \x01(\x05\x12\x13\n\x0bis_nullable\x18\x11 \x01(\t\x12\x18\n\x10is_autoincrement\x18\x12 \x01(\t\"\xf5\x01\n\tIndexMeta\x12\x41\n\x06values\x18\x01 \x03(\x0b\x32\x31.seata.rm.datasource.undo.parser.proto.ColumnMeta\x12\x12\n\nnon_unique\x18\x02 \x01(\x08\x12\x17\n\x0findex_qualifier\x18\x03 \x01(\t\x12\x12\n\nindex_name\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\x05\x12\x12\n\nindex_type\x18\x06 \x01(\x05\x12\x13\n\x0b\x61sc_or_desc\x18\x07 \x01(\t\x12\x13\n\x0b\x63\x61rdinality\x18\x08 \x01(\x05\x12\x18\n\x10ordinal_position\x18\t \x01(\x05\"C\n\x03Row\x12<\n\x06\x66ields\x18\x01 \x03(\x0b\x32,.seata.rm.datasource.undo.parser.proto.Field\"Z\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08key_type\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12#\n\x05value\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_BRANCHUNDOLOG = _descriptor.Descriptor(
  name='BranchUndoLog',
  full_name='seata.rm.datasource.undo.parser.proto.BranchUndoLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='xid', full_name='seata.rm.datasource.undo.parser.proto.BranchUndoLog.xid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='branch_id', full_name='seata.rm.datasource.undo.parser.proto.BranchUndoLog.branch_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sql_undo_logs', full_name='seata.rm.datasource.undo.parser.proto.BranchUndoLog.sql_undo_logs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_xid', full_name='seata.rm.datasource.undo.parser.proto.BranchUndoLog._xid',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_branch_id', full_name='seata.rm.datasource.undo.parser.proto.BranchUndoLog._branch_id',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=91,
  serialized_end=244,
)


_SQLUNDOLOG = _descriptor.Descriptor(
  name='SQLUndoLog',
  full_name='seata.rm.datasource.undo.parser.proto.SQLUndoLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sql_type', full_name='seata.rm.datasource.undo.parser.proto.SQLUndoLog.sql_type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='seata.rm.datasource.undo.parser.proto.SQLUndoLog.table_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='before_image', full_name='seata.rm.datasource.undo.parser.proto.SQLUndoLog.before_image', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='after_image', full_name='seata.rm.datasource.undo.parser.proto.SQLUndoLog.after_image', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=247,
  serialized_end=446,
)


_TABLERECORDS = _descriptor.Descriptor(
  name='TableRecords',
  full_name='seata.rm.datasource.undo.parser.proto.TableRecords',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_meta', full_name='seata.rm.datasource.undo.parser.proto.TableRecords.table_meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='seata.rm.datasource.undo.parser.proto.TableRecords.table_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rows', full_name='seata.rm.datasource.undo.parser.proto.TableRecords.rows', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=449,
  serialized_end=611,
)


_TABLEMETA_ALLCOLUMNSENTRY = _descriptor.Descriptor(
  name='AllColumnsEntry',
  full_name='seata.rm.datasource.undo.parser.proto.TableMeta.AllColumnsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='seata.rm.datasource.undo.parser.proto.TableMeta.AllColumnsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='seata.rm.datasource.undo.parser.proto.TableMeta.AllColumnsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=819,
  serialized_end=919,
)

_TABLEMETA_ALLINDEXSENTRY = _descriptor.Descriptor(
  name='AllIndexsEntry',
  full_name='seata.rm.datasource.undo.parser.proto.TableMeta.AllIndexsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='seata.rm.datasource.undo.parser.proto.TableMeta.AllIndexsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='seata.rm.datasource.undo.parser.proto.TableMeta.AllIndexsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=921,
  serialized_end=1019,
)

_TABLEMETA = _descriptor.Descriptor(
  name='TableMeta',
  full_name='seata.rm.datasource.undo.parser.proto.TableMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='seata.rm.datasource.undo.parser.proto.TableMeta.table_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='all_columns', full_name='seata.rm.datasource.undo.parser.proto.TableMeta.all_columns', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='all_indexs', full_name='seata.rm.datasource.undo.parser.proto.TableMeta.all_indexs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TABLEMETA_ALLCOLUMNSENTRY, _TABLEMETA_ALLINDEXSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=614,
  serialized_end=1019,
)


_COLUMNMETA = _descriptor.Descriptor(
  name='ColumnMeta',
  full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_cat', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.table_cat', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table_schema_name', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.table_schema_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.table_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column_name', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.column_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.data_type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data_type_name', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.data_type_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column_size', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.column_size', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='decimal_digits', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.decimal_digits', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_prec_radix', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.num_prec_radix', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='null_able', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.null_able', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remarks', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.remarks', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='column_def', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.column_def', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sql_data_type', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.sql_data_type', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sql_datetime_sub', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.sql_datetime_sub', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='char_octet_length', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.char_octet_length', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ordinal_position', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.ordinal_position', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_nullable', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.is_nullable', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_autoincrement', full_name='seata.rm.datasource.undo.parser.proto.ColumnMeta.is_autoincrement', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1022,
  serialized_end=1460,
)


_INDEXMETA = _descriptor.Descriptor(
  name='IndexMeta',
  full_name='seata.rm.datasource.undo.parser.proto.IndexMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='seata.rm.datasource.undo.parser.proto.IndexMeta.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='non_unique', full_name='seata.rm.datasource.undo.parser.proto.IndexMeta.non_unique', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index_qualifier', full_name='seata.rm.datasource.undo.parser.proto.IndexMeta.index_qualifier', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index_name', full_name='seata.rm.datasource.undo.parser.proto.IndexMeta.index_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='seata.rm.datasource.undo.parser.proto.IndexMeta.type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='index_type', full_name='seata.rm.datasource.undo.parser.proto.IndexMeta.index_type', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='asc_or_desc', full_name='seata.rm.datasource.undo.parser.proto.IndexMeta.asc_or_desc', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cardinality', full_name='seata.rm.datasource.undo.parser.proto.IndexMeta.cardinality', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ordinal_position', full_name='seata.rm.datasource.undo.parser.proto.IndexMeta.ordinal_position', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1463,
  serialized_end=1708,
)


_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='seata.rm.datasource.undo.parser.proto.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='fields', full_name='seata.rm.datasource.undo.parser.proto.Row.fields', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1710,
  serialized_end=1777,
)


_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='seata.rm.datasource.undo.parser.proto.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='seata.rm.datasource.undo.parser.proto.Field.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_type', full_name='seata.rm.datasource.undo.parser.proto.Field.key_type', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='seata.rm.datasource.undo.parser.proto.Field.type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='seata.rm.datasource.undo.parser.proto.Field.value', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1779,
  serialized_end=1869,
)

_BRANCHUNDOLOG.fields_by_name['sql_undo_logs'].message_type = _SQLUNDOLOG
_BRANCHUNDOLOG.oneofs_by_name['_xid'].fields.append(
  _BRANCHUNDOLOG.fields_by_name['xid'])
_BRANCHUNDOLOG.fields_by_name['xid'].containing_oneof = _BRANCHUNDOLOG.oneofs_by_name['_xid']
_BRANCHUNDOLOG.oneofs_by_name['_branch_id'].fields.append(
  _BRANCHUNDOLOG.fields_by_name['branch_id'])
_BRANCHUNDOLOG.fields_by_name['branch_id'].containing_oneof = _BRANCHUNDOLOG.oneofs_by_name['_branch_id']
_SQLUNDOLOG.fields_by_name['before_image'].message_type = _TABLERECORDS
_SQLUNDOLOG.fields_by_name['after_image'].message_type = _TABLERECORDS
_TABLERECORDS.fields_by_name['table_meta'].message_type = _TABLEMETA
_TABLERECORDS.fields_by_name['rows'].message_type = _ROW
_TABLEMETA_ALLCOLUMNSENTRY.fields_by_name['value'].message_type = _COLUMNMETA
_TABLEMETA_ALLCOLUMNSENTRY.containing_type = _TABLEMETA
_TABLEMETA_ALLINDEXSENTRY.fields_by_name['value'].message_type = _INDEXMETA
_TABLEMETA_ALLINDEXSENTRY.containing_type = _TABLEMETA
_TABLEMETA.fields_by_name['all_columns'].message_type = _TABLEMETA_ALLCOLUMNSENTRY
_TABLEMETA.fields_by_name['all_indexs'].message_type = _TABLEMETA_ALLINDEXSENTRY
_COLUMNMETA.fields_by_name['char_octet_length'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_INDEXMETA.fields_by_name['values'].message_type = _COLUMNMETA
_ROW.fields_by_name['fields'].message_type = _FIELD
_FIELD.fields_by_name['value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['BranchUndoLog'] = _BRANCHUNDOLOG
DESCRIPTOR.message_types_by_name['SQLUndoLog'] = _SQLUNDOLOG
DESCRIPTOR.message_types_by_name['TableRecords'] = _TABLERECORDS
DESCRIPTOR.message_types_by_name['TableMeta'] = _TABLEMETA
DESCRIPTOR.message_types_by_name['ColumnMeta'] = _COLUMNMETA
DESCRIPTOR.message_types_by_name['IndexMeta'] = _INDEXMETA
DESCRIPTOR.message_types_by_name['Row'] = _ROW
DESCRIPTOR.message_types_by_name['Field'] = _FIELD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BranchUndoLog = _reflection.GeneratedProtocolMessageType('BranchUndoLog', (_message.Message,), {
  'DESCRIPTOR' : _BRANCHUNDOLOG,
  '__module__' : 'branch_undolog_pb2'
  # @@protoc_insertion_point(class_scope:seata.rm.datasource.undo.parser.proto.BranchUndoLog)
  })
_sym_db.RegisterMessage(BranchUndoLog)

SQLUndoLog = _reflection.GeneratedProtocolMessageType('SQLUndoLog', (_message.Message,), {
  'DESCRIPTOR' : _SQLUNDOLOG,
  '__module__' : 'branch_undolog_pb2'
  # @@protoc_insertion_point(class_scope:seata.rm.datasource.undo.parser.proto.SQLUndoLog)
  })
_sym_db.RegisterMessage(SQLUndoLog)

TableRecords = _reflection.GeneratedProtocolMessageType('TableRecords', (_message.Message,), {
  'DESCRIPTOR' : _TABLERECORDS,
  '__module__' : 'branch_undolog_pb2'
  # @@protoc_insertion_point(class_scope:seata.rm.datasource.undo.parser.proto.TableRecords)
  })
_sym_db.RegisterMessage(TableRecords)

TableMeta = _reflection.GeneratedProtocolMessageType('TableMeta', (_message.Message,), {

  'AllColumnsEntry' : _reflection.GeneratedProtocolMessageType('AllColumnsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TABLEMETA_ALLCOLUMNSENTRY,
    '__module__' : 'branch_undolog_pb2'
    # @@protoc_insertion_point(class_scope:seata.rm.datasource.undo.parser.proto.TableMeta.AllColumnsEntry)
    })
  ,

  'AllIndexsEntry' : _reflection.GeneratedProtocolMessageType('AllIndexsEntry', (_message.Message,), {
    'DESCRIPTOR' : _TABLEMETA_ALLINDEXSENTRY,
    '__module__' : 'branch_undolog_pb2'
    # @@protoc_insertion_point(class_scope:seata.rm.datasource.undo.parser.proto.TableMeta.AllIndexsEntry)
    })
  ,
  'DESCRIPTOR' : _TABLEMETA,
  '__module__' : 'branch_undolog_pb2'
  # @@protoc_insertion_point(class_scope:seata.rm.datasource.undo.parser.proto.TableMeta)
  })
_sym_db.RegisterMessage(TableMeta)
_sym_db.RegisterMessage(TableMeta.AllColumnsEntry)
_sym_db.RegisterMessage(TableMeta.AllIndexsEntry)

ColumnMeta = _reflection.GeneratedProtocolMessageType('ColumnMeta', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNMETA,
  '__module__' : 'branch_undolog_pb2'
  # @@protoc_insertion_point(class_scope:seata.rm.datasource.undo.parser.proto.ColumnMeta)
  })
_sym_db.RegisterMessage(ColumnMeta)

IndexMeta = _reflection.GeneratedProtocolMessageType('IndexMeta', (_message.Message,), {
  'DESCRIPTOR' : _INDEXMETA,
  '__module__' : 'branch_undolog_pb2'
  # @@protoc_insertion_point(class_scope:seata.rm.datasource.undo.parser.proto.IndexMeta)
  })
_sym_db.RegisterMessage(IndexMeta)

Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), {
  'DESCRIPTOR' : _ROW,
  '__module__' : 'branch_undolog_pb2'
  # @@protoc_insertion_point(class_scope:seata.rm.datasource.undo.parser.proto.Row)
  })
_sym_db.RegisterMessage(Row)

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
  'DESCRIPTOR' : _FIELD,
  '__module__' : 'branch_undolog_pb2'
  # @@protoc_insertion_point(class_scope:seata.rm.datasource.undo.parser.proto.Field)
  })
_sym_db.RegisterMessage(Field)


_TABLEMETA_ALLCOLUMNSENTRY._options = None
_TABLEMETA_ALLINDEXSENTRY._options = None
# @@protoc_insertion_point(module_scope)