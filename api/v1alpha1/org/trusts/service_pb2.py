# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/trusts/service.proto
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
    'api/v1alpha1/org/trusts/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.org import agent_profile_group_pb2 as api_dot_v1alpha1_dot_org_dot_agent__profile__group__pb2
from api.v1alpha1.org import auth_token_pb2 as api_dot_v1alpha1_dot_org_dot_auth__token__pb2
from api.v1alpha1.org import huntgroup_pb2 as api_dot_v1alpha1_dot_org_dot_huntgroup__pb2
from api.v1alpha1.org import labels_pb2 as api_dot_v1alpha1_dot_org_dot_labels__pb2
from api.v1alpha1.org import notifications_pb2 as api_dot_v1alpha1_dot_org_dot_notifications__pb2
from api.v1alpha1.org import organization_pb2 as api_dot_v1alpha1_dot_org_dot_organization__pb2
from api.v1alpha1.org import p3_permissions_pb2 as api_dot_v1alpha1_dot_org_dot_p3__permissions__pb2
from api.v1alpha1.org import permissions_pb2 as api_dot_v1alpha1_dot_org_dot_permissions__pb2
from api.v1alpha1.org import preferences_pb2 as api_dot_v1alpha1_dot_org_dot_preferences__pb2
from api.v1alpha1.org import trusts_pb2 as api_dot_v1alpha1_dot_org_dot_trusts__pb2
from api.v1alpha1.org import user_pb2 as api_dot_v1alpha1_dot_org_dot_user__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/org/trusts/service.proto\x12\x17\x61pi.v1alpha1.org.trusts\x1a\x17\x61nnotations/authz.proto\x1a*api/v1alpha1/org/agent_profile_group.proto\x1a!api/v1alpha1/org/auth_token.proto\x1a api/v1alpha1/org/huntgroup.proto\x1a\x1d\x61pi/v1alpha1/org/labels.proto\x1a$api/v1alpha1/org/notifications.proto\x1a#api/v1alpha1/org/organization.proto\x1a%api/v1alpha1/org/p3_permissions.proto\x1a\"api/v1alpha1/org/permissions.proto\x1a\"api/v1alpha1/org/preferences.proto\x1a\x1d\x61pi/v1alpha1/org/trusts.proto\x1a\x1b\x61pi/v1alpha1/org/user.proto\x1a\x1cgoogle/api/annotations.proto2\xda\x0c\n\rTrustsService\x12\x95\x01\n\x0b\x43reateTrust\x12$.api.v1alpha1.org.CreateTrustRequest\x1a%.api.v1alpha1.org.CreateTrustResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/trusts/createtrust:\x01*\x12\x95\x01\n\x0b\x41\x63\x63\x65ptTrust\x12$.api.v1alpha1.org.AcceptTrustRequest\x1a%.api.v1alpha1.org.AcceptTrustResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/trusts/accepttrust:\x01*\x12\x95\x01\n\x0bRejectTrust\x12$.api.v1alpha1.org.RejectTrustRequest\x1a%.api.v1alpha1.org.RejectTrustResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/trusts/rejecttrust:\x01*\x12\x89\x01\n\x08GetTrust\x12!.api.v1alpha1.org.GetTrustRequest\x1a\".api.v1alpha1.org.GetTrustResponse\"6\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x01\x82\xd3\xe4\x93\x02&\"!/api/v1alpha1/org/trusts/gettrust:\x01*\x12\xb6\x01\n\x12ListIncomingTrusts\x12+.api.v1alpha1.org.ListIncomingTrustsRequest\x1a,.api.v1alpha1.org.ListIncomingTrustsResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x01\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/org/trusts/list/listincomingtrusts:\x01*\x12\xaa\x01\n\x0fListGivenTrusts\x12(.api.v1alpha1.org.ListGivenTrustsRequest\x1a).api.v1alpha1.org.ListGivenTrustsResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x01\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/org/trusts/list/listgiventrusts:\x01*\x12\xbe\x01\n\x14ListAssignableTrusts\x12-.api.v1alpha1.org.ListAssignableTrustsRequest\x1a..api.v1alpha1.org.ListAssignableTrustsResponse\"G\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x01\x82\xd3\xe4\x93\x02\x37\"2/api/v1alpha1/org/trusts/list/listassignabletrusts:\x01*\x12\x95\x01\n\x0b\x44\x65leteTrust\x12$.api.v1alpha1.org.DeleteTrustRequest\x1a%.api.v1alpha1.org.DeleteTrustResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/trusts/deletetrust:\x01*\x12\x95\x01\n\x0b\x41ssignTrust\x12$.api.v1alpha1.org.AssignTrustRequest\x1a%.api.v1alpha1.org.AssignTrustResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x01\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/org/trusts/assigntrust:\x01*\x12\x9d\x01\n\rUnassignTrust\x12&.api.v1alpha1.org.UnassignTrustRequest\x1a\'.api.v1alpha1.org.UnassignTrustResponse\";\xba\xb8\x91\x02\x05\n\x03\x08\xa0\x01\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/org/trusts/unassigntrust:\x01*B\xab\x01\n\x1b\x63om.api.v1alpha1.org.trustsB\x0cServiceProtoP\x01\xa2\x02\x04\x41VOT\xaa\x02\x17\x41pi.V1alpha1.Org.Trusts\xca\x02\x17\x41pi\\V1alpha1\\Org\\Trusts\xe2\x02#Api\\V1alpha1\\Org\\Trusts\\GPBMetadata\xea\x02\x1a\x41pi::V1alpha1::Org::Trustsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.trusts.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.org.trustsB\014ServiceProtoP\001\242\002\004AVOT\252\002\027Api.V1alpha1.Org.Trusts\312\002\027Api\\V1alpha1\\Org\\Trusts\342\002#Api\\V1alpha1\\Org\\Trusts\\GPBMetadata\352\002\032Api::V1alpha1::Org::Trusts'
  _globals['_TRUSTSSERVICE'].methods_by_name['CreateTrust']._loaded_options = None
  _globals['_TRUSTSSERVICE'].methods_by_name['CreateTrust']._serialized_options = b'\272\270\221\002\005\n\003\010\240\001\202\323\344\223\002)\"$/api/v1alpha1/org/trusts/createtrust:\001*'
  _globals['_TRUSTSSERVICE'].methods_by_name['AcceptTrust']._loaded_options = None
  _globals['_TRUSTSSERVICE'].methods_by_name['AcceptTrust']._serialized_options = b'\272\270\221\002\005\n\003\010\240\001\202\323\344\223\002)\"$/api/v1alpha1/org/trusts/accepttrust:\001*'
  _globals['_TRUSTSSERVICE'].methods_by_name['RejectTrust']._loaded_options = None
  _globals['_TRUSTSSERVICE'].methods_by_name['RejectTrust']._serialized_options = b'\272\270\221\002\005\n\003\010\240\001\202\323\344\223\002)\"$/api/v1alpha1/org/trusts/rejecttrust:\001*'
  _globals['_TRUSTSSERVICE'].methods_by_name['GetTrust']._loaded_options = None
  _globals['_TRUSTSSERVICE'].methods_by_name['GetTrust']._serialized_options = b'\272\270\221\002\005\n\003\010\240\001\202\323\344\223\002&\"!/api/v1alpha1/org/trusts/gettrust:\001*'
  _globals['_TRUSTSSERVICE'].methods_by_name['ListIncomingTrusts']._loaded_options = None
  _globals['_TRUSTSSERVICE'].methods_by_name['ListIncomingTrusts']._serialized_options = b'\272\270\221\002\005\n\003\010\240\001\202\323\344\223\0025\"0/api/v1alpha1/org/trusts/list/listincomingtrusts:\001*'
  _globals['_TRUSTSSERVICE'].methods_by_name['ListGivenTrusts']._loaded_options = None
  _globals['_TRUSTSSERVICE'].methods_by_name['ListGivenTrusts']._serialized_options = b'\272\270\221\002\005\n\003\010\240\001\202\323\344\223\0022\"-/api/v1alpha1/org/trusts/list/listgiventrusts:\001*'
  _globals['_TRUSTSSERVICE'].methods_by_name['ListAssignableTrusts']._loaded_options = None
  _globals['_TRUSTSSERVICE'].methods_by_name['ListAssignableTrusts']._serialized_options = b'\272\270\221\002\005\n\003\010\240\001\202\323\344\223\0027\"2/api/v1alpha1/org/trusts/list/listassignabletrusts:\001*'
  _globals['_TRUSTSSERVICE'].methods_by_name['DeleteTrust']._loaded_options = None
  _globals['_TRUSTSSERVICE'].methods_by_name['DeleteTrust']._serialized_options = b'\272\270\221\002\005\n\003\010\240\001\202\323\344\223\002)\"$/api/v1alpha1/org/trusts/deletetrust:\001*'
  _globals['_TRUSTSSERVICE'].methods_by_name['AssignTrust']._loaded_options = None
  _globals['_TRUSTSSERVICE'].methods_by_name['AssignTrust']._serialized_options = b'\272\270\221\002\005\n\003\010\240\001\202\323\344\223\002)\"$/api/v1alpha1/org/trusts/assigntrust:\001*'
  _globals['_TRUSTSSERVICE'].methods_by_name['UnassignTrust']._loaded_options = None
  _globals['_TRUSTSSERVICE'].methods_by_name['UnassignTrust']._serialized_options = b'\272\270\221\002\005\n\003\010\240\001\202\323\344\223\002+\"&/api/v1alpha1/org/trusts/unassigntrust:\001*'
  _globals['_TRUSTSSERVICE']._serialized_start=512
  _globals['_TRUSTSSERVICE']._serialized_end=2138
# @@protoc_insertion_point(module_scope)
