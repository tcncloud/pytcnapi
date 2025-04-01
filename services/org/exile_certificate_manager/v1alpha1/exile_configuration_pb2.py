# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/org/exile_certificate_manager/v1alpha1/exile_configuration.proto
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
    'services/org/exile_certificate_manager/v1alpha1/exile_configuration.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from services.org.exile_certificate_manager.v1alpha1 import entities_pb2 as services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_entities__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIservices/org/exile_certificate_manager/v1alpha1/exile_configuration.proto\x12/services.org.exile_certificate_manager.v1alpha1\x1a google/protobuf/field_mask.proto\x1a>services/org/exile_certificate_manager/v1alpha1/entities.proto\"\xd4\x01\n\x1f\x43reateExileConfigurationRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12[\n\x04type\x18\x03 \x01(\x0e\x32G.services.org.exile_certificate_manager.v1alpha1.ExileConfigurationTypeR\x04type\x12\x1e\n\nparameters\x18\x04 \x01(\tR\nparameters\"\xd2\x01\n CreateExileConfigurationResponse\x12\x38\n\x16\x65xile_configuration_id\x18\x01 \x01(\tB\x02\x18\x01R\x14\x65xileConfigurationId\x12t\n\x13\x65xile_configuration\x18\x02 \x01(\x0b\x32\x43.services.org.exile_certificate_manager.v1alpha1.ExileConfigurationR\x12\x65xileConfiguration\"\xc7\x01\n\x1fUpdateExileConfigurationRequest\x12i\n\rconfiguration\x18\x01 \x01(\x0b\x32\x43.services.org.exile_certificate_manager.v1alpha1.ExileConfigurationR\rconfiguration\x12\x39\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\"\n UpdateExileConfigurationResponse\"W\n\x1f\x44\x65leteExileConfigurationRequest\x12\x34\n\x16\x65xile_configuration_id\x18\x01 \x01(\tR\x14\x65xileConfigurationId\"\"\n DeleteExileConfigurationResponse\"[\n\x1eListExileConfigurationsRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x99\x01\n\x1fListExileConfigurationsResponse\x12v\n\x14\x65xile_configurations\x18\x01 \x03(\x0b\x32\x43.services.org.exile_certificate_manager.v1alpha1.ExileConfigurationR\x13\x65xileConfigurationsB\xa5\x02\n3com.services.org.exile_certificate_manager.v1alpha1B\x17\x45xileConfigurationProtoP\x01\xa2\x02\x03SOE\xaa\x02-Services.Org.ExileCertificateManager.V1alpha1\xca\x02-Services\\Org\\ExileCertificateManager\\V1alpha1\xe2\x02\x39Services\\Org\\ExileCertificateManager\\V1alpha1\\GPBMetadata\xea\x02\x30Services::Org::ExileCertificateManager::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.org.exile_certificate_manager.v1alpha1.exile_configuration_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n3com.services.org.exile_certificate_manager.v1alpha1B\027ExileConfigurationProtoP\001\242\002\003SOE\252\002-Services.Org.ExileCertificateManager.V1alpha1\312\002-Services\\Org\\ExileCertificateManager\\V1alpha1\342\0029Services\\Org\\ExileCertificateManager\\V1alpha1\\GPBMetadata\352\0020Services::Org::ExileCertificateManager::V1alpha1'
  _globals['_CREATEEXILECONFIGURATIONRESPONSE'].fields_by_name['exile_configuration_id']._loaded_options = None
  _globals['_CREATEEXILECONFIGURATIONRESPONSE'].fields_by_name['exile_configuration_id']._serialized_options = b'\030\001'
  _globals['_CREATEEXILECONFIGURATIONREQUEST']._serialized_start=225
  _globals['_CREATEEXILECONFIGURATIONREQUEST']._serialized_end=437
  _globals['_CREATEEXILECONFIGURATIONRESPONSE']._serialized_start=440
  _globals['_CREATEEXILECONFIGURATIONRESPONSE']._serialized_end=650
  _globals['_UPDATEEXILECONFIGURATIONREQUEST']._serialized_start=653
  _globals['_UPDATEEXILECONFIGURATIONREQUEST']._serialized_end=852
  _globals['_UPDATEEXILECONFIGURATIONRESPONSE']._serialized_start=854
  _globals['_UPDATEEXILECONFIGURATIONRESPONSE']._serialized_end=888
  _globals['_DELETEEXILECONFIGURATIONREQUEST']._serialized_start=890
  _globals['_DELETEEXILECONFIGURATIONREQUEST']._serialized_end=977
  _globals['_DELETEEXILECONFIGURATIONRESPONSE']._serialized_start=979
  _globals['_DELETEEXILECONFIGURATIONRESPONSE']._serialized_end=1013
  _globals['_LISTEXILECONFIGURATIONSREQUEST']._serialized_start=1015
  _globals['_LISTEXILECONFIGURATIONSREQUEST']._serialized_end=1106
  _globals['_LISTEXILECONFIGURATIONSRESPONSE']._serialized_start=1109
  _globals['_LISTEXILECONFIGURATIONSRESPONSE']._serialized_end=1262
# @@protoc_insertion_point(module_scope)
