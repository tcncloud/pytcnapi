# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/omnichannel/api/entities/v1alpha1/flows.proto
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
    'services/omnichannel/api/entities/v1alpha1/flows.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6services/omnichannel/api/entities/v1alpha1/flows.proto\x12*services.omnichannel.api.entities.v1alpha1\"\\\n\x0b\x46lowPayload\x12M\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x35.services.omnichannel.api.entities.v1alpha1.FlowFieldR\x06\x66ields\"\x84\x01\n\tFlowField\x12M\n\x04name\x18\x01 \x01(\x0e\x32\x39.services.omnichannel.api.entities.v1alpha1.FlowFieldNameR\x04name\x12\x1f\n\nuser_input\x18\x64 \x01(\tH\x00R\tuserInputB\x07\n\x05value*F\n\rFlowFieldName\x12\x1a\n\x16\x46IELD_NAME_UNSPECIFIED\x10\x00\x12\x19\n\x15\x46IELD_NAME_USER_INPUT\x10\x01\x42\x89\x02\n.com.services.omnichannel.api.entities.v1alpha1B\nFlowsProtoP\x01\xa2\x02\x04SOAE\xaa\x02*Services.Omnichannel.Api.Entities.V1alpha1\xca\x02*Services\\Omnichannel\\Api\\Entities\\V1alpha1\xe2\x02\x36Services\\Omnichannel\\Api\\Entities\\V1alpha1\\GPBMetadata\xea\x02.Services::Omnichannel::Api::Entities::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.omnichannel.api.entities.v1alpha1.flows_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n.com.services.omnichannel.api.entities.v1alpha1B\nFlowsProtoP\001\242\002\004SOAE\252\002*Services.Omnichannel.Api.Entities.V1alpha1\312\002*Services\\Omnichannel\\Api\\Entities\\V1alpha1\342\0026Services\\Omnichannel\\Api\\Entities\\V1alpha1\\GPBMetadata\352\002.Services::Omnichannel::Api::Entities::V1alpha1'
  _globals['_FLOWFIELDNAME']._serialized_start=331
  _globals['_FLOWFIELDNAME']._serialized_end=401
  _globals['_FLOWPAYLOAD']._serialized_start=102
  _globals['_FLOWPAYLOAD']._serialized_end=194
  _globals['_FLOWFIELD']._serialized_start=197
  _globals['_FLOWFIELD']._serialized_end=329
# @@protoc_insertion_point(module_scope)
