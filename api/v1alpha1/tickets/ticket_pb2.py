# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/tickets/ticket.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!api/v1alpha1/tickets/ticket.proto\x12\x14\x61pi.v1alpha1.tickets\x1a\x19\x61pi/commons/tickets.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\t\n\x07PingReq\"\t\n\x07PingRes\"\x9f\x03\n\x0f\x43reateTicketReq\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12#\n\x0bproject_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\nprojectSid\x12\x35\n\x08\x64ue_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x64ueDate\x12\x31\n\x08metadata\x18\t \x03(\x0b\x32\x15.api.commons.MetadataR\x08metadata\x12\x38\n\rticket_skills\x18\n \x03(\x0b\x32\x13.api.commons.SkillsR\x0cticketSkills\x12\x16\n\x06status\x18\x0b \x01(\x03R\x06status\x12/\n\nticket_sla\x18\x0c \x03(\x0b\x32\x10.api.commons.SlaR\tticketSla\x12\x1f\n\x0b\x61ssign_self\x18\r \x01(\x08R\nassignSelf\x12!\n\x0c\x61ssign_other\x18\x0e \x01(\tR\x0b\x61ssignOther\">\n\x0f\x43reateTicketRes\x12+\n\x06ticket\x18\x01 \x01(\x0b\x32\x13.api.commons.TicketR\x06ticket\"m\n\rEditTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x39\n\nedit_value\x18\x02 \x01(\x0b\x32\x1a.api.commons.EditAttributeR\teditValue\"\xb4\x01\n\x11\x45\x64itMaskTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x32\n\nedit_value\x18\x02 \x01(\x0b\x32\x13.api.commons.TicketR\teditValue\x12H\n\x12\x65\x64ited_fields_mask\x18\x03 \x03(\x0b\x32\x1a.google.protobuf.FieldMaskR\x10\x65\x64itedFieldsMask\"0\n\x11\x45\x64itMaskTicketRes\x12\x1b\n\tis_edited\x18\x01 \x01(\x08R\x08isEdited\"?\n\x16ListAllocatedTicketRes\x12!\n\nticket_sid\x18\x01 \x03(\x03\x42\x02\x30\x01R\tticketSid:\x02\x18\x01\"\x1c\n\x16ListAllocatedTicketReq:\x02\x18\x01\"s\n!ListAvailableAgentTicketsResponse\x12!\n\nticket_sid\x18\x01 \x03(\x03\x42\x02\x30\x01R\tticketSid\x12+\n\x06ticket\x18\x02 \x03(\x0b\x32\x13.api.commons.TicketR\x06ticket\"\"\n ListAvailableAgentTicketsRequest\",\n\rEditTicketRes\x12\x1b\n\tis_edited\x18\x01 \x01(\x08R\x08isEdited\"\x10\n\x0eListTicketsReq\"?\n\x0eListTicketsRes\x12-\n\x07tickets\x18\x01 \x03(\x0b\x32\x13.api.commons.TicketR\x07tickets\"z\n\x0f\x41ssignTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12#\n\rassignee_list\x18\x02 \x01(\tR\x0c\x61ssigneeList\x12\x1f\n\x0b\x61ssigned_id\x18\x03 \x01(\tR\nassignedId\"z\n\x0f\x41ssignTicketRes\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12#\n\rassignee_list\x18\x02 \x01(\tR\x0c\x61ssigneeList\x12\x1f\n\x0b\x61ssigned_id\x18\x03 \x01(\tR\nassignedId\"2\n\rViewTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\"\xae\x01\n\rViewTicketRes\x12+\n\x06ticket\x18\x01 \x01(\x0b\x32\x13.api.commons.TicketR\x06ticket\x12\x30\n\x08\x63omments\x18\x02 \x03(\x0b\x32\x14.api.commons.CommentR\x08\x63omments\x12>\n\rreply_comment\x18\x03 \x03(\x0b\x32\x19.api.commons.ReplyCommentR\x0creplyComment\"O\n\x10\x43reateCommentReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x18\n\x07\x63omment\x18\x02 \x01(\tR\x07\x63omment\"B\n\x10\x43reateCommentRes\x12.\n\x07\x63omment\x18\x01 \x01(\x0b\x32\x14.api.commons.CommentR\x07\x63omment\"r\n\x0e\x43loseTicketReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x18\n\x07\x63omment\x18\x02 \x01(\tR\x07\x63omment\x12#\n\x0b\x66rom_status\x18\x03 \x01(\x03\x42\x02\x30\x01R\nfromStatus\"-\n\x0e\x43loseTicketRes\x12\x1b\n\tis_status\x18\x01 \x01(\x08R\x08isStatus\"}\n\x0c\x43reateSlaReq\x12\x1b\n\x07sla_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x06slaSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08interval\x18\x04 \x01(\x03R\x08interval\"8\n\x0c\x43reateSlaRes\x12(\n\x03sla\x18\x01 \x01(\x0b\x32\x16.api.commons.TicketSlaR\x03sla\"\x0c\n\nListSlaReq\"D\n\nListSlaRes\x12\x36\n\nticketsSla\x18\x01 \x03(\x0b\x32\x16.api.commons.TicketSlaR\nticketsSla\"H\n\x0cUpdateSlaReq\x12\x1b\n\x07sla_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x06slaSid\x12\x1b\n\tis_active\x18\x02 \x01(\x03R\x08isActive\"F\n\x0cUpdateSlaRes\x12\x36\n\nticketsSla\x18\x01 \x01(\x0b\x32\x16.api.commons.TicketSlaR\nticketsSla\"\x15\n\x13ListSlaConditionReq\"U\n\x13ListSlaConditionRes\x12>\n\x0cslaCondition\x18\x01 \x03(\x0b\x32\x1a.api.commons.SlaConditionsR\x0cslaCondition\"\x93\x01\n\x0fReplyCommentReq\x12#\n\x0b\x63omment_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\ncommentSid\x12!\n\nticket_sid\x18\x02 \x01(\x03\x42\x02\x30\x01R\tticketSid\x12\x14\n\x05reply\x18\x03 \x01(\tR\x05reply\x12\"\n\rcreated_by_id\x18\x04 \x01(\tR\x0b\x63reatedById\"R\n\x0fReplyCommentRes\x12?\n\nis_created\x18\x01 \x01(\x0b\x32 .api.commons.ConfirmReplyCommentR\tisCreated\"8\n\x13\x43reateSelfAssignReq\x12!\n\nticket_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tticketSid\"6\n\x13\x43reateSelfAssignRes\x12\x1f\n\x0bis_assigned\x18\x01 \x01(\x08R\nisAssigned\"\x13\n\x11ListSkillsRequest\"I\n\x12ListSkillsResponse\x12\x33\n\x06skills\x18\x01 \x03(\x0b\x32\x1b.api.v1alpha1.tickets.SkillR\x06skills\"6\n\x05Skill\x12\x19\n\x08skill_id\x18\x01 \x01(\tR\x07skillId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\x12\n\x10ListUsersRequest\"E\n\x11ListUsersResponse\x12\x30\n\x05users\x18\x01 \x03(\x0b\x32\x1a.api.v1alpha1.tickets.UserR\x05users\"[\n\x04User\x12\x17\n\x07user_id\x18\x01 \x01(\tR\x06userId\x12\x1d\n\nfirst_name\x18\x02 \x01(\tR\tfirstName\x12\x1b\n\tlast_name\x18\x03 \x01(\tR\x08lastNameB\x99\x01\n\x18\x63om.api.v1alpha1.ticketsB\x0bTicketProtoP\x01\xa2\x02\x03\x41VT\xaa\x02\x14\x41pi.V1alpha1.Tickets\xca\x02\x14\x41pi\\V1alpha1\\Tickets\xe2\x02 Api\\V1alpha1\\Tickets\\GPBMetadata\xea\x02\x16\x41pi::V1alpha1::Ticketsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.tickets.ticket_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.api.v1alpha1.ticketsB\013TicketProtoP\001\242\002\003AVT\252\002\024Api.V1alpha1.Tickets\312\002\024Api\\V1alpha1\\Tickets\342\002 Api\\V1alpha1\\Tickets\\GPBMetadata\352\002\026Api::V1alpha1::Tickets'
  _CREATETICKETREQ.fields_by_name['project_sid']._options = None
  _CREATETICKETREQ.fields_by_name['project_sid']._serialized_options = b'0\001'
  _EDITTICKETREQ.fields_by_name['ticket_sid']._options = None
  _EDITTICKETREQ.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _EDITMASKTICKETREQ.fields_by_name['ticket_sid']._options = None
  _EDITMASKTICKETREQ.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _LISTALLOCATEDTICKETRES.fields_by_name['ticket_sid']._options = None
  _LISTALLOCATEDTICKETRES.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _LISTALLOCATEDTICKETRES._options = None
  _LISTALLOCATEDTICKETRES._serialized_options = b'\030\001'
  _LISTALLOCATEDTICKETREQ._options = None
  _LISTALLOCATEDTICKETREQ._serialized_options = b'\030\001'
  _LISTAVAILABLEAGENTTICKETSRESPONSE.fields_by_name['ticket_sid']._options = None
  _LISTAVAILABLEAGENTTICKETSRESPONSE.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _ASSIGNTICKETREQ.fields_by_name['ticket_sid']._options = None
  _ASSIGNTICKETREQ.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _ASSIGNTICKETRES.fields_by_name['ticket_sid']._options = None
  _ASSIGNTICKETRES.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _VIEWTICKETREQ.fields_by_name['ticket_sid']._options = None
  _VIEWTICKETREQ.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _CREATECOMMENTREQ.fields_by_name['ticket_sid']._options = None
  _CREATECOMMENTREQ.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _CLOSETICKETREQ.fields_by_name['ticket_sid']._options = None
  _CLOSETICKETREQ.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _CLOSETICKETREQ.fields_by_name['from_status']._options = None
  _CLOSETICKETREQ.fields_by_name['from_status']._serialized_options = b'0\001'
  _CREATESLAREQ.fields_by_name['sla_sid']._options = None
  _CREATESLAREQ.fields_by_name['sla_sid']._serialized_options = b'0\001'
  _UPDATESLAREQ.fields_by_name['sla_sid']._options = None
  _UPDATESLAREQ.fields_by_name['sla_sid']._serialized_options = b'0\001'
  _REPLYCOMMENTREQ.fields_by_name['comment_sid']._options = None
  _REPLYCOMMENTREQ.fields_by_name['comment_sid']._serialized_options = b'0\001'
  _REPLYCOMMENTREQ.fields_by_name['ticket_sid']._options = None
  _REPLYCOMMENTREQ.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _CREATESELFASSIGNREQ.fields_by_name['ticket_sid']._options = None
  _CREATESELFASSIGNREQ.fields_by_name['ticket_sid']._serialized_options = b'0\001'
  _globals['_PINGREQ']._serialized_start=153
  _globals['_PINGREQ']._serialized_end=162
  _globals['_PINGRES']._serialized_start=164
  _globals['_PINGRES']._serialized_end=173
  _globals['_CREATETICKETREQ']._serialized_start=176
  _globals['_CREATETICKETREQ']._serialized_end=591
  _globals['_CREATETICKETRES']._serialized_start=593
  _globals['_CREATETICKETRES']._serialized_end=655
  _globals['_EDITTICKETREQ']._serialized_start=657
  _globals['_EDITTICKETREQ']._serialized_end=766
  _globals['_EDITMASKTICKETREQ']._serialized_start=769
  _globals['_EDITMASKTICKETREQ']._serialized_end=949
  _globals['_EDITMASKTICKETRES']._serialized_start=951
  _globals['_EDITMASKTICKETRES']._serialized_end=999
  _globals['_LISTALLOCATEDTICKETRES']._serialized_start=1001
  _globals['_LISTALLOCATEDTICKETRES']._serialized_end=1064
  _globals['_LISTALLOCATEDTICKETREQ']._serialized_start=1066
  _globals['_LISTALLOCATEDTICKETREQ']._serialized_end=1094
  _globals['_LISTAVAILABLEAGENTTICKETSRESPONSE']._serialized_start=1096
  _globals['_LISTAVAILABLEAGENTTICKETSRESPONSE']._serialized_end=1211
  _globals['_LISTAVAILABLEAGENTTICKETSREQUEST']._serialized_start=1213
  _globals['_LISTAVAILABLEAGENTTICKETSREQUEST']._serialized_end=1247
  _globals['_EDITTICKETRES']._serialized_start=1249
  _globals['_EDITTICKETRES']._serialized_end=1293
  _globals['_LISTTICKETSREQ']._serialized_start=1295
  _globals['_LISTTICKETSREQ']._serialized_end=1311
  _globals['_LISTTICKETSRES']._serialized_start=1313
  _globals['_LISTTICKETSRES']._serialized_end=1376
  _globals['_ASSIGNTICKETREQ']._serialized_start=1378
  _globals['_ASSIGNTICKETREQ']._serialized_end=1500
  _globals['_ASSIGNTICKETRES']._serialized_start=1502
  _globals['_ASSIGNTICKETRES']._serialized_end=1624
  _globals['_VIEWTICKETREQ']._serialized_start=1626
  _globals['_VIEWTICKETREQ']._serialized_end=1676
  _globals['_VIEWTICKETRES']._serialized_start=1679
  _globals['_VIEWTICKETRES']._serialized_end=1853
  _globals['_CREATECOMMENTREQ']._serialized_start=1855
  _globals['_CREATECOMMENTREQ']._serialized_end=1934
  _globals['_CREATECOMMENTRES']._serialized_start=1936
  _globals['_CREATECOMMENTRES']._serialized_end=2002
  _globals['_CLOSETICKETREQ']._serialized_start=2004
  _globals['_CLOSETICKETREQ']._serialized_end=2118
  _globals['_CLOSETICKETRES']._serialized_start=2120
  _globals['_CLOSETICKETRES']._serialized_end=2165
  _globals['_CREATESLAREQ']._serialized_start=2167
  _globals['_CREATESLAREQ']._serialized_end=2292
  _globals['_CREATESLARES']._serialized_start=2294
  _globals['_CREATESLARES']._serialized_end=2350
  _globals['_LISTSLAREQ']._serialized_start=2352
  _globals['_LISTSLAREQ']._serialized_end=2364
  _globals['_LISTSLARES']._serialized_start=2366
  _globals['_LISTSLARES']._serialized_end=2434
  _globals['_UPDATESLAREQ']._serialized_start=2436
  _globals['_UPDATESLAREQ']._serialized_end=2508
  _globals['_UPDATESLARES']._serialized_start=2510
  _globals['_UPDATESLARES']._serialized_end=2580
  _globals['_LISTSLACONDITIONREQ']._serialized_start=2582
  _globals['_LISTSLACONDITIONREQ']._serialized_end=2603
  _globals['_LISTSLACONDITIONRES']._serialized_start=2605
  _globals['_LISTSLACONDITIONRES']._serialized_end=2690
  _globals['_REPLYCOMMENTREQ']._serialized_start=2693
  _globals['_REPLYCOMMENTREQ']._serialized_end=2840
  _globals['_REPLYCOMMENTRES']._serialized_start=2842
  _globals['_REPLYCOMMENTRES']._serialized_end=2924
  _globals['_CREATESELFASSIGNREQ']._serialized_start=2926
  _globals['_CREATESELFASSIGNREQ']._serialized_end=2982
  _globals['_CREATESELFASSIGNRES']._serialized_start=2984
  _globals['_CREATESELFASSIGNRES']._serialized_end=3038
  _globals['_LISTSKILLSREQUEST']._serialized_start=3040
  _globals['_LISTSKILLSREQUEST']._serialized_end=3059
  _globals['_LISTSKILLSRESPONSE']._serialized_start=3061
  _globals['_LISTSKILLSRESPONSE']._serialized_end=3134
  _globals['_SKILL']._serialized_start=3136
  _globals['_SKILL']._serialized_end=3190
  _globals['_LISTUSERSREQUEST']._serialized_start=3192
  _globals['_LISTUSERSREQUEST']._serialized_end=3210
  _globals['_LISTUSERSRESPONSE']._serialized_start=3212
  _globals['_LISTUSERSRESPONSE']._serialized_end=3281
  _globals['_USER']._serialized_start=3283
  _globals['_USER']._serialized_end=3374
# @@protoc_insertion_point(module_scope)
