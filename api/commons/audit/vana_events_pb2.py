# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/audit/vana_events.proto
# Protobuf Python Version: 6.30.1
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
    1,
    '',
    'api/commons/audit/vana_events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/commons/audit/vana_events.proto\x12\x11\x61pi.commons.audit\x1a\x15\x61pi/commons/acd.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9e\x01\n\rVanaFlagEvent\x12\x1b\n\tflag_name\x18\x01 \x01(\tR\x08\x66lagName\x12\x19\n\x08\x66lag_sid\x18\x02 \x01(\x03R\x07\x66lagSid\x12\x10\n\x03url\x18\x03 \x01(\tR\x03url\x12\'\n\x0fnum_transcripts\x18\x04 \x01(\x03R\x0enumTranscripts\x12\x1a\n\x08priority\x18\x05 \x01(\x05R\x08priority\"\xa4\x01\n\x13VanaFlagReviewEvent\x12\x1b\n\tflag_name\x18\x01 \x01(\tR\x08\x66lagName\x12\x19\n\x08\x66lag_sid\x18\x02 \x01(\x03R\x07\x66lagSid\x12\x10\n\x03url\x18\x03 \x01(\tR\x03url\x12\'\n\x0fnum_transcripts\x18\x04 \x01(\x03R\x0enumTranscripts\x12\x1a\n\x08priority\x18\x05 \x01(\x05R\x08priority\"\x9c\x01\n\x16VanaBillingReportEvent\x12\x39\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x10\n\x03url\x18\x03 \x01(\tR\x03url\"\xb7\x02\n\x14VanaFlagSummaryEvent\x12\x39\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12Z\n\x0e\x66lag_summaries\x18\x03 \x03(\x0b\x32\x33.api.commons.audit.VanaFlagSummaryEvent.FlagSummaryR\rflagSummaries\x1aQ\n\x0b\x46lagSummary\x12%\n\x0etranscript_sid\x18\x01 \x01(\x03R\rtranscriptSid\x12\x1b\n\tflag_sids\x18\x02 \x03(\x03R\x08\x66lagSids\"\x89\x02\n\x19VanaPhraseCorrectionEvent\x12<\n\x0cstart_offset\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0bstartOffset\x12\x38\n\nend_offset\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\tendOffset\x12#\n\roriginal_text\x18\x03 \x01(\tR\x0coriginalText\x12#\n\rproposed_text\x18\x04 \x01(\tR\x0cproposedText\x12\x10\n\x03url\x18\x05 \x01(\tR\x03url\x12\x18\n\x07\x63hannel\x18\x06 \x01(\rR\x07\x63hannel\"\xde\x03\n\x19VanaCreateTranscriptEvent\x12%\n\x0etranscript_sid\x18\x01 \x01(\x03R\rtranscriptSid\x12G\n\x04\x63\x61ll\x18\x02 \x01(\x0b\x32\x31.api.commons.audit.VanaCreateTranscriptEvent.CallH\x00R\x04\x63\x61ll\x12\x44\n\x03sms\x18\x03 \x01(\x0b\x32\x30.api.commons.audit.VanaCreateTranscriptEvent.SmsH\x00R\x03sms\x1a\xcc\x01\n\x04\x43\x61ll\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x02 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12\x36\n\ttalk_time\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08talkTime\x12\x38\n\naudio_time\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\taudioTime\x1a\x30\n\x03Sms\x12)\n\x10\x63onversation_sid\x18\x01 \x01(\x03R\x0f\x63onversationSidB\n\n\x08metadata\"\xe8\x02\n\x18VanaCreateSentimentEvent\x12%\n\x0etranscript_sid\x18\x01 \x01(\x03R\rtranscriptSid\x12\x46\n\x04\x63\x61ll\x18\x02 \x01(\x0b\x32\x30.api.commons.audit.VanaCreateSentimentEvent.CallH\x00R\x04\x63\x61ll\x12\x43\n\x03sms\x18\x03 \x01(\x0b\x32/.api.commons.audit.VanaCreateSentimentEvent.SmsH\x00R\x03sms\x1aZ\n\x04\x43\x61ll\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x02 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x1a\x30\n\x03Sms\x12)\n\x10\x63onversation_sid\x18\x01 \x01(\x03R\x0f\x63onversationSidB\n\n\x08metadata\"\xe2\x02\n\x16VanaCreateSummaryEvent\x12%\n\x0etranscript_sid\x18\x01 \x01(\x03R\rtranscriptSid\x12\x44\n\x04\x63\x61ll\x18\x02 \x01(\x0b\x32..api.commons.audit.VanaCreateSummaryEvent.CallH\x00R\x04\x63\x61ll\x12\x41\n\x03sms\x18\x03 \x01(\x0b\x32-.api.commons.audit.VanaCreateSummaryEvent.SmsH\x00R\x03sms\x1aZ\n\x04\x43\x61ll\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x02 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x1a\x30\n\x03Sms\x12)\n\x10\x63onversation_sid\x18\x01 \x01(\x03R\x0f\x63onversationSidB\n\n\x08metadataB\x8e\x01\n\x15\x63om.api.commons.auditB\x0fVanaEventsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.vana_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\017VanaEventsProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_VANAFLAGEVENT']._serialized_start=147
  _globals['_VANAFLAGEVENT']._serialized_end=305
  _globals['_VANAFLAGREVIEWEVENT']._serialized_start=308
  _globals['_VANAFLAGREVIEWEVENT']._serialized_end=472
  _globals['_VANABILLINGREPORTEVENT']._serialized_start=475
  _globals['_VANABILLINGREPORTEVENT']._serialized_end=631
  _globals['_VANAFLAGSUMMARYEVENT']._serialized_start=634
  _globals['_VANAFLAGSUMMARYEVENT']._serialized_end=945
  _globals['_VANAFLAGSUMMARYEVENT_FLAGSUMMARY']._serialized_start=864
  _globals['_VANAFLAGSUMMARYEVENT_FLAGSUMMARY']._serialized_end=945
  _globals['_VANAPHRASECORRECTIONEVENT']._serialized_start=948
  _globals['_VANAPHRASECORRECTIONEVENT']._serialized_end=1213
  _globals['_VANACREATETRANSCRIPTEVENT']._serialized_start=1216
  _globals['_VANACREATETRANSCRIPTEVENT']._serialized_end=1694
  _globals['_VANACREATETRANSCRIPTEVENT_CALL']._serialized_start=1428
  _globals['_VANACREATETRANSCRIPTEVENT_CALL']._serialized_end=1632
  _globals['_VANACREATETRANSCRIPTEVENT_SMS']._serialized_start=1634
  _globals['_VANACREATETRANSCRIPTEVENT_SMS']._serialized_end=1682
  _globals['_VANACREATESENTIMENTEVENT']._serialized_start=1697
  _globals['_VANACREATESENTIMENTEVENT']._serialized_end=2057
  _globals['_VANACREATESENTIMENTEVENT_CALL']._serialized_start=1428
  _globals['_VANACREATESENTIMENTEVENT_CALL']._serialized_end=1518
  _globals['_VANACREATESENTIMENTEVENT_SMS']._serialized_start=1634
  _globals['_VANACREATESENTIMENTEVENT_SMS']._serialized_end=1682
  _globals['_VANACREATESUMMARYEVENT']._serialized_start=2060
  _globals['_VANACREATESUMMARYEVENT']._serialized_end=2414
  _globals['_VANACREATESUMMARYEVENT_CALL']._serialized_start=1428
  _globals['_VANACREATESUMMARYEVENT_CALL']._serialized_end=1518
  _globals['_VANACREATESUMMARYEVENT_SMS']._serialized_start=1634
  _globals['_VANACREATESUMMARYEVENT_SMS']._serialized_end=1682
# @@protoc_insertion_point(module_scope)
