# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/entities/v1alpha4/tags.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'services/billing/entities/v1alpha4/tags.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-services/billing/entities/v1alpha4/tags.proto\x12\"services.billing.entities.v1alpha4\x1a\x1fgoogle/protobuf/timestamp.proto\"\xf6\x02\n\nBillingTag\x12$\n\x0e\x62illing_tag_id\x18\x01 \x01(\tR\x0c\x62illingTagId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12;\n\x0b\x63reate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12;\n\x0b\x64\x65lete_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12\x1e\n\x08\x63\x61tegory\x18\x06 \x01(\tB\x02\x18\x01R\x08\x63\x61tegory\x12W\n\x10\x62illing_category\x18\x07 \x01(\x0e\x32,.services.billing.entities.v1alpha4.CategoryR\x0f\x62illingCategory*\xed\x02\n\x08\x43\x61tegory\x12\x18\n\x14\x43\x41TEGORY_UNSPECIFIED\x10\x00\x12%\n!CATEGORY_COMMUNICATIONS_OMNI_CHAT\x10\x64\x12&\n\"CATEGORY_COMMUNICATIONS_OMNI_EMAIL\x10\x65\x12$\n CATEGORY_COMMUNICATIONS_OMNI_SMS\x10\x66\x12&\n\"CATEGORY_COMMUNICATIONS_OMNI_AGENT\x10g\x12*\n&CATEGORY_COMMUNICATIONS_OMNI_RESOURCES\x10h\x12\x33\n.CATEGORY_DATA_MANAGEMENT_COMPLIANCE_COMPLIANCE\x10\xc8\x01\x12I\nDCATEGORY_WORKFORCE_ENGAGEMENT_WORKFORCE_OPTIMIZATION_VOICE_ANALYTICS\x10\xac\x02\x42\xde\x01\n&com.services.billing.entities.v1alpha4B\tTagsProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha4\xca\x02\"Services\\Billing\\Entities\\V1alpha4\xe2\x02.Services\\Billing\\Entities\\V1alpha4\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha4b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha4.tags_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha4B\tTagsProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha4\312\002\"Services\\Billing\\Entities\\V1alpha4\342\002.Services\\Billing\\Entities\\V1alpha4\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha4'
  _globals['_BILLINGTAG'].fields_by_name['category']._loaded_options = None
  _globals['_BILLINGTAG'].fields_by_name['category']._serialized_options = b'\030\001'
  _globals['_CATEGORY']._serialized_start=496
  _globals['_CATEGORY']._serialized_end=861
  _globals['_BILLINGTAG']._serialized_start=119
  _globals['_BILLINGTAG']._serialized_end=493
# @@protoc_insertion_point(module_scope)
