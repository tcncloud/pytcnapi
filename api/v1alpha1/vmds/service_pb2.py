# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/vmds/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61pi/v1alpha1/vmds/service.proto\x12\x11\x61pi.v1alpha1.vmds\x1a\x17\x61nnotations/authz.proto\x1a\x15\x61pi/commons/acd.proto\x1a\x1cgoogle/api/annotations.proto\"\x8c\x02\n DownloadSpecifiedMessagesRequest\x12^\n\x08messages\x18\x01 \x03(\x0b\x32\x42.api.v1alpha1.vmds.DownloadSpecifiedMessagesRequest.MessageRequestR\x08messages\x1a\x87\x01\n\x0eMessageRequest\x12\x19\n\x08mail_box\x18\x01 \x01(\tR\x07mailBox\x12\x1d\n\ncaller_sid\x18\x02 \x01(\tR\tcallerSid\x12;\n\x0b\x63\x61ller_type\x18\x03 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\ncallerType\"5\n!DownloadSpecifiedMessagesResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url2\xd9\x01\n\x0bVmdsService\x12\xc9\x01\n\x19\x44ownloadSpecifiedMessages\x12\x33.api.v1alpha1.vmds.DownloadSpecifiedMessagesRequest\x1a\x34.api.v1alpha1.vmds.DownloadSpecifiedMessagesResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xf9\n\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/vmds/downloadspecifiedmessages:\x01*B\x8b\x01\n\x15\x63om.api.v1alpha1.vmdsB\x0cServiceProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x11\x41pi.V1alpha1.Vmds\xca\x02\x11\x41pi\\V1alpha1\\Vmds\xe2\x02\x1d\x41pi\\V1alpha1\\Vmds\\GPBMetadata\xea\x02\x13\x41pi::V1alpha1::Vmdsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vmds.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.api.v1alpha1.vmdsB\014ServiceProtoP\001\242\002\003AVV\252\002\021Api.V1alpha1.Vmds\312\002\021Api\\V1alpha1\\Vmds\342\002\035Api\\V1alpha1\\Vmds\\GPBMetadata\352\002\023Api::V1alpha1::Vmds'
  _VMDSSERVICE.methods_by_name['DownloadSpecifiedMessages']._options = None
  _VMDSSERVICE.methods_by_name['DownloadSpecifiedMessages']._serialized_options = b'\272\270\221\002\005\n\003\010\371\n\202\323\344\223\0021\",/api/v1alpha1/vmds/downloadspecifiedmessages:\001*'
  _globals['_DOWNLOADSPECIFIEDMESSAGESREQUEST']._serialized_start=133
  _globals['_DOWNLOADSPECIFIEDMESSAGESREQUEST']._serialized_end=401
  _globals['_DOWNLOADSPECIFIEDMESSAGESREQUEST_MESSAGEREQUEST']._serialized_start=266
  _globals['_DOWNLOADSPECIFIEDMESSAGESREQUEST_MESSAGEREQUEST']._serialized_end=401
  _globals['_DOWNLOADSPECIFIEDMESSAGESRESPONSE']._serialized_start=403
  _globals['_DOWNLOADSPECIFIEDMESSAGESRESPONSE']._serialized_end=456
  _globals['_VMDSSERVICE']._serialized_start=459
  _globals['_VMDSSERVICE']._serialized_end=676
# @@protoc_insertion_point(module_scope)
