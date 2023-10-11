# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/cfg/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61pi/v1alpha1/cfg/service.proto\x12\x10\x61pi.v1alpha1.cfg\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\"3\n\x14GetWebAgentConfigReq\x12\x1b\n\tregion_id\x18\x01 \x01(\tR\x08regionId\"\xa4\x06\n\x08WebAgent\x12@\n\topen_sips\x18\x01 \x01(\x0b\x32#.api.v1alpha1.cfg.WebAgent.OpenSipsR\x08openSips\x12R\n\x0f\x65ngine_priority\x18\x02 \x01(\x0b\x32).api.v1alpha1.cfg.WebAgent.EnginePriorityR\x0e\x65nginePriority\x12\x1b\n\tlog_level\x18\x03 \x01(\x03R\x08logLevel\x12\x19\n\x08use_stun\x18\x04 \x01(\x03R\x07useStun\x12\"\n\ruse_fast_stun\x18\x05 \x01(\x03R\x0buseFastStun\x12 \n\x0cuse_fast_ice\x18\x06 \x01(\x03R\nuseFastIce\x12\x1f\n\x0bice_timeout\x18\x07 \x01(\x03R\niceTimeout\x12&\n\x0fset_final_codec\x18\x08 \x01(\x03R\rsetFinalCodec\x12\x1b\n\tuse_rport\x18\t \x01(\x03R\x08useRport\x12\x39\n\x06server\x18\n \x01(\x0b\x32!.api.v1alpha1.cfg.WebAgent.ServerR\x06server\x12\x19\n\x08\x62\x61se_url\x18\x0b \x01(\tR\x07\x62\x61seUrl\x12.\n\x13stun_server_address\x18\x0c \x01(\tR\x11stunServerAddress\x1a$\n\x08OpenSips\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\x1a\xbd\x01\n\x0e\x45nginePriority\x12\x12\n\x04java\x18\x01 \x01(\x03R\x04java\x12\x16\n\x06webrtc\x18\x02 \x01(\x03R\x06webrtc\x12\x0e\n\x02ns\x18\x03 \x01(\x03R\x02ns\x12\x14\n\x05\x66lash\x18\x04 \x01(\x03R\x05\x66lash\x12\x10\n\x03\x61pp\x18\x05 \x01(\x03R\x03\x61pp\x12\x10\n\x03p2p\x18\x06 \x01(\x03R\x03p2p\x12\x1d\n\naccess_num\x18\x07 \x01(\x03R\taccessNum\x12\x16\n\x06native\x18\x08 \x01(\x03R\x06native\x1a\x32\n\x06Server\x12\x10\n\x03sip\x18\x01 \x01(\tR\x03sip\x12\x16\n\x06webrtc\x18\x02 \x01(\tR\x06webrtc2\x96\x01\n\x03\x43\x66g\x12\x8e\x01\n\x11GetWebAgentConfig\x12&.api.v1alpha1.cfg.GetWebAgentConfigReq\x1a\x1a.api.v1alpha1.cfg.WebAgent\"5\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02(\"#/api/v1alpha1/cfg/getwebagentconfig:\x01*B\x86\x01\n\x14\x63om.api.v1alpha1.cfgB\x0cServiceProtoP\x01\xa2\x02\x03\x41VC\xaa\x02\x10\x41pi.V1alpha1.Cfg\xca\x02\x10\x41pi\\V1alpha1\\Cfg\xe2\x02\x1c\x41pi\\V1alpha1\\Cfg\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Cfgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.cfg.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.cfgB\014ServiceProtoP\001\242\002\003AVC\252\002\020Api.V1alpha1.Cfg\312\002\020Api\\V1alpha1\\Cfg\342\002\034Api\\V1alpha1\\Cfg\\GPBMetadata\352\002\022Api::V1alpha1::Cfg'
  _globals['_CFG'].methods_by_name['GetWebAgentConfig']._options = None
  _globals['_CFG'].methods_by_name['GetWebAgentConfig']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002(\"#/api/v1alpha1/cfg/getwebagentconfig:\001*'
  _globals['_GETWEBAGENTCONFIGREQ']._serialized_start=107
  _globals['_GETWEBAGENTCONFIGREQ']._serialized_end=158
  _globals['_WEBAGENT']._serialized_start=161
  _globals['_WEBAGENT']._serialized_end=965
  _globals['_WEBAGENT_OPENSIPS']._serialized_start=685
  _globals['_WEBAGENT_OPENSIPS']._serialized_end=721
  _globals['_WEBAGENT_ENGINEPRIORITY']._serialized_start=724
  _globals['_WEBAGENT_ENGINEPRIORITY']._serialized_end=913
  _globals['_WEBAGENT_SERVER']._serialized_start=915
  _globals['_WEBAGENT_SERVER']._serialized_end=965
  _globals['_CFG']._serialized_start=968
  _globals['_CFG']._serialized_end=1118
# @@protoc_insertion_point(module_scope)
