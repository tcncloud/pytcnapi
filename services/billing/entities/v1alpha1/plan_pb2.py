# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/entities/v1alpha1/plan.proto
# Protobuf Python Version: 5.29.1
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
    1,
    '',
    'services/billing/entities/v1alpha1/plan.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha1 import rates_pb2 as services_dot_billing_dot_entities_dot_v1alpha1_dot_rates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-services/billing/entities/v1alpha1/plan.proto\x12\"services.billing.entities.v1alpha1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a.services/billing/entities/v1alpha1/rates.proto\"\xd1\x01\n\x13\x42illingPlanSnapshot\x12\x39\n\nstart_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartDate\x12\x35\n\x08\x65nd_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndDate\x12H\n\x05rates\x18\x03 \x03(\x0b\x32\x32.services.billing.entities.v1alpha1.RateDefinitionR\x05rates\"\xa9\x04\n\x0b\x42illingPlan\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12;\n\x0b\x63reate_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12;\n\x0b\x64\x65lete_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12.\n\x13rate_definition_ids\x18\x07 \x03(\tR\x11rateDefinitionIds\x12M\n\x06status\x18\x08 \x01(\x0e\x32\x35.services.billing.entities.v1alpha1.BillingPlanStatusR\x06status\x12J\n\x11\x61\x63tual_start_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x0f\x61\x63tualStartTime*|\n\x11\x42illingPlanStatus\x12#\n\x1f\x42ILLING_PLAN_STATUS_UNSPECIFIED\x10\x00\x12 \n\x1c\x42ILLING_PLAN_STATUS_CREATING\x10\x64\x12 \n\x1b\x42ILLING_PLAN_STATUS_CREATED\x10\xc8\x01\x42\xde\x01\n&com.services.billing.entities.v1alpha1B\tPlanProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha1\xca\x02\"Services\\Billing\\Entities\\V1alpha1\xe2\x02.Services\\Billing\\Entities\\V1alpha1\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha1.plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha1B\tPlanProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha1\312\002\"Services\\Billing\\Entities\\V1alpha1\342\002.Services\\Billing\\Entities\\V1alpha1\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha1'
  _globals['_BILLINGPLAN'].fields_by_name['actual_start_time']._loaded_options = None
  _globals['_BILLINGPLAN'].fields_by_name['actual_start_time']._serialized_options = b'\030\001'
  _globals['_BILLINGPLANSTATUS']._serialized_start=934
  _globals['_BILLINGPLANSTATUS']._serialized_end=1058
  _globals['_BILLINGPLANSNAPSHOT']._serialized_start=167
  _globals['_BILLINGPLANSNAPSHOT']._serialized_end=376
  _globals['_BILLINGPLAN']._serialized_start=379
  _globals['_BILLINGPLAN']._serialized_end=932
# @@protoc_insertion_point(module_scope)
