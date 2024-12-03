# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/org/exile_certificate_manager/v1alpha1/entities.proto
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
    'services/org/exile_certificate_manager/v1alpha1/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>services/org/exile_certificate_manager/v1alpha1/entities.proto\x12/services.org.exile_certificate_manager.v1alpha1\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc5\x03\n\x10\x45xileCertificate\x12\x30\n\x14\x65xile_certificate_id\x18\x01 \x01(\tR\x12\x65xileCertificateId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x12\n\x04hash\x18\x05 \x01(\tR\x04hash\x12\x43\n\x0f\x65xpiration_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0e\x65xpirationDate\x12?\n\rcreation_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x63reationDate\x12\x1d\n\nrequest_by\x18\x08 \x01(\tR\trequestBy\x12\x18\n\x07revoked\x18\t \x01(\x08R\x07revoked\x12\x34\n\x16\x65xile_configuration_id\x18\n \x01(\tR\x14\x65xileConfigurationId\x12)\n\x10renewal_instance\x18\x0b \x01(\x03R\x0frenewalInstance\"\x94\x02\n\x12\x45xileConfiguration\x12\x34\n\x16\x65xile_configuration_id\x18\x01 \x01(\tR\x14\x65xileConfigurationId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12[\n\x04type\x18\x05 \x01(\x0e\x32G.services.org.exile_certificate_manager.v1alpha1.ExileConfigurationTypeR\x04type\x12\x1e\n\nparameters\x18\x06 \x01(\tR\nparameters*\xdd\x02\n\x16\x45xileConfigurationType\x12(\n$EXILE_CONFIGURATION_TYPE_UNSPECIFIED\x10\x00\x12!\n\x1d\x45XILE_CONFIGURATION_TYPE_NONE\x10\x01\x12\'\n#EXILE_CONFIGURATION_TYPE_ARTIVA_HCX\x10\x02\x12&\n\"EXILE_CONFIGURATION_TYPE_ARTIVA_RM\x10\x03\x12!\n\x1d\x45XILE_CONFIGURATION_TYPE_FACS\x10\x04\x12%\n!EXILE_CONFIGURATION_TYPE_VELOSIDY\x10\x05\x12-\n)EXILE_CONFIGURATION_TYPE_LATITUDE_CLASSIC\x10\x06\x12,\n(EXILE_CONFIGURATION_TYPE_LATITUDE_LIQUID\x10\x07\x42\x9b\x02\n3com.services.org.exile_certificate_manager.v1alpha1B\rEntitiesProtoP\x01\xa2\x02\x03SOE\xaa\x02-Services.Org.ExileCertificateManager.V1alpha1\xca\x02-Services\\Org\\ExileCertificateManager\\V1alpha1\xe2\x02\x39Services\\Org\\ExileCertificateManager\\V1alpha1\\GPBMetadata\xea\x02\x30Services::Org::ExileCertificateManager::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.org.exile_certificate_manager.v1alpha1.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n3com.services.org.exile_certificate_manager.v1alpha1B\rEntitiesProtoP\001\242\002\003SOE\252\002-Services.Org.ExileCertificateManager.V1alpha1\312\002-Services\\Org\\ExileCertificateManager\\V1alpha1\342\0029Services\\Org\\ExileCertificateManager\\V1alpha1\\GPBMetadata\352\0020Services::Org::ExileCertificateManager::V1alpha1'
  _globals['_EXILECONFIGURATIONTYPE']._serialized_start=884
  _globals['_EXILECONFIGURATIONTYPE']._serialized_end=1233
  _globals['_EXILECERTIFICATE']._serialized_start=149
  _globals['_EXILECERTIFICATE']._serialized_end=602
  _globals['_EXILECONFIGURATION']._serialized_start=605
  _globals['_EXILECONFIGURATION']._serialized_end=881
# @@protoc_insertion_point(module_scope)
