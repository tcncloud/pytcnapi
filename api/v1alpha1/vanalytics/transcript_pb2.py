# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/vanalytics/transcript.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from api.v1alpha1.vanalytics.aclpb import aclpb_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_aclpb_dot_aclpb__pb2
from api.v1alpha1.vanalytics import expr_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_expr__pb2
from api.v1alpha1.vanalytics import transcript_summary_pb2 as api_dot_v1alpha1_dot_vanalytics_dot_transcript__summary__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(api/v1alpha1/vanalytics/transcript.proto\x12\x17\x61pi.v1alpha1.vanalytics\x1a\x15\x61pi/commons/acd.proto\x1a)api/v1alpha1/vanalytics/aclpb/aclpb.proto\x1a\"api/v1alpha1/vanalytics/expr.proto\x1a\x30\x61pi/v1alpha1/vanalytics/transcript_summary.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\\\n\x1c\x42ulkDeleteTranscriptsRequest\x12<\n\x05query\x18\x01 \x01(\x0b\x32&.api.v1alpha1.vanalytics.SearchRequestR\x05query\"5\n\x1d\x42ulkDeleteTranscriptsResponse\x12\x14\n\x05total\x18\x01 \x01(\rR\x05total\"]\n\x1d\x42ulkRestoreTranscriptsRequest\x12<\n\x05query\x18\x01 \x01(\x0b\x32&.api.v1alpha1.vanalytics.SearchRequestR\x05query\"6\n\x1e\x42ulkRestoreTranscriptsResponse\x12\x14\n\x05total\x18\x01 \x01(\rR\x05total\"\xc1\x17\n\rSearchRequest\x12H\n\x07silence\x18\x02 \x01(\x0b\x32..api.v1alpha1.vanalytics.SearchRequest.SilenceR\x07silence\x12@\n\ttalk_time\x18\x03 \x01(\x0b\x32#.api.v1alpha1.vanalytics.Uint32ExprR\x08talkTime\x12\x42\n\x05\x61gent\x18\x04 \x01(\x0b\x32,.api.v1alpha1.vanalytics.SearchRequest.AgentR\x05\x61gent\x12\x1b\n\tpage_size\x18\x05 \x01(\rR\x08pageSize\x12\x31\n\x04sort\x18\x06 \x01(\x0b\x32\x1d.api.v1alpha1.vanalytics.SortR\x04sort\x12G\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32&.api.v1alpha1.vanalytics.TimestampExprR\ncreateTime\x12L\n\ttalk_over\x18\x08 \x01(\x0b\x32/.api.v1alpha1.vanalytics.SearchRequest.TalkOverR\x08talkOver\x12\x42\n\x05terms\x18\t \x01(\x0b\x32,.api.v1alpha1.vanalytics.SearchRequest.TermsR\x05terms\x12\x18\n\x07\x63hannel\x18\n \x01(\rR\x07\x63hannel\x12\x45\n\x06phrase\x18\x0b \x01(\x0b\x32-.api.v1alpha1.vanalytics.SearchRequest.PhraseR\x06phrase\x12\x43\n\x0ftranscript_mask\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0etranscriptMask\x12%\n\x0etranscript_sid\x18\r \x01(\x03R\rtranscriptSid\x12!\n\x0cphone_number\x18\x0e \x01(\tR\x0bphoneNumber\x12\x1b\n\tcaller_id\x18\x0f \x01(\tR\x08\x63\x61llerId\x12\'\n\x0ftranscript_sids\x18\x10 \x03(\x03R\x0etranscriptSids\x12N\n\x0f\x63\x61ll_start_time\x18\x11 \x01(\x0b\x32&.api.v1alpha1.vanalytics.TimestampExprR\rcallStartTime\x12\x39\n\ncall_types\x18\x12 \x03(\x0e\x32\x1a.api.commons.CallType.EnumR\tcallTypes\x12\x1b\n\tcall_sids\x18\x13 \x03(\x03R\x08\x63\x61llSids\x12&\n\x0fhunt_group_sids\x18\x14 \x03(\x03R\rhuntGroupSids\x12\x1f\n\x0bgroup_names\x18\x15 \x03(\tR\ngroupNames\x12P\n\x0e\x61gent_call_log\x18\x16 \x01(\x0b\x32*.api.v1alpha1.vanalytics.AgentCallLogQueryR\x0c\x61gentCallLog\x12:\n\x05where\x18\x17 \x01(\x0b\x32$.api.v1alpha1.vanalytics.SearchQueryR\x05where\x12\x43\n\ntime_frame\x18\x18 \x01(\x0b\x32$.api.v1alpha1.vanalytics.Uint32RangeR\ttimeFrame\x1a\xa9\x04\n\x06Phrase\x12H\n\x05words\x18\x01 \x03(\x0b\x32\x32.api.v1alpha1.vanalytics.SearchRequest.Phrase.WordR\x05words\x12\x12\n\x04slop\x18\x02 \x01(\rR\x04slop\x12\x19\n\x08in_order\x18\x03 \x01(\x08R\x07inOrder\x12U\n\thighlight\x18\x04 \x01(\x0b\x32\x37.api.v1alpha1.vanalytics.SearchRequest.Phrase.HighlightR\thighlight\x12\x10\n\x03not\x18\x05 \x01(\x08R\x03not\x12\x42\n\x05\x61gent\x18\x06 \x01(\x0b\x32,.api.v1alpha1.vanalytics.SearchRequest.AgentR\x05\x61gent\x12\x18\n\x07\x63hannel\x18\x07 \x01(\rR\x07\x63hannel\x12^\n\x0fposition_offset\x18\x08 \x01(\x0b\x32\x35.api.v1alpha1.vanalytics.SearchRequest.PositionOffsetR\x0epositionOffset\x1a:\n\x04Word\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12\x1c\n\tfuzziness\x18\x02 \x01(\tR\tfuzziness\x1a\x43\n\tHighlight\x12\x19\n\x08pre_tags\x18\x01 \x03(\tR\x07preTags\x12\x1b\n\tpost_tags\x18\x02 \x03(\tR\x08postTags\x1ap\n\x0ePositionOffset\x12/\n\x05start\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x05start\x12-\n\x04stop\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x04stop\x1a\xc3\x02\n\x07Silence\x12J\n\x0e\x64uration_total\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.Uint32ExprR\rdurationTotal\x12\x46\n\x0c\x64uration_max\x18\x02 \x01(\x0b\x32#.api.v1alpha1.vanalytics.Uint32ExprR\x0b\x64urationMax\x12N\n\x10occurrence_total\x18\x03 \x01(\x0b\x32#.api.v1alpha1.vanalytics.Uint32ExprR\x0foccurrenceTotal\x12T\n\x13\x64uration_percentage\x18\x04 \x01(\x0b\x32#.api.v1alpha1.vanalytics.Uint32ExprR\x12\x64urationPercentage\x1a\xc4\x02\n\x08TalkOver\x12J\n\x0e\x64uration_total\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.Uint32ExprR\rdurationTotal\x12\x46\n\x0c\x64uration_max\x18\x02 \x01(\x0b\x32#.api.v1alpha1.vanalytics.Uint32ExprR\x0b\x64urationMax\x12N\n\x10occurrence_total\x18\x03 \x01(\x0b\x32#.api.v1alpha1.vanalytics.Uint32ExprR\x0foccurrenceTotal\x12T\n\x13\x64uration_percentage\x18\x04 \x01(\x0b\x32#.api.v1alpha1.vanalytics.Uint32ExprR\x12\x64urationPercentage\x1a\xfb\x01\n\x05Terms\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x12\x10\n\x03\x61ll\x18\x02 \x03(\tR\x03\x61ll\x12\x10\n\x03not\x18\x03 \x01(\x08R\x03not\x12\x42\n\x05\x61gent\x18\x04 \x01(\x0b\x32,.api.v1alpha1.vanalytics.SearchRequest.AgentR\x05\x61gent\x12\x18\n\x07\x63hannel\x18\x05 \x01(\rR\x07\x63hannel\x12^\n\x0fposition_offset\x18\x06 \x01(\x0b\x32\x35.api.v1alpha1.vanalytics.SearchRequest.PositionOffsetR\x0epositionOffset\x1a\x8b\x01\n\x05\x41gent\x12R\n\tuser_name\x18\x01 \x01(\x0b\x32\x35.api.v1alpha1.vanalytics.SearchRequest.Agent.UserNameR\x08userName\x1a.\n\x08UserName\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x12\x10\n\x03\x61ll\x18\x02 \x03(\tR\x03\x61llJ\x04\x08\x01\x10\x02\"\xcd(\n\x0bSearchQuery\x12Y\n\x0etranscript_sid\x18\x01 \x01(\x0b\x32\x32.api.v1alpha1.vanalytics.SearchQuery.TranscriptSidR\rtranscriptSid\x12S\n\x0c\x66lag_summary\x18\x02 \x01(\x0b\x32\x30.api.v1alpha1.vanalytics.SearchQuery.FlagSummaryR\x0b\x66lagSummary\x12\x34\n\x02or\x18\x03 \x03(\x0b\x32$.api.v1alpha1.vanalytics.SearchQueryR\x02or\x12\x36\n\x03\x61nd\x18\x04 \x03(\x0b\x32$.api.v1alpha1.vanalytics.SearchQueryR\x03\x61nd\x12M\n\naudio_time\x18\x05 \x01(\x0b\x32..api.v1alpha1.vanalytics.SearchQuery.AudioTimeR\taudioTime\x12P\n\x0b\x64\x65lete_time\x18\x06 \x01(\x0b\x32/.api.v1alpha1.vanalytics.SearchQuery.DeleteTimeR\ndeleteTime\x12\x36\n\x03not\x18\x07 \x01(\x0b\x32$.api.v1alpha1.vanalytics.SearchQueryR\x03not\x12\x46\n\x07results\x18\x08 \x01(\x0b\x32,.api.v1alpha1.vanalytics.SearchQuery.ResultsR\x07results\x12Y\n\x0e\x61gent_response\x18\t \x01(\x0b\x32\x32.api.v1alpha1.vanalytics.SearchQuery.AgentResponseR\ragentResponse\x12W\n\x0e\x61gent_call_log\x18\n \x01(\x0b\x32\x31.api.v1alpha1.vanalytics.SearchQuery.AgentCallLogR\x0c\x61gentCallLog\x12@\n\x05phone\x18\x0b \x01(\x0b\x32*.api.v1alpha1.vanalytics.SearchQuery.PhoneR\x05phone\x1a\xf5\x05\n\x05Phone\x12\x37\n\x02\x63\x63\x18\x01 \x01(\x0b\x32\'.api.v1alpha1.vanalytics.SearchQuery.CcR\x02\x63\x63\x12:\n\x03ndc\x18\x02 \x01(\x0b\x32(.api.v1alpha1.vanalytics.SearchQuery.NdcR\x03ndc\x12\x43\n\x06prefix\x18\x03 \x01(\x0b\x32+.api.v1alpha1.vanalytics.SearchQuery.PrefixR\x06prefix\x12=\n\x04\x63ity\x18\x04 \x01(\x0b\x32).api.v1alpha1.vanalytics.SearchQuery.CityR\x04\x63ity\x12=\n\x04iso2\x18\x05 \x01(\x0b\x32).api.v1alpha1.vanalytics.SearchQuery.Iso2R\x04iso2\x12P\n\x0bregion_code\x18\x06 \x01(\x0b\x32/.api.v1alpha1.vanalytics.SearchQuery.RegionCodeR\nregionCode\x12P\n\x0bregion_name\x18\x07 \x01(\x0b\x32/.api.v1alpha1.vanalytics.SearchQuery.RegionNameR\nregionName\x12J\n\ttime_zone\x18\x08 \x01(\x0b\x32-.api.v1alpha1.vanalytics.SearchQuery.TimeZoneR\x08timeZone\x12=\n\x04type\x18\t \x01(\x0b\x32).api.v1alpha1.vanalytics.SearchQuery.TypeR\x04type\x12:\n\x03utc\x18\n \x01(\x0b\x32(.api.v1alpha1.vanalytics.SearchQuery.UtcR\x03utc\x12I\n\x08location\x18\x0b \x01(\x0b\x32-.api.v1alpha1.vanalytics.SearchQuery.LocationR\x08location\x1a\x14\n\x02\x43\x63\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x1a\x15\n\x03Ndc\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x1a\x18\n\x06Prefix\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x1a\x16\n\x04\x43ity\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x1a\x16\n\x04Iso2\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x1a\x1c\n\nRegionCode\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x1a\x1c\n\nRegionName\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x1a\x1a\n\x08TimeZone\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x1a\x16\n\x04Type\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x1a\x15\n\x03Utc\x12\x0e\n\x02in\x18\x01 \x03(\x02R\x02in\x1a\xe6\x01\n\x08Location\x12l\n\x12zip_code_proximity\x18\x01 \x01(\x0b\x32>.api.v1alpha1.vanalytics.SearchQuery.Location.ZipCodeProximityR\x10zipCodeProximity\x1al\n\x10ZipCodeProximity\x12!\n\x0c\x63ountry_code\x18\x01 \x01(\tR\x0b\x63ountryCode\x12\x19\n\x08zip_code\x18\x02 \x01(\tR\x07zipCode\x12\x1a\n\x08\x64istance\x18\x03 \x01(\tR\x08\x64istance\x1a\xc5\x01\n\x0c\x41gentCallLog\x12\x66\n\x13\x63\x61ll_skills_initial\x18\x01 \x01(\x0b\x32\x36.api.v1alpha1.vanalytics.SearchQuery.CallSkillsInitialR\x11\x63\x61llSkillsInitial\x12M\n\ncall_ended\x18\x02 \x01(\x0b\x32..api.v1alpha1.vanalytics.SearchQuery.CallEndedR\tcallEnded\x1aI\n\tCallEnded\x12<\n\x07reasons\x18\x01 \x03(\x0e\x32\".api.commons.AgentCallLogCallEndedR\x07reasons\x1a;\n\x11\x43\x61llSkillsInitial\x12\x12\n\x04need\x18\x01 \x03(\tR\x04need\x12\x12\n\x04want\x18\x02 \x03(\tR\x04want\x1a\xb3\x05\n\rAgentResponse\x12H\n\x03key\x18\x01 \x01(\x0b\x32\x36.api.v1alpha1.vanalytics.SearchQuery.AgentResponse.KeyR\x03key\x12Q\n\x06values\x18\x02 \x01(\x0b\x32\x39.api.v1alpha1.vanalytics.SearchQuery.AgentResponse.ValuesR\x06values\x12T\n\x07numbers\x18\x03 \x01(\x0b\x32:.api.v1alpha1.vanalytics.SearchQuery.AgentResponse.NumbersR\x07numbers\x1aU\n\x06Values\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x12\x1f\n\x0bstarts_with\x18\x02 \x01(\tR\nstartsWith\x12\x1a\n\x08\x63ontains\x18\x03 \x01(\tR\x08\x63ontains\x1a\x83\x02\n\x07Numbers\x12\x0e\n\x02in\x18\x01 \x03(\x01R\x02in\x12.\n\x03gte\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x03gte\x12.\n\x03lte\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x03lte\x12,\n\x02gt\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x02gt\x12,\n\x02lt\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x02lt\x12,\n\x02\x65q\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x02\x65q\x1aR\n\x03Key\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x12\x1f\n\x0bstarts_with\x18\x02 \x01(\tR\nstartsWith\x12\x1a\n\x08\x63ontains\x18\x03 \x01(\tR\x08\x63ontains\x1a\xf5\x05\n\x07Results\x12N\n\x07\x63hannel\x18\x01 \x01(\x0b\x32\x34.api.v1alpha1.vanalytics.SearchQuery.Results.ChannelR\x07\x63hannel\x12\x62\n\x0f\x61gent_user_name\x18\x02 \x01(\x0b\x32:.api.v1alpha1.vanalytics.SearchQuery.Results.AgentUserNameR\ragentUserName\x12Q\n\x08segments\x18\x03 \x01(\x0b\x32\x35.api.v1alpha1.vanalytics.SearchQuery.Results.SegmentsR\x08segments\x1a\x19\n\x07\x43hannel\x12\x0e\n\x02\x65q\x18\x01 \x01(\rR\x02\x65q\x1a\x33\n\rAgentUserName\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x12\x10\n\x03\x61ll\x18\x02 \x03(\tR\x03\x61ll\x1a\x92\x03\n\x08Segments\x12N\n\x04text\x18\x01 \x01(\x0b\x32:.api.v1alpha1.vanalytics.SearchQuery.Results.Segments.TextR\x04text\x1a\xb5\x02\n\x04Text\x12Y\n\x06phrase\x18\x01 \x01(\x0b\x32\x41.api.v1alpha1.vanalytics.SearchQuery.Results.Segments.Text.PhraseR\x06phrase\x1a\xd1\x01\n\x06Phrase\x12\\\n\x05words\x18\x01 \x03(\x0b\x32\x46.api.v1alpha1.vanalytics.SearchQuery.Results.Segments.Text.Phrase.WordR\x05words\x12\x12\n\x04slop\x18\x02 \x01(\rR\x04slop\x12\x19\n\x08in_order\x18\x03 \x01(\x08R\x07inOrder\x1a:\n\x04Word\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12\x1c\n\tfuzziness\x18\x02 \x01(\tR\tfuzziness\x1a@\n\nDeleteTime\x12\x32\n\x06\x65xists\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValueR\x06\x65xists\x1aP\n\rTranscriptSid\x12\x10\n\x03\x61ny\x18\x01 \x03(\x03R\x03\x61ny\x12-\n\x03gte\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x03gte\x1a\xc3\x01\n\tAudioTime\x12-\n\x03gte\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x03gte\x12-\n\x03lte\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x03lte\x12+\n\x02gt\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x02gt\x12+\n\x02lt\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x02lt\x1a\xd1\x07\n\x0b\x46lagSummary\x12\\\n\x0bneed_review\x18\x01 \x01(\x0b\x32;.api.v1alpha1.vanalytics.SearchQuery.FlagSummary.NeedReviewR\nneedReview\x12\x62\n\rreview_status\x18\x02 \x01(\x0b\x32=.api.v1alpha1.vanalytics.SearchQuery.FlagSummary.ReviewStatusR\x0creviewStatus\x12L\n\x05\x66lags\x18\x03 \x01(\x0b\x32\x36.api.v1alpha1.vanalytics.SearchQuery.FlagSummary.FlagsR\x05\x66lags\x12L\n\x05\x63ount\x18\x04 \x01(\x0b\x32\x36.api.v1alpha1.vanalytics.SearchQuery.FlagSummary.CountR\x05\x63ount\x1a\x8d\x01\n\nNeedReview\x12\x61\n\tflag_sids\x18\x01 \x01(\x0b\x32\x44.api.v1alpha1.vanalytics.SearchQuery.FlagSummary.NeedReview.FlagSidsR\x08\x66lagSids\x1a\x1c\n\x08\x46lagSids\x12\x10\n\x03\x61ny\x18\x01 \x03(\x03R\x03\x61ny\x1aQ\n\x0cReviewStatus\x12\x41\n\x03\x61ny\x18\x01 \x03(\x0e\x32/.api.v1alpha1.vanalytics.TranscriptReviewStatusR\x03\x61ny\x1a\x91\x01\n\x05\x46lags\x12Y\n\x08\x66lag_sid\x18\x01 \x01(\x0b\x32>.api.v1alpha1.vanalytics.SearchQuery.FlagSummary.Flags.FlagSidR\x07\x66lagSid\x1a-\n\x07\x46lagSid\x12\x10\n\x03\x61ny\x18\x01 \x03(\x03R\x03\x61ny\x12\x10\n\x03\x61ll\x18\x02 \x03(\x03R\x03\x61ll\x1a\xec\x01\n\x05\x43ount\x12-\n\x03gte\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x03gte\x12-\n\x03lte\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x03lte\x12+\n\x02gt\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x02gt\x12+\n\x02lt\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x02lt\x12+\n\x02\x65q\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x02\x65q\"\xe6\x01\n\x0eSearchResponse\x12\x14\n\x05total\x18\x01 \x01(\x04R\x05total\x12?\n\x04hits\x18\x04 \x03(\x0b\x32+.api.v1alpha1.vanalytics.SearchResponse.HitR\x04hits\x12\x31\n\x04sort\x18\x05 \x01(\x0b\x32\x1d.api.v1alpha1.vanalytics.SortR\x04sort\x1aJ\n\x03Hit\x12\x43\n\ntranscript\x18\x01 \x01(\x0b\x32#.api.v1alpha1.vanalytics.TranscriptR\ntranscript\"t\n\x11\x41gentCallLogQuery\x12_\n\x13\x63\x61ll_skills_initial\x18\x01 \x01(\x0b\x32/.api.v1alpha1.vanalytics.CallSkillsInitialQueryR\x11\x63\x61llSkillsInitial\"\x92\x01\n\x16\x43\x61llSkillsInitialQuery\x12;\n\x04need\x18\x01 \x03(\x0b\x32\'.api.v1alpha1.vanalytics.VanaTermsQueryR\x04need\x12;\n\x04want\x18\x02 \x03(\x0b\x32\'.api.v1alpha1.vanalytics.VanaTermsQueryR\x04want\"N\n\x0eVanaTermsQuery\x12\x14\n\x05terms\x18\x01 \x03(\tR\x05terms\x12\x14\n\x05lacks\x18\x02 \x01(\x08R\x05lacks\x12\x10\n\x03\x61ll\x18\x03 \x01(\x08R\x03\x61ll\"\x8a\x01\n\x04Sort\x12;\n\x06\x66ields\x18\x01 \x03(\x0b\x32#.api.v1alpha1.vanalytics.Sort.FieldR\x06\x66ields\x12\x14\n\x05\x61\x66ter\x18\x02 \x03(\tR\x05\x61\x66ter\x1a/\n\x05\x46ield\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x12\n\x04\x64\x65sc\x18\x02 \x01(\x08R\x04\x64\x65sc\"!\n\x1fListTranscriptGroupNamesRequest\"q\n ListTranscriptGroupNamesResponse\x12M\n\x0bgroup_names\x18\x01 \x03(\x0b\x32,.api.v1alpha1.vanalytics.TranscriptGroupNameR\ngroupNames\"+\n\x13TranscriptGroupName\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\"2\n\x1eListAgentResponseValuesRequest\x12\x10\n\x03key\x18\x02 \x01(\tR\x03key\"9\n\x1fListAgentResponseValuesResponse\x12\x16\n\x06values\x18\x01 \x03(\tR\x06values\"\x88\t\n\nTranscript\x12%\n\x0etranscript_sid\x18\x01 \x01(\x03R\rtranscriptSid\x12\x19\n\x08\x63\x61ll_sid\x18\x03 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x04 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12\x39\n\x07results\x18\x05 \x03(\x0b\x32\x1f.api.v1alpha1.vanalytics.ResultR\x07results\x12:\n\x07silence\x18\x06 \x01(\x0b\x32 .api.v1alpha1.vanalytics.SilenceR\x07silence\x12\x1b\n\ttalk_time\x18\x07 \x01(\rR\x08talkTime\x12;\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12\x42\n\x0f\x63\x61ll_start_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rcallStartTime\x12>\n\ttalk_over\x18\x0b \x01(\x0b\x32!.api.v1alpha1.vanalytics.TalkOverR\x08talkOver\x12\x1b\n\tcaller_id\x18\x0c \x01(\tR\x08\x63\x61llerId\x12!\n\x0cphone_number\x18\r \x01(\tR\x0bphoneNumber\x12\x1d\n\naudio_time\x18\x0e \x01(\rR\taudioTime\x12\x1f\n\x0b\x61udio_bytes\x18\x0f \x01(\x03R\naudioBytes\x12\x1d\n\ngroup_name\x18\x11 \x01(\tR\tgroupName\x12Q\n\x0e\x61gent_call_log\x18\x12 \x01(\x0b\x32+.api.v1alpha1.vanalytics.aclpb.AgentCallLogR\x0c\x61gentCallLog\x12G\n\x0c\x66lag_summary\x18\x13 \x01(\x0b\x32$.api.v1alpha1.vanalytics.FlagSummaryR\x0b\x66lagSummary\x12;\n\x0b\x64\x65lete_time\x18\x14 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12#\n\rnumber_format\x18\x15 \x01(\tR\x0cnumberFormat\x12]\n\x0e\x61gent_response\x18\x16 \x03(\x0b\x32\x36.api.v1alpha1.vanalytics.Transcript.AgentResponseEntryR\ragentResponse\x12\x44\n\x07summary\x18\x18 \x01(\x0b\x32*.api.v1alpha1.vanalytics.TranscriptSummaryR\x07summary\x1ah\n\x12\x41gentResponseEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.vanalytics.AgentResponseR\x05value:\x02\x38\x01\"\xcf\x02\n\x06Result\x12\x18\n\x07\x63hannel\x18\x01 \x01(\x05R\x07\x63hannel\x12<\n\x08segments\x18\x02 \x03(\x0b\x32 .api.v1alpha1.vanalytics.SegmentR\x08segments\x12(\n\x10\x61gent_first_name\x18\x05 \x01(\tR\x0e\x61gentFirstName\x12&\n\x0f\x61gent_last_name\x18\x06 \x01(\tR\ragentLastName\x12&\n\x0f\x61gent_user_name\x18\x07 \x01(\tR\ragentUserName\x12\x1d\n\nbegin_time\x18\x08 \x01(\rR\tbeginTime\x12\x1a\n\x08\x64uration\x18\t \x01(\rR\x08\x64uration\x12\x12\n\x04text\x18\n \x01(\tR\x04text\x12$\n\x0ehunt_group_sid\x18\x0b \x01(\x03R\x0chuntGroupSid\"\xad\x01\n\x07Segment\x12\x1d\n\nbegin_time\x18\x01 \x01(\rR\tbeginTime\x12\x1e\n\nconfidence\x18\x02 \x01(\rR\nconfidence\x12\x1a\n\x08\x64uration\x18\x03 \x01(\rR\x08\x64uration\x12\x12\n\x04text\x18\x04 \x01(\tR\x04text\x12\x33\n\x05words\x18\x05 \x03(\x0b\x32\x1d.api.v1alpha1.vanalytics.WordR\x05words\"\x95\x01\n\x04Word\x12\x1d\n\nbegin_time\x18\x01 \x01(\rR\tbeginTime\x12\x1e\n\nconfidence\x18\x02 \x01(\rR\nconfidence\x12\x1a\n\x08\x64uration\x18\x03 \x01(\rR\x08\x64uration\x12\x16\n\x06spoken\x18\x04 \x01(\tR\x06spoken\x12\x1a\n\x08redacted\x18\x05 \x01(\x08R\x08redacted\"\xbf\x03\n\x07Silence\x12\x45\n\x08\x64uration\x18\x01 \x01(\x0b\x32).api.v1alpha1.vanalytics.Silence.DurationR\x08\x64uration\x12\x44\n\x08segments\x18\x02 \x03(\x0b\x32(.api.v1alpha1.vanalytics.Silence.SegmentR\x08segments\x12K\n\noccurrence\x18\x03 \x01(\x0b\x32+.api.v1alpha1.vanalytics.Silence.OccurrenceR\noccurrence\x12\x1c\n\tthreshold\x18\x04 \x01(\rR\tthreshold\x1aR\n\x08\x44uration\x12\x14\n\x05total\x18\x01 \x01(\rR\x05total\x12\x10\n\x03max\x18\x02 \x01(\rR\x03max\x12\x1e\n\npercentage\x18\x03 \x01(\rR\npercentage\x1a\x44\n\x07Segment\x12\x1d\n\nbegin_time\x18\x01 \x01(\rR\tbeginTime\x12\x1a\n\x08\x64uration\x18\x02 \x01(\rR\x08\x64uration\x1a\"\n\nOccurrence\x12\x14\n\x05total\x18\x01 \x01(\rR\x05total\"\x96\x06\n\x08TalkOver\x12L\n\noccurrence\x18\x01 \x01(\x0b\x32,.api.v1alpha1.vanalytics.TalkOver.OccurrenceR\noccurrence\x12\x46\n\x08\x64uration\x18\x02 \x01(\x0b\x32*.api.v1alpha1.vanalytics.TalkOver.DurationR\x08\x64uration\x12\x42\n\x07results\x18\x03 \x03(\x0b\x32(.api.v1alpha1.vanalytics.TalkOver.ResultR\x07results\x12\x1c\n\tthreshold\x18\x04 \x01(\rR\tthreshold\x1aR\n\x08\x44uration\x12\x14\n\x05total\x18\x01 \x01(\rR\x05total\x12\x10\n\x03max\x18\x02 \x01(\rR\x03max\x12\x1e\n\npercentage\x18\x03 \x01(\rR\npercentage\x1a\xd3\x02\n\x06Result\x12\x18\n\x07\x63hannel\x18\x01 \x01(\x05R\x07\x63hannel\x12L\n\noccurrence\x18\x02 \x01(\x0b\x32,.api.v1alpha1.vanalytics.TalkOver.OccurrenceR\noccurrence\x12\x46\n\x08\x64uration\x18\x03 \x01(\x0b\x32*.api.v1alpha1.vanalytics.TalkOver.DurationR\x08\x64uration\x12\x45\n\x08segments\x18\x04 \x03(\x0b\x32).api.v1alpha1.vanalytics.TalkOver.SegmentR\x08segments\x12&\n\x0f\x61gent_user_name\x18\x05 \x01(\tR\ragentUserName\x12*\n\x11\x61gent_session_sid\x18\x06 \x01(\x03R\x0f\x61gentSessionSid\x1a\x44\n\x07Segment\x12\x1d\n\nbegin_time\x18\x01 \x01(\rR\tbeginTime\x12\x1a\n\x08\x64uration\x18\x02 \x01(\rR\x08\x64uration\x1a\"\n\nOccurrence\x12\x14\n\x05total\x18\x01 \x01(\rR\x05total\"\xff\x07\n\x0b\x46lagSummary\x12\x14\n\x05\x63ount\x18\x01 \x01(\x05R\x05\x63ount\x12!\n\x0cpriority_sum\x18\x02 \x01(\x05R\x0bprioritySum\x12!\n\x0cpriority_max\x18\x03 \x01(\x05R\x0bpriorityMax\x12P\n\x0bneed_review\x18\x04 \x01(\x0b\x32/.api.v1alpha1.vanalytics.FlagSummary.NeedReviewR\nneedReview\x12?\n\x05\x66lags\x18\x05 \x03(\x0b\x32).api.v1alpha1.vanalytics.FlagSummary.FlagR\x05\x66lags\x12T\n\rreview_status\x18\x06 \x01(\x0e\x32/.api.v1alpha1.vanalytics.TranscriptReviewStatusR\x0creviewStatus\x1a\x85\x01\n\nNeedReview\x12!\n\x0cpriority_sum\x18\x01 \x01(\x05R\x0bprioritySum\x12!\n\x0cpriority_max\x18\x02 \x01(\x05R\x0bpriorityMax\x12\x14\n\x05\x63ount\x18\x03 \x01(\x05R\x05\x63ount\x12\x1b\n\tflag_sids\x18\x04 \x03(\x03R\x08\x66lagSids\x1a\xbb\x02\n\x04\x46lag\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1a\n\x08priority\x18\x03 \x01(\x05R\x08priority\x12\x18\n\x07version\x18\x04 \x01(\x03R\x07version\x12\x45\n\x07\x66ilters\x18\x05 \x03(\x0b\x32+.api.v1alpha1.vanalytics.FlagSummary.FilterR\x07\x66ilters\x12\x1f\n\x0bmust_review\x18\x06 \x01(\x08R\nmustReview\x12\x1f\n\x0bmust_notify\x18\x07 \x01(\x08R\nmustNotify\x12\x45\n\x07reviews\x18\x08 \x03(\x0b\x32+.api.v1alpha1.vanalytics.FlagSummary.ReviewR\x07reviews\x1a\x8b\x01\n\x06\x46ilter\x12\x19\n\x08join_key\x18\x01 \x01(\tR\x07joinKey\x12\x19\n\x08\x66lag_sid\x18\x02 \x01(\x03R\x07\x66lagSid\x12\x1d\n\nfilter_sid\x18\x03 \x01(\x03R\tfilterSid\x12\x18\n\x07version\x18\x04 \x01(\x03R\x07version\x12\x12\n\x04name\x18\x05 \x01(\tR\x04name\x1aW\n\x06Review\x12\x19\n\x08join_key\x18\x01 \x01(\tR\x07joinKey\x12\x19\n\x08\x66lag_sid\x18\x02 \x01(\x03R\x07\x66lagSid\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userId\"\'\n\rAgentResponse\x12\x16\n\x06values\x18\x01 \x03(\tR\x06values\"\x97\x02\n\x14SearchByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x31\n\x04sort\x18\x03 \x01(\x0b\x32\x1d.api.v1alpha1.vanalytics.SortR\x04sort\x12\x43\n\x0ftranscript_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0etranscriptMask\x12S\n\x0c\x66lag_summary\x18\x05 \x01(\x0b\x32\x30.api.v1alpha1.vanalytics.SearchQuery.FlagSummaryR\x0b\x66lagSummary*\x81\x01\n\x16TranscriptReviewStatus\x12!\n\x1dTRANSCRIPT_REVIEW_STATUS_TODO\x10\x00\x12!\n\x1dTRANSCRIPT_REVIEW_STATUS_DONE\x10\x01\x12!\n\x1dTRANSCRIPT_REVIEW_STATUS_NONE\x10\x02\x42\xac\x01\n\x1b\x63om.api.v1alpha1.vanalyticsB\x0fTranscriptProtoP\x01\xa2\x02\x03\x41VV\xaa\x02\x17\x41pi.V1alpha1.Vanalytics\xca\x02\x17\x41pi\\V1alpha1\\Vanalytics\xe2\x02#Api\\V1alpha1\\Vanalytics\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Vanalyticsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.vanalytics.transcript_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.vanalyticsB\017TranscriptProtoP\001\242\002\003AVV\252\002\027Api.V1alpha1.Vanalytics\312\002\027Api\\V1alpha1\\Vanalytics\342\002#Api\\V1alpha1\\Vanalytics\\GPBMetadata\352\002\031Api::V1alpha1::Vanalytics'
  _globals['_TRANSCRIPT_AGENTRESPONSEENTRY']._loaded_options = None
  _globals['_TRANSCRIPT_AGENTRESPONSEENTRY']._serialized_options = b'8\001'
  _globals['_TRANSCRIPTREVIEWSTATUS']._serialized_start=14313
  _globals['_TRANSCRIPTREVIEWSTATUS']._serialized_end=14442
  _globals['_BULKDELETETRANSCRIPTSREQUEST']._serialized_start=352
  _globals['_BULKDELETETRANSCRIPTSREQUEST']._serialized_end=444
  _globals['_BULKDELETETRANSCRIPTSRESPONSE']._serialized_start=446
  _globals['_BULKDELETETRANSCRIPTSRESPONSE']._serialized_end=499
  _globals['_BULKRESTORETRANSCRIPTSREQUEST']._serialized_start=501
  _globals['_BULKRESTORETRANSCRIPTSREQUEST']._serialized_end=594
  _globals['_BULKRESTORETRANSCRIPTSRESPONSE']._serialized_start=596
  _globals['_BULKRESTORETRANSCRIPTSRESPONSE']._serialized_end=650
  _globals['_SEARCHREQUEST']._serialized_start=653
  _globals['_SEARCHREQUEST']._serialized_end=3662
  _globals['_SEARCHREQUEST_PHRASE']._serialized_start=1940
  _globals['_SEARCHREQUEST_PHRASE']._serialized_end=2493
  _globals['_SEARCHREQUEST_PHRASE_WORD']._serialized_start=2366
  _globals['_SEARCHREQUEST_PHRASE_WORD']._serialized_end=2424
  _globals['_SEARCHREQUEST_PHRASE_HIGHLIGHT']._serialized_start=2426
  _globals['_SEARCHREQUEST_PHRASE_HIGHLIGHT']._serialized_end=2493
  _globals['_SEARCHREQUEST_POSITIONOFFSET']._serialized_start=2495
  _globals['_SEARCHREQUEST_POSITIONOFFSET']._serialized_end=2607
  _globals['_SEARCHREQUEST_SILENCE']._serialized_start=2610
  _globals['_SEARCHREQUEST_SILENCE']._serialized_end=2933
  _globals['_SEARCHREQUEST_TALKOVER']._serialized_start=2936
  _globals['_SEARCHREQUEST_TALKOVER']._serialized_end=3260
  _globals['_SEARCHREQUEST_TERMS']._serialized_start=3263
  _globals['_SEARCHREQUEST_TERMS']._serialized_end=3514
  _globals['_SEARCHREQUEST_AGENT']._serialized_start=3517
  _globals['_SEARCHREQUEST_AGENT']._serialized_end=3656
  _globals['_SEARCHREQUEST_AGENT_USERNAME']._serialized_start=3610
  _globals['_SEARCHREQUEST_AGENT_USERNAME']._serialized_end=3656
  _globals['_SEARCHQUERY']._serialized_start=3665
  _globals['_SEARCHQUERY']._serialized_end=8862
  _globals['_SEARCHQUERY_PHONE']._serialized_start=4502
  _globals['_SEARCHQUERY_PHONE']._serialized_end=5259
  _globals['_SEARCHQUERY_CC']._serialized_start=5261
  _globals['_SEARCHQUERY_CC']._serialized_end=5281
  _globals['_SEARCHQUERY_NDC']._serialized_start=5283
  _globals['_SEARCHQUERY_NDC']._serialized_end=5304
  _globals['_SEARCHQUERY_PREFIX']._serialized_start=5306
  _globals['_SEARCHQUERY_PREFIX']._serialized_end=5330
  _globals['_SEARCHQUERY_CITY']._serialized_start=5332
  _globals['_SEARCHQUERY_CITY']._serialized_end=5354
  _globals['_SEARCHQUERY_ISO2']._serialized_start=5356
  _globals['_SEARCHQUERY_ISO2']._serialized_end=5378
  _globals['_SEARCHQUERY_REGIONCODE']._serialized_start=5380
  _globals['_SEARCHQUERY_REGIONCODE']._serialized_end=5408
  _globals['_SEARCHQUERY_REGIONNAME']._serialized_start=5410
  _globals['_SEARCHQUERY_REGIONNAME']._serialized_end=5438
  _globals['_SEARCHQUERY_TIMEZONE']._serialized_start=5440
  _globals['_SEARCHQUERY_TIMEZONE']._serialized_end=5466
  _globals['_SEARCHQUERY_TYPE']._serialized_start=5468
  _globals['_SEARCHQUERY_TYPE']._serialized_end=5490
  _globals['_SEARCHQUERY_UTC']._serialized_start=5492
  _globals['_SEARCHQUERY_UTC']._serialized_end=5513
  _globals['_SEARCHQUERY_LOCATION']._serialized_start=5516
  _globals['_SEARCHQUERY_LOCATION']._serialized_end=5746
  _globals['_SEARCHQUERY_LOCATION_ZIPCODEPROXIMITY']._serialized_start=5638
  _globals['_SEARCHQUERY_LOCATION_ZIPCODEPROXIMITY']._serialized_end=5746
  _globals['_SEARCHQUERY_AGENTCALLLOG']._serialized_start=5749
  _globals['_SEARCHQUERY_AGENTCALLLOG']._serialized_end=5946
  _globals['_SEARCHQUERY_CALLENDED']._serialized_start=5948
  _globals['_SEARCHQUERY_CALLENDED']._serialized_end=6021
  _globals['_SEARCHQUERY_CALLSKILLSINITIAL']._serialized_start=6023
  _globals['_SEARCHQUERY_CALLSKILLSINITIAL']._serialized_end=6082
  _globals['_SEARCHQUERY_AGENTRESPONSE']._serialized_start=6085
  _globals['_SEARCHQUERY_AGENTRESPONSE']._serialized_end=6776
  _globals['_SEARCHQUERY_AGENTRESPONSE_VALUES']._serialized_start=6345
  _globals['_SEARCHQUERY_AGENTRESPONSE_VALUES']._serialized_end=6430
  _globals['_SEARCHQUERY_AGENTRESPONSE_NUMBERS']._serialized_start=6433
  _globals['_SEARCHQUERY_AGENTRESPONSE_NUMBERS']._serialized_end=6692
  _globals['_SEARCHQUERY_AGENTRESPONSE_KEY']._serialized_start=6694
  _globals['_SEARCHQUERY_AGENTRESPONSE_KEY']._serialized_end=6776
  _globals['_SEARCHQUERY_RESULTS']._serialized_start=6779
  _globals['_SEARCHQUERY_RESULTS']._serialized_end=7536
  _globals['_SEARCHQUERY_RESULTS_CHANNEL']._serialized_start=7053
  _globals['_SEARCHQUERY_RESULTS_CHANNEL']._serialized_end=7078
  _globals['_SEARCHQUERY_RESULTS_AGENTUSERNAME']._serialized_start=7080
  _globals['_SEARCHQUERY_RESULTS_AGENTUSERNAME']._serialized_end=7131
  _globals['_SEARCHQUERY_RESULTS_SEGMENTS']._serialized_start=7134
  _globals['_SEARCHQUERY_RESULTS_SEGMENTS']._serialized_end=7536
  _globals['_SEARCHQUERY_RESULTS_SEGMENTS_TEXT']._serialized_start=7227
  _globals['_SEARCHQUERY_RESULTS_SEGMENTS_TEXT']._serialized_end=7536
  _globals['_SEARCHQUERY_RESULTS_SEGMENTS_TEXT_PHRASE']._serialized_start=7327
  _globals['_SEARCHQUERY_RESULTS_SEGMENTS_TEXT_PHRASE']._serialized_end=7536
  _globals['_SEARCHQUERY_RESULTS_SEGMENTS_TEXT_PHRASE_WORD']._serialized_start=2366
  _globals['_SEARCHQUERY_RESULTS_SEGMENTS_TEXT_PHRASE_WORD']._serialized_end=2424
  _globals['_SEARCHQUERY_DELETETIME']._serialized_start=7538
  _globals['_SEARCHQUERY_DELETETIME']._serialized_end=7602
  _globals['_SEARCHQUERY_TRANSCRIPTSID']._serialized_start=7604
  _globals['_SEARCHQUERY_TRANSCRIPTSID']._serialized_end=7684
  _globals['_SEARCHQUERY_AUDIOTIME']._serialized_start=7687
  _globals['_SEARCHQUERY_AUDIOTIME']._serialized_end=7882
  _globals['_SEARCHQUERY_FLAGSUMMARY']._serialized_start=7885
  _globals['_SEARCHQUERY_FLAGSUMMARY']._serialized_end=8862
  _globals['_SEARCHQUERY_FLAGSUMMARY_NEEDREVIEW']._serialized_start=8251
  _globals['_SEARCHQUERY_FLAGSUMMARY_NEEDREVIEW']._serialized_end=8392
  _globals['_SEARCHQUERY_FLAGSUMMARY_NEEDREVIEW_FLAGSIDS']._serialized_start=8364
  _globals['_SEARCHQUERY_FLAGSUMMARY_NEEDREVIEW_FLAGSIDS']._serialized_end=8392
  _globals['_SEARCHQUERY_FLAGSUMMARY_REVIEWSTATUS']._serialized_start=8394
  _globals['_SEARCHQUERY_FLAGSUMMARY_REVIEWSTATUS']._serialized_end=8475
  _globals['_SEARCHQUERY_FLAGSUMMARY_FLAGS']._serialized_start=8478
  _globals['_SEARCHQUERY_FLAGSUMMARY_FLAGS']._serialized_end=8623
  _globals['_SEARCHQUERY_FLAGSUMMARY_FLAGS_FLAGSID']._serialized_start=8578
  _globals['_SEARCHQUERY_FLAGSUMMARY_FLAGS_FLAGSID']._serialized_end=8623
  _globals['_SEARCHQUERY_FLAGSUMMARY_COUNT']._serialized_start=8626
  _globals['_SEARCHQUERY_FLAGSUMMARY_COUNT']._serialized_end=8862
  _globals['_SEARCHRESPONSE']._serialized_start=8865
  _globals['_SEARCHRESPONSE']._serialized_end=9095
  _globals['_SEARCHRESPONSE_HIT']._serialized_start=9021
  _globals['_SEARCHRESPONSE_HIT']._serialized_end=9095
  _globals['_AGENTCALLLOGQUERY']._serialized_start=9097
  _globals['_AGENTCALLLOGQUERY']._serialized_end=9213
  _globals['_CALLSKILLSINITIALQUERY']._serialized_start=9216
  _globals['_CALLSKILLSINITIALQUERY']._serialized_end=9362
  _globals['_VANATERMSQUERY']._serialized_start=9364
  _globals['_VANATERMSQUERY']._serialized_end=9442
  _globals['_SORT']._serialized_start=9445
  _globals['_SORT']._serialized_end=9583
  _globals['_SORT_FIELD']._serialized_start=9536
  _globals['_SORT_FIELD']._serialized_end=9583
  _globals['_LISTTRANSCRIPTGROUPNAMESREQUEST']._serialized_start=9585
  _globals['_LISTTRANSCRIPTGROUPNAMESREQUEST']._serialized_end=9618
  _globals['_LISTTRANSCRIPTGROUPNAMESRESPONSE']._serialized_start=9620
  _globals['_LISTTRANSCRIPTGROUPNAMESRESPONSE']._serialized_end=9733
  _globals['_TRANSCRIPTGROUPNAME']._serialized_start=9735
  _globals['_TRANSCRIPTGROUPNAME']._serialized_end=9778
  _globals['_LISTAGENTRESPONSEVALUESREQUEST']._serialized_start=9780
  _globals['_LISTAGENTRESPONSEVALUESREQUEST']._serialized_end=9830
  _globals['_LISTAGENTRESPONSEVALUESRESPONSE']._serialized_start=9832
  _globals['_LISTAGENTRESPONSEVALUESRESPONSE']._serialized_end=9889
  _globals['_TRANSCRIPT']._serialized_start=9892
  _globals['_TRANSCRIPT']._serialized_end=11052
  _globals['_TRANSCRIPT_AGENTRESPONSEENTRY']._serialized_start=10948
  _globals['_TRANSCRIPT_AGENTRESPONSEENTRY']._serialized_end=11052
  _globals['_RESULT']._serialized_start=11055
  _globals['_RESULT']._serialized_end=11390
  _globals['_SEGMENT']._serialized_start=11393
  _globals['_SEGMENT']._serialized_end=11566
  _globals['_WORD']._serialized_start=11569
  _globals['_WORD']._serialized_end=11718
  _globals['_SILENCE']._serialized_start=11721
  _globals['_SILENCE']._serialized_end=12168
  _globals['_SILENCE_DURATION']._serialized_start=11980
  _globals['_SILENCE_DURATION']._serialized_end=12062
  _globals['_SILENCE_SEGMENT']._serialized_start=12064
  _globals['_SILENCE_SEGMENT']._serialized_end=12132
  _globals['_SILENCE_OCCURRENCE']._serialized_start=12134
  _globals['_SILENCE_OCCURRENCE']._serialized_end=12168
  _globals['_TALKOVER']._serialized_start=12171
  _globals['_TALKOVER']._serialized_end=12961
  _globals['_TALKOVER_DURATION']._serialized_start=11980
  _globals['_TALKOVER_DURATION']._serialized_end=12062
  _globals['_TALKOVER_RESULT']._serialized_start=12516
  _globals['_TALKOVER_RESULT']._serialized_end=12855
  _globals['_TALKOVER_SEGMENT']._serialized_start=12064
  _globals['_TALKOVER_SEGMENT']._serialized_end=12132
  _globals['_TALKOVER_OCCURRENCE']._serialized_start=12134
  _globals['_TALKOVER_OCCURRENCE']._serialized_end=12168
  _globals['_FLAGSUMMARY']._serialized_start=12964
  _globals['_FLAGSUMMARY']._serialized_end=13987
  _globals['_FLAGSUMMARY_NEEDREVIEW']._serialized_start=13305
  _globals['_FLAGSUMMARY_NEEDREVIEW']._serialized_end=13438
  _globals['_FLAGSUMMARY_FLAG']._serialized_start=13441
  _globals['_FLAGSUMMARY_FLAG']._serialized_end=13756
  _globals['_FLAGSUMMARY_FILTER']._serialized_start=13759
  _globals['_FLAGSUMMARY_FILTER']._serialized_end=13898
  _globals['_FLAGSUMMARY_REVIEW']._serialized_start=13900
  _globals['_FLAGSUMMARY_REVIEW']._serialized_end=13987
  _globals['_AGENTRESPONSE']._serialized_start=13989
  _globals['_AGENTRESPONSE']._serialized_end=14028
  _globals['_SEARCHBYORGIDREQUEST']._serialized_start=14031
  _globals['_SEARCHBYORGIDREQUEST']._serialized_end=14310
# @@protoc_insertion_point(module_scope)
