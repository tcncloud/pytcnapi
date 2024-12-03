# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/vanalytics/service.proto
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
    'api/v1alpha1/vanalytics/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.vanalytics import correction_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_correction__pb2
from api.v1alpha1.vanalytics import filter_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_filter__pb2
from api.v1alpha1.vanalytics import flag_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_flag__pb2
from api.v1alpha1.vanalytics import flag_filter_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_flag__filter__pb2
from api.v1alpha1.vanalytics import flag_review_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_flag__review__pb2
from api.v1alpha1.vanalytics import flag_snapshot_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_flag__snapshot__pb2
from api.v1alpha1.vanalytics import flag_transcript_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_flag__transcript__pb2
from api.v1alpha1.vanalytics import flag_transcript_filter_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_flag__transcript__filter__pb2
from api.v1alpha1.vanalytics import transcript_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_transcript__pb2
from api.v1alpha1.vanalytics import transcript_summary_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_transcript__summary__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%api/v1alpha1/vanalytics/service.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a\x17\x61nnotations/authz.proto\x1a(api/v1alpha1/vanalytics/correction.proto\x1a$api/v1alpha1/vanalytics/filter.proto\x1a\"api/v1alpha1/vanalytics/flag.proto\x1a)api/v1alpha1/vanalytics/flag_filter.proto\x1a)api/v1alpha1/vanalytics/flag_review.proto\x1a+api/v1alpha1/vanalytics/flag_snapshot.proto\x1a-api/v1alpha1/vanalytics/flag_transcript.proto\x1a\x34\x61pi/v1alpha1/vanalytics/flag_transcript_filter.proto\x1a(api/v1alpha1/vanalytics/transcript.proto\x1a\x30\x61pi/v1alpha1/vanalytics/transcript_summary.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"r\n\x0c\x41uditRequest\x12\x30\n\x05since\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05since\x12\x30\n\x05until\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05until\"\xc4\x01\n\rAuditResponse\x12\x1d\n\naudio_time\x18\x01 \x01(\x01R\taudioTime\x12*\n\x11\x62illed_audio_time\x18\x02 \x01(\x01R\x0f\x62illedAudioTime\x12\x39\n\nlast_usage\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tlastUsage\x12-\n\x12\x62illed_transcripts\x18\x04 \x01(\x03R\x11\x62illedTranscripts\"S\n\x16GetRecordingUrlRequest\x12%\n\x0etranscript_sid\x18\x02 \x01(\x03R\rtranscriptSid\x12\x12\n\x04kind\x18\x04 \x01(\tR\x04kind\"+\n\x17GetRecordingUrlResponse\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"T\n\x16ListBillingSpanRequest\x12\x1b\n\tpage_size\x18\x01 \x01(\rR\x08pageSize\x12\x1d\n\npage_token\x18\x02 \x01(\tR\tpageToken\"}\n\x17ListBillingSpanResponse\x12&\n\x0fnext_page_token\x18\x01 \x01(\tR\rnextPageToken\x12:\n\x05spans\x18\x02 \x03(\x0b\x32$.api.v1alpha1.vanalytics.BillingSpanR\x05spans\"\xbf\x01\n\x0b\x42illingSpan\x12\x14\n\x05\x63\x61lls\x18\x01 \x01(\x03R\x05\x63\x61lls\x12\x14\n\x05hours\x18\x02 \x01(\x03R\x05hours\x12\x12\n\x04\x63ost\x18\x03 \x01(\x01R\x04\x63ost\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime2\xc3\x32\n\nVanalytics\x12\x96\x01\n\x05\x41udit\x12%.api.v1alpha1.vanalytics.AuditRequest\x1a&.api.v1alpha1.vanalytics.AuditResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/vanalytics/vanalytics/audit:\x01*\x12\xc3\x01\n\x0fGetRecordingUrl\x12/.api.v1alpha1.vanalytics.GetRecordingUrlRequest\x1a\x30.api.v1alpha1.vanalytics.GetRecordingUrlResponse\"M\xba\xb8\x91\x02\n\n\x03\x08\xf4\x03\n\x03\x08\xd4\x02\x82\xd3\xe4\x93\x02\x38\"3/api/v1alpha1/vanalytics/vanalytics/getrecordingurl:\x01*\x12\xbe\x01\n\x0fListBillingSpan\x12/.api.v1alpha1.vanalytics.ListBillingSpanRequest\x1a\x30.api.v1alpha1.vanalytics.ListBillingSpanResponse\"H\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x38\"3/api/v1alpha1/vanalytics/vanalytics/listbillingspan:\x01*\x12\x9f\x01\n\x06Search\x12&.api.v1alpha1.vanalytics.SearchRequest\x1a\'.api.v1alpha1.vanalytics.SearchResponse\"D\xba\xb8\x91\x02\n\n\x03\x08\xf4\x03\n\x03\x08\xd4\x02\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/vanalytics/vanalytics/search:\x01*\x12\xe2\x01\n\x18ListTranscriptGroupNames\x12\x38.api.v1alpha1.vanalytics.ListTranscriptGroupNamesRequest\x1a\x39.api.v1alpha1.vanalytics.ListTranscriptGroupNamesResponse\"Q\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x41\"</api/v1alpha1/vanalytics/vanalytics/listtranscriptgroupnames:\x01*\x12\xd6\x01\n\x15\x42ulkDeleteTranscripts\x12\x35.api.v1alpha1.vanalytics.BulkDeleteTranscriptsRequest\x1a\x36.api.v1alpha1.vanalytics.BulkDeleteTranscriptsResponse\"N\xba\xb8\x91\x02\x05\n\x03\x08\xfa\x03\x82\xd3\xe4\x93\x02>\"9/api/v1alpha1/vanalytics/vanalytics/bulkdeletetranscripts:\x01*\x12\xda\x01\n\x16\x42ulkRestoreTranscripts\x12\x36.api.v1alpha1.vanalytics.BulkRestoreTranscriptsRequest\x1a\x37.api.v1alpha1.vanalytics.BulkRestoreTranscriptsResponse\"O\xba\xb8\x91\x02\x05\n\x03\x08\xfa\x03\x82\xd3\xe4\x93\x02?\":/api/v1alpha1/vanalytics/vanalytics/bulkrestoretranscripts:\x01*\x12\xde\x01\n\x17ListAgentResponseValues\x12\x37.api.v1alpha1.vanalytics.ListAgentResponseValuesRequest\x1a\x38.api.v1alpha1.vanalytics.ListAgentResponseValuesResponse\"P\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02@\";/api/v1alpha1/vanalytics/vanalytics/listagentresponsevalues:\x01*\x12\xd2\x01\n\x14GetTranscriptSummary\x12\x34.api.v1alpha1.vanalytics.GetTranscriptSummaryRequest\x1a\x35.api.v1alpha1.vanalytics.GetTranscriptSummaryResponse\"M\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02=\"8/api/v1alpha1/vanalytics/vanalytics/gettranscriptsummary:\x01*\x12\xa4\x01\n\x0c\x43reateFilter\x12,.api.v1alpha1.vanalytics.CreateFilterRequest\x1a\x1f.api.v1alpha1.vanalytics.Filter\"E\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/vanalytics/vanalytics/createfilter:\x01*\x12\xae\x01\n\x0bListFilters\x12+.api.v1alpha1.vanalytics.ListFiltersRequest\x1a,.api.v1alpha1.vanalytics.ListFiltersResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/vanalytics/vanalytics/listfilters:\x01*\x12\xa4\x01\n\x0cUpdateFilter\x12,.api.v1alpha1.vanalytics.UpdateFilterRequest\x1a\x1f.api.v1alpha1.vanalytics.Filter\"E\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/vanalytics/vanalytics/updatefilter:\x01*\x12\xb2\x01\n\x0c\x44\x65leteFilter\x12,.api.v1alpha1.vanalytics.DeleteFilterRequest\x1a-.api.v1alpha1.vanalytics.DeleteFilterResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/vanalytics/vanalytics/deletefilter:\x01*\x12\x9b\x01\n\tGetFilter\x12).api.v1alpha1.vanalytics.GetFilterRequest\x1a\x1f.api.v1alpha1.vanalytics.Filter\"B\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/vanalytics/vanalytics/getfilter:\x01*\x12\x93\x01\n\x07GetFlag\x12\'.api.v1alpha1.vanalytics.GetFlagRequest\x1a\x1d.api.v1alpha1.vanalytics.Flag\"@\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/vanalytics/vanalytics/getflag:\x01*\x12\x9c\x01\n\nCreateFlag\x12*.api.v1alpha1.vanalytics.CreateFlagRequest\x1a\x1d.api.v1alpha1.vanalytics.Flag\"C\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/vanalytics/vanalytics/createflag:\x01*\x12\xa6\x01\n\tListFlags\x12).api.v1alpha1.vanalytics.ListFlagsRequest\x1a*.api.v1alpha1.vanalytics.ListFlagsResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/vanalytics/vanalytics/listflags:\x01*\x12\x9c\x01\n\nUpdateFlag\x12*.api.v1alpha1.vanalytics.UpdateFlagRequest\x1a\x1d.api.v1alpha1.vanalytics.Flag\"C\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/vanalytics/vanalytics/updateflag:\x01*\x12\xaa\x01\n\nDeleteFlag\x12*.api.v1alpha1.vanalytics.DeleteFlagRequest\x1a+.api.v1alpha1.vanalytics.DeleteFlagResponse\"C\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/vanalytics/vanalytics/deleteflag:\x01*\x12\xb4\x01\n\x10\x43reateFlagReview\x12\x30.api.v1alpha1.vanalytics.CreateFlagReviewRequest\x1a#.api.v1alpha1.vanalytics.FlagReview\"I\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/vanalytics/vanalytics/createflagreview:\x01*\x12\xd2\x01\n\x14\x42ulkCreateFlagReview\x12\x34.api.v1alpha1.vanalytics.BulkCreateFlagReviewRequest\x1a\x35.api.v1alpha1.vanalytics.BulkCreateFlagReviewResponse\"M\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02=\"8/api/v1alpha1/vanalytics/vanalytics/bulkcreateflagreview:\x01*\x12\xbe\x01\n\x0fListFlagReviews\x12/.api.v1alpha1.vanalytics.ListFlagReviewsRequest\x1a\x30.api.v1alpha1.vanalytics.ListFlagReviewsResponse\"H\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x38\"3/api/v1alpha1/vanalytics/vanalytics/listflagreviews:\x01*\x12\xd2\x01\n\x14\x43reateFlagTranscript\x12\x34.api.v1alpha1.vanalytics.CreateFlagTranscriptRequest\x1a\x35.api.v1alpha1.vanalytics.CreateFlagTranscriptResponse\"M\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02=\"8/api/v1alpha1/vanalytics/vanalytics/createflagtranscript:\x01*\x12\xd6\x01\n\x15SearchFlagTranscripts\x12\x35.api.v1alpha1.vanalytics.SearchFlagTranscriptsRequest\x1a\x36.api.v1alpha1.vanalytics.SearchFlagTranscriptsResponse\"N\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02>\"9/api/v1alpha1/vanalytics/vanalytics/searchflagtranscripts:\x01*\x12\xb4\x01\n\x10\x43reateFlagFilter\x12\x30.api.v1alpha1.vanalytics.CreateFlagFilterRequest\x1a#.api.v1alpha1.vanalytics.FlagFilter\"I\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/vanalytics/vanalytics/createflagfilter:\x01*\x12\xbe\x01\n\x0fListFlagFilters\x12/.api.v1alpha1.vanalytics.ListFlagFiltersRequest\x1a\x30.api.v1alpha1.vanalytics.ListFlagFiltersResponse\"H\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x38\"3/api/v1alpha1/vanalytics/vanalytics/listflagfilters:\x01*\x12\xc2\x01\n\x10\x44\x65leteFlagFilter\x12\x30.api.v1alpha1.vanalytics.DeleteFlagFilterRequest\x1a\x31.api.v1alpha1.vanalytics.DeleteFlagFilterResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/vanalytics/vanalytics/deleteflagfilter:\x01*\x12\xc6\x01\n\x11ListFlagSnapshots\x12\x31.api.v1alpha1.vanalytics.ListFlagSnapshotsRequest\x1a\x32.api.v1alpha1.vanalytics.ListFlagSnapshotsResponse\"J\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02:\"5/api/v1alpha1/vanalytics/vanalytics/listflagSnapshots:\x01*\x12\xe6\x01\n\x19ListFlagTranscriptFilters\x12\x39.api.v1alpha1.vanalytics.ListFlagTranscriptFiltersRequest\x1a:.api.v1alpha1.vanalytics.ListFlagTranscriptFiltersResponse\"R\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x42\"=/api/v1alpha1/vanalytics/vanalytics/listflagtranscriptfilters:\x01*\x12\xc2\x01\n\x10\x43reateCorrection\x12\x30.api.v1alpha1.vanalytics.CreateCorrectionRequest\x1a\x31.api.v1alpha1.vanalytics.CreateCorrectionResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/vanalytics/vanalytics/createcorrection:\x01*\x12\xab\x01\n\rGetCorrection\x12-.api.v1alpha1.vanalytics.GetCorrectionRequest\x1a#.api.v1alpha1.vanalytics.Correction\"F\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x36\"1/api/v1alpha1/vanalytics/vanalytics/getcorrection:\x01*\x12\xc2\x01\n\x10\x44\x65leteCorrection\x12\x30.api.v1alpha1.vanalytics.DeleteCorrectionRequest\x1a\x31.api.v1alpha1.vanalytics.DeleteCorrectionResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/vanalytics/vanalytics/deletecorrection:\x01*\x12\xbe\x01\n\x0fListCorrections\x12/.api.v1alpha1.vanalytics.ListCorrectionsRequest\x1a\x30.api.v1alpha1.vanalytics.ListCorrectionsResponse\"H\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x38\"3/api/v1alpha1/vanalytics/vanalytics/listcorrections:\x01*\x12\xc2\x01\n\x10UpdateCorrection\x12\x30.api.v1alpha1.vanalytics.UpdateCorrectionRequest\x1a\x31.api.v1alpha1.vanalytics.UpdateCorrectionResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xf4\x03\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/vanalytics/vanalytics/updatecorrection:\x01*B\xa9\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x0cServiceProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\014ServiceProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_VANALYTICS'].methods_by_name['Audit']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['Audit']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002.\")/api/v1alpha1/vanalytics/vanalytics/audit:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetRecordingUrl']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetRecordingUrl']._serialized_options = b'\272\270\221\002\n\n\003\010\364\003\n\003\010\324\002\202\323\344\223\0028\"3/api/v1alpha1/vanalytics/vanalytics/getrecordingurl:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListBillingSpan']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListBillingSpan']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0028\"3/api/v1alpha1/vanalytics/vanalytics/listbillingspan:\001*'
  _globals['_VANALYTICS'].methods_by_name['Search']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['Search']._serialized_options = b'\272\270\221\002\n\n\003\010\364\003\n\003\010\324\002\202\323\344\223\002/\"*/api/v1alpha1/vanalytics/vanalytics/search:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListTranscriptGroupNames']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListTranscriptGroupNames']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002A\"</api/v1alpha1/vanalytics/vanalytics/listtranscriptgroupnames:\001*'
  _globals['_VANALYTICS'].methods_by_name['BulkDeleteTranscripts']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['BulkDeleteTranscripts']._serialized_options = b'\272\270\221\002\005\n\003\010\372\003\202\323\344\223\002>\"9/api/v1alpha1/vanalytics/vanalytics/bulkdeletetranscripts:\001*'
  _globals['_VANALYTICS'].methods_by_name['BulkRestoreTranscripts']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['BulkRestoreTranscripts']._serialized_options = b'\272\270\221\002\005\n\003\010\372\003\202\323\344\223\002?\":/api/v1alpha1/vanalytics/vanalytics/bulkrestoretranscripts:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListAgentResponseValues']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListAgentResponseValues']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002@\";/api/v1alpha1/vanalytics/vanalytics/listagentresponsevalues:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetTranscriptSummary']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetTranscriptSummary']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002=\"8/api/v1alpha1/vanalytics/vanalytics/gettranscriptsummary:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0025\"0/api/v1alpha1/vanalytics/vanalytics/createfilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFilters']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFilters']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0024\"//api/v1alpha1/vanalytics/vanalytics/listfilters:\001*'
  _globals['_VANALYTICS'].methods_by_name['UpdateFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['UpdateFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0025\"0/api/v1alpha1/vanalytics/vanalytics/updatefilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['DeleteFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['DeleteFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0025\"0/api/v1alpha1/vanalytics/vanalytics/deletefilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0022\"-/api/v1alpha1/vanalytics/vanalytics/getfilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetFlag']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetFlag']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0020\"+/api/v1alpha1/vanalytics/vanalytics/getflag:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateFlag']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateFlag']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0023\"./api/v1alpha1/vanalytics/vanalytics/createflag:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlags']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlags']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0022\"-/api/v1alpha1/vanalytics/vanalytics/listflags:\001*'
  _globals['_VANALYTICS'].methods_by_name['UpdateFlag']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['UpdateFlag']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0023\"./api/v1alpha1/vanalytics/vanalytics/updateflag:\001*'
  _globals['_VANALYTICS'].methods_by_name['DeleteFlag']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['DeleteFlag']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0023\"./api/v1alpha1/vanalytics/vanalytics/deleteflag:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateFlagReview']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateFlagReview']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0029\"4/api/v1alpha1/vanalytics/vanalytics/createflagreview:\001*'
  _globals['_VANALYTICS'].methods_by_name['BulkCreateFlagReview']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['BulkCreateFlagReview']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002=\"8/api/v1alpha1/vanalytics/vanalytics/bulkcreateflagreview:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlagReviews']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlagReviews']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0028\"3/api/v1alpha1/vanalytics/vanalytics/listflagreviews:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateFlagTranscript']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateFlagTranscript']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002=\"8/api/v1alpha1/vanalytics/vanalytics/createflagtranscript:\001*'
  _globals['_VANALYTICS'].methods_by_name['SearchFlagTranscripts']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['SearchFlagTranscripts']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002>\"9/api/v1alpha1/vanalytics/vanalytics/searchflagtranscripts:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateFlagFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateFlagFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0029\"4/api/v1alpha1/vanalytics/vanalytics/createflagfilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlagFilters']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlagFilters']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0028\"3/api/v1alpha1/vanalytics/vanalytics/listflagfilters:\001*'
  _globals['_VANALYTICS'].methods_by_name['DeleteFlagFilter']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['DeleteFlagFilter']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0029\"4/api/v1alpha1/vanalytics/vanalytics/deleteflagfilter:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlagSnapshots']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlagSnapshots']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002:\"5/api/v1alpha1/vanalytics/vanalytics/listflagSnapshots:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListFlagTranscriptFilters']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListFlagTranscriptFilters']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\002B\"=/api/v1alpha1/vanalytics/vanalytics/listflagtranscriptfilters:\001*'
  _globals['_VANALYTICS'].methods_by_name['CreateCorrection']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['CreateCorrection']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0029\"4/api/v1alpha1/vanalytics/vanalytics/createcorrection:\001*'
  _globals['_VANALYTICS'].methods_by_name['GetCorrection']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['GetCorrection']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0026\"1/api/v1alpha1/vanalytics/vanalytics/getcorrection:\001*'
  _globals['_VANALYTICS'].methods_by_name['DeleteCorrection']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['DeleteCorrection']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0029\"4/api/v1alpha1/vanalytics/vanalytics/deletecorrection:\001*'
  _globals['_VANALYTICS'].methods_by_name['ListCorrections']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['ListCorrections']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0028\"3/api/v1alpha1/vanalytics/vanalytics/listcorrections:\001*'
  _globals['_VANALYTICS'].methods_by_name['UpdateCorrection']._loaded_options = None
  _globals['_VANALYTICS'].methods_by_name['UpdateCorrection']._serialized_options = b'\272\270\221\002\005\n\003\010\364\003\202\323\344\223\0029\"4/api/v1alpha1/vanalytics/vanalytics/updatecorrection:\001*'
  _globals['_AUDITREQUEST']._serialized_start=594
  _globals['_AUDITREQUEST']._serialized_end=708
  _globals['_AUDITRESPONSE']._serialized_start=711
  _globals['_AUDITRESPONSE']._serialized_end=907
  _globals['_GETRECORDINGURLREQUEST']._serialized_start=909
  _globals['_GETRECORDINGURLREQUEST']._serialized_end=992
  _globals['_GETRECORDINGURLRESPONSE']._serialized_start=994
  _globals['_GETRECORDINGURLRESPONSE']._serialized_end=1037
  _globals['_LISTBILLINGSPANREQUEST']._serialized_start=1039
  _globals['_LISTBILLINGSPANREQUEST']._serialized_end=1123
  _globals['_LISTBILLINGSPANRESPONSE']._serialized_start=1125
  _globals['_LISTBILLINGSPANRESPONSE']._serialized_end=1250
  _globals['_BILLINGSPAN']._serialized_start=1253
  _globals['_BILLINGSPAN']._serialized_end=1444
  _globals['_VANALYTICS']._serialized_start=1447
  _globals['_VANALYTICS']._serialized_end=7914
# @@protoc_insertion_point(module_scope)
