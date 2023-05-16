# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/room303/room.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import room303_pb2 as api_dot_commons_dot_room303__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61pi/v1alpha1/room303/room.proto\x12\x14\x61pi.v1alpha1.room303\x1a\x19\x61pi/commons/room303.proto\"l\n\x11\x43reateRoomRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x15.api.commons.RoomTypeR\x04type\x12\x18\n\x07members\x18\x03 \x03(\tR\x07members\")\n\x0eGetRoomRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\"\x15\n\x13ListAllRoomsRequest\"\x1b\n\x19ListRoomsForMemberRequest\"<\n\x11ListRoomsResponse\x12\'\n\x05rooms\x18\x01 \x03(\x0b\x32\x11.api.commons.RoomR\x05rooms\"-\n\x12\x41rchiveRoomRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomIdB\x97\x01\n\x18\x63om.api.v1alpha1.room303B\tRoomProtoP\x01\xa2\x02\x03\x41VR\xaa\x02\x14\x41pi.V1alpha1.Room303\xca\x02\x14\x41pi\\V1alpha1\\Room303\xe2\x02 Api\\V1alpha1\\Room303\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Room303b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.room303.room_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.api.v1alpha1.room303B\tRoomProtoP\001\242\002\003AVR\252\002\024Api.V1alpha1.Room303\312\002\024Api\\V1alpha1\\Room303\342\002 Api\\V1alpha1\\Room303\\GPBMetadata\352\002\026Api::V1alpha1::Room303'
  _globals['_CREATEROOMREQUEST']._serialized_start=84
  _globals['_CREATEROOMREQUEST']._serialized_end=192
  _globals['_GETROOMREQUEST']._serialized_start=194
  _globals['_GETROOMREQUEST']._serialized_end=235
  _globals['_LISTALLROOMSREQUEST']._serialized_start=237
  _globals['_LISTALLROOMSREQUEST']._serialized_end=258
  _globals['_LISTROOMSFORMEMBERREQUEST']._serialized_start=260
  _globals['_LISTROOMSFORMEMBERREQUEST']._serialized_end=287
  _globals['_LISTROOMSRESPONSE']._serialized_start=289
  _globals['_LISTROOMSRESPONSE']._serialized_end=349
  _globals['_ARCHIVEROOMREQUEST']._serialized_start=351
  _globals['_ARCHIVEROOMREQUEST']._serialized_end=396
# @@protoc_insertion_point(module_scope)
