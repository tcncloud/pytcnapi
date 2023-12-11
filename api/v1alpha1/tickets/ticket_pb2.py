# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/tickets/ticket.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import tickets_pb2 as api_dot_commons_dot_tickets__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!api/v1alpha1/tickets/ticket.proto\x12\x14\x61pi.v1alpha1.tickets\x1a\x19\x61pi/commons/tickets.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\t\n\x07PingReq\"\t\n\x07PingRes\"\x88\x04\n\x0f\x43reateTicketReq\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12#\n\x0bproject_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\nprojectSid\x12\x35\n\x08\x64ue_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x64ueDate\x12\x31\n\x08metadata\x18\t \x03(\x0b\x32\x15.api.commons.MetadataR\x08metadata\x12\x38\n\rticket_skills\x18\n \x03(\x0b\x32\x13.api.commons.SkillsR\x0cticketSkills\x12\x16\n\x06status\x18\x0b \x01(\x03R\x06status\x12/\n\nticket_sla\x18\x0c \x03(\x0b\x32\x10.api.commons.SlaR\tticketSla\x12\x1f\n\x0b\x61ssign_self\x18\r \x01(\x08R\nassignSelf\x12!\n\x0c\x61ssign_other\x18\x0e \x01(\tR\x0b\x61ssignOther\x12>\n\rticket_action\x18\x0f \x03(\x0b\x32\x19.api.commons.TicketActionR\x0cticketAction\x12\'\n\x0fticket_assignee\x18\x10 \x03(\tR\x0eticketAssignee\"c\n\x1b\x43reateTicketTemplateRequest\x12\x44\n\x0fticket_template\x18\x01 \x01(\x0b\x32\x1b.api.commons.TicketTemplateR\x0eticketTemplate\"d\n\x1c\x43reateTicketTemplateResponse\x12\x44\n\x0fticket_template\x18\x01 \x01(\x0b\x32\x1b.api.commons.TicketTemplateR\x0eticketTemplate\"\xd3\x01\n\x19\x45\x64itTicketTemplateRequest\x12\x30\n\x12ticket_template_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x10ticketTemplateId\x12:\n\nedit_value\x18\x02 \x01(\x0b\x32\x1b.api.commons.TicketTemplateR\teditValue\x12H\n\x12\x65\x64ited_fields_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x10\x65\x64itedFieldsMask\"9\n\x1a\x45\x64itTicketTemplateResponse\x12\x1b\n\tis_edited\x18\x01 \x01(\x08R\x08isEdited\"\x88\x02\n\x19ListTicketTemplateRequest\x12\x30\n\x12ticket_template_id\x18\x01 \x01(\x03\x42\x02\x18\x01R\x10ticketTemplateId\x12!\n\nproject_id\x18\x02 \x01(\x03\x42\x02\x18\x01R\tprojectId\x12=\n\x0crequest_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0brequestMask\x12#\n\x0btemplate_id\x18\x04 \x01(\x03\x42\x02\x30\x01R\ntemplateId\x12\x32\n\x13template_project_id\x18\x05 \x01(\x03\x42\x02\x30\x01R\x11templateProjectId\"\xc4\x01\n\x1aListTicketTemplateResponse\x12J\n\x11\x65nabled_templates\x18\x01 \x03(\x0b\x32\x19.api.commons.ListTemplateB\x02\x18\x01R\x10\x65nabledTemplates\x12Z\n\x17ticket_project_template\x18\x02 \x03(\x0b\x32\".api.commons.TicketProjectTemplateR\x15ticketProjectTemplate\"\xe9\x01\n\x1c\x41ssignProjectTemplateRequest\x12Q\n\x10project_template\x18\x01 \x01(\x0b\x32\".api.commons.AssignProjectTemplateB\x02\x18\x01R\x0fprojectTemplate\x12!\n\nproject_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\tprojectId\x12S\n\x14template_description\x18\x03 \x03(\x0b\x32 .api.commons.TemplateDescriptionR\x13templateDescription\"@\n\x1d\x41ssignProjectTemplateResponse\x12\x1f\n\x0bis_assigned\x18\x01 \x01(\x08R\nisAssigned\">\n\x0f\x43reateTicketRes\x12+\n\x06ticket\x18\x01 \x01(\x0b\x32\x13.api.commons.TicketR\x06ticket\"\x16\n\x14GetActionTypeRequest\"Q\n\x15GetActionTypeResponse\x12\x38\n\x0b\x61\x63tion_type\x18\x01 \x03(\x0b\x32\x17.api.commons.ActionTypeR\nactionType\"q\n\rEditTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x39\n\nedit_value\x18\x02 \x01(\x0b\x32\x1a.api.commons.EditAttributeR\teditValue:\x02\x18\x01\"\xb4\x01\n\x11\x45\x64itMaskTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x32\n\nedit_value\x18\x02 \x01(\x0b\x32\x13.api.commons.TicketR\teditValue\x12H\n\x12\x65\x64ited_fields_mask\x18\x03 \x03(\x0b\x32\x1a.google.protobuf.FieldMaskR\x10\x65\x64itedFieldsMask\"0\n\x11\x45\x64itMaskTicketRes\x12\x1b\n\tis_edited\x18\x01 \x01(\x08R\x08isEdited\"?\n\x16ListAllocatedTicketRes\x12!\n\nticket_sid\x18\x01 \x03(\x03\x42\x02\x30\x01R\tticketSid:\x02\x18\x01\"\x1c\n\x16ListAllocatedTicketReq:\x02\x18\x01\"s\n!ListAvailableAgentTicketsResponse\x12!\n\nticket_sid\x18\x01 \x03(\x03\x42\x02\x30\x01R\tticketSid\x12+\n\x06ticket\x18\x02 \x03(\x0b\x32\x13.api.commons.TicketR\x06ticket\"\"\n ListAvailableAgentTicketsRequest\",\n\rEditTicketRes\x12\x1b\n\tis_edited\x18\x01 \x01(\x08R\x08isEdited\"\x10\n\x0eListTicketsReq\"?\n\x0eListTicketsRes\x12-\n\x07tickets\x18\x01 \x03(\x0b\x32\x13.api.commons.TicketR\x07tickets\"z\n\x0f\x41ssignTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12#\n\rassignee_list\x18\x02 \x01(\tR\x0c\x61ssigneeList\x12\x1f\n\x0b\x61ssigned_id\x18\x03 \x01(\tR\nassignedId\"z\n\x0f\x41ssignTicketRes\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12#\n\rassignee_list\x18\x02 \x01(\tR\x0c\x61ssigneeList\x12\x1f\n\x0b\x61ssigned_id\x18\x03 \x01(\tR\nassignedId\"2\n\rViewTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\"\xae\x01\n\rViewTicketRes\x12+\n\x06ticket\x18\x01 \x01(\x0b\x32\x13.api.commons.TicketR\x06ticket\x12\x30\n\x08\x63omments\x18\x02 \x03(\x0b\x32\x14.api.commons.CommentR\x08\x63omments\x12>\n\rreply_comment\x18\x03 \x03(\x0b\x32\x19.api.commons.ReplyCommentR\x0creplyComment\"O\n\x10\x43reateCommentReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x18\n\x07\x63omment\x18\x02 \x01(\tR\x07\x63omment\"B\n\x10\x43reateCommentRes\x12.\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x14.api.commons.CommentR\x07\x63omment\"r\n\x0e\x43loseTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x18\n\x07\x63omment\x18\x02 \x01(\tR\x07\x63omment\x12#\n\x0b\x66rom_status\x18\x03 \x01(\x03\x42\x02\x30\x01R\nfromStatus\"-\n\x0e\x43loseTicketRes\x12\x1b\n\tis_status\x18\x01 \x01(\x08R\x08isStatus\"\xb0\x01\n\x0c\x43reateSlaReq\x12\x1b\n\x07sla_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x06slaSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08interval\x18\x04 \x01(\x03R\x08interval\x12\x31\n\x08\x64uration\x18\x05 \x01(\x0b\x32\x15.api.commons.DurationR\x08\x64uration\"8\n\x0c\x43reateSlaRes\x12(\n\x03sla\x18\x01 \x01(\x0b\x32\x16.api.commons.TicketSlaR\x03sla\"\x0c\n\nListSlaReq\"D\n\nListSlaRes\x12\x36\n\nticketsSla\x18\x01 \x03(\x0b\x32\x16.api.commons.TicketSlaR\nticketsSla\"H\n\x0cUpdateSlaReq\x12\x1b\n\x07sla_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x06slaSid\x12\x1b\n\tis_active\x18\x02 \x01(\x03R\x08isActive\"F\n\x0cUpdateSlaRes\x12\x36\n\nticketsSla\x18\x01 \x01(\x0b\x32\x16.api.commons.TicketSlaR\nticketsSla\"\x15\n\x13ListSlaConditionReq\"U\n\x13ListSlaConditionRes\x12>\n\x0cslaCondition\x18\x01 \x03(\x0b\x32\x1a.api.commons.SlaConditionsR\x0cslaCondition\"\x93\x01\n\x0fReplyCommentReq\x12#\n\x0b\x63omment_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\ncommentSid\x12!\n\nticket_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x14\n\x05reply\x18\x03 \x01(\tR\x05reply\x12\"\n\rcreated_by_id\x18\x04 \x01(\tR\x0b\x63reatedById\"R\n\x0fReplyCommentRes\x12?\n\nis_created\x18\x01 \x01(\x0b\x32 .api.commons.ConfirmReplyCommentR\tisCreated\"8\n\x13\x43reateSelfAssignReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\"6\n\x13\x43reateSelfAssignRes\x12\x1f\n\x0bis_assigned\x18\x01 \x01(\x08R\nisAssigned\"\x13\n\x11ListSkillsRequest\"I\n\x12ListSkillsResponse\x12\x33\n\x06skills\x18\x01 \x03(\x0b\x32\x1b.api.v1alpha1.tickets.SkillR\x06skills\"6\n\x05Skill\x12\x19\n\x08skill_id\x18\x01 \x01(\tR\x07skillId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\x12\n\x10ListUsersRequest\"E\n\x11ListUsersResponse\x12\x30\n\x05users\x18\x01 \x03(\x0b\x32\x1a.api.v1alpha1.tickets.UserR\x05users\"x\n\x04User\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1d\n\nfirst_name\x18\x02 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x03 \x01(\tR\x08lastName\x12\x1b\n\tis_active\x18\x04 \x01(\x08R\x08isActive\"[\n\x19\x43reateTicketActionRequest\x12>\n\rticket_action\x18\x01 \x01(\x0b\x32\x19.api.commons.TicketActionR\x0cticketAction\"\\\n\x1a\x43reateTicketActionResponse\x12>\n\rticket_action\x18\x01 \x01(\x0b\x32\x19.api.commons.TicketActionR\x0cticketAction\"\x83\x01\n\x18\x43loseTicketActionRequest\x12,\n\x10ticket_action_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0eticketActionId\x12\x1f\n\tticket_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\x08ticketId\x12\x18\n\x07\x63omment\x18\x03 \x01(\tR\x07\x63omment\"8\n\x19\x43loseTicketActionResponse\x12\x1b\n\tis_closed\x18\x01 \x01(\x08R\x08isClosed\"I\n\x19\x41ssignTicketActionRequest\x12,\n\x10ticket_action_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0eticketActionId\"=\n\x1a\x41ssignTicketActionResponse\x12\x1f\n\x0bis_assigned\x18\x01 \x01(\x08R\nisAssigned\"\x9d\x01\n\x19\x43hangeTicketStatusRequest\x12\x1f\n\tticket_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x08ticketId\x12\x1f\n\tstatus_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\x08statusId\x12>\n\rticket_status\x18\x03 \x01(\x0e\x32\x19.api.commons.TicketStatusR\x0cticketStatus\"F\n\x1a\x43hangeTicketStatusResponse\x12(\n\x10is_status_edited\x18\x01 \x01(\x08R\x0eisStatusEditedB\x99\x01\n\x18\x63om.api.v1alpha1.ticketsB\x0bTicketProtoP\x01\xa2\x02\x03\x41VT\xaa\x02\x14\x41pi.V1alpha1.Tickets\xca\x02\x14\x41pi\\V1alpha1\\Tickets\xe2\x02 Api\\V1alpha1\\Tickets\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Ticketsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.tickets.ticket_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.ticketsB\013TicketProtoP\001\242\002\003AVT\252\002\024Api.V1alpha1.Tickets\312\002\024Api\\V1alpha1\\Tickets\342\002 Api\\V1alpha1\\Tickets\\GPBMetadata\352\002\026Api::V1alpha1::Tickets'
  _globals['_CREATETICKETREQ'].fields_by_name['project_sid']._options = None
  _globals['_CREATETICKETREQ'].fields_by_name['project_sid']._serialized_options = b'0\001'
  _globals['_EDITTICKETTEMPLATEREQUEST'].fields_by_name['ticket_template_id']._options = None
  _globals['_EDITTICKETTEMPLATEREQUEST'].fields_by_name['ticket_template_id']._serialized_options = b'0\001'
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['ticket_template_id']._options = None
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['ticket_template_id']._serialized_options = b'\030\001'
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['project_id']._options = None
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['project_id']._serialized_options = b'\030\001'
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['template_id']._options = None
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['template_id']._serialized_options = b'0\001'
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['template_project_id']._options = None
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['template_project_id']._serialized_options = b'0\001'
  _globals['_LISTTICKETTEMPLATERESPONSE'].fields_by_name['enabled_templates']._options = None
  _globals['_LISTTICKETTEMPLATERESPONSE'].fields_by_name['enabled_templates']._serialized_options = b'\030\001'
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST'].fields_by_name['project_template']._options = None
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST'].fields_by_name['project_template']._serialized_options = b'\030\001'
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST'].fields_by_name['project_id']._options = None
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST'].fields_by_name['project_id']._serialized_options = b'0\001'
  _globals['_EDITTICKETREQ'].fields_by_name['ticket_sid']._options = None
  _globals['_EDITTICKETREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_EDITTICKETREQ']._options = None
  _globals['_EDITTICKETREQ']._serialized_options = b'\030\001'
  _globals['_EDITMASKTICKETREQ'].fields_by_name['ticket_sid']._options = None
  _globals['_EDITMASKTICKETREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_LISTALLOCATEDTICKETRES'].fields_by_name['ticket_sid']._options = None
  _globals['_LISTALLOCATEDTICKETRES'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_LISTALLOCATEDTICKETRES']._options = None
  _globals['_LISTALLOCATEDTICKETRES']._serialized_options = b'\030\001'
  _globals['_LISTALLOCATEDTICKETREQ']._options = None
  _globals['_LISTALLOCATEDTICKETREQ']._serialized_options = b'\030\001'
  _globals['_LISTAVAILABLEAGENTTICKETSRESPONSE'].fields_by_name['ticket_sid']._options = None
  _globals['_LISTAVAILABLEAGENTTICKETSRESPONSE'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_ASSIGNTICKETREQ'].fields_by_name['ticket_sid']._options = None
  _globals['_ASSIGNTICKETREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_ASSIGNTICKETRES'].fields_by_name['ticket_sid']._options = None
  _globals['_ASSIGNTICKETRES'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_VIEWTICKETREQ'].fields_by_name['ticket_sid']._options = None
  _globals['_VIEWTICKETREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_CREATECOMMENTREQ'].fields_by_name['ticket_sid']._options = None
  _globals['_CREATECOMMENTREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_CLOSETICKETREQ'].fields_by_name['ticket_sid']._options = None
  _globals['_CLOSETICKETREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_CLOSETICKETREQ'].fields_by_name['from_status']._options = None
  _globals['_CLOSETICKETREQ'].fields_by_name['from_status']._serialized_options = b'0\001'
  _globals['_CREATESLAREQ'].fields_by_name['sla_sid']._options = None
  _globals['_CREATESLAREQ'].fields_by_name['sla_sid']._serialized_options = b'0\001'
  _globals['_UPDATESLAREQ'].fields_by_name['sla_sid']._options = None
  _globals['_UPDATESLAREQ'].fields_by_name['sla_sid']._serialized_options = b'0\001'
  _globals['_REPLYCOMMENTREQ'].fields_by_name['comment_sid']._options = None
  _globals['_REPLYCOMMENTREQ'].fields_by_name['comment_sid']._serialized_options = b'0\001'
  _globals['_REPLYCOMMENTREQ'].fields_by_name['ticket_sid']._options = None
  _globals['_REPLYCOMMENTREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_CREATESELFASSIGNREQ'].fields_by_name['ticket_sid']._options = None
  _globals['_CREATESELFASSIGNREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_CLOSETICKETACTIONREQUEST'].fields_by_name['ticket_action_id']._options = None
  _globals['_CLOSETICKETACTIONREQUEST'].fields_by_name['ticket_action_id']._serialized_options = b'0\001'
  _globals['_CLOSETICKETACTIONREQUEST'].fields_by_name['ticket_id']._options = None
  _globals['_CLOSETICKETACTIONREQUEST'].fields_by_name['ticket_id']._serialized_options = b'0\001'
  _globals['_ASSIGNTICKETACTIONREQUEST'].fields_by_name['ticket_action_id']._options = None
  _globals['_ASSIGNTICKETACTIONREQUEST'].fields_by_name['ticket_action_id']._serialized_options = b'0\001'
  _globals['_CHANGETICKETSTATUSREQUEST'].fields_by_name['ticket_id']._options = None
  _globals['_CHANGETICKETSTATUSREQUEST'].fields_by_name['ticket_id']._serialized_options = b'0\001'
  _globals['_CHANGETICKETSTATUSREQUEST'].fields_by_name['status_id']._options = None
  _globals['_CHANGETICKETSTATUSREQUEST'].fields_by_name['status_id']._serialized_options = b'0\001'
  _globals['_PINGREQ']._serialized_start=153
  _globals['_PINGREQ']._serialized_end=162
  _globals['_PINGRES']._serialized_start=164
  _globals['_PINGRES']._serialized_end=173
  _globals['_CREATETICKETREQ']._serialized_start=176
  _globals['_CREATETICKETREQ']._serialized_end=696
  _globals['_CREATETICKETTEMPLATEREQUEST']._serialized_start=698
  _globals['_CREATETICKETTEMPLATEREQUEST']._serialized_end=797
  _globals['_CREATETICKETTEMPLATERESPONSE']._serialized_start=799
  _globals['_CREATETICKETTEMPLATERESPONSE']._serialized_end=899
  _globals['_EDITTICKETTEMPLATEREQUEST']._serialized_start=902
  _globals['_EDITTICKETTEMPLATEREQUEST']._serialized_end=1113
  _globals['_EDITTICKETTEMPLATERESPONSE']._serialized_start=1115
  _globals['_EDITTICKETTEMPLATERESPONSE']._serialized_end=1172
  _globals['_LISTTICKETTEMPLATEREQUEST']._serialized_start=1175
  _globals['_LISTTICKETTEMPLATEREQUEST']._serialized_end=1439
  _globals['_LISTTICKETTEMPLATERESPONSE']._serialized_start=1442
  _globals['_LISTTICKETTEMPLATERESPONSE']._serialized_end=1638
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST']._serialized_start=1641
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST']._serialized_end=1874
  _globals['_ASSIGNPROJECTTEMPLATERESPONSE']._serialized_start=1876
  _globals['_ASSIGNPROJECTTEMPLATERESPONSE']._serialized_end=1940
  _globals['_CREATETICKETRES']._serialized_start=1942
  _globals['_CREATETICKETRES']._serialized_end=2004
  _globals['_GETACTIONTYPEREQUEST']._serialized_start=2006
  _globals['_GETACTIONTYPEREQUEST']._serialized_end=2028
  _globals['_GETACTIONTYPERESPONSE']._serialized_start=2030
  _globals['_GETACTIONTYPERESPONSE']._serialized_end=2111
  _globals['_EDITTICKETREQ']._serialized_start=2113
  _globals['_EDITTICKETREQ']._serialized_end=2226
  _globals['_EDITMASKTICKETREQ']._serialized_start=2229
  _globals['_EDITMASKTICKETREQ']._serialized_end=2409
  _globals['_EDITMASKTICKETRES']._serialized_start=2411
  _globals['_EDITMASKTICKETRES']._serialized_end=2459
  _globals['_LISTALLOCATEDTICKETRES']._serialized_start=2461
  _globals['_LISTALLOCATEDTICKETRES']._serialized_end=2524
  _globals['_LISTALLOCATEDTICKETREQ']._serialized_start=2526
  _globals['_LISTALLOCATEDTICKETREQ']._serialized_end=2554
  _globals['_LISTAVAILABLEAGENTTICKETSRESPONSE']._serialized_start=2556
  _globals['_LISTAVAILABLEAGENTTICKETSRESPONSE']._serialized_end=2671
  _globals['_LISTAVAILABLEAGENTTICKETSREQUEST']._serialized_start=2673
  _globals['_LISTAVAILABLEAGENTTICKETSREQUEST']._serialized_end=2707
  _globals['_EDITTICKETRES']._serialized_start=2709
  _globals['_EDITTICKETRES']._serialized_end=2753
  _globals['_LISTTICKETSREQ']._serialized_start=2755
  _globals['_LISTTICKETSREQ']._serialized_end=2771
  _globals['_LISTTICKETSRES']._serialized_start=2773
  _globals['_LISTTICKETSRES']._serialized_end=2836
  _globals['_ASSIGNTICKETREQ']._serialized_start=2838
  _globals['_ASSIGNTICKETREQ']._serialized_end=2960
  _globals['_ASSIGNTICKETRES']._serialized_start=2962
  _globals['_ASSIGNTICKETRES']._serialized_end=3084
  _globals['_VIEWTICKETREQ']._serialized_start=3086
  _globals['_VIEWTICKETREQ']._serialized_end=3136
  _globals['_VIEWTICKETRES']._serialized_start=3139
  _globals['_VIEWTICKETRES']._serialized_end=3313
  _globals['_CREATECOMMENTREQ']._serialized_start=3315
  _globals['_CREATECOMMENTREQ']._serialized_end=3394
  _globals['_CREATECOMMENTRES']._serialized_start=3396
  _globals['_CREATECOMMENTRES']._serialized_end=3462
  _globals['_CLOSETICKETREQ']._serialized_start=3464
  _globals['_CLOSETICKETREQ']._serialized_end=3578
  _globals['_CLOSETICKETRES']._serialized_start=3580
  _globals['_CLOSETICKETRES']._serialized_end=3625
  _globals['_CREATESLAREQ']._serialized_start=3628
  _globals['_CREATESLAREQ']._serialized_end=3804
  _globals['_CREATESLARES']._serialized_start=3806
  _globals['_CREATESLARES']._serialized_end=3862
  _globals['_LISTSLAREQ']._serialized_start=3864
  _globals['_LISTSLAREQ']._serialized_end=3876
  _globals['_LISTSLARES']._serialized_start=3878
  _globals['_LISTSLARES']._serialized_end=3946
  _globals['_UPDATESLAREQ']._serialized_start=3948
  _globals['_UPDATESLAREQ']._serialized_end=4020
  _globals['_UPDATESLARES']._serialized_start=4022
  _globals['_UPDATESLARES']._serialized_end=4092
  _globals['_LISTSLACONDITIONREQ']._serialized_start=4094
  _globals['_LISTSLACONDITIONREQ']._serialized_end=4115
  _globals['_LISTSLACONDITIONRES']._serialized_start=4117
  _globals['_LISTSLACONDITIONRES']._serialized_end=4202
  _globals['_REPLYCOMMENTREQ']._serialized_start=4205
  _globals['_REPLYCOMMENTREQ']._serialized_end=4352
  _globals['_REPLYCOMMENTRES']._serialized_start=4354
  _globals['_REPLYCOMMENTRES']._serialized_end=4436
  _globals['_CREATESELFASSIGNREQ']._serialized_start=4438
  _globals['_CREATESELFASSIGNREQ']._serialized_end=4494
  _globals['_CREATESELFASSIGNRES']._serialized_start=4496
  _globals['_CREATESELFASSIGNRES']._serialized_end=4550
  _globals['_LISTSKILLSREQUEST']._serialized_start=4552
  _globals['_LISTSKILLSREQUEST']._serialized_end=4571
  _globals['_LISTSKILLSRESPONSE']._serialized_start=4573
  _globals['_LISTSKILLSRESPONSE']._serialized_end=4646
  _globals['_SKILL']._serialized_start=4648
  _globals['_SKILL']._serialized_end=4702
  _globals['_LISTUSERSREQUEST']._serialized_start=4704
  _globals['_LISTUSERSREQUEST']._serialized_end=4722
  _globals['_LISTUSERSRESPONSE']._serialized_start=4724
  _globals['_LISTUSERSRESPONSE']._serialized_end=4793
  _globals['_USER']._serialized_start=4795
  _globals['_USER']._serialized_end=4915
  _globals['_CREATETICKETACTIONREQUEST']._serialized_start=4917
  _globals['_CREATETICKETACTIONREQUEST']._serialized_end=5008
  _globals['_CREATETICKETACTIONRESPONSE']._serialized_start=5010
  _globals['_CREATETICKETACTIONRESPONSE']._serialized_end=5102
  _globals['_CLOSETICKETACTIONREQUEST']._serialized_start=5105
  _globals['_CLOSETICKETACTIONREQUEST']._serialized_end=5236
  _globals['_CLOSETICKETACTIONRESPONSE']._serialized_start=5238
  _globals['_CLOSETICKETACTIONRESPONSE']._serialized_end=5294
  _globals['_ASSIGNTICKETACTIONREQUEST']._serialized_start=5296
  _globals['_ASSIGNTICKETACTIONREQUEST']._serialized_end=5369
  _globals['_ASSIGNTICKETACTIONRESPONSE']._serialized_start=5371
  _globals['_ASSIGNTICKETACTIONRESPONSE']._serialized_end=5432
  _globals['_CHANGETICKETSTATUSREQUEST']._serialized_start=5435
  _globals['_CHANGETICKETSTATUSREQUEST']._serialized_end=5592
  _globals['_CHANGETICKETSTATUSRESPONSE']._serialized_start=5594
  _globals['_CHANGETICKETSTATUSRESPONSE']._serialized_end=5664
# @@protoc_insertion_point(module_scope)
