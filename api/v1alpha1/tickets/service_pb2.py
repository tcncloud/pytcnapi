# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/tickets/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.tickets import project_pb2 as api_dot_v1alpha1_dot_tickets_dot_project__pb2
from api.v1alpha1.tickets import ticket_pb2 as api_dot_v1alpha1_dot_tickets_dot_ticket__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/tickets/service.proto\x12\x14\x61pi.v1alpha1.tickets\x1a\x17\x61nnotations/authz.proto\x1a\"api/v1alpha1/tickets/project.proto\x1a!api/v1alpha1/tickets/ticket.proto\x1a\x1cgoogle/api/annotations.proto2\xe0\x12\n\x07Tickets\x12\x9d\x01\n\x0c\x43reateTicket\x12%.api.v1alpha1.tickets.CreateTicketReq\x1a%.api.v1alpha1.tickets.CreateTicketRes\"?\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/tickets/tickets/createticket:\x01*\x12\x95\x01\n\nEditTicket\x12#.api.v1alpha1.tickets.EditTicketReq\x1a#.api.v1alpha1.tickets.EditTicketRes\"=\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/tickets/tickets/editticket:\x01*\x12\x99\x01\n\x0bListTickets\x12$.api.v1alpha1.tickets.ListTicketsReq\x1a$.api.v1alpha1.tickets.ListTicketsRes\">\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/tickets/tickets/listtickets:\x01*\x12\x9d\x01\n\x0c\x41ssignTicket\x12%.api.v1alpha1.tickets.AssignTicketReq\x1a%.api.v1alpha1.tickets.AssignTicketRes\"?\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/tickets/tickets/assignticket:\x01*\x12\x99\x01\n\x0b\x43loseTicket\x12$.api.v1alpha1.tickets.CloseTicketReq\x1a$.api.v1alpha1.tickets.CloseTicketRes\">\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/tickets/tickets/closeticket:\x01*\x12\x95\x01\n\nViewTicket\x12#.api.v1alpha1.tickets.ViewTicketReq\x1a#.api.v1alpha1.tickets.ViewTicketRes\"=\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/tickets/tickets/viewticket:\x01*\x12\xa1\x01\n\rCreateComment\x12&.api.v1alpha1.tickets.CreateCommentReq\x1a&.api.v1alpha1.tickets.CreateCommentRes\"@\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/tickets/tickets/createcomment:\x01*\x12\xa1\x01\n\rEnableProject\x12&.api.v1alpha1.tickets.EnableProjectReq\x1a&.api.v1alpha1.tickets.EnableProjectRes\"@\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/tickets/tickets/enableproject:\x01*\x12\xb2\x01\n\x13ListEnabledProjects\x12,.api.v1alpha1.tickets.ListEnabledProjectsReq\x1a,.api.v1alpha1.tickets.ListEnabledProjectsRes\"?\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/tickets/tickets/listprojects:\x01*\x12\x91\x01\n\tCreateSLA\x12\".api.v1alpha1.tickets.CreateSlaReq\x1a\".api.v1alpha1.tickets.CreateSlaRes\"<\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/tickets/tickets/createsla:\x01*\x12\x89\x01\n\x07ListSLA\x12 .api.v1alpha1.tickets.ListSlaReq\x1a .api.v1alpha1.tickets.ListSlaRes\":\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/tickets/tickets/listsla:\x01*\x12\x91\x01\n\tUpdateSLA\x12\".api.v1alpha1.tickets.UpdateSlaReq\x1a\".api.v1alpha1.tickets.UpdateSlaRes\"<\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/tickets/tickets/updatesla:\x01*\x12\xad\x01\n\x10ListSLACondition\x12).api.v1alpha1.tickets.ListSlaConditionReq\x1a).api.v1alpha1.tickets.ListSlaConditionRes\"C\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/tickets/tickets/listslacondition:\x01*\x12\x9d\x01\n\x0cReplyComment\x12%.api.v1alpha1.tickets.ReplyCommentReq\x1a%.api.v1alpha1.tickets.ReplyCommentRes\"?\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/tickets/tickets/replycomment:\x01*\x12\xab\x01\n\x12ListTicketAuditLog\x12+.api.v1alpha1.tickets.ListTicketAuditLogReq\x1a+.api.v1alpha1.tickets.ListTicketAuditLogRes\";\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/tickets/tickets/auditlog:\x01*B\x9a\x01\n\x18\x63om.api.v1alpha1.ticketsB\x0cServiceProtoP\x01\xa2\x02\x03\x41VT\xaa\x02\x14\x41pi.V1alpha1.Tickets\xca\x02\x14\x41pi\\V1alpha1\\Tickets\xe2\x02 Api\\V1alpha1\\Tickets\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Ticketsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.tickets.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.api.v1alpha1.ticketsB\014ServiceProtoP\001\242\002\003AVT\252\002\024Api.V1alpha1.Tickets\312\002\024Api\\V1alpha1\\Tickets\342\002 Api\\V1alpha1\\Tickets\\GPBMetadata\352\002\026Api::V1alpha1::Tickets'
  _TICKETS.methods_by_name['CreateTicket']._options = None
  _TICKETS.methods_by_name['CreateTicket']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002/\"*/api/v1alpha1/tickets/tickets/createticket:\001*'
  _TICKETS.methods_by_name['EditTicket']._options = None
  _TICKETS.methods_by_name['EditTicket']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002-\"(/api/v1alpha1/tickets/tickets/editticket:\001*'
  _TICKETS.methods_by_name['ListTickets']._options = None
  _TICKETS.methods_by_name['ListTickets']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002.\")/api/v1alpha1/tickets/tickets/listtickets:\001*'
  _TICKETS.methods_by_name['AssignTicket']._options = None
  _TICKETS.methods_by_name['AssignTicket']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002/\"*/api/v1alpha1/tickets/tickets/assignticket:\001*'
  _TICKETS.methods_by_name['CloseTicket']._options = None
  _TICKETS.methods_by_name['CloseTicket']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002.\")/api/v1alpha1/tickets/tickets/closeticket:\001*'
  _TICKETS.methods_by_name['ViewTicket']._options = None
  _TICKETS.methods_by_name['ViewTicket']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002-\"(/api/v1alpha1/tickets/tickets/viewticket:\001*'
  _TICKETS.methods_by_name['CreateComment']._options = None
  _TICKETS.methods_by_name['CreateComment']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0020\"+/api/v1alpha1/tickets/tickets/createcomment:\001*'
  _TICKETS.methods_by_name['EnableProject']._options = None
  _TICKETS.methods_by_name['EnableProject']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\0020\"+/api/v1alpha1/tickets/tickets/enableproject:\001*'
  _TICKETS.methods_by_name['ListEnabledProjects']._options = None
  _TICKETS.methods_by_name['ListEnabledProjects']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002/\"*/api/v1alpha1/tickets/tickets/listprojects:\001*'
  _TICKETS.methods_by_name['CreateSLA']._options = None
  _TICKETS.methods_by_name['CreateSLA']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\002,\"\'/api/v1alpha1/tickets/tickets/createsla:\001*'
  _TICKETS.methods_by_name['ListSLA']._options = None
  _TICKETS.methods_by_name['ListSLA']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\002*\"%/api/v1alpha1/tickets/tickets/listsla:\001*'
  _TICKETS.methods_by_name['UpdateSLA']._options = None
  _TICKETS.methods_by_name['UpdateSLA']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\002,\"\'/api/v1alpha1/tickets/tickets/updatesla:\001*'
  _TICKETS.methods_by_name['ListSLACondition']._options = None
  _TICKETS.methods_by_name['ListSLACondition']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\0023\"./api/v1alpha1/tickets/tickets/listslacondition:\001*'
  _TICKETS.methods_by_name['ReplyComment']._options = None
  _TICKETS.methods_by_name['ReplyComment']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002/\"*/api/v1alpha1/tickets/tickets/replycomment:\001*'
  _TICKETS.methods_by_name['ListTicketAuditLog']._options = None
  _TICKETS.methods_by_name['ListTicketAuditLog']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002+\"&/api/v1alpha1/tickets/tickets/auditlog:\001*'
  _globals['_TICKETS']._serialized_start=187
  _globals['_TICKETS']._serialized_end=2587
# @@protoc_insertion_point(module_scope)
