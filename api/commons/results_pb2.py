# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/results.proto
# Protobuf Python Version: 5.28.3
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
    3,
    '',
    'api/commons/results.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/commons/results.proto\x12\x0b\x61pi.commons*\xda\r\n\nCallResult\x12\x17\n\x13\x43\x41LL_RESULT_UNKNOWN\x10\x00\x12\x18\n\x13\x43\x41LL_RESULT_PENDING\x10\xe8\x07\x12\x19\n\x14\x43\x41LL_RESULT_ANSWERED\x10\xd0\x0f\x12\"\n\x1d\x43\x41LL_RESULT_ANSWERED_LINKCALL\x10\xb4\x10\x12,\n\'CALL_RESULT_ANSWERED_LINKCALL_ABANDONED\x10\xbe\x10\x12-\n(CALL_RESULT_ANSWERED_LINKCALL_AGENT_TALK\x10\xc8\x10\x12,\n\'CALL_RESULT_ANSWERED_LINKCALL_SUSPENDED\x10\xd2\x10\x12\x34\n/CALL_RESULT_ANSWERED_LINKCALL_SUSPENDED_TIMEOUT\x10\xdc\x10\x12=\n8CALL_RESULT_ANSWERED_LINKCALL_SUSPENDED_INBOUND_OVERRIDE\x10\xe6\x10\x12\x34\n/CALL_RESULT_ANSWERED_LINKCALL_SUSPENDED_RESUMED\x10\xf0\x10\x12 \n\x1b\x43\x41LL_RESULT_ANSWERED_HANGUP\x10\x98\x11\x12#\n\x1e\x43\x41LL_RESULT_ANSWERED_VOICEMAIL\x10\xfc\x11\x12\x18\n\x13\x43\x41LL_RESULT_MACHINE\x10\xb8\x17\x12\"\n\x1d\x43\x41LL_RESULT_MACHINE_DELIVERED\x10\x9c\x18\x12\x1f\n\x1a\x43\x41LL_RESULT_MACHINE_HANGUP\x10\x80\x19\x12\x1f\n\x1a\x43\x41LL_RESULT_MACHINE_FAILED\x10\xe4\x19\x12\x14\n\x0f\x43\x41LL_RESULT_FAX\x10\xa0\x1f\x12\x1e\n\x19\x43\x41LL_RESULT_FAX_DELIVERED\x10\x84 \x12\x15\n\x10\x43\x41LL_RESULT_BUSY\x10\x88\'\x12\x1a\n\x15\x43\x41LL_RESULT_NO_ANSWER\x10\xf0.\x12\x18\n\x13\x43\x41LL_RESULT_INVALID\x10\xd8\x36\x12*\n%CALL_RESULT_INVALID_INCOMPLETE_NUMBER\x10\xbc\x37\x12\'\n\"CALL_RESULT_INVALID_UNKNOWN_PREFIX\x10\xa0\x38\x12+\n&CALL_RESULT_INVALID_UNKNOWN_PREFIX_NPA\x10\xaa\x38\x12.\n)CALL_RESULT_INVALID_UNKNOWN_PREFIX_NPANXX\x10\xb4\x38\x12\x30\n+CALL_RESULT_INVALID_PREFIX_NPANXX_NOT_FOUND\x10\xbe\x38\x12!\n\x1c\x43\x41LL_RESULT_INVALID_NO_ROUTE\x10\x84\x39\x12%\n CALL_RESULT_INVALID_DISCONNECTED\x10\xe8\x39\x12/\n*CALL_RESULT_INVALID_DISCONNECTED_SKIPTRACE\x10\xf2\x39\x12\x17\n\x12\x43\x41LL_RESULT_FAILED\x10\xc0>\x12 \n\x1b\x43\x41LL_RESULT_FAILED_NO_LINES\x10\xa4?\x12%\n CALL_RESULT_FAILED_CIRCUITS_BUSY\x10\x88@\x12\x1f\n\x1a\x43\x41LL_RESULT_FAILED_REFUSED\x10\xec@\x12%\n CALL_RESULT_FAILED_REFUSED_LEGAL\x10\xf6@\x12)\n$CALL_RESULT_FAILED_REFUSED_TECHNICAL\x10\x80\x41\x12&\n!CALL_RESULT_FAILED_INTERNAL_ERROR\x10\x8a\x41\x12\x31\n,CALL_RESULT_FAILED_REFUSED_RETRIES_EXHAUSTED\x10\x94\x41\x12%\n CALL_RESULT_FAILED_REFUSED_BLOCK\x10\x9e\x41\x12\x19\n\x14\x43\x41LL_RESULT_CANCELED\x10\xa8\x46\x12\"\n\x1d\x43\x41LL_RESULT_CANCELED_TIMEZONE\x10\x8cG\x12!\n\x1c\x43\x41LL_RESULT_CANCELED_TIMEOUT\x10\xf0G\x12\x1e\n\x19\x43\x41LL_RESULT_CANCELED_DNCL\x10\xd4H\x12\'\n\"CALL_RESULT_CANCELED_CELLULAR_DNCL\x10\xdeH\x12\'\n\"CALL_RESULT_CANCELED_DNCL_ZIP_CODE\x10\xe8H\x12#\n\x1e\x43\x41LL_RESULT_CANCELED_MAX_RETRY\x10\xb8I\x12+\n&CALL_RESULT_CANCELED_INCOMPLETE_NUMBER\x10\x9cJBl\n\x0f\x63om.api.commonsB\x0cResultsProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.results_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\014ResultsProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_CALLRESULT']._serialized_start=43
  _globals['_CALLRESULT']._serialized_end=1797
# @@protoc_insertion_point(module_scope)
