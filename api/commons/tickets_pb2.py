# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/tickets.proto
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
    'api/commons/tickets.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/commons/tickets.proto\x12\x0b\x61pi.commons\x1a\x1fgoogle/protobuf/timestamp.proto\"\x89\x07\n\x06Ticket\x12#\n\nticket_sid\x18\x01 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12#\n\x0bproject_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\nprojectSid\x12#\n\rproject_title\x18\x03 \x01(\tR\x0cprojectTitle\x12\x1f\n\x0bticket_code\x18\x04 \x01(\tR\nticketCode\x12\x14\n\x05title\x18\x05 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12\x15\n\x06org_id\x18\x07 \x01(\tR\x05orgId\x12\"\n\rcreated_by_id\x18\x08 \x01(\tR\x0b\x63reatedById\x12&\n\x0f\x63reated_by_name\x18\t \x01(\tR\rcreatedByName\x12\x42\n\x0f\x63reated_by_date\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rcreatedByDate\x12\x39\n\x08\x64ue_date\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x07\x64ueDate\x12\'\n\rassignee_list\x18\x0c \x01(\tB\x02\x18\x01R\x0c\x61ssigneeList\x12\x31\n\x08metadata\x18\x0e \x03(\x0b\x32\x15.api.commons.MetadataR\x08metadata\x12<\n\rticket_skills\x18\x0f \x03(\x0b\x32\x13.api.commons.SkillsB\x02\x18\x01R\x0cticketSkills\x12\x16\n\x06status\x18\x10 \x01(\x03R\x06status\x12/\n\nticket_sla\x18\x11 \x03(\x0b\x32\x10.api.commons.SlaR\tticketSla\x12\x1a\n\x08\x61ssignee\x18\x12 \x01(\tR\x08\x61ssignee\x12>\n\rticket_action\x18\x13 \x03(\x0b\x32\x19.api.commons.TicketActionR\x0cticketAction\x12>\n\rticket_status\x18\x14 \x01(\x0e\x32\x19.api.commons.TicketStatusR\x0cticketStatus\x12\'\n\x0fticket_assignee\x18\x15 \x03(\tR\x0eticketAssignee\x12-\n\x12ticket_participant\x18\x16 \x03(\tR\x11ticketParticipant\"\xd9\x03\n\x0eTicketTemplate\x12\x30\n\x12ticket_template_id\x18\x01 \x01(\x03\x42\x02\x18\x01R\x10ticketTemplateId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x1a\n\x08template\x18\x03 \x01(\tR\x08template\x12\x36\n\x17template_entity_version\x18\x04 \x01(\tR\x15templateEntityVersion\x12#\n\rtemplate_name\x18\x05 \x01(\tR\x0ctemplateName\x12\"\n\rcreated_by_id\x18\x06 \x01(\tR\x0b\x63reatedById\x12\x1f\n\x0bmodified_by\x18\x07 \x01(\tR\nmodifiedBy\x12=\n\x0c\x63reated_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x63reatedDate\x12?\n\rmodified_date\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cmodifiedDate\x12\x1b\n\tis_active\x18\n \x01(\x08R\x08isActive\x12#\n\x0btemplate_id\x18\x0b \x01(\x03\x42\x02\x30\x01R\ntemplateId\"\xaf\x01\n\x15TicketProjectTemplate\x12\x44\n\x0fticket_template\x18\x01 \x01(\x0b\x32\x1b.api.commons.TicketTemplateR\x0eticketTemplate\x12P\n\x13project_description\x18\x02 \x03(\x0b\x32\x1f.api.commons.ProjectDescriptionR\x12projectDescription\"\\\n\x12ProjectDescription\x12!\n\nproject_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\tprojectId\x12#\n\rproject_title\x18\x02 \x01(\tR\x0cprojectTitle\"\xb0\x03\n\x0cListTemplate\x12\x30\n\x12ticket_template_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x10ticketTemplateId\x12#\n\rtemplate_name\x18\x02 \x01(\tR\x0ctemplateName\x12!\n\nproject_id\x18\x03 \x01(\x03\x42\x02\x30\x01R\tprojectId\x12\x1a\n\x08template\x18\x04 \x01(\tR\x08template\x12\x36\n\x17template_entity_version\x18\x05 \x01(\tR\x15templateEntityVersion\x12\x1b\n\tis_active\x18\x06 \x01(\x08R\x08isActive\x12\"\n\rcreated_by_id\x18\x07 \x01(\tR\x0b\x63reatedById\x12=\n\x0c\x63reated_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x63reatedDate\x12#\n\rproject_title\x18\t \x01(\tR\x0cprojectTitle\x12)\n\x10\x61ssigned_project\x18\n \x03(\x03R\x0f\x61ssignedProject:\x02\x18\x01\"p\n\x15\x41ssignProjectTemplate\x12\x30\n\x12ticket_template_id\x18\x01 \x03(\x03\x42\x02\x30\x01R\x10ticketTemplateId\x12!\n\nproject_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\tprojectId:\x02\x18\x01\"R\n\x08\x44uration\x12\x18\n\x05value\x18\x01 \x01(\x03\x42\x02\x30\x01R\x05value\x12,\n\x05scale\x18\x02 \x01(\x0e\x32\x16.api.commons.TimeScaleR\x05scale\"\x81\x06\n\x0cTicketAction\x12,\n\x10ticket_action_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0eticketActionId\x12\x1f\n\taction_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\x08\x61\x63tionId\x12K\n\x10\x63\x61llback_context\x18\x03 \x01(\x0b\x32\x1c.api.commons.CallbackContextB\x02\x18\x01R\x0f\x63\x61llbackContext\x12!\n\tticket_id\x18\x04 \x01(\x03\x42\x04\x18\x01\x30\x01R\x08ticketId\x12\x35\n\x08start_ts\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07startTs\x12\x37\n\texpiry_ts\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08\x65xpiryTs\x12\x14\n\x05state\x18\x08 \x01(\x03R\x05state\x12#\n\raction_skills\x18\t \x03(\tR\x0c\x61\x63tionSkills\x12\x34\n\raction_sla_id\x18\n \x03(\x0b\x32\x10.api.commons.SlaR\x0b\x61\x63tionSlaId\x12 \n\x0cwork_done_by\x18\x0b \x01(\tR\nworkDoneBy\x12\x43\n\rvoice_context\x18\x0c \x01(\x0b\x32\x1c.api.commons.CallbackContextH\x00R\x0cvoiceContext\x12>\n\x0bsms_context\x18\r \x01(\x0b\x32\x1b.api.commons.SmsbackContextH\x00R\nsmsContext\x12\x44\n\remail_context\x18\x0e \x01(\x0b\x32\x1d.api.commons.EmailbackContextH\x00R\x0c\x65mailContext\x12\x38\n\x0b\x61\x63tion_type\x18\x0f \x01(\x0b\x32\x17.api.commons.ActionTypeR\nactionType\x12\x1f\n\x0bticket_code\x18\x10 \x01(\tR\nticketCodeB\t\n\x07\x63ontext\"\xbd\x01\n\x0f\x43\x61llbackContext\x12\x1b\n\tcaller_id\x18\x01 \x01(\tR\x08\x63\x61llerId\x12\x19\n\x08phone_no\x18\x02 \x01(\tR\x07phoneNo\x12!\n\x0c\x63ountry_code\x18\x03 \x01(\tR\x0b\x63ountryCode\x12\x1f\n\x0b\x63\x61ller_name\x18\x04 \x01(\tR\ncallerName\x12.\n\x13\x63\x61ller_country_code\x18\x05 \x01(\tR\x11\x63\x61llerCountryCode\"\xb9\x01\n\x0eSmsbackContext\x12!\n\x0c\x63ontact_name\x18\x01 \x01(\tR\x0b\x63ontactName\x12\x15\n\x06to_sms\x18\x02 \x01(\tR\x05toSms\x12\x19\n\x08\x66rom_sms\x18\x03 \x01(\tR\x07\x66romSms\x12&\n\x0fto_country_code\x18\x04 \x01(\tR\rtoCountryCode\x12*\n\x11\x66rom_country_code\x18\x05 \x01(\tR\x0f\x66romCountryCode\"W\n\nActionType\x12(\n\x0e\x61\x63tion_type_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0c\x61\x63tionTypeId\x12\x1f\n\x0b\x61\x63tion_name\x18\x02 \x01(\tR\nactionName\"o\n\x10\x45mailbackContext\x12!\n\x0c\x63ontact_name\x18\x01 \x01(\tR\x0b\x63ontactName\x12\x19\n\x08to_email\x18\x02 \x01(\tR\x07toEmail\x12\x1d\n\nfrom_email\x18\x03 \x01(\tR\tfromEmail\"4\n\x08Metadata\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"J\n\x06Skills\x12\x19\n\x08skill_id\x18\x01 \x01(\tR\x07skillId\x12!\n\x0cis_preferred\x18\x02 \x01(\x08R\x0bisPreferred:\x02\x18\x01\"\xa2\x01\n\x03Sla\x12\'\n\rcondition_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0c\x63onditionSid\x12\x1b\n\x07sla_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x06slaSid\x12\x1b\n\x07sla_min\x18\x03 \x01(\x03\x42\x02\x30\x01R\x06slaMin\x12\x38\n\x0csla_duration\x18\x04 \x01(\x0b\x32\x15.api.commons.DurationR\x0bslaDuration\"\x9e\x02\n\x07\x43omment\x12#\n\x0b\x63omment_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\ncommentSid\x12#\n\nticket_sid\x18\x02 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12\x18\n\x07\x63omment\x18\x03 \x01(\tR\x07\x63omment\x12\"\n\rcreated_by_id\x18\x04 \x01(\tR\x0b\x63reatedById\x12&\n\x0f\x63reated_by_name\x18\x05 \x01(\tR\rcreatedByName\x12\x42\n\x0f\x63reated_by_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rcreatedByDate\x12\x1f\n\x0bticket_code\x18\x07 \x01(\tR\nticketCode\"\xca\x01\n\x0b\x43loseTicket\x12#\n\nticket_sid\x18\x01 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12\x16\n\x06status\x18\x02 \x01(\x03R\x06status\x12\x18\n\x07\x63omment\x18\x03 \x01(\tR\x07\x63omment\x12\x1f\n\x0b\x66rom_status\x18\x04 \x01(\x03R\nfromStatus\x12\"\n\rcreated_by_id\x18\x05 \x01(\tR\x0b\x63reatedById\x12\x1f\n\x0bticket_code\x18\x06 \x01(\tR\nticketCode\"*\n\x0c\x43onfirmClose\x12\x16\n\x06status\x18\x01 \x01(\x03R\x06status:\x02\x18\x01\"\xa7\x02\n\rTicketProject\x12.\n\x11ticket_project_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0fticketProjectId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12#\n\x0bproject_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\nprojectSid\x12!\n\x0cproject_code\x18\x04 \x01(\tR\x0bprojectCode\x12#\n\rproject_title\x18\x05 \x01(\tR\x0cprojectTitle\x12\x1b\n\tis_active\x18\x06 \x01(\x08R\x08isActive\x12\x45\n\rtemplate_desc\x18\x07 \x03(\x0b\x32 .api.commons.TemplateDescriptionR\x0ctemplateDesc\"l\n\x13TemplateDescription\x12\x30\n\x12ticket_template_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x10ticketTemplateId\x12#\n\rtemplate_name\x18\x02 \x01(\tR\x0ctemplateName\"\xde\x01\n\tTicketSla\x12\x1b\n\x07sla_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x06slaSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08interval\x18\x04 \x01(\x03R\x08interval\x12\x1b\n\tis_active\x18\x05 \x01(\x03R\x08isActive\x12\x45\n\x13ticket_sla_duration\x18\x06 \x01(\x0b\x32\x15.api.commons.DurationR\x11ticketSlaDuration\"m\n\rSlaConditions\x12.\n\x11sla_condition_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0fslaConditionSid\x12,\n\x12sla_condition_name\x18\x02 \x01(\tR\x10slaConditionName\"\xf7\x01\n\x0cReplyComment\x12#\n\x0b\x63omment_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\ncommentSid\x12#\n\nticket_sid\x18\x02 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12\x14\n\x05reply\x18\x03 \x01(\tR\x05reply\x12\"\n\rcreated_by_id\x18\x04 \x01(\tR\x0b\x63reatedById\x12\x42\n\x0f\x63reated_by_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rcreatedByDate\x12\x1f\n\x0bticket_code\x18\x06 \x01(\tR\nticketCode\"8\n\x13\x43onfirmReplyComment\x12!\n\nis_created\x18\x01 \x01(\x08\x42\x02\x18\x01R\tisCreated\"\xc4\x02\n\x0eTicketAuditLog\x12\x38\n\x19ticket_audit_event_log_id\x18\x01 \x01(\tR\x15ticketAuditEventLogId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x14\n\x05\x65vent\x18\x03 \x01(\tR\x05\x65vent\x12#\n\nticket_sid\x18\x04 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12\x1d\n\nevent_type\x18\x05 \x01(\tR\teventType\x12\"\n\rcreated_by_id\x18\x06 \x01(\tR\x0b\x63reatedById\x12\x42\n\x0f\x63reated_by_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rcreatedByDate\x12\x1f\n\x0bticket_code\x18\x08 \x01(\tR\nticketCode\"\xbb\x01\n\nEditTicket\x12#\n\nticket_sid\x18\x01 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12\x39\n\nedit_value\x18\x02 \x01(\x0b\x32\x1a.api.commons.EditAttributeR\teditValue\x12\x1f\n\x0bticket_code\x18\x03 \x01(\tR\nticketCode\x12,\n\x10ticket_action_id\x18\x04 \x01(\x03\x42\x02\x30\x01R\x0eticketActionId\"}\n\rEditAttribute\x12\x1d\n\x08\x63ol_desc\x18\x01 \x01(\x03\x42\x02\x30\x01R\x07\x63olDesc\x12\x19\n\x08\x66rom_val\x18\x02 \x01(\tR\x07\x66romVal\x12\x15\n\x06to_val\x18\x03 \x01(\tR\x05toVal\x12\x1b\n\tis_edited\x18\x04 \x01(\x08R\x08isEdited\"\x82\x03\n\x0b\x43ustomField\x12,\n\x10\x63ustom_field_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0e\x63ustomFieldSid\x12*\n\x11\x63ustom_field_name\x18\x02 \x01(\tR\x0f\x63ustomFieldName\x12,\n\x12\x63ustom_field_value\x18\x03 \x01(\tR\x10\x63ustomFieldValue\x12.\n\x11\x63ustom_field_type\x18\x04 \x01(\tB\x02\x18\x01R\x0f\x63ustomFieldType\x12?\n\rdate_modified\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x64\x61teModified\x12\x1d\n\nis_deleted\x18\x06 \x01(\x08R\tisDeleted\x12[\n\x18ticket_custom_field_type\x18\x08 \x01(\x0e\x32\".api.commons.TicketCustomFieldTypeR\x15ticketCustomFieldType\"\x97\x01\n\x19TicketCustomFieldAuditLog\x12Y\n\x17\x63ustom_field_attributes\x18\x01 \x03(\x0b\x32!.api.commons.CustomFieldAttributeR\x15\x63ustomFieldAttributes\x12\x1f\n\x0bticket_code\x18\x02 \x01(\tR\nticketCode\"\xeb\x02\n\x14\x43ustomFieldAttribute\x12*\n\x0f\x63ustom_field_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\rcustomFieldId\x12N\n\x11\x63ustom_field_type\x18\x02 \x01(\x0e\x32\".api.commons.TicketCustomFieldTypeR\x0f\x63ustomFieldType\x12!\n\x0c\x65\x64ited_value\x18\x03 \x01(\tR\x0b\x65\x64itedValue\x12%\n\x0eprevious_value\x18\x04 \x01(\tR\rpreviousValue\x12*\n\x11\x63ustom_field_name\x18\x05 \x01(\tR\x0f\x63ustomFieldName\x12\x61\n\x1aticket_custom_field_status\x18\x06 \x01(\x0e\x32$.api.commons.TicketCustomFieldStatusR\x17ticketCustomFieldStatus*\x8b\x01\n\tTimeScale\x12\x15\n\x11TIME_SCALE_MINUTE\x10\x00\x12\x13\n\x0fTIME_SCALE_HOUR\x10\x01\x12\x12\n\x0eTIME_SCALE_DAY\x10\x02\x12\x13\n\x0fTIME_SCALE_WEEK\x10\x03\x12\x14\n\x10TIME_SCALE_MONTH\x10\x04\x12\x13\n\x0fTIME_SCALE_YEAR\x10\x05*V\n\x0cTicketStatus\x12\x15\n\x11TICKET_STATUS_NEW\x10\x00\x12\x16\n\x12TICKET_STATUS_OPEN\x10\x01\x12\x17\n\x13TICKET_STATUS_CLOSE\x10\x02*?\n\x0fPhoneNumberType\x12\n\n\x06MOBILE\x10\x00\x12\t\n\x05OTHER\x10\x01\x12\x11\n\rINVALID_ERROR\x10\x02\x1a\x02\x18\x01*\xfd\x01\n\x15TicketCustomFieldType\x12#\n\x1fTICKET_CUSTOMFIELD_TYPE_BOOLEAN\x10\x00\x12\"\n\x1eTICKET_CUSTOMFIELD_TYPE_STRING\x10\x01\x12\"\n\x1eTICKET_CUSTOMFIELD_TYPE_NUMBER\x10\x02\x12$\n TICKET_CUSTOMFIELD_TYPE_DATETIME\x10\x03\x12\'\n#TICKET_CUSTOMFIELD_TYPE_MULTISELECT\x10\x04\x12(\n$TICKET_CUSTOMFIELD_TYPE_SINGLESELECT\x10\x05*\x8f\x01\n\x17TicketCustomFieldStatus\x12$\n Ticket_Custom_Field_Status_Added\x10\x00\x12&\n\"Ticket_Custom_Field_Status_Updated\x10\x01\x12&\n\"Ticket_Custom_Field_Status_Deleted\x10\x02\x42l\n\x0f\x63om.api.commonsB\x0cTicketsProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.tickets_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\014TicketsProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_PHONENUMBERTYPE']._loaded_options = None
  _globals['_PHONENUMBERTYPE']._serialized_options = b'\030\001'
  _globals['_TICKET'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_TICKET'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_TICKET'].fields_by_name['project_sid']._loaded_options = None
  _globals['_TICKET'].fields_by_name['project_sid']._serialized_options = b'0\001'
  _globals['_TICKET'].fields_by_name['due_date']._loaded_options = None
  _globals['_TICKET'].fields_by_name['due_date']._serialized_options = b'\030\001'
  _globals['_TICKET'].fields_by_name['assignee_list']._loaded_options = None
  _globals['_TICKET'].fields_by_name['assignee_list']._serialized_options = b'\030\001'
  _globals['_TICKET'].fields_by_name['ticket_skills']._loaded_options = None
  _globals['_TICKET'].fields_by_name['ticket_skills']._serialized_options = b'\030\001'
  _globals['_TICKETTEMPLATE'].fields_by_name['ticket_template_id']._loaded_options = None
  _globals['_TICKETTEMPLATE'].fields_by_name['ticket_template_id']._serialized_options = b'\030\001'
  _globals['_TICKETTEMPLATE'].fields_by_name['template_id']._loaded_options = None
  _globals['_TICKETTEMPLATE'].fields_by_name['template_id']._serialized_options = b'0\001'
  _globals['_PROJECTDESCRIPTION'].fields_by_name['project_id']._loaded_options = None
  _globals['_PROJECTDESCRIPTION'].fields_by_name['project_id']._serialized_options = b'0\001'
  _globals['_LISTTEMPLATE'].fields_by_name['ticket_template_id']._loaded_options = None
  _globals['_LISTTEMPLATE'].fields_by_name['ticket_template_id']._serialized_options = b'0\001'
  _globals['_LISTTEMPLATE'].fields_by_name['project_id']._loaded_options = None
  _globals['_LISTTEMPLATE'].fields_by_name['project_id']._serialized_options = b'0\001'
  _globals['_LISTTEMPLATE']._loaded_options = None
  _globals['_LISTTEMPLATE']._serialized_options = b'\030\001'
  _globals['_ASSIGNPROJECTTEMPLATE'].fields_by_name['ticket_template_id']._loaded_options = None
  _globals['_ASSIGNPROJECTTEMPLATE'].fields_by_name['ticket_template_id']._serialized_options = b'0\001'
  _globals['_ASSIGNPROJECTTEMPLATE'].fields_by_name['project_id']._loaded_options = None
  _globals['_ASSIGNPROJECTTEMPLATE'].fields_by_name['project_id']._serialized_options = b'0\001'
  _globals['_ASSIGNPROJECTTEMPLATE']._loaded_options = None
  _globals['_ASSIGNPROJECTTEMPLATE']._serialized_options = b'\030\001'
  _globals['_DURATION'].fields_by_name['value']._loaded_options = None
  _globals['_DURATION'].fields_by_name['value']._serialized_options = b'0\001'
  _globals['_TICKETACTION'].fields_by_name['ticket_action_id']._loaded_options = None
  _globals['_TICKETACTION'].fields_by_name['ticket_action_id']._serialized_options = b'0\001'
  _globals['_TICKETACTION'].fields_by_name['action_id']._loaded_options = None
  _globals['_TICKETACTION'].fields_by_name['action_id']._serialized_options = b'0\001'
  _globals['_TICKETACTION'].fields_by_name['callback_context']._loaded_options = None
  _globals['_TICKETACTION'].fields_by_name['callback_context']._serialized_options = b'\030\001'
  _globals['_TICKETACTION'].fields_by_name['ticket_id']._loaded_options = None
  _globals['_TICKETACTION'].fields_by_name['ticket_id']._serialized_options = b'\030\0010\001'
  _globals['_ACTIONTYPE'].fields_by_name['action_type_id']._loaded_options = None
  _globals['_ACTIONTYPE'].fields_by_name['action_type_id']._serialized_options = b'0\001'
  _globals['_SKILLS']._loaded_options = None
  _globals['_SKILLS']._serialized_options = b'\030\001'
  _globals['_SLA'].fields_by_name['condition_sid']._loaded_options = None
  _globals['_SLA'].fields_by_name['condition_sid']._serialized_options = b'0\001'
  _globals['_SLA'].fields_by_name['sla_sid']._loaded_options = None
  _globals['_SLA'].fields_by_name['sla_sid']._serialized_options = b'0\001'
  _globals['_SLA'].fields_by_name['sla_min']._loaded_options = None
  _globals['_SLA'].fields_by_name['sla_min']._serialized_options = b'0\001'
  _globals['_COMMENT'].fields_by_name['comment_sid']._loaded_options = None
  _globals['_COMMENT'].fields_by_name['comment_sid']._serialized_options = b'0\001'
  _globals['_COMMENT'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_COMMENT'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_CLOSETICKET'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_CLOSETICKET'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_CONFIRMCLOSE']._loaded_options = None
  _globals['_CONFIRMCLOSE']._serialized_options = b'\030\001'
  _globals['_TICKETPROJECT'].fields_by_name['ticket_project_id']._loaded_options = None
  _globals['_TICKETPROJECT'].fields_by_name['ticket_project_id']._serialized_options = b'0\001'
  _globals['_TICKETPROJECT'].fields_by_name['project_sid']._loaded_options = None
  _globals['_TICKETPROJECT'].fields_by_name['project_sid']._serialized_options = b'0\001'
  _globals['_TEMPLATEDESCRIPTION'].fields_by_name['ticket_template_id']._loaded_options = None
  _globals['_TEMPLATEDESCRIPTION'].fields_by_name['ticket_template_id']._serialized_options = b'0\001'
  _globals['_TICKETSLA'].fields_by_name['sla_sid']._loaded_options = None
  _globals['_TICKETSLA'].fields_by_name['sla_sid']._serialized_options = b'0\001'
  _globals['_SLACONDITIONS'].fields_by_name['sla_condition_sid']._loaded_options = None
  _globals['_SLACONDITIONS'].fields_by_name['sla_condition_sid']._serialized_options = b'0\001'
  _globals['_REPLYCOMMENT'].fields_by_name['comment_sid']._loaded_options = None
  _globals['_REPLYCOMMENT'].fields_by_name['comment_sid']._serialized_options = b'0\001'
  _globals['_REPLYCOMMENT'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_REPLYCOMMENT'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_CONFIRMREPLYCOMMENT'].fields_by_name['is_created']._loaded_options = None
  _globals['_CONFIRMREPLYCOMMENT'].fields_by_name['is_created']._serialized_options = b'\030\001'
  _globals['_TICKETAUDITLOG'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_TICKETAUDITLOG'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_EDITTICKET'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_EDITTICKET'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_EDITTICKET'].fields_by_name['ticket_action_id']._loaded_options = None
  _globals['_EDITTICKET'].fields_by_name['ticket_action_id']._serialized_options = b'0\001'
  _globals['_EDITATTRIBUTE'].fields_by_name['col_desc']._loaded_options = None
  _globals['_EDITATTRIBUTE'].fields_by_name['col_desc']._serialized_options = b'0\001'
  _globals['_CUSTOMFIELD'].fields_by_name['custom_field_sid']._loaded_options = None
  _globals['_CUSTOMFIELD'].fields_by_name['custom_field_sid']._serialized_options = b'0\001'
  _globals['_CUSTOMFIELD'].fields_by_name['custom_field_type']._loaded_options = None
  _globals['_CUSTOMFIELD'].fields_by_name['custom_field_type']._serialized_options = b'\030\001'
  _globals['_CUSTOMFIELDATTRIBUTE'].fields_by_name['custom_field_id']._loaded_options = None
  _globals['_CUSTOMFIELDATTRIBUTE'].fields_by_name['custom_field_id']._serialized_options = b'0\001'
  _globals['_TIMESCALE']._serialized_start=7157
  _globals['_TIMESCALE']._serialized_end=7296
  _globals['_TICKETSTATUS']._serialized_start=7298
  _globals['_TICKETSTATUS']._serialized_end=7384
  _globals['_PHONENUMBERTYPE']._serialized_start=7386
  _globals['_PHONENUMBERTYPE']._serialized_end=7449
  _globals['_TICKETCUSTOMFIELDTYPE']._serialized_start=7452
  _globals['_TICKETCUSTOMFIELDTYPE']._serialized_end=7705
  _globals['_TICKETCUSTOMFIELDSTATUS']._serialized_start=7708
  _globals['_TICKETCUSTOMFIELDSTATUS']._serialized_end=7851
  _globals['_TICKET']._serialized_start=76
  _globals['_TICKET']._serialized_end=981
  _globals['_TICKETTEMPLATE']._serialized_start=984
  _globals['_TICKETTEMPLATE']._serialized_end=1457
  _globals['_TICKETPROJECTTEMPLATE']._serialized_start=1460
  _globals['_TICKETPROJECTTEMPLATE']._serialized_end=1635
  _globals['_PROJECTDESCRIPTION']._serialized_start=1637
  _globals['_PROJECTDESCRIPTION']._serialized_end=1729
  _globals['_LISTTEMPLATE']._serialized_start=1732
  _globals['_LISTTEMPLATE']._serialized_end=2164
  _globals['_ASSIGNPROJECTTEMPLATE']._serialized_start=2166
  _globals['_ASSIGNPROJECTTEMPLATE']._serialized_end=2278
  _globals['_DURATION']._serialized_start=2280
  _globals['_DURATION']._serialized_end=2362
  _globals['_TICKETACTION']._serialized_start=2365
  _globals['_TICKETACTION']._serialized_end=3134
  _globals['_CALLBACKCONTEXT']._serialized_start=3137
  _globals['_CALLBACKCONTEXT']._serialized_end=3326
  _globals['_SMSBACKCONTEXT']._serialized_start=3329
  _globals['_SMSBACKCONTEXT']._serialized_end=3514
  _globals['_ACTIONTYPE']._serialized_start=3516
  _globals['_ACTIONTYPE']._serialized_end=3603
  _globals['_EMAILBACKCONTEXT']._serialized_start=3605
  _globals['_EMAILBACKCONTEXT']._serialized_end=3716
  _globals['_METADATA']._serialized_start=3718
  _globals['_METADATA']._serialized_end=3770
  _globals['_SKILLS']._serialized_start=3772
  _globals['_SKILLS']._serialized_end=3846
  _globals['_SLA']._serialized_start=3849
  _globals['_SLA']._serialized_end=4011
  _globals['_COMMENT']._serialized_start=4014
  _globals['_COMMENT']._serialized_end=4300
  _globals['_CLOSETICKET']._serialized_start=4303
  _globals['_CLOSETICKET']._serialized_end=4505
  _globals['_CONFIRMCLOSE']._serialized_start=4507
  _globals['_CONFIRMCLOSE']._serialized_end=4549
  _globals['_TICKETPROJECT']._serialized_start=4552
  _globals['_TICKETPROJECT']._serialized_end=4847
  _globals['_TEMPLATEDESCRIPTION']._serialized_start=4849
  _globals['_TEMPLATEDESCRIPTION']._serialized_end=4957
  _globals['_TICKETSLA']._serialized_start=4960
  _globals['_TICKETSLA']._serialized_end=5182
  _globals['_SLACONDITIONS']._serialized_start=5184
  _globals['_SLACONDITIONS']._serialized_end=5293
  _globals['_REPLYCOMMENT']._serialized_start=5296
  _globals['_REPLYCOMMENT']._serialized_end=5543
  _globals['_CONFIRMREPLYCOMMENT']._serialized_start=5545
  _globals['_CONFIRMREPLYCOMMENT']._serialized_end=5601
  _globals['_TICKETAUDITLOG']._serialized_start=5604
  _globals['_TICKETAUDITLOG']._serialized_end=5928
  _globals['_EDITTICKET']._serialized_start=5931
  _globals['_EDITTICKET']._serialized_end=6118
  _globals['_EDITATTRIBUTE']._serialized_start=6120
  _globals['_EDITATTRIBUTE']._serialized_end=6245
  _globals['_CUSTOMFIELD']._serialized_start=6248
  _globals['_CUSTOMFIELD']._serialized_end=6634
  _globals['_TICKETCUSTOMFIELDAUDITLOG']._serialized_start=6637
  _globals['_TICKETCUSTOMFIELDAUDITLOG']._serialized_end=6788
  _globals['_CUSTOMFIELDATTRIBUTE']._serialized_start=6791
  _globals['_CUSTOMFIELDATTRIBUTE']._serialized_end=7154
# @@protoc_insertion_point(module_scope)
