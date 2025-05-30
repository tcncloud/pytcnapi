# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/agenttraining/service.proto
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
    'api/v1alpha1/agenttraining/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.agenttraining import learning_opportunity_pb2 as api_dot_v1alpha1_dot_agenttraining_dot_learning__opportunity__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(api/v1alpha1/agenttraining/service.proto\x12\x1a\x61pi.v1alpha1.agenttraining\x1a\x17\x61nnotations/authz.proto\x1a\x35\x61pi/v1alpha1/agenttraining/learning_opportunity.proto\x1a\x1cgoogle/api/annotations.proto2\xd1\x11\n\x14\x41gentTrainingService\x12\xf9\x01\n\x19\x43reateLearningOpportunity\x12<.api.v1alpha1.agenttraining.CreateLearningOpportunityRequest\x1a=.api.v1alpha1.agenttraining.CreateLearningOpportunityResponse\"_\xba\xb8\x91\x02\x05\n\x03\x08\xc4\x0c\x82\xd3\xe4\x93\x02O\"J/api/v1alpha1/agenttraining/agenttrainingservice/createlearningopportunity:\x01*\x12\xf9\x01\n\x19ListLearningOpportunities\x12<.api.v1alpha1.agenttraining.ListLearningOpportunitiesRequest\x1a=.api.v1alpha1.agenttraining.ListLearningOpportunitiesResponse\"_\xba\xb8\x91\x02\x05\n\x03\x08\xc4\x0c\x82\xd3\xe4\x93\x02O\"J/api/v1alpha1/agenttraining/agenttrainingservice/listlearningopportunities:\x01*\x12\x8d\x02\n\x1eListAgentLearningOpportunities\x12\x41.api.v1alpha1.agenttraining.ListAgentLearningOpportunitiesRequest\x1a\x42.api.v1alpha1.agenttraining.ListAgentLearningOpportunitiesResponse\"d\xba\xb8\x91\x02\x05\n\x03\x08\xd4\x02\x82\xd3\xe4\x93\x02T\"O/api/v1alpha1/agenttraining/agenttrainingservice/listagentlearningopportunities:\x01*\x12\x95\x02\n CompleteAgentLearningOpportunity\x12\x43.api.v1alpha1.agenttraining.CompleteAgentLearningOpportunityRequest\x1a\x44.api.v1alpha1.agenttraining.CompleteAgentLearningOpportunityResponse\"f\xba\xb8\x91\x02\x05\n\x03\x08\xd4\x02\x82\xd3\xe4\x93\x02V\"Q/api/v1alpha1/agenttraining/agenttrainingservice/completeagentlearningopportunity:\x01*\x12\xcd\x01\n\x0eListDashboards\x12\x31.api.v1alpha1.agenttraining.ListDashboardsRequest\x1a\x32.api.v1alpha1.agenttraining.ListDashboardsResponse\"T\xba\xb8\x91\x02\x05\n\x03\x08\xd4\x02\x82\xd3\xe4\x93\x02\x44\"?/api/v1alpha1/agenttraining/agenttrainingservice/listdashboards:\x01*\x12\xe0\x01\n\x15ListManagerDashboards\x12\x31.api.v1alpha1.agenttraining.ListDashboardsRequest\x1a\x32.api.v1alpha1.agenttraining.ListDashboardsResponse\"`\xba\xb8\x91\x02\n\n\x03\x08\xc0\x0c\n\x03\x08\xc1\x0c\x82\xd3\xe4\x93\x02K\"F/api/v1alpha1/agenttraining/agenttrainingservice/listmanagerdashboards:\x01*\x12\xf9\x01\n\x19UpdateLearningOpportunity\x12<.api.v1alpha1.agenttraining.UpdateLearningOpportunityRequest\x1a=.api.v1alpha1.agenttraining.UpdateLearningOpportunityResponse\"_\xba\xb8\x91\x02\x05\n\x03\x08\xc4\x0c\x82\xd3\xe4\x93\x02O\"J/api/v1alpha1/agenttraining/agenttrainingservice/updatelearningopportunity:\x01*\x12\xf9\x01\n\x19\x44\x65leteLearningOpportunity\x12<.api.v1alpha1.agenttraining.DeleteLearningOpportunityRequest\x1a=.api.v1alpha1.agenttraining.DeleteLearningOpportunityResponse\"_\xba\xb8\x91\x02\x05\n\x03\x08\xc4\x0c\x82\xd3\xe4\x93\x02O\"J/api/v1alpha1/agenttraining/agenttrainingservice/deletelearningopportunity:\x01*\x12\xed\x01\n\x16GetLearningOpportunity\x12\x39.api.v1alpha1.agenttraining.GetLearningOpportunityRequest\x1a:.api.v1alpha1.agenttraining.GetLearningOpportunityResponse\"\\\xba\xb8\x91\x02\x05\n\x03\x08\xc4\x0c\x82\xd3\xe4\x93\x02L\"G/api/v1alpha1/agenttraining/agenttrainingservice/getlearningopportunity:\x01*B\xb8\x01\n\x1e\x63om.api.v1alpha1.agenttrainingB\x0cServiceProtoP\x01\xa2\x02\x03\x41VA\xaa\x02\x1a\x41pi.V1alpha1.Agenttraining\xca\x02\x1a\x41pi\\V1alpha1\\Agenttraining\xe2\x02&Api\\V1alpha1\\Agenttraining\\GPBMetadata\xea\x02\x1c\x41pi::V1alpha1::Agenttrainingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.agenttraining.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.api.v1alpha1.agenttrainingB\014ServiceProtoP\001\242\002\003AVA\252\002\032Api.V1alpha1.Agenttraining\312\002\032Api\\V1alpha1\\Agenttraining\342\002&Api\\V1alpha1\\Agenttraining\\GPBMetadata\352\002\034Api::V1alpha1::Agenttraining'
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['CreateLearningOpportunity']._loaded_options = None
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['CreateLearningOpportunity']._serialized_options = b'\272\270\221\002\005\n\003\010\304\014\202\323\344\223\002O\"J/api/v1alpha1/agenttraining/agenttrainingservice/createlearningopportunity:\001*'
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['ListLearningOpportunities']._loaded_options = None
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['ListLearningOpportunities']._serialized_options = b'\272\270\221\002\005\n\003\010\304\014\202\323\344\223\002O\"J/api/v1alpha1/agenttraining/agenttrainingservice/listlearningopportunities:\001*'
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['ListAgentLearningOpportunities']._loaded_options = None
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['ListAgentLearningOpportunities']._serialized_options = b'\272\270\221\002\005\n\003\010\324\002\202\323\344\223\002T\"O/api/v1alpha1/agenttraining/agenttrainingservice/listagentlearningopportunities:\001*'
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['CompleteAgentLearningOpportunity']._loaded_options = None
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['CompleteAgentLearningOpportunity']._serialized_options = b'\272\270\221\002\005\n\003\010\324\002\202\323\344\223\002V\"Q/api/v1alpha1/agenttraining/agenttrainingservice/completeagentlearningopportunity:\001*'
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['ListDashboards']._loaded_options = None
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['ListDashboards']._serialized_options = b'\272\270\221\002\005\n\003\010\324\002\202\323\344\223\002D\"?/api/v1alpha1/agenttraining/agenttrainingservice/listdashboards:\001*'
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['ListManagerDashboards']._loaded_options = None
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['ListManagerDashboards']._serialized_options = b'\272\270\221\002\n\n\003\010\300\014\n\003\010\301\014\202\323\344\223\002K\"F/api/v1alpha1/agenttraining/agenttrainingservice/listmanagerdashboards:\001*'
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['UpdateLearningOpportunity']._loaded_options = None
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['UpdateLearningOpportunity']._serialized_options = b'\272\270\221\002\005\n\003\010\304\014\202\323\344\223\002O\"J/api/v1alpha1/agenttraining/agenttrainingservice/updatelearningopportunity:\001*'
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['DeleteLearningOpportunity']._loaded_options = None
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['DeleteLearningOpportunity']._serialized_options = b'\272\270\221\002\005\n\003\010\304\014\202\323\344\223\002O\"J/api/v1alpha1/agenttraining/agenttrainingservice/deletelearningopportunity:\001*'
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['GetLearningOpportunity']._loaded_options = None
  _globals['_AGENTTRAININGSERVICE'].methods_by_name['GetLearningOpportunity']._serialized_options = b'\272\270\221\002\005\n\003\010\304\014\202\323\344\223\002L\"G/api/v1alpha1/agenttraining/agenttrainingservice/getlearningopportunity:\001*'
  _globals['_AGENTTRAININGSERVICE']._serialized_start=183
  _globals['_AGENTTRAININGSERVICE']._serialized_end=2440
# @@protoc_insertion_point(module_scope)
