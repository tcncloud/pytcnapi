# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/idp/entities.proto
# Protobuf Python Version: 5.29.2
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
    2,
    '',
    'api/v1alpha1/org/idp/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.org import idp_pb2 as api_dot_commons_dot_org_dot_idp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/org/idp/entities.proto\x12\x14\x61pi.v1alpha1.org.idp\x1a\x19\x61pi/commons/org/idp.proto\"I\n\x13\x43reateClientRequest\x12\x32\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x1a.api.commons.org.IdpClientR\x06\x63lient\"q\n\x14\x43reateClientResponse\x12%\n\x0e\x61lready_exists\x18\x01 \x01(\x08R\ralreadyExists\x12\x32\n\x06\x63lient\x18\x02 \x01(\x0b\x32\x1a.api.commons.org.IdpClientR\x06\x63lient\"%\n\x13\x44\x65leteClientRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"3\n\x14\x44\x65leteClientResponse\x12\x1b\n\tnot_found\x18\x01 \x01(\x08R\x08notFound\"I\n\x13UpdateClientRequest\x12\x32\n\x06\x63lient\x18\x01 \x01(\x0b\x32\x1a.api.commons.org.IdpClientR\x06\x63lient\"3\n\x14UpdateClientResponse\x12\x1b\n\tnot_found\x18\x01 \x01(\x08R\x08notFound\"\x14\n\x12ListClientsRequest\"K\n\x13ListClientsResponse\x12\x34\n\x07\x63lients\x18\x01 \x03(\x0b\x32\x1a.api.commons.org.IdpClientR\x07\x63lientsB\x9d\x01\n\x18\x63om.api.v1alpha1.org.idpB\rEntitiesProtoP\x01\xa2\x02\x04\x41VOI\xaa\x02\x14\x41pi.V1alpha1.Org.Idp\xca\x02\x14\x41pi\\V1alpha1\\Org\\Idp\xe2\x02 Api\\V1alpha1\\Org\\Idp\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Org::Idpb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.idp.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.org.idpB\rEntitiesProtoP\001\242\002\004AVOI\252\002\024Api.V1alpha1.Org.Idp\312\002\024Api\\V1alpha1\\Org\\Idp\342\002 Api\\V1alpha1\\Org\\Idp\\GPBMetadata\352\002\027Api::V1alpha1::Org::Idp'
  _globals['_CREATECLIENTREQUEST']._serialized_start=88
  _globals['_CREATECLIENTREQUEST']._serialized_end=161
  _globals['_CREATECLIENTRESPONSE']._serialized_start=163
  _globals['_CREATECLIENTRESPONSE']._serialized_end=276
  _globals['_DELETECLIENTREQUEST']._serialized_start=278
  _globals['_DELETECLIENTREQUEST']._serialized_end=315
  _globals['_DELETECLIENTRESPONSE']._serialized_start=317
  _globals['_DELETECLIENTRESPONSE']._serialized_end=368
  _globals['_UPDATECLIENTREQUEST']._serialized_start=370
  _globals['_UPDATECLIENTREQUEST']._serialized_end=443
  _globals['_UPDATECLIENTRESPONSE']._serialized_start=445
  _globals['_UPDATECLIENTRESPONSE']._serialized_end=496
  _globals['_LISTCLIENTSREQUEST']._serialized_start=498
  _globals['_LISTCLIENTSREQUEST']._serialized_end=518
  _globals['_LISTCLIENTSRESPONSE']._serialized_start=520
  _globals['_LISTCLIENTSRESPONSE']._serialized_end=595
# @@protoc_insertion_point(module_scope)
