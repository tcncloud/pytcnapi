# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/room303.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/commons/room303.proto\x12\x0b\x61pi.commons\x1a\x1fgoogle/protobuf/timestamp.proto\"b\n\x07UserSid\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1b\n\tfull_name\x18\x02 \x01(\tR\x08\x66ullName\x12!\n\x0c\x64isplay_name\x18\x03 \x01(\tR\x0b\x64isplayName\"\xd0\x01\n\x06Member\x12/\n\x08user_sid\x18\x01 \x01(\x0b\x32\x14.api.commons.UserSidR\x07userSid\x12/\n\x08\x61\x64\x64\x65\x64_by\x18\x02 \x01(\x0b\x32\x14.api.commons.UserSidR\x07\x61\x64\x64\x65\x64\x42y\x12\x35\n\x08\x61\x64\x64\x65\x64_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x61\x64\x64\x65\x64\x41t\x12\x17\n\x07room_id\x18\x04 \x01(\tR\x06roomId\x12\x14\n\x05\x61\x64min\x18\x05 \x01(\x08R\x05\x61\x64min\"\xf2\x02\n\x04Room\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x17\n\x07room_id\x18\x02 \x01(\tR\x06roomId\x12)\n\x04type\x18\x04 \x01(\x0e\x32\x15.api.commons.RoomTypeR\x04type\x12\x39\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x39\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tupdatedAt\x12/\n\x06status\x18\x07 \x01(\x0e\x32\x17.api.commons.RoomStatusR\x06status\x12\x0e\n\x02id\x18\x08 \x01(\tR\x02id\x12!\n\x0c\x64isplay_name\x18\t \x01(\tR\x0b\x64isplayName\x12/\n\x06\x63onfig\x18\n \x01(\x0b\x32\x17.api.commons.RoomConfigR\x06\x63onfigJ\x04\x08\x03\x10\x04\"\xff\x02\n\x07Message\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nmessage_id\x18\x02 \x01(\tR\tmessageId\x12\x17\n\x07room_id\x18\x03 \x01(\tR\x06roomId\x12\x31\n\tfrom_user\x18\x04 \x01(\x0b\x32\x14.api.commons.UserSidR\x08\x66romUser\x12\x32\n\x06status\x18\x05 \x01(\x0e\x32\x1a.api.commons.MessageStatusR\x06status\x12;\n\x0breceived_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nreceivedAt\x12\x39\n\nupdated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tupdatedAt\x12\x18\n\x07payload\x18\x08 \x01(\tR\x07payload\x12\x16\n\x06unread\x18\t \x01(\x08R\x06unread\x12\x14\n\x05nonce\x18\n \x01(\tR\x05nonce\"O\n\x0bMessageStat\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\x12\'\n\x0funread_messages\x18\x02 \x01(\x05R\x0eunreadMessages\"\xea\x02\n\x0cGlobalConfig\x12\x42\n\x0b\x63reate_room\x18\x01 \x01(\x0e\x32!.api.commons.ConfigPermissionEnumR\ncreateRoom\x12O\n\x12join_existing_room\x18\x02 \x01(\x0e\x32!.api.commons.ConfigPermissionEnumR\x10joinExistingRoom\x12^\n\x1asend_message_to_supervisor\x18\x03 \x01(\x0e\x32!.api.commons.ConfigPermissionEnumR\x17sendMessageToSupervisor\x12\x65\n\x1esend_message_to_non_supervisor\x18\x04 \x01(\x0e\x32!.api.commons.ConfigPermissionEnumR\x1asendMessageToNonSupervisor\"\xaf\x03\n\nRoomConfig\x12<\n\x08\x61\x64\x64_user\x18\x01 \x01(\x0e\x32!.api.commons.ConfigPermissionEnumR\x07\x61\x64\x64User\x12\x42\n\x0bremove_user\x18\x02 \x01(\x0e\x32!.api.commons.ConfigPermissionEnumR\nremoveUser\x12K\n\x10promote_to_admin\x18\x03 \x01(\x0e\x32!.api.commons.ConfigPermissionEnumR\x0epromoteToAdmin\x12\x46\n\rread_messages\x18\x04 \x01(\x0e\x32!.api.commons.ConfigPermissionEnumR\x0creadMessages\x12\x44\n\x0csend_message\x18\x05 \x01(\x0e\x32!.api.commons.ConfigPermissionEnumR\x0bsendMessage\x12\x44\n\x0c\x61rchive_room\x18\x06 \x01(\x0e\x32!.api.commons.ConfigPermissionEnumR\x0b\x61rchiveRoom*h\n\x08RoomType\x12\x14\n\x10ROOM_TYPE_DIRECT\x10\x00\x12\x13\n\x0fROOM_TYPE_MULTI\x10\x01\x12\x14\n\x10ROOM_TYPE_SYSTEM\x10\x02\x12\x1b\n\x17ROOM_TYPE_GLOBAL_SYSTEM\x10\x03*b\n\rMessageStatus\x12\x19\n\x15MESSAGE_STATUS_ACTIVE\x10\x00\x12\x19\n\x15MESSAGE_STATUS_EDITED\x10\x01\x12\x1b\n\x17MESSAGE_STATUS_ARCHIVED\x10\x02*W\n\nRoomStatus\x12\x16\n\x12ROOM_STATUS_ACTIVE\x10\x00\x12\x18\n\x14ROOM_STATUS_ARCHIVED\x10\x01\x12\x17\n\x13ROOM_STATUS_DELETED\x10\x02*O\n\x14\x43onfigPermissionEnum\x12\x0b\n\x07LIMITED\x10\x00\x12\x12\n\x0eROOM303_MEMBER\x10\x01\x12\x16\n\x12ROOM303_SUPERVISOR\x10\x02\x42l\n\x0f\x63om.api.commonsB\x0cRoom303ProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.room303_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\014Room303ProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_ROOMTYPE']._serialized_start=2025
  _globals['_ROOMTYPE']._serialized_end=2129
  _globals['_MESSAGESTATUS']._serialized_start=2131
  _globals['_MESSAGESTATUS']._serialized_end=2229
  _globals['_ROOMSTATUS']._serialized_start=2231
  _globals['_ROOMSTATUS']._serialized_end=2318
  _globals['_CONFIGPERMISSIONENUM']._serialized_start=2320
  _globals['_CONFIGPERMISSIONENUM']._serialized_end=2399
  _globals['_USERSID']._serialized_start=75
  _globals['_USERSID']._serialized_end=173
  _globals['_MEMBER']._serialized_start=176
  _globals['_MEMBER']._serialized_end=384
  _globals['_ROOM']._serialized_start=387
  _globals['_ROOM']._serialized_end=757
  _globals['_MESSAGE']._serialized_start=760
  _globals['_MESSAGE']._serialized_end=1143
  _globals['_MESSAGESTAT']._serialized_start=1145
  _globals['_MESSAGESTAT']._serialized_end=1224
  _globals['_GLOBALCONFIG']._serialized_start=1227
  _globals['_GLOBALCONFIG']._serialized_end=1589
  _globals['_ROOMCONFIG']._serialized_start=1592
  _globals['_ROOMCONFIG']._serialized_end=2023
# @@protoc_insertion_point(module_scope)
