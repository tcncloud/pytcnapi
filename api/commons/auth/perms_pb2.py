# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/auth/perms.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations.perms import tcn_pb2 as annotations_dot_perms_dot_tcn__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/commons/auth/perms.proto\x12\x10\x61pi.commons.auth\x1a\x1b\x61nnotations/perms/tcn.proto*\x9c!\n\nPermission\x12\x1a\n\x16PERMISSION_UNSPECIFIED\x10\x00\x12\x12\n\x0ePERMISSION_DEV\x10\x01\x12\x19\n\x15PERMISSION_LEARN_EDIT\x10\n\x12!\n\x13PERMISSION_ORG_EDIT\x10\x64\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x01\x12K\n\x13PERMISSION_ORG_VIEW\x10\x65\x1a\x32\x8a\xb5\x18.\x10\t\x18\x01\"\x08Overview\"\x11\x43\x61mpaign Settings\"\x0bPreferences\x12L\n\x1fPERMISSION_OWNING_ORG_IMITATION\x10\x82\x01\x1a&\x8a\xb5\x18\"\x10\t\x18\x01\"\x1cImitate Within Org Hierarchy\x12$\n\x16PERMISSION_USER_CREATE\x10v\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x02\x12\"\n\x14PERMISSION_USER_EDIT\x10w\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x02\x12+\n\x1dPERMISSION_USER_EDIT_PASSWORD\x10x\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x02\x12*\n\x1cPERMISSION_USER_EDIT_OPTIONS\x10y\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x02\x12+\n\x1cPERMISSION_LOGIN_CONNECTIONS\x10\x84\x02\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x02\x12\x32\n$PERMISSION_USER_EDIT_AGENT_CALLER_ID\x10z\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x03\x12\x64\n\x1bPERMISSION_AGENT_MANAGEMENT\x10\x90\x03\x1a\x42\x8a\xb5\x18>\x10\t\x18\x03\"\x0eProfile Groups\"\nExtensions\"\x14Statistics Templates\"\x06Skills\x12.\n PERMISSION_PERMISSION_GROUP_EDIT\x10n\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x04\x12\x30\n\"PERMISSION_PERMISSION_GROUP_ASSIGN\x10o\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x04\x12*\n\x1bPERMISSION_LABEL_MANAGEMENT\x10\x96\x01\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x05\x12,\n\x1bPERMISSION_TRUST_MANAGEMENT\x10\xa0\x01\x1a\n\x8a\xb5\x18\x06\x08\x01\x10\t\x18\x06\x12\x95\x01\n\x19PERMISSION_HUNTGROUP_VIEW\x10\xec\x0e\x1au\x8a\xb5\x18q\x10\t\x18\x07\"\rGroup Scripts\"\rPause Options\"\x12Web Link Templates\"\x10Group Extensions\"\x11Trigger Templates\"\x14\x44isplay Limited Keys\x12(\n\x19PERMISSION_HUNTGROUP_EDIT\x10\xed\x0e\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x07\x12)\n\x1aPERMISSION_SOUNDBOARD_VIEW\x10\xa4\r\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x08\x12)\n\x1aPERMISSION_SOUNDBOARD_EDIT\x10\xa5\r\x1a\x08\x8a\xb5\x18\x04\x10\t\x18\x08\x12Y\n\"PERMISSION_SUBSCRIPTION_MANAGEMENT\x10\x8c\x01\x1a\x30\x8a\xb5\x18,\x10\t\x18\t\"\x10My Subscriptions\"\x14Manage Subscriptions\x12 \n\x1bPERMISSION_CUSTOMER_SUPPORT\x10\xc8\x01\x12\x19\n\x14PERMISSION_IMITATION\x10\xd2\x01\x12\x1c\n\x17PERMISSION_BILLING_EDIT\x10\xdc\x01\x12\"\n\x1dPERMISSION_TCN_ADMIN_SETTINGS\x10\xe6\x01\x12\x1b\n\x16PERMISSION_TCN_BILLING\x10\xf0\x01\x12\x1d\n\x10PERMISSION_AGENT\x10\xac\x02\x1a\x06\x8a\xb5\x18\x02\x10\x01\x12+\n\x1ePERMISSION_ACCEPT_QUEUED_CALLS\x10\xb6\x02\x1a\x06\x8a\xb5\x18\x02\x10\x01\x12\x30\n#PERMISSION_VIEW_CAMPAIGN_COMPLETION\x10\xc0\x02\x1a\x06\x8a\xb5\x18\x02\x10\x01\x12\'\n\x1aPERMISSION_VIEW_VOICE_MAIL\x10\xc1\x02\x1a\x06\x8a\xb5\x18\x02\x10\x01\x12:\n-PERMISSION_AGENT_COMPLIANCE_SCRUBLIST_OPTIONS\x10\xca\x02\x1a\x06\x8a\xb5\x18\x02\x10\x01\x12&\n\x19PERMISSION_EXTENSION_EDIT\x10\xf8\n\x1a\x06\x8a\xb5\x18\x02\x10\x01\x12*\n\x1dPERMISSION_VOICEMAIL_DOWNLOAD\x10\xf9\n\x1a\x06\x8a\xb5\x18\x02\x10\x01\x12\x33\n\x1dPERMISSION_AGENT_PORTALS_VIEW\x10\xd4\x02\x1a\x0f\x8a\xb5\x18\x0b\x10\x01\"\x07Portals\x12Q\n\x1aPERMISSION_VOICE_ANALYTICS\x10\xf4\x03\x1a\x30\x8a\xb5\x18,\x10\x0e\"\x07\x42illing\"\x0fMonthly Billing\"\x0e\x42illing Report\x12,\n\x1fPERMISSION_VOICE_ANALYTICS_FLAG\x10\xf5\x03\x1a\x06\x8a\xb5\x18\x02\x10\x0e\x12.\n!PERMISSION_VOICE_ANALYTICS_CONFIG\x10\xf6\x03\x1a\x06\x8a\xb5\x18\x02\x10\x0e\x12:\n-PERMISSION_VOICE_ANALYTICS_RECORDING_DOWNLOAD\x10\xf7\x03\x1a\x06\x8a\xb5\x18\x02\x10\x0e\x12;\n.PERMISSION_VOICE_ANALYTICS_TRANSCRIPT_DOWNLOAD\x10\xf8\x03\x1a\x06\x8a\xb5\x18\x02\x10\x0e\x12\x38\n+PERMISSION_VOICE_ANALYTICS_SCREEN_RECORDING\x10\xf9\x03\x1a\x06\x8a\xb5\x18\x02\x10\x0e\x12\x39\n,PERMISSION_VOICE_ANALYTICS_TRANSCRIPT_DELETE\x10\xfa\x03\x1a\x06\x8a\xb5\x18\x02\x10\x0e\x12\x41\n2PERMISSION_VOICE_ANALYTICS_SCREEN_RECORDING_DELETE\x10\xfb\x03\x1a\x08\x8a\xb5\x18\x04\x08\x01\x10\x0e\x12P\n PERMISSION_BUSINESS_INTELLIGENCE\x10\xd8\x04\x1a)\x8a\xb5\x18%\x10\x02\"\x06Viewer\"\x07\x42uilder\"\x10Legacy Analytics\x12/\n\x1aPERMISSION_DASHBOARDS_VIEW\x10\xd9\x04\x1a\x0e\x8a\xb5\x18\n\x10\x02\"\x06Viewer\x12\x42\n\x1aPERMISSION_DASHBOARDS_EDIT\x10\xda\x04\x1a!\x8a\xb5\x18\x1d\x10\x02\"\x07\x42uilder\"\x10Legacy Analytics\x12\x38\n)PERMISSION_INSIGHTS_COMMON_LIBRARY_MANAGE\x10\xdb\x04\x1a\x08\x8a\xb5\x18\x04\x08\x01\x10\x02\x12\x38\n\x1aPERMISSION_INSIGHTS_MANAGE\x10\xdc\x04\x1a\x17\x8a\xb5\x18\x13\x10\x02\"\x0fInsight Builder\x12Y\n\x12PERMISSION_ROOM303\x10\xbc\x05\x1a@\x8a\xb5\x18<\x10\n\"\x0fUnread Messages\"\x05Rooms\"\x0f\x44irect Messages\"\x0fSystem Messages\x12J\n\x1dPERMISSION_AGENT_CALL_SCRIPTS\x10\xa0\x06\x1a&\x8a\xb5\x18\"\x10\x0c\"\x0eScript Builder\"\x0eScript Mapping\x12\x45\n\x15PERMISSION_COMPLIANCE\x10\x84\x07\x1a)\x8a\xb5\x18%\x10\x07\"\tRule Sets\"\x0bScrub Lists\"\tScenarios\x12\x33\n\x1dPERMISSION_COMPLIANCE_CONSENT\x10\x8e\x07\x1a\x0f\x8a\xb5\x18\x0b\x10\x07\"\x07\x43onsent\x12\x96\x01\n\x13PERMISSION_LMS_VIEW\x10\xe8\x07\x1a|\x8a\xb5\x18x\x10\x06\"\x0c\x44\x61ta Manager\"\x15\x46ile Template Manager\"\x1d\x46ile Field Definition Manager\"\x15Journey Data Explorer\"\x19New File Template Manager\x12 \n\x13PERMISSION_LMS_EDIT\x10\xe9\x07\x1a\x06\x8a\xb5\x18\x02\x10\x06\x12n\n\x14PERMISSION_OMNI_BOSS\x10\xb0\t\x1aS\x8a\xb5\x18O\x10\x08\"\x0cSSO Settings\"\x0b\x46orm Emails\"\x0f\x43\x61nned Messages\"\x0c\x44ispositions\"\x11Unsubscribe Links\x12\x32\n\x1cPERMISSION_OMNI_PORTALS_VIEW\x10\xba\t\x1a\x0f\x8a\xb5\x18\x0b\x10\x08\"\x07Portals\x12K\n\x1cPERMISSION_INTEGRATIONS_VIEW\x10\x94\n\x1a(\x8a\xb5\x18$\x10\x05\"\x0e\x43onfigurations\"\x07Plugins\"\x07Portals\x12\x42\n\x1fPERMISSION_INTEGRATIONS_PAYMENT\x10\x95\n\x1a\x1c\x8a\xb5\x18\x18\x10\x05\"\x14Payment Integrations\x12\x42\n\x1fPERMISSION_INTEGRATIONS_JOURNEY\x10\x96\n\x1a\x1c\x8a\xb5\x18\x18\x10\x05\"\x14Journey Integrations\x12\xb0\x01\n\x0ePERMISSION_WFM\x10\xdc\x0b\x1a\x9a\x01\x8a\xb5\x18\x95\x01\x10\x0f\"\nForecaster\"\x0eSkill Profiles\"\x16\x46orecasting Parameters\"\x13Profile Forecasting\"\x16Regression Forecasting\"\x13\x43urrent Forecasting\"\tScheduler\"\x10\x41gent Management\x12\"\n\x15PERMISSION_SCORECARDS\x10\xc0\x0c\x1a\x06\x8a\xb5\x18\x02\x10\x0b\x12)\n\x1cPERMISSION_SCORECARDS_MANAGE\x10\xc1\x0c\x1a\x06\x8a\xb5\x18\x02\x10\x0b\x12+\n\x1ePERMISSION_SCORECARDS_EVALUATE\x10\xc2\x0c\x1a\x06\x8a\xb5\x18\x02\x10\x0b\x12,\n\x1fPERMISSION_SCORECARDS_FLAG_EVAL\x10\xc3\x0c\x1a\x06\x8a\xb5\x18\x02\x10\x0b\x12/\n\x14PERMISSION_DEV_TOOLS\x10\x88\x0e\x1a\x14\x8a\xb5\x18\x10\x10\x04\"\x0c\x41PI Explorer\x12\x33\n&PERMISSION_DELIVERY_NOTIFICATIONS_VIEW\x10\xd0\x0f\x1a\x06\x8a\xb5\x18\x02\x10\x03\x12\x33\n&PERMISSION_DELIVERY_NOTIFICATIONS_EDIT\x10\xd1\x0f\x1a\x06\x8a\xb5\x18\x02\x10\x03\x12%\n\x16PERMISSION_TICKETS_APP\x10\x9c\x18\x1a\x08\x8a\xb5\x18\x04\x08\x01\x10\r\x12\'\n\x18PERMISSION_TICKETS_ADMIN\x10\x9d\x18\x1a\x08\x8a\xb5\x18\x04\x08\x01\x10\r\x12!\n\x14PERMISSION_WORKFLOWS\x10\xa0\x1f\x1a\x06\x8a\xb5\x18\x02\x10\x10\x12Y\n\x1bPERMISSION_PBX_MANAGER_VIEW\x10\x84 \x1a\x37\x8a\xb5\x18\x33\x10\t\x18\n\"\x12PBX User Managment\"\x19\x45xtension Group Managment\x12Y\n\x1bPERMISSION_PBX_MANAGER_EDIT\x10\x85 \x1a\x37\x8a\xb5\x18\x33\x10\t\x18\n\"\x12PBX User Managment\"\x19\x45xtension Group Managment\x12%\n\x18PERMISSION_NEWSROOM_EDIT\x10\xe8 \x1a\x06\x8a\xb5\x18\x02\x10\x11\x12(\n\x1bPERMISSION_NEWSROOM_PUBLISH\x10\xe9 \x1a\x06\x8a\xb5\x18\x02\x10\x11\x42\x84\x01\n\x14\x63om.api.commons.authB\nPermsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x10\x41pi.Commons.Auth\xca\x02\x10\x41pi\\Commons\\Auth\xe2\x02\x1c\x41pi\\Commons\\Auth\\GPBMetadata\xea\x02\x12\x41pi::Commons::Authb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.auth.perms_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024com.api.commons.authB\nPermsProtoP\001\242\002\003ACA\252\002\020Api.Commons.Auth\312\002\020Api\\Commons\\Auth\342\002\034Api\\Commons\\Auth\\GPBMetadata\352\002\022Api::Commons::Auth'
  _PERMISSION.values_by_name["PERMISSION_ORG_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_ORG_EDIT"]._serialized_options = b'\212\265\030\004\020\t\030\001'
  _PERMISSION.values_by_name["PERMISSION_ORG_VIEW"]._options = None
  _PERMISSION.values_by_name["PERMISSION_ORG_VIEW"]._serialized_options = b'\212\265\030.\020\t\030\001\"\010Overview\"\021Campaign Settings\"\013Preferences'
  _PERMISSION.values_by_name["PERMISSION_OWNING_ORG_IMITATION"]._options = None
  _PERMISSION.values_by_name["PERMISSION_OWNING_ORG_IMITATION"]._serialized_options = b'\212\265\030\"\020\t\030\001\"\034Imitate Within Org Hierarchy'
  _PERMISSION.values_by_name["PERMISSION_USER_CREATE"]._options = None
  _PERMISSION.values_by_name["PERMISSION_USER_CREATE"]._serialized_options = b'\212\265\030\004\020\t\030\002'
  _PERMISSION.values_by_name["PERMISSION_USER_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_USER_EDIT"]._serialized_options = b'\212\265\030\004\020\t\030\002'
  _PERMISSION.values_by_name["PERMISSION_USER_EDIT_PASSWORD"]._options = None
  _PERMISSION.values_by_name["PERMISSION_USER_EDIT_PASSWORD"]._serialized_options = b'\212\265\030\004\020\t\030\002'
  _PERMISSION.values_by_name["PERMISSION_USER_EDIT_OPTIONS"]._options = None
  _PERMISSION.values_by_name["PERMISSION_USER_EDIT_OPTIONS"]._serialized_options = b'\212\265\030\004\020\t\030\002'
  _PERMISSION.values_by_name["PERMISSION_LOGIN_CONNECTIONS"]._options = None
  _PERMISSION.values_by_name["PERMISSION_LOGIN_CONNECTIONS"]._serialized_options = b'\212\265\030\004\020\t\030\002'
  _PERMISSION.values_by_name["PERMISSION_USER_EDIT_AGENT_CALLER_ID"]._options = None
  _PERMISSION.values_by_name["PERMISSION_USER_EDIT_AGENT_CALLER_ID"]._serialized_options = b'\212\265\030\004\020\t\030\003'
  _PERMISSION.values_by_name["PERMISSION_AGENT_MANAGEMENT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_AGENT_MANAGEMENT"]._serialized_options = b'\212\265\030>\020\t\030\003\"\016Profile Groups\"\nExtensions\"\024Statistics Templates\"\006Skills'
  _PERMISSION.values_by_name["PERMISSION_PERMISSION_GROUP_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_PERMISSION_GROUP_EDIT"]._serialized_options = b'\212\265\030\004\020\t\030\004'
  _PERMISSION.values_by_name["PERMISSION_PERMISSION_GROUP_ASSIGN"]._options = None
  _PERMISSION.values_by_name["PERMISSION_PERMISSION_GROUP_ASSIGN"]._serialized_options = b'\212\265\030\004\020\t\030\004'
  _PERMISSION.values_by_name["PERMISSION_LABEL_MANAGEMENT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_LABEL_MANAGEMENT"]._serialized_options = b'\212\265\030\004\020\t\030\005'
  _PERMISSION.values_by_name["PERMISSION_TRUST_MANAGEMENT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_TRUST_MANAGEMENT"]._serialized_options = b'\212\265\030\006\010\001\020\t\030\006'
  _PERMISSION.values_by_name["PERMISSION_HUNTGROUP_VIEW"]._options = None
  _PERMISSION.values_by_name["PERMISSION_HUNTGROUP_VIEW"]._serialized_options = b'\212\265\030q\020\t\030\007\"\rGroup Scripts\"\rPause Options\"\022Web Link Templates\"\020Group Extensions\"\021Trigger Templates\"\024Display Limited Keys'
  _PERMISSION.values_by_name["PERMISSION_HUNTGROUP_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_HUNTGROUP_EDIT"]._serialized_options = b'\212\265\030\004\020\t\030\007'
  _PERMISSION.values_by_name["PERMISSION_SOUNDBOARD_VIEW"]._options = None
  _PERMISSION.values_by_name["PERMISSION_SOUNDBOARD_VIEW"]._serialized_options = b'\212\265\030\004\020\t\030\010'
  _PERMISSION.values_by_name["PERMISSION_SOUNDBOARD_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_SOUNDBOARD_EDIT"]._serialized_options = b'\212\265\030\004\020\t\030\010'
  _PERMISSION.values_by_name["PERMISSION_SUBSCRIPTION_MANAGEMENT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_SUBSCRIPTION_MANAGEMENT"]._serialized_options = b'\212\265\030,\020\t\030\t\"\020My Subscriptions\"\024Manage Subscriptions'
  _PERMISSION.values_by_name["PERMISSION_AGENT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_AGENT"]._serialized_options = b'\212\265\030\002\020\001'
  _PERMISSION.values_by_name["PERMISSION_ACCEPT_QUEUED_CALLS"]._options = None
  _PERMISSION.values_by_name["PERMISSION_ACCEPT_QUEUED_CALLS"]._serialized_options = b'\212\265\030\002\020\001'
  _PERMISSION.values_by_name["PERMISSION_VIEW_CAMPAIGN_COMPLETION"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VIEW_CAMPAIGN_COMPLETION"]._serialized_options = b'\212\265\030\002\020\001'
  _PERMISSION.values_by_name["PERMISSION_VIEW_VOICE_MAIL"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VIEW_VOICE_MAIL"]._serialized_options = b'\212\265\030\002\020\001'
  _PERMISSION.values_by_name["PERMISSION_AGENT_COMPLIANCE_SCRUBLIST_OPTIONS"]._options = None
  _PERMISSION.values_by_name["PERMISSION_AGENT_COMPLIANCE_SCRUBLIST_OPTIONS"]._serialized_options = b'\212\265\030\002\020\001'
  _PERMISSION.values_by_name["PERMISSION_EXTENSION_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_EXTENSION_EDIT"]._serialized_options = b'\212\265\030\002\020\001'
  _PERMISSION.values_by_name["PERMISSION_VOICEMAIL_DOWNLOAD"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VOICEMAIL_DOWNLOAD"]._serialized_options = b'\212\265\030\002\020\001'
  _PERMISSION.values_by_name["PERMISSION_AGENT_PORTALS_VIEW"]._options = None
  _PERMISSION.values_by_name["PERMISSION_AGENT_PORTALS_VIEW"]._serialized_options = b'\212\265\030\013\020\001\"\007Portals'
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS"]._serialized_options = b'\212\265\030,\020\016\"\007Billing\"\017Monthly Billing\"\016Billing Report'
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_FLAG"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_FLAG"]._serialized_options = b'\212\265\030\002\020\016'
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_CONFIG"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_CONFIG"]._serialized_options = b'\212\265\030\002\020\016'
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_RECORDING_DOWNLOAD"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_RECORDING_DOWNLOAD"]._serialized_options = b'\212\265\030\002\020\016'
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_TRANSCRIPT_DOWNLOAD"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_TRANSCRIPT_DOWNLOAD"]._serialized_options = b'\212\265\030\002\020\016'
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_SCREEN_RECORDING"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_SCREEN_RECORDING"]._serialized_options = b'\212\265\030\002\020\016'
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_TRANSCRIPT_DELETE"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_TRANSCRIPT_DELETE"]._serialized_options = b'\212\265\030\002\020\016'
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_SCREEN_RECORDING_DELETE"]._options = None
  _PERMISSION.values_by_name["PERMISSION_VOICE_ANALYTICS_SCREEN_RECORDING_DELETE"]._serialized_options = b'\212\265\030\004\010\001\020\016'
  _PERMISSION.values_by_name["PERMISSION_BUSINESS_INTELLIGENCE"]._options = None
  _PERMISSION.values_by_name["PERMISSION_BUSINESS_INTELLIGENCE"]._serialized_options = b'\212\265\030%\020\002\"\006Viewer\"\007Builder\"\020Legacy Analytics'
  _PERMISSION.values_by_name["PERMISSION_DASHBOARDS_VIEW"]._options = None
  _PERMISSION.values_by_name["PERMISSION_DASHBOARDS_VIEW"]._serialized_options = b'\212\265\030\n\020\002\"\006Viewer'
  _PERMISSION.values_by_name["PERMISSION_DASHBOARDS_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_DASHBOARDS_EDIT"]._serialized_options = b'\212\265\030\035\020\002\"\007Builder\"\020Legacy Analytics'
  _PERMISSION.values_by_name["PERMISSION_INSIGHTS_COMMON_LIBRARY_MANAGE"]._options = None
  _PERMISSION.values_by_name["PERMISSION_INSIGHTS_COMMON_LIBRARY_MANAGE"]._serialized_options = b'\212\265\030\004\010\001\020\002'
  _PERMISSION.values_by_name["PERMISSION_INSIGHTS_MANAGE"]._options = None
  _PERMISSION.values_by_name["PERMISSION_INSIGHTS_MANAGE"]._serialized_options = b'\212\265\030\023\020\002\"\017Insight Builder'
  _PERMISSION.values_by_name["PERMISSION_ROOM303"]._options = None
  _PERMISSION.values_by_name["PERMISSION_ROOM303"]._serialized_options = b'\212\265\030<\020\n\"\017Unread Messages\"\005Rooms\"\017Direct Messages\"\017System Messages'
  _PERMISSION.values_by_name["PERMISSION_AGENT_CALL_SCRIPTS"]._options = None
  _PERMISSION.values_by_name["PERMISSION_AGENT_CALL_SCRIPTS"]._serialized_options = b'\212\265\030\"\020\014\"\016Script Builder\"\016Script Mapping'
  _PERMISSION.values_by_name["PERMISSION_COMPLIANCE"]._options = None
  _PERMISSION.values_by_name["PERMISSION_COMPLIANCE"]._serialized_options = b'\212\265\030%\020\007\"\tRule Sets\"\013Scrub Lists\"\tScenarios'
  _PERMISSION.values_by_name["PERMISSION_COMPLIANCE_CONSENT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_COMPLIANCE_CONSENT"]._serialized_options = b'\212\265\030\013\020\007\"\007Consent'
  _PERMISSION.values_by_name["PERMISSION_LMS_VIEW"]._options = None
  _PERMISSION.values_by_name["PERMISSION_LMS_VIEW"]._serialized_options = b'\212\265\030x\020\006\"\014Data Manager\"\025File Template Manager\"\035File Field Definition Manager\"\025Journey Data Explorer\"\031New File Template Manager'
  _PERMISSION.values_by_name["PERMISSION_LMS_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_LMS_EDIT"]._serialized_options = b'\212\265\030\002\020\006'
  _PERMISSION.values_by_name["PERMISSION_OMNI_BOSS"]._options = None
  _PERMISSION.values_by_name["PERMISSION_OMNI_BOSS"]._serialized_options = b'\212\265\030O\020\010\"\014SSO Settings\"\013Form Emails\"\017Canned Messages\"\014Dispositions\"\021Unsubscribe Links'
  _PERMISSION.values_by_name["PERMISSION_OMNI_PORTALS_VIEW"]._options = None
  _PERMISSION.values_by_name["PERMISSION_OMNI_PORTALS_VIEW"]._serialized_options = b'\212\265\030\013\020\010\"\007Portals'
  _PERMISSION.values_by_name["PERMISSION_INTEGRATIONS_VIEW"]._options = None
  _PERMISSION.values_by_name["PERMISSION_INTEGRATIONS_VIEW"]._serialized_options = b'\212\265\030$\020\005\"\016Configurations\"\007Plugins\"\007Portals'
  _PERMISSION.values_by_name["PERMISSION_INTEGRATIONS_PAYMENT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_INTEGRATIONS_PAYMENT"]._serialized_options = b'\212\265\030\030\020\005\"\024Payment Integrations'
  _PERMISSION.values_by_name["PERMISSION_INTEGRATIONS_JOURNEY"]._options = None
  _PERMISSION.values_by_name["PERMISSION_INTEGRATIONS_JOURNEY"]._serialized_options = b'\212\265\030\030\020\005\"\024Journey Integrations'
  _PERMISSION.values_by_name["PERMISSION_WFM"]._options = None
  _PERMISSION.values_by_name["PERMISSION_WFM"]._serialized_options = b'\212\265\030\225\001\020\017\"\nForecaster\"\016Skill Profiles\"\026Forecasting Parameters\"\023Profile Forecasting\"\026Regression Forecasting\"\023Current Forecasting\"\tScheduler\"\020Agent Management'
  _PERMISSION.values_by_name["PERMISSION_SCORECARDS"]._options = None
  _PERMISSION.values_by_name["PERMISSION_SCORECARDS"]._serialized_options = b'\212\265\030\002\020\013'
  _PERMISSION.values_by_name["PERMISSION_SCORECARDS_MANAGE"]._options = None
  _PERMISSION.values_by_name["PERMISSION_SCORECARDS_MANAGE"]._serialized_options = b'\212\265\030\002\020\013'
  _PERMISSION.values_by_name["PERMISSION_SCORECARDS_EVALUATE"]._options = None
  _PERMISSION.values_by_name["PERMISSION_SCORECARDS_EVALUATE"]._serialized_options = b'\212\265\030\002\020\013'
  _PERMISSION.values_by_name["PERMISSION_SCORECARDS_FLAG_EVAL"]._options = None
  _PERMISSION.values_by_name["PERMISSION_SCORECARDS_FLAG_EVAL"]._serialized_options = b'\212\265\030\002\020\013'
  _PERMISSION.values_by_name["PERMISSION_DEV_TOOLS"]._options = None
  _PERMISSION.values_by_name["PERMISSION_DEV_TOOLS"]._serialized_options = b'\212\265\030\020\020\004\"\014API Explorer'
  _PERMISSION.values_by_name["PERMISSION_DELIVERY_NOTIFICATIONS_VIEW"]._options = None
  _PERMISSION.values_by_name["PERMISSION_DELIVERY_NOTIFICATIONS_VIEW"]._serialized_options = b'\212\265\030\002\020\003'
  _PERMISSION.values_by_name["PERMISSION_DELIVERY_NOTIFICATIONS_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_DELIVERY_NOTIFICATIONS_EDIT"]._serialized_options = b'\212\265\030\002\020\003'
  _PERMISSION.values_by_name["PERMISSION_TICKETS_APP"]._options = None
  _PERMISSION.values_by_name["PERMISSION_TICKETS_APP"]._serialized_options = b'\212\265\030\004\010\001\020\r'
  _PERMISSION.values_by_name["PERMISSION_TICKETS_ADMIN"]._options = None
  _PERMISSION.values_by_name["PERMISSION_TICKETS_ADMIN"]._serialized_options = b'\212\265\030\004\010\001\020\r'
  _PERMISSION.values_by_name["PERMISSION_WORKFLOWS"]._options = None
  _PERMISSION.values_by_name["PERMISSION_WORKFLOWS"]._serialized_options = b'\212\265\030\002\020\020'
  _PERMISSION.values_by_name["PERMISSION_PBX_MANAGER_VIEW"]._options = None
  _PERMISSION.values_by_name["PERMISSION_PBX_MANAGER_VIEW"]._serialized_options = b'\212\265\0303\020\t\030\n\"\022PBX User Managment\"\031Extension Group Managment'
  _PERMISSION.values_by_name["PERMISSION_PBX_MANAGER_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_PBX_MANAGER_EDIT"]._serialized_options = b'\212\265\0303\020\t\030\n\"\022PBX User Managment\"\031Extension Group Managment'
  _PERMISSION.values_by_name["PERMISSION_NEWSROOM_EDIT"]._options = None
  _PERMISSION.values_by_name["PERMISSION_NEWSROOM_EDIT"]._serialized_options = b'\212\265\030\002\020\021'
  _PERMISSION.values_by_name["PERMISSION_NEWSROOM_PUBLISH"]._options = None
  _PERMISSION.values_by_name["PERMISSION_NEWSROOM_PUBLISH"]._serialized_options = b'\212\265\030\002\020\021'
  _globals['_PERMISSION']._serialized_start=80
  _globals['_PERMISSION']._serialized_end=4332
# @@protoc_insertion_point(module_scope)
