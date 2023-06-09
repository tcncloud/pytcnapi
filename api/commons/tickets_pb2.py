# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/tickets.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/commons/tickets.proto\x12\x0b\x61pi.commons\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa3\x05\n\x06Ticket\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12#\n\x0bproject_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\nprojectSid\x12#\n\rproject_title\x18\x03 \x01(\tR\x0cprojectTitle\x12\x1f\n\x0bticket_code\x18\x04 \x01(\tR\nticketCode\x12\x14\n\x05title\x18\x05 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12\x15\n\x06org_id\x18\x07 \x01(\tR\x05orgId\x12\"\n\rcreated_by_id\x18\x08 \x01(\tR\x0b\x63reatedById\x12&\n\x0f\x63reated_by_name\x18\t \x01(\tR\rcreatedByName\x12\x42\n\x0f\x63reated_by_date\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rcreatedByDate\x12\x35\n\x08\x64ue_date\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x64ueDate\x12#\n\rassignee_list\x18\x0c \x01(\tR\x0c\x61ssigneeList\x12\x31\n\x08metadata\x18\x0e \x03(\x0b\x32\x15.api.commons.MetadataR\x08metadata\x12\x38\n\rticket_skills\x18\x0f \x03(\x0b\x32\x13.api.commons.SkillsR\x0cticketSkills\x12\x16\n\x06status\x18\x10 \x01(\x03R\x06status\x12/\n\nticket_sla\x18\x11 \x03(\x0b\x32\x10.api.commons.SlaR\tticketSla\x12\x1a\n\x08\x61ssignee\x18\x12 \x01(\tR\x08\x61ssignee\"4\n\x08Metadata\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"F\n\x06Skills\x12\x19\n\x08skill_id\x18\x01 \x01(\tR\x07skillId\x12!\n\x0cis_preferred\x18\x02 \x01(\x08R\x0bisPreferred\"h\n\x03Sla\x12\'\n\rcondition_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0c\x63onditionSid\x12\x1b\n\x07sla_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\x06slaSid\x12\x1b\n\x07sla_min\x18\x03 \x01(\x03\x42\x02\x30\x01R\x06slaMin\"\xfb\x01\n\x07\x43omment\x12#\n\x0b\x63omment_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\ncommentSid\x12!\n\nticket_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x18\n\x07\x63omment\x18\x03 \x01(\tR\x07\x63omment\x12\"\n\rcreated_by_id\x18\x04 \x01(\tR\x0b\x63reatedById\x12&\n\x0f\x63reated_by_name\x18\x05 \x01(\tR\rcreatedByName\x12\x42\n\x0f\x63reated_by_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rcreatedByDate\"\xa7\x01\n\x0b\x43loseTicket\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x16\n\x06status\x18\x02 \x01(\x03R\x06status\x12\x18\n\x07\x63omment\x18\x03 \x01(\tR\x07\x63omment\x12\x1f\n\x0b\x66rom_status\x18\x04 \x01(\x03R\nfromStatus\x12\"\n\rcreated_by_id\x18\x05 \x01(\tR\x0b\x63reatedById\"&\n\x0c\x43onfirmClose\x12\x16\n\x06status\x18\x01 \x01(\x03R\x06status\"\xe0\x01\n\rTicketProject\x12.\n\x11ticket_project_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0fticketProjectId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12#\n\x0bproject_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\nprojectSid\x12!\n\x0cproject_code\x18\x04 \x01(\tR\x0bprojectCode\x12#\n\rproject_title\x18\x05 \x01(\tR\x0cprojectTitle\x12\x1b\n\tis_active\x18\x06 \x01(\x08R\x08isActive\"\x97\x01\n\tTicketSla\x12\x1b\n\x07sla_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x06slaSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08interval\x18\x04 \x01(\x03R\x08interval\x12\x1b\n\tis_active\x18\x05 \x01(\x03R\x08isActive\"m\n\rSlaConditions\x12.\n\x11sla_condition_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0fslaConditionSid\x12,\n\x12sla_condition_name\x18\x02 \x01(\tR\x10slaConditionName\"\xd4\x01\n\x0cReplyComment\x12#\n\x0b\x63omment_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\ncommentSid\x12!\n\nticket_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x14\n\x05reply\x18\x03 \x01(\tR\x05reply\x12\"\n\rcreated_by_id\x18\x04 \x01(\tR\x0b\x63reatedById\x12\x42\n\x0f\x63reated_by_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rcreatedByDate\"4\n\x13\x43onfirmReplyComment\x12\x1d\n\nis_created\x18\x01 \x01(\x08R\tisCreated\"\xa1\x02\n\x0eTicketAuditLog\x12\x38\n\x19ticket_audit_event_log_id\x18\x01 \x01(\tR\x15ticketAuditEventLogId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x14\n\x05\x65vent\x18\x03 \x01(\tR\x05\x65vent\x12!\n\nticket_sid\x18\x04 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x1d\n\nevent_type\x18\x05 \x01(\tR\teventType\x12\"\n\rcreated_by_id\x18\x06 \x01(\tR\x0b\x63reatedById\x12\x42\n\x0f\x63reated_by_date\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rcreatedByDate\"j\n\nEditTicket\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x39\n\nedit_value\x18\x02 \x01(\x0b\x32\x1a.api.commons.EditAttributeR\teditValue\"}\n\rEditAttribute\x12\x1d\n\x08\x63ol_desc\x18\x01 \x01(\x03\x42\x02\x30\x01R\x07\x63olDesc\x12\x19\n\x08\x66rom_val\x18\x02 \x01(\tR\x07\x66romVal\x12\x15\n\x06to_val\x18\x03 \x01(\tR\x05toVal\x12\x1b\n\tis_edited\x18\x04 \x01(\x08R\x08isEditedBl\n\x0f\x63om.api.commonsB\x0cTicketsProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.tickets_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.api.commonsB\014TicketsProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _TICKET.fields_by_name['ticket_sid']._options = None
  _TICKET.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _TICKET.fields_by_name['project_sid']._options = None
  _TICKET.fields_by_name['project_sid']._serialized_options = b'0\001'
  _SLA.fields_by_name['condition_sid']._options = None
  _SLA.fields_by_name['condition_sid']._serialized_options = b'0\001'
  _SLA.fields_by_name['sla_sid']._options = None
  _SLA.fields_by_name['sla_sid']._serialized_options = b'0\001'
  _SLA.fields_by_name['sla_min']._options = None
  _SLA.fields_by_name['sla_min']._serialized_options = b'0\001'
  _COMMENT.fields_by_name['comment_sid']._options = None
  _COMMENT.fields_by_name['comment_sid']._serialized_options = b'0\001'
  _COMMENT.fields_by_name['ticket_sid']._options = None
  _COMMENT.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _CLOSETICKET.fields_by_name['ticket_sid']._options = None
  _CLOSETICKET.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _TICKETPROJECT.fields_by_name['ticket_project_id']._options = None
  _TICKETPROJECT.fields_by_name['ticket_project_id']._serialized_options = b'0\001'
  _TICKETPROJECT.fields_by_name['project_sid']._options = None
  _TICKETPROJECT.fields_by_name['project_sid']._serialized_options = b'0\001'
  _TICKETSLA.fields_by_name['sla_sid']._options = None
  _TICKETSLA.fields_by_name['sla_sid']._serialized_options = b'0\001'
  _SLACONDITIONS.fields_by_name['sla_condition_sid']._options = None
  _SLACONDITIONS.fields_by_name['sla_condition_sid']._serialized_options = b'0\001'
  _REPLYCOMMENT.fields_by_name['comment_sid']._options = None
  _REPLYCOMMENT.fields_by_name['comment_sid']._serialized_options = b'0\001'
  _REPLYCOMMENT.fields_by_name['ticket_sid']._options = None
  _REPLYCOMMENT.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _TICKETAUDITLOG.fields_by_name['ticket_sid']._options = None
  _TICKETAUDITLOG.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _EDITTICKET.fields_by_name['ticket_sid']._options = None
  _EDITTICKET.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _EDITATTRIBUTE.fields_by_name['col_desc']._options = None
  _EDITATTRIBUTE.fields_by_name['col_desc']._serialized_options = b'0\001'
  _globals['_TICKET']._serialized_start=76
  _globals['_TICKET']._serialized_end=751
  _globals['_METADATA']._serialized_start=753
  _globals['_METADATA']._serialized_end=805
  _globals['_SKILLS']._serialized_start=807
  _globals['_SKILLS']._serialized_end=877
  _globals['_SLA']._serialized_start=879
  _globals['_SLA']._serialized_end=983
  _globals['_COMMENT']._serialized_start=986
  _globals['_COMMENT']._serialized_end=1237
  _globals['_CLOSETICKET']._serialized_start=1240
  _globals['_CLOSETICKET']._serialized_end=1407
  _globals['_CONFIRMCLOSE']._serialized_start=1409
  _globals['_CONFIRMCLOSE']._serialized_end=1447
  _globals['_TICKETPROJECT']._serialized_start=1450
  _globals['_TICKETPROJECT']._serialized_end=1674
  _globals['_TICKETSLA']._serialized_start=1677
  _globals['_TICKETSLA']._serialized_end=1828
  _globals['_SLACONDITIONS']._serialized_start=1830
  _globals['_SLACONDITIONS']._serialized_end=1939
  _globals['_REPLYCOMMENT']._serialized_start=1942
  _globals['_REPLYCOMMENT']._serialized_end=2154
  _globals['_CONFIRMREPLYCOMMENT']._serialized_start=2156
  _globals['_CONFIRMREPLYCOMMENT']._serialized_end=2208
  _globals['_TICKETAUDITLOG']._serialized_start=2211
  _globals['_TICKETAUDITLOG']._serialized_end=2500
  _globals['_EDITTICKET']._serialized_start=2502
  _globals['_EDITTICKET']._serialized_end=2608
  _globals['_EDITATTRIBUTE']._serialized_start=2610
  _globals['_EDITATTRIBUTE']._serialized_end=2735
# @@protoc_insertion_point(module_scope)
