# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/room303/message.proto
# Protobuf Python Version: 5.27.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    0,
    '',
    'api/v1alpha1/room303/message.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import room303_pb2 as api_dot_commons_dot_room303__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/room303/message.proto\x12\x14\x61pi.v1alpha1.room303\x1a\x19\x61pi/commons/room303.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"_\n\x14\x43reateMessageRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\x12\x18\n\x07payload\x18\x02 \x01(\tR\x07payload\x12\x14\n\x05nonce\x18\x03 \x01(\tR\x05nonce\"G\n\x15\x43reateMessageResponse\x12.\n\x07message\x18\x01 \x01(\x0b\x32\x14.api.commons.MessageR\x07message\"|\n\x12\x45\x64itMessageRequest\x12\x1d\n\nmessage_id\x18\x01 \x01(\tR\tmessageId\x12\x18\n\x07payload\x18\x02 \x01(\tR\x07payload\x12\x17\n\x07room_id\x18\x03 \x01(\tR\x06roomId\x12\x14\n\x05nonce\x18\x04 \x01(\tR\x05nonce\"E\n\x13\x45\x64itMessageResponse\x12.\n\x07message\x18\x01 \x01(\x0b\x32\x14.api.commons.MessageR\x07message\"g\n\x12GetMessagesRequest\x12\x17\n\x07room_id\x18\x02 \x01(\tR\x06roomId\x12\x32\n\x06offset\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x06offsetJ\x04\x08\x01\x10\x02\"G\n\x13GetMessagesResponse\x12\x30\n\x08messages\x18\x01 \x03(\x0b\x32\x14.api.commons.MessageR\x08messages\"S\n\x1bStreamMessageUpdatesRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\x12\x1b\n\tmember_id\x18\x02 \x01(\tR\x08memberId\"N\n\x1cStreamMessageUpdatesResponse\x12.\n\x07message\x18\x01 \x01(\x0b\x32\x14.api.commons.MessageR\x07message\"T\n\x16MarkMessageReadRequest\x12\x1d\n\nmessage_id\x18\x01 \x01(\tR\tmessageId\x12\x1b\n\tmember_id\x18\x02 \x01(\tR\x08memberId\"\x19\n\x17MarkMessageReadResponse\"5\n\x1aMarkAllMessagesReadRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\"V\n\x1bMarkAllMessagesReadResponse\x12\x37\n\x0crows_updated\x18\x01 \x03(\x0b\x32\x14.api.commons.MessageR\x0browsUpdated\"\x17\n\x15GetUnreadStatsRequest\"H\n\x16GetUnreadStatsResponse\x12.\n\x05stats\x18\x01 \x03(\x0b\x32\x18.api.commons.MessageStatR\x05stats\"d\n\x14\x44\x65leteMessageRequest\x12\x1d\n\nmessage_id\x18\x01 \x01(\tR\tmessageId\x12\x17\n\x07room_id\x18\x02 \x01(\tR\x06roomId\x12\x14\n\x05nonce\x18\x03 \x01(\tR\x05nonce\"G\n\x15\x44\x65leteMessageResponse\x12.\n\x07message\x18\x01 \x01(\x0b\x32\x14.api.commons.MessageR\x07message\"V\n\x1a\x42ulkMarkMessageReadRequest\x12\x17\n\x07room_id\x18\x01 \x01(\tR\x06roomId\x12\x1f\n\x0bmessage_ids\x18\x02 \x03(\tR\nmessageIds\"O\n\x1b\x42ulkMarkMessageReadResponse\x12\x30\n\x08messages\x18\x01 \x03(\x0b\x32\x14.api.commons.MessageR\x08messagesB\x9a\x01\n\x18\x63om.api.v1alpha1.room303B\x0cMessageProtoP\x01\xa2\x02\x03\x41VR\xaa\x02\x14\x41pi.V1alpha1.Room303\xca\x02\x14\x41pi\\V1alpha1\\Room303\xe2\x02 Api\\V1alpha1\\Room303\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Room303b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.room303.message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.room303B\014MessageProtoP\001\242\002\003AVR\252\002\024Api.V1alpha1.Room303\312\002\024Api\\V1alpha1\\Room303\342\002 Api\\V1alpha1\\Room303\\GPBMetadata\352\002\026Api::V1alpha1::Room303'
  _globals['_CREATEMESSAGEREQUEST']._serialized_start=120
  _globals['_CREATEMESSAGEREQUEST']._serialized_end=215
  _globals['_CREATEMESSAGERESPONSE']._serialized_start=217
  _globals['_CREATEMESSAGERESPONSE']._serialized_end=288
  _globals['_EDITMESSAGEREQUEST']._serialized_start=290
  _globals['_EDITMESSAGEREQUEST']._serialized_end=414
  _globals['_EDITMESSAGERESPONSE']._serialized_start=416
  _globals['_EDITMESSAGERESPONSE']._serialized_end=485
  _globals['_GETMESSAGESREQUEST']._serialized_start=487
  _globals['_GETMESSAGESREQUEST']._serialized_end=590
  _globals['_GETMESSAGESRESPONSE']._serialized_start=592
  _globals['_GETMESSAGESRESPONSE']._serialized_end=663
  _globals['_STREAMMESSAGEUPDATESREQUEST']._serialized_start=665
  _globals['_STREAMMESSAGEUPDATESREQUEST']._serialized_end=748
  _globals['_STREAMMESSAGEUPDATESRESPONSE']._serialized_start=750
  _globals['_STREAMMESSAGEUPDATESRESPONSE']._serialized_end=828
  _globals['_MARKMESSAGEREADREQUEST']._serialized_start=830
  _globals['_MARKMESSAGEREADREQUEST']._serialized_end=914
  _globals['_MARKMESSAGEREADRESPONSE']._serialized_start=916
  _globals['_MARKMESSAGEREADRESPONSE']._serialized_end=941
  _globals['_MARKALLMESSAGESREADREQUEST']._serialized_start=943
  _globals['_MARKALLMESSAGESREADREQUEST']._serialized_end=996
  _globals['_MARKALLMESSAGESREADRESPONSE']._serialized_start=998
  _globals['_MARKALLMESSAGESREADRESPONSE']._serialized_end=1084
  _globals['_GETUNREADSTATSREQUEST']._serialized_start=1086
  _globals['_GETUNREADSTATSREQUEST']._serialized_end=1109
  _globals['_GETUNREADSTATSRESPONSE']._serialized_start=1111
  _globals['_GETUNREADSTATSRESPONSE']._serialized_end=1183
  _globals['_DELETEMESSAGEREQUEST']._serialized_start=1185
  _globals['_DELETEMESSAGEREQUEST']._serialized_end=1285
  _globals['_DELETEMESSAGERESPONSE']._serialized_start=1287
  _globals['_DELETEMESSAGERESPONSE']._serialized_end=1358
  _globals['_BULKMARKMESSAGEREADREQUEST']._serialized_start=1360
  _globals['_BULKMARKMESSAGEREADREQUEST']._serialized_end=1446
  _globals['_BULKMARKMESSAGEREADRESPONSE']._serialized_start=1448
  _globals['_BULKMARKMESSAGEREADRESPONSE']._serialized_end=1527
# @@protoc_insertion_point(module_scope)
