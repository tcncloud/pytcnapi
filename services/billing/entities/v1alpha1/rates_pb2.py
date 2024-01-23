# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/billing/entities/v1alpha1/rates.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.audit import event_types_pb2 as api_dot_commons_dot_audit_dot_event__types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha1 import matching_pb2 as services_dot_billing_dot_entities_dot_v1alpha1_dot_matching__pb2
from services.billing.entities.v1alpha1 import modules_pb2 as services_dot_billing_dot_entities_dot_v1alpha1_dot_modules__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.services/billing/entities/v1alpha1/rates.proto\x12\"services.billing.entities.v1alpha1\x1a#api/commons/audit/event_types.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x31services/billing/entities/v1alpha1/matching.proto\x1a\x30services/billing/entities/v1alpha1/modules.proto\"\xb8\x06\n\x0eRateDefinition\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12?\n\x1arate_definition_feature_id\x18\x02 \x01(\tB\x02\x18\x01R\x17rateDefinitionFeatureId\x12;\n\x18rate_definition_group_id\x18\x03 \x01(\tB\x02\x18\x01R\x15rateDefinitionGroupId\x12;\n\nevent_type\x18\x04 \x01(\x0e\x32\x1c.api.commons.audit.EventTypeR\teventType\x12]\n\x0b\x63onfig_type\x18\x05 \x01(\x0e\x32<.services.billing.entities.v1alpha1.RateDefinitionConfigTypeR\nconfigType\x12U\n\rmatching_rule\x18\x06 \x01(\x0e\x32\x30.services.billing.entities.v1alpha1.MatchingRuleR\x0cmatchingRule\x12[\n\x0fmatching_config\x18\x07 \x01(\x0b\x32\x32.services.billing.entities.v1alpha1.MatchingConfigR\x0ematchingConfig\x12P\n\x06\x63onfig\x18\x08 \x01(\x0b\x32\x38.services.billing.entities.v1alpha1.RateDefinitionConfigR\x06\x63onfig\x12;\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12;\n\x0b\x64\x65lete_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12!\n\x0cmatching_sha\x18\x0c \x01(\tR\x0bmatchingSha\"\xfe&\n\x14RateDefinitionConfig\x12_\n\x12\x61gent_seats_config\x18\x02 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x10\x61gentSeatsConfig\x12u\n\x1e\x61gent_text_message_chat_config\x18\x64 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1a\x61gentTextMessageChatConfig\x12\x86\x01\n\'agent_text_message_email_message_config\x18\x65 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\"agentTextMessageEmailMessageConfig\x12\x84\x01\n$agent_text_message_email_size_config\x18\x66 \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R\x1f\x61gentTextMessageEmailSizeConfig\x12s\n\x1d\x61gent_text_message_sms_config\x18g \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x19\x61gentTextMessageSmsConfig\x12\x84\x01\n&task_message_sent_email_message_config\x18h \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R!taskMessageSentEmailMessageConfig\x12\x82\x01\n#task_message_sent_email_size_config\x18i \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R\x1etaskMessageSentEmailSizeConfig\x12q\n\x1ctask_message_sent_sms_config\x18j \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x18taskMessageSentSmsConfig\x12p\n\x1b\x63onnected_inbox_poll_config\x18k \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x18\x63onnectedInboxPollConfig\x12y\n manager_text_message_chat_config\x18l \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1cmanagerTextMessageChatConfig\x12\x8a\x01\n)manager_text_message_email_message_config\x18m \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R$managerTextMessageEmailMessageConfig\x12\x88\x01\n&manager_text_message_email_size_config\x18n \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R!managerTextMessageEmailSizeConfig\x12w\n\x1fmanager_text_message_sms_config\x18o \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1bmanagerTextMessageSmsConfig\x12{\n!customer_text_message_chat_config\x18p \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1d\x63ustomerTextMessageChatConfig\x12\x8c\x01\n*customer_text_message_email_message_config\x18q \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R%customerTextMessageEmailMessageConfig\x12\x8a\x01\n\'customer_text_message_email_size_config\x18r \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R\"customerTextMessageEmailSizeConfig\x12y\n customer_text_message_sms_config\x18s \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1c\x63ustomerTextMessageSmsConfig\x12\x82\x01\n#agent_text_message_chat_size_config\x18t \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R\x1e\x61gentTextMessageChatSizeConfig\x12\x86\x01\n%manager_text_message_chat_size_config\x18u \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R managerTextMessageChatSizeConfig\x12\x88\x01\n&customer_text_message_chat_size_config\x18v \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R!customerTextMessageChatSizeConfig\x12v\n\x1e\x63onnected_inbox_created_config\x18w \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1b\x63onnectedInboxCreatedConfig\x12\x80\x01\n\"agent_text_message_sms_size_config\x18x \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R\x1d\x61gentTextMessageSmsSizeConfig\x12\x84\x01\n$manager_text_message_sms_size_config\x18y \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R\x1fmanagerTextMessageSmsSizeConfig\x12\x86\x01\n%customer_text_message_sms_size_config\x18z \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R customerTextMessageSmsSizeConfig\x12~\n!task_message_sent_sms_size_config\x18{ \x01(\x0b\x32\x33.services.billing.entities.v1alpha1.BasicUnitConfigH\x00R\x1ctaskMessageSentSmsSizeConfig\x12w\n\x1f\x61gent_chat_message_units_config\x18| \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1b\x61gentChatMessageUnitsConfig\x12y\n agent_email_message_units_config\x18} \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1c\x61gentEmailMessageUnitsConfig\x12u\n\x1e\x61gent_sms_message_units_config\x18~ \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1a\x61gentSmsMessageUnitsConfig\x12{\n!manager_chat_message_units_config\x18\x7f \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1dmanagerChatMessageUnitsConfig\x12~\n\"manager_email_message_units_config\x18\x80\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1emanagerEmailMessageUnitsConfig\x12z\n manager_sms_message_units_config\x18\x81\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1cmanagerSmsMessageUnitsConfig\x12~\n\"customer_chat_message_units_config\x18\x82\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1e\x63ustomerChatMessageUnitsConfig\x12\x80\x01\n#customer_email_message_units_config\x18\x83\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1f\x63ustomerEmailMessageUnitsConfig\x12|\n!customer_sms_message_units_config\x18\x84\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1d\x63ustomerSmsMessageUnitsConfig\x12z\n system_chat_message_units_config\x18\x85\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1csystemChatMessageUnitsConfig\x12|\n!system_email_message_units_config\x18\x86\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1dsystemEmailMessageUnitsConfig\x12x\n\x1fsystem_sms_message_units_config\x18\x87\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1bsystemSmsMessageUnitsConfig\x12q\n\x1b\x63ompliance_rnd_query_config\x18\xc8\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x18\x63omplianceRndQueryConfig\x12~\n\"compliance_rnd_query_cached_config\x18\xc9\x01 \x01(\x0b\x32/.services.billing.entities.v1alpha1.BasicConfigH\x00R\x1e\x63omplianceRndQueryCachedConfigB\x08\n\x06\x63onfig*\xa7\x13\n\x18RateDefinitionConfigType\x12+\n\'RATE_DEFINITION_CONFIG_TYPE_UNSPECIFIED\x10\x00\x12$\n RATE_DEFINITION_CONFIG_TYPE_NOOP\x10\x01\x12+\n\'RATE_DEFINITION_CONFIG_TYPE_AGENT_SEATS\x10\x02\x12\x37\n3RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT\x10\x64\x12@\n<RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_MESSAGE\x10\x65\x12=\n9RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_SIZE\x10\x66\x12\x36\n2RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS\x10g\x12?\n;RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_MESSAGE\x10h\x12<\n8RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_SIZE\x10i\x12\x35\n1RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS\x10j\x12\x34\n0RATE_DEFINITION_CONFIG_TYPE_CONNECTED_INBOX_POLL\x10k\x12\x39\n5RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT\x10l\x12\x42\n>RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_MESSAGE\x10m\x12?\n;RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_SIZE\x10n\x12\x38\n4RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS\x10o\x12:\n6RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT\x10p\x12\x43\n?RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_MESSAGE\x10q\x12@\n<RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_SIZE\x10r\x12\x39\n5RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS\x10s\x12<\n8RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT_SIZE\x10t\x12>\n:RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT_SIZE\x10u\x12?\n;RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT_SIZE\x10v\x12\x37\n3RATE_DEFINITION_CONFIG_TYPE_CONNECTED_INBOX_CREATED\x10w\x12;\n7RATE_DEFINITION_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS_SIZE\x10x\x12=\n9RATE_DEFINITION_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS_SIZE\x10y\x12>\n:RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS_SIZE\x10z\x12:\n6RATE_DEFINITION_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS_SIZE\x10{\x12\x38\n4RATE_DEFINITION_CONFIG_TYPE_AGENT_CHAT_MESSAGE_UNITS\x10|\x12\x39\n5RATE_DEFINITION_CONFIG_TYPE_AGENT_EMAIL_MESSAGE_UNITS\x10}\x12\x37\n3RATE_DEFINITION_CONFIG_TYPE_AGENT_SMS_MESSAGE_UNITS\x10~\x12:\n6RATE_DEFINITION_CONFIG_TYPE_MANAGER_CHAT_MESSAGE_UNITS\x10\x7f\x12<\n7RATE_DEFINITION_CONFIG_TYPE_MANAGER_EMAIL_MESSAGE_UNITS\x10\x80\x01\x12:\n5RATE_DEFINITION_CONFIG_TYPE_MANAGER_SMS_MESSAGE_UNITS\x10\x81\x01\x12<\n7RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_CHAT_MESSAGE_UNITS\x10\x82\x01\x12=\n8RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_EMAIL_MESSAGE_UNITS\x10\x83\x01\x12;\n6RATE_DEFINITION_CONFIG_TYPE_CUSTOMER_SMS_MESSAGE_UNITS\x10\x84\x01\x12:\n5RATE_DEFINITION_CONFIG_TYPE_SYSTEM_CHAT_MESSAGE_UNITS\x10\x85\x01\x12;\n6RATE_DEFINITION_CONFIG_TYPE_SYSTEM_EMAIL_MESSAGE_UNITS\x10\x86\x01\x12\x39\n4RATE_DEFINITION_CONFIG_TYPE_SYSTEM_SMS_MESSAGE_UNITS\x10\x87\x01\x12\x35\n0RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY\x10\xc8\x01\x12<\n7RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY_CACHED\x10\xc9\x01\x42\xdf\x01\n&com.services.billing.entities.v1alpha1B\nRatesProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha1\xca\x02\"Services\\Billing\\Entities\\V1alpha1\xe2\x02.Services\\Billing\\Entities\\V1alpha1\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha1.rates_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha1B\nRatesProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha1\312\002\"Services\\Billing\\Entities\\V1alpha1\342\002.Services\\Billing\\Entities\\V1alpha1\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha1'
  _globals['_RATEDEFINITION'].fields_by_name['rate_definition_feature_id']._options = None
  _globals['_RATEDEFINITION'].fields_by_name['rate_definition_feature_id']._serialized_options = b'\030\001'
  _globals['_RATEDEFINITION'].fields_by_name['rate_definition_group_id']._options = None
  _globals['_RATEDEFINITION'].fields_by_name['rate_definition_group_id']._serialized_options = b'\030\001'
  _globals['_RATEDEFINITIONCONFIGTYPE']._serialized_start=6078
  _globals['_RATEDEFINITIONCONFIGTYPE']._serialized_end=8549
  _globals['_RATEDEFINITION']._serialized_start=258
  _globals['_RATEDEFINITION']._serialized_end=1082
  _globals['_RATEDEFINITIONCONFIG']._serialized_start=1085
  _globals['_RATEDEFINITIONCONFIG']._serialized_end=6075
# @@protoc_insertion_point(module_scope)
