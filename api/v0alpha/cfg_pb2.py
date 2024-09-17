# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v0alpha/cfg.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'api/v0alpha/cfg.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/v0alpha/cfg.proto\x12\x0b\x61pi.v0alpha\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\"+\n\x0cGetConfigReq\x12\x1b\n\tregion_id\x18\x01 \x01(\tR\x08regionId\"\x95\x06\n\x08WebAgent\x12;\n\topen_sips\x18\x01 \x01(\x0b\x32\x1e.api.v0alpha.WebAgent.OpenSipsR\x08openSips\x12M\n\x0f\x65ngine_priority\x18\x02 \x01(\x0b\x32$.api.v0alpha.WebAgent.EnginePriorityR\x0e\x65nginePriority\x12\x1b\n\tlog_level\x18\x03 \x01(\x03R\x08logLevel\x12\x19\n\x08use_stun\x18\x04 \x01(\x03R\x07useStun\x12\"\n\ruse_fast_stun\x18\x05 \x01(\x03R\x0buseFastStun\x12 \n\x0cuse_fast_ice\x18\x06 \x01(\x03R\nuseFastIce\x12\x1f\n\x0bice_timeout\x18\x07 \x01(\x03R\niceTimeout\x12&\n\x0fset_final_codec\x18\x08 \x01(\x03R\rsetFinalCodec\x12\x1b\n\tuse_rport\x18\t \x01(\x03R\x08useRport\x12\x34\n\x06server\x18\n \x01(\x0b\x32\x1c.api.v0alpha.WebAgent.ServerR\x06server\x12\x19\n\x08\x62\x61se_url\x18\x0b \x01(\tR\x07\x62\x61seUrl\x12.\n\x13stun_server_address\x18\x0c \x01(\tR\x11stunServerAddress\x1a$\n\x08OpenSips\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x1a\xbd\x01\n\x0e\x45nginePriority\x12\x12\n\x04java\x18\x01 \x01(\x03R\x04java\x12\x16\n\x06webrtc\x18\x02 \x01(\x03R\x06webrtc\x12\x0e\n\x02ns\x18\x03 \x01(\x03R\x02ns\x12\x14\n\x05\x66lash\x18\x04 \x01(\x03R\x05\x66lash\x12\x10\n\x03\x61pp\x18\x05 \x01(\x03R\x03\x61pp\x12\x10\n\x03p2p\x18\x06 \x01(\x03R\x03p2p\x12\x1d\n\naccess_num\x18\x07 \x01(\x03R\taccessNum\x12\x16\n\x06native\x18\x08 \x01(\x03R\x06native\x1a\x32\n\x06Server\x12\x10\n\x03sip\x18\x01 \x01(\tR\x03sip\x12\x16\n\x06webrtc\x18\x02 \x01(\tR\x06webrtc2\x82\x01\n\x03\x43\x66g\x12{\n\x11GetWebAgentConfig\x12\x19.api.v0alpha.GetConfigReq\x1a\x15.api.v0alpha.WebAgent\"4\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\'\"\"/api/v0alpha/cfg/getwebagentconfig:\x01*Bh\n\x0f\x63om.api.v0alphaB\x08\x43\x66gProtoP\x01\xa2\x02\x03\x41VX\xaa\x02\x0b\x41pi.V0alpha\xca\x02\x0b\x41pi\\V0alpha\xe2\x02\x17\x41pi\\V0alpha\\GPBMetadata\xea\x02\x0c\x41pi::V0alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v0alpha.cfg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.v0alphaB\010CfgProtoP\001\242\002\003AVX\252\002\013Api.V0alpha\312\002\013Api\\V0alpha\342\002\027Api\\V0alpha\\GPBMetadata\352\002\014Api::V0alpha'
  _globals['_CFG'].methods_by_name['GetWebAgentConfig']._loaded_options = None
  _globals['_CFG'].methods_by_name['GetWebAgentConfig']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\'\"\"/api/v0alpha/cfg/getwebagentconfig:\001*'
  _globals['_GETCONFIGREQ']._serialized_start=93
  _globals['_GETCONFIGREQ']._serialized_end=136
  _globals['_WEBAGENT']._serialized_start=139
  _globals['_WEBAGENT']._serialized_end=928
  _globals['_WEBAGENT_OPENSIPS']._serialized_start=648
  _globals['_WEBAGENT_OPENSIPS']._serialized_end=684
  _globals['_WEBAGENT_ENGINEPRIORITY']._serialized_start=687
  _globals['_WEBAGENT_ENGINEPRIORITY']._serialized_end=876
  _globals['_WEBAGENT_SERVER']._serialized_start=878
  _globals['_WEBAGENT_SERVER']._serialized_end=928
  _globals['_CFG']._serialized_start=931
  _globals['_CFG']._serialized_end=1061
# @@protoc_insertion_point(module_scope)
