# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/users/notifications.proto
# Protobuf Python Version: 5.27.0
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
    0,
    '',
    'api/v1alpha1/org/users/notifications.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.audit import event_types_pb2 as api_dot_commons_dot_audit_dot_event__types__pb2
from api.commons import notifications_pb2 as api_dot_commons_dot_notifications__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*api/v1alpha1/org/users/notifications.proto\x12\x16\x61pi.v1alpha1.org.users\x1a#api/commons/audit/event_types.proto\x1a\x1f\x61pi/commons/notifications.proto\x1a google/protobuf/field_mask.proto\"\xfc\x03\n\x10UserSubscription\x12\'\n\x0fsubscription_id\x18\x01 \x01(\tR\x0esubscriptionId\x12;\n\nevent_type\x18\x02 \x01(\x0e\x32\x1c.api.commons.audit.EventTypeR\teventType\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userId\x12L\n\x07room303\x18\x64 \x01(\x0b\x32\x30.api.v1alpha1.org.users.UserSubscription.Room303H\x00R\x07room303\x12P\n\x08\x64\x65livery\x18\xc8\x01 \x01(\x0b\x32\x31.api.v1alpha1.org.users.UserSubscription.DeliveryH\x00R\x08\x64\x65livery\x12\x37\n\x07\x66ilters\x18\x04 \x03(\x0b\x32\x1d.api.commons.FieldValueFilterR\x07\x66ilters\x12\x18\n\x07version\x18\x05 \x01(\x03R\x07version\x1a&\n\x07Room303\x12\x1b\n\troom_name\x18\x01 \x01(\tR\x08roomName\x1a<\n\x08\x44\x65livery\x12\x30\n\x14transfer_config_name\x18\x01 \x01(\tR\x12transferConfigNameB\x10\n\x0e\x64\x65liver_method\"j\n\x1a\x41\x64\x64UserSubscriptionRequest\x12L\n\x0csubscription\x18\x01 \x01(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\x0csubscription\"k\n\x1b\x41\x64\x64UserSubscriptionResponse\x12L\n\x0csubscription\x18\x01 \x01(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\x0csubscription\"\x8b\x01\n\"AddUserSubscriptionByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12L\n\x0csubscription\x18\x02 \x01(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\x0csubscription\"s\n#AddUserSubscriptionByUserIdResponse\x12L\n\x0csubscription\x18\x01 \x01(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\x0csubscription\"E\n\x1aGetUserSubscriptionRequest\x12\'\n\x0fsubscription_id\x18\x01 \x01(\tR\x0esubscriptionId\"k\n\x1bGetUserSubscriptionResponse\x12L\n\x0csubscription\x18\x01 \x01(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\x0csubscription\"f\n\"GetUserSubscriptionByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\'\n\x0fsubscription_id\x18\x02 \x01(\tR\x0esubscriptionId\"s\n#GetUserSubscriptionByUserIdResponse\x12L\n\x0csubscription\x18\x01 \x01(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\x0csubscription\"\xa8\x01\n\x1dUpdateUserSubscriptionRequest\x12L\n\x0csubscription\x18\x01 \x01(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\x0csubscription\x12\x39\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"n\n\x1eUpdateUserSubscriptionResponse\x12L\n\x0csubscription\x18\x01 \x01(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\x0csubscription\"\xb0\x01\n%UpdateUserSubscriptionByUserIdRequest\x12L\n\x0csubscription\x18\x01 \x01(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\x0csubscription\x12\x39\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"v\n&UpdateUserSubscriptionByUserIdResponse\x12L\n\x0csubscription\x18\x01 \x01(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\x0csubscription\"H\n\x1dRemoveUserSubscriptionRequest\x12\'\n\x0fsubscription_id\x18\x01 \x01(\tR\x0esubscriptionId\" \n\x1eRemoveUserSubscriptionResponse\"i\n%RemoveUserSubscriptionByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\'\n\x0fsubscription_id\x18\x02 \x01(\tR\x0esubscriptionId\"(\n&RemoveUserSubscriptionByUserIdResponse\"\x1e\n\x1cListUserSubscriptionsRequest\"o\n\x1dListUserSubscriptionsResponse\x12N\n\rsubscriptions\x18\x01 \x03(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\rsubscriptions\"?\n$ListUserSubscriptionsByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"w\n%ListUserSubscriptionsByUserIdResponse\x12N\n\rsubscriptions\x18\x01 \x03(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\rsubscriptions\"q\n\x1bListOrgSubscriptionsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12;\n\nevent_type\x18\x02 \x01(\x0e\x32\x1c.api.commons.audit.EventTypeR\teventType\"n\n\x1cListOrgSubscriptionsResponse\x12N\n\rsubscriptions\x18\x01 \x03(\x0b\x32(.api.v1alpha1.org.users.UserSubscriptionR\rsubscriptionsB\xac\x01\n\x1a\x63om.api.v1alpha1.org.usersB\x12NotificationsProtoP\x01\xa2\x02\x04\x41VOU\xaa\x02\x16\x41pi.V1alpha1.Org.Users\xca\x02\x16\x41pi\\V1alpha1\\Org\\Users\xe2\x02\"Api\\V1alpha1\\Org\\Users\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Org::Usersb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.users.notifications_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.api.v1alpha1.org.usersB\022NotificationsProtoP\001\242\002\004AVOU\252\002\026Api.V1alpha1.Org.Users\312\002\026Api\\V1alpha1\\Org\\Users\342\002\"Api\\V1alpha1\\Org\\Users\\GPBMetadata\352\002\031Api::V1alpha1::Org::Users'
  _globals['_USERSUBSCRIPTION']._serialized_start=175
  _globals['_USERSUBSCRIPTION']._serialized_end=683
  _globals['_USERSUBSCRIPTION_ROOM303']._serialized_start=565
  _globals['_USERSUBSCRIPTION_ROOM303']._serialized_end=603
  _globals['_USERSUBSCRIPTION_DELIVERY']._serialized_start=605
  _globals['_USERSUBSCRIPTION_DELIVERY']._serialized_end=665
  _globals['_ADDUSERSUBSCRIPTIONREQUEST']._serialized_start=685
  _globals['_ADDUSERSUBSCRIPTIONREQUEST']._serialized_end=791
  _globals['_ADDUSERSUBSCRIPTIONRESPONSE']._serialized_start=793
  _globals['_ADDUSERSUBSCRIPTIONRESPONSE']._serialized_end=900
  _globals['_ADDUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_start=903
  _globals['_ADDUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_end=1042
  _globals['_ADDUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_start=1044
  _globals['_ADDUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_end=1159
  _globals['_GETUSERSUBSCRIPTIONREQUEST']._serialized_start=1161
  _globals['_GETUSERSUBSCRIPTIONREQUEST']._serialized_end=1230
  _globals['_GETUSERSUBSCRIPTIONRESPONSE']._serialized_start=1232
  _globals['_GETUSERSUBSCRIPTIONRESPONSE']._serialized_end=1339
  _globals['_GETUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_start=1341
  _globals['_GETUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_end=1443
  _globals['_GETUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_start=1445
  _globals['_GETUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_end=1560
  _globals['_UPDATEUSERSUBSCRIPTIONREQUEST']._serialized_start=1563
  _globals['_UPDATEUSERSUBSCRIPTIONREQUEST']._serialized_end=1731
  _globals['_UPDATEUSERSUBSCRIPTIONRESPONSE']._serialized_start=1733
  _globals['_UPDATEUSERSUBSCRIPTIONRESPONSE']._serialized_end=1843
  _globals['_UPDATEUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_start=1846
  _globals['_UPDATEUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_end=2022
  _globals['_UPDATEUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_start=2024
  _globals['_UPDATEUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_end=2142
  _globals['_REMOVEUSERSUBSCRIPTIONREQUEST']._serialized_start=2144
  _globals['_REMOVEUSERSUBSCRIPTIONREQUEST']._serialized_end=2216
  _globals['_REMOVEUSERSUBSCRIPTIONRESPONSE']._serialized_start=2218
  _globals['_REMOVEUSERSUBSCRIPTIONRESPONSE']._serialized_end=2250
  _globals['_REMOVEUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_start=2252
  _globals['_REMOVEUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_end=2357
  _globals['_REMOVEUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_start=2359
  _globals['_REMOVEUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_end=2399
  _globals['_LISTUSERSUBSCRIPTIONSREQUEST']._serialized_start=2401
  _globals['_LISTUSERSUBSCRIPTIONSREQUEST']._serialized_end=2431
  _globals['_LISTUSERSUBSCRIPTIONSRESPONSE']._serialized_start=2433
  _globals['_LISTUSERSUBSCRIPTIONSRESPONSE']._serialized_end=2544
  _globals['_LISTUSERSUBSCRIPTIONSBYUSERIDREQUEST']._serialized_start=2546
  _globals['_LISTUSERSUBSCRIPTIONSBYUSERIDREQUEST']._serialized_end=2609
  _globals['_LISTUSERSUBSCRIPTIONSBYUSERIDRESPONSE']._serialized_start=2611
  _globals['_LISTUSERSUBSCRIPTIONSBYUSERIDRESPONSE']._serialized_end=2730
  _globals['_LISTORGSUBSCRIPTIONSREQUEST']._serialized_start=2732
  _globals['_LISTORGSUBSCRIPTIONSREQUEST']._serialized_end=2845
  _globals['_LISTORGSUBSCRIPTIONSRESPONSE']._serialized_start=2847
  _globals['_LISTORGSUBSCRIPTIONSRESPONSE']._serialized_end=2957
# @@protoc_insertion_point(module_scope)
