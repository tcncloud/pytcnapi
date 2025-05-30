# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/p3_permissions.proto
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
    'api/v1alpha1/org/p3_permissions.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.org import permissions_pb2 as api_dot_commons_dot_org_dot_permissions__pb2
from api.commons import perms_pb2 as api_dot_commons_dot_perms__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/org/p3_permissions.proto\x12\x10\x61pi.v1alpha1.org\x1a!api/commons/org/permissions.proto\x1a\x17\x61pi/commons/perms.proto\x1a google/protobuf/field_mask.proto\"\x91\x01\n\x1e\x43reateP3PermissionGroupRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x39\n\x0bpermissions\x18\x03 \x03(\x0e\x32\x17.api.commons.PermissionR\x0bpermissions\"V\n\x1f\x43reateP3PermissionGroupResponse\x12\x33\n\x16p3_permission_group_id\x18\x01 \x01(\tR\x13p3PermissionGroupId\"\xe4\x01\n\x1eUpdateP3PermissionGroupRequest\x12\x33\n\x16p3_permission_group_id\x18\x01 \x01(\tR\x13p3PermissionGroupId\x12R\n\x13p3_permission_group\x18\x03 \x01(\x0b\x32\".api.commons.org.P3PermissionGroupR\x11p3PermissionGroup\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"u\n\x1fUpdateP3PermissionGroupResponse\x12R\n\x13p3_permission_group\x18\x01 \x01(\x0b\x32\".api.commons.org.P3PermissionGroupR\x11p3PermissionGroup\"\x82\x02\n%UpdateP3PermissionGroupByOrgIdRequest\x12\x33\n\x16p3_permission_group_id\x18\x01 \x01(\tR\x13p3PermissionGroupId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12R\n\x13p3_permission_group\x18\x03 \x01(\x0b\x32\".api.commons.org.P3PermissionGroupR\x11p3PermissionGroup\x12\x39\n\nfield_mask\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"|\n&UpdateP3PermissionGroupByOrgIdResponse\x12R\n\x13p3_permission_group\x18\x01 \x01(\x0b\x32\".api.commons.org.P3PermissionGroupR\x11p3PermissionGroup\"U\n\x1e\x44\x65leteP3PermissionGroupRequest\x12\x33\n\x16p3_permission_group_id\x18\x01 \x01(\tR\x13p3PermissionGroupId\"!\n\x1f\x44\x65leteP3PermissionGroupResponse\"u\n#AssignUsersP3PermissionGroupRequest\x12\x33\n\x16p3_permission_group_id\x18\x01 \x01(\tR\x13p3PermissionGroupId\x12\x19\n\x08user_ids\x18\x02 \x03(\tR\x07userIds\"A\n$AssignUsersP3PermissionGroupResponse\x12\x19\n\x08user_ids\x18\x01 \x03(\tR\x07userIds\"@\n#RevokeUsersP3PermissionGroupRequest\x12\x19\n\x08user_ids\x18\x01 \x03(\tR\x07userIds\"A\n$RevokeUsersP3PermissionGroupResponse\x12\x19\n\x08user_ids\x18\x01 \x03(\tR\x07userIds\"6\n\x1dListP3PermissionGroupsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"v\n\x1eListP3PermissionGroupsResponse\x12T\n\x14p3_permission_groups\x18\x01 \x03(\x0b\x32\".api.commons.org.P3PermissionGroupR\x12p3PermissionGroupsB\x8c\x01\n\x14\x63om.api.v1alpha1.orgB\x12P3PermissionsProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.p3_permissions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\022P3PermissionsProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_CREATEP3PERMISSIONGROUPREQUEST']._serialized_start=154
  _globals['_CREATEP3PERMISSIONGROUPREQUEST']._serialized_end=299
  _globals['_CREATEP3PERMISSIONGROUPRESPONSE']._serialized_start=301
  _globals['_CREATEP3PERMISSIONGROUPRESPONSE']._serialized_end=387
  _globals['_UPDATEP3PERMISSIONGROUPREQUEST']._serialized_start=390
  _globals['_UPDATEP3PERMISSIONGROUPREQUEST']._serialized_end=618
  _globals['_UPDATEP3PERMISSIONGROUPRESPONSE']._serialized_start=620
  _globals['_UPDATEP3PERMISSIONGROUPRESPONSE']._serialized_end=737
  _globals['_UPDATEP3PERMISSIONGROUPBYORGIDREQUEST']._serialized_start=740
  _globals['_UPDATEP3PERMISSIONGROUPBYORGIDREQUEST']._serialized_end=998
  _globals['_UPDATEP3PERMISSIONGROUPBYORGIDRESPONSE']._serialized_start=1000
  _globals['_UPDATEP3PERMISSIONGROUPBYORGIDRESPONSE']._serialized_end=1124
  _globals['_DELETEP3PERMISSIONGROUPREQUEST']._serialized_start=1126
  _globals['_DELETEP3PERMISSIONGROUPREQUEST']._serialized_end=1211
  _globals['_DELETEP3PERMISSIONGROUPRESPONSE']._serialized_start=1213
  _globals['_DELETEP3PERMISSIONGROUPRESPONSE']._serialized_end=1246
  _globals['_ASSIGNUSERSP3PERMISSIONGROUPREQUEST']._serialized_start=1248
  _globals['_ASSIGNUSERSP3PERMISSIONGROUPREQUEST']._serialized_end=1365
  _globals['_ASSIGNUSERSP3PERMISSIONGROUPRESPONSE']._serialized_start=1367
  _globals['_ASSIGNUSERSP3PERMISSIONGROUPRESPONSE']._serialized_end=1432
  _globals['_REVOKEUSERSP3PERMISSIONGROUPREQUEST']._serialized_start=1434
  _globals['_REVOKEUSERSP3PERMISSIONGROUPREQUEST']._serialized_end=1498
  _globals['_REVOKEUSERSP3PERMISSIONGROUPRESPONSE']._serialized_start=1500
  _globals['_REVOKEUSERSP3PERMISSIONGROUPRESPONSE']._serialized_end=1565
  _globals['_LISTP3PERMISSIONGROUPSREQUEST']._serialized_start=1567
  _globals['_LISTP3PERMISSIONGROUPSREQUEST']._serialized_end=1621
  _globals['_LISTP3PERMISSIONGROUPSRESPONSE']._serialized_start=1623
  _globals['_LISTP3PERMISSIONGROUPSRESPONSE']._serialized_end=1741
# @@protoc_insertion_point(module_scope)
