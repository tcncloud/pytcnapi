# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/agenttraining/support_service.proto
# Protobuf Python Version: 5.29.3
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
    3,
    '',
    'api/v1alpha1/agenttraining/support_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.agenttraining import learning_opportunity_pb2 as api_dot_v1alpha1_dot_agenttraining_dot_learning__opportunity__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0api/v1alpha1/agenttraining/support_service.proto\x12\x1a\x61pi.v1alpha1.agenttraining\x1a\x17\x61nnotations/authz.proto\x1a\x35\x61pi/v1alpha1/agenttraining/learning_opportunity.proto\x1a\x1cgoogle/api/annotations.proto2\xcd\x04\n\x1b\x41gentTrainingSupportService\x12\x95\x02\n ListLearningOpportunitiesByOrgId\x12\x43.api.v1alpha1.agenttraining.ListLearningOpportunitiesByOrgIdRequest\x1a=.api.v1alpha1.agenttraining.ListLearningOpportunitiesResponse\"m\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02]\"X/api/v1alpha1/agenttraining/agenttrainingsupportservice/listlearningopportunitiesbyorgid:\x01*\x12\x95\x02\n DeleteLearningOpportunityByOrgId\x12\x43.api.v1alpha1.agenttraining.DeleteLearningOpportunityByOrgIdRequest\x1a=.api.v1alpha1.agenttraining.DeleteLearningOpportunityResponse\"m\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02]\"X/api/v1alpha1/agenttraining/agenttrainingsupportservice/deletelearningopportunitybyorgid:\x01*B\xbf\x01\n\x1e\x63om.api.v1alpha1.agenttrainingB\x13SupportServiceProtoP\x01\xa2\x02\x03\x41VA\xaa\x02\x1a\x41pi.V1alpha1.Agenttraining\xca\x02\x1a\x41pi\\V1alpha1\\Agenttraining\xe2\x02&Api\\V1alpha1\\Agenttraining\\GPBMetadata\xea\x02\x1c\x41pi::V1alpha1::Agenttrainingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.agenttraining.support_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.api.v1alpha1.agenttrainingB\023SupportServiceProtoP\001\242\002\003AVA\252\002\032Api.V1alpha1.Agenttraining\312\002\032Api\\V1alpha1\\Agenttraining\342\002&Api\\V1alpha1\\Agenttraining\\GPBMetadata\352\002\034Api::V1alpha1::Agenttraining'
  _globals['_AGENTTRAININGSUPPORTSERVICE'].methods_by_name['ListLearningOpportunitiesByOrgId']._loaded_options = None
  _globals['_AGENTTRAININGSUPPORTSERVICE'].methods_by_name['ListLearningOpportunitiesByOrgId']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002]\"X/api/v1alpha1/agenttraining/agenttrainingsupportservice/listlearningopportunitiesbyorgid:\001*'
  _globals['_AGENTTRAININGSUPPORTSERVICE'].methods_by_name['DeleteLearningOpportunityByOrgId']._loaded_options = None
  _globals['_AGENTTRAININGSUPPORTSERVICE'].methods_by_name['DeleteLearningOpportunityByOrgId']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002]\"X/api/v1alpha1/agenttraining/agenttrainingsupportservice/deletelearningopportunitybyorgid:\001*'
  _globals['_AGENTTRAININGSUPPORTSERVICE']._serialized_start=191
  _globals['_AGENTTRAININGSUPPORTSERVICE']._serialized_end=780
# @@protoc_insertion_point(module_scope)
