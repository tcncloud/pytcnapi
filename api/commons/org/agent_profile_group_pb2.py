# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/org/agent_profile_group.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'api/commons/org/agent_profile_group.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)api/commons/org/agent_profile_group.proto\x12\x0f\x61pi.commons.org\x1a\x1d\x61pi/commons/omnichannel.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xfb\x01\n\x11\x41gentProfileGroup\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12G\n\x0fpriority_groups\x18\x04 \x03(\x0b\x32\x1e.api.commons.org.PriorityGroupR\x0epriorityGroups\x12=\n\x0clast_updated\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0blastUpdated\x12#\n\rdefault_group\x18\n \x01(\x08R\x0c\x64\x65\x66\x61ultGroup\"j\n\rPriorityGroup\x12\x1c\n\tthreshold\x18\x01 \x01(\x05R\tthreshold\x12;\n\x0c\x63hannel_type\x18\x02 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelTypeB\x8b\x01\n\x13\x63om.api.commons.orgB\x16\x41gentProfileGroupProtoP\x01\xa2\x02\x03\x41\x43O\xaa\x02\x0f\x41pi.Commons.Org\xca\x02\x0f\x41pi\\Commons\\Org\xe2\x02\x1b\x41pi\\Commons\\Org\\GPBMetadata\xea\x02\x11\x41pi::Commons::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org.agent_profile_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023com.api.commons.orgB\026AgentProfileGroupProtoP\001\242\002\003ACO\252\002\017Api.Commons.Org\312\002\017Api\\Commons\\Org\342\002\033Api\\Commons\\Org\\GPBMetadata\352\002\021Api::Commons::Org'
  _globals['_AGENTPROFILEGROUP']._serialized_start=127
  _globals['_AGENTPROFILEGROUP']._serialized_end=378
  _globals['_PRIORITYGROUP']._serialized_start=380
  _globals['_PRIORITYGROUP']._serialized_end=486
# @@protoc_insertion_point(module_scope)
