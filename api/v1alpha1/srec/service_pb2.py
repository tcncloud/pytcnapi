# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/srec/service.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61pi/v1alpha1/srec/service.proto\x12\x11\x61pi.v1alpha1.srec\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"Y\n\x1bListScreenRecordingsRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\"\x8a\x01\n\x1cListScreenRecordingsResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12\x42\n\nrecordings\x18\x02 \x03(\x0b\x32\".api.v1alpha1.srec.ScreenRecordingR\nrecordings\"\xfd\x01\n\x0fScreenRecording\x12\x1d\n\nsession_id\x18\x02 \x01(\x03R\tsessionId\x12(\n\x10\x61gent_first_name\x18\x03 \x01(\tR\x0e\x61gentFirstName\x12&\n\x0f\x61gent_last_name\x18\x04 \x01(\tR\ragentLastName\x12\x39\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x1d\n\naudio_time\x18\x06 \x01(\rR\taudioTime\x12\x1f\n\x0b\x61udio_bytes\x18\x07 \x01(\x03R\naudioBytes\"=\n\x1cGetScreenRecordingURLRequest\x12\x1d\n\nsession_id\x18\x02 \x01(\x03R\tsessionId\"1\n\x1dGetScreenRecordingURLResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"=\n\x1c\x44\x65leteScreenRecordingRequest\x12\x1d\n\nsession_id\x18\x01 \x01(\x03R\tsessionId\"\x1f\n\x1d\x44\x65leteScreenRecordingResponse2\xc5\x04\n\x04Srec\x12\xba\x01\n\x14ListScreenRecordings\x12..api.v1alpha1.srec.ListScreenRecordingsRequest\x1a/.api.v1alpha1.srec.ListScreenRecordingsResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xf9\x03\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/srec/srec/listscreenrecordings:\x01*\x12\xbe\x01\n\x15GetScreenRecordingURL\x12/.api.v1alpha1.srec.GetScreenRecordingURLRequest\x1a\x30.api.v1alpha1.srec.GetScreenRecordingURLResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xf9\x03\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/srec/srec/getscreenrecordingurl:\x01*\x12\xbe\x01\n\x15\x44\x65leteScreenRecording\x12/.api.v1alpha1.srec.DeleteScreenRecordingRequest\x1a\x30.api.v1alpha1.srec.DeleteScreenRecordingResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xfb\x03\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/srec/srec/deletescreenrecording:\x01*B\x8b\x01\n\x15\x63om.api.v1alpha1.srecB\x0cServiceProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x11\x41pi.V1alpha1.Srec\xca\x02\x11\x41pi\\V1alpha1\\Srec\xe2\x02\x1d\x41pi\\V1alpha1\\Srec\\GPBMetadata\xea\x02\x13\x41pi::V1alpha1::Srecb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.srec.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.v1alpha1.srecB\014ServiceProtoP\001\242\002\003AVS\252\002\021Api.V1alpha1.Srec\312\002\021Api\\V1alpha1\\Srec\342\002\035Api\\V1alpha1\\Srec\\GPBMetadata\352\002\023Api::V1alpha1::Srec'
  _globals['_SREC'].methods_by_name['ListScreenRecordings']._options = None
  _globals['_SREC'].methods_by_name['ListScreenRecordings']._serialized_options = b'\272\270\221\002\005\n\003\010\371\003\202\323\344\223\0021\",/api/v1alpha1/srec/srec/listscreenrecordings:\001*'
  _globals['_SREC'].methods_by_name['GetScreenRecordingURL']._options = None
  _globals['_SREC'].methods_by_name['GetScreenRecordingURL']._serialized_options = b'\272\270\221\002\005\n\003\010\371\003\202\323\344\223\0022\"-/api/v1alpha1/srec/srec/getscreenrecordingurl:\001*'
  _globals['_SREC'].methods_by_name['DeleteScreenRecording']._options = None
  _globals['_SREC'].methods_by_name['DeleteScreenRecording']._serialized_options = b'\272\270\221\002\005\n\003\010\373\003\202\323\344\223\0022\"-/api/v1alpha1/srec/srec/deletescreenrecording:\001*'
  _globals['_LISTSCREENRECORDINGSREQUEST']._serialized_start=142
  _globals['_LISTSCREENRECORDINGSREQUEST']._serialized_end=231
  _globals['_LISTSCREENRECORDINGSRESPONSE']._serialized_start=234
  _globals['_LISTSCREENRECORDINGSRESPONSE']._serialized_end=372
  _globals['_SCREENRECORDING']._serialized_start=375
  _globals['_SCREENRECORDING']._serialized_end=628
  _globals['_GETSCREENRECORDINGURLREQUEST']._serialized_start=630
  _globals['_GETSCREENRECORDINGURLREQUEST']._serialized_end=691
  _globals['_GETSCREENRECORDINGURLRESPONSE']._serialized_start=693
  _globals['_GETSCREENRECORDINGURLRESPONSE']._serialized_end=742
  _globals['_DELETESCREENRECORDINGREQUEST']._serialized_start=744
  _globals['_DELETESCREENRECORDINGREQUEST']._serialized_end=805
  _globals['_DELETESCREENRECORDINGRESPONSE']._serialized_start=807
  _globals['_DELETESCREENRECORDINGRESPONSE']._serialized_end=838
  _globals['_SREC']._serialized_start=841
  _globals['_SREC']._serialized_end=1422
# @@protoc_insertion_point(module_scope)
