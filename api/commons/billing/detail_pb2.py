# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/billing/detail.proto
# Protobuf Python Version: 5.28.1
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
    1,
    '',
    'api/commons/billing/detail.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.audit import event_types_pb2 as api_dot_commons_dot_audit_dot_event__types__pb2
from api.commons.billing.modules import modules_pb2 as api_dot_commons_dot_billing_dot_modules_dot_modules__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n api/commons/billing/detail.proto\x12\x13\x61pi.commons.billing\x1a#api/commons/audit/event_types.proto\x1a)api/commons/billing/modules/modules.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8a\x03\n\x04Plan\x12\x39\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x1b.api.commons.billing.DetailB\x02\x18\x01R\x07\x64\x65tails\x12\x19\n\x06org_id\x18\x02 \x01(\tB\x02\x18\x01R\x05orgId\x12,\n\x0f\x62illing_plan_id\x18\x03 \x01(\x03\x42\x04\x18\x01\x30\x01R\rbillingPlanId\x12?\n\x0b\x63reate_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\ncreateTime\x12?\n\x0bupdate_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\nupdateTime\x12=\n\nstart_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\tstartTime\x12\x39\n\x08\x65nd_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x07\x65ndTime:\x02\x18\x01\"\xff\x03\n\x06\x44\x65tail\x12\x30\n\x12\x62illing_detail_sid\x18\x01 \x01(\x03\x42\x02\x18\x01R\x10\x62illingDetailSid\x12?\n\nevent_type\x18\x02 \x01(\x0e\x32\x1c.api.commons.audit.EventTypeB\x02\x18\x01R\teventType\x12J\n\x0b\x63onfig_type\x18\x03 \x01(\x0e\x32%.api.commons.billing.DetailConfigTypeB\x02\x18\x01R\nconfigType\x12=\n\x06\x63onfig\x18\x04 \x01(\x0b\x32!.api.commons.billing.DetailConfigB\x02\x18\x01R\x06\x63onfig\x12\x41\n\x0c\x64\x61te_created\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x0b\x64\x61teCreated\x12\x43\n\rdate_modified\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x0c\x64\x61teModified\x12=\n\ndeleted_on\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\tdeletedOn\x12,\n\x0f\x62illing_plan_id\x18\x08 \x01(\x03\x42\x04\x18\x01\x30\x01R\rbillingPlanId:\x02\x18\x01\"\x99&\n\x0c\x44\x65tailConfig\x12\\\n\x12\x61gent_seats_config\x18\x02 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x10\x61gentSeatsConfig\x12r\n\x1e\x61gent_text_message_chat_config\x18\x64 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1a\x61gentTextMessageChatConfig\x12\x83\x01\n\'agent_text_message_email_message_config\x18\x65 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\"agentTextMessageEmailMessageConfig\x12\x83\x01\n$agent_text_message_email_size_config\x18\x66 \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R\x1f\x61gentTextMessageEmailSizeConfig\x12p\n\x1d\x61gent_text_message_sms_config\x18g \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x19\x61gentTextMessageSmsConfig\x12\x81\x01\n&task_message_sent_email_message_config\x18h \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R!taskMessageSentEmailMessageConfig\x12\x81\x01\n#task_message_sent_email_size_config\x18i \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R\x1etaskMessageSentEmailSizeConfig\x12n\n\x1ctask_message_sent_sms_config\x18j \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x18taskMessageSentSmsConfig\x12m\n\x1b\x63onnected_inbox_poll_config\x18k \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x18\x63onnectedInboxPollConfig\x12v\n manager_text_message_chat_config\x18l \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1cmanagerTextMessageChatConfig\x12\x87\x01\n)manager_text_message_email_message_config\x18m \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R$managerTextMessageEmailMessageConfig\x12\x87\x01\n&manager_text_message_email_size_config\x18n \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R!managerTextMessageEmailSizeConfig\x12t\n\x1fmanager_text_message_sms_config\x18o \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1bmanagerTextMessageSmsConfig\x12x\n!customer_text_message_chat_config\x18p \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1d\x63ustomerTextMessageChatConfig\x12\x89\x01\n*customer_text_message_email_message_config\x18q \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R%customerTextMessageEmailMessageConfig\x12\x89\x01\n\'customer_text_message_email_size_config\x18r \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R\"customerTextMessageEmailSizeConfig\x12v\n customer_text_message_sms_config\x18s \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1c\x63ustomerTextMessageSmsConfig\x12\x81\x01\n#agent_text_message_chat_size_config\x18t \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R\x1e\x61gentTextMessageChatSizeConfig\x12\x85\x01\n%manager_text_message_chat_size_config\x18u \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R managerTextMessageChatSizeConfig\x12\x87\x01\n&customer_text_message_chat_size_config\x18v \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R!customerTextMessageChatSizeConfig\x12s\n\x1e\x63onnected_inbox_created_config\x18w \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1b\x63onnectedInboxCreatedConfig\x12\x7f\n\"agent_text_message_sms_size_config\x18x \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R\x1d\x61gentTextMessageSmsSizeConfig\x12\x83\x01\n$manager_text_message_sms_size_config\x18y \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R\x1fmanagerTextMessageSmsSizeConfig\x12\x85\x01\n%customer_text_message_sms_size_config\x18z \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R customerTextMessageSmsSizeConfig\x12}\n!task_message_sent_sms_size_config\x18{ \x01(\x0b\x32..api.commons.billing.modules.BasicAmountConfigB\x02\x18\x01H\x00R\x1ctaskMessageSentSmsSizeConfig\x12t\n\x1f\x61gent_chat_message_units_config\x18| \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1b\x61gentChatMessageUnitsConfig\x12v\n agent_email_message_units_config\x18} \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1c\x61gentEmailMessageUnitsConfig\x12r\n\x1e\x61gent_sms_message_units_config\x18~ \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1a\x61gentSmsMessageUnitsConfig\x12x\n!manager_chat_message_units_config\x18\x7f \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1dmanagerChatMessageUnitsConfig\x12{\n\"manager_email_message_units_config\x18\x80\x01 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1emanagerEmailMessageUnitsConfig\x12w\n manager_sms_message_units_config\x18\x81\x01 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1cmanagerSmsMessageUnitsConfig\x12{\n\"customer_chat_message_units_config\x18\x82\x01 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1e\x63ustomerChatMessageUnitsConfig\x12}\n#customer_email_message_units_config\x18\x83\x01 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1f\x63ustomerEmailMessageUnitsConfig\x12y\n!customer_sms_message_units_config\x18\x84\x01 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1d\x63ustomerSmsMessageUnitsConfig\x12w\n system_chat_message_units_config\x18\x85\x01 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1csystemChatMessageUnitsConfig\x12y\n!system_email_message_units_config\x18\x86\x01 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1dsystemEmailMessageUnitsConfig\x12u\n\x1fsystem_sms_message_units_config\x18\x87\x01 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1bsystemSmsMessageUnitsConfig\x12n\n\x1b\x63ompliance_rnd_query_config\x18\xc8\x01 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x18\x63omplianceRndQueryConfig\x12{\n\"compliance_rnd_query_cached_config\x18\xc9\x01 \x01(\x0b\x32(.api.commons.billing.modules.BasicConfigB\x02\x18\x01H\x00R\x1e\x63omplianceRndQueryCachedConfig:\x02\x18\x01\x42\x08\n\x06\x63onfig*\xbc\x10\n\x10\x44\x65tailConfigType\x12\"\n\x1e\x44\x45TAIL_CONFIG_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x44\x45TAIL_CONFIG_TYPE_NOOP\x10\x01\x12\"\n\x1e\x44\x45TAIL_CONFIG_TYPE_AGENT_SEATS\x10\x02\x12.\n*DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT\x10\x64\x12\x37\n3DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_MESSAGE\x10\x65\x12\x34\n0DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_SIZE\x10\x66\x12-\n)DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS\x10g\x12\x36\n2DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_MESSAGE\x10h\x12\x33\n/DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_SIZE\x10i\x12,\n(DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS\x10j\x12+\n\'DETAIL_CONFIG_TYPE_CONNECTED_INBOX_POLL\x10k\x12\x30\n,DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT\x10l\x12\x39\n5DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_MESSAGE\x10m\x12\x36\n2DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_SIZE\x10n\x12/\n+DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS\x10o\x12\x31\n-DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT\x10p\x12:\n6DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_MESSAGE\x10q\x12\x37\n3DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_SIZE\x10r\x12\x30\n,DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS\x10s\x12\x33\n/DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT_SIZE\x10t\x12\x35\n1DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT_SIZE\x10u\x12\x36\n2DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT_SIZE\x10v\x12.\n*DETAIL_CONFIG_TYPE_CONNECTED_INBOX_CREATED\x10w\x12\x32\n.DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS_SIZE\x10x\x12\x34\n0DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS_SIZE\x10y\x12\x35\n1DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS_SIZE\x10z\x12\x31\n-DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS_SIZE\x10{\x12/\n+DETAIL_CONFIG_TYPE_AGENT_CHAT_MESSAGE_UNITS\x10|\x12\x30\n,DETAIL_CONFIG_TYPE_AGENT_EMAIL_MESSAGE_UNITS\x10}\x12.\n*DETAIL_CONFIG_TYPE_AGENT_SMS_MESSAGE_UNITS\x10~\x12\x31\n-DETAIL_CONFIG_TYPE_MANAGER_CHAT_MESSAGE_UNITS\x10\x7f\x12\x33\n.DETAIL_CONFIG_TYPE_MANAGER_EMAIL_MESSAGE_UNITS\x10\x80\x01\x12\x31\n,DETAIL_CONFIG_TYPE_MANAGER_SMS_MESSAGE_UNITS\x10\x81\x01\x12\x33\n.DETAIL_CONFIG_TYPE_CUSTOMER_CHAT_MESSAGE_UNITS\x10\x82\x01\x12\x34\n/DETAIL_CONFIG_TYPE_CUSTOMER_EMAIL_MESSAGE_UNITS\x10\x83\x01\x12\x32\n-DETAIL_CONFIG_TYPE_CUSTOMER_SMS_MESSAGE_UNITS\x10\x84\x01\x12\x31\n,DETAIL_CONFIG_TYPE_SYSTEM_CHAT_MESSAGE_UNITS\x10\x85\x01\x12\x32\n-DETAIL_CONFIG_TYPE_SYSTEM_EMAIL_MESSAGE_UNITS\x10\x86\x01\x12\x30\n+DETAIL_CONFIG_TYPE_SYSTEM_SMS_MESSAGE_UNITS\x10\x87\x01\x12\x31\n,BillingDetailConfigType_COMPLIANCE_RND_QUERY\x10\xc8\x01\x12\x38\n3BillingDetailConfigType_COMPLIANCE_RND_QUERY_CACHED\x10\xc9\x01\x1a\x02\x18\x01\x42\x94\x01\n\x17\x63om.api.commons.billingB\x0b\x44\x65tailProtoP\x01\xa2\x02\x03\x41\x43\x42\xaa\x02\x13\x41pi.Commons.Billing\xca\x02\x13\x41pi\\Commons\\Billing\xe2\x02\x1f\x41pi\\Commons\\Billing\\GPBMetadata\xea\x02\x15\x41pi::Commons::Billingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.billing.detail_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027com.api.commons.billingB\013DetailProtoP\001\242\002\003ACB\252\002\023Api.Commons.Billing\312\002\023Api\\Commons\\Billing\342\002\037Api\\Commons\\Billing\\GPBMetadata\352\002\025Api::Commons::Billing'
  _globals['_DETAILCONFIGTYPE']._loaded_options = None
  _globals['_DETAILCONFIGTYPE']._serialized_options = b'\030\001'
  _globals['_PLAN'].fields_by_name['details']._loaded_options = None
  _globals['_PLAN'].fields_by_name['details']._serialized_options = b'\030\001'
  _globals['_PLAN'].fields_by_name['org_id']._loaded_options = None
  _globals['_PLAN'].fields_by_name['org_id']._serialized_options = b'\030\001'
  _globals['_PLAN'].fields_by_name['billing_plan_id']._loaded_options = None
  _globals['_PLAN'].fields_by_name['billing_plan_id']._serialized_options = b'\030\0010\001'
  _globals['_PLAN'].fields_by_name['create_time']._loaded_options = None
  _globals['_PLAN'].fields_by_name['create_time']._serialized_options = b'\030\001'
  _globals['_PLAN'].fields_by_name['update_time']._loaded_options = None
  _globals['_PLAN'].fields_by_name['update_time']._serialized_options = b'\030\001'
  _globals['_PLAN'].fields_by_name['start_time']._loaded_options = None
  _globals['_PLAN'].fields_by_name['start_time']._serialized_options = b'\030\001'
  _globals['_PLAN'].fields_by_name['end_time']._loaded_options = None
  _globals['_PLAN'].fields_by_name['end_time']._serialized_options = b'\030\001'
  _globals['_PLAN']._loaded_options = None
  _globals['_PLAN']._serialized_options = b'\030\001'
  _globals['_DETAIL'].fields_by_name['billing_detail_sid']._loaded_options = None
  _globals['_DETAIL'].fields_by_name['billing_detail_sid']._serialized_options = b'\030\001'
  _globals['_DETAIL'].fields_by_name['event_type']._loaded_options = None
  _globals['_DETAIL'].fields_by_name['event_type']._serialized_options = b'\030\001'
  _globals['_DETAIL'].fields_by_name['config_type']._loaded_options = None
  _globals['_DETAIL'].fields_by_name['config_type']._serialized_options = b'\030\001'
  _globals['_DETAIL'].fields_by_name['config']._loaded_options = None
  _globals['_DETAIL'].fields_by_name['config']._serialized_options = b'\030\001'
  _globals['_DETAIL'].fields_by_name['date_created']._loaded_options = None
  _globals['_DETAIL'].fields_by_name['date_created']._serialized_options = b'\030\001'
  _globals['_DETAIL'].fields_by_name['date_modified']._loaded_options = None
  _globals['_DETAIL'].fields_by_name['date_modified']._serialized_options = b'\030\001'
  _globals['_DETAIL'].fields_by_name['deleted_on']._loaded_options = None
  _globals['_DETAIL'].fields_by_name['deleted_on']._serialized_options = b'\030\001'
  _globals['_DETAIL'].fields_by_name['billing_plan_id']._loaded_options = None
  _globals['_DETAIL'].fields_by_name['billing_plan_id']._serialized_options = b'\030\0010\001'
  _globals['_DETAIL']._loaded_options = None
  _globals['_DETAIL']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['agent_seats_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['agent_seats_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_chat_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_chat_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_email_message_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_email_message_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_email_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_email_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_sms_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_sms_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['task_message_sent_email_message_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['task_message_sent_email_message_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['task_message_sent_email_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['task_message_sent_email_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['task_message_sent_sms_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['task_message_sent_sms_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['connected_inbox_poll_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['connected_inbox_poll_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_chat_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_chat_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_email_message_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_email_message_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_email_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_email_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_sms_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_sms_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_chat_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_chat_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_email_message_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_email_message_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_email_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_email_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_sms_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_sms_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_chat_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_chat_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_chat_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_chat_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_chat_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_chat_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['connected_inbox_created_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['connected_inbox_created_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_sms_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['agent_text_message_sms_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_sms_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['manager_text_message_sms_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_sms_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['customer_text_message_sms_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['task_message_sent_sms_size_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['task_message_sent_sms_size_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['agent_chat_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['agent_chat_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['agent_email_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['agent_email_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['agent_sms_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['agent_sms_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['manager_chat_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['manager_chat_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['manager_email_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['manager_email_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['manager_sms_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['manager_sms_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['customer_chat_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['customer_chat_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['customer_email_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['customer_email_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['customer_sms_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['customer_sms_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['system_chat_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['system_chat_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['system_email_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['system_email_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['system_sms_message_units_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['system_sms_message_units_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['compliance_rnd_query_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['compliance_rnd_query_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG'].fields_by_name['compliance_rnd_query_cached_config']._loaded_options = None
  _globals['_DETAILCONFIG'].fields_by_name['compliance_rnd_query_cached_config']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIG']._loaded_options = None
  _globals['_DETAILCONFIG']._serialized_options = b'\030\001'
  _globals['_DETAILCONFIGTYPE']._serialized_start=5974
  _globals['_DETAILCONFIGTYPE']._serialized_end=8082
  _globals['_PLAN']._serialized_start=171
  _globals['_PLAN']._serialized_end=565
  _globals['_DETAIL']._serialized_start=568
  _globals['_DETAIL']._serialized_end=1079
  _globals['_DETAILCONFIG']._serialized_start=1082
  _globals['_DETAILCONFIG']._serialized_end=5971
# @@protoc_insertion_point(module_scope)
