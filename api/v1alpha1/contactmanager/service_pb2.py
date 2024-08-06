# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/contactmanager/service.proto
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
    'api/v1alpha1/contactmanager/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.contactmanager import contactmanager_pb2 as api_dot_v1alpha1_dot_contactmanager_dot_contactmanager__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)api/v1alpha1/contactmanager/service.proto\x12\x1b\x61pi.v1alpha1.contactmanager\x1a\x17\x61nnotations/authz.proto\x1a\x30\x61pi/v1alpha1/contactmanager/contactmanager.proto\x1a\x1cgoogle/api/annotations.proto2\xeb\x0b\n\x0e\x43ontactManager\x12\xca\x01\n\x0eGetContactList\x12\x32.api.v1alpha1.contactmanager.GetContactListRequest\x1a\x33.api.v1alpha1.contactmanager.GetContactListResponse\"O\xba\xb8\x91\x02\x05\n\x03\x08\xec\'\x82\xd3\xe4\x93\x02?\":/api/v1alpha1/contactmanager/contactmanager/getcontactlist:\x01*\x12\xe2\x01\n\x14ListContactEntryList\x12\x38.api.v1alpha1.contactmanager.ListContactEntryListRequest\x1a\x39.api.v1alpha1.contactmanager.ListContactEntryListResponse\"U\xba\xb8\x91\x02\x05\n\x03\x08\xec\'\x82\xd3\xe4\x93\x02\x45\"@/api/v1alpha1/contactmanager/contactmanager/listcontactentrylist:\x01*\x12\xda\x01\n\x12GetEncContactEntry\x12\x36.api.v1alpha1.contactmanager.GetEncContactEntryRequest\x1a\x37.api.v1alpha1.contactmanager.GetEncContactEntryResponse\"S\xba\xb8\x91\x02\x05\n\x03\x08\xec\'\x82\xd3\xe4\x93\x02\x43\">/api/v1alpha1/contactmanager/contactmanager/getenccontactentry:\x01*\x12\xe6\x01\n\x15GetKYCEncContactEntry\x12\x39.api.v1alpha1.contactmanager.GetKYCEncContactEntryRequest\x1a:.api.v1alpha1.contactmanager.GetKYCEncContactEntryResponse\"V\xba\xb8\x91\x02\x05\n\x03\x08\xed\'\x82\xd3\xe4\x93\x02\x46\"A/api/v1alpha1/contactmanager/contactmanager/getkycenccontactentry:\x01*\x12\xba\x01\n\nGetKYCKeys\x12..api.v1alpha1.contactmanager.GetKYCKeysRequest\x1a/.api.v1alpha1.contactmanager.GetKYCKeysResponse\"K\xba\xb8\x91\x02\x05\n\x03\x08\xed\'\x82\xd3\xe4\x93\x02;\"6/api/v1alpha1/contactmanager/contactmanager/getkyckeys:\x01*\x12\xce\x01\n\x0f\x41\x64\x64\x43ontactEntry\x12\x33.api.v1alpha1.contactmanager.AddContactEntryRequest\x1a\x34.api.v1alpha1.contactmanager.AddContactEntryResponse\"P\xba\xb8\x91\x02\x05\n\x03\x08\xec\'\x82\xd3\xe4\x93\x02@\";/api/v1alpha1/contactmanager/contactmanager/addcontactentry:\x01*\x12\xd2\x01\n\x10\x45\x64itContactEntry\x12\x34.api.v1alpha1.contactmanager.EditContactEntryRequest\x1a\x35.api.v1alpha1.contactmanager.EditContactEntryResponse\"Q\xba\xb8\x91\x02\x05\n\x03\x08\xec\'\x82\xd3\xe4\x93\x02\x41\"</api/v1alpha1/contactmanager/contactmanager/editcontactentry:\x01*B\xbd\x01\n\x1f\x63om.api.v1alpha1.contactmanagerB\x0cServiceProtoP\x01\xa2\x02\x03\x41VC\xaa\x02\x1b\x41pi.V1alpha1.Contactmanager\xca\x02\x1b\x41pi\\V1alpha1\\Contactmanager\xe2\x02\'Api\\V1alpha1\\Contactmanager\\GPBMetadata\xea\x02\x1d\x41pi::V1alpha1::Contactmanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.contactmanager.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.api.v1alpha1.contactmanagerB\014ServiceProtoP\001\242\002\003AVC\252\002\033Api.V1alpha1.Contactmanager\312\002\033Api\\V1alpha1\\Contactmanager\342\002\'Api\\V1alpha1\\Contactmanager\\GPBMetadata\352\002\035Api::V1alpha1::Contactmanager'
  _globals['_CONTACTMANAGER'].methods_by_name['GetContactList']._loaded_options = None
  _globals['_CONTACTMANAGER'].methods_by_name['GetContactList']._serialized_options = b'\272\270\221\002\005\n\003\010\354\'\202\323\344\223\002?\":/api/v1alpha1/contactmanager/contactmanager/getcontactlist:\001*'
  _globals['_CONTACTMANAGER'].methods_by_name['ListContactEntryList']._loaded_options = None
  _globals['_CONTACTMANAGER'].methods_by_name['ListContactEntryList']._serialized_options = b'\272\270\221\002\005\n\003\010\354\'\202\323\344\223\002E\"@/api/v1alpha1/contactmanager/contactmanager/listcontactentrylist:\001*'
  _globals['_CONTACTMANAGER'].methods_by_name['GetEncContactEntry']._loaded_options = None
  _globals['_CONTACTMANAGER'].methods_by_name['GetEncContactEntry']._serialized_options = b'\272\270\221\002\005\n\003\010\354\'\202\323\344\223\002C\">/api/v1alpha1/contactmanager/contactmanager/getenccontactentry:\001*'
  _globals['_CONTACTMANAGER'].methods_by_name['GetKYCEncContactEntry']._loaded_options = None
  _globals['_CONTACTMANAGER'].methods_by_name['GetKYCEncContactEntry']._serialized_options = b'\272\270\221\002\005\n\003\010\355\'\202\323\344\223\002F\"A/api/v1alpha1/contactmanager/contactmanager/getkycenccontactentry:\001*'
  _globals['_CONTACTMANAGER'].methods_by_name['GetKYCKeys']._loaded_options = None
  _globals['_CONTACTMANAGER'].methods_by_name['GetKYCKeys']._serialized_options = b'\272\270\221\002\005\n\003\010\355\'\202\323\344\223\002;\"6/api/v1alpha1/contactmanager/contactmanager/getkyckeys:\001*'
  _globals['_CONTACTMANAGER'].methods_by_name['AddContactEntry']._loaded_options = None
  _globals['_CONTACTMANAGER'].methods_by_name['AddContactEntry']._serialized_options = b'\272\270\221\002\005\n\003\010\354\'\202\323\344\223\002@\";/api/v1alpha1/contactmanager/contactmanager/addcontactentry:\001*'
  _globals['_CONTACTMANAGER'].methods_by_name['EditContactEntry']._loaded_options = None
  _globals['_CONTACTMANAGER'].methods_by_name['EditContactEntry']._serialized_options = b'\272\270\221\002\005\n\003\010\354\'\202\323\344\223\002A\"</api/v1alpha1/contactmanager/contactmanager/editcontactentry:\001*'
  _globals['_CONTACTMANAGER']._serialized_start=180
  _globals['_CONTACTMANAGER']._serialized_end=1695
# @@protoc_insertion_point(module_scope)
