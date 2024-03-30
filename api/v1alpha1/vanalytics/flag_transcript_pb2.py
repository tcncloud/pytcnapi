# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/vanalytics/flag_transcript.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v1alpha1.vanalytics import flag_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_flag__pb2
from api.v1alpha1.vanalytics import transcript_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_transcript__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/v1alpha1/vanalytics/flag_transcript.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a\"api/v1alpha1/vanalytics/flag.proto\x1a(api/v1alpha1/vanalytics/transcript.proto\"y\n\x1b\x43reateFlagTranscriptRequest\x12\'\n\x0ftranscript_sids\x18\x01 \x03(\x03R\x0etranscriptSids\x12\x31\n\x04\x66lag\x18\x02 \x01(\x0b\x32\x1d.api.v1alpha1.vanalytics.FlagR\x04\x66lag\"\x1e\n\x1c\x43reateFlagTranscriptResponse\"\xcb\x06\n\x1cSearchFlagTranscriptsRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x1d\n\npage_token\x18\x03 \x01(\tR\tpageToken\x12X\n\x08\x66lag_sid\x18\x05 \x01(\x0b\x32=.api.v1alpha1.vanalytics.SearchFlagTranscriptsRequest.FlagSidR\x07\x66lagSid\x12W\n\x12\x66lag_review_status\x18\x06 \x01(\x0e\x32).api.v1alpha1.vanalytics.FlagReviewStatusR\x10\x66lagReviewStatus\x12k\n\x0fnotify_group_id\x18\x07 \x01(\x0b\x32\x43.api.v1alpha1.vanalytics.SearchFlagTranscriptsRequest.NotifyGroupIdR\rnotifyGroupId\x12k\n\x0freview_group_id\x18\x08 \x01(\x0b\x32\x43.api.v1alpha1.vanalytics.SearchFlagTranscriptsRequest.ReviewGroupIdR\rreviewGroupId\x12\x30\n\x14start_transcript_sid\x18\n \x01(\x03R\x12startTranscriptSid\x12,\n\x12\x65nd_transcript_sid\x18\x0b \x01(\x03R\x10\x65ndTranscriptSid\x12\x19\n\x08order_by\x18\x0c \x01(\tR\x07orderBy\x1a\x37\n\x07\x46lagSid\x12\x16\n\x06\x66ilter\x18\x01 \x03(\x03R\x06\x66ilter\x12\x14\n\x05match\x18\x02 \x01(\x05R\x05match\x1aV\n\rNotifyGroupId\x12\x17\n\x07is_null\x18\x01 \x01(\x08R\x06isNull\x12\x16\n\x06\x66ilter\x18\x02 \x03(\tR\x06\x66ilter\x12\x14\n\x05match\x18\x03 \x01(\x05R\x05match\x1aV\n\rReviewGroupId\x12\x17\n\x07is_null\x18\x01 \x01(\x08R\x06isNull\x12\x16\n\x06\x66ilter\x18\x02 \x03(\tR\x06\x66ilter\x12\x14\n\x05match\x18\x03 \x01(\x05R\x05match\"\xe8\x03\n\x1dSearchFlagTranscriptsResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12N\n\x04hits\x18\x02 \x03(\x0b\x32:.api.v1alpha1.vanalytics.SearchFlagTranscriptsResponse.HitR\x04hits\x12\x14\n\x05total\x18\x03 \x01(\x04R\x05total\x1a\xb8\x02\n\x03Hit\x12\x43\n\ntranscript\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.TranscriptR\ntranscript\x12,\n\x12\x66lag_snapshot_sids\x18\x02 \x03(\x03R\x10\x66lagSnapshotSids\x12\x64\n\x08reviewed\x18\x03 \x03(\x0b\x32H.api.v1alpha1.vanalytics.SearchFlagTranscriptsResponse.Hit.ReviewedEntryR\x08reviewed\x12\x1b\n\tflag_sids\x18\x04 \x03(\x03R\x08\x66lagSids\x1a;\n\rReviewedEntry\x12\x10\n\x03key\x18\x01 \x01(\x03R\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01*9\n\x10\x46lagReviewStatus\x12\x07\n\x03\x41NY\x10\x00\x12\x08\n\x04TODO\x10\x01\x12\x08\n\x04\x44ONE\x10\x02\x12\x08\n\x04NONE\x10\x03\x42\xb0\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x13\x46lagTranscriptProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.flag_transcript_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\023FlagTranscriptProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_SEARCHFLAGTRANSCRIPTSRESPONSE_HIT_REVIEWEDENTRY']._loaded_options = None
  _globals['_SEARCHFLAGTRANSCRIPTSRESPONSE_HIT_REVIEWEDENTRY']._serialized_options = b'8\001'
  _globals['_FLAGREVIEWSTATUS']._serialized_start=1644
  _globals['_FLAGREVIEWSTATUS']._serialized_end=1701
  _globals['_CREATEFLAGTRANSCRIPTREQUEST']._serialized_start=152
  _globals['_CREATEFLAGTRANSCRIPTREQUEST']._serialized_end=273
  _globals['_CREATEFLAGTRANSCRIPTRESPONSE']._serialized_start=275
  _globals['_CREATEFLAGTRANSCRIPTRESPONSE']._serialized_end=305
  _globals['_SEARCHFLAGTRANSCRIPTSREQUEST']._serialized_start=308
  _globals['_SEARCHFLAGTRANSCRIPTSREQUEST']._serialized_end=1151
  _globals['_SEARCHFLAGTRANSCRIPTSREQUEST_FLAGSID']._serialized_start=920
  _globals['_SEARCHFLAGTRANSCRIPTSREQUEST_FLAGSID']._serialized_end=975
  _globals['_SEARCHFLAGTRANSCRIPTSREQUEST_NOTIFYGROUPID']._serialized_start=977
  _globals['_SEARCHFLAGTRANSCRIPTSREQUEST_NOTIFYGROUPID']._serialized_end=1063
  _globals['_SEARCHFLAGTRANSCRIPTSREQUEST_REVIEWGROUPID']._serialized_start=1065
  _globals['_SEARCHFLAGTRANSCRIPTSREQUEST_REVIEWGROUPID']._serialized_end=1151
  _globals['_SEARCHFLAGTRANSCRIPTSRESPONSE']._serialized_start=1154
  _globals['_SEARCHFLAGTRANSCRIPTSRESPONSE']._serialized_end=1642
  _globals['_SEARCHFLAGTRANSCRIPTSRESPONSE_HIT']._serialized_start=1330
  _globals['_SEARCHFLAGTRANSCRIPTSRESPONSE_HIT']._serialized_end=1642
  _globals['_SEARCHFLAGTRANSCRIPTSRESPONSE_HIT_REVIEWEDENTRY']._serialized_start=1583
  _globals['_SEARCHFLAGTRANSCRIPTSRESPONSE_HIT_REVIEWEDENTRY']._serialized_end=1642
# @@protoc_insertion_point(module_scope)
