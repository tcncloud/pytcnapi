# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wfo/vanalytics/v2/transcript.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from wfo.vanalytics.v2 import agent_call_log_pb2 as wfo_dot_vanalytics_dot_v2_dot_agent__call__log__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"wfo/vanalytics/v2/transcript.proto\x12\x11wfo.vanalytics.v2\x1a\x15\x61pi/commons/acd.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a&wfo/vanalytics/v2/agent_call_log.proto\"\x91\x03\n\nTranscript\x12-\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x17.wfo.vanalytics.v2.CallH\x00R\x04\x63\x61ll\x12*\n\x03sms\x18\x02 \x01(\x0b\x32\x16.wfo.vanalytics.v2.SmsH\x00R\x03sms\x12\x34\n\x07\x63hannel\x18\x0c \x01(\x0e\x32\x1a.wfo.vanalytics.v2.ChannelR\x07\x63hannel\x12\x39\n\nstart_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12;\n\x0b\x64\x65lete_time\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12\x41\n\x0c\x66lag_summary\x18\x10 \x01(\x0b\x32\x1e.wfo.vanalytics.v2.FlagSummaryR\x0b\x66lagSummary\x12%\n\x0etranscript_sid\x18\x11 \x01(\x03R\rtranscriptSidB\n\n\x08metadataJ\x04\x08\x0b\x10\x0c\"\xd7\x07\n\x0b\x46lagSummary\x12\x14\n\x05\x63ount\x18\x01 \x01(\x05R\x05\x63ount\x12!\n\x0cpriority_sum\x18\x02 \x01(\x05R\x0bprioritySum\x12!\n\x0cpriority_max\x18\x03 \x01(\x05R\x0bpriorityMax\x12J\n\x0bneed_review\x18\x04 \x01(\x0b\x32).wfo.vanalytics.v2.FlagSummary.NeedReviewR\nneedReview\x12\x39\n\x05\x66lags\x18\x05 \x03(\x0b\x32#.wfo.vanalytics.v2.FlagSummary.FlagR\x05\x66lags\x12\x44\n\rreview_status\x18\x06 \x01(\x0e\x32\x1f.wfo.vanalytics.v2.ReviewStatusR\x0creviewStatus\x1a\x85\x01\n\nNeedReview\x12!\n\x0cpriority_sum\x18\x01 \x01(\x05R\x0bprioritySum\x12!\n\x0cpriority_max\x18\x02 \x01(\x05R\x0bpriorityMax\x12\x14\n\x05\x63ount\x18\x03 \x01(\x05R\x05\x63ount\x12\x1b\n\tflag_sids\x18\x04 \x03(\x03R\x08\x66lagSids\x1a\xaf\x02\n\x04\x46lag\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x1a\n\x08priority\x18\x03 \x01(\x05R\x08priority\x12\x18\n\x07version\x18\x04 \x01(\x03R\x07version\x12?\n\x07\x66ilters\x18\x05 \x03(\x0b\x32%.wfo.vanalytics.v2.FlagSummary.FilterR\x07\x66ilters\x12\x1f\n\x0bmust_review\x18\x06 \x01(\x08R\nmustReview\x12\x1f\n\x0bmust_notify\x18\x07 \x01(\x08R\nmustNotify\x12?\n\x07reviews\x18\x08 \x03(\x0b\x32%.wfo.vanalytics.v2.FlagSummary.ReviewR\x07reviews\x1a\x8b\x01\n\x06\x46ilter\x12\x19\n\x08join_key\x18\x01 \x01(\tR\x07joinKey\x12\x19\n\x08\x66lag_sid\x18\x02 \x01(\x03R\x07\x66lagSid\x12\x1d\n\nfilter_sid\x18\x03 \x01(\x03R\tfilterSid\x12\x18\n\x07version\x18\x04 \x01(\x03R\x07version\x12\x12\n\x04name\x18\x05 \x01(\tR\x04name\x1aW\n\x06Review\x12\x19\n\x08join_key\x18\x01 \x01(\tR\x07joinKey\x12\x19\n\x08\x66lag_sid\x18\x02 \x01(\x03R\x07\x66lagSid\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userId\"\xaa\x02\n\x03Sms\x12)\n\x10\x63onversation_sid\x18\x01 \x01(\x03R\x0f\x63onversationSid\x12\x37\n\x07threads\x18\x02 \x03(\x0b\x32\x1d.wfo.vanalytics.v2.Sms.ThreadR\x07threads\x1am\n\x06Thread\x12\x0e\n\x02id\x18\x01 \x01(\x05R\x02id\x12:\n\x08segments\x18\x02 \x03(\x0b\x32\x1e.wfo.vanalytics.v2.Sms.SegmentR\x08segments\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userId\x1aP\n\x07Segment\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x31\n\x06offset\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x06offset\"\xb5\r\n\x04\x43\x61ll\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x02 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12\x1d\n\naudio_time\x18\x03 \x01(\rR\taudioTime\x12\x38\n\x07threads\x18\x04 \x03(\x0b\x32\x1e.wfo.vanalytics.v2.Call.ThreadR\x07threads\x12\x39\n\x07silence\x18\x05 \x01(\x0b\x32\x1f.wfo.vanalytics.v2.Call.SilenceR\x07silence\x12=\n\ttalk_over\x18\x06 \x01(\x0b\x32 .wfo.vanalytics.v2.Call.TalkOverR\x08talkOver\x12\x36\n\ttalk_time\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08talkTime\x12\x1b\n\tcaller_id\x18\x08 \x01(\tR\x08\x63\x61llerId\x12\x1d\n\ngroup_name\x18\t \x01(\tR\tgroupName\x12Q\n\x0e\x61gent_response\x18\n \x03(\x0b\x32*.wfo.vanalytics.v2.Call.AgentResponseEntryR\ragentResponse\x12&\n\x0fhunt_group_sids\x18\x0b \x03(\x03R\rhuntGroupSids\x12#\n\rnumber_format\x18\x0c \x01(\tR\x0cnumberFormat\x12\x45\n\x0e\x61gent_call_log\x18\r \x01(\x0b\x32\x1f.wfo.vanalytics.v2.AgentCallLogR\x0c\x61gentCallLog\x1ag\n\x12\x41gentResponseEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12;\n\x05value\x18\x02 \x01(\x0b\x32%.wfo.vanalytics.v2.Call.AgentResponseR\x05value:\x02\x38\x01\x1a\'\n\rAgentResponse\x12\x16\n\x06values\x18\x01 \x03(\tR\x06values\x1an\n\x06Thread\x12\x0e\n\x02id\x18\x01 \x01(\x05R\x02id\x12;\n\x08segments\x18\x02 \x03(\x0b\x32\x1f.wfo.vanalytics.v2.Call.SegmentR\x08segments\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userId\x1aP\n\x07Segment\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x31\n\x06offset\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x06offset\x1a\xeb\x02\n\x08TalkOver\x12\x45\n\x08\x64uration\x18\x01 \x01(\x0b\x32).wfo.vanalytics.v2.Call.TalkOver.DurationR\x08\x64uration\x12K\n\noccurrence\x18\x02 \x01(\x0b\x32+.wfo.vanalytics.v2.Call.TalkOver.OccurrenceR\noccurrence\x12\x1c\n\tthreshold\x18\x03 \x01(\rR\tthreshold\x1a\x88\x01\n\x08\x44uration\x12/\n\x05total\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x05total\x12+\n\x03max\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03max\x12\x1e\n\npercentage\x18\x03 \x01(\rR\npercentage\x1a\"\n\nOccurrence\x12\x14\n\x05total\x18\x01 \x01(\rR\x05total\x1a\xe8\x02\n\x07Silence\x12\x44\n\x08\x64uration\x18\x01 \x01(\x0b\x32(.wfo.vanalytics.v2.Call.Silence.DurationR\x08\x64uration\x12J\n\noccurrence\x18\x02 \x01(\x0b\x32*.wfo.vanalytics.v2.Call.Silence.OccurrenceR\noccurrence\x12\x1c\n\tthreshold\x18\x03 \x01(\rR\tthreshold\x1a\x88\x01\n\x08\x44uration\x12/\n\x05total\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x05total\x12+\n\x03max\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03max\x12\x1e\n\npercentage\x18\x03 \x01(\rR\npercentage\x1a\"\n\nOccurrence\x12\x14\n\x05total\x18\x01 \x01(\rR\x05total\"\xb3\x02\n\x18SearchTranscriptsRequest\x12\x1b\n\tpage_size\x18\x02 \x01(\rR\x08pageSize\x12\x19\n\x08order_by\x18\x03 \x01(\tR\x07orderBy\x12\x37\n\tread_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x08readMask\x12\x45\n\nbool_query\x18\x05 \x01(\x0b\x32&.wfo.vanalytics.v2.TranscriptBoolQueryR\tboolQuery\x12\x1d\n\npage_token\x18\x06 \x01(\tR\tpageToken\x12:\n\thighlight\x18\x07 \x01(\x0b\x32\x1c.wfo.vanalytics.v2.HighlightR\thighlightJ\x04\x08\x01\x10\x02\";\n\tHighlight\x12\x16\n\x06prefix\x18\x01 \x01(\tR\x06prefix\x12\x16\n\x06suffix\x18\x02 \x01(\tR\x06suffix\"\xdb\x01\n\x19SearchTranscriptsResponse\x12\x44\n\x04hits\x18\x01 \x03(\x0b\x32\x30.wfo.vanalytics.v2.SearchTranscriptsResponse.HitR\x04hits\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\x1aP\n\x03Hit\x12=\n\ntranscript\x18\x01 \x01(\x0b\x32\x1d.wfo.vanalytics.v2.TranscriptR\ntranscriptJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04\"Y\n\x13TranscriptBoolQuery\x12\x42\n\ntranscript\x18\x01 \x01(\x0b\x32\".wfo.vanalytics.v2.TranscriptQueryR\ntranscript\"\xc0H\n\x0fTranscriptQuery\x12W\n\x0etranscript_sid\x18\x01 \x01(\x0b\x32\x30.wfo.vanalytics.v2.TranscriptQuery.TranscriptSidR\rtranscriptSid\x12\x44\n\x07\x63hannel\x18\x02 \x01(\x0b\x32*.wfo.vanalytics.v2.TranscriptQuery.ChannelR\x07\x63hannel\x12G\n\x08metadata\x18\x03 \x01(\x0b\x32+.wfo.vanalytics.v2.TranscriptQuery.MetadataR\x08metadata\x12\x44\n\x07threads\x18\x04 \x01(\x0b\x32*.wfo.vanalytics.v2.TranscriptQuery.ThreadsR\x07threads\x12Q\n\x0c\x66lag_summary\x18\x05 \x01(\x0b\x32..wfo.vanalytics.v2.TranscriptQuery.FlagSummaryR\x0b\x66lagSummary\x12K\n\nstart_time\x18\x06 \x01(\x0b\x32,.wfo.vanalytics.v2.TranscriptQuery.StartTimeR\tstartTime\x12N\n\x0b\x64\x65lete_time\x18\x07 \x01(\x0b\x32-.wfo.vanalytics.v2.TranscriptQuery.DeleteTimeR\ndeleteTime\x12>\n\x05phone\x18\x08 \x01(\x0b\x32(.wfo.vanalytics.v2.TranscriptQuery.PhoneR\x05phone\x1a\xf9\n\n\x05Phone\x12;\n\x02\x63\x63\x18\x01 \x01(\x0b\x32+.wfo.vanalytics.v2.TranscriptQuery.Phone.CcR\x02\x63\x63\x12>\n\x03ndc\x18\x02 \x01(\x0b\x32,.wfo.vanalytics.v2.TranscriptQuery.Phone.NdcR\x03ndc\x12G\n\x06prefix\x18\x03 \x01(\x0b\x32/.wfo.vanalytics.v2.TranscriptQuery.Phone.PrefixR\x06prefix\x12\x41\n\x04\x63ity\x18\x04 \x01(\x0b\x32-.wfo.vanalytics.v2.TranscriptQuery.Phone.CityR\x04\x63ity\x12\x41\n\x04iso2\x18\x05 \x01(\x0b\x32-.wfo.vanalytics.v2.TranscriptQuery.Phone.Iso2R\x04iso2\x12T\n\x0bregion_code\x18\x06 \x01(\x0b\x32\x33.wfo.vanalytics.v2.TranscriptQuery.Phone.RegionCodeR\nregionCode\x12T\n\x0bregion_name\x18\x07 \x01(\x0b\x32\x33.wfo.vanalytics.v2.TranscriptQuery.Phone.RegionNameR\nregionName\x12N\n\ttime_zone\x18\x08 \x01(\x0b\x32\x31.wfo.vanalytics.v2.TranscriptQuery.Phone.TimeZoneR\x08timeZone\x12\x41\n\x04type\x18\t \x01(\x0b\x32-.wfo.vanalytics.v2.TranscriptQuery.Phone.TypeR\x04type\x12>\n\x03utc\x18\n \x01(\x0b\x32,.wfo.vanalytics.v2.TranscriptQuery.Phone.UtcR\x03utc\x12M\n\x08location\x18\x0b \x01(\x0b\x32\x31.wfo.vanalytics.v2.TranscriptQuery.Phone.LocationR\x08location\x12>\n\x03raw\x18\x0c \x01(\x0b\x32,.wfo.vanalytics.v2.TranscriptQuery.Phone.RawR\x03raw\x1a\x16\n\x02\x43\x63\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x17\n\x03Ndc\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x1a\n\x06Prefix\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x18\n\x04\x43ity\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x18\n\x04Iso2\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x1e\n\nRegionCode\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x1e\n\nRegionName\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x1c\n\x08TimeZone\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x18\n\x04Type\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x17\n\x03Utc\x12\x10\n\x03\x61ny\x18\x01 \x03(\x02R\x03\x61ny\x1a\xea\x01\n\x08Location\x12p\n\x12zip_code_proximity\x18\x01 \x01(\x0b\x32\x42.wfo.vanalytics.v2.TranscriptQuery.Phone.Location.ZipCodeProximityR\x10zipCodeProximity\x1al\n\x10ZipCodeProximity\x12!\n\x0c\x63ountry_code\x18\x01 \x01(\tR\x0b\x63ountryCode\x12\x19\n\x08zip_code\x18\x02 \x01(\tR\x07zipCode\x12\x1a\n\x08\x64istance\x18\x03 \x01(\tR\x08\x64istance\x1a\x17\n\x03Raw\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a!\n\rTranscriptSid\x12\x10\n\x03\x61ny\x18\x01 \x03(\x03R\x03\x61ny\x1a\x37\n\x07\x43hannel\x12,\n\x03\x61ny\x18\x01 \x03(\x0e\x32\x1a.wfo.vanalytics.v2.ChannelR\x03\x61ny\x1a\x81\x01\n\x08Metadata\x12;\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\'.wfo.vanalytics.v2.TranscriptQuery.CallR\x04\x63\x61ll\x12\x38\n\x03sms\x18\x02 \x01(\x0b\x32&.wfo.vanalytics.v2.TranscriptQuery.SmsR\x03sms\x1a\xd6%\n\x04\x43\x61ll\x12J\n\x08\x63\x61ll_sid\x18\x01 \x01(\x0b\x32/.wfo.vanalytics.v2.TranscriptQuery.Call.CallSidR\x07\x63\x61llSid\x12P\n\naudio_time\x18\x02 \x01(\x0b\x32\x31.wfo.vanalytics.v2.TranscriptQuery.Call.AudioTimeR\taudioTime\x12M\n\tcall_type\x18\x03 \x01(\x0b\x32\x30.wfo.vanalytics.v2.TranscriptQuery.Call.CallTypeR\x08\x63\x61llType\x12I\n\x07silence\x18\x04 \x01(\x0b\x32/.wfo.vanalytics.v2.TranscriptQuery.Call.SilenceR\x07silence\x12M\n\ttalk_over\x18\x05 \x01(\x0b\x32\x30.wfo.vanalytics.v2.TranscriptQuery.Call.TalkOverR\x08talkOver\x12M\n\ttalk_time\x18\x06 \x01(\x0b\x32\x30.wfo.vanalytics.v2.TranscriptQuery.Call.TalkTimeR\x08talkTime\x12M\n\tcaller_id\x18\x07 \x01(\x0b\x32\x30.wfo.vanalytics.v2.TranscriptQuery.Call.CallerIdR\x08\x63\x61llerId\x12P\n\ngroup_name\x18\x08 \x01(\x0b\x32\x31.wfo.vanalytics.v2.TranscriptQuery.Call.GroupNameR\tgroupName\x12\\\n\x0e\x61gent_response\x18\t \x01(\x0b\x32\x35.wfo.vanalytics.v2.TranscriptQuery.Call.AgentResponseR\ragentResponse\x12]\n\x0fhunt_group_sids\x18\n \x01(\x0b\x32\x35.wfo.vanalytics.v2.TranscriptQuery.Call.HuntGroupSidsR\rhuntGroupSids\x12J\n\x0e\x61gent_call_log\x18\x0c \x01(\x0b\x32$.wfo.vanalytics.v2.AgentCallLogQueryR\x0c\x61gentCallLog\x1a!\n\rHuntGroupSids\x12\x10\n\x03\x61ny\x18\x01 \x03(\x03R\x03\x61ny\x1a\xde\x06\n\rAgentResponse\x12G\n\x03\x61nd\x18\x01 \x03(\x0b\x32\x35.wfo.vanalytics.v2.TranscriptQuery.Call.AgentResponseR\x03\x61nd\x12\x45\n\x02or\x18\x02 \x03(\x0b\x32\x35.wfo.vanalytics.v2.TranscriptQuery.Call.AgentResponseR\x02or\x12\x10\n\x03not\x18\x03 \x01(\x08R\x03not\x12K\n\x03key\x18\x04 \x01(\x0b\x32\x39.wfo.vanalytics.v2.TranscriptQuery.Call.AgentResponse.KeyR\x03key\x12T\n\x06values\x18\x05 \x01(\x0b\x32<.wfo.vanalytics.v2.TranscriptQuery.Call.AgentResponse.ValuesR\x06values\x12W\n\x07numbers\x18\x06 \x01(\x0b\x32=.wfo.vanalytics.v2.TranscriptQuery.Call.AgentResponse.NumbersR\x07numbers\x1aU\n\x06Values\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x12\x1f\n\x0bstarts_with\x18\x02 \x01(\tR\nstartsWith\x12\x1a\n\x08\x63ontains\x18\x03 \x01(\tR\x08\x63ontains\x1a\x83\x02\n\x07Numbers\x12\x0e\n\x02in\x18\x01 \x03(\x01R\x02in\x12.\n\x03gte\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x03gte\x12.\n\x03lte\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x03lte\x12,\n\x02gt\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x02gt\x12,\n\x02lt\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x02lt\x12,\n\x02\x65q\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x02\x65q\x1aR\n\x03Key\x12\x0e\n\x02in\x18\x01 \x03(\tR\x02in\x12\x1f\n\x0bstarts_with\x18\x02 \x01(\tR\nstartsWith\x12\x1a\n\x08\x63ontains\x18\x03 \x01(\tR\x08\x63ontains\x1a\x38\n\x08\x43\x61llType\x12,\n\x03\x61ny\x18\x01 \x03(\x0e\x32\x1a.api.commons.CallType.EnumR\x03\x61ny\x1a\x1d\n\tGroupName\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x1b\n\x07\x43\x61llSid\x12\x10\n\x03\x61ny\x18\x01 \x03(\x03R\x03\x61ny\x1a\x1c\n\x08\x43\x61llerId\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\xc3\x01\n\tAudioTime\x12-\n\x03gte\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x03gte\x12-\n\x03lte\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x03lte\x12+\n\x02gt\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x02gt\x12+\n\x02lt\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x02lt\x1a\xba\x01\n\x08TalkTime\x12+\n\x03gte\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03gte\x12+\n\x03lte\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03lte\x12)\n\x02gt\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x02gt\x12)\n\x02lt\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x02lt\x1a\xda\t\n\x08TalkOver\x12\x65\n\x0e\x64uration_total\x18\x01 \x01(\x0b\x32>.wfo.vanalytics.v2.TranscriptQuery.Call.TalkOver.DurationTotalR\rdurationTotal\x12_\n\x0c\x64uration_max\x18\x02 \x01(\x0b\x32<.wfo.vanalytics.v2.TranscriptQuery.Call.TalkOver.DurationMaxR\x0b\x64urationMax\x12k\n\x10occurrence_total\x18\x03 \x01(\x0b\x32@.wfo.vanalytics.v2.TranscriptQuery.Call.TalkOver.OccurrenceTotalR\x0foccurrenceTotal\x12t\n\x13\x64uration_percentage\x18\x04 \x01(\x0b\x32\x43.wfo.vanalytics.v2.TranscriptQuery.Call.TalkOver.DurationPercentageR\x12\x64urationPercentage\x1a\xbf\x01\n\rDurationTotal\x12+\n\x03gte\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03gte\x12+\n\x03lte\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03lte\x12)\n\x02gt\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x02gt\x12)\n\x02lt\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x02lt\x1a\xbd\x01\n\x0b\x44urationMax\x12+\n\x03gte\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03gte\x12+\n\x03lte\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03lte\x12)\n\x02gt\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x02gt\x12)\n\x02lt\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x02lt\x1a\xcd\x01\n\x0fOccurrenceTotal\x12.\n\x03gte\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x03gte\x12.\n\x03lte\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x03lte\x12,\n\x02gt\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x02gt\x12,\n\x02lt\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x02lt\x1a\xd0\x01\n\x12\x44urationPercentage\x12.\n\x03gte\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x03gte\x12.\n\x03lte\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x03lte\x12,\n\x02gt\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x02gt\x12,\n\x02lt\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x02lt\x1a\xd5\t\n\x07Silence\x12\x64\n\x0e\x64uration_total\x18\x01 \x01(\x0b\x32=.wfo.vanalytics.v2.TranscriptQuery.Call.Silence.DurationTotalR\rdurationTotal\x12^\n\x0c\x64uration_max\x18\x02 \x01(\x0b\x32;.wfo.vanalytics.v2.TranscriptQuery.Call.Silence.DurationMaxR\x0b\x64urationMax\x12j\n\x10occurrence_total\x18\x03 \x01(\x0b\x32?.wfo.vanalytics.v2.TranscriptQuery.Call.Silence.OccurrenceTotalR\x0foccurrenceTotal\x12s\n\x13\x64uration_percentage\x18\x04 \x01(\x0b\x32\x42.wfo.vanalytics.v2.TranscriptQuery.Call.Silence.DurationPercentageR\x12\x64urationPercentage\x1a\xbf\x01\n\rDurationTotal\x12+\n\x03gte\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03gte\x12+\n\x03lte\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03lte\x12)\n\x02gt\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x02gt\x12)\n\x02lt\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x02lt\x1a\xbd\x01\n\x0b\x44urationMax\x12+\n\x03gte\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03gte\x12+\n\x03lte\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x03lte\x12)\n\x02gt\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x02gt\x12)\n\x02lt\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x02lt\x1a\xcd\x01\n\x0fOccurrenceTotal\x12.\n\x03gte\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x03gte\x12.\n\x03lte\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x03lte\x12,\n\x02gt\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x02gt\x12,\n\x02lt\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x02lt\x1a\xd0\x01\n\x12\x44urationPercentage\x12.\n\x03gte\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x03gte\x12.\n\x03lte\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x03lte\x12,\n\x02gt\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x02gt\x12,\n\x02lt\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueR\x02lt\x1a\x8d\x01\n\x03Sms\x12\x61\n\x10\x63onversation_sid\x18\x01 \x01(\x0b\x32\x36.wfo.vanalytics.v2.TranscriptQuery.Sms.ConversationSidR\x0f\x63onversationSid\x1a#\n\x0f\x43onversationSid\x12\x10\n\x03\x61ny\x18\x01 \x03(\x03R\x03\x61ny\x1a\xcc\x05\n\x07Threads\x12<\n\x03\x61nd\x18\x01 \x03(\x0b\x32*.wfo.vanalytics.v2.TranscriptQuery.ThreadsR\x03\x61nd\x12:\n\x02or\x18\x02 \x03(\x0b\x32*.wfo.vanalytics.v2.TranscriptQuery.ThreadsR\x02or\x12=\n\x02id\x18\x04 \x01(\x0b\x32-.wfo.vanalytics.v2.TranscriptQuery.Threads.IdR\x02id\x12\x43\n\x04text\x18\x05 \x01(\x0b\x32/.wfo.vanalytics.v2.TranscriptQuery.Threads.TextR\x04text\x12J\n\x07user_id\x18\x06 \x01(\x0b\x32\x31.wfo.vanalytics.v2.TranscriptQuery.Threads.UserIdR\x06userId\x1a\x1a\n\x06UserId\x12\x10\n\x03\x61ny\x18\x01 \x03(\tR\x03\x61ny\x1a\x16\n\x02Id\x12\x10\n\x03\x61ny\x18\x01 \x03(\x05R\x03\x61ny\x1a\xc2\x02\n\x04Text\x12.\n\x05match\x18\x01 \x01(\x0b\x32\x18.wfo.vanalytics.v2.MatchR\x05match\x12\x38\n\tspan_near\x18\x02 \x01(\x0b\x32\x1b.wfo.vanalytics.v2.SpanNearR\x08spanNear\x12T\n\x08timespan\x18\x03 \x01(\x0b\x32\x38.wfo.vanalytics.v2.TranscriptQuery.Threads.Text.TimespanR\x08timespan\x12\x10\n\x03not\x18\x04 \x01(\x08R\x03not\x1ah\n\x08Timespan\x12-\n\x04head\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\x04head\x12-\n\x04tail\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationR\x04tail\x1a\xb5\x07\n\x0b\x46lagSummary\x12Z\n\x0bneed_review\x18\x01 \x01(\x0b\x32\x39.wfo.vanalytics.v2.TranscriptQuery.FlagSummary.NeedReviewR\nneedReview\x12`\n\rreview_status\x18\x02 \x01(\x0b\x32;.wfo.vanalytics.v2.TranscriptQuery.FlagSummary.ReviewStatusR\x0creviewStatus\x12J\n\x05\x66lags\x18\x03 \x01(\x0b\x32\x34.wfo.vanalytics.v2.TranscriptQuery.FlagSummary.FlagsR\x05\x66lags\x12J\n\x05\x63ount\x18\x04 \x01(\x0b\x32\x34.wfo.vanalytics.v2.TranscriptQuery.FlagSummary.CountR\x05\x63ount\x1a\x8b\x01\n\nNeedReview\x12_\n\tflag_sids\x18\x01 \x01(\x0b\x32\x42.wfo.vanalytics.v2.TranscriptQuery.FlagSummary.NeedReview.FlagSidsR\x08\x66lagSids\x1a\x1c\n\x08\x46lagSids\x12\x10\n\x03\x61ny\x18\x01 \x03(\x03R\x03\x61ny\x1a\x41\n\x0cReviewStatus\x12\x31\n\x03\x61ny\x18\x01 \x03(\x0e\x32\x1f.wfo.vanalytics.v2.ReviewStatusR\x03\x61ny\x1a\x8f\x01\n\x05\x46lags\x12W\n\x08\x66lag_sid\x18\x01 \x01(\x0b\x32<.wfo.vanalytics.v2.TranscriptQuery.FlagSummary.Flags.FlagSidR\x07\x66lagSid\x1a-\n\x07\x46lagSid\x12\x10\n\x03\x61ny\x18\x01 \x03(\x03R\x03\x61ny\x12\x10\n\x03\x61ll\x18\x02 \x03(\x03R\x03\x61ll\x1a\xec\x01\n\x05\x43ount\x12-\n\x03gte\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x03gte\x12-\n\x03lte\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x03lte\x12+\n\x02gt\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x02gt\x12+\n\x02lt\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x02lt\x12+\n\x02\x65q\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x02\x65q\x1a\xbf\x01\n\tStartTime\x12,\n\x03gte\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03gte\x12,\n\x03lte\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03lte\x12*\n\x02gt\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02gt\x12*\n\x02lt\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02lt\x1a\xc0\x01\n\nDeleteTime\x12,\n\x03gte\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03gte\x12,\n\x03lte\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03lte\x12*\n\x02gt\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02gt\x12*\n\x02lt\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02lt\"5\n\rFuzzinessAuto\x12\x10\n\x03low\x18\x01 \x01(\rR\x03low\x12\x12\n\x04high\x18\x02 \x01(\rR\x04high\"\xba\x01\n\x05Match\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1a\n\x08operator\x18\x02 \x01(\tR\x08operator\x12I\n\x0e\x66uzziness_auto\x18\x0f \x01(\x0b\x32 .wfo.vanalytics.v2.FuzzinessAutoH\x00R\rfuzzinessAuto\x12)\n\x0f\x66uzziness_value\x18\x10 \x01(\rH\x00R\x0e\x66uzzinessValueB\x0b\n\tfuzziness\"\xc2\x02\n\x08SpanNear\x12\x12\n\x04slop\x18\x01 \x01(\x05R\x04slop\x12\x19\n\x08in_order\x18\x02 \x01(\x08R\x07inOrder\x12<\n\x07\x63lauses\x18\x03 \x03(\x0b\x32\".wfo.vanalytics.v2.SpanNear.ClauseR\x07\x63lauses\x1a\xc8\x01\n\x06\x43lause\x12:\n\tspan_near\x18\x01 \x01(\x0b\x32\x1b.wfo.vanalytics.v2.SpanNearH\x00R\x08spanNear\x12=\n\nspan_fuzzy\x18\x02 \x01(\x0b\x32\x1c.wfo.vanalytics.v2.SpanFuzzyH\x00R\tspanFuzzy\x12:\n\tspan_term\x18\x03 \x01(\x0b\x32\x1b.wfo.vanalytics.v2.SpanTermH\x00R\x08spanTermB\x07\n\x05match\" \n\x08SpanTerm\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\"\xa4\x01\n\tSpanFuzzy\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12I\n\x0e\x66uzziness_auto\x18\n \x01(\x0b\x32 .wfo.vanalytics.v2.FuzzinessAutoH\x00R\rfuzzinessAuto\x12)\n\x0f\x66uzziness_value\x18\x0b \x01(\rH\x00R\x0e\x66uzzinessValueB\x0b\n\tfuzziness*,\n\x07\x43hannel\x12\x10\n\x0c\x43HANNEL_CALL\x10\x00\x12\x0f\n\x0b\x43HANNEL_SMS\x10\x01*V\n\x0cReviewStatus\x12\x16\n\x12REVIEW_STATUS_TODO\x10\x00\x12\x16\n\x12REVIEW_STATUS_DONE\x10\x01\x12\x16\n\x12REVIEW_STATUS_NONE\x10\x02\x42\x8e\x01\n\x15\x63om.wfo.vanalytics.v2B\x0fTranscriptProtoP\x01\xa2\x02\x03WVX\xaa\x02\x11Wfo.Vanalytics.V2\xca\x02\x11Wfo\\Vanalytics\\V2\xe2\x02\x1dWfo\\Vanalytics\\V2\\GPBMetadata\xea\x02\x13Wfo::Vanalytics::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wfo.vanalytics.v2.transcript_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.wfo.vanalytics.v2B\017TranscriptProtoP\001\242\002\003WVX\252\002\021Wfo.Vanalytics.V2\312\002\021Wfo\\Vanalytics\\V2\342\002\035Wfo\\Vanalytics\\V2\\GPBMetadata\352\002\023Wfo::Vanalytics::V2'
  _globals['_CALL_AGENTRESPONSEENTRY']._loaded_options = None
  _globals['_CALL_AGENTRESPONSEENTRY']._serialized_options = b'8\001'
  _globals['_CHANNEL']._serialized_start=14399
  _globals['_CHANNEL']._serialized_end=14443
  _globals['_REVIEWSTATUS']._serialized_start=14445
  _globals['_REVIEWSTATUS']._serialized_end=14531
  _globals['_TRANSCRIPT']._serialized_start=252
  _globals['_TRANSCRIPT']._serialized_end=653
  _globals['_FLAGSUMMARY']._serialized_start=656
  _globals['_FLAGSUMMARY']._serialized_end=1639
  _globals['_FLAGSUMMARY_NEEDREVIEW']._serialized_start=969
  _globals['_FLAGSUMMARY_NEEDREVIEW']._serialized_end=1102
  _globals['_FLAGSUMMARY_FLAG']._serialized_start=1105
  _globals['_FLAGSUMMARY_FLAG']._serialized_end=1408
  _globals['_FLAGSUMMARY_FILTER']._serialized_start=1411
  _globals['_FLAGSUMMARY_FILTER']._serialized_end=1550
  _globals['_FLAGSUMMARY_REVIEW']._serialized_start=1552
  _globals['_FLAGSUMMARY_REVIEW']._serialized_end=1639
  _globals['_SMS']._serialized_start=1642
  _globals['_SMS']._serialized_end=1940
  _globals['_SMS_THREAD']._serialized_start=1749
  _globals['_SMS_THREAD']._serialized_end=1858
  _globals['_SMS_SEGMENT']._serialized_start=1860
  _globals['_SMS_SEGMENT']._serialized_end=1940
  _globals['_CALL']._serialized_start=1943
  _globals['_CALL']._serialized_end=3660
  _globals['_CALL_AGENTRESPONSEENTRY']._serialized_start=2593
  _globals['_CALL_AGENTRESPONSEENTRY']._serialized_end=2696
  _globals['_CALL_AGENTRESPONSE']._serialized_start=2698
  _globals['_CALL_AGENTRESPONSE']._serialized_end=2737
  _globals['_CALL_THREAD']._serialized_start=2739
  _globals['_CALL_THREAD']._serialized_end=2849
  _globals['_CALL_SEGMENT']._serialized_start=1860
  _globals['_CALL_SEGMENT']._serialized_end=1940
  _globals['_CALL_TALKOVER']._serialized_start=2934
  _globals['_CALL_TALKOVER']._serialized_end=3297
  _globals['_CALL_TALKOVER_DURATION']._serialized_start=3125
  _globals['_CALL_TALKOVER_DURATION']._serialized_end=3261
  _globals['_CALL_TALKOVER_OCCURRENCE']._serialized_start=3263
  _globals['_CALL_TALKOVER_OCCURRENCE']._serialized_end=3297
  _globals['_CALL_SILENCE']._serialized_start=3300
  _globals['_CALL_SILENCE']._serialized_end=3660
  _globals['_CALL_SILENCE_DURATION']._serialized_start=3125
  _globals['_CALL_SILENCE_DURATION']._serialized_end=3261
  _globals['_CALL_SILENCE_OCCURRENCE']._serialized_start=3263
  _globals['_CALL_SILENCE_OCCURRENCE']._serialized_end=3297
  _globals['_SEARCHTRANSCRIPTSREQUEST']._serialized_start=3663
  _globals['_SEARCHTRANSCRIPTSREQUEST']._serialized_end=3970
  _globals['_HIGHLIGHT']._serialized_start=3972
  _globals['_HIGHLIGHT']._serialized_end=4031
  _globals['_SEARCHTRANSCRIPTSRESPONSE']._serialized_start=4034
  _globals['_SEARCHTRANSCRIPTSRESPONSE']._serialized_end=4253
  _globals['_SEARCHTRANSCRIPTSRESPONSE_HIT']._serialized_start=4173
  _globals['_SEARCHTRANSCRIPTSRESPONSE_HIT']._serialized_end=4253
  _globals['_TRANSCRIPTBOOLQUERY']._serialized_start=4255
  _globals['_TRANSCRIPTBOOLQUERY']._serialized_end=4344
  _globals['_TRANSCRIPTQUERY']._serialized_start=4347
  _globals['_TRANSCRIPTQUERY']._serialized_end=13627
  _globals['_TRANSCRIPTQUERY_PHONE']._serialized_start=4973
  _globals['_TRANSCRIPTQUERY_PHONE']._serialized_end=6374
  _globals['_TRANSCRIPTQUERY_PHONE_CC']._serialized_start=5840
  _globals['_TRANSCRIPTQUERY_PHONE_CC']._serialized_end=5862
  _globals['_TRANSCRIPTQUERY_PHONE_NDC']._serialized_start=5864
  _globals['_TRANSCRIPTQUERY_PHONE_NDC']._serialized_end=5887
  _globals['_TRANSCRIPTQUERY_PHONE_PREFIX']._serialized_start=5889
  _globals['_TRANSCRIPTQUERY_PHONE_PREFIX']._serialized_end=5915
  _globals['_TRANSCRIPTQUERY_PHONE_CITY']._serialized_start=5917
  _globals['_TRANSCRIPTQUERY_PHONE_CITY']._serialized_end=5941
  _globals['_TRANSCRIPTQUERY_PHONE_ISO2']._serialized_start=5943
  _globals['_TRANSCRIPTQUERY_PHONE_ISO2']._serialized_end=5967
  _globals['_TRANSCRIPTQUERY_PHONE_REGIONCODE']._serialized_start=5969
  _globals['_TRANSCRIPTQUERY_PHONE_REGIONCODE']._serialized_end=5999
  _globals['_TRANSCRIPTQUERY_PHONE_REGIONNAME']._serialized_start=6001
  _globals['_TRANSCRIPTQUERY_PHONE_REGIONNAME']._serialized_end=6031
  _globals['_TRANSCRIPTQUERY_PHONE_TIMEZONE']._serialized_start=6033
  _globals['_TRANSCRIPTQUERY_PHONE_TIMEZONE']._serialized_end=6061
  _globals['_TRANSCRIPTQUERY_PHONE_TYPE']._serialized_start=6063
  _globals['_TRANSCRIPTQUERY_PHONE_TYPE']._serialized_end=6087
  _globals['_TRANSCRIPTQUERY_PHONE_UTC']._serialized_start=6089
  _globals['_TRANSCRIPTQUERY_PHONE_UTC']._serialized_end=6112
  _globals['_TRANSCRIPTQUERY_PHONE_LOCATION']._serialized_start=6115
  _globals['_TRANSCRIPTQUERY_PHONE_LOCATION']._serialized_end=6349
  _globals['_TRANSCRIPTQUERY_PHONE_LOCATION_ZIPCODEPROXIMITY']._serialized_start=6241
  _globals['_TRANSCRIPTQUERY_PHONE_LOCATION_ZIPCODEPROXIMITY']._serialized_end=6349
  _globals['_TRANSCRIPTQUERY_PHONE_RAW']._serialized_start=6351
  _globals['_TRANSCRIPTQUERY_PHONE_RAW']._serialized_end=6374
  _globals['_TRANSCRIPTQUERY_TRANSCRIPTSID']._serialized_start=6376
  _globals['_TRANSCRIPTQUERY_TRANSCRIPTSID']._serialized_end=6409
  _globals['_TRANSCRIPTQUERY_CHANNEL']._serialized_start=6411
  _globals['_TRANSCRIPTQUERY_CHANNEL']._serialized_end=6466
  _globals['_TRANSCRIPTQUERY_METADATA']._serialized_start=6469
  _globals['_TRANSCRIPTQUERY_METADATA']._serialized_end=6598
  _globals['_TRANSCRIPTQUERY_CALL']._serialized_start=6601
  _globals['_TRANSCRIPTQUERY_CALL']._serialized_end=11423
  _globals['_TRANSCRIPTQUERY_CALL_HUNTGROUPSIDS']._serialized_start=7505
  _globals['_TRANSCRIPTQUERY_CALL_HUNTGROUPSIDS']._serialized_end=7538
  _globals['_TRANSCRIPTQUERY_CALL_AGENTRESPONSE']._serialized_start=7541
  _globals['_TRANSCRIPTQUERY_CALL_AGENTRESPONSE']._serialized_end=8403
  _globals['_TRANSCRIPTQUERY_CALL_AGENTRESPONSE_VALUES']._serialized_start=7972
  _globals['_TRANSCRIPTQUERY_CALL_AGENTRESPONSE_VALUES']._serialized_end=8057
  _globals['_TRANSCRIPTQUERY_CALL_AGENTRESPONSE_NUMBERS']._serialized_start=8060
  _globals['_TRANSCRIPTQUERY_CALL_AGENTRESPONSE_NUMBERS']._serialized_end=8319
  _globals['_TRANSCRIPTQUERY_CALL_AGENTRESPONSE_KEY']._serialized_start=8321
  _globals['_TRANSCRIPTQUERY_CALL_AGENTRESPONSE_KEY']._serialized_end=8403
  _globals['_TRANSCRIPTQUERY_CALL_CALLTYPE']._serialized_start=8405
  _globals['_TRANSCRIPTQUERY_CALL_CALLTYPE']._serialized_end=8461
  _globals['_TRANSCRIPTQUERY_CALL_GROUPNAME']._serialized_start=8463
  _globals['_TRANSCRIPTQUERY_CALL_GROUPNAME']._serialized_end=8492
  _globals['_TRANSCRIPTQUERY_CALL_CALLSID']._serialized_start=8494
  _globals['_TRANSCRIPTQUERY_CALL_CALLSID']._serialized_end=8521
  _globals['_TRANSCRIPTQUERY_CALL_CALLERID']._serialized_start=8523
  _globals['_TRANSCRIPTQUERY_CALL_CALLERID']._serialized_end=8551
  _globals['_TRANSCRIPTQUERY_CALL_AUDIOTIME']._serialized_start=8554
  _globals['_TRANSCRIPTQUERY_CALL_AUDIOTIME']._serialized_end=8749
  _globals['_TRANSCRIPTQUERY_CALL_TALKTIME']._serialized_start=8752
  _globals['_TRANSCRIPTQUERY_CALL_TALKTIME']._serialized_end=8938
  _globals['_TRANSCRIPTQUERY_CALL_TALKOVER']._serialized_start=8941
  _globals['_TRANSCRIPTQUERY_CALL_TALKOVER']._serialized_end=10183
  _globals['_TRANSCRIPTQUERY_CALL_TALKOVER_DURATIONTOTAL']._serialized_start=9381
  _globals['_TRANSCRIPTQUERY_CALL_TALKOVER_DURATIONTOTAL']._serialized_end=9572
  _globals['_TRANSCRIPTQUERY_CALL_TALKOVER_DURATIONMAX']._serialized_start=9575
  _globals['_TRANSCRIPTQUERY_CALL_TALKOVER_DURATIONMAX']._serialized_end=9764
  _globals['_TRANSCRIPTQUERY_CALL_TALKOVER_OCCURRENCETOTAL']._serialized_start=9767
  _globals['_TRANSCRIPTQUERY_CALL_TALKOVER_OCCURRENCETOTAL']._serialized_end=9972
  _globals['_TRANSCRIPTQUERY_CALL_TALKOVER_DURATIONPERCENTAGE']._serialized_start=9975
  _globals['_TRANSCRIPTQUERY_CALL_TALKOVER_DURATIONPERCENTAGE']._serialized_end=10183
  _globals['_TRANSCRIPTQUERY_CALL_SILENCE']._serialized_start=10186
  _globals['_TRANSCRIPTQUERY_CALL_SILENCE']._serialized_end=11423
  _globals['_TRANSCRIPTQUERY_CALL_SILENCE_DURATIONTOTAL']._serialized_start=9381
  _globals['_TRANSCRIPTQUERY_CALL_SILENCE_DURATIONTOTAL']._serialized_end=9572
  _globals['_TRANSCRIPTQUERY_CALL_SILENCE_DURATIONMAX']._serialized_start=9575
  _globals['_TRANSCRIPTQUERY_CALL_SILENCE_DURATIONMAX']._serialized_end=9764
  _globals['_TRANSCRIPTQUERY_CALL_SILENCE_OCCURRENCETOTAL']._serialized_start=9767
  _globals['_TRANSCRIPTQUERY_CALL_SILENCE_OCCURRENCETOTAL']._serialized_end=9972
  _globals['_TRANSCRIPTQUERY_CALL_SILENCE_DURATIONPERCENTAGE']._serialized_start=9975
  _globals['_TRANSCRIPTQUERY_CALL_SILENCE_DURATIONPERCENTAGE']._serialized_end=10183
  _globals['_TRANSCRIPTQUERY_SMS']._serialized_start=11426
  _globals['_TRANSCRIPTQUERY_SMS']._serialized_end=11567
  _globals['_TRANSCRIPTQUERY_SMS_CONVERSATIONSID']._serialized_start=11532
  _globals['_TRANSCRIPTQUERY_SMS_CONVERSATIONSID']._serialized_end=11567
  _globals['_TRANSCRIPTQUERY_THREADS']._serialized_start=11570
  _globals['_TRANSCRIPTQUERY_THREADS']._serialized_end=12286
  _globals['_TRANSCRIPTQUERY_THREADS_USERID']._serialized_start=11911
  _globals['_TRANSCRIPTQUERY_THREADS_USERID']._serialized_end=11937
  _globals['_TRANSCRIPTQUERY_THREADS_ID']._serialized_start=11939
  _globals['_TRANSCRIPTQUERY_THREADS_ID']._serialized_end=11961
  _globals['_TRANSCRIPTQUERY_THREADS_TEXT']._serialized_start=11964
  _globals['_TRANSCRIPTQUERY_THREADS_TEXT']._serialized_end=12286
  _globals['_TRANSCRIPTQUERY_THREADS_TEXT_TIMESPAN']._serialized_start=12182
  _globals['_TRANSCRIPTQUERY_THREADS_TEXT_TIMESPAN']._serialized_end=12286
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY']._serialized_start=12289
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY']._serialized_end=13238
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_NEEDREVIEW']._serialized_start=12647
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_NEEDREVIEW']._serialized_end=12786
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_NEEDREVIEW_FLAGSIDS']._serialized_start=12758
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_NEEDREVIEW_FLAGSIDS']._serialized_end=12786
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_REVIEWSTATUS']._serialized_start=12788
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_REVIEWSTATUS']._serialized_end=12853
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_FLAGS']._serialized_start=12856
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_FLAGS']._serialized_end=12999
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_FLAGS_FLAGSID']._serialized_start=12954
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_FLAGS_FLAGSID']._serialized_end=12999
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_COUNT']._serialized_start=13002
  _globals['_TRANSCRIPTQUERY_FLAGSUMMARY_COUNT']._serialized_end=13238
  _globals['_TRANSCRIPTQUERY_STARTTIME']._serialized_start=13241
  _globals['_TRANSCRIPTQUERY_STARTTIME']._serialized_end=13432
  _globals['_TRANSCRIPTQUERY_DELETETIME']._serialized_start=13435
  _globals['_TRANSCRIPTQUERY_DELETETIME']._serialized_end=13627
  _globals['_FUZZINESSAUTO']._serialized_start=13629
  _globals['_FUZZINESSAUTO']._serialized_end=13682
  _globals['_MATCH']._serialized_start=13685
  _globals['_MATCH']._serialized_end=13871
  _globals['_SPANNEAR']._serialized_start=13874
  _globals['_SPANNEAR']._serialized_end=14196
  _globals['_SPANNEAR_CLAUSE']._serialized_start=13996
  _globals['_SPANNEAR_CLAUSE']._serialized_end=14196
  _globals['_SPANTERM']._serialized_start=14198
  _globals['_SPANTERM']._serialized_end=14230
  _globals['_SPANFUZZY']._serialized_start=14233
  _globals['_SPANFUZZY']._serialized_end=14397
# @@protoc_insertion_point(module_scope)
