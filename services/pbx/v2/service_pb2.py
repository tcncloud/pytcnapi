# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/pbx/v2/service.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'services/pbx/v2/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dservices/pbx/v2/service.proto\x12\x0fservices.pbx.v2\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"q\n\x07PBXUser\x12\x1e\n\x0bpbx_user_id\x18\x01 \x01(\tR\tpbxUserId\x12\x1e\n\x0borg_user_id\x18\x02 \x01(\tR\torgUserId\x12&\n\x0fsip_account_ids\x18\x03 \x03(\tR\rsipAccountIds\"\xa4\x01\n\nSIPAccount\x12\x15\n\x06sip_id\x18\x01 \x01(\tR\x05sipId\x12\x1b\n\tis_active\x18\x02 \x01(\x08R\x08isActive\x12\x1c\n\textension\x18\x03 \x01(\tR\textension\x12$\n\x0ering_group_ids\x18\x04 \x03(\tR\x0cringGroupIds\x12\x1e\n\x0borg_user_id\x18\x05 \x01(\tR\torgUserId\"\xdb\x01\n\tRingGroup\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1c\n\textension\x18\x04 \x01(\tR\textension\x12\x42\n\rring_strategy\x18\x05 \x01(\x0e\x32\x1d.services.pbx.v2.RingStrategyR\x0cringStrategy\x12&\n\x0fsip_account_ids\x18\x06 \x03(\tR\rsipAccountIds\"\x15\n\x13ListPBXUsersRequest\"F\n\x14ListPBXUsersResponse\x12.\n\x05users\x18\x01 \x03(\x0b\x32\x18.services.pbx.v2.PBXUserR\x05users\"\x18\n\x16ListSIPAccountsRequest\"Y\n\x17ListSIPAccountsResponse\x12>\n\x0csip_accounts\x18\x01 \x03(\x0b\x32\x1b.services.pbx.v2.SIPAccountR\x0bsipAccounts\"I\n#ListSIPAccountsByRingGroupIdRequest\x12\"\n\rring_group_id\x18\x01 \x01(\tR\x0bringGroupId\"f\n$ListSIPAccountsByRingGroupIdResponse\x12>\n\x0csip_accounts\x18\x01 \x03(\x0b\x32\x1b.services.pbx.v2.SIPAccountR\x0bsipAccounts\">\n\x1cGetSIPAccountByUserIdRequest\x12\x1e\n\x0borg_user_id\x18\x01 \x01(\tR\torgUserId\"]\n\x1dGetSIPAccountByUserIdResponse\x12<\n\x0bsip_account\x18\x01 \x01(\x0b\x32\x1b.services.pbx.v2.SIPAccountR\nsipAccount\"<\n\x14GetSIPAccountRequest\x12$\n\x0esip_account_id\x18\x01 \x01(\tR\x0csipAccountId\"U\n\x15GetSIPAccountResponse\x12<\n\x0bsip_account\x18\x01 \x03(\x0b\x32\x1b.services.pbx.v2.SIPAccountR\nsipAccount\"3\n\x11GetPBXUserRequest\x12\x1e\n\x0bpbx_user_id\x18\x01 \x01(\tR\tpbxUserId\"B\n\x12GetPBXUserResponse\x12,\n\x04user\x18\x01 \x01(\x0b\x32\x18.services.pbx.v2.PBXUserR\x04user\"\x17\n\x15ListRingGroupsRequest\"L\n\x16ListRingGroupsResponse\x12\x32\n\x06groups\x18\x01 \x03(\x0b\x32\x1a.services.pbx.v2.RingGroupR\x06groups\"D\n\x1cListRingGroupsBySipIdRequest\x12$\n\x0esip_account_id\x18\x01 \x01(\tR\x0csipAccountId\"S\n\x1dListRingGroupsBySipIdResponse\x12\x32\n\x06groups\x18\x01 \x03(\x0b\x32\x1a.services.pbx.v2.RingGroupR\x06groups\"9\n\x13GetRingGroupRequest\x12\"\n\rring_group_id\x18\x01 \x01(\tR\x0bringGroupId\"H\n\x14GetRingGroupResponse\x12\x30\n\x05group\x18\x01 \x01(\x0b\x32\x1a.services.pbx.v2.RingGroupR\x05group\"\x94\x01\n\x17UpdateSIPAccountRequest\x12<\n\x0bsip_account\x18\x01 \x01(\x0b\x32\x1b.services.pbx.v2.SIPAccountR\nsipAccount\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"X\n\x18UpdateSIPAccountResponse\x12<\n\x0bsip_account\x18\x01 \x01(\x0b\x32\x1b.services.pbx.v2.SIPAccountR\nsipAccount\"\x87\x01\n\x16UpdateRingGroupRequest\x12\x30\n\x05group\x18\x01 \x01(\x0b\x32\x1a.services.pbx.v2.RingGroupR\x05group\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"K\n\x17UpdateRingGroupResponse\x12\x30\n\x05group\x18\x01 \x01(\x0b\x32\x1a.services.pbx.v2.RingGroupR\x05group\"\x1e\n\x1c\x41ssignRandomExtensionRequest\"=\n\x1d\x41ssignRandomExtensionResponse\x12\x1c\n\textension\x18\x01 \x01(\tR\textension\"J\n\x16\x43reateRingGroupRequest\x12\x30\n\x05group\x18\x01 \x01(\x0b\x32\x1a.services.pbx.v2.RingGroupR\x05group\"K\n\x17\x43reateRingGroupResponse\x12\x30\n\x05group\x18\x01 \x01(\x0b\x32\x1a.services.pbx.v2.RingGroupR\x05group\"3\n\x16\x44\x65leteRingGroupRequest\x12\x19\n\x08group_id\x18\x01 \x01(\tR\x07groupId\"\x19\n\x17\x44\x65leteRingGroupResponse*\x9d\x01\n\x0cRingStrategy\x12\x1d\n\x19RING_STRATEGY_UNSPECIFIED\x10\x00\x12\x1a\n\x16RING_STRATEGY_RING_ALL\x10\x01\x12\x1d\n\x19RING_STRATEGY_ROUND_ROBIN\x10\x02\x12\x18\n\x14RING_STRATEGY_RANDOM\x10\x03\x12\x19\n\x15RING_STRATEGY_ORDERED\x10\x04\x32\x92\x13\n\nPBXService\x12\x9a\x01\n\x0cListPBXUsers\x12$.services.pbx.v2.ListPBXUsersRequest\x1a%.services.pbx.v2.ListPBXUsersResponse\"=\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02-\"(/services/pbx/v2/pbxservice/listpbxusers:\x01*\x12\x92\x01\n\nGetPBXUser\x12\".services.pbx.v2.GetPBXUserRequest\x1a#.services.pbx.v2.GetPBXUserResponse\";\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02+\"&/services/pbx/v2/pbxservice/getpbxuser:\x01*\x12\xa2\x01\n\x0eListRingGroups\x12&.services.pbx.v2.ListRingGroupsRequest\x1a\'.services.pbx.v2.ListRingGroupsResponse\"?\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02/\"*/services/pbx/v2/pbxservice/listringgroups:\x01*\x12\xbe\x01\n\x15ListRingGroupsBySipId\x12-.services.pbx.v2.ListRingGroupsBySipIdRequest\x1a..services.pbx.v2.ListRingGroupsBySipIdResponse\"F\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02\x36\"1/services/pbx/v2/pbxservice/listringgroupsbysipid:\x01*\x12\x9a\x01\n\x0cGetRingGroup\x12$.services.pbx.v2.GetRingGroupRequest\x1a%.services.pbx.v2.GetRingGroupResponse\"=\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02-\"(/services/pbx/v2/pbxservice/getringgroup:\x01*\x12\x9e\x01\n\rGetSIPAccount\x12%.services.pbx.v2.GetSIPAccountRequest\x1a&.services.pbx.v2.GetSIPAccountResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02.\")/services/pbx/v2/pbxservice/getsipaccount:\x01*\x12\xbe\x01\n\x15GetSIPAccountByUserId\x12-.services.pbx.v2.GetSIPAccountByUserIdRequest\x1a..services.pbx.v2.GetSIPAccountByUserIdResponse\"F\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02\x36\"1/services/pbx/v2/pbxservice/getsipaccountbyuserid:\x01*\x12\xa6\x01\n\x0fListSIPAccounts\x12\'.services.pbx.v2.ListSIPAccountsRequest\x1a(.services.pbx.v2.ListSIPAccountsResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02\x30\"+/services/pbx/v2/pbxservice/listsipaccounts:\x01*\x12\xda\x01\n\x1cListSIPAccountsByRingGroupId\x12\x34.services.pbx.v2.ListSIPAccountsByRingGroupIdRequest\x1a\x35.services.pbx.v2.ListSIPAccountsByRingGroupIdResponse\"M\xba\xb8\x91\x02\x05\n\x03\x08\x84 \x82\xd3\xe4\x93\x02=\"8/services/pbx/v2/pbxservice/listsipaccountsbyringgroupid:\x01*\x12\xaa\x01\n\x10UpdateSIPAccount\x12(.services.pbx.v2.UpdateSIPAccountRequest\x1a).services.pbx.v2.UpdateSIPAccountResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\x85 \x82\xd3\xe4\x93\x02\x31\",/services/pbx/v2/pbxservice/updatesipaccount:\x01*\x12\xa6\x01\n\x0fUpdateRingGroup\x12\'.services.pbx.v2.UpdateRingGroupRequest\x1a(.services.pbx.v2.UpdateRingGroupResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\x85 \x82\xd3\xe4\x93\x02\x30\"+/services/pbx/v2/pbxservice/updateringgroup:\x01*\x12\xa6\x01\n\x0f\x43reateRingGroup\x12\'.services.pbx.v2.CreateRingGroupRequest\x1a(.services.pbx.v2.CreateRingGroupResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\x85 \x82\xd3\xe4\x93\x02\x30\"+/services/pbx/v2/pbxservice/createringgroup:\x01*\x12\xa6\x01\n\x0f\x44\x65leteRingGroup\x12\'.services.pbx.v2.DeleteRingGroupRequest\x1a(.services.pbx.v2.DeleteRingGroupResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\x85 \x82\xd3\xe4\x93\x02\x30\"+/services/pbx/v2/pbxservice/deleteringgroup:\x01*\x12\xbe\x01\n\x15\x41ssignRandomExtension\x12-.services.pbx.v2.AssignRandomExtensionRequest\x1a..services.pbx.v2.AssignRandomExtensionResponse\"F\xba\xb8\x91\x02\x05\n\x03\x08\x85 \x82\xd3\xe4\x93\x02\x36\"1/services/pbx/v2/pbxservice/assignrandomextension:\x01*B\x81\x01\n\x13\x63om.services.pbx.v2B\x0cServiceProtoP\x01\xa2\x02\x03SPX\xaa\x02\x0fServices.Pbx.V2\xca\x02\x0fServices\\Pbx\\V2\xe2\x02\x1bServices\\Pbx\\V2\\GPBMetadata\xea\x02\x11Services::Pbx::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.pbx.v2.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.services.pbx.v2B\014ServiceProtoP\001\242\002\003SPX\252\002\017Services.Pbx.V2\312\002\017Services\\Pbx\\V2\342\002\033Services\\Pbx\\V2\\GPBMetadata\352\002\021Services::Pbx::V2'
  _globals['_PBXSERVICE'].methods_by_name['ListPBXUsers']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['ListPBXUsers']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\002-\"(/services/pbx/v2/pbxservice/listpbxusers:\001*'
  _globals['_PBXSERVICE'].methods_by_name['GetPBXUser']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['GetPBXUser']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\002+\"&/services/pbx/v2/pbxservice/getpbxuser:\001*'
  _globals['_PBXSERVICE'].methods_by_name['ListRingGroups']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['ListRingGroups']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\002/\"*/services/pbx/v2/pbxservice/listringgroups:\001*'
  _globals['_PBXSERVICE'].methods_by_name['ListRingGroupsBySipId']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['ListRingGroupsBySipId']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\0026\"1/services/pbx/v2/pbxservice/listringgroupsbysipid:\001*'
  _globals['_PBXSERVICE'].methods_by_name['GetRingGroup']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['GetRingGroup']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\002-\"(/services/pbx/v2/pbxservice/getringgroup:\001*'
  _globals['_PBXSERVICE'].methods_by_name['GetSIPAccount']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['GetSIPAccount']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\002.\")/services/pbx/v2/pbxservice/getsipaccount:\001*'
  _globals['_PBXSERVICE'].methods_by_name['GetSIPAccountByUserId']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['GetSIPAccountByUserId']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\0026\"1/services/pbx/v2/pbxservice/getsipaccountbyuserid:\001*'
  _globals['_PBXSERVICE'].methods_by_name['ListSIPAccounts']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['ListSIPAccounts']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\0020\"+/services/pbx/v2/pbxservice/listsipaccounts:\001*'
  _globals['_PBXSERVICE'].methods_by_name['ListSIPAccountsByRingGroupId']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['ListSIPAccountsByRingGroupId']._serialized_options = b'\272\270\221\002\005\n\003\010\204 \202\323\344\223\002=\"8/services/pbx/v2/pbxservice/listsipaccountsbyringgroupid:\001*'
  _globals['_PBXSERVICE'].methods_by_name['UpdateSIPAccount']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['UpdateSIPAccount']._serialized_options = b'\272\270\221\002\005\n\003\010\205 \202\323\344\223\0021\",/services/pbx/v2/pbxservice/updatesipaccount:\001*'
  _globals['_PBXSERVICE'].methods_by_name['UpdateRingGroup']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['UpdateRingGroup']._serialized_options = b'\272\270\221\002\005\n\003\010\205 \202\323\344\223\0020\"+/services/pbx/v2/pbxservice/updateringgroup:\001*'
  _globals['_PBXSERVICE'].methods_by_name['CreateRingGroup']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['CreateRingGroup']._serialized_options = b'\272\270\221\002\005\n\003\010\205 \202\323\344\223\0020\"+/services/pbx/v2/pbxservice/createringgroup:\001*'
  _globals['_PBXSERVICE'].methods_by_name['DeleteRingGroup']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['DeleteRingGroup']._serialized_options = b'\272\270\221\002\005\n\003\010\205 \202\323\344\223\0020\"+/services/pbx/v2/pbxservice/deleteringgroup:\001*'
  _globals['_PBXSERVICE'].methods_by_name['AssignRandomExtension']._loaded_options = None
  _globals['_PBXSERVICE'].methods_by_name['AssignRandomExtension']._serialized_options = b'\272\270\221\002\005\n\003\010\205 \202\323\344\223\0026\"1/services/pbx/v2/pbxservice/assignrandomextension:\001*'
  _globals['_RINGSTRATEGY']._serialized_start=2639
  _globals['_RINGSTRATEGY']._serialized_end=2796
  _globals['_PBXUSER']._serialized_start=139
  _globals['_PBXUSER']._serialized_end=252
  _globals['_SIPACCOUNT']._serialized_start=255
  _globals['_SIPACCOUNT']._serialized_end=419
  _globals['_RINGGROUP']._serialized_start=422
  _globals['_RINGGROUP']._serialized_end=641
  _globals['_LISTPBXUSERSREQUEST']._serialized_start=643
  _globals['_LISTPBXUSERSREQUEST']._serialized_end=664
  _globals['_LISTPBXUSERSRESPONSE']._serialized_start=666
  _globals['_LISTPBXUSERSRESPONSE']._serialized_end=736
  _globals['_LISTSIPACCOUNTSREQUEST']._serialized_start=738
  _globals['_LISTSIPACCOUNTSREQUEST']._serialized_end=762
  _globals['_LISTSIPACCOUNTSRESPONSE']._serialized_start=764
  _globals['_LISTSIPACCOUNTSRESPONSE']._serialized_end=853
  _globals['_LISTSIPACCOUNTSBYRINGGROUPIDREQUEST']._serialized_start=855
  _globals['_LISTSIPACCOUNTSBYRINGGROUPIDREQUEST']._serialized_end=928
  _globals['_LISTSIPACCOUNTSBYRINGGROUPIDRESPONSE']._serialized_start=930
  _globals['_LISTSIPACCOUNTSBYRINGGROUPIDRESPONSE']._serialized_end=1032
  _globals['_GETSIPACCOUNTBYUSERIDREQUEST']._serialized_start=1034
  _globals['_GETSIPACCOUNTBYUSERIDREQUEST']._serialized_end=1096
  _globals['_GETSIPACCOUNTBYUSERIDRESPONSE']._serialized_start=1098
  _globals['_GETSIPACCOUNTBYUSERIDRESPONSE']._serialized_end=1191
  _globals['_GETSIPACCOUNTREQUEST']._serialized_start=1193
  _globals['_GETSIPACCOUNTREQUEST']._serialized_end=1253
  _globals['_GETSIPACCOUNTRESPONSE']._serialized_start=1255
  _globals['_GETSIPACCOUNTRESPONSE']._serialized_end=1340
  _globals['_GETPBXUSERREQUEST']._serialized_start=1342
  _globals['_GETPBXUSERREQUEST']._serialized_end=1393
  _globals['_GETPBXUSERRESPONSE']._serialized_start=1395
  _globals['_GETPBXUSERRESPONSE']._serialized_end=1461
  _globals['_LISTRINGGROUPSREQUEST']._serialized_start=1463
  _globals['_LISTRINGGROUPSREQUEST']._serialized_end=1486
  _globals['_LISTRINGGROUPSRESPONSE']._serialized_start=1488
  _globals['_LISTRINGGROUPSRESPONSE']._serialized_end=1564
  _globals['_LISTRINGGROUPSBYSIPIDREQUEST']._serialized_start=1566
  _globals['_LISTRINGGROUPSBYSIPIDREQUEST']._serialized_end=1634
  _globals['_LISTRINGGROUPSBYSIPIDRESPONSE']._serialized_start=1636
  _globals['_LISTRINGGROUPSBYSIPIDRESPONSE']._serialized_end=1719
  _globals['_GETRINGGROUPREQUEST']._serialized_start=1721
  _globals['_GETRINGGROUPREQUEST']._serialized_end=1778
  _globals['_GETRINGGROUPRESPONSE']._serialized_start=1780
  _globals['_GETRINGGROUPRESPONSE']._serialized_end=1852
  _globals['_UPDATESIPACCOUNTREQUEST']._serialized_start=1855
  _globals['_UPDATESIPACCOUNTREQUEST']._serialized_end=2003
  _globals['_UPDATESIPACCOUNTRESPONSE']._serialized_start=2005
  _globals['_UPDATESIPACCOUNTRESPONSE']._serialized_end=2093
  _globals['_UPDATERINGGROUPREQUEST']._serialized_start=2096
  _globals['_UPDATERINGGROUPREQUEST']._serialized_end=2231
  _globals['_UPDATERINGGROUPRESPONSE']._serialized_start=2233
  _globals['_UPDATERINGGROUPRESPONSE']._serialized_end=2308
  _globals['_ASSIGNRANDOMEXTENSIONREQUEST']._serialized_start=2310
  _globals['_ASSIGNRANDOMEXTENSIONREQUEST']._serialized_end=2340
  _globals['_ASSIGNRANDOMEXTENSIONRESPONSE']._serialized_start=2342
  _globals['_ASSIGNRANDOMEXTENSIONRESPONSE']._serialized_end=2403
  _globals['_CREATERINGGROUPREQUEST']._serialized_start=2405
  _globals['_CREATERINGGROUPREQUEST']._serialized_end=2479
  _globals['_CREATERINGGROUPRESPONSE']._serialized_start=2481
  _globals['_CREATERINGGROUPRESPONSE']._serialized_end=2556
  _globals['_DELETERINGGROUPREQUEST']._serialized_start=2558
  _globals['_DELETERINGGROUPREQUEST']._serialized_end=2609
  _globals['_DELETERINGGROUPRESPONSE']._serialized_start=2611
  _globals['_DELETERINGGROUPRESPONSE']._serialized_end=2636
  _globals['_PBXSERVICE']._serialized_start=2799
  _globals['_PBXSERVICE']._serialized_end=5249
# @@protoc_insertion_point(module_scope)
