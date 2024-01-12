# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/org/permissions.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.auth import perms_pb2 as api_dot_commons_dot_auth_dot_perms__pb2
from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from api.commons.org import labels_pb2 as api_dot_commons_dot_org_dot_labels__pb2
from api.commons.org import permissions_pb2 as api_dot_commons_dot_org_dot_permissions__pb2
from api.commons.org import user_pb2 as api_dot_commons_dot_org_dot_user__pb2
from api.commons import perms_pb2 as api_dot_commons_dot_perms__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/org/permissions.proto\x12\x10\x61pi.v1alpha1.org\x1a\x1c\x61pi/commons/auth/perms.proto\x1a\x15\x61pi/commons/org.proto\x1a\x1c\x61pi/commons/org/labels.proto\x1a!api/commons/org/permissions.proto\x1a\x1a\x61pi/commons/org/user.proto\x1a\x17\x61pi/commons/perms.proto\"\x17\n\x15GetPermissionsRequest\"\x87\x02\n\x16GetPermissionsResponse\x12>\n\x0bpermissions\x18\x01 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\x0bpermissions\x12>\n\x0ep3_permissions\x18\x02 \x03(\x0e\x32\x17.api.commons.PermissionR\rp3Permissions\x12)\n\x04user\x18\x03 \x01(\x0b\x32\x15.api.commons.org.UserR\x04user\x12\x42\n\x0b\x64\x65\x66\x61ult_app\x18\x04 \x01(\x0e\x32!.api.commons.OperatorApplicationsR\ndefaultApp\"\x1b\n\x19GetUserPermissionsRequest\"\x8c\x01\n\x1aGetUserPermissionsResponse\x12>\n\x0bpermissions\x18\x01 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\x0bpermissions\x12.\n\x06labels\x18\x02 \x03(\x0b\x32\x16.api.commons.org.LabelR\x06labels\"\x94\x01\n\x1c\x43reatePermissionGroupRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12>\n\x0bpermissions\x18\x03 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\x0bpermissions\"O\n\x1d\x43reatePermissionGroupResponse\x12.\n\x13permission_group_id\x18\x01 \x01(\tR\x11permissionGroupId\"\xc4\x01\n\x1cUpdatePermissionGroupRequest\x12.\n\x13permission_group_id\x18\x01 \x01(\tR\x11permissionGroupId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12>\n\x0bpermissions\x18\x04 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\x0bpermissions\"l\n\x1dUpdatePermissionGroupResponse\x12K\n\x10permission_group\x18\x01 \x01(\x0b\x32 .api.commons.org.PermissionGroupR\x0fpermissionGroup\"N\n\x1c\x44\x65letePermissionGroupRequest\x12.\n\x13permission_group_id\x18\x01 \x01(\tR\x11permissionGroupId\"\x1f\n\x1d\x44\x65letePermissionGroupResponse\"\x1d\n\x1bListPermissionGroupsRequest\"m\n\x1cListPermissionGroupsResponse\x12M\n\x11permission_groups\x18\x01 \x03(\x0b\x32 .api.commons.org.PermissionGroupR\x10permissionGroups\";\n\"ListPermissionGroupsByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"t\n#ListPermissionGroupsByOrgIdResponse\x12M\n\x11permission_groups\x18\x01 \x03(\x0b\x32 .api.commons.org.PermissionGroupR\x10permissionGroups\"{\n!AssignUsersPermissionGroupRequest\x12.\n\x13permission_group_id\x18\x01 \x01(\tR\x11permissionGroupId\x12&\n\x0f\x61ssign_user_ids\x18\x02 \x03(\tR\rassignUserIds\"$\n\"AssignUsersPermissionGroupResponse\"{\n!RevokeUsersPermissionGroupRequest\x12.\n\x13permission_group_id\x18\x01 \x01(\tR\x11permissionGroupId\x12&\n\x0frevoke_user_ids\x18\x02 \x03(\tR\rrevokeUserIds\"$\n\"RevokeUsersPermissionGroupResponse\"D\n)AssignAccountOwnerPermissionToUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\",\n*AssignAccountOwnerPermissionToUserResponse\"]\n+RevokeAccountOwnerPermissionFromUserRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\".\n,RevokeAccountOwnerPermissionFromUserResponse\"$\n\"InitDefaultPermissionGroupsRequest\"\x83\x01\n#InitDefaultPermissionGroupsResponse\x12\\\n\x19\x64\x65\x66\x61ult_permission_groups\x18\x01 \x03(\x0b\x32 .api.commons.org.PermissionGroupR\x17\x64\x65\x66\x61ultPermissionGroups\"4\n\x1bGetAccountOwnerGroupRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"k\n\x1cGetAccountOwnerGroupResponse\x12K\n\x10permission_group\x18\x01 \x01(\x0b\x32 .api.commons.org.PermissionGroupR\x0fpermissionGroup\"+\n\x12GetLicensesRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"K\n\x13GetLicensesResponse\x12\x34\n\x08licenses\x18\x01 \x03(\x0b\x32\x18.api.commons.org.LicenseR\x08licenses\"\x17\n\x15GetOrgLicensesRequest\"N\n\x16GetOrgLicensesResponse\x12\x34\n\x08licenses\x18\x01 \x03(\x0b\x32\x18.api.commons.org.LicenseR\x08licenses\"\xbc\x01\n\x15UpdateLicensesRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x43\n\x0e\x61\x64\x64\x65\x64_licenses\x18\x02 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\raddedLicenses\x12G\n\x10revoked_licenses\x18\x03 \x03(\x0e\x32\x1c.api.commons.auth.PermissionR\x0frevokedLicenses\"\x18\n\x16UpdateLicensesResponse\"\x85\x01\n.RemovePermissionFromAllPermissionGroupsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12<\n\npermission\x18\x02 \x01(\x0e\x32\x1c.api.commons.auth.PermissionR\npermission\"1\n/RemovePermissionFromAllPermissionGroupsResponseB\x8a\x01\n\x14\x63om.api.v1alpha1.orgB\x10PermissionsProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.permissions_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\020PermissionsProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_GETPERMISSIONSREQUEST']._serialized_start=227
  _globals['_GETPERMISSIONSREQUEST']._serialized_end=250
  _globals['_GETPERMISSIONSRESPONSE']._serialized_start=253
  _globals['_GETPERMISSIONSRESPONSE']._serialized_end=516
  _globals['_GETUSERPERMISSIONSREQUEST']._serialized_start=518
  _globals['_GETUSERPERMISSIONSREQUEST']._serialized_end=545
  _globals['_GETUSERPERMISSIONSRESPONSE']._serialized_start=548
  _globals['_GETUSERPERMISSIONSRESPONSE']._serialized_end=688
  _globals['_CREATEPERMISSIONGROUPREQUEST']._serialized_start=691
  _globals['_CREATEPERMISSIONGROUPREQUEST']._serialized_end=839
  _globals['_CREATEPERMISSIONGROUPRESPONSE']._serialized_start=841
  _globals['_CREATEPERMISSIONGROUPRESPONSE']._serialized_end=920
  _globals['_UPDATEPERMISSIONGROUPREQUEST']._serialized_start=923
  _globals['_UPDATEPERMISSIONGROUPREQUEST']._serialized_end=1119
  _globals['_UPDATEPERMISSIONGROUPRESPONSE']._serialized_start=1121
  _globals['_UPDATEPERMISSIONGROUPRESPONSE']._serialized_end=1229
  _globals['_DELETEPERMISSIONGROUPREQUEST']._serialized_start=1231
  _globals['_DELETEPERMISSIONGROUPREQUEST']._serialized_end=1309
  _globals['_DELETEPERMISSIONGROUPRESPONSE']._serialized_start=1311
  _globals['_DELETEPERMISSIONGROUPRESPONSE']._serialized_end=1342
  _globals['_LISTPERMISSIONGROUPSREQUEST']._serialized_start=1344
  _globals['_LISTPERMISSIONGROUPSREQUEST']._serialized_end=1373
  _globals['_LISTPERMISSIONGROUPSRESPONSE']._serialized_start=1375
  _globals['_LISTPERMISSIONGROUPSRESPONSE']._serialized_end=1484
  _globals['_LISTPERMISSIONGROUPSBYORGIDREQUEST']._serialized_start=1486
  _globals['_LISTPERMISSIONGROUPSBYORGIDREQUEST']._serialized_end=1545
  _globals['_LISTPERMISSIONGROUPSBYORGIDRESPONSE']._serialized_start=1547
  _globals['_LISTPERMISSIONGROUPSBYORGIDRESPONSE']._serialized_end=1663
  _globals['_ASSIGNUSERSPERMISSIONGROUPREQUEST']._serialized_start=1665
  _globals['_ASSIGNUSERSPERMISSIONGROUPREQUEST']._serialized_end=1788
  _globals['_ASSIGNUSERSPERMISSIONGROUPRESPONSE']._serialized_start=1790
  _globals['_ASSIGNUSERSPERMISSIONGROUPRESPONSE']._serialized_end=1826
  _globals['_REVOKEUSERSPERMISSIONGROUPREQUEST']._serialized_start=1828
  _globals['_REVOKEUSERSPERMISSIONGROUPREQUEST']._serialized_end=1951
  _globals['_REVOKEUSERSPERMISSIONGROUPRESPONSE']._serialized_start=1953
  _globals['_REVOKEUSERSPERMISSIONGROUPRESPONSE']._serialized_end=1989
  _globals['_ASSIGNACCOUNTOWNERPERMISSIONTOUSERREQUEST']._serialized_start=1991
  _globals['_ASSIGNACCOUNTOWNERPERMISSIONTOUSERREQUEST']._serialized_end=2059
  _globals['_ASSIGNACCOUNTOWNERPERMISSIONTOUSERRESPONSE']._serialized_start=2061
  _globals['_ASSIGNACCOUNTOWNERPERMISSIONTOUSERRESPONSE']._serialized_end=2105
  _globals['_REVOKEACCOUNTOWNERPERMISSIONFROMUSERREQUEST']._serialized_start=2107
  _globals['_REVOKEACCOUNTOWNERPERMISSIONFROMUSERREQUEST']._serialized_end=2200
  _globals['_REVOKEACCOUNTOWNERPERMISSIONFROMUSERRESPONSE']._serialized_start=2202
  _globals['_REVOKEACCOUNTOWNERPERMISSIONFROMUSERRESPONSE']._serialized_end=2248
  _globals['_INITDEFAULTPERMISSIONGROUPSREQUEST']._serialized_start=2250
  _globals['_INITDEFAULTPERMISSIONGROUPSREQUEST']._serialized_end=2286
  _globals['_INITDEFAULTPERMISSIONGROUPSRESPONSE']._serialized_start=2289
  _globals['_INITDEFAULTPERMISSIONGROUPSRESPONSE']._serialized_end=2420
  _globals['_GETACCOUNTOWNERGROUPREQUEST']._serialized_start=2422
  _globals['_GETACCOUNTOWNERGROUPREQUEST']._serialized_end=2474
  _globals['_GETACCOUNTOWNERGROUPRESPONSE']._serialized_start=2476
  _globals['_GETACCOUNTOWNERGROUPRESPONSE']._serialized_end=2583
  _globals['_GETLICENSESREQUEST']._serialized_start=2585
  _globals['_GETLICENSESREQUEST']._serialized_end=2628
  _globals['_GETLICENSESRESPONSE']._serialized_start=2630
  _globals['_GETLICENSESRESPONSE']._serialized_end=2705
  _globals['_GETORGLICENSESREQUEST']._serialized_start=2707
  _globals['_GETORGLICENSESREQUEST']._serialized_end=2730
  _globals['_GETORGLICENSESRESPONSE']._serialized_start=2732
  _globals['_GETORGLICENSESRESPONSE']._serialized_end=2810
  _globals['_UPDATELICENSESREQUEST']._serialized_start=2813
  _globals['_UPDATELICENSESREQUEST']._serialized_end=3001
  _globals['_UPDATELICENSESRESPONSE']._serialized_start=3003
  _globals['_UPDATELICENSESRESPONSE']._serialized_end=3027
  _globals['_REMOVEPERMISSIONFROMALLPERMISSIONGROUPSREQUEST']._serialized_start=3030
  _globals['_REMOVEPERMISSIONFROMALLPERMISSIONGROUPSREQUEST']._serialized_end=3163
  _globals['_REMOVEPERMISSIONFROMALLPERMISSIONGROUPSRESPONSE']._serialized_start=3165
  _globals['_REMOVEPERMISSIONFROMALLPERMISSIONGROUPSRESPONSE']._serialized_end=3214
# @@protoc_insertion_point(module_scope)
