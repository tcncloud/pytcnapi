# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/entities/v1alpha3/plan.proto
# Protobuf Python Version: 5.27.1
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
    1,
    '',
    'services/billing/entities/v1alpha3/plan.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-services/billing/entities/v1alpha3/plan.proto\x12\"services.billing.entities.v1alpha3\x1a\x1fgoogle/protobuf/timestamp.proto\"\xba\x03\n\x0b\x42illingPlan\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12G\n\x04type\x18\x03 \x01(\x0e\x32\x33.services.billing.entities.v1alpha3.BillingPlanTypeR\x04type\x12\x19\n\x08is_draft\x18\x04 \x01(\x08R\x07isDraft\x12\x39\n\nstart_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12;\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12;\n\x0b\x64\x65lete_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12\x17\n\x07user_id\x18\t \x01(\tR\x06userId*n\n\x0f\x42illingPlanType\x12!\n\x1d\x42ILLING_PLAN_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x42ILLING_PLAN_TYPE_DEFAULT\x10\x01\x12\x19\n\x15\x42ILLING_PLAN_TYPE_ORG\x10\x02\x42\xde\x01\n&com.services.billing.entities.v1alpha3B\tPlanProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha3\xca\x02\"Services\\Billing\\Entities\\V1alpha3\xe2\x02.Services\\Billing\\Entities\\V1alpha3\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha3.plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha3B\tPlanProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha3\312\002\"Services\\Billing\\Entities\\V1alpha3\342\002.Services\\Billing\\Entities\\V1alpha3\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha3'
  _globals['_BILLINGPLANTYPE']._serialized_start=563
  _globals['_BILLINGPLANTYPE']._serialized_end=673
  _globals['_BILLINGPLAN']._serialized_start=119
  _globals['_BILLINGPLAN']._serialized_end=561
# @@protoc_insertion_point(module_scope)
