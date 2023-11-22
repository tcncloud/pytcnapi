# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/tickets/project.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.audit import audit_pb2 as api_dot_commons_dot_audit_dot_audit__pb2
from api.commons import tickets_pb2 as api_dot_commons_dot_tickets__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/tickets/project.proto\x12\x14\x61pi.v1alpha1.tickets\x1a\x1d\x61pi/commons/audit/audit.proto\x1a\x19\x61pi/commons/tickets.proto\"\x9c\x01\n\x10\x45nableProjectReq\x12#\n\x0bproject_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\nprojectSid\x12!\n\x0cproject_code\x18\x02 \x01(\tR\x0bprojectCode\x12#\n\rproject_title\x18\x03 \x01(\tR\x0cprojectTitle\x12\x1b\n\tis_active\x18\x04 \x01(\x08R\x08isActive\",\n\x10\x45nableProjectRes\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\"\x18\n\x16ListEnabledProjectsReq\"P\n\x16ListEnabledProjectsRes\x12\x36\n\x08projects\x18\x01 \x03(\x0b\x32\x1a.api.commons.TicketProjectR\x08projects\":\n\x15ListTicketAuditLogReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\"N\n\x15ListTicketAuditLogRes\x12\x35\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x1d.api.commons.audit.AuditEventR\x06\x65ventsB\x9a\x01\n\x18\x63om.api.v1alpha1.ticketsB\x0cProjectProtoP\x01\xa2\x02\x03\x41VT\xaa\x02\x14\x41pi.V1alpha1.Tickets\xca\x02\x14\x41pi\\V1alpha1\\Tickets\xe2\x02 Api\\V1alpha1\\Tickets\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Ticketsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.tickets.project_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.ticketsB\014ProjectProtoP\001\242\002\003AVT\252\002\024Api.V1alpha1.Tickets\312\002\024Api\\V1alpha1\\Tickets\342\002 Api\\V1alpha1\\Tickets\\GPBMetadata\352\002\026Api::V1alpha1::Tickets'
  _globals['_ENABLEPROJECTREQ'].fields_by_name['project_sid']._options = None
  _globals['_ENABLEPROJECTREQ'].fields_by_name['project_sid']._serialized_options = b'0\001'
  _globals['_LISTTICKETAUDITLOGREQ'].fields_by_name['ticket_sid']._options = None
  _globals['_LISTTICKETAUDITLOGREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_ENABLEPROJECTREQ']._serialized_start=119
  _globals['_ENABLEPROJECTREQ']._serialized_end=275
  _globals['_ENABLEPROJECTRES']._serialized_start=277
  _globals['_ENABLEPROJECTRES']._serialized_end=321
  _globals['_LISTENABLEDPROJECTSREQ']._serialized_start=323
  _globals['_LISTENABLEDPROJECTSREQ']._serialized_end=347
  _globals['_LISTENABLEDPROJECTSRES']._serialized_start=349
  _globals['_LISTENABLEDPROJECTSRES']._serialized_end=429
  _globals['_LISTTICKETAUDITLOGREQ']._serialized_start=431
  _globals['_LISTTICKETAUDITLOGREQ']._serialized_end=489
  _globals['_LISTTICKETAUDITLOGRES']._serialized_start=491
  _globals['_LISTTICKETAUDITLOGRES']._serialized_end=569
# @@protoc_insertion_point(module_scope)
