# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/org/exile_certificate_manager/v1alpha1/exile_certificate.proto
# Protobuf Python Version: 5.27.3
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
    3,
    '',
    'services/org/exile_certificate_manager/v1alpha1/exile_certificate.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from services.org.exile_certificate_manager.v1alpha1 import entities_pb2 as services_dot_org_dot_exile__certificate__manager_dot_v1alpha1_dot_entities__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGservices/org/exile_certificate_manager/v1alpha1/exile_certificate.proto\x12/services.org.exile_certificate_manager.v1alpha1\x1a google/protobuf/field_mask.proto\x1a>services/org/exile_certificate_manager/v1alpha1/entities.proto\"U\n\x1d\x43reateExileCertificateRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"\\\n\x1e\x43reateExileCertificateResponse\x12:\n\x19\x65ncoded_exile_certificate\x18\x01 \x01(\tR\x17\x65ncodedExileCertificate\"Q\n\x1dRevokeExileCertificateRequest\x12\x30\n\x14\x65xile_certificate_id\x18\x01 \x01(\tR\x12\x65xileCertificateId\" \n\x1eRevokeExileCertificateResponse\"\x89\x01\n\x1f\x41ssignExileConfigurationRequest\x12\x30\n\x14\x65xile_certificate_id\x18\x01 \x01(\tR\x12\x65xileCertificateId\x12\x34\n\x16\x65xile_configuration_id\x18\x02 \x01(\tR\x14\x65xileConfigurationId\"\"\n AssignExileConfigurationResponse\"U\n!UnassignExileConfigurationRequest\x12\x30\n\x14\x65xile_certificate_id\x18\x01 \x01(\tR\x12\x65xileCertificateId\"$\n\"UnassignExileConfigurationResponse\"Y\n\x1cListExileCertificatesRequest\x12\x39\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x91\x01\n\x1dListExileCertificatesResponse\x12p\n\x12\x65xile_certificates\x18\x01 \x03(\x0b\x32\x41.services.org.exile_certificate_manager.v1alpha1.ExileCertificateR\x11\x65xileCertificatesB\xa3\x02\n3com.services.org.exile_certificate_manager.v1alpha1B\x15\x45xileCertificateProtoP\x01\xa2\x02\x03SOE\xaa\x02-Services.Org.ExileCertificateManager.V1alpha1\xca\x02-Services\\Org\\ExileCertificateManager\\V1alpha1\xe2\x02\x39Services\\Org\\ExileCertificateManager\\V1alpha1\\GPBMetadata\xea\x02\x30Services::Org::ExileCertificateManager::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.org.exile_certificate_manager.v1alpha1.exile_certificate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n3com.services.org.exile_certificate_manager.v1alpha1B\025ExileCertificateProtoP\001\242\002\003SOE\252\002-Services.Org.ExileCertificateManager.V1alpha1\312\002-Services\\Org\\ExileCertificateManager\\V1alpha1\342\0029Services\\Org\\ExileCertificateManager\\V1alpha1\\GPBMetadata\352\0020Services::Org::ExileCertificateManager::V1alpha1'
  _globals['_CREATEEXILECERTIFICATEREQUEST']._serialized_start=222
  _globals['_CREATEEXILECERTIFICATEREQUEST']._serialized_end=307
  _globals['_CREATEEXILECERTIFICATERESPONSE']._serialized_start=309
  _globals['_CREATEEXILECERTIFICATERESPONSE']._serialized_end=401
  _globals['_REVOKEEXILECERTIFICATEREQUEST']._serialized_start=403
  _globals['_REVOKEEXILECERTIFICATEREQUEST']._serialized_end=484
  _globals['_REVOKEEXILECERTIFICATERESPONSE']._serialized_start=486
  _globals['_REVOKEEXILECERTIFICATERESPONSE']._serialized_end=518
  _globals['_ASSIGNEXILECONFIGURATIONREQUEST']._serialized_start=521
  _globals['_ASSIGNEXILECONFIGURATIONREQUEST']._serialized_end=658
  _globals['_ASSIGNEXILECONFIGURATIONRESPONSE']._serialized_start=660
  _globals['_ASSIGNEXILECONFIGURATIONRESPONSE']._serialized_end=694
  _globals['_UNASSIGNEXILECONFIGURATIONREQUEST']._serialized_start=696
  _globals['_UNASSIGNEXILECONFIGURATIONREQUEST']._serialized_end=781
  _globals['_UNASSIGNEXILECONFIGURATIONRESPONSE']._serialized_start=783
  _globals['_UNASSIGNEXILECONFIGURATIONRESPONSE']._serialized_end=819
  _globals['_LISTEXILECERTIFICATESREQUEST']._serialized_start=821
  _globals['_LISTEXILECERTIFICATESREQUEST']._serialized_end=910
  _globals['_LISTEXILECERTIFICATESRESPONSE']._serialized_start=913
  _globals['_LISTEXILECERTIFICATESRESPONSE']._serialized_end=1058
# @@protoc_insertion_point(module_scope)
