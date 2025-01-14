# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: wfo/vanalytics/v2/service.proto
# Protobuf Python Version: 5.29.3
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
    3,
    '',
    'wfo/vanalytics/v2/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from wfo.vanalytics.v2 import correction_pb2 as wfo_dot_vanalytics_dot_v2_dot_correction__pb2
from wfo.vanalytics.v2 import filter_pb2 as wfo_dot_vanalytics_dot_v2_dot_filter__pb2
from wfo.vanalytics.v2 import flag_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__pb2
from wfo.vanalytics.v2 import flag_filter_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__filter__pb2
from wfo.vanalytics.v2 import flag_review_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__review__pb2
from wfo.vanalytics.v2 import flag_snapshot_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__snapshot__pb2
from wfo.vanalytics.v2 import flag_transcript_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__transcript__pb2
from wfo.vanalytics.v2 import flag_transcript_filter_pb2 as wfo_dot_vanalytics_dot_v2_dot_flag__transcript__filter__pb2
from wfo.vanalytics.v2 import transcript_pb2 as wfo_dot_vanalytics_dot_v2_dot_transcript__pb2
from wfo.vanalytics.v2 import transcript_summary_pb2 as wfo_dot_vanalytics_dot_v2_dot_transcript__summary__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwfo/vanalytics/v2/service.proto\x12\x11wfo.vanalytics.v2\x1a\x17\x61nnotations/authz.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"wfo/vanalytics/v2/correction.proto\x1a\x1ewfo/vanalytics/v2/filter.proto\x1a\x1cwfo/vanalytics/v2/flag.proto\x1a#wfo/vanalytics/v2/flag_filter.proto\x1a#wfo/vanalytics/v2/flag_review.proto\x1a%wfo/vanalytics/v2/flag_snapshot.proto\x1a\'wfo/vanalytics/v2/flag_transcript.proto\x1a.wfo/vanalytics/v2/flag_transcript_filter.proto\x1a\"wfo/vanalytics/v2/transcript.proto\x1a*wfo/vanalytics/v2/transcript_summary.proto\"r\n\x0c\x41uditRequest\x12\x30\n\x05since\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05since\x12\x30\n\x05until\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05until\"\xc4\x01\n\rAuditResponse\x12\x1d\n\naudio_time\x18\x01 \x01(\x01R\taudioTime\x12*\n\x11\x62illed_audio_time\x18\x02 \x01(\x01R\x0f\x62illedAudioTime\x12\x39\n\nlast_usage\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tlastUsage\x12-\n\x12\x62illed_transcripts\x18\x04 \x01(\x03R\x11\x62illedTranscripts\"S\n\x16GetRecordingUrlRequest\x12%\n\x0etranscript_sid\x18\x02 \x01(\x03R\rtranscriptSid\x12\x12\n\x04kind\x18\x04 \x01(\tR\x04kind\"+\n\x17GetRecordingUrlResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"T\n\x16ListBillingSpanRequest\x12\x1b\n\tpage_size\x18\x01 \x01(\rR\x08pageSize\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken\"w\n\x17ListBillingSpanResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12\x34\n\x05spans\x18\x02 \x03(\x0b\x32\x1e.wfo.vanalytics.v2.BillingSpanR\x05spans\"\xbf\x01\n\x0b\x42illingSpan\x12\x14\n\x05\x63\x61lls\x18\x01 \x01(\x03R\x05\x63\x61lls\x12\x14\n\x05hours\x18\x02 \x01(\x03R\x05hours\x12\x12\n\x04\x63ost\x18\x03 \x01(\x01R\x04\x63ost\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime2\x9e\'\n\nVanalytics\x12\x84\x01\n\x05\x41udit\x12\x1f.wfo.vanalytics.v2.AuditRequest\x1a .wfo.vanalytics.v2.AuditResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02(\"#/wfo/vanalytics/v2/vanalytics/audit:\x01*\x12\xa6\x01\n\x0fGetRecordingUrl\x12).wfo.vanalytics.v2.GetRecordingUrlRequest\x1a*.wfo.vanalytics.v2.GetRecordingUrlResponse\"<\xba\xb8\x91\x02\n\n\x03\x08\xf4\x03\n\x03\x08\xd4\x02\x82\xd3\xe4\x93\x02\'\"\"/wfo/vanalytics/v2/getrecordingurl:\x01*\x12\xa1\x01\n\x0fListBillingSpan\x12).wfo.vanalytics.v2.ListBillingSpanRequest\x1a*.wfo.vanalytics.v2.ListBillingSpanResponse\"7\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\'\"\"/wfo/vanalytics/v2/listbillingspan:\x01*\x12\xae\x01\n\x11SearchTranscripts\x12+.wfo.vanalytics.v2.SearchTranscriptsRequest\x1a,.wfo.vanalytics.v2.SearchTranscriptsResponse\">\xba\xb8\x91\x02\n\n\x03\x08\xf4\x03\n\x03\x08\xd4\x02\x82\xd3\xe4\x93\x02)\"$/wfo/vanalytics/v2/searchtranscripts:\x01*\x12\xb9\x01\n\x15\x42ulkDeleteTranscripts\x12/.wfo.vanalytics.v2.BulkDeleteTranscriptsRequest\x1a\x30.wfo.vanalytics.v2.BulkDeleteTranscriptsResponse\"=\xba\xb8\x91\x02\x05\n\x03\x08\xfa\x03\x82\xd3\xe4\x93\x02-\"(/wfo/vanalytics/v2/bulkdeletetranscripts:\x01*\x12\xbd\x01\n\x16\x42ulkRestoreTranscripts\x12\x30.wfo.vanalytics.v2.BulkRestoreTranscriptsRequest\x1a\x31.wfo.vanalytics.v2.BulkRestoreTranscriptsResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\xfa\x03\x82\xd3\xe4\x93\x02.\")/wfo/vanalytics/v2/bulkrestoretranscripts:\x01*\x12\xc5\x01\n\x18ListTranscriptGroupNames\x12\x32.wfo.vanalytics.v2.ListTranscriptGroupNamesRequest\x1a\x33.wfo.vanalytics.v2.ListTranscriptGroupNamesResponse\"@\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x30\"+/wfo/vanalytics/v2/listtranscriptgroupnames:\x01*\x12\xc1\x01\n\x17ListAgentResponseValues\x12\x31.wfo.vanalytics.v2.ListAgentResponseValuesRequest\x1a\x32.wfo.vanalytics.v2.ListAgentResponseValuesResponse\"?\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02/\"*/wfo/vanalytics/v2/listagentresponsevalues:\x01*\x12\xb5\x01\n\x14GetTranscriptSummary\x12..wfo.vanalytics.v2.GetTranscriptSummaryRequest\x1a/.wfo.vanalytics.v2.GetTranscriptSummaryResponse\"<\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02,\"\'/wfo/vanalytics/v2/gettranscriptsummary:\x01*\x12\x87\x01\n\x0c\x43reateFilter\x12&.wfo.vanalytics.v2.CreateFilterRequest\x1a\x19.wfo.vanalytics.v2.Filter\"4\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02$\"\x1f/wfo/vanalytics/v2/createfilter:\x01*\x12\x91\x01\n\x0bListFilters\x12%.wfo.vanalytics.v2.ListFiltersRequest\x1a&.wfo.vanalytics.v2.ListFiltersResponse\"3\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02#\"\x1e/wfo/vanalytics/v2/listfilters:\x01*\x12\x87\x01\n\x0cUpdateFilter\x12&.wfo.vanalytics.v2.UpdateFilterRequest\x1a\x19.wfo.vanalytics.v2.Filter\"4\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02$\"\x1f/wfo/vanalytics/v2/updatefilter:\x01*\x12\x95\x01\n\x0c\x44\x65leteFilter\x12&.wfo.vanalytics.v2.DeleteFilterRequest\x1a\'.wfo.vanalytics.v2.DeleteFilterResponse\"4\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02$\"\x1f/wfo/vanalytics/v2/deletefilter:\x01*\x12~\n\tGetFilter\x12#.wfo.vanalytics.v2.GetFilterRequest\x1a\x19.wfo.vanalytics.v2.Filter\"1\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02!\"\x1c/wfo/vanalytics/v2/getfilter:\x01*\x12\xc9\x01\n\x19ListFlagTranscriptFilters\x12\x33.wfo.vanalytics.v2.ListFlagTranscriptFiltersRequest\x1a\x34.wfo.vanalytics.v2.ListFlagTranscriptFiltersResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x31\",/wfo/vanalytics/v2/listflagtranscriptfilters:\x01*\x12\xa1\x01\n\x0fListFlagFilters\x12).wfo.vanalytics.v2.ListFlagFiltersRequest\x1a*.wfo.vanalytics.v2.ListFlagFiltersResponse\"7\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\'\"\"/wfo/vanalytics/v2/listflagfilters:\x01*\x12v\n\x07GetFlag\x12!.wfo.vanalytics.v2.GetFlagRequest\x1a\x17.wfo.vanalytics.v2.Flag\"/\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x1f\"\x1a/wfo/vanalytics/v2/getflag:\x01*\x12\x7f\n\nCreateFlag\x12$.wfo.vanalytics.v2.CreateFlagRequest\x1a\x17.wfo.vanalytics.v2.Flag\"2\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\"\"\x1d/wfo/vanalytics/v2/createflag:\x01*\x12\x89\x01\n\tListFlags\x12#.wfo.vanalytics.v2.ListFlagsRequest\x1a$.wfo.vanalytics.v2.ListFlagsResponse\"1\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02!\"\x1c/wfo/vanalytics/v2/listflags:\x01*\x12\x7f\n\nUpdateFlag\x12$.wfo.vanalytics.v2.UpdateFlagRequest\x1a\x17.wfo.vanalytics.v2.Flag\"2\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\"\"\x1d/wfo/vanalytics/v2/updateflag:\x01*\x12\x8d\x01\n\nDeleteFlag\x12$.wfo.vanalytics.v2.DeleteFlagRequest\x1a%.wfo.vanalytics.v2.DeleteFlagResponse\"2\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\"\"\x1d/wfo/vanalytics/v2/deleteflag:\x01*\x12\x97\x01\n\x10\x43reateFlagReview\x12*.wfo.vanalytics.v2.CreateFlagReviewRequest\x1a\x1d.wfo.vanalytics.v2.FlagReview\"8\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02(\"#/wfo/vanalytics/v2/createflagreview:\x01*\x12\xb5\x01\n\x14\x42ulkCreateFlagReview\x12..wfo.vanalytics.v2.BulkCreateFlagReviewRequest\x1a/.wfo.vanalytics.v2.BulkCreateFlagReviewResponse\"<\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02,\"\'/wfo/vanalytics/v2/bulkcreateflagreview:\x01*\x12\xa1\x01\n\x0fListFlagReviews\x12).wfo.vanalytics.v2.ListFlagReviewsRequest\x1a*.wfo.vanalytics.v2.ListFlagReviewsResponse\"7\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\'\"\"/wfo/vanalytics/v2/listflagreviews:\x01*\x12\xb5\x01\n\x14\x43reateFlagTranscript\x12..wfo.vanalytics.v2.CreateFlagTranscriptRequest\x1a/.wfo.vanalytics.v2.CreateFlagTranscriptResponse\"<\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02,\"\'/wfo/vanalytics/v2/createflagtranscript:\x01*\x12\xa9\x01\n\x11ListFlagSnapshots\x12+.wfo.vanalytics.v2.ListFlagSnapshotsRequest\x1a,.wfo.vanalytics.v2.ListFlagSnapshotsResponse\"9\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02)\"$/wfo/vanalytics/v2/listflagsnapshots:\x01*\x12\xa5\x01\n\x10\x43reateCorrection\x12*.wfo.vanalytics.v2.CreateCorrectionRequest\x1a+.wfo.vanalytics.v2.CreateCorrectionResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02(\"#/wfo/vanalytics/v2/createcorrection:\x01*\x12\x8e\x01\n\rGetCorrection\x12\'.wfo.vanalytics.v2.GetCorrectionRequest\x1a\x1d.wfo.vanalytics.v2.Correction\"5\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02%\" /wfo/vanalytics/v2/getcorrection:\x01*\x12\xa5\x01\n\x10\x44\x65leteCorrection\x12*.wfo.vanalytics.v2.DeleteCorrectionRequest\x1a+.wfo.vanalytics.v2.DeleteCorrectionResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02(\"#/wfo/vanalytics/v2/deletecorrection:\x01*\x12\xa1\x01\n\x0fListCorrections\x12).wfo.vanalytics.v2.ListCorrectionsRequest\x1a*.wfo.vanalytics.v2.ListCorrectionsResponse\"7\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\'\"\"/wfo/vanalytics/v2/listcorrections:\x01*\x12\xa5\x01\n\x10UpdateCorrection\x12*.wfo.vanalytics.v2.UpdateCorrectionRequest\x1a+.wfo.vanalytics.v2.UpdateCorrectionResponse\"8\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02(\"#/wfo/vanalytics/v2/updatecorrection:\x01*B\x8b\x01\n\x15\x63om.wfo.vanalytics.v2B\x0cServiceProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\014ServiceProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_VANALYTICS'].methods_by_name['Audit']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['Audit']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002(\"#/wfo/vanalytics/v2/vanalytics/audit:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetRecordingUrl']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetRecordingUrl']._serialized_options = b'\272\270\221\002\n\n\003\010\364\003\n\003\010\324\002\202\323\344\223\002\'\"\"/wfo/vanalytics/v2/getrecordingurl:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListBillingSpan']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListBillingSpan']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002\'\"\"/wfo/vanalytics/v2/listbillingspan:\001*'
  _globals['_VANALYTICS'].methods_by_name['SearchTranscripts']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['SearchTranscripts']._serialized_options = b'\272\270\221\002\n\n\003\010\364\003\n\003\010\324\002\202\323\344\223\002)\"$/wfo/vanalytics/v2/searchtranscripts:\001*'
  _globals['_VANALYTICS'].methods_by_name['BulkDeleteTranscripts']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['BulkDeleteTranscripts']._serialized_options = b'\272\270\221\002\005\n\003\010\372\003\202\323\344\223\002-\"(/wfo/vanalytics/v2/bulkdeletetranscripts:\001*'
  _globals['_VANALYTICS'].methods_by_name['BulkRestoreTranscripts']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['BulkRestoreTranscripts']._serialized_options = b'\272\270\221\002\005\n\003\010\372\003\202\323\344\223\002.\")/wfo/vanalytics/v2/bulkrestoretranscripts:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListTranscriptGroupNames']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListTranscriptGroupNames']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0020\"+/wfo/vanalytics/v2/listtranscriptgroupnames:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListAgentResponseValues']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListAgentResponseValues']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002/\"*/wfo/vanalytics/v2/listagentresponsevalues:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetTranscriptSummary']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetTranscriptSummary']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002,\"\'/wfo/vanalytics/v2/gettranscriptsummary:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002$\"\037/wfo/vanalytics/v2/createfilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFilters']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFilters']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002#\"\036/wfo/vanalytics/v2/listfilters:\001*'
  _globals['_VANALYTICS'].methods_by_name['UpdateFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['UpdateFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002$\"\037/wfo/vanalytics/v2/updatefilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['DeleteFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['DeleteFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002$\"\037/wfo/vanalytics/v2/deletefilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002!\"\034/wfo/vanalytics/v2/getfilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlagTranscriptFilters']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlagTranscriptFilters']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0021\",/wfo/vanalytics/v2/listflagtranscriptfilters:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlagFilters']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlagFilters']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002\'\"\"/wfo/vanalytics/v2/listflagfilters:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetFlag']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetFlag']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002\037\"\032/wfo/vanalytics/v2/getflag:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateFlag']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateFlag']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002\"\"\035/wfo/vanalytics/v2/createflag:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlags']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlags']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002!\"\034/wfo/vanalytics/v2/listflags:\001*'
  _globals['_VANALYTICS'].methods_by_name['UpdateFlag']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['UpdateFlag']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002\"\"\035/wfo/vanalytics/v2/updateflag:\001*'
  _globals['_VANALYTICS'].methods_by_name['DeleteFlag']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['DeleteFlag']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002\"\"\035/wfo/vanalytics/v2/deleteflag:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateFlagReview']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateFlagReview']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002(\"#/wfo/vanalytics/v2/createflagreview:\001*'
  _globals['_VANALYTICS'].methods_by_name['BulkCreateFlagReview']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['BulkCreateFlagReview']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002,\"\'/wfo/vanalytics/v2/bulkcreateflagreview:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlagReviews']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlagReviews']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002\'\"\"/wfo/vanalytics/v2/listflagreviews:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateFlagTranscript']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateFlagTranscript']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002,\"\'/wfo/vanalytics/v2/createflagtranscript:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlagSnapshots']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlagSnapshots']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002)\"$/wfo/vanalytics/v2/listflagsnapshots:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateCorrection']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateCorrection']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002(\"#/wfo/vanalytics/v2/createcorrection:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetCorrection']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetCorrection']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002%\" /wfo/vanalytics/v2/getcorrection:\001*'
  _globals['_VANALYTICS'].methods_by_name['DeleteCorrection']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['DeleteCorrection']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002(\"#/wfo/vanalytics/v2/deletecorrection:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListCorrections']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListCorrections']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002\'\"\"/wfo/vanalytics/v2/listcorrections:\001*'
  _globals['_VANALYTICS'].methods_by_name['UpdateCorrection']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['UpdateCorrection']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002(\"#/wfo/vanalytics/v2/updatecorrection:\001*'
  _globals['_AUDITREQUEST']._serialized_start=522
  _globals['_AUDITREQUEST']._serialized_end=636
  _globals['_AUDITRESPONSE']._serialized_start=639
  _globals['_AUDITRESPONSE']._serialized_end=835
  _globals['_GETRECORDINGURLREQUEST']._serialized_start=837
  _globals['_GETRECORDINGURLREQUEST']._serialized_end=920
  _globals['_GETRECORDINGURLRESPONSE']._serialized_start=922
  _globals['_GETRECORDINGURLRESPONSE']._serialized_end=965
  _globals['_LISTBILLINGSPANREQUEST']._serialized_start=967
  _globals['_LISTBILLINGSPANREQUEST']._serialized_end=1051
  _globals['_LISTBILLINGSPANRESPONSE']._serialized_start=1053
  _globals['_LISTBILLINGSPANRESPONSE']._serialized_end=1172
  _globals['_BILLINGSPAN']._serialized_start=1175
  _globals['_BILLINGSPAN']._serialized_end=1366
  _globals['_VANALYTICS']._serialized_start=1369
  _globals['_VANALYTICS']._serialized_end=6391
# @@protoc_insertion_point(module_scope)
