# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/businesshours/service.proto
# Protobuf Python Version: 6.30.1
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
    1,
    '',
    'api/v1alpha1/org/businesshours/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.org.businesshours import entities_pb2 as api_dot_v1alpha1_dot_org_dot_businesshours_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,api/v1alpha1/org/businesshours/service.proto\x12\x1e\x61pi.v1alpha1.org.businesshours\x1a\x17\x61nnotations/authz.proto\x1a-api/v1alpha1/org/businesshours/entities.proto\x1a\x1cgoogle/api/annotations.proto2\xbc\r\n\x14\x42usinessHoursService\x12\xc2\x01\n\x11ListBusinessHours\x12\x38.api.v1alpha1.org.businesshours.ListBusinessHoursRequest\x1a\x39.api.v1alpha1.org.businesshours.ListBusinessHoursResponse\"8\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/businesshours/list:\x01*\x12\xbe\x01\n\x10GetBusinessHours\x12\x37.api.v1alpha1.org.businesshours.GetBusinessHoursRequest\x1a\x38.api.v1alpha1.org.businesshours.GetBusinessHoursResponse\"7\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/businesshours/get:\x01*\x12\xbe\x01\n\x10SetBusinessHours\x12\x37.api.v1alpha1.org.businesshours.SetBusinessHoursRequest\x1a\x38.api.v1alpha1.org.businesshours.SetBusinessHoursResponse\"7\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/businesshours/set:\x01*\x12\xe4\x01\n\x1a\x41\x64\x64IntervalToBusinessHours\x12\x41.api.v1alpha1.org.businesshours.AddIntervalToBusinessHoursRequest\x1a\x42.api.v1alpha1.org.businesshours.AddIntervalToBusinessHoursResponse\"?\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/org/businesshours/addinterval:\x01*\x12\xf6\x01\n\x1fRemoveIntervalFromBusinessHours\x12\x46.api.v1alpha1.org.businesshours.RemoveIntervalFromBusinessHoursRequest\x1aG.api.v1alpha1.org.businesshours.RemoveIntervalFromBusinessHoursResponse\"B\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/org/businesshours/removeinterval:\x01*\x12\xda\x01\n\x17UpdateBusinessHoursInfo\x12>.api.v1alpha1.org.businesshours.UpdateBusinessHoursInfoRequest\x1a?.api.v1alpha1.org.businesshours.UpdateBusinessHoursInfoResponse\">\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/org/businesshours/updateinfo:\x01*\x12\xca\x01\n\x13\x44\x65leteBusinessHours\x12:.api.v1alpha1.org.businesshours.DeleteBusinessHoursRequest\x1a;.api.v1alpha1.org.businesshours.DeleteBusinessHoursResponse\":\xba\xb8\x91\x02\x04\n\x02\x08\x64\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/org/businesshours/delete:\x01*\x12\xd2\x01\n\x15\x45valuateBusinessHours\x12<.api.v1alpha1.org.businesshours.EvaluateBusinessHoursRequest\x1a=.api.v1alpha1.org.businesshours.EvaluateBusinessHoursResponse\"<\xba\xb8\x91\x02\x04\n\x02\x08\x65\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/org/businesshours/evaluate:\x01*B\xce\x01\n\"com.api.v1alpha1.org.businesshoursB\x0cServiceProtoP\x01\xa2\x02\x04\x41VOB\xaa\x02\x1e\x41pi.V1alpha1.Org.Businesshours\xca\x02\x1e\x41pi\\V1alpha1\\Org\\Businesshours\xe2\x02*Api\\V1alpha1\\Org\\Businesshours\\GPBMetadata\xea\x02!Api::V1alpha1::Org::Businesshoursb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.businesshours.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.api.v1alpha1.org.businesshoursB\014ServiceProtoP\001\242\002\004AVOB\252\002\036Api.V1alpha1.Org.Businesshours\312\002\036Api\\V1alpha1\\Org\\Businesshours\342\002*Api\\V1alpha1\\Org\\Businesshours\\GPBMetadata\352\002!Api::V1alpha1::Org::Businesshours'
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['ListBusinessHours']._loaded_options = None
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['ListBusinessHours']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\002)\"$/api/v1alpha1/org/businesshours/list:\001*'
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['GetBusinessHours']._loaded_options = None
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['GetBusinessHours']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\002(\"#/api/v1alpha1/org/businesshours/get:\001*'
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['SetBusinessHours']._loaded_options = None
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['SetBusinessHours']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\002(\"#/api/v1alpha1/org/businesshours/set:\001*'
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['AddIntervalToBusinessHours']._loaded_options = None
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['AddIntervalToBusinessHours']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\0020\"+/api/v1alpha1/org/businesshours/addinterval:\001*'
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['RemoveIntervalFromBusinessHours']._loaded_options = None
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['RemoveIntervalFromBusinessHours']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\0023\"./api/v1alpha1/org/businesshours/removeinterval:\001*'
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['UpdateBusinessHoursInfo']._loaded_options = None
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['UpdateBusinessHoursInfo']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\002/\"*/api/v1alpha1/org/businesshours/updateinfo:\001*'
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['DeleteBusinessHours']._loaded_options = None
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['DeleteBusinessHours']._serialized_options = b'\272\270\221\002\004\n\002\010d\202\323\344\223\002+\"&/api/v1alpha1/org/businesshours/delete:\001*'
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['EvaluateBusinessHours']._loaded_options = None
  _globals['_BUSINESSHOURSSERVICE'].methods_by_name['EvaluateBusinessHours']._serialized_options = b'\272\270\221\002\004\n\002\010e\202\323\344\223\002-\"(/api/v1alpha1/org/businesshours/evaluate:\001*'
  _globals['_BUSINESSHOURSSERVICE']._serialized_start=183
  _globals['_BUSINESSHOURSSERVICE']._serialized_end=1907
# @@protoc_insertion_point(module_scope)
