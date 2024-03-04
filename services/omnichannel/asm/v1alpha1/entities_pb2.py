# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: services/omnichannel/asm/v1alpha1/entities.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from services.omnichannel.asm.entities.v1alpha1 import session_pb2 as services_dot_omnichannel_dot_asm_dot_entities_dot_v1alpha1_dot_session__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0services/omnichannel/asm/v1alpha1/entities.proto\x12!services.omnichannel.asm.v1alpha1\x1a\x38services/omnichannel/asm/entities/v1alpha1/session.proto\"\x16\n\x14\x43reateSessionRequest\"p\n\x15\x43reateSessionResponse\x12W\n\x0b\x61sm_session\x18\x01 \x01(\x0b\x32\x36.services.omnichannel.asm.entities.v1alpha1.AsmSessionR\nasmSession\"S\n\x11\x45ndSessionRequest\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12\x16\n\x06reason\x18\x02 \x01(\tR\x06reason\"\x14\n\x12\x45ndSessionResponse\"\x1a\n\x18GetCurrentSessionRequest\"t\n\x19GetCurrentSessionResponse\x12W\n\x0b\x61sm_session\x18\x01 \x01(\x0b\x32\x36.services.omnichannel.asm.entities.v1alpha1.AsmSessionR\nasmSession\"\xf8\x01\n\x12\x45nableVoiceRequest\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\x12Y\n\x06skills\x18\x03 \x03(\x0b\x32\x41.services.omnichannel.asm.v1alpha1.EnableVoiceRequest.SkillsEntryR\x06skills\x1a\x39\n\x0bSkillsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x03R\x05value:\x02\x38\x01\"\xe2\x01\n\x13\x45nableVoiceResponse\x12]\n\rvoice_session\x18\x01 \x01(\x0b\x32\x38.services.omnichannel.asm.entities.v1alpha1.VoiceSessionR\x0cvoiceSession\x12l\n\x12voice_registration\x18\x02 \x01(\x0b\x32=.services.omnichannel.asm.entities.v1alpha1.VoiceRegistrationR\x11voiceRegistration\"=\n\x13\x44isableVoiceRequest\x12&\n\x0f\x61sm_session_sid\x18\x01 \x01(\x03R\rasmSessionSid\"\x16\n\x14\x44isableVoiceResponse\"\x1b\n\x19ListAsmUserDetailsRequest\"t\n\x1aListAsmUserDetailsResponse\x12V\n\x08sessions\x18\x01 \x03(\x0b\x32:.services.omnichannel.asm.entities.v1alpha1.AsmUserDetailsR\x08sessionsB\xdd\x01\n%com.services.omnichannel.asm.v1alpha1B\rEntitiesProtoP\x01\xa2\x02\x03SOA\xaa\x02!Services.Omnichannel.Asm.V1alpha1\xca\x02!Services\\Omnichannel\\Asm\\V1alpha1\xe2\x02-Services\\Omnichannel\\Asm\\V1alpha1\\GPBMetadata\xea\x02$Services::Omnichannel::Asm::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.omnichannel.asm.v1alpha1.entities_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.services.omnichannel.asm.v1alpha1B\rEntitiesProtoP\001\242\002\003SOA\252\002!Services.Omnichannel.Asm.V1alpha1\312\002!Services\\Omnichannel\\Asm\\V1alpha1\342\002-Services\\Omnichannel\\Asm\\V1alpha1\\GPBMetadata\352\002$Services::Omnichannel::Asm::V1alpha1'
  _globals['_ENABLEVOICEREQUEST_SKILLSENTRY']._options = None
  _globals['_ENABLEVOICEREQUEST_SKILLSENTRY']._serialized_options = b'8\001'
  _globals['_CREATESESSIONREQUEST']._serialized_start=145
  _globals['_CREATESESSIONREQUEST']._serialized_end=167
  _globals['_CREATESESSIONRESPONSE']._serialized_start=169
  _globals['_CREATESESSIONRESPONSE']._serialized_end=281
  _globals['_ENDSESSIONREQUEST']._serialized_start=283
  _globals['_ENDSESSIONREQUEST']._serialized_end=366
  _globals['_ENDSESSIONRESPONSE']._serialized_start=368
  _globals['_ENDSESSIONRESPONSE']._serialized_end=388
  _globals['_GETCURRENTSESSIONREQUEST']._serialized_start=390
  _globals['_GETCURRENTSESSIONREQUEST']._serialized_end=416
  _globals['_GETCURRENTSESSIONRESPONSE']._serialized_start=418
  _globals['_GETCURRENTSESSIONRESPONSE']._serialized_end=534
  _globals['_ENABLEVOICEREQUEST']._serialized_start=537
  _globals['_ENABLEVOICEREQUEST']._serialized_end=785
  _globals['_ENABLEVOICEREQUEST_SKILLSENTRY']._serialized_start=728
  _globals['_ENABLEVOICEREQUEST_SKILLSENTRY']._serialized_end=785
  _globals['_ENABLEVOICERESPONSE']._serialized_start=788
  _globals['_ENABLEVOICERESPONSE']._serialized_end=1014
  _globals['_DISABLEVOICEREQUEST']._serialized_start=1016
  _globals['_DISABLEVOICEREQUEST']._serialized_end=1077
  _globals['_DISABLEVOICERESPONSE']._serialized_start=1079
  _globals['_DISABLEVOICERESPONSE']._serialized_end=1101
  _globals['_LISTASMUSERDETAILSREQUEST']._serialized_start=1103
  _globals['_LISTASMUSERDETAILSREQUEST']._serialized_end=1130
  _globals['_LISTASMUSERDETAILSRESPONSE']._serialized_start=1132
  _globals['_LISTASMUSERDETAILSRESPONSE']._serialized_end=1248
# @@protoc_insertion_point(module_scope)
