# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/billing/entities/v1alpha2/rates.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.audit import event_types_pb2 as api_dot_commons_dot_audit_dot_event__types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha2 import matching_pb2 as services_dot_billing_dot_entities_dot_v1alpha2_dot_matching__pb2
from services.billing.entities.v1alpha2 import modules_pb2 as services_dot_billing_dot_entities_dot_v1alpha2_dot_modules__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.services/billing/entities/v1alpha2/rates.proto\x12\"services.billing.entities.v1alpha2\x1a#api/commons/audit/event_types.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x31services/billing/entities/v1alpha2/matching.proto\x1a\x30services/billing/entities/v1alpha2/modules.proto\"\xca\x01\n\x0cRateSnapshot\x12\x39\n\nstart_date\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartDate\x12\x35\n\x08\x65nd_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndDate\x12H\n\x05rates\x18\x03 \x03(\x0b\x32\x32.services.billing.entities.v1alpha2.RateDefinitionR\x05rates\"\xd4\x06\n\x0eRateDefinition\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12;\n\nevent_type\x18\x02 \x01(\x0e\x32\x1c.api.commons.audit.EventTypeR\teventType\x12]\n\x0b\x63onfig_type\x18\x03 \x01(\x0e\x32<.services.billing.entities.v1alpha2.RateDefinitionConfigTypeR\nconfigType\x12U\n\rmatching_rule\x18\x04 \x01(\x0e\x32\x30.services.billing.entities.v1alpha2.MatchingRuleR\x0cmatchingRule\x12[\n\x0fmatching_config\x18\x05 \x01(\x0b\x32\x32.services.billing.entities.v1alpha2.MatchingConfigR\x0ematchingConfig\x12!\n\x0cmatching_sha\x18\x06 \x01(\tR\x0bmatchingSha\x12;\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12;\n\x0b\x64\x65lete_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12\x41\n\x0e\x65\x66\x66\x65\x63tive_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\reffectiveTime\x12P\n\x06\x63onfig\x18\x0b \x01(\x0b\x32\x38.services.billing.entities.v1alpha2.RateDefinitionConfigR\x06\x63onfig\x12\x19\n\x08group_id\x18\x0c \x01(\tR\x07groupId\x12\x1d\n\nconfig_sha\x18\r \x01(\tR\tconfigSha\x12\x1b\n\tthread_id\x18\x0e \x01(\tR\x08threadId\"\xf4\"\n\x14RateDefinitionConfig\x12S\n\x0b\x61gent_seats\x18\xe8\x07 \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\nagentSeats\x12\x64\n\x14\x63onnected_inbox_poll\x18\xdc\x0b \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x12\x63onnectedInboxPoll\x12j\n\x17\x63onnected_inbox_created\x18\xdd\x0b \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x15\x63onnectedInboxCreated\x12`\n\x12\x61gent_message_chat\x18\xc0\x0c \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x10\x61gentMessageChat\x12m\n\x17\x61gent_message_chat_size\x18\xc1\x0c \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x14\x61gentMessageChatSize\x12k\n\x18\x61gent_message_chat_units\x18\xc2\x0c \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x15\x61gentMessageChatUnits\x12\x62\n\x13\x61gent_message_email\x18\xca\x0c \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x11\x61gentMessageEmail\x12o\n\x18\x61gent_message_email_size\x18\xcb\x0c \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x15\x61gentMessageEmailSize\x12m\n\x19\x61gent_message_email_units\x18\xcc\x0c \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x16\x61gentMessageEmailUnits\x12^\n\x11\x61gent_message_sms\x18\xd4\x0c \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x0f\x61gentMessageSms\x12k\n\x16\x61gent_message_sms_size\x18\xd5\x0c \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x13\x61gentMessageSmsSize\x12i\n\x17\x61gent_message_sms_units\x18\xd6\x0c \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x14\x61gentMessageSmsUnits\x12\x64\n\x14manager_message_chat\x18\xa4\r \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x12managerMessageChat\x12q\n\x19manager_message_chat_size\x18\xa5\r \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x16managerMessageChatSize\x12o\n\x1amanager_message_chat_units\x18\xa6\r \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x17managerMessageChatUnits\x12\x66\n\x15manager_message_email\x18\xae\r \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x13managerMessageEmail\x12s\n\x1amanager_message_email_size\x18\xaf\r \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x17managerMessageEmailSize\x12q\n\x1bmanager_message_email_units\x18\xb0\r \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x18managerMessageEmailUnits\x12\x62\n\x13manager_message_sms\x18\xb8\r \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x11managerMessageSms\x12o\n\x18manager_message_sms_size\x18\xb9\r \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x15managerMessageSmsSize\x12m\n\x19manager_message_sms_units\x18\xba\r \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x16managerMessageSmsUnits\x12\x62\n\x13system_message_chat\x18\x88\x0e \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x11systemMessageChat\x12o\n\x18system_message_chat_size\x18\x89\x0e \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x15systemMessageChatSize\x12m\n\x19system_message_chat_units\x18\x8a\x0e \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x16systemMessageChatUnits\x12\x64\n\x14system_message_email\x18\x92\x0e \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x12systemMessageEmail\x12q\n\x19system_message_email_size\x18\x93\x0e \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x16systemMessageEmailSize\x12o\n\x1asystem_message_email_units\x18\x94\x0e \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x17systemMessageEmailUnits\x12`\n\x12system_message_sms\x18\x9c\x0e \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x10systemMessageSms\x12m\n\x17system_message_sms_size\x18\x9d\x0e \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x14systemMessageSmsSize\x12k\n\x18system_message_sms_units\x18\x9e\x0e \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x15systemMessageSmsUnits\x12\x66\n\x15\x63ustomer_message_chat\x18\xec\x0e \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x13\x63ustomerMessageChat\x12s\n\x1a\x63ustomer_message_chat_size\x18\xed\x0e \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x17\x63ustomerMessageChatSize\x12q\n\x1b\x63ustomer_message_chat_units\x18\xee\x0e \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x18\x63ustomerMessageChatUnits\x12h\n\x16\x63ustomer_message_email\x18\xf6\x0e \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x14\x63ustomerMessageEmail\x12u\n\x1b\x63ustomer_message_email_size\x18\xf7\x0e \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x18\x63ustomerMessageEmailSize\x12s\n\x1c\x63ustomer_message_email_units\x18\xf8\x0e \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x19\x63ustomerMessageEmailUnits\x12\x64\n\x14\x63ustomer_message_sms\x18\x80\x0f \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x12\x63ustomerMessageSms\x12q\n\x19\x63ustomer_message_sms_size\x18\x81\x0f \x01(\x0b\x32\x33.services.billing.entities.v1alpha2.BasicUnitConfigH\x00R\x16\x63ustomerMessageSmsSize\x12o\n\x1a\x63ustomer_message_sms_units\x18\x82\x0f \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x17\x63ustomerMessageSmsUnits\x12\x64\n\x14\x63ompliance_rnd_query\x18\xd0\x0f \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x12\x63omplianceRndQuery\x12q\n\x1b\x63ompliance_rnd_query_cached\x18\xd1\x0f \x01(\x0b\x32/.services.billing.entities.v1alpha2.BasicConfigH\x00R\x18\x63omplianceRndQueryCachedB\x08\n\x06\x63onfig*\xf2\x14\n\x18RateDefinitionConfigType\x12+\n\'RATE_DEFINITION_CONFIG_TYPE_UNSPECIFIED\x10\x00\x12$\n RATE_DEFINITION_CONFIG_TYPE_NOOP\x10\x01\x12\x31\n,RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_SEATS\x10\xe8\x07\x12:\n5RATE_DEFINITION_CONFIG_TYPE_OMNI_CONNECTED_INBOX_POLL\x10\xdc\x0b\x12=\n8RATE_DEFINITION_CONFIG_TYPE_OMNI_CONNECTED_INBOX_CREATED\x10\xdd\x0b\x12\x38\n3RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_CHAT\x10\xc0\x0c\x12=\n8RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_CHAT_SIZE\x10\xc1\x0c\x12>\n9RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_CHAT_UNITS\x10\xc2\x0c\x12\x39\n4RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_EMAIL\x10\xca\x0c\x12>\n9RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_EMAIL_SIZE\x10\xcb\x0c\x12?\n:RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_EMAIL_UNITS\x10\xcc\x0c\x12\x37\n2RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_SMS\x10\xd4\x0c\x12<\n7RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_SMS_SIZE\x10\xd5\x0c\x12=\n8RATE_DEFINITION_CONFIG_TYPE_OMNI_AGENT_MESSAGE_SMS_UNITS\x10\xd6\x0c\x12:\n5RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_CHAT\x10\xa4\r\x12?\n:RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_CHAT_SIZE\x10\xa5\r\x12@\n;RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_CHAT_UNITS\x10\xa6\r\x12;\n6RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_EMAIL\x10\xae\r\x12@\n;RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_EMAIL_SIZE\x10\xaf\r\x12\x41\n<RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_EMAIL_UNITS\x10\xb0\r\x12\x39\n4RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_SMS\x10\xb8\r\x12>\n9RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_SMS_SIZE\x10\xb9\r\x12?\n:RATE_DEFINITION_CONFIG_TYPE_OMNI_MANAGER_MESSAGE_SMS_UNITS\x10\xba\r\x12\x39\n4RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_CHAT\x10\x88\x0e\x12>\n9RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_CHAT_SIZE\x10\x89\x0e\x12?\n:RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_CHAT_UNITS\x10\x8a\x0e\x12:\n5RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_EMAIL\x10\x92\x0e\x12?\n:RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_EMAIL_SIZE\x10\x93\x0e\x12@\n;RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_EMAIL_UNITS\x10\x94\x0e\x12\x38\n3RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_SMS\x10\x9c\x0e\x12=\n8RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_SMS_SIZE\x10\x9d\x0e\x12>\n9RATE_DEFINITION_CONFIG_TYPE_OMNI_SYSTEM_MESSAGE_SMS_UNITS\x10\x9e\x0e\x12;\n6RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_CHAT\x10\xec\x0e\x12@\n;RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_CHAT_SIZE\x10\xed\x0e\x12\x41\n<RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_CHAT_UNITS\x10\xee\x0e\x12<\n7RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_EMAIL\x10\xf6\x0e\x12\x41\n<RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_EMAIL_SIZE\x10\xf7\x0e\x12\x42\n=RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_EMAIL_UNITS\x10\xf8\x0e\x12:\n5RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_SMS\x10\x80\x0f\x12?\n:RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_SMS_SIZE\x10\x81\x0f\x12@\n;RATE_DEFINITION_CONFIG_TYPE_OMNI_CUSTOMER_MESSAGE_SMS_UNITS\x10\x82\x0f\x12\x35\n0RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY\x10\xd0\x0f\x12<\n7RATE_DEFINITION_CONFIG_TYPE_COMPLIANCE_RND_QUERY_CACHED\x10\xd1\x0f\x42\xdf\x01\n&com.services.billing.entities.v1alpha2B\nRatesProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha2\xca\x02\"Services\\Billing\\Entities\\V1alpha2\xe2\x02.Services\\Billing\\Entities\\V1alpha2\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha2.rates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha2B\nRatesProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha2\312\002\"Services\\Billing\\Entities\\V1alpha2\342\002.Services\\Billing\\Entities\\V1alpha2\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha2'
  _globals['_RATEDEFINITIONCONFIGTYPE']._serialized_start=5789
  _globals['_RATEDEFINITIONCONFIGTYPE']._serialized_end=8463
  _globals['_RATESNAPSHOT']._serialized_start=258
  _globals['_RATESNAPSHOT']._serialized_end=460
  _globals['_RATEDEFINITION']._serialized_start=463
  _globals['_RATEDEFINITION']._serialized_end=1315
  _globals['_RATEDEFINITIONCONFIG']._serialized_start=1318
  _globals['_RATEDEFINITIONCONFIG']._serialized_end=5786
# @@protoc_insertion_point(module_scope)