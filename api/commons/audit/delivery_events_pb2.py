# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/audit/delivery_events.proto
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
    'api/commons/audit/delivery_events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'api/commons/audit/delivery_events.proto\x12\x11\x61pi.commons.audit\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf9\x02\n\x14\x44\x65liveryFailureEvent\x12\x38\n\x18\x64\x65livery_definition_name\x18\x01 \x01(\x03R\x16\x64\x65liveryDefinitionName\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\'\n\x0ftransaction_sid\x18\x03 \x01(\x03R\x0etransactionSid\x12)\n\x10\x61ttachment_names\x18\x04 \x03(\tR\x0f\x61ttachmentNames\x12=\n\x0c\x66\x61ilure_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x66\x61ilureTime\x12\x32\n\x15\x66\x61ilure_error_message\x18\x06 \x01(\tR\x13\x66\x61ilureErrorMessage\x12\x1e\n\ndefinition\x18\x07 \x01(\tR\ndefinition\x12)\n\x10original_payload\x18\x08 \x01(\tR\x0foriginalPayload\"\xa3\x02\n\x14\x44\x65liverySuccessEvent\x12\x38\n\x18\x64\x65livery_definition_name\x18\x01 \x01(\tR\x16\x64\x65liveryDefinitionName\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\'\n\x0ftransaction_sid\x18\x03 \x01(\x03R\x0etransactionSid\x12)\n\x10\x61ttachment_names\x18\x04 \x03(\tR\x0f\x61ttachmentNames\x12=\n\x0csuccess_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0bsuccessTime\x12\'\n\x0fsuccess_message\x18\x06 \x01(\tR\x0esuccessMessageB\x92\x01\n\x15\x63om.api.commons.auditB\x13\x44\x65liveryEventsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.delivery_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\023DeliveryEventsProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_DELIVERYFAILUREEVENT']._serialized_start=96
  _globals['_DELIVERYFAILUREEVENT']._serialized_end=473
  _globals['_DELIVERYSUCCESSEVENT']._serialized_start=476
  _globals['_DELIVERYSUCCESSEVENT']._serialized_end=767
# @@protoc_insertion_point(module_scope)
