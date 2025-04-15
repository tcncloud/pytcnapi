# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/evaluation.proto
# Protobuf Python Version: 6.30.2
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
    2,
    '',
    'api/v1alpha1/scorecards/evaluation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(api/v1alpha1/scorecards/evaluation.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x15\x61pi/commons/acd.proto\x1a\x1d\x61pi/commons/omnichannel.proto\x1a\x1c\x61pi/commons/scorecards.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"R\n\x17\x43reateEvaluationRequest\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"S\n\x18\x43reateEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"\x8f\x01\n\x17UpdateEvaluationRequest\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"S\n\x18UpdateEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\">\n\x17\x44\x65leteEvaluationRequest\x12#\n\revaluation_id\x18\x02 \x01(\x03R\x0c\x65valuationId\"S\n\x18\x44\x65leteEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\";\n\x14GetEvaluationRequest\x12#\n\revaluation_id\x18\x02 \x01(\x03R\x0c\x65valuationId\"P\n\x15GetEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"=\n\x16ScoreEvaluationRequest\x12#\n\revaluation_id\x18\x03 \x01(\x03R\x0c\x65valuationId\"R\n\x17ScoreEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"\x8f\x04\n\x16ListEvaluationsRequest\x12\x1b\n\tscorer_id\x18\x02 \x03(\tR\x08scorerId\x12:\n\x0c\x63ompleted_at\x18\x03 \x01(\x0b\x32\x17.api.commons.TimeFilterR\x0b\x63ompletedAt\x12!\n\x0c\x63\x61tegory_ids\x18\x04 \x03(\x03R\x0b\x63\x61tegoryIds\x12$\n\x0e\x61gent_user_ids\x18\x05 \x03(\tR\x0c\x61gentUserIds\x12#\n\rscorecard_ids\x18\x06 \x03(\x03R\x0cscorecardIds\x12?\n\rreturn_fields\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0creturnFields\x12\x1d\n\nis_deleted\x18\x0b \x01(\x08R\tisDeleted\x12=\n\rchannel_types\x18\x0e \x03(\x0e\x32\x18.api.commons.ChannelTypeR\x0c\x63hannelTypes\x12\x19\n\x08order_by\x18\x0f \x01(\tR\x07orderBy\x12\x1b\n\tpage_size\x18\x10 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x11 \x01(\tR\tpageToken\x12\x38\n\x08statuses\x18\x12 \x03(\x0e\x32\x1c.api.commons.EvaluationStateR\x08statuses\"|\n\x17ListEvaluationsResponse\x12\x39\n\x0b\x65valuations\x18\x01 \x03(\x0b\x32\x17.api.commons.EvaluationR\x0b\x65valuations\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\x8e\x01\n\x1dPreviewEvaluationScoreRequest\x12\x37\n\nevaluation\x18\x02 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\x12\x34\n\tscorecard\x18\x03 \x01(\x0b\x32\x16.api.commons.ScorecardR\tscorecard\"Y\n\x1ePreviewEvaluationScoreResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"\xbe\x02\n\x1dListEvaluationsByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1b\n\tscorer_id\x18\x02 \x03(\tR\x08scorerId\x12:\n\x0c\x63ompleted_at\x18\x03 \x01(\x0b\x32\x17.api.commons.TimeFilterR\x0b\x63ompletedAt\x12!\n\x0c\x63\x61tegory_ids\x18\x04 \x03(\x03R\x0b\x63\x61tegoryIds\x12$\n\x0e\x61gent_user_ids\x18\x05 \x03(\tR\x0c\x61gentUserIds\x12#\n\rscorecard_ids\x18\x06 \x03(\x03R\x0cscorecardIds\x12?\n\rreturn_fields\x18\n \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0creturnFields\"\\\n\x1e\x44\x65leteEvaluationByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12#\n\revaluation_id\x18\x02 \x01(\x03R\x0c\x65valuationId\"\xa3\x02\n\x1c\x42ulkDeleteEvaluationsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12%\n\x0e\x65valuation_ids\x18\x02 \x03(\x03R\revaluationIds\x12:\n\x0c\x63ompleted_at\x18\x03 \x01(\x0b\x32\x17.api.commons.TimeFilterR\x0b\x63ompletedAt\x12!\n\x0c\x63\x61tegory_ids\x18\x04 \x03(\x03R\x0b\x63\x61tegoryIds\x12$\n\x0e\x61gent_user_ids\x18\x05 \x03(\tR\x0c\x61gentUserIds\x12#\n\rscorecard_ids\x18\x06 \x03(\x03R\x0cscorecardIds\x12\x1b\n\tscorer_id\x18\x07 \x03(\tR\x08scorerId\"5\n\x1d\x42ulkDeleteEvaluationsResponse\x12\x14\n\x05\x63ount\x18\x01 \x01(\x03R\x05\x63ount\"X\n\x18RestoreEvaluationRequest\x12#\n\revaluation_id\x18\x02 \x01(\x03R\x0c\x65valuationId\x12\x17\n\x07user_id\x18\x03 \x01(\tR\x06userId\"T\n\x19RestoreEvaluationResponse\x12\x37\n\nevaluation\x18\x01 \x01(\x0b\x32\x17.api.commons.EvaluationR\nevaluation\"\xdc\x02\n\x1fSampleAgentConversationsRequest\x12!\n\x0cscorecard_id\x18\x03 \x01(\x03R\x0bscorecardId\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x32\n\x15max_agent_evaluations\x18\x06 \x01(\x05R\x13maxAgentEvaluations\x12+\n\x11sample_percentage\x18\x07 \x01(\x05R\x10samplePercentage\x12$\n\x0e\x61gent_user_ids\x18\x08 \x03(\tR\x0c\x61gentUserIds\x12\x1d\n\nfilter_sid\x18\t \x01(\x03R\tfilterSid\"\x7f\n SampleAgentConversationsResponse\x12[\n\x13\x61gent_conversations\x18\x01 \x03(\x0b\x32*.api.v1alpha1.scorecards.AgentConversationR\x12\x61gentConversations\"\xe0\x07\n\x11\x41gentConversation\x12%\n\x0etranscript_sid\x18\x01 \x01(\x03R\rtranscriptSid\x12\x32\n\x07\x63hannel\x18\x02 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x07\x63hannel\x12\"\n\ragent_user_id\x18\x03 \x01(\tR\x0b\x61gentUserId\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12^\n\rcall_metadata\x18\n \x01(\x0b\x32\x37.api.v1alpha1.scorecards.AgentConversation.CallMetadataH\x00R\x0c\x63\x61llMetadata\x12[\n\x0csms_metadata\x18\x0b \x01(\x0b\x32\x36.api.v1alpha1.scorecards.AgentConversation.SmsMetadataH\x00R\x0bsmsMetadata\x12^\n\rchat_metadata\x18\x0c \x01(\x0b\x32\x37.api.v1alpha1.scorecards.AgentConversation.ChatMetadataH\x00R\x0c\x63hatMetadata\x1a\xac\x02\n\x0c\x43\x61llMetadata\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x02 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12>\n\rcall_duration\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0c\x63\x61llDuration\x12\x42\n\x0fspeech_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0espeechDuration\x12\x44\n\x10silence_duration\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0fsilenceDuration\x1a[\n\x0bSmsMetadata\x12)\n\x10\x63onversation_sid\x18\x01 \x01(\x03R\x0f\x63onversationSid\x12!\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03R\x0b\x63\x61mpaignSid\x1a\\\n\x0c\x43hatMetadata\x12)\n\x10\x63onversation_sid\x18\x01 \x01(\x03R\x0f\x63onversationSid\x12!\n\x0c\x63\x61mpaign_sid\x18\x02 \x01(\x03R\x0b\x63\x61mpaignSidB\n\n\x08metadataB\xac\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\x0f\x45valuationProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.evaluation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\017EvaluationProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_CREATEEVALUATIONREQUEST']._serialized_start=252
  _globals['_CREATEEVALUATIONREQUEST']._serialized_end=334
  _globals['_CREATEEVALUATIONRESPONSE']._serialized_start=336
  _globals['_CREATEEVALUATIONRESPONSE']._serialized_end=419
  _globals['_UPDATEEVALUATIONREQUEST']._serialized_start=422
  _globals['_UPDATEEVALUATIONREQUEST']._serialized_end=565
  _globals['_UPDATEEVALUATIONRESPONSE']._serialized_start=567
  _globals['_UPDATEEVALUATIONRESPONSE']._serialized_end=650
  _globals['_DELETEEVALUATIONREQUEST']._serialized_start=652
  _globals['_DELETEEVALUATIONREQUEST']._serialized_end=714
  _globals['_DELETEEVALUATIONRESPONSE']._serialized_start=716
  _globals['_DELETEEVALUATIONRESPONSE']._serialized_end=799
  _globals['_GETEVALUATIONREQUEST']._serialized_start=801
  _globals['_GETEVALUATIONREQUEST']._serialized_end=860
  _globals['_GETEVALUATIONRESPONSE']._serialized_start=862
  _globals['_GETEVALUATIONRESPONSE']._serialized_end=942
  _globals['_SCOREEVALUATIONREQUEST']._serialized_start=944
  _globals['_SCOREEVALUATIONREQUEST']._serialized_end=1005
  _globals['_SCOREEVALUATIONRESPONSE']._serialized_start=1007
  _globals['_SCOREEVALUATIONRESPONSE']._serialized_end=1089
  _globals['_LISTEVALUATIONSREQUEST']._serialized_start=1092
  _globals['_LISTEVALUATIONSREQUEST']._serialized_end=1619
  _globals['_LISTEVALUATIONSRESPONSE']._serialized_start=1621
  _globals['_LISTEVALUATIONSRESPONSE']._serialized_end=1745
  _globals['_PREVIEWEVALUATIONSCOREREQUEST']._serialized_start=1748
  _globals['_PREVIEWEVALUATIONSCOREREQUEST']._serialized_end=1890
  _globals['_PREVIEWEVALUATIONSCORERESPONSE']._serialized_start=1892
  _globals['_PREVIEWEVALUATIONSCORERESPONSE']._serialized_end=1981
  _globals['_LISTEVALUATIONSBYORGIDREQUEST']._serialized_start=1984
  _globals['_LISTEVALUATIONSBYORGIDREQUEST']._serialized_end=2302
  _globals['_DELETEEVALUATIONBYORGIDREQUEST']._serialized_start=2304
  _globals['_DELETEEVALUATIONBYORGIDREQUEST']._serialized_end=2396
  _globals['_BULKDELETEEVALUATIONSREQUEST']._serialized_start=2399
  _globals['_BULKDELETEEVALUATIONSREQUEST']._serialized_end=2690
  _globals['_BULKDELETEEVALUATIONSRESPONSE']._serialized_start=2692
  _globals['_BULKDELETEEVALUATIONSRESPONSE']._serialized_end=2745
  _globals['_RESTOREEVALUATIONREQUEST']._serialized_start=2747
  _globals['_RESTOREEVALUATIONREQUEST']._serialized_end=2835
  _globals['_RESTOREEVALUATIONRESPONSE']._serialized_start=2837
  _globals['_RESTOREEVALUATIONRESPONSE']._serialized_end=2921
  _globals['_SAMPLEAGENTCONVERSATIONSREQUEST']._serialized_start=2924
  _globals['_SAMPLEAGENTCONVERSATIONSREQUEST']._serialized_end=3272
  _globals['_SAMPLEAGENTCONVERSATIONSRESPONSE']._serialized_start=3274
  _globals['_SAMPLEAGENTCONVERSATIONSRESPONSE']._serialized_end=3401
  _globals['_AGENTCONVERSATION']._serialized_start=3404
  _globals['_AGENTCONVERSATION']._serialized_end=4396
  _globals['_AGENTCONVERSATION_CALLMETADATA']._serialized_start=3897
  _globals['_AGENTCONVERSATION_CALLMETADATA']._serialized_end=4197
  _globals['_AGENTCONVERSATION_SMSMETADATA']._serialized_start=4199
  _globals['_AGENTCONVERSATION_SMSMETADATA']._serialized_end=4290
  _globals['_AGENTCONVERSATION_CHATMETADATA']._serialized_start=4292
  _globals['_AGENTCONVERSATION_CHATMETADATA']._serialized_end=4384
# @@protoc_insertion_point(module_scope)
