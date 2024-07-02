# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/pbx/v1/service.proto
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
    'services/pbx/v1/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dservices/pbx/v1/service.proto\x12\x0fservices.pbx.v1\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"\x89\x01\n\x07PBXUser\x12\x1e\n\x0bpbx_user_id\x18\x01 \x01(\tR\tpbxUserId\x12\x1e\n\x0borg_user_id\x18\x02 \x01(\tR\torgUserId\x12>\n\x0csip_accounts\x18\x03 \x03(\x0b\x32\x1b.services.pbx.v1.SIPAccountR\x0bsipAccounts\"\x9b\x01\n\nSIPAccount\x12\x15\n\x06sip_id\x18\x01 \x01(\tR\x05sipId\x12\x1b\n\tis_active\x18\x02 \x01(\x08R\x08isActive\x12\x1c\n\textension\x18\x03 \x01(\x05R\textension\x12;\n\x0bring_groups\x18\x04 \x03(\x0b\x32\x1a.services.pbx.v1.RingGroupR\nringGroups\"\xea\x01\n\tRingGroup\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1c\n\textension\x18\x04 \x01(\x05R\textension\x12\x42\n\rring_strategy\x18\x05 \x01(\x0e\x32\x1d.services.pbx.v1.RingStrategyR\x0cringStrategy\x12\x35\n\tpbx_users\x18\x06 \x03(\x0b\x32\x18.services.pbx.v1.PBXUserR\x08pbxUsers\"w\n\x14QueryPbxUsersRequest\x12\x1e\n\x0bpbx_user_id\x18\x01 \x01(\tR\tpbxUserId\x12?\n\rresponse_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0cresponseMask\"G\n\x15QueryPbxUsersResponse\x12.\n\x05users\x18\x01 \x03(\x0b\x32\x18.services.pbx.v1.PBXUserR\x05users\"t\n\x16QueryRingGroupsRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\x12?\n\rresponse_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0cresponseMask\"M\n\x17QueryRingGroupsResponse\x12\x32\n\x06groups\x18\x01 \x03(\x0b\x32\x1a.services.pbx.v1.RingGroupR\x06groups\"\x81\x01\n\x14UpdatePbxUserRequest\x12,\n\x04user\x18\x01 \x01(\x0b\x32\x18.services.pbx.v1.PBXUserR\x04user\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"E\n\x15UpdatePbxUserResponse\x12,\n\x04user\x18\x01 \x01(\x0b\x32\x18.services.pbx.v1.PBXUserR\x04user\"\x87\x01\n\x16UpdateRingGroupRequest\x12\x30\n\x05group\x18\x01 \x01(\x0b\x32\x1a.services.pbx.v1.RingGroupR\x05group\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"K\n\x17UpdateRingGroupResponse\x12\x30\n\x05group\x18\x01 \x01(\x0b\x32\x1a.services.pbx.v1.RingGroupR\x05group\"\x1e\n\x1c\x41ssignRandomExtensionRequest\"=\n\x1d\x41ssignRandomExtensionResponse\x12\x1c\n\textension\x18\x01 \x01(\x05R\textension\"\xd2\x01\n\x16\x43reateRingGroupRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x42\n\rring_strategy\x18\x03 \x01(\x0e\x32\x1d.services.pbx.v1.RingStrategyR\x0cringStrategy\x12 \n\x0cpbx_user_ids\x18\x04 \x03(\tR\npbxUserIds\x12\x1c\n\textension\x18\x05 \x01(\x05R\textension\"K\n\x17\x43reateRingGroupResponse\x12\x30\n\x05group\x18\x01 \x01(\x0b\x32\x1a.services.pbx.v1.RingGroupR\x05group\"3\n\x16\x44\x65leteRingGroupRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\"\x19\n\x17\x44\x65leteRingGroupResponse*\x82\x01\n\x0cRingStrategy\x12\x1d\n\x19RING_STRATEGY_UNSPECIFIED\x10\x00\x12\x1a\n\x16RING_STRATEGY_RING_ALL\x10\x01\x12\x1d\n\x19RING_STRATEGY_ROUND_ROBIN\x10\x02\x12\x18\n\x14RING_STRATEGY_RANDOM\x10\x03\x32\xb3\t\n\nPBXService\x12\x9e\x01\n\rQueryPbxUsers\x12%.services.pbx.v1.QueryPbxUsersRequest\x1a&.services.pbx.v1.QueryPbxUsersResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02.\")/services/pbx/v1/pbxservice/querypbxusers:\x01*\x12\xa6\x01\n\x0fQueryRingGroups\x12\'.services.pbx.v1.QueryRingGroupsRequest\x1a(.services.pbx.v1.QueryRingGroupsResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02\x30\"+/services/pbx/v1/pbxservice/queryringgroups:\x01*\x12\x9e\x01\n\rUpdatePbxUser\x12%.services.pbx.v1.UpdatePbxUserRequest\x1a&.services.pbx.v1.UpdatePbxUserResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\x85 \x82\xd3\xe4\x93\x02.\")/services/pbx/v1/pbxservice/updatepbxuser:\x01*\x12\xa6\x01\n\x0fUpdateRingGroup\x12\'.services.pbx.v1.UpdateRingGroupRequest\x1a(.services.pbx.v1.UpdateRingGroupResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\x85 \x82\xd3\xe4\x93\x02\x30\"+/services/pbx/v1/pbxservice/updateringgroup:\x01*\x12\xa6\x01\n\x0f\x43reateRingGroup\x12\'.services.pbx.v1.CreateRingGroupRequest\x1a(.services.pbx.v1.CreateRingGroupResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\x85 \x82\xd3\xe4\x93\x02\x30\"+/services/pbx/v1/pbxservice/createringgroup:\x01*\x12\xa6\x01\n\x0f\x44\x65leteRingGroup\x12\'.services.pbx.v1.DeleteRingGroupRequest\x1a(.services.pbx.v1.DeleteRingGroupResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\x85 \x82\xd3\xe4\x93\x02\x30\"+/services/pbx/v1/pbxservice/deleteringgroup:\x01*\x12\xbe\x01\n\x15\x41ssignRandomExtension\x12-.services.pbx.v1.AssignRandomExtensionRequest\x1a..services.pbx.v1.AssignRandomExtensionResponse\"F\xba\xb8\x91\x02\x05\n\x03\x08\x85 \x82\xd3\xe4\x93\x02\x36\"1/services/pbx/v1/pbxservice/assignrandomextension:\x01*B\x81\x01\n\x13\x63om.services.pbx.v1B\x0cServiceProtoP\x01\xa2\x02\x03SPX\xaa\x02\x0fServices.Pbx.V1\xca\x02\x0fServices\\Pbx\\V1\xe2\x02\x1bServices\\Pbx\\V1\\GPBMetadata\xea\x02\x11Services::Pbx::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.pbx.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.services.pbx.v1B\014ServiceProtoP\001\242\002\003SPX\252\002\017Services.Pbx.V1\312\002\017Services\\Pbx\\V1\342\002\033Services\\Pbx\\V1\\GPBMetadata\352\002\021Services::Pbx::V1'
  _globals['_PBXSERVICE'].methods_by_name['QueryPbxUsers']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['QueryPbxUsers']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\002.\")/services/pbx/v1/pbxservice/querypbxusers:\001*'
  _globals['_PBXSERVICE'].methods_by_name['QueryRingGroups']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['QueryRingGroups']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\0020\"+/services/pbx/v1/pbxservice/queryringgroups:\001*'
  _globals['_PBXSERVICE'].methods_by_name['UpdatePbxUser']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['UpdatePbxUser']._serialized_options = b'\272\270\221\002\005\n\003\010\205 \202\323\344\223\002.\")/services/pbx/v1/pbxservice/updatepbxuser:\001*'
  _globals['_PBXSERVICE'].methods_by_name['UpdateRingGroup']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['UpdateRingGroup']._serialized_options = b'\272\270\221\002\005\n\003\010\205 \202\323\344\223\0020\"+/services/pbx/v1/pbxservice/updateringgroup:\001*'
  _globals['_PBXSERVICE'].methods_by_name['CreateRingGroup']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['CreateRingGroup']._serialized_options = b'\272\270\221\002\005\n\003\010\205 \202\323\344\223\0020\"+/services/pbx/v1/pbxservice/createringgroup:\001*'
  _globals['_PBXSERVICE'].methods_by_name['DeleteRingGroup']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['DeleteRingGroup']._serialized_options = b'\272\270\221\002\005\n\003\010\205 \202\323\344\223\0020\"+/services/pbx/v1/pbxservice/deleteringgroup:\001*'
  _globals['_PBXSERVICE'].methods_by_name['AssignRandomExtension']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['AssignRandomExtension']._serialized_options = b'\272\270\221\002\005\n\003\010\205 \202\323\344\223\0026\"1/services/pbx/v1/pbxservice/assignrandomextension:\001*'
  _globals['_RINGSTRATEGY']._serialized_start=1949
  _globals['_RINGSTRATEGY']._serialized_end=2079
  _globals['_PBXUSER']._serialized_start=140
  _globals['_PBXUSER']._serialized_end=277
  _globals['_SIPACCOUNT']._serialized_start=280
  _globals['_SIPACCOUNT']._serialized_end=435
  _globals['_RINGGROUP']._serialized_start=438
  _globals['_RINGGROUP']._serialized_end=672
  _globals['_QUERYPBXUSERSREQUEST']._serialized_start=674
  _globals['_QUERYPBXUSERSREQUEST']._serialized_end=793
  _globals['_QUERYPBXUSERSRESPONSE']._serialized_start=795
  _globals['_QUERYPBXUSERSRESPONSE']._serialized_end=866
  _globals['_QUERYRINGGROUPSREQUEST']._serialized_start=868
  _globals['_QUERYRINGGROUPSREQUEST']._serialized_end=984
  _globals['_QUERYRINGGROUPSRESPONSE']._serialized_start=986
  _globals['_QUERYRINGGROUPSRESPONSE']._serialized_end=1063
  _globals['_UPDATEPBXUSERREQUEST']._serialized_start=1066
  _globals['_UPDATEPBXUSERREQUEST']._serialized_end=1195
  _globals['_UPDATEPBXUSERRESPONSE']._serialized_start=1197
  _globals['_UPDATEPBXUSERRESPONSE']._serialized_end=1266
  _globals['_UPDATERINGGROUPREQUEST']._serialized_start=1269
  _globals['_UPDATERINGGROUPREQUEST']._serialized_end=1404
  _globals['_UPDATERINGGROUPRESPONSE']._serialized_start=1406
  _globals['_UPDATERINGGROUPRESPONSE']._serialized_end=1481
  _globals['_ASSIGNRANDOMEXTENSIONREQUEST']._serialized_start=1483
  _globals['_ASSIGNRANDOMEXTENSIONREQUEST']._serialized_end=1513
  _globals['_ASSIGNRANDOMEXTENSIONRESPONSE']._serialized_start=1515
  _globals['_ASSIGNRANDOMEXTENSIONRESPONSE']._serialized_end=1576
  _globals['_CREATERINGGROUPREQUEST']._serialized_start=1579
  _globals['_CREATERINGGROUPREQUEST']._serialized_end=1789
  _globals['_CREATERINGGROUPRESPONSE']._serialized_start=1791
  _globals['_CREATERINGGROUPRESPONSE']._serialized_end=1866
  _globals['_DELETERINGGROUPREQUEST']._serialized_start=1868
  _globals['_DELETERINGGROUPREQUEST']._serialized_end=1919
  _globals['_DELETERINGGROUPRESPONSE']._serialized_start=1921
  _globals['_DELETERINGGROUPRESPONSE']._serialized_end=1946
  _globals['_PBXSERVICE']._serialized_start=2082
  _globals['_PBXSERVICE']._serialized_end=3285
# @@protoc_insertion_point(module_scope)
