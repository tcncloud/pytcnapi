# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/omnichannel/asm/v1alpha1/entities.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'services/omnichannel/asm/v1alpha1/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import event_pb2 as api_dot_commons_dot_event__pb2
from services.omnichannel.asm.entities.v1alpha1 import session_pb2 as services_dot_omnichannel_dot_asm_dot_entities_dot_v1alpha1_dot_session__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0services/omnichannel/asm/v1alpha1/entities.proto\x12!services.omnichannel.asm.v1alpha1\x1a\x17\x61pi/commons/event.proto\x1a\x38services/omnichannel/asm/entities/v1alpha1/session.proto\"\x16\n\x14\x43reateSessionRequest\"p\n\x15\x43reateSessionResponse\x12W\n\x0b\x61sm_session\x18\x01 \x01(\x0b\x32\x36.services.omnichannel.asm.entities.v1alpha1.AsmSessionR\nasmSession\"S\n\x11\x45ndSessionRequest\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12\x16\n\x06reason\x18\x02 \x01(\tR\x06reason\"\x14\n\x12\x45ndSessionResponse\"\x1a\n\x18GetCurrentSessionRequest\"t\n\x19GetCurrentSessionResponse\x12W\n\x0b\x61sm_session\x18\x01 \x01(\x0b\x32\x36.services.omnichannel.asm.entities.v1alpha1.AsmSessionR\nasmSession\"\xf8\x01\n\x12\x45nableVoiceRequest\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\x12Y\n\x06skills\x18\x03 \x03(\x0b\x32\x41.services.omnichannel.asm.v1alpha1.EnableVoiceRequest.SkillsEntryR\x06skills\x1a\x39\n\x0bSkillsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"\xe2\x01\n\x13\x45nableVoiceResponse\x12]\n\rvoice_session\x18\x01 \x01(\x0b\x32\x38.services.omnichannel.asm.entities.v1alpha1.VoiceSessionR\x0cvoiceSession\x12l\n\x12voice_registration\x18\x02 \x01(\x0b\x32=.services.omnichannel.asm.entities.v1alpha1.VoiceRegistrationR\x11voiceRegistration\"=\n\x13\x44isableVoiceRequest\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\"\x16\n\x14\x44isableVoiceResponse\"\x1b\n\x19ListAsmUserDetailsRequest\"\xde\x01\n\x1aListAsmUserDetailsResponse\x12Z\n\x08sessions\x18\x01 \x03(\x0b\x32:.services.omnichannel.asm.entities.v1alpha1.AsmUserDetailsB\x02\x18\x01R\x08sessions\x12\x64\n\x10\x61sm_user_details\x18\x02 \x03(\x0b\x32:.services.omnichannel.asm.entities.v1alpha1.AsmUserDetailsR\x0e\x61smUserDetails\"\x9d\x01\n\x11PushEventsRequest\x12*\n\x0f\x61ms_session_sid\x18\x01 \x01(\x03\x42\x02\x18\x01R\ramsSessionSid\x12\x34\n\nasm_events\x18\x02 \x03(\x0b\x32\x15.api.commons.AsmEventR\tasmEvents\x12&\n\x0f\x61sm_session_sid\x18\x03 \x01(\x03R\rasmSessionSid\"\x13\n\x11PushEventResponseB\xdd\x01\n%com.services.omnichannel.asm.v1alpha1B\rEntitiesProtoP\x01\xa2\x02\x03SOA\xaa\x02!Services.Omnichannel.Asm.V1alpha1\xca\x02!Services\\Omnichannel\\Asm\\V1alpha1\xe2\x02-Services\\Omnichannel\\Asm\\V1alpha1\\GPBMetadata\xea\x02$Services::Omnichannel::Asm::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.omnichannel.asm.v1alpha1.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.services.omnichannel.asm.v1alpha1B\rEntitiesProtoP\001\242\002\003SOA\252\002!Services.Omnichannel.Asm.V1alpha1\312\002!Services\\Omnichannel\\Asm\\V1alpha1\342\002-Services\\Omnichannel\\Asm\\V1alpha1\\GPBMetadata\352\002$Services::Omnichannel::Asm::V1alpha1'
  _globals['_ENABLEVOICEREQUEST_SKILLSENTRY']._loaded_options = None
  _globals['_ENABLEVOICEREQUEST_SKILLSENTRY']._serialized_options = b'8\001'
  _globals['_LISTASMUSERDETAILSRESPONSE'].fields_by_name['sessions']._loaded_options = None
  _globals['_LISTASMUSERDETAILSRESPONSE'].fields_by_name['sessions']._serialized_options = b'\030\001'
  _globals['_PUSHEVENTSREQUEST'].fields_by_name['ams_session_sid']._loaded_options = None
  _globals['_PUSHEVENTSREQUEST'].fields_by_name['ams_session_sid']._serialized_options = b'\030\001'
  _globals['_CREATESESSIONREQUEST']._serialized_start=170
  _globals['_CREATESESSIONREQUEST']._serialized_end=192
  _globals['_CREATESESSIONRESPONSE']._serialized_start=194
  _globals['_CREATESESSIONRESPONSE']._serialized_end=306
  _globals['_ENDSESSIONREQUEST']._serialized_start=308
  _globals['_ENDSESSIONREQUEST']._serialized_end=391
  _globals['_ENDSESSIONRESPONSE']._serialized_start=393
  _globals['_ENDSESSIONRESPONSE']._serialized_end=413
  _globals['_GETCURRENTSESSIONREQUEST']._serialized_start=415
  _globals['_GETCURRENTSESSIONREQUEST']._serialized_end=441
  _globals['_GETCURRENTSESSIONRESPONSE']._serialized_start=443
  _globals['_GETCURRENTSESSIONRESPONSE']._serialized_end=559
  _globals['_ENABLEVOICEREQUEST']._serialized_start=562
  _globals['_ENABLEVOICEREQUEST']._serialized_end=810
  _globals['_ENABLEVOICEREQUEST_SKILLSENTRY']._serialized_start=753
  _globals['_ENABLEVOICEREQUEST_SKILLSENTRY']._serialized_end=810
  _globals['_ENABLEVOICERESPONSE']._serialized_start=813
  _globals['_ENABLEVOICERESPONSE']._serialized_end=1039
  _globals['_DISABLEVOICEREQUEST']._serialized_start=1041
  _globals['_DISABLEVOICEREQUEST']._serialized_end=1102
  _globals['_DISABLEVOICERESPONSE']._serialized_start=1104
  _globals['_DISABLEVOICERESPONSE']._serialized_end=1126
  _globals['_LISTASMUSERDETAILSREQUEST']._serialized_start=1128
  _globals['_LISTASMUSERDETAILSREQUEST']._serialized_end=1155
  _globals['_LISTASMUSERDETAILSRESPONSE']._serialized_start=1158
  _globals['_LISTASMUSERDETAILSRESPONSE']._serialized_end=1380
  _globals['_PUSHEVENTSREQUEST']._serialized_start=1383
  _globals['_PUSHEVENTSREQUEST']._serialized_end=1540
  _globals['_PUSHEVENTRESPONSE']._serialized_start=1542
  _globals['_PUSHEVENTRESPONSE']._serialized_end=1561
# @@protoc_insertion_point(module_scope)
