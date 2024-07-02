# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/notifier/service.proto
# Protobuf Python Version: 5.27.2
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
    2,
    '',
    'api/v1alpha1/vanalytics/notifier/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.api/v1alpha1/vanalytics/notifier/service.proto\x12 api.v1alpha1.vanalytics.notifier\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"/\n\x10GetNotifyRequest\x12\x1b\n\tnotify_id\x18\x01 \x01(\tR\x08notifyId\"\xdd\x01\n\x06Notify\x12\x1b\n\tnotify_id\x18\x01 \x01(\tR\x08notifyId\x12\x30\n\x14start_transcript_sid\x18\x02 \x01(\x03R\x12startTranscriptSid\x12,\n\x12\x65nd_transcript_sid\x18\x03 \x01(\x03R\x10\x65ndTranscriptSid\x12\x19\n\x08\x66lag_sid\x18\x04 \x01(\x03R\x07\x66lagSid\x12;\n\x0b\x63reate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime2\xc1\x01\n\x08Notifier\x12\xb4\x01\n\tGetNotify\x12\x32.api.v1alpha1.vanalytics.notifier.GetNotifyRequest\x1a(.api.v1alpha1.vanalytics.notifier.Notify\"I\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/vanalytics/notifier/notifier/getnotify:\x01*B\xd8\x01\n$com.api.v1alpha1.vanalytics.notifierB\x0cServiceProtoP\x01\xa2\x02\x04\x41VVN\xaa\x02 Api.V1alpha1.Vanalytics.Notifier\xca\x02 Api\\V1alpha1\\Vanalytics\\Notifier\xe2\x02,Api\\V1alpha1\\Vanalytics\\Notifier\\GPBMetadata\xea\x02#Api::V1alpha1::Vanalytics::Notifierb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.notifier.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.api.v1alpha1.vanalytics.notifierB\014ServiceProtoP\001\242\002\004AVVN\252\002 Api.V1alpha1.Vanalytics.Notifier\312\002 Api\\V1alpha1\\Vanalytics\\Notifier\342\002,Api\\V1alpha1\\Vanalytics\\Notifier\\GPBMetadata\352\002#Api::V1alpha1::Vanalytics::Notifier'
  _globals['_NOTIFIER'].methods_by_name['GetNotify']._loaded_options = None
  _globals['_NOTIFIER'].methods_by_name['GetNotify']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0029\"4/api/v1alpha1/vanalytics/notifier/notifier/getnotify:\001*'
  _globals['_GETNOTIFYREQUEST']._serialized_start=172
  _globals['_GETNOTIFYREQUEST']._serialized_end=219
  _globals['_NOTIFY']._serialized_start=222
  _globals['_NOTIFY']._serialized_end=443
  _globals['_NOTIFIER']._serialized_start=446
  _globals['_NOTIFIER']._serialized_end=639
# @@protoc_insertion_point(module_scope)
