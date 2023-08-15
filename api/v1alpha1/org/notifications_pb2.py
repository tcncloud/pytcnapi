# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/org/notifications.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.audit import event_types_pb2 as api_dot_commons_dot_audit_dot_event__types__pb2
from api.commons import notifications_pb2 as api_dot_commons_dot_notifications__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$api/v1alpha1/org/notifications.proto\x12\x10\x61pi.v1alpha1.org\x1a#api/commons/audit/event_types.proto\x1a\x1f\x61pi/commons/notifications.proto\x1a google/protobuf/field_mask.proto\"\xe6\x02\n\x10UserSubscription\x12\'\n\x0fsubscription_id\x18\x01 \x01(\tR\x0esubscriptionId\x12;\n\nevent_type\x18\x02 \x01(\x0e\x32\x1c.api.commons.audit.EventTypeR\teventType\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userId\x12\x46\n\x07room303\x18\x64 \x01(\x0b\x32*.api.v1alpha1.org.UserSubscription.Room303H\x00R\x07room303\x12\x37\n\x07\x66ilters\x18\x04 \x03(\x0b\x32\x1d.api.commons.FieldValueFilterR\x07\x66ilters\x12\x18\n\x07version\x18\x05 \x01(\x03R\x07version\x1a&\n\x07Room303\x12\x1b\n\troom_name\x18\x01 \x01(\tR\x08roomNameB\x10\n\x0e\x64\x65liver_method\"d\n\x1a\x41\x64\x64UserSubscriptionRequest\x12\x46\n\x0csubscription\x18\x01 \x01(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\x0csubscription\"e\n\x1b\x41\x64\x64UserSubscriptionResponse\x12\x46\n\x0csubscription\x18\x01 \x01(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\x0csubscription\"\x85\x01\n\"AddUserSubscriptionByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x46\n\x0csubscription\x18\x02 \x01(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\x0csubscription\"m\n#AddUserSubscriptionByUserIdResponse\x12\x46\n\x0csubscription\x18\x01 \x01(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\x0csubscription\"E\n\x1aGetUserSubscriptionRequest\x12\'\n\x0fsubscription_id\x18\x01 \x01(\tR\x0esubscriptionId\"e\n\x1bGetUserSubscriptionResponse\x12\x46\n\x0csubscription\x18\x01 \x01(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\x0csubscription\"f\n\"GetUserSubscriptionByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\'\n\x0fsubscription_id\x18\x02 \x01(\tR\x0esubscriptionId\"m\n#GetUserSubscriptionByUserIdResponse\x12\x46\n\x0csubscription\x18\x01 \x01(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\x0csubscription\"\xa2\x01\n\x1dUpdateUserSubscriptionRequest\x12\x46\n\x0csubscription\x18\x01 \x01(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\x0csubscription\x12\x39\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"h\n\x1eUpdateUserSubscriptionResponse\x12\x46\n\x0csubscription\x18\x01 \x01(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\x0csubscription\"\xaa\x01\n%UpdateUserSubscriptionByUserIdRequest\x12\x46\n\x0csubscription\x18\x01 \x01(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\x0csubscription\x12\x39\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"p\n&UpdateUserSubscriptionByUserIdResponse\x12\x46\n\x0csubscription\x18\x01 \x01(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\x0csubscription\"H\n\x1dRemoveUserSubscriptionRequest\x12\'\n\x0fsubscription_id\x18\x01 \x01(\tR\x0esubscriptionId\" \n\x1eRemoveUserSubscriptionResponse\"i\n%RemoveUserSubscriptionByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\'\n\x0fsubscription_id\x18\x02 \x01(\tR\x0esubscriptionId\"(\n&RemoveUserSubscriptionByUserIdResponse\"\x1e\n\x1cListUserSubscriptionsRequest\"i\n\x1dListUserSubscriptionsResponse\x12H\n\rsubscriptions\x18\x01 \x03(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\rsubscriptions\"?\n$ListUserSubscriptionsByUserIdRequest\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\"q\n%ListUserSubscriptionsByUserIdResponse\x12H\n\rsubscriptions\x18\x01 \x03(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\rsubscriptions\"q\n\x1bListOrgSubscriptionsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12;\n\nevent_type\x18\x02 \x01(\x0e\x32\x1c.api.commons.audit.EventTypeR\teventType\"h\n\x1cListOrgSubscriptionsResponse\x12H\n\rsubscriptions\x18\x01 \x03(\x0b\x32\".api.v1alpha1.org.UserSubscriptionR\rsubscriptionsB\x8c\x01\n\x14\x63om.api.v1alpha1.orgB\x12NotificationsProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.notifications_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024com.api.v1alpha1.orgB\022NotificationsProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_USERSUBSCRIPTION']._serialized_start=163
  _globals['_USERSUBSCRIPTION']._serialized_end=521
  _globals['_USERSUBSCRIPTION_ROOM303']._serialized_start=465
  _globals['_USERSUBSCRIPTION_ROOM303']._serialized_end=503
  _globals['_ADDUSERSUBSCRIPTIONREQUEST']._serialized_start=523
  _globals['_ADDUSERSUBSCRIPTIONREQUEST']._serialized_end=623
  _globals['_ADDUSERSUBSCRIPTIONRESPONSE']._serialized_start=625
  _globals['_ADDUSERSUBSCRIPTIONRESPONSE']._serialized_end=726
  _globals['_ADDUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_start=729
  _globals['_ADDUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_end=862
  _globals['_ADDUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_start=864
  _globals['_ADDUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_end=973
  _globals['_GETUSERSUBSCRIPTIONREQUEST']._serialized_start=975
  _globals['_GETUSERSUBSCRIPTIONREQUEST']._serialized_end=1044
  _globals['_GETUSERSUBSCRIPTIONRESPONSE']._serialized_start=1046
  _globals['_GETUSERSUBSCRIPTIONRESPONSE']._serialized_end=1147
  _globals['_GETUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_start=1149
  _globals['_GETUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_end=1251
  _globals['_GETUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_start=1253
  _globals['_GETUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_end=1362
  _globals['_UPDATEUSERSUBSCRIPTIONREQUEST']._serialized_start=1365
  _globals['_UPDATEUSERSUBSCRIPTIONREQUEST']._serialized_end=1527
  _globals['_UPDATEUSERSUBSCRIPTIONRESPONSE']._serialized_start=1529
  _globals['_UPDATEUSERSUBSCRIPTIONRESPONSE']._serialized_end=1633
  _globals['_UPDATEUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_start=1636
  _globals['_UPDATEUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_end=1806
  _globals['_UPDATEUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_start=1808
  _globals['_UPDATEUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_end=1920
  _globals['_REMOVEUSERSUBSCRIPTIONREQUEST']._serialized_start=1922
  _globals['_REMOVEUSERSUBSCRIPTIONREQUEST']._serialized_end=1994
  _globals['_REMOVEUSERSUBSCRIPTIONRESPONSE']._serialized_start=1996
  _globals['_REMOVEUSERSUBSCRIPTIONRESPONSE']._serialized_end=2028
  _globals['_REMOVEUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_start=2030
  _globals['_REMOVEUSERSUBSCRIPTIONBYUSERIDREQUEST']._serialized_end=2135
  _globals['_REMOVEUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_start=2137
  _globals['_REMOVEUSERSUBSCRIPTIONBYUSERIDRESPONSE']._serialized_end=2177
  _globals['_LISTUSERSUBSCRIPTIONSREQUEST']._serialized_start=2179
  _globals['_LISTUSERSUBSCRIPTIONSREQUEST']._serialized_end=2209
  _globals['_LISTUSERSUBSCRIPTIONSRESPONSE']._serialized_start=2211
  _globals['_LISTUSERSUBSCRIPTIONSRESPONSE']._serialized_end=2316
  _globals['_LISTUSERSUBSCRIPTIONSBYUSERIDREQUEST']._serialized_start=2318
  _globals['_LISTUSERSUBSCRIPTIONSBYUSERIDREQUEST']._serialized_end=2381
  _globals['_LISTUSERSUBSCRIPTIONSBYUSERIDRESPONSE']._serialized_start=2383
  _globals['_LISTUSERSUBSCRIPTIONSBYUSERIDRESPONSE']._serialized_end=2496
  _globals['_LISTORGSUBSCRIPTIONSREQUEST']._serialized_start=2498
  _globals['_LISTORGSUBSCRIPTIONSREQUEST']._serialized_end=2611
  _globals['_LISTORGSUBSCRIPTIONSRESPONSE']._serialized_start=2613
  _globals['_LISTORGSUBSCRIPTIONSRESPONSE']._serialized_end=2717
# @@protoc_insertion_point(module_scope)
