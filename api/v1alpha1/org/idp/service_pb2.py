# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/org/idp/service.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.org.idp import entities_pb2 as api_dot_v1alpha1_dot_org_dot_idp_dot_entities__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/org/idp/service.proto\x12\x14\x61pi.v1alpha1.org.idp\x1a\x17\x61nnotations/authz.proto\x1a#api/v1alpha1/org/idp/entities.proto\x1a\x1cgoogle/api/annotations.proto2\x8f\x05\n\nIdpService\x12\x9f\x01\n\x0c\x43reateClient\x12).api.v1alpha1.org.idp.CreateClientRequest\x1a*.api.v1alpha1.org.idp.CreateClientResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/idp/client/create:\x01*\x12\x9f\x01\n\x0cUpdateClient\x12).api.v1alpha1.org.idp.UpdateClientRequest\x1a*.api.v1alpha1.org.idp.UpdateClientResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/idp/client/update:\x01*\x12\x9f\x01\n\x0c\x44\x65leteClient\x12).api.v1alpha1.org.idp.DeleteClientRequest\x1a*.api.v1alpha1.org.idp.DeleteClientResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/org/idp/client/delete:\x01*\x12\x9a\x01\n\x0bListClients\x12(.api.v1alpha1.org.idp.ListClientsRequest\x1a).api.v1alpha1.org.idp.ListClientsResponse\"6\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02&\"!/api/v1alpha1/org/idp/client/list:\x01*B\x9c\x01\n\x18\x63om.api.v1alpha1.org.idpB\x0cServiceProtoP\x01\xa2\x02\x04\x41VOI\xaa\x02\x14\x41pi.V1alpha1.Org.Idp\xca\x02\x14\x41pi\\V1alpha1\\Org\\Idp\xe2\x02 Api\\V1alpha1\\Org\\Idp\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Org::Idpb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.idp.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.org.idpB\014ServiceProtoP\001\242\002\004AVOI\252\002\024Api.V1alpha1.Org.Idp\312\002\024Api\\V1alpha1\\Org\\Idp\342\002 Api\\V1alpha1\\Org\\Idp\\GPBMetadata\352\002\027Api::V1alpha1::Org::Idp'
  _globals['_IDPSERVICE'].methods_by_name['CreateClient']._loaded_options = None
  _globals['_IDPSERVICE'].methods_by_name['CreateClient']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002(\"#/api/v1alpha1/org/idp/client/create:\001*'
  _globals['_IDPSERVICE'].methods_by_name['UpdateClient']._loaded_options = None
  _globals['_IDPSERVICE'].methods_by_name['UpdateClient']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002(\"#/api/v1alpha1/org/idp/client/update:\001*'
  _globals['_IDPSERVICE'].methods_by_name['DeleteClient']._loaded_options = None
  _globals['_IDPSERVICE'].methods_by_name['DeleteClient']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002(\"#/api/v1alpha1/org/idp/client/delete:\001*'
  _globals['_IDPSERVICE'].methods_by_name['ListClients']._loaded_options = None
  _globals['_IDPSERVICE'].methods_by_name['ListClients']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\002&\"!/api/v1alpha1/org/idp/client/list:\001*'
  _globals['_IDPSERVICE']._serialized_start=153
  _globals['_IDPSERVICE']._serialized_end=808
# @@protoc_insertion_point(module_scope)
