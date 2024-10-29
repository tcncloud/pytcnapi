# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/billing/entities/v1alpha3/rates.proto
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
    'services/billing/entities/v1alpha3/rates.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from services.billing.entities.v1alpha3 import modules_pb2 as services_dot_billing_dot_entities_dot_v1alpha3_dot_modules__pb2
from services.billing.entities.v1alpha3 import omni_pb2 as services_dot_billing_dot_entities_dot_v1alpha3_dot_omni__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.services/billing/entities/v1alpha3/rates.proto\x12\"services.billing.entities.v1alpha3\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x30services/billing/entities/v1alpha3/modules.proto\x1a-services/billing/entities/v1alpha3/omni.proto\"\xb9\x03\n\x0eRateDefinition\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12\x15\n\x06sku_id\x18\x02 \x01(\tR\x05skuId\x12\x45\n\x07product\x18\x03 \x01(\x0b\x32+.services.billing.entities.v1alpha3.ProductR\x07product\x12I\n\x06\x63onfig\x18\x04 \x01(\x0b\x32\x31.services.billing.entities.v1alpha3.ProductConfigR\x06\x63onfig\x12\x19\n\x08is_draft\x18\x05 \x01(\x08R\x07isDraft\x12;\n\x0b\x63reate_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12;\n\x0b\x64\x65lete_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\"\x99\x01\n\x07Product\x12!\n\x0c\x63\x61tegory_one\x18\x01 \x01(\tR\x0b\x63\x61tegoryOne\x12!\n\x0c\x63\x61tegory_two\x18\x02 \x01(\tR\x0b\x63\x61tegoryTwo\x12%\n\x0e\x63\x61tegory_three\x18\x03 \x01(\tR\rcategoryThree\x12!\n\x0cproduct_name\x18\x04 \x01(\tR\x0bproductName\"\x93\x32\n\rProductConfig\x12\x8f\x01\n+communications_omni_chat_agent_message_unit\x18\xe8\x07 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R&communicationsOmniChatAgentMessageUnit\x12\x90\x01\n)communications_omni_chat_agent_attachment\x18\xe9\x07 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R%communicationsOmniChatAgentAttachment\x12\xa9\x01\n6communications_omni_chat_agent_accumulated_attachments\x18\xea\x07 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R1communicationsOmniChatAgentAccumulatedAttachments\x12\x95\x01\n.communications_omni_chat_customer_message_unit\x18\xf2\x07 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R)communicationsOmniChatCustomerMessageUnit\x12\x96\x01\n,communications_omni_chat_customer_attachment\x18\xf3\x07 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R(communicationsOmniChatCustomerAttachment\x12\xaf\x01\n9communications_omni_chat_customer_accumulated_attachments\x18\xf4\x07 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R4communicationsOmniChatCustomerAccumulatedAttachments\x12\x93\x01\n-communications_omni_chat_manager_message_unit\x18\xfc\x07 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R(communicationsOmniChatManagerMessageUnit\x12\x94\x01\n+communications_omni_chat_manager_attachment\x18\xfd\x07 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R\'communicationsOmniChatManagerAttachment\x12\xad\x01\n8communications_omni_chat_manager_accumulated_attachments\x18\xfe\x07 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R3communicationsOmniChatManagerAccumulatedAttachments\x12\x91\x01\n,communications_omni_chat_system_message_unit\x18\x86\x08 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R\'communicationsOmniChatSystemMessageUnit\x12\x92\x01\n*communications_omni_chat_system_attachment\x18\x87\x08 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R&communicationsOmniChatSystemAttachment\x12\xab\x01\n7communications_omni_chat_system_accumulated_attachments\x18\x88\x08 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R2communicationsOmniChatSystemAccumulatedAttachments\x12\x91\x01\n,communications_omni_email_agent_message_unit\x18\xcc\x08 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R\'communicationsOmniEmailAgentMessageUnit\x12\x86\x01\n$communications_omni_email_agent_size\x18\xcd\x08 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R communicationsOmniEmailAgentSize\x12\x9d\x01\n0communications_omni_email_agent_accumulated_size\x18\xce\x08 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R+communicationsOmniEmailAgentAccumulatedSize\x12\x97\x01\n/communications_omni_email_customer_message_unit\x18\xd6\x08 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R*communicationsOmniEmailCustomerMessageUnit\x12\x8c\x01\n\'communications_omni_email_customer_size\x18\xd7\x08 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R#communicationsOmniEmailCustomerSize\x12\xa3\x01\n3communications_omni_email_customer_accumulated_size\x18\xd8\x08 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R.communicationsOmniEmailCustomerAccumulatedSize\x12\x95\x01\n.communications_omni_email_manager_message_unit\x18\xe0\x08 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R)communicationsOmniEmailManagerMessageUnit\x12\x8a\x01\n&communications_omni_email_manager_size\x18\xe1\x08 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R\"communicationsOmniEmailManagerSize\x12\xa1\x01\n2communications_omni_email_manager_accumulated_size\x18\xe2\x08 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R-communicationsOmniEmailManagerAccumulatedSize\x12\x93\x01\n-communications_omni_email_system_message_unit\x18\xea\x08 \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R(communicationsOmniEmailSystemMessageUnit\x12\x88\x01\n%communications_omni_email_system_size\x18\xeb\x08 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R!communicationsOmniEmailSystemSize\x12\x9f\x01\n1communications_omni_email_system_accumulated_size\x18\xec\x08 \x01(\x0b\x32\x33.services.billing.entities.v1alpha3.BasicUnitConfigH\x00R,communicationsOmniEmailSystemAccumulatedSize\x12\x8f\x01\n*communications_omni_sms_agent_message_unit\x18\xb0\t \x01(\x0b\x32\x31.services.billing.entities.v1alpha3.OmniSmsConfigH\x00R%communicationsOmniSmsAgentMessageUnit\x12\x92\x01\n)communications_omni_sms_agent_attatchment\x18\xb1\t \x01(\x0b\x32\x35.services.billing.entities.v1alpha3.OmniSmsUnitConfigH\x00R%communicationsOmniSmsAgentAttatchment\x12\xab\x01\n6communications_omni_sms_agent_accumulated_attatchments\x18\xb2\t \x01(\x0b\x32\x35.services.billing.entities.v1alpha3.OmniSmsUnitConfigH\x00R1communicationsOmniSmsAgentAccumulatedAttatchments\x12\x95\x01\n-communications_omni_sms_customer_message_unit\x18\xba\t \x01(\x0b\x32\x31.services.billing.entities.v1alpha3.OmniSmsConfigH\x00R(communicationsOmniSmsCustomerMessageUnit\x12\x98\x01\n,communications_omni_sms_customer_attatchment\x18\xbb\t \x01(\x0b\x32\x35.services.billing.entities.v1alpha3.OmniSmsUnitConfigH\x00R(communicationsOmniSmsCustomerAttatchment\x12\xb1\x01\n9communications_omni_sms_customer_accumulated_attatchments\x18\xbc\t \x01(\x0b\x32\x35.services.billing.entities.v1alpha3.OmniSmsUnitConfigH\x00R4communicationsOmniSmsCustomerAccumulatedAttatchments\x12\x93\x01\n,communications_omni_sms_manager_message_unit\x18\xc4\t \x01(\x0b\x32\x31.services.billing.entities.v1alpha3.OmniSmsConfigH\x00R\'communicationsOmniSmsManagerMessageUnit\x12\x96\x01\n+communications_omni_sms_manager_attatchment\x18\xc5\t \x01(\x0b\x32\x35.services.billing.entities.v1alpha3.OmniSmsUnitConfigH\x00R\'communicationsOmniSmsManagerAttatchment\x12\xaf\x01\n8communications_omni_sms_manager_accumulated_attatchments\x18\xc6\t \x01(\x0b\x32\x35.services.billing.entities.v1alpha3.OmniSmsUnitConfigH\x00R3communicationsOmniSmsManagerAccumulatedAttatchments\x12\x91\x01\n+communications_omni_sms_system_message_unit\x18\xce\t \x01(\x0b\x32\x31.services.billing.entities.v1alpha3.OmniSmsConfigH\x00R&communicationsOmniSmsSystemMessageUnit\x12\x94\x01\n*communications_omni_sms_system_attatchment\x18\xcf\t \x01(\x0b\x32\x35.services.billing.entities.v1alpha3.OmniSmsUnitConfigH\x00R&communicationsOmniSmsSystemAttatchment\x12\xad\x01\n7communications_omni_sms_system_accumulated_attatchments\x18\xd0\t \x01(\x0b\x32\x35.services.billing.entities.v1alpha3.OmniSmsUnitConfigH\x00R2communicationsOmniSmsSystemAccumulatedAttatchments\x12y\n\x1f\x63ommunications_omni_agent_seats\x18\x94\n \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R\x1c\x63ommunicationsOmniAgentSeats\x12\x9d\x01\n2communications_omni_resources_connected_inbox_poll\x18\xf8\n \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R-communicationsOmniResourcesConnectedInboxPoll\x12\xa3\x01\n5communications_omni_resources_connected_inbox_created\x18\xf9\n \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R0communicationsOmniResourcesConnectedInboxCreated\x12\x97\x01\n/data_management_compliance_compliance_rnd_query\x18\x90N \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R*dataManagementComplianceComplianceRndQuery\x12\xa4\x01\n6data_management_compliance_compliance_rnd_query_cached\x18\x91N \x01(\x0b\x32/.services.billing.entities.v1alpha3.BasicConfigH\x00R0dataManagementComplianceComplianceRndQueryCachedB\x08\n\x06\x63onfigB\xdf\x01\n&com.services.billing.entities.v1alpha3B\nRatesProtoP\x01\xa2\x02\x03SBE\xaa\x02\"Services.Billing.Entities.V1alpha3\xca\x02\"Services\\Billing\\Entities\\V1alpha3\xe2\x02.Services\\Billing\\Entities\\V1alpha3\\GPBMetadata\xea\x02%Services::Billing::Entities::V1alpha3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.billing.entities.v1alpha3.rates_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.services.billing.entities.v1alpha3B\nRatesProtoP\001\242\002\003SBE\252\002\"Services.Billing.Entities.V1alpha3\312\002\"Services\\Billing\\Entities\\V1alpha3\342\002.Services\\Billing\\Entities\\V1alpha3\\GPBMetadata\352\002%Services::Billing::Entities::V1alpha3'
  _globals['_RATEDEFINITION']._serialized_start=217
  _globals['_RATEDEFINITION']._serialized_end=658
  _globals['_PRODUCT']._serialized_start=661
  _globals['_PRODUCT']._serialized_end=814
  _globals['_PRODUCTCONFIG']._serialized_start=817
  _globals['_PRODUCTCONFIG']._serialized_end=7236
# @@protoc_insertion_point(module_scope)
