# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/room303/member.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'api/v1alpha1/room303/member.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import room303_pb2 as api_dot_commons_dot_room303__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!api/v1alpha1/room303/member.proto\x12\x14\x61pi.v1alpha1.room303\x1a\x19\x61pi/commons/room303.proto\"^\n\x14\x41\x64\x64RoomMemberRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\x12\x14\n\x05\x61\x64min\x18\x03 \x01(\x08R\x05\x61\x64min\"K\n\x17RemoveRoomMemberRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x17\n\x07room_id\x18\x02 \x01(\tR\x06roomId\"\x1a\n\x18RemoveRoomMemberResponse\"1\n\x16ListRoomMembersRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\"H\n\x17ListRoomMembersResponse\x12-\n\x07members\x18\x01 \x03(\x0b\x32\x13.api.commons.MemberR\x07members\"P\n\x1cSetAdminForRoomMemberRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"\x1f\n\x1dSetAdminForRoomMemberResponse\"*\n\x0fJoinRoomRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\"H\n\x14GetRoomMemberRequest\x12\x17\n\x07room_id\x18\x02 \x01(\tR\x06roomId\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userIdB\x99\x01\n\x18\x63om.api.v1alpha1.room303B\x0bMemberProtoP\x01\xa2\x02\x03\x41VR\xaa\x02\x14\x41pi.V1alpha1.Room303\xca\x02\x14\x41pi\\V1alpha1\\Room303\xe2\x02 Api\\V1alpha1\\Room303\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Room303b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.room303.member_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.room303B\013MemberProtoP\001\242\002\003AVR\252\002\024Api.V1alpha1.Room303\312\002\024Api\\V1alpha1\\Room303\342\002 Api\\V1alpha1\\Room303\\GPBMetadata\352\002\026Api::V1alpha1::Room303'
  _globals['_ADDROOMMEMBERREQUEST']._serialized_start=86
  _globals['_ADDROOMMEMBERREQUEST']._serialized_end=180
  _globals['_REMOVEROOMMEMBERREQUEST']._serialized_start=182
  _globals['_REMOVEROOMMEMBERREQUEST']._serialized_end=257
  _globals['_REMOVEROOMMEMBERRESPONSE']._serialized_start=259
  _globals['_REMOVEROOMMEMBERRESPONSE']._serialized_end=285
  _globals['_LISTROOMMEMBERSREQUEST']._serialized_start=287
  _globals['_LISTROOMMEMBERSREQUEST']._serialized_end=336
  _globals['_LISTROOMMEMBERSRESPONSE']._serialized_start=338
  _globals['_LISTROOMMEMBERSRESPONSE']._serialized_end=410
  _globals['_SETADMINFORROOMMEMBERREQUEST']._serialized_start=412
  _globals['_SETADMINFORROOMMEMBERREQUEST']._serialized_end=492
  _globals['_SETADMINFORROOMMEMBERRESPONSE']._serialized_start=494
  _globals['_SETADMINFORROOMMEMBERRESPONSE']._serialized_end=525
  _globals['_JOINROOMREQUEST']._serialized_start=527
  _globals['_JOINROOMREQUEST']._serialized_end=569
  _globals['_GETROOMMEMBERREQUEST']._serialized_start=571
  _globals['_GETROOMMEMBERREQUEST']._serialized_end=643
# @@protoc_insertion_point(module_scope)
