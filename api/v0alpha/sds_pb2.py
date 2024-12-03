# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v0alpha/sds.proto
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
    'api/v0alpha/sds.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/v0alpha/sds.proto\x12\x0b\x61pi.v0alpha\x1a\x17\x61nnotations/authz.proto\x1a\x15\x61pi/commons/acd.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"m\n\x17GetAgentResponseDataReq\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x02 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\"\xfe\x01\n\x17GetAgentResponseDataRes\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x02 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12Q\n\tresponses\x18\x03 \x03(\x0b\x32\x33.api.v0alpha.GetAgentResponseDataRes.ResponsesEntryR\tresponses\x1a<\n\x0eResponsesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"`\n\nGetCallReq\x12\x19\n\x08\x63\x61ll_sid\x18\x02 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x03 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\"\x90\x01\n\x15UpdateVoicemailBoxReq\x12\x19\n\x08\x63\x61ll_sid\x18\x02 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x03 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12#\n\rpbx_extension\x18\x04 \x01(\tR\x0cpbxExtension\"\x17\n\x15UpdateVoicemailBoxRes\"\xeb\x07\n\nCallObject\x12\x10\n\x03oid\x18\x01 \x01(\tR\x03oid\x12\x19\n\x08\x63\x61ll_sid\x18\x02 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x03 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12\x18\n\x07updated\x18\n \x01(\x03R\x07updated\x12;\n\x06skills\x18\x0b \x03(\x0b\x32#.api.v0alpha.CallObject.SkillsEntryR\x06skills\x12%\n\x0erecording_file\x18\x0c \x01(\tR\rrecordingFile\x12=\n\x0cupdated_date\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0bupdatedDate\x12\x1d\n\nsrc_number\x18\x0e \x01(\tR\tsrcNumber\x12\x1d\n\ndst_number\x18\x0f \x01(\tR\tdstNumber\x12$\n\x0e\x63\x61ller_id_name\x18\x10 \x01(\tR\x0c\x63\x61llerIdName\x12!\n\x0c\x61gent_worker\x18\x11 \x01(\tR\x0b\x61gentWorker\x12\x16\n\x06\x65vents\x18\x12 \x03(\tR\x06\x65vents\x12\x1b\n\tcall_data\x18\x13 \x01(\tR\x08\x63\x61llData\x12^\n\x13\x61gent_response_data\x18\x14 \x03(\x0b\x32..api.v0alpha.CallObject.AgentResponseDataEntryR\x11\x61gentResponseData\x12\x1a\n\x08recorded\x18\x15 \x01(\x08R\x08recorded\x12\x1c\n\tconnected\x18\x16 \x01(\x08R\tconnected\x12\x1c\n\tsuspended\x18\x17 \x01(\x08R\tsuspended\x12+\n\x11\x64isconnect_reason\x18\x18 \x01(\tR\x10\x64isconnectReason\x12 \n\x0bvoicemailed\x18\x19 \x01(\x08R\x0bvoicemailed\x12#\n\rvoicemail_box\x18\x1a \x01(\tR\x0cvoicemailBox\x12\x1e\n\noriginated\x18\x1b \x01(\tR\noriginated\x12\x16\n\x06\x66older\x18\x1c \x01(\tR\x06\x66older\x12\x19\n\x08rtp_info\x18\x1d \x01(\tR\x07rtpInfo\x1a\x39\n\x0bSkillsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\x1a\x44\n\x16\x41gentResponseDataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x84\x02\n\x1aUpdateAgentResponseDataReq\x12\x19\n\x08\x63\x61ll_sid\x18\x02 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x03 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12T\n\tresponses\x18\x04 \x03(\x0b\x32\x36.api.v0alpha.UpdateAgentResponseDataReq.ResponsesEntryR\tresponses\x1a<\n\x0eResponsesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x1c\n\x1aUpdateAgentResponseDataRes2\xcc\x04\n\x03Sds\x12\x9b\x01\n\x14GetAgentResponseData\x12$.api.v0alpha.GetAgentResponseDataReq\x1a$.api.v0alpha.GetAgentResponseDataRes\"7\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02*\"%/api/v0alpha/sds/getagentresponsedata:\x01*\x12g\n\x07GetCall\x12\x17.api.v0alpha.GetCallReq\x1a\x17.api.v0alpha.CallObject\"*\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x1d\"\x18/api/v0alpha/sds/getcall:\x01*\x12\xa7\x01\n\x17UpdateAgentResponseData\x12\'.api.v0alpha.UpdateAgentResponseDataReq\x1a\'.api.v0alpha.UpdateAgentResponseDataRes\":\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02-\"(/api/v0alpha/sds/updateagentresponsedata:\x01*\x12\x93\x01\n\x12UpdateVoicemailBox\x12\".api.v0alpha.UpdateVoicemailBoxReq\x1a\".api.v0alpha.UpdateVoicemailBoxRes\"5\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02(\"#/api/v0alpha/sds/updatevoicemailbox:\x01*Bh\n\x0f\x63om.api.v0alphaB\x08SdsProtoP\x01\xa2\x02\x03\x41VX\xaa\x02\x0b\x41pi.V0alpha\xca\x02\x0b\x41pi\\V0alpha\xe2\x02\x17\x41pi\\V0alpha\\GPBMetadata\xea\x02\x0c\x41pi::V0alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v0alpha.sds_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.v0alphaB\010SdsProtoP\001\242\002\003AVX\252\002\013Api.V0alpha\312\002\013Api\\V0alpha\342\002\027Api\\V0alpha\\GPBMetadata\352\002\014Api::V0alpha'
  _globals['_GETAGENTRESPONSEDATARES_RESPONSESENTRY']._loaded_options = None
  _globals['_GETAGENTRESPONSEDATARES_RESPONSESENTRY']._serialized_options = b'8\001'
  _globals['_CALLOBJECT_SKILLSENTRY']._loaded_options = None
  _globals['_CALLOBJECT_SKILLSENTRY']._serialized_options = b'8\001'
  _globals['_CALLOBJECT_AGENTRESPONSEDATAENTRY']._loaded_options = None
  _globals['_CALLOBJECT_AGENTRESPONSEDATAENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEAGENTRESPONSEDATAREQ_RESPONSESENTRY']._loaded_options = None
  _globals['_UPDATEAGENTRESPONSEDATAREQ_RESPONSESENTRY']._serialized_options = b'8\001'
  _globals['_SDS'].methods_by_name['GetAgentResponseData']._loaded_options = None
  _globals['_SDS'].methods_by_name['GetAgentResponseData']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002*\"%/api/v0alpha/sds/getagentresponsedata:\001*'
  _globals['_SDS'].methods_by_name['GetCall']._loaded_options = None
  _globals['_SDS'].methods_by_name['GetCall']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\035\"\030/api/v0alpha/sds/getcall:\001*'
  _globals['_SDS'].methods_by_name['UpdateAgentResponseData']._loaded_options = None
  _globals['_SDS'].methods_by_name['UpdateAgentResponseData']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002-\"(/api/v0alpha/sds/updateagentresponsedata:\001*'
  _globals['_SDS'].methods_by_name['UpdateVoicemailBox']._loaded_options = None
  _globals['_SDS'].methods_by_name['UpdateVoicemailBox']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002(\"#/api/v0alpha/sds/updatevoicemailbox:\001*'
  _globals['_GETAGENTRESPONSEDATAREQ']._serialized_start=149
  _globals['_GETAGENTRESPONSEDATAREQ']._serialized_end=258
  _globals['_GETAGENTRESPONSEDATARES']._serialized_start=261
  _globals['_GETAGENTRESPONSEDATARES']._serialized_end=515
  _globals['_GETAGENTRESPONSEDATARES_RESPONSESENTRY']._serialized_start=455
  _globals['_GETAGENTRESPONSEDATARES_RESPONSESENTRY']._serialized_end=515
  _globals['_GETCALLREQ']._serialized_start=517
  _globals['_GETCALLREQ']._serialized_end=613
  _globals['_UPDATEVOICEMAILBOXREQ']._serialized_start=616
  _globals['_UPDATEVOICEMAILBOXREQ']._serialized_end=760
  _globals['_UPDATEVOICEMAILBOXRES']._serialized_start=762
  _globals['_UPDATEVOICEMAILBOXRES']._serialized_end=785
  _globals['_CALLOBJECT']._serialized_start=788
  _globals['_CALLOBJECT']._serialized_end=1791
  _globals['_CALLOBJECT_SKILLSENTRY']._serialized_start=1664
  _globals['_CALLOBJECT_SKILLSENTRY']._serialized_end=1721
  _globals['_CALLOBJECT_AGENTRESPONSEDATAENTRY']._serialized_start=1723
  _globals['_CALLOBJECT_AGENTRESPONSEDATAENTRY']._serialized_end=1791
  _globals['_UPDATEAGENTRESPONSEDATAREQ']._serialized_start=1794
  _globals['_UPDATEAGENTRESPONSEDATAREQ']._serialized_end=2054
  _globals['_UPDATEAGENTRESPONSEDATAREQ_RESPONSESENTRY']._serialized_start=455
  _globals['_UPDATEAGENTRESPONSEDATAREQ_RESPONSESENTRY']._serialized_end=515
  _globals['_UPDATEAGENTRESPONSEDATARES']._serialized_start=2056
  _globals['_UPDATEAGENTRESPONSEDATARES']._serialized_end=2084
  _globals['_SDS']._serialized_start=2087
  _globals['_SDS']._serialized_end=2675
# @@protoc_insertion_point(module_scope)
