# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wfo/vanalytics/v2/flag_transcript.proto
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
    'wfo/vanalytics/v2/flag_transcript.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wfo.vanalytics.v2 import flag_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__pb2
from wfo.vanalytics.v2 import transcript_pb2 as wfo_dot_vanalytics_dot_v2_dot_transcript__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'wfo/vanalytics/v2/flag_transcript.proto\x12\x11wfo.vanalytics.v2\x1a\x1cwfo/vanalytics/v2/flag.proto\x1a\"wfo/vanalytics/v2/transcript.proto\"s\n\x1b\x43reateFlagTranscriptRequest\x12\'\n\x0ftranscript_sids\x18\x01 \x03(\x03R\x0etranscriptSids\x12+\n\x04\x66lag\x18\x02 \x01(\x0b\x32\x17.wfo.vanalytics.v2.FlagR\x04\x66lag\"\x1e\n\x1c\x43reateFlagTranscriptResponseB\x92\x01\n\x15\x63om.wfo.vanalytics.v2B\x13\x46lagTranscriptProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.flag_transcript_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\023FlagTranscriptProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_CREATEFLAGTRANSCRIPTREQUEST']._serialized_start=128
  _globals['_CREATEFLAGTRANSCRIPTREQUEST']._serialized_end=243
  _globals['_CREATEFLAGTRANSCRIPTRESPONSE']._serialized_start=245
  _globals['_CREATEFLAGTRANSCRIPTRESPONSE']._serialized_end=275
# @@protoc_insertion_point(module_scope)
