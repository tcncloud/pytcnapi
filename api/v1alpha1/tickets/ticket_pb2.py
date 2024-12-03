# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/tickets/ticket.proto
# Protobuf Python Version: 5.29.0
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
    0,
    '',
    'api/v1alpha1/tickets/ticket.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import tickets_pb2 as api_dot_commons_dot_tickets__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!api/v1alpha1/tickets/ticket.proto\x12\x14\x61pi.v1alpha1.tickets\x1a\x19\x61pi/commons/tickets.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\t\n\x07PingReq\"\t\n\x07PingRes\"\xbe\x04\n\x0f\x43reateTicketReq\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12#\n\x0bproject_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\nprojectSid\x12\x35\n\x08\x64ue_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x64ueDate\x12\x31\n\x08metadata\x18\t \x03(\x0b\x32\x15.api.commons.MetadataR\x08metadata\x12<\n\rticket_skills\x18\n \x03(\x0b\x32\x13.api.commons.SkillsB\x02\x18\x01R\x0cticketSkills\x12\x16\n\x06status\x18\x0b \x01(\x03R\x06status\x12/\n\nticket_sla\x18\x0c \x03(\x0b\x32\x10.api.commons.SlaR\tticketSla\x12\x1f\n\x0b\x61ssign_self\x18\r \x01(\x08R\nassignSelf\x12%\n\x0c\x61ssign_other\x18\x0e \x01(\tB\x02\x18\x01R\x0b\x61ssignOther\x12>\n\rticket_action\x18\x0f \x03(\x0b\x32\x19.api.commons.TicketActionR\x0cticketAction\x12\'\n\x0fticket_assignee\x18\x10 \x03(\tR\x0eticketAssignee\x12,\n\x10\x63ontact_entry_id\x18\x11 \x01(\x03\x42\x02\x30\x01R\x0e\x63ontactEntryId\"c\n\x1b\x43reateTicketTemplateRequest\x12\x44\n\x0fticket_template\x18\x01 \x01(\x0b\x32\x1b.api.commons.TicketTemplateR\x0eticketTemplate\"d\n\x1c\x43reateTicketTemplateResponse\x12\x44\n\x0fticket_template\x18\x01 \x01(\x0b\x32\x1b.api.commons.TicketTemplateR\x0eticketTemplate\"\xd3\x01\n\x19\x45\x64itTicketTemplateRequest\x12\x30\n\x12ticket_template_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x10ticketTemplateId\x12:\n\nedit_value\x18\x02 \x01(\x0b\x32\x1b.api.commons.TicketTemplateR\teditValue\x12H\n\x12\x65\x64ited_fields_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x10\x65\x64itedFieldsMask\"=\n\x1a\x45\x64itTicketTemplateResponse\x12\x1f\n\tis_edited\x18\x01 \x01(\x08\x42\x02\x18\x01R\x08isEdited\"\x88\x02\n\x19ListTicketTemplateRequest\x12\x30\n\x12ticket_template_id\x18\x01 \x01(\x03\x42\x02\x18\x01R\x10ticketTemplateId\x12!\n\nproject_id\x18\x02 \x01(\x03\x42\x02\x18\x01R\tprojectId\x12=\n\x0crequest_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0brequestMask\x12#\n\x0btemplate_id\x18\x04 \x01(\x03\x42\x02\x30\x01R\ntemplateId\x12\x32\n\x13template_project_id\x18\x05 \x01(\x03\x42\x02\x30\x01R\x11templateProjectId\"\xc4\x01\n\x1aListTicketTemplateResponse\x12J\n\x11\x65nabled_templates\x18\x01 \x03(\x0b\x32\x19.api.commons.ListTemplateB\x02\x18\x01R\x10\x65nabledTemplates\x12Z\n\x17ticket_project_template\x18\x02 \x03(\x0b\x32\".api.commons.TicketProjectTemplateR\x15ticketProjectTemplate\"\xe9\x01\n\x1c\x41ssignProjectTemplateRequest\x12Q\n\x10project_template\x18\x01 \x01(\x0b\x32\".api.commons.AssignProjectTemplateB\x02\x18\x01R\x0fprojectTemplate\x12!\n\nproject_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\tprojectId\x12S\n\x14template_description\x18\x03 \x03(\x0b\x32 .api.commons.TemplateDescriptionR\x13templateDescription\"D\n\x1d\x41ssignProjectTemplateResponse\x12#\n\x0bis_assigned\x18\x01 \x01(\x08\x42\x02\x18\x01R\nisAssigned\">\n\x0f\x43reateTicketRes\x12+\n\x06ticket\x18\x01 \x01(\x0b\x32\x13.api.commons.TicketR\x06ticket\"\x16\n\x14GetActionTypeRequest\"Q\n\x15GetActionTypeResponse\x12\x38\n\x0b\x61\x63tion_type\x18\x01 \x03(\x0b\x32\x17.api.commons.ActionTypeR\nactionType\"B\n\x19GetPhoneNumberTypeRequest\x12!\n\x0cphone_number\x18\x01 \x01(\tR\x0bphoneNumber:\x02\x18\x01\"]\n\x1aGetPhoneNumberTypeResponse\x12;\n\nphone_type\x18\x01 \x01(\x0e\x32\x1c.api.commons.PhoneNumberTypeR\tphoneType:\x02\x18\x01\"q\n\rEditTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x39\n\nedit_value\x18\x02 \x01(\x0b\x32\x1a.api.commons.EditAttributeR\teditValue:\x02\x18\x01\"\x85\x02\n\x11\x45\x64itMaskTicketReq\x12#\n\nticket_sid\x18\x01 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12\x32\n\nedit_value\x18\x02 \x01(\x0b\x32\x13.api.commons.TicketR\teditValue\x12H\n\x12\x65\x64ited_fields_mask\x18\x03 \x03(\x0b\x32\x1a.google.protobuf.FieldMaskR\x10\x65\x64itedFieldsMask\x12\x1f\n\x0bticket_code\x18\x04 \x01(\tR\nticketCode\x12,\n\x10\x63ontact_entry_id\x18\x05 \x01(\x03\x42\x02\x30\x01R\x0e\x63ontactEntryId\"4\n\x11\x45\x64itMaskTicketRes\x12\x1f\n\tis_edited\x18\x01 \x01(\x08\x42\x02\x18\x01R\x08isEdited\"?\n\x16ListAllocatedTicketRes\x12!\n\nticket_sid\x18\x01 \x03(\x03\x42\x02\x30\x01R\tticketSid:\x02\x18\x01\"\x1c\n\x16ListAllocatedTicketReq:\x02\x18\x01\"G\n\x18ListAgentTicketsResponse\x12+\n\x06ticket\x18\x01 \x03(\x0b\x32\x13.api.commons.TicketR\x06ticket\"\x9e\x01\n\x17ListAgentTicketsRequest\x12\x46\n\x11select_field_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0fselectFieldMask\x12;\n\x0b\x66ilter_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nfilterMask\"u\n!ListAvailableAgentTicketsResponse\x12#\n\nticket_sid\x18\x01 \x03(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12+\n\x06ticket\x18\x02 \x03(\x0b\x32\x13.api.commons.TicketR\x06ticket\"\xed\x01\n ListAvailableAgentTicketsRequest\x12\x46\n\x11select_field_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0fselectFieldMask\x12W\n\x10\x61vailable_filter\x18\x02 \x01(\x0b\x32,.api.v1alpha1.tickets.AvailableTicketsFilterR\x0f\x61vailableFilter\x12(\n\x10\x61gent_view_limit\x18\x03 \x01(\x03R\x0e\x61gentViewLimit\">\n\x16\x41vailableTicketsFilter\x12$\n\x0e\x61gent_skill_id\x18\x01 \x03(\tR\x0c\x61gentSkillId\"0\n\rEditTicketRes\x12\x1b\n\tis_edited\x18\x01 \x01(\x08R\x08isEdited:\x02\x18\x01\"\x10\n\x0eListTicketsReq\"?\n\x0eListTicketsRes\x12-\n\x07tickets\x18\x01 \x03(\x0b\x32\x13.api.commons.TicketR\x07tickets\"~\n\x0f\x41ssignTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12#\n\rassignee_list\x18\x02 \x01(\tR\x0c\x61ssigneeList\x12\x1f\n\x0b\x61ssigned_id\x18\x03 \x01(\tR\nassignedId:\x02\x18\x01\"~\n\x0f\x41ssignTicketRes\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12#\n\rassignee_list\x18\x02 \x01(\tR\x0c\x61ssigneeList\x12\x1f\n\x0b\x61ssigned_id\x18\x03 \x01(\tR\nassignedId:\x02\x18\x01\"U\n\rViewTicketReq\x12#\n\nticket_sid\x18\x01 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12\x1f\n\x0bticket_code\x18\x02 \x01(\tR\nticketCode\"\xae\x01\n\rViewTicketRes\x12+\n\x06ticket\x18\x01 \x01(\x0b\x32\x13.api.commons.TicketR\x06ticket\x12\x30\n\x08\x63omments\x18\x02 \x03(\x0b\x32\x14.api.commons.CommentR\x08\x63omments\x12>\n\rreply_comment\x18\x03 \x03(\x0b\x32\x19.api.commons.ReplyCommentR\x0creplyComment\"r\n\x10\x43reateCommentReq\x12#\n\nticket_sid\x18\x01 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12\x18\n\x07\x63omment\x18\x02 \x01(\tR\x07\x63omment\x12\x1f\n\x0bticket_code\x18\x03 \x01(\tR\nticketCode\"B\n\x10\x43reateCommentRes\x12.\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x14.api.commons.CommentR\x07\x63omment\"\x97\x01\n\x0e\x43loseTicketReq\x12#\n\nticket_sid\x18\x01 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12\x18\n\x07\x63omment\x18\x02 \x01(\tR\x07\x63omment\x12%\n\x0b\x66rom_status\x18\x03 \x01(\x03\x42\x04\x18\x01\x30\x01R\nfromStatus\x12\x1f\n\x0bticket_code\x18\x04 \x01(\tR\nticketCode\"1\n\x0e\x43loseTicketRes\x12\x1f\n\tis_status\x18\x01 \x01(\x08\x42\x02\x18\x01R\x08isStatus\"\xb4\x01\n\x0c\x43reateSlaReq\x12\x1b\n\x07sla_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x06slaSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1e\n\x08interval\x18\x04 \x01(\x03\x42\x02\x18\x01R\x08interval\x12\x31\n\x08\x64uration\x18\x05 \x01(\x0b\x32\x15.api.commons.DurationR\x08\x64uration\"8\n\x0c\x43reateSlaRes\x12(\n\x03sla\x18\x01 \x01(\x0b\x32\x16.api.commons.TicketSlaR\x03sla\"\x0c\n\nListSlaReq\"D\n\nListSlaRes\x12\x36\n\nticketsSla\x18\x01 \x03(\x0b\x32\x16.api.commons.TicketSlaR\nticketsSla\"H\n\x0cUpdateSlaReq\x12\x1b\n\x07sla_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x06slaSid\x12\x1b\n\tis_active\x18\x02 \x01(\x03R\x08isActive\"F\n\x0cUpdateSlaRes\x12\x36\n\nticketsSla\x18\x01 \x01(\x0b\x32\x16.api.commons.TicketSlaR\nticketsSla\"\x15\n\x13ListSlaConditionReq\"U\n\x13ListSlaConditionRes\x12>\n\x0cslaCondition\x18\x01 \x03(\x0b\x32\x1a.api.commons.SlaConditionsR\x0cslaCondition\"\xb6\x01\n\x0fReplyCommentReq\x12#\n\x0b\x63omment_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\ncommentSid\x12#\n\nticket_sid\x18\x02 \x01(\x03\x42\x04\x18\x01\x30\x01R\tticketSid\x12\x14\n\x05reply\x18\x03 \x01(\tR\x05reply\x12\"\n\rcreated_by_id\x18\x04 \x01(\tR\x0b\x63reatedById\x12\x1f\n\x0bticket_code\x18\x05 \x01(\tR\nticketCode\"R\n\x0fReplyCommentRes\x12?\n\nis_created\x18\x01 \x01(\x0b\x32 .api.commons.ConfirmReplyCommentR\tisCreated\"<\n\x13\x43reateSelfAssignReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid:\x02\x18\x01\":\n\x13\x43reateSelfAssignRes\x12\x1f\n\x0bis_assigned\x18\x01 \x01(\x08R\nisAssigned:\x02\x18\x01\"\x13\n\x11ListSkillsRequest\"I\n\x12ListSkillsResponse\x12\x33\n\x06skills\x18\x01 \x03(\x0b\x32\x1b.api.v1alpha1.tickets.SkillR\x06skills\"6\n\x05Skill\x12\x19\n\x08skill_id\x18\x01 \x01(\tR\x07skillId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\x12\n\x10ListUsersRequest\"E\n\x11ListUsersResponse\x12\x30\n\x05users\x18\x01 \x03(\x0b\x32\x1a.api.v1alpha1.tickets.UserR\x05users\"x\n\x04User\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1d\n\nfirst_name\x18\x02 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x03 \x01(\tR\x08lastName\x12\x1b\n\tis_active\x18\x04 \x01(\x08R\x08isActive\"[\n\x19\x43reateTicketActionRequest\x12>\n\rticket_action\x18\x01 \x01(\x0b\x32\x19.api.commons.TicketActionR\x0cticketAction\"\\\n\x1a\x43reateTicketActionResponse\x12>\n\rticket_action\x18\x01 \x01(\x0b\x32\x19.api.commons.TicketActionR\x0cticketAction\"\xaa\x01\n\x18\x43loseTicketActionRequest\x12,\n\x10ticket_action_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0eticketActionId\x12!\n\tticket_id\x18\x02 \x01(\x03\x42\x04\x18\x01\x30\x01R\x08ticketId\x12\x1c\n\x07\x63omment\x18\x03 \x01(\tB\x02\x18\x01R\x07\x63omment\x12\x1f\n\x0bticket_code\x18\x04 \x01(\tR\nticketCode\"<\n\x19\x43loseTicketActionResponse\x12\x1f\n\tis_closed\x18\x01 \x01(\x08\x42\x02\x18\x01R\x08isClosed\"M\n\x19\x41ssignTicketActionRequest\x12,\n\x10ticket_action_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0eticketActionId:\x02\x18\x01\"A\n\x1a\x41ssignTicketActionResponse\x12\x1f\n\x0bis_assigned\x18\x01 \x01(\x08R\nisAssigned:\x02\x18\x01\"\xa1\x01\n\x19\x43hangeTicketStatusRequest\x12\x1f\n\tticket_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x08ticketId\x12\x1f\n\tstatus_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\x08statusId\x12>\n\rticket_status\x18\x03 \x01(\x0e\x32\x19.api.commons.TicketStatusR\x0cticketStatus:\x02\x18\x01\"J\n\x1a\x43hangeTicketStatusResponse\x12(\n\x10is_status_edited\x18\x01 \x01(\x08R\x0eisStatusEdited:\x02\x18\x01\"U\n\x13\x41\x64\x64\x45ntityRefRequest\x12>\n\nentity_ref\x18\x01 \x01(\x0b\x32\x1f.api.v1alpha1.tickets.EntityRefR\tentityRef\"\x16\n\x14\x41\x64\x64\x45ntityRefResponse\"@\n\x1dListEntityRefsByTicketRequest\x12\x1f\n\x0bticket_code\x18\x01 \x01(\tR\nticketCode\"`\n\x1eListEntityRefsByTicketResponse\x12>\n\nentity_ref\x18\x01 \x03(\x0b\x32\x1f.api.v1alpha1.tickets.EntityRefR\tentityRef\"1\n\x1dListTicketsByEntityRefRequest\x12\x10\n\x03uri\x18\x01 \x01(\tR\x03uri\"O\n\x1eListTicketsByEntityRefResponse\x12-\n\x07tickets\x18\x01 \x03(\x0b\x32\x13.api.commons.TicketR\x07tickets\"r\n\tEntityRef\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1b\n\tregion_id\x18\x02 \x01(\tR\x08regionId\x12\x1f\n\x0bticket_code\x18\x03 \x01(\tR\nticketCode\x12\x10\n\x03uri\x18\x04 \x01(\tR\x03uri*?\n\x0b\x41\x63tionTypes\x12\x06\n\x02NA\x10\x00\x12\x0c\n\x08\x43\x61llback\x10\x01\x12\r\n\tEmailback\x10\x02\x12\x0b\n\x07Smsback\x10\x03*3\n\rSLAConditions\x12\x08\n\x04None\x10\x00\x12\x0b\n\x07Respond\x10\x01\x12\x0b\n\x07Resolve\x10\x02\x42\x99\x01\n\x18\x63om.api.v1alpha1.ticketsB\x0bTicketProtoP\x01\xa2\x02\x03\x41VT\xaa\x02\x14\x41pi.V1alpha1.Tickets\xca\x02\x14\x41pi\\V1alpha1\\Tickets\xe2\x02 Api\\V1alpha1\\Tickets\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Ticketsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.tickets.ticket_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030com.api.v1alpha1.ticketsB\013TicketProtoP\001\242\002\003AVT\252\002\024Api.V1alpha1.Tickets\312\002\024Api\\V1alpha1\\Tickets\342\002 Api\\V1alpha1\\Tickets\\GPBMetadata\352\002\026Api::V1alpha1::Tickets'
  _globals['_CREATETICKETREQ'].fields_by_name['project_sid']._loaded_options = None
  _globals['_CREATETICKETREQ'].fields_by_name['project_sid']._serialized_options = b'0\001'
  _globals['_CREATETICKETREQ'].fields_by_name['ticket_skills']._loaded_options = None
  _globals['_CREATETICKETREQ'].fields_by_name['ticket_skills']._serialized_options = b'\030\001'
  _globals['_CREATETICKETREQ'].fields_by_name['assign_other']._loaded_options = None
  _globals['_CREATETICKETREQ'].fields_by_name['assign_other']._serialized_options = b'\030\001'
  _globals['_CREATETICKETREQ'].fields_by_name['contact_entry_id']._loaded_options = None
  _globals['_CREATETICKETREQ'].fields_by_name['contact_entry_id']._serialized_options = b'0\001'
  _globals['_EDITTICKETTEMPLATEREQUEST'].fields_by_name['ticket_template_id']._loaded_options = None
  _globals['_EDITTICKETTEMPLATEREQUEST'].fields_by_name['ticket_template_id']._serialized_options = b'0\001'
  _globals['_EDITTICKETTEMPLATERESPONSE'].fields_by_name['is_edited']._loaded_options = None
  _globals['_EDITTICKETTEMPLATERESPONSE'].fields_by_name['is_edited']._serialized_options = b'\030\001'
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['ticket_template_id']._loaded_options = None
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['ticket_template_id']._serialized_options = b'\030\001'
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['project_id']._loaded_options = None
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['project_id']._serialized_options = b'\030\001'
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['template_id']._loaded_options = None
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['template_id']._serialized_options = b'0\001'
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['template_project_id']._loaded_options = None
  _globals['_LISTTICKETTEMPLATEREQUEST'].fields_by_name['template_project_id']._serialized_options = b'0\001'
  _globals['_LISTTICKETTEMPLATERESPONSE'].fields_by_name['enabled_templates']._loaded_options = None
  _globals['_LISTTICKETTEMPLATERESPONSE'].fields_by_name['enabled_templates']._serialized_options = b'\030\001'
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST'].fields_by_name['project_template']._loaded_options = None
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST'].fields_by_name['project_template']._serialized_options = b'\030\001'
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST'].fields_by_name['project_id']._loaded_options = None
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST'].fields_by_name['project_id']._serialized_options = b'0\001'
  _globals['_ASSIGNPROJECTTEMPLATERESPONSE'].fields_by_name['is_assigned']._loaded_options = None
  _globals['_ASSIGNPROJECTTEMPLATERESPONSE'].fields_by_name['is_assigned']._serialized_options = b'\030\001'
  _globals['_GETPHONENUMBERTYPEREQUEST']._loaded_options = None
  _globals['_GETPHONENUMBERTYPEREQUEST']._serialized_options = b'\030\001'
  _globals['_GETPHONENUMBERTYPERESPONSE']._loaded_options = None
  _globals['_GETPHONENUMBERTYPERESPONSE']._serialized_options = b'\030\001'
  _globals['_EDITTICKETREQ'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_EDITTICKETREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_EDITTICKETREQ']._loaded_options = None
  _globals['_EDITTICKETREQ']._serialized_options = b'\030\001'
  _globals['_EDITMASKTICKETREQ'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_EDITMASKTICKETREQ'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_EDITMASKTICKETREQ'].fields_by_name['contact_entry_id']._loaded_options = None
  _globals['_EDITMASKTICKETREQ'].fields_by_name['contact_entry_id']._serialized_options = b'0\001'
  _globals['_EDITMASKTICKETRES'].fields_by_name['is_edited']._loaded_options = None
  _globals['_EDITMASKTICKETRES'].fields_by_name['is_edited']._serialized_options = b'\030\001'
  _globals['_LISTALLOCATEDTICKETRES'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_LISTALLOCATEDTICKETRES'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_LISTALLOCATEDTICKETRES']._loaded_options = None
  _globals['_LISTALLOCATEDTICKETRES']._serialized_options = b'\030\001'
  _globals['_LISTALLOCATEDTICKETREQ']._loaded_options = None
  _globals['_LISTALLOCATEDTICKETREQ']._serialized_options = b'\030\001'
  _globals['_LISTAVAILABLEAGENTTICKETSRESPONSE'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_LISTAVAILABLEAGENTTICKETSRESPONSE'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_EDITTICKETRES']._loaded_options = None
  _globals['_EDITTICKETRES']._serialized_options = b'\030\001'
  _globals['_ASSIGNTICKETREQ'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_ASSIGNTICKETREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_ASSIGNTICKETREQ']._loaded_options = None
  _globals['_ASSIGNTICKETREQ']._serialized_options = b'\030\001'
  _globals['_ASSIGNTICKETRES'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_ASSIGNTICKETRES'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_ASSIGNTICKETRES']._loaded_options = None
  _globals['_ASSIGNTICKETRES']._serialized_options = b'\030\001'
  _globals['_VIEWTICKETREQ'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_VIEWTICKETREQ'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_CREATECOMMENTREQ'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_CREATECOMMENTREQ'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_CLOSETICKETREQ'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_CLOSETICKETREQ'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_CLOSETICKETREQ'].fields_by_name['from_status']._loaded_options = None
  _globals['_CLOSETICKETREQ'].fields_by_name['from_status']._serialized_options = b'\030\0010\001'
  _globals['_CLOSETICKETRES'].fields_by_name['is_status']._loaded_options = None
  _globals['_CLOSETICKETRES'].fields_by_name['is_status']._serialized_options = b'\030\001'
  _globals['_CREATESLAREQ'].fields_by_name['sla_sid']._loaded_options = None
  _globals['_CREATESLAREQ'].fields_by_name['sla_sid']._serialized_options = b'0\001'
  _globals['_CREATESLAREQ'].fields_by_name['interval']._loaded_options = None
  _globals['_CREATESLAREQ'].fields_by_name['interval']._serialized_options = b'\030\001'
  _globals['_UPDATESLAREQ'].fields_by_name['sla_sid']._loaded_options = None
  _globals['_UPDATESLAREQ'].fields_by_name['sla_sid']._serialized_options = b'0\001'
  _globals['_REPLYCOMMENTREQ'].fields_by_name['comment_sid']._loaded_options = None
  _globals['_REPLYCOMMENTREQ'].fields_by_name['comment_sid']._serialized_options = b'0\001'
  _globals['_REPLYCOMMENTREQ'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_REPLYCOMMENTREQ'].fields_by_name['ticket_sid']._serialized_options = b'\030\0010\001'
  _globals['_CREATESELFASSIGNREQ'].fields_by_name['ticket_sid']._loaded_options = None
  _globals['_CREATESELFASSIGNREQ'].fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_CREATESELFASSIGNREQ']._loaded_options = None
  _globals['_CREATESELFASSIGNREQ']._serialized_options = b'\030\001'
  _globals['_CREATESELFASSIGNRES']._loaded_options = None
  _globals['_CREATESELFASSIGNRES']._serialized_options = b'\030\001'
  _globals['_CLOSETICKETACTIONREQUEST'].fields_by_name['ticket_action_id']._loaded_options = None
  _globals['_CLOSETICKETACTIONREQUEST'].fields_by_name['ticket_action_id']._serialized_options = b'0\001'
  _globals['_CLOSETICKETACTIONREQUEST'].fields_by_name['ticket_id']._loaded_options = None
  _globals['_CLOSETICKETACTIONREQUEST'].fields_by_name['ticket_id']._serialized_options = b'\030\0010\001'
  _globals['_CLOSETICKETACTIONREQUEST'].fields_by_name['comment']._loaded_options = None
  _globals['_CLOSETICKETACTIONREQUEST'].fields_by_name['comment']._serialized_options = b'\030\001'
  _globals['_CLOSETICKETACTIONRESPONSE'].fields_by_name['is_closed']._loaded_options = None
  _globals['_CLOSETICKETACTIONRESPONSE'].fields_by_name['is_closed']._serialized_options = b'\030\001'
  _globals['_ASSIGNTICKETACTIONREQUEST'].fields_by_name['ticket_action_id']._loaded_options = None
  _globals['_ASSIGNTICKETACTIONREQUEST'].fields_by_name['ticket_action_id']._serialized_options = b'0\001'
  _globals['_ASSIGNTICKETACTIONREQUEST']._loaded_options = None
  _globals['_ASSIGNTICKETACTIONREQUEST']._serialized_options = b'\030\001'
  _globals['_ASSIGNTICKETACTIONRESPONSE']._loaded_options = None
  _globals['_ASSIGNTICKETACTIONRESPONSE']._serialized_options = b'\030\001'
  _globals['_CHANGETICKETSTATUSREQUEST'].fields_by_name['ticket_id']._loaded_options = None
  _globals['_CHANGETICKETSTATUSREQUEST'].fields_by_name['ticket_id']._serialized_options = b'0\001'
  _globals['_CHANGETICKETSTATUSREQUEST'].fields_by_name['status_id']._loaded_options = None
  _globals['_CHANGETICKETSTATUSREQUEST'].fields_by_name['status_id']._serialized_options = b'0\001'
  _globals['_CHANGETICKETSTATUSREQUEST']._loaded_options = None
  _globals['_CHANGETICKETSTATUSREQUEST']._serialized_options = b'\030\001'
  _globals['_CHANGETICKETSTATUSRESPONSE']._loaded_options = None
  _globals['_CHANGETICKETSTATUSRESPONSE']._serialized_options = b'\030\001'
  _globals['_ACTIONTYPES']._serialized_start=7233
  _globals['_ACTIONTYPES']._serialized_end=7296
  _globals['_SLACONDITIONS']._serialized_start=7298
  _globals['_SLACONDITIONS']._serialized_end=7349
  _globals['_PINGREQ']._serialized_start=153
  _globals['_PINGREQ']._serialized_end=162
  _globals['_PINGRES']._serialized_start=164
  _globals['_PINGRES']._serialized_end=173
  _globals['_CREATETICKETREQ']._serialized_start=176
  _globals['_CREATETICKETREQ']._serialized_end=750
  _globals['_CREATETICKETTEMPLATEREQUEST']._serialized_start=752
  _globals['_CREATETICKETTEMPLATEREQUEST']._serialized_end=851
  _globals['_CREATETICKETTEMPLATERESPONSE']._serialized_start=853
  _globals['_CREATETICKETTEMPLATERESPONSE']._serialized_end=953
  _globals['_EDITTICKETTEMPLATEREQUEST']._serialized_start=956
  _globals['_EDITTICKETTEMPLATEREQUEST']._serialized_end=1167
  _globals['_EDITTICKETTEMPLATERESPONSE']._serialized_start=1169
  _globals['_EDITTICKETTEMPLATERESPONSE']._serialized_end=1230
  _globals['_LISTTICKETTEMPLATEREQUEST']._serialized_start=1233
  _globals['_LISTTICKETTEMPLATEREQUEST']._serialized_end=1497
  _globals['_LISTTICKETTEMPLATERESPONSE']._serialized_start=1500
  _globals['_LISTTICKETTEMPLATERESPONSE']._serialized_end=1696
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST']._serialized_start=1699
  _globals['_ASSIGNPROJECTTEMPLATEREQUEST']._serialized_end=1932
  _globals['_ASSIGNPROJECTTEMPLATERESPONSE']._serialized_start=1934
  _globals['_ASSIGNPROJECTTEMPLATERESPONSE']._serialized_end=2002
  _globals['_CREATETICKETRES']._serialized_start=2004
  _globals['_CREATETICKETRES']._serialized_end=2066
  _globals['_GETACTIONTYPEREQUEST']._serialized_start=2068
  _globals['_GETACTIONTYPEREQUEST']._serialized_end=2090
  _globals['_GETACTIONTYPERESPONSE']._serialized_start=2092
  _globals['_GETACTIONTYPERESPONSE']._serialized_end=2173
  _globals['_GETPHONENUMBERTYPEREQUEST']._serialized_start=2175
  _globals['_GETPHONENUMBERTYPEREQUEST']._serialized_end=2241
  _globals['_GETPHONENUMBERTYPERESPONSE']._serialized_start=2243
  _globals['_GETPHONENUMBERTYPERESPONSE']._serialized_end=2336
  _globals['_EDITTICKETREQ']._serialized_start=2338
  _globals['_EDITTICKETREQ']._serialized_end=2451
  _globals['_EDITMASKTICKETREQ']._serialized_start=2454
  _globals['_EDITMASKTICKETREQ']._serialized_end=2715
  _globals['_EDITMASKTICKETRES']._serialized_start=2717
  _globals['_EDITMASKTICKETRES']._serialized_end=2769
  _globals['_LISTALLOCATEDTICKETRES']._serialized_start=2771
  _globals['_LISTALLOCATEDTICKETRES']._serialized_end=2834
  _globals['_LISTALLOCATEDTICKETREQ']._serialized_start=2836
  _globals['_LISTALLOCATEDTICKETREQ']._serialized_end=2864
  _globals['_LISTAGENTTICKETSRESPONSE']._serialized_start=2866
  _globals['_LISTAGENTTICKETSRESPONSE']._serialized_end=2937
  _globals['_LISTAGENTTICKETSREQUEST']._serialized_start=2940
  _globals['_LISTAGENTTICKETSREQUEST']._serialized_end=3098
  _globals['_LISTAVAILABLEAGENTTICKETSRESPONSE']._serialized_start=3100
  _globals['_LISTAVAILABLEAGENTTICKETSRESPONSE']._serialized_end=3217
  _globals['_LISTAVAILABLEAGENTTICKETSREQUEST']._serialized_start=3220
  _globals['_LISTAVAILABLEAGENTTICKETSREQUEST']._serialized_end=3457
  _globals['_AVAILABLETICKETSFILTER']._serialized_start=3459
  _globals['_AVAILABLETICKETSFILTER']._serialized_end=3521
  _globals['_EDITTICKETRES']._serialized_start=3523
  _globals['_EDITTICKETRES']._serialized_end=3571
  _globals['_LISTTICKETSREQ']._serialized_start=3573
  _globals['_LISTTICKETSREQ']._serialized_end=3589
  _globals['_LISTTICKETSRES']._serialized_start=3591
  _globals['_LISTTICKETSRES']._serialized_end=3654
  _globals['_ASSIGNTICKETREQ']._serialized_start=3656
  _globals['_ASSIGNTICKETREQ']._serialized_end=3782
  _globals['_ASSIGNTICKETRES']._serialized_start=3784
  _globals['_ASSIGNTICKETRES']._serialized_end=3910
  _globals['_VIEWTICKETREQ']._serialized_start=3912
  _globals['_VIEWTICKETREQ']._serialized_end=3997
  _globals['_VIEWTICKETRES']._serialized_start=4000
  _globals['_VIEWTICKETRES']._serialized_end=4174
  _globals['_CREATECOMMENTREQ']._serialized_start=4176
  _globals['_CREATECOMMENTREQ']._serialized_end=4290
  _globals['_CREATECOMMENTRES']._serialized_start=4292
  _globals['_CREATECOMMENTRES']._serialized_end=4358
  _globals['_CLOSETICKETREQ']._serialized_start=4361
  _globals['_CLOSETICKETREQ']._serialized_end=4512
  _globals['_CLOSETICKETRES']._serialized_start=4514
  _globals['_CLOSETICKETRES']._serialized_end=4563
  _globals['_CREATESLAREQ']._serialized_start=4566
  _globals['_CREATESLAREQ']._serialized_end=4746
  _globals['_CREATESLARES']._serialized_start=4748
  _globals['_CREATESLARES']._serialized_end=4804
  _globals['_LISTSLAREQ']._serialized_start=4806
  _globals['_LISTSLAREQ']._serialized_end=4818
  _globals['_LISTSLARES']._serialized_start=4820
  _globals['_LISTSLARES']._serialized_end=4888
  _globals['_UPDATESLAREQ']._serialized_start=4890
  _globals['_UPDATESLAREQ']._serialized_end=4962
  _globals['_UPDATESLARES']._serialized_start=4964
  _globals['_UPDATESLARES']._serialized_end=5034
  _globals['_LISTSLACONDITIONREQ']._serialized_start=5036
  _globals['_LISTSLACONDITIONREQ']._serialized_end=5057
  _globals['_LISTSLACONDITIONRES']._serialized_start=5059
  _globals['_LISTSLACONDITIONRES']._serialized_end=5144
  _globals['_REPLYCOMMENTREQ']._serialized_start=5147
  _globals['_REPLYCOMMENTREQ']._serialized_end=5329
  _globals['_REPLYCOMMENTRES']._serialized_start=5331
  _globals['_REPLYCOMMENTRES']._serialized_end=5413
  _globals['_CREATESELFASSIGNREQ']._serialized_start=5415
  _globals['_CREATESELFASSIGNREQ']._serialized_end=5475
  _globals['_CREATESELFASSIGNRES']._serialized_start=5477
  _globals['_CREATESELFASSIGNRES']._serialized_end=5535
  _globals['_LISTSKILLSREQUEST']._serialized_start=5537
  _globals['_LISTSKILLSREQUEST']._serialized_end=5556
  _globals['_LISTSKILLSRESPONSE']._serialized_start=5558
  _globals['_LISTSKILLSRESPONSE']._serialized_end=5631
  _globals['_SKILL']._serialized_start=5633
  _globals['_SKILL']._serialized_end=5687
  _globals['_LISTUSERSREQUEST']._serialized_start=5689
  _globals['_LISTUSERSREQUEST']._serialized_end=5707
  _globals['_LISTUSERSRESPONSE']._serialized_start=5709
  _globals['_LISTUSERSRESPONSE']._serialized_end=5778
  _globals['_USER']._serialized_start=5780
  _globals['_USER']._serialized_end=5900
  _globals['_CREATETICKETACTIONREQUEST']._serialized_start=5902
  _globals['_CREATETICKETACTIONREQUEST']._serialized_end=5993
  _globals['_CREATETICKETACTIONRESPONSE']._serialized_start=5995
  _globals['_CREATETICKETACTIONRESPONSE']._serialized_end=6087
  _globals['_CLOSETICKETACTIONREQUEST']._serialized_start=6090
  _globals['_CLOSETICKETACTIONREQUEST']._serialized_end=6260
  _globals['_CLOSETICKETACTIONRESPONSE']._serialized_start=6262
  _globals['_CLOSETICKETACTIONRESPONSE']._serialized_end=6322
  _globals['_ASSIGNTICKETACTIONREQUEST']._serialized_start=6324
  _globals['_ASSIGNTICKETACTIONREQUEST']._serialized_end=6401
  _globals['_ASSIGNTICKETACTIONRESPONSE']._serialized_start=6403
  _globals['_ASSIGNTICKETACTIONRESPONSE']._serialized_end=6468
  _globals['_CHANGETICKETSTATUSREQUEST']._serialized_start=6471
  _globals['_CHANGETICKETSTATUSREQUEST']._serialized_end=6632
  _globals['_CHANGETICKETSTATUSRESPONSE']._serialized_start=6634
  _globals['_CHANGETICKETSTATUSRESPONSE']._serialized_end=6708
  _globals['_ADDENTITYREFREQUEST']._serialized_start=6710
  _globals['_ADDENTITYREFREQUEST']._serialized_end=6795
  _globals['_ADDENTITYREFRESPONSE']._serialized_start=6797
  _globals['_ADDENTITYREFRESPONSE']._serialized_end=6819
  _globals['_LISTENTITYREFSBYTICKETREQUEST']._serialized_start=6821
  _globals['_LISTENTITYREFSBYTICKETREQUEST']._serialized_end=6885
  _globals['_LISTENTITYREFSBYTICKETRESPONSE']._serialized_start=6887
  _globals['_LISTENTITYREFSBYTICKETRESPONSE']._serialized_end=6983
  _globals['_LISTTICKETSBYENTITYREFREQUEST']._serialized_start=6985
  _globals['_LISTTICKETSBYENTITYREFREQUEST']._serialized_end=7034
  _globals['_LISTTICKETSBYENTITYREFRESPONSE']._serialized_start=7036
  _globals['_LISTTICKETSBYENTITYREFRESPONSE']._serialized_end=7115
  _globals['_ENTITYREF']._serialized_start=7117
  _globals['_ENTITYREF']._serialized_end=7231
# @@protoc_insertion_point(module_scope)
