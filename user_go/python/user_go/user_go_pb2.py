# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_go/user_go.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15user_go/user_go.proto\"\x16\n\x05Token\x12\r\n\x05token\x18\x01 \x01(\t\"=\n\x0cInternalUser\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t24\n\x0bUserService\x12%\n\nCheckToken\x12\x06.Token\x1a\r.InternalUser\"\x00\x42$Z\"github.com/lwinmgmg/grpc_m/user_gob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_go.user_go_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\"github.com/lwinmgmg/grpc_m/user_go'
  _globals['_TOKEN']._serialized_start=25
  _globals['_TOKEN']._serialized_end=47
  _globals['_INTERNALUSER']._serialized_start=49
  _globals['_INTERNALUSER']._serialized_end=110
  _globals['_USERSERVICE']._serialized_start=112
  _globals['_USERSERVICE']._serialized_end=164
# @@protoc_insertion_point(module_scope)
