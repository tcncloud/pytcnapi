# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/room303/room.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import room303_pb2 as api_dot_commons_dot_room303__pb2
from api.commons import user_pb2 as api_dot_commons_dot_user__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61pi/v1alpha1/room303/room.proto\x12\x14\x61pi.v1alpha1.room303\x1a\x19\x61pi/commons/room303.proto\x1a\x16\x61pi/commons/user.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"l\n\x11\x43reateRoomRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x15.api.commons.RoomTypeR\x04type\x12\x18\n\x07members\x18\x03 \x03(\tR\x07members\")\n\x0eGetRoomRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\"\x15\n\x13ListAllRoomsRequest\"\x1b\n\x19ListRoomsForMemberRequest\"<\n\x11ListRoomsResponse\x12\'\n\x05rooms\x18\x01 \x03(\x0b\x32\x11.api.commons.RoomR\x05rooms\"-\n\x12\x41rchiveRoomRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\"\x93\x01\n\x15ListUsersNamesRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x14\n\x05\x61gent\x18\x02 \x01(\x08R\x05\x61gent\x12M\n\x0f\x61rchived_filter\x18\x03 \x01(\x0e\x32$.api.commons.UserArchivedStateFilterR\x0e\x61rchivedFilter\"^\n\x16ListUsersNamesResponse\x12\x44\n\x0cuser_details\x18\x01 \x03(\x0b\x32!.api.v1alpha1.room303.UserDetailsR\x0buserDetails\"\x7f\n\x0bUserDetails\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1b\n\tuser_name\x18\x02 \x01(\tR\x08userName\x12\x1d\n\nfirst_name\x18\x03 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x04 \x01(\tR\x08lastName\"\x9e\x01\n\x17UpdateRoomConfigRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\x12/\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x17.api.commons.RoomConfigR\x06\x63onfig\x12\x39\n\nfield_mask\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x89\x01\n\x19UpdateGlobalConfigRequest\x12\x31\n\x06\x63onfig\x18\x01 \x01(\x0b\x32\x19.api.commons.GlobalConfigR\x06\x63onfig\x12\x39\n\nfield_mask\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\xe8\x01\n\x1aUpdateGlobalConfigResponse\x12\x1b\n\tedited_by\x18\x01 \x01(\tR\x08\x65\x64itedBy\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.api.commons.GlobalConfigR\x06\x63onfig\x12=\n\x0c\x64\x61te_created\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated\x12;\n\x0blast_edited\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastEdited\"\x18\n\x16GetGlobalConfigRequest\"\xe5\x01\n\x17GetGlobalConfigResponse\x12\x1b\n\tedited_by\x18\x01 \x01(\tR\x08\x65\x64itedBy\x12\x31\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x19.api.commons.GlobalConfigR\x06\x63onfig\x12=\n\x0c\x64\x61te_created\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated\x12;\n\x0blast_edited\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastEditedB\x97\x01\n\x18\x63om.api.v1alpha1.room303B\tRoomProtoP\x01\xa2\x02\x03\x41VR\xaa\x02\x14\x41pi.V1alpha1.Room303\xca\x02\x14\x41pi\\V1alpha1\\Room303\xe2\x02 Api\\V1alpha1\\Room303\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Room303b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.room303.room_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.room303B\tRoomProtoP\001\242\002\003AVR\252\002\024Api.V1alpha1.Room303\312\002\024Api\\V1alpha1\\Room303\342\002 Api\\V1alpha1\\Room303\\GPBMetadata\352\002\026Api::V1alpha1::Room303'
  _globals['_CREATEROOMREQUEST']._serialized_start=175
  _globals['_CREATEROOMREQUEST']._serialized_end=283
  _globals['_GETROOMREQUEST']._serialized_start=285
  _globals['_GETROOMREQUEST']._serialized_end=326
  _globals['_LISTALLROOMSREQUEST']._serialized_start=328
  _globals['_LISTALLROOMSREQUEST']._serialized_end=349
  _globals['_LISTROOMSFORMEMBERREQUEST']._serialized_start=351
  _globals['_LISTROOMSFORMEMBERREQUEST']._serialized_end=378
  _globals['_LISTROOMSRESPONSE']._serialized_start=380
  _globals['_LISTROOMSRESPONSE']._serialized_end=440
  _globals['_ARCHIVEROOMREQUEST']._serialized_start=442
  _globals['_ARCHIVEROOMREQUEST']._serialized_end=487
  _globals['_LISTUSERSNAMESREQUEST']._serialized_start=490
  _globals['_LISTUSERSNAMESREQUEST']._serialized_end=637
  _globals['_LISTUSERSNAMESRESPONSE']._serialized_start=639
  _globals['_LISTUSERSNAMESRESPONSE']._serialized_end=733
  _globals['_USERDETAILS']._serialized_start=735
  _globals['_USERDETAILS']._serialized_end=862
  _globals['_UPDATEROOMCONFIGREQUEST']._serialized_start=865
  _globals['_UPDATEROOMCONFIGREQUEST']._serialized_end=1023
  _globals['_UPDATEGLOBALCONFIGREQUEST']._serialized_start=1026
  _globals['_UPDATEGLOBALCONFIGREQUEST']._serialized_end=1163
  _globals['_UPDATEGLOBALCONFIGRESPONSE']._serialized_start=1166
  _globals['_UPDATEGLOBALCONFIGRESPONSE']._serialized_end=1398
  _globals['_GETGLOBALCONFIGREQUEST']._serialized_start=1400
  _globals['_GETGLOBALCONFIGREQUEST']._serialized_end=1424
  _globals['_GETGLOBALCONFIGRESPONSE']._serialized_start=1427
  _globals['_GETGLOBALCONFIGRESPONSE']._serialized_end=1656
# @@protoc_insertion_point(module_scope)
