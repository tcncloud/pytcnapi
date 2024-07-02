# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/org/trusts.proto
# Protobuf Python Version: 5.27.2
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
    2,
    '',
    'api/commons/org/trusts.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.auth import perms_pb2 as api_dot_commons_dot_auth_dot_perms__pb2
from api.commons.org import labels_pb2 as api_dot_commons_dot_org_dot_labels__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/commons/org/trusts.proto\x12\x0f\x61pi.commons.org\x1a\x1c\x61pi/commons/auth/perms.proto\x1a\x1c\x61pi/commons/org/labels.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xc7\x02\n\x05Trust\x12\x19\n\x08trust_id\x18\x01 \x01(\tR\x07trustId\x12\x18\n\x07grantor\x18\x02 \x01(\tR\x07grantor\x12\x18\n\x07grantee\x18\x03 \x01(\tR\x07grantee\x12\x12\n\x04name\x18\x04 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12>\n\x0bpermissions\x18\x06 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\x0bpermissions\x12.\n\x06labels\x18\x07 \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\x12/\n\x06status\x18\x08 \x01(\x0e\x32\x17.api.commons.org.StatusR\x06status\x12\x18\n\x07\x64\x65leted\x18\t \x01(\x08R\x07\x64\x65leted\"\x8e\x02\n\nTrustGroup\x12\x18\n\x07grantor\x18\x01 \x01(\tR\x07grantor\x12_\n\x13labeled_permissions\x18\x02 \x03(\x0b\x32..api.commons.org.TrustGroup.LabeledPermissionsR\x12labeledPermissions\x1a\x84\x01\n\x12LabeledPermissions\x12>\n\x0bpermissions\x18\x01 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\x0bpermissions\x12.\n\x06labels\x18\x02 \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\"\x8e\x02\n\x0bTrustFilter\x12\x36\n\x07grantor\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x07grantor\x12\x36\n\x07grantee\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x07grantee\x12N\n\rstatus_filter\x18\x03 \x01(\x0b\x32).api.commons.org.TrustFilter.StatusFilterR\x0cstatusFilter\x1a?\n\x0cStatusFilter\x12/\n\x06values\x18\x01 \x03(\x0e\x32\x17.api.commons.org.StatusR\x06values*1\n\x06Status\x12\x0b\n\x07PENDING\x10\x00\x12\x0c\n\x08REJECTED\x10\x01\x12\x0c\n\x08\x41\x43\x43\x45PTED\x10\x02\x42\x80\x01\n\x13\x63om.api.commons.orgB\x0bTrustsProtoP\x01\xa2\x02\x03\x41\x43O\xaa\x02\x0f\x41pi.Commons.Org\xca\x02\x0f\x41pi\\Commons\\Org\xe2\x02\x1b\x41pi\\Commons\\Org\\GPBMetadata\xea\x02\x11\x41pi::Commons::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org.trusts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.api.commons.orgB\013TrustsProtoP\001\242\002\003ACO\252\002\017Api.Commons.Org\312\002\017Api\\Commons\\Org\342\002\033Api\\Commons\\Org\\GPBMetadata\352\002\021Api::Commons::Org'
  _globals['_STATUS']._serialized_start=1017
  _globals['_STATUS']._serialized_end=1066
  _globals['_TRUST']._serialized_start=142
  _globals['_TRUST']._serialized_end=469
  _globals['_TRUSTGROUP']._serialized_start=472
  _globals['_TRUSTGROUP']._serialized_end=742
  _globals['_TRUSTGROUP_LABELEDPERMISSIONS']._serialized_start=610
  _globals['_TRUSTGROUP_LABELEDPERMISSIONS']._serialized_end=742
  _globals['_TRUSTFILTER']._serialized_start=745
  _globals['_TRUSTFILTER']._serialized_end=1015
  _globals['_TRUSTFILTER_STATUSFILTER']._serialized_start=952
  _globals['_TRUSTFILTER_STATUSFILTER']._serialized_end=1015
# @@protoc_insertion_point(module_scope)
