# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/tickets/service.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'api/v1alpha1/tickets/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.tickets import project_pb2 as api_dot_v1alpha1_dot_tickets_dot_project__pb2
from api.v1alpha1.tickets import ticket_pb2 as api_dot_v1alpha1_dot_tickets_dot_ticket__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/v1alpha1/tickets/service.proto\x12\x14\x61pi.v1alpha1.tickets\x1a\x17\x61nnotations/authz.proto\x1a\"api/v1alpha1/tickets/project.proto\x1a!api/v1alpha1/tickets/ticket.proto\x1a\x1cgoogle/api/annotations.proto2\xfa\x34\n\x07Tickets\x12\x9d\x01\n\x0c\x43reateTicket\x12%.api.v1alpha1.tickets.CreateTicketReq\x1a%.api.v1alpha1.tickets.CreateTicketRes\"?\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/tickets/tickets/createticket:\x01*\x12\x98\x01\n\nEditTicket\x12#.api.v1alpha1.tickets.EditTicketReq\x1a#.api.v1alpha1.tickets.EditTicketRes\"@\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/tickets/tickets/editticket:\x01*\x12\x99\x01\n\x0bListTickets\x12$.api.v1alpha1.tickets.ListTicketsReq\x1a$.api.v1alpha1.tickets.ListTicketsRes\">\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/tickets/tickets/listtickets:\x01*\x12\xa0\x01\n\x0c\x41ssignTicket\x12%.api.v1alpha1.tickets.AssignTicketReq\x1a%.api.v1alpha1.tickets.AssignTicketRes\"B\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/tickets/tickets/assignticket:\x01*\x12\x99\x01\n\x0b\x43loseTicket\x12$.api.v1alpha1.tickets.CloseTicketReq\x1a$.api.v1alpha1.tickets.CloseTicketRes\">\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/tickets/tickets/closeticket:\x01*\x12\x95\x01\n\nViewTicket\x12#.api.v1alpha1.tickets.ViewTicketReq\x1a#.api.v1alpha1.tickets.ViewTicketRes\"=\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/tickets/tickets/viewticket:\x01*\x12\xa1\x01\n\rCreateComment\x12&.api.v1alpha1.tickets.CreateCommentReq\x1a&.api.v1alpha1.tickets.CreateCommentRes\"@\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/tickets/tickets/createcomment:\x01*\x12\xa1\x01\n\rEnableProject\x12&.api.v1alpha1.tickets.EnableProjectReq\x1a&.api.v1alpha1.tickets.EnableProjectRes\"@\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/tickets/tickets/enableproject:\x01*\x12\xb2\x01\n\x13ListEnabledProjects\x12,.api.v1alpha1.tickets.ListEnabledProjectsReq\x1a,.api.v1alpha1.tickets.ListEnabledProjectsRes\"?\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/tickets/tickets/listprojects:\x01*\x12\x91\x01\n\tCreateSLA\x12\".api.v1alpha1.tickets.CreateSlaReq\x1a\".api.v1alpha1.tickets.CreateSlaRes\"<\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/tickets/tickets/createsla:\x01*\x12\x8e\x01\n\x07ListSLA\x12 .api.v1alpha1.tickets.ListSlaReq\x1a .api.v1alpha1.tickets.ListSlaRes\"?\xba\xb8\x91\x02\n\n\x03\x08\x9d\x18\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/tickets/tickets/listsla:\x01*\x12\x91\x01\n\tUpdateSLA\x12\".api.v1alpha1.tickets.UpdateSlaReq\x1a\".api.v1alpha1.tickets.UpdateSlaRes\"<\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/tickets/tickets/updatesla:\x01*\x12\xb2\x01\n\x10ListSLACondition\x12).api.v1alpha1.tickets.ListSlaConditionReq\x1a).api.v1alpha1.tickets.ListSlaConditionRes\"H\xba\xb8\x91\x02\n\n\x03\x08\x9d\x18\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/tickets/tickets/listslacondition:\x01*\x12\x9d\x01\n\x0cReplyComment\x12%.api.v1alpha1.tickets.ReplyCommentReq\x1a%.api.v1alpha1.tickets.ReplyCommentRes\"?\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/tickets/tickets/replycomment:\x01*\x12\xab\x01\n\x12ListTicketAuditLog\x12+.api.v1alpha1.tickets.ListTicketAuditLogReq\x1a+.api.v1alpha1.tickets.ListTicketAuditLogRes\";\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02+\"&/api/v1alpha1/tickets/tickets/auditlog:\x01*\x12\xa4\x01\n\nAssignSelf\x12).api.v1alpha1.tickets.CreateSelfAssignReq\x1a).api.v1alpha1.tickets.CreateSelfAssignRes\"@\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/tickets/tickets/assignself:\x01*\x12\xa5\x01\n\x0e\x45\x64itMaskTicket\x12\'.api.v1alpha1.tickets.EditMaskTicketReq\x1a\'.api.v1alpha1.tickets.EditMaskTicketRes\"A\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/tickets/tickets/editmaskticket:\x01*\x12\xbe\x01\n\x14ListAllocatedTickets\x12,.api.v1alpha1.tickets.ListAllocatedTicketReq\x1a,.api.v1alpha1.tickets.ListAllocatedTicketRes\"J\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x37\"2/api/v1alpha1/tickets/tickets/listallocatedtickets:\x01*\x12\xda\x01\n\x19ListAvailableAgentTickets\x12\x36.api.v1alpha1.tickets.ListAvailableAgentTicketsRequest\x1a\x37.api.v1alpha1.tickets.ListAvailableAgentTicketsResponse\"L\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02<\"7/api/v1alpha1/tickets/tickets/listavailableagenttickets:\x01*\x12\xb6\x01\n\x10ListAgentTickets\x12-.api.v1alpha1.tickets.ListAgentTicketsRequest\x1a..api.v1alpha1.tickets.ListAgentTicketsResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/tickets/tickets/listagenttickets:\x01*\x12\x9e\x01\n\nListSkills\x12\'.api.v1alpha1.tickets.ListSkillsRequest\x1a(.api.v1alpha1.tickets.ListSkillsResponse\"=\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/tickets/tickets/listskills:\x01*\x12\x9a\x01\n\tListUsers\x12&.api.v1alpha1.tickets.ListUsersRequest\x1a\'.api.v1alpha1.tickets.ListUsersResponse\"<\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/tickets/tickets/listusers:\x01*\x12\xba\x01\n\x11\x43loseTicketAction\x12..api.v1alpha1.tickets.CloseTicketActionRequest\x1a/.api.v1alpha1.tickets.CloseTicketActionResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/tickets/tickets/closeticketaction:\x01*\x12\xc1\x01\n\x12\x41ssignTicketAction\x12/.api.v1alpha1.tickets.AssignTicketActionRequest\x1a\x30.api.v1alpha1.tickets.AssignTicketActionResponse\"H\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/tickets/tickets/assignticketaction:\x01*\x12\xbe\x01\n\x12\x43reateTicketAction\x12/.api.v1alpha1.tickets.CreateTicketActionRequest\x1a\x30.api.v1alpha1.tickets.CreateTicketActionResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/tickets/tickets/createticketaction:\x01*\x12\xc1\x01\n\x12\x43hangeTicketStatus\x12/.api.v1alpha1.tickets.ChangeTicketStatusRequest\x1a\x30.api.v1alpha1.tickets.ChangeTicketStatusResponse\"H\x88\x02\x01\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/tickets/tickets/changeticketstatus:\x01*\x12\xc6\x01\n\x14\x43reateTicketTemplate\x12\x31.api.v1alpha1.tickets.CreateTicketTemplateRequest\x1a\x32.api.v1alpha1.tickets.CreateTicketTemplateResponse\"G\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02\x37\"2/api/v1alpha1/tickets/tickets/createtickettemplate:\x01*\x12\xbe\x01\n\x12\x45\x64itTicketTemplate\x12/.api.v1alpha1.tickets.EditTicketTemplateRequest\x1a\x30.api.v1alpha1.tickets.EditTicketTemplateResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/tickets/tickets/edittickettemplate:\x01*\x12\xc3\x01\n\x12ListTicketTemplate\x12/.api.v1alpha1.tickets.ListTicketTemplateRequest\x1a\x30.api.v1alpha1.tickets.ListTicketTemplateResponse\"J\xba\xb8\x91\x02\n\n\x03\x08\x9d\x18\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/tickets/tickets/listtickettemplate:\x01*\x12\xc8\x01\n\x14\x41ssignTicketTemplate\x12\x32.api.v1alpha1.tickets.AssignProjectTemplateRequest\x1a\x33.api.v1alpha1.tickets.AssignProjectTemplateResponse\"G\xba\xb8\x91\x02\x05\n\x03\x08\x9d\x18\x82\xd3\xe4\x93\x02\x37\"2/api/v1alpha1/tickets/tickets/assigntickettemplate:\x01*\x12\xb5\x01\n\x10GetAllActionType\x12*.api.v1alpha1.tickets.GetActionTypeRequest\x1a+.api.v1alpha1.tickets.GetActionTypeResponse\"H\xba\xb8\x91\x02\n\n\x03\x08\x9d\x18\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/tickets/tickets/getallActiontype:\x01*\x12\xc6\x01\n\x12GetPhoneNumberType\x12/.api.v1alpha1.tickets.GetPhoneNumberTypeRequest\x1a\x30.api.v1alpha1.tickets.GetPhoneNumberTypeResponse\"M\x88\x02\x01\xba\xb8\x91\x02\n\n\x03\x08\x9d\x18\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/tickets/tickets/getphonenumbertype:\x01*\x12\xab\x01\n\x0c\x41\x64\x64\x45ntityRef\x12).api.v1alpha1.tickets.AddEntityRefRequest\x1a*.api.v1alpha1.tickets.AddEntityRefResponse\"D\xba\xb8\x91\x02\n\n\x03\x08\x9d\x18\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/tickets/tickets/addentityref:\x01*\x12\xd3\x01\n\x16ListTicketsByEntityRef\x12\x33.api.v1alpha1.tickets.ListTicketsByEntityRefRequest\x1a\x34.api.v1alpha1.tickets.ListTicketsByEntityRefResponse\"N\xba\xb8\x91\x02\n\n\x03\x08\x9d\x18\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/tickets/tickets/listticketsbyentityref:\x01*\x12\xd3\x01\n\x16ListEntityRefsByTicket\x12\x33.api.v1alpha1.tickets.ListEntityRefsByTicketRequest\x1a\x34.api.v1alpha1.tickets.ListEntityRefsByTicketResponse\"N\xba\xb8\x91\x02\n\n\x03\x08\x9d\x18\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/tickets/tickets/listentityrefsbyticket:\x01*\x12\xba\x01\n\x11\x43reateCustomField\x12..api.v1alpha1.tickets.CreateCustomFieldRequest\x1a/.api.v1alpha1.tickets.CreateCustomFieldResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/tickets/tickets/createcustomfield:\x01*\x12\xb2\x01\n\x0f\x45\x64itCustomField\x12,.api.v1alpha1.tickets.EditCustomFieldRequest\x1a-.api.v1alpha1.tickets.EditCustomFieldResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/tickets/tickets/editcustomfield:\x01*\x12\xb5\x01\n\x10ListCustomFields\x12-.api.v1alpha1.tickets.ListCustomFieldsRequest\x1a..api.v1alpha1.tickets.ListCustomFieldsResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\x9c\x18\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/tickets/tickets/listcustomfield:\x01*B\x9a\x01\n\x18\x63om.api.v1alpha1.ticketsB\x0cServiceProtoP\x01\xa2\x02\x03\x41VT\xaa\x02\x14\x41pi.V1alpha1.Tickets\xca\x02\x14\x41pi\\V1alpha1\\Tickets\xe2\x02 Api\\V1alpha1\\Tickets\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Ticketsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.tickets.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.ticketsB\014ServiceProtoP\001\242\002\003AVT\252\002\024Api.V1alpha1.Tickets\312\002\024Api\\V1alpha1\\Tickets\342\002 Api\\V1alpha1\\Tickets\\GPBMetadata\352\002\026Api::V1alpha1::Tickets'
  _globals['_TICKETS'].methods_by_name['CreateTicket']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['CreateTicket']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002/\"*/api/v1alpha1/tickets/tickets/createticket:\001*'
  _globals['_TICKETS'].methods_by_name['EditTicket']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['EditTicket']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002-\"(/api/v1alpha1/tickets/tickets/editticket:\001*'
  _globals['_TICKETS'].methods_by_name['ListTickets']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListTickets']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002.\")/api/v1alpha1/tickets/tickets/listtickets:\001*'
  _globals['_TICKETS'].methods_by_name['AssignTicket']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['AssignTicket']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002/\"*/api/v1alpha1/tickets/tickets/assignticket:\001*'
  _globals['_TICKETS'].methods_by_name['CloseTicket']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['CloseTicket']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002.\")/api/v1alpha1/tickets/tickets/closeticket:\001*'
  _globals['_TICKETS'].methods_by_name['ViewTicket']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ViewTicket']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002-\"(/api/v1alpha1/tickets/tickets/viewticket:\001*'
  _globals['_TICKETS'].methods_by_name['CreateComment']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['CreateComment']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0020\"+/api/v1alpha1/tickets/tickets/createcomment:\001*'
  _globals['_TICKETS'].methods_by_name['EnableProject']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['EnableProject']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\0020\"+/api/v1alpha1/tickets/tickets/enableproject:\001*'
  _globals['_TICKETS'].methods_by_name['ListEnabledProjects']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListEnabledProjects']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002/\"*/api/v1alpha1/tickets/tickets/listprojects:\001*'
  _globals['_TICKETS'].methods_by_name['CreateSLA']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['CreateSLA']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\002,\"\'/api/v1alpha1/tickets/tickets/createsla:\001*'
  _globals['_TICKETS'].methods_by_name['ListSLA']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListSLA']._serialized_options = b'\272\270\221\002\n\n\003\010\235\030\n\003\010\234\030\202\323\344\223\002*\"%/api/v1alpha1/tickets/tickets/listsla:\001*'
  _globals['_TICKETS'].methods_by_name['UpdateSLA']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['UpdateSLA']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\002,\"\'/api/v1alpha1/tickets/tickets/updatesla:\001*'
  _globals['_TICKETS'].methods_by_name['ListSLACondition']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListSLACondition']._serialized_options = b'\272\270\221\002\n\n\003\010\235\030\n\003\010\234\030\202\323\344\223\0023\"./api/v1alpha1/tickets/tickets/listslacondition:\001*'
  _globals['_TICKETS'].methods_by_name['ReplyComment']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ReplyComment']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002/\"*/api/v1alpha1/tickets/tickets/replycomment:\001*'
  _globals['_TICKETS'].methods_by_name['ListTicketAuditLog']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListTicketAuditLog']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002+\"&/api/v1alpha1/tickets/tickets/auditlog:\001*'
  _globals['_TICKETS'].methods_by_name['AssignSelf']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['AssignSelf']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002-\"(/api/v1alpha1/tickets/tickets/assignself:\001*'
  _globals['_TICKETS'].methods_by_name['EditMaskTicket']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['EditMaskTicket']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0021\",/api/v1alpha1/tickets/tickets/editmaskticket:\001*'
  _globals['_TICKETS'].methods_by_name['ListAllocatedTickets']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListAllocatedTickets']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0027\"2/api/v1alpha1/tickets/tickets/listallocatedtickets:\001*'
  _globals['_TICKETS'].methods_by_name['ListAvailableAgentTickets']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListAvailableAgentTickets']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002<\"7/api/v1alpha1/tickets/tickets/listavailableagenttickets:\001*'
  _globals['_TICKETS'].methods_by_name['ListAgentTickets']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListAgentTickets']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0023\"./api/v1alpha1/tickets/tickets/listagenttickets:\001*'
  _globals['_TICKETS'].methods_by_name['ListSkills']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListSkills']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002-\"(/api/v1alpha1/tickets/tickets/listskills:\001*'
  _globals['_TICKETS'].methods_by_name['ListUsers']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListUsers']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\002,\"\'/api/v1alpha1/tickets/tickets/listusers:\001*'
  _globals['_TICKETS'].methods_by_name['CloseTicketAction']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['CloseTicketAction']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0024\"//api/v1alpha1/tickets/tickets/closeticketaction:\001*'
  _globals['_TICKETS'].methods_by_name['AssignTicketAction']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['AssignTicketAction']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0025\"0/api/v1alpha1/tickets/tickets/assignticketaction:\001*'
  _globals['_TICKETS'].methods_by_name['CreateTicketAction']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['CreateTicketAction']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0025\"0/api/v1alpha1/tickets/tickets/createticketaction:\001*'
  _globals['_TICKETS'].methods_by_name['ChangeTicketStatus']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ChangeTicketStatus']._serialized_options = b'\210\002\001\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0025\"0/api/v1alpha1/tickets/tickets/changeticketstatus:\001*'
  _globals['_TICKETS'].methods_by_name['CreateTicketTemplate']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['CreateTicketTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\0027\"2/api/v1alpha1/tickets/tickets/createtickettemplate:\001*'
  _globals['_TICKETS'].methods_by_name['EditTicketTemplate']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['EditTicketTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\0025\"0/api/v1alpha1/tickets/tickets/edittickettemplate:\001*'
  _globals['_TICKETS'].methods_by_name['ListTicketTemplate']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListTicketTemplate']._serialized_options = b'\272\270\221\002\n\n\003\010\235\030\n\003\010\234\030\202\323\344\223\0025\"0/api/v1alpha1/tickets/tickets/listtickettemplate:\001*'
  _globals['_TICKETS'].methods_by_name['AssignTicketTemplate']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['AssignTicketTemplate']._serialized_options = b'\272\270\221\002\005\n\003\010\235\030\202\323\344\223\0027\"2/api/v1alpha1/tickets/tickets/assigntickettemplate:\001*'
  _globals['_TICKETS'].methods_by_name['GetAllActionType']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['GetAllActionType']._serialized_options = b'\272\270\221\002\n\n\003\010\235\030\n\003\010\234\030\202\323\344\223\0023\"./api/v1alpha1/tickets/tickets/getallActiontype:\001*'
  _globals['_TICKETS'].methods_by_name['GetPhoneNumberType']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['GetPhoneNumberType']._serialized_options = b'\210\002\001\272\270\221\002\n\n\003\010\235\030\n\003\010\234\030\202\323\344\223\0025\"0/api/v1alpha1/tickets/tickets/getphonenumbertype:\001*'
  _globals['_TICKETS'].methods_by_name['AddEntityRef']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['AddEntityRef']._serialized_options = b'\272\270\221\002\n\n\003\010\235\030\n\003\010\234\030\202\323\344\223\002/\"*/api/v1alpha1/tickets/tickets/addentityref:\001*'
  _globals['_TICKETS'].methods_by_name['ListTicketsByEntityRef']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListTicketsByEntityRef']._serialized_options = b'\272\270\221\002\n\n\003\010\235\030\n\003\010\234\030\202\323\344\223\0029\"4/api/v1alpha1/tickets/tickets/listticketsbyentityref:\001*'
  _globals['_TICKETS'].methods_by_name['ListEntityRefsByTicket']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListEntityRefsByTicket']._serialized_options = b'\272\270\221\002\n\n\003\010\235\030\n\003\010\234\030\202\323\344\223\0029\"4/api/v1alpha1/tickets/tickets/listentityrefsbyticket:\001*'
  _globals['_TICKETS'].methods_by_name['CreateCustomField']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['CreateCustomField']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0024\"//api/v1alpha1/tickets/tickets/createcustomfield:\001*'
  _globals['_TICKETS'].methods_by_name['EditCustomField']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['EditCustomField']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0022\"-/api/v1alpha1/tickets/tickets/editcustomfield:\001*'
  _globals['_TICKETS'].methods_by_name['ListCustomFields']._loaded_options = None
  _globals['_TICKETS'].methods_by_name['ListCustomFields']._serialized_options = b'\272\270\221\002\005\n\003\010\234\030\202\323\344\223\0022\"-/api/v1alpha1/tickets/tickets/listcustomfield:\001*'
  _globals['_TICKETS']._serialized_start=187
  _globals['_TICKETS']._serialized_end=6965
# @@protoc_insertion_point(module_scope)
