# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/audit/compliance_events.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)api/commons/audit/compliance_events.proto\x12\x11\x61pi.commons.audit\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb3\x01\n\x17\x43omplianceRndQueryEvent\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12!\n\x0cphone_number\x18\x02 \x01(\tR\x0bphoneNumber\x12\x16\n\x06result\x18\x03 \x01(\tR\x06result\x12\x46\n\x11\x64\x61te_last_contact\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0f\x64\x61teLastContactB\x94\x01\n\x15\x63om.api.commons.auditB\x15\x43omplianceEventsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.compliance_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\025ComplianceEventsProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_COMPLIANCERNDQUERYEVENT']._serialized_start=98
  _globals['_COMPLIANCERNDQUERYEVENT']._serialized_end=277
# @@protoc_insertion_point(module_scope)
