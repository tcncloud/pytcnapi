# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/scorecards.proto
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
    'api/commons/scorecards.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from api.commons import omnichannel_pb2 as api_dot_commons_dot_omnichannel__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/commons/scorecards.proto\x12\x0b\x61pi.commons\x1a\x15\x61pi/commons/acd.proto\x1a\x1d\x61pi/commons/omnichannel.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xec\x01\n\nTimeFilter\x12*\n\x02\x65q\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02\x65q\x12,\n\x03gte\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03gte\x12,\n\x03lte\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03lte\x12*\n\x02gt\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02gt\x12*\n\x02lt\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x02lt\"\x96\x03\n\x08\x43\x61tegory\x12\x1f\n\x0b\x63\x61tegory_id\x18\x01 \x01(\x03R\ncategoryId\x12\x1b\n\tauthor_id\x18\x03 \x01(\tR\x08\x61uthorId\x12\x14\n\x05title\x18\x04 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12%\n\x0eskill_profiles\x18\x06 \x03(\x03R\rskillProfiles\x12\x18\n\x07version\x18\x07 \x01(\x05R\x07version\x12=\n\ncall_types\x18\n \x03(\x0e\x32\x1a.api.commons.CallType.EnumB\x02\x18\x01R\tcallTypes\x12\x1b\n\tis_system\x18\x0b \x01(\x08R\x08isSystem\x12>\n\rcategory_type\x18\x0c \x01(\x0e\x32\x19.api.commons.CategoryTypeR\x0c\x63\x61tegoryType\x12\x37\n\x18skill_profile_group_sids\x18\r \x03(\x03R\x15skillProfileGroupSids\"\xde\x07\n\nEvaluation\x12#\n\revaluation_id\x18\x02 \x01(\x03R\x0c\x65valuationId\x12!\n\x0cscorecard_id\x18\x03 \x01(\x03R\x0bscorecardId\x12\x1b\n\tscorer_id\x18\x04 \x01(\tR\x08scorerId\x12\x1d\n\x08\x63\x61ll_sid\x18\x06 \x01(\x03\x42\x02\x18\x01R\x07\x63\x61llSid\x12\x14\n\x05score\x18\x07 \x01(\x01R\x05score\x12G\n\x10\x65valuation_state\x18\x08 \x01(\x0e\x32\x1c.api.commons.EvaluationStateR\x0f\x65valuationState\x12O\n\x13\x65valuation_sections\x18\t \x03(\x0b\x32\x1e.api.commons.EvaluationSectionR\x12\x65valuationSections\x12=\n\x0c\x63ompleted_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x63ompletedAt\x12\x39\n\ndeleted_at\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tdeletedAt\x12\"\n\ragent_user_id\x18\r \x01(\tR\x0b\x61gentUserId\x12;\n\tcall_type\x18\x0e \x01(\x0e\x32\x1a.api.commons.CallType.EnumB\x02\x18\x01R\x08\x63\x61llType\x12%\n\x0etranscript_sid\x18\x0f \x01(\x03R\rtranscriptSid\x12H\n\rcustom_fields\x18\x11 \x03(\x0b\x32#.api.commons.Evaluation.CustomFieldR\x0c\x63ustomFields\x12\x1d\n\ndeleted_by\x18\x12 \x01(\tR\tdeletedBy\x12%\n\x0eis_recoverable\x18\x14 \x01(\x08R\risRecoverable\x12;\n\x0c\x63hannel_type\x18\x16 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\rcall_metadata\x18\x17 \x01(\x0b\x32\x19.api.commons.CallMetadataR\x0c\x63\x61llMetadata\x12V\n\x15\x63onversation_metadata\x18\x18 \x01(\x0b\x32!.api.commons.ConversationMetadataR\x14\x63onversationMetadata\x1a\x35\n\x0b\x43ustomField\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05\x66ield\x18\x02 \x01(\tR\x05\x66ield\"\xb0\x04\n\x11\x45valuationSection\x12\x32\n\x15\x65valuation_section_id\x18\x02 \x01(\x03R\x13\x65valuationSectionId\x12#\n\revaluation_id\x18\x03 \x01(\x03R\x0c\x65valuationId\x12\x1d\n\nsection_id\x18\x04 \x01(\x03R\tsectionId\x12\x16\n\x06points\x18\x05 \x01(\x05R\x06points\x12\'\n\x0fpossible_points\x18\x06 \x01(\x05R\x0epossiblePoints\x12\x1d\n\nsort_order\x18\x07 \x01(\x05R\tsortOrder\x12\x39\n\ndeleted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tdeletedAt\x12\x39\n\ncreated_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12R\n\x14\x65valuation_questions\x18\n \x03(\x0b\x32\x1f.api.commons.EvaluationQuestionR\x13\x65valuationQuestions\x12_\n\x19\x61uto_evaluation_questions\x18\x0b \x03(\x0b\x32#.api.commons.AutoEvaluationQuestionR\x17\x61utoEvaluationQuestions\x12\x18\n\x07skipped\x18\x0c \x01(\x08R\x07skipped\"\xb9\x04\n\x12\x45valuationQuestion\x12\x34\n\x16\x65valuation_question_id\x18\x02 \x01(\x03R\x14\x65valuationQuestionId\x12#\n\revaluation_id\x18\x03 \x01(\x03R\x0c\x65valuationId\x12\x32\n\x15scorecard_question_id\x18\x04 \x01(\x03R\x13scorecardQuestionId\x12\x18\n\x07skipped\x18\x05 \x01(\x08R\x07skipped\x12\x16\n\x06points\x18\x06 \x01(\x03R\x06points\x12@\n\x07\x61nswers\x18\x07 \x03(\x0b\x32&.api.commons.EvaluationQuestion.AnswerR\x07\x61nswers\x12\x32\n\x15\x65valuation_section_id\x18\x08 \x01(\x03R\x13\x65valuationSectionId\x12\x18\n\x07\x63omment\x18\t \x01(\tR\x07\x63omment\x12\x1d\n\nsort_order\x18\n \x01(\x05R\tsortOrder\x1a\xb2\x01\n\x06\x41nswer\x12#\n\ranswer_option\x18\x01 \x01(\tR\x0c\x61nswerOption\x12\x1c\n\x06points\x18\x02 \x01(\rB\x02\x18\x01H\x00R\x06points\x12\x34\n\tfail_type\x18\x03 \x01(\x0e\x32\x15.api.commons.FailTypeH\x00R\x08\x66\x61ilType\x12%\n\ranswer_points\x18\x04 \x01(\x05H\x00R\x0c\x61nswerPointsB\x08\n\x06result\"\xaa\x08\n\x0e\x41utoEvaluation\x12,\n\x12\x61uto_evaluation_id\x18\x02 \x01(\x03R\x10\x61utoEvaluationId\x12!\n\x0cscorecard_id\x18\x03 \x01(\x03R\x0bscorecardId\x12\x1d\n\x08\x63\x61ll_sid\x18\x04 \x01(\x03\x42\x02\x18\x01R\x07\x63\x61llSid\x12\"\n\ragent_user_id\x18\x05 \x01(\tR\x0b\x61gentUserId\x12\\\n\x18\x61uto_evaluation_sections\x18\x06 \x03(\x0b\x32\".api.commons.AutoEvaluationSectionR\x16\x61utoEvaluationSections\x12=\n\x0c\x63ompleted_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x63ompletedAt\x12\x39\n\ndeleted_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tdeletedAt\x12;\n\tcall_type\x18\t \x01(\x0e\x32\x1a.api.commons.CallType.EnumB\x02\x18\x01R\x08\x63\x61llType\x12%\n\x0etranscript_sid\x18\n \x01(\x03R\rtranscriptSid\x12-\n\x12\x65xpression_matched\x18\x0b \x01(\x08R\x11\x65xpressionMatched\x12\x35\n\nrisk_level\x18\x0c \x01(\x0e\x32\x16.api.commons.RiskLevelR\triskLevel\x12\x1f\n\x0b\x63\x61ll_length\x18\x10 \x01(\x05R\ncallLength\x12P\n\x0escorecard_info\x18\x11 \x01(\x0b\x32).api.commons.AutoEvaluation.ScorecardInfoR\rscorecardInfo\x12M\n\rcategory_info\x18\x12 \x01(\x0b\x32(.api.commons.AutoEvaluation.CategoryInfoR\x0c\x63\x61tegoryInfo\x12;\n\x0c\x63hannel_type\x18\x13 \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\rcall_metadata\x18\x14 \x01(\x0b\x32\x19.api.commons.CallMetadataR\x0c\x63\x61llMetadata\x12V\n\x15\x63onversation_metadata\x18\x15 \x01(\x0b\x32!.api.commons.ConversationMetadataR\x14\x63onversationMetadata\x1a%\n\rScorecardInfo\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x1a$\n\x0c\x43\x61tegoryInfo\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\"\xa3\x03\n\x16\x41utoEvaluationQuestion\x12=\n\x1b\x61uto_evaluation_question_id\x18\x02 \x01(\x03R\x18\x61utoEvaluationQuestionId\x12,\n\x12\x61uto_evaluation_id\x18\x03 \x01(\x03R\x10\x61utoEvaluationId\x12;\n\x1a\x61uto_evaluation_section_id\x18\x04 \x01(\x03R\x17\x61utoEvaluationSectionId\x12(\n\x10\x61uto_question_id\x18\x05 \x01(\x03R\x0e\x61utoQuestionId\x12\x18\n\x07\x66lagged\x18\x06 \x03(\x03R\x07\x66lagged\x12\x16\n\x06passed\x18\x07 \x01(\x08R\x06passed\x12\x1d\n\nsort_order\x18\x08 \x01(\x05R\tsortOrder\x12\x35\n\nrisk_level\x18\x0b \x01(\x0e\x32\x16.api.commons.RiskLevelR\triskLevel\x12-\n\x12\x65xpression_matched\x18\x0e \x01(\x08R\x11\x65xpressionMatched\"\xce\x03\n\x15\x41utoEvaluationSection\x12;\n\x1a\x61uto_evaluation_section_id\x18\x02 \x01(\x03R\x17\x61utoEvaluationSectionId\x12,\n\x12\x61uto_evaluation_id\x18\x03 \x01(\x03R\x10\x61utoEvaluationId\x12\x1d\n\nsection_id\x18\x04 \x01(\x03R\tsectionId\x12\x1d\n\nsort_order\x18\x05 \x01(\x05R\tsortOrder\x12\x39\n\ndeleted_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tdeletedAt\x12\x39\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12_\n\x19\x61uto_evaluation_questions\x18\x08 \x03(\x0b\x32#.api.commons.AutoEvaluationQuestionR\x17\x61utoEvaluationQuestions\x12\x35\n\nrisk_level\x18\t \x01(\x0e\x32\x16.api.commons.RiskLevelR\triskLevel\"\xef\x01\n\x08Question\x12\x1f\n\x0bquestion_id\x18\x02 \x01(\x03R\nquestionId\x12\x1b\n\tauthor_id\x18\x03 \x01(\tR\x08\x61uthorId\x12\x1a\n\x08question\x18\x04 \x01(\tR\x08question\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12\x35\n\ncategories\x18\x06 \x03(\x0b\x32\x15.api.commons.CategoryR\ncategories\x12\x30\n\x05\x66ocus\x18\x07 \x01(\x0e\x32\x1a.api.commons.QuestionFocusR\x05\x66ocus\"\xb3\x05\n\x11ScorecardQuestion\x12\x32\n\x15scorecard_question_id\x18\x02 \x01(\x03R\x13scorecardQuestionId\x12\x1a\n\x08question\x18\x03 \x01(\tR\x08question\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x1f\n\x0bquestion_id\x18\x05 \x01(\x03R\nquestionId\x12\x1d\n\nallow_skip\x18\x06 \x01(\x08R\tallowSkip\x12?\n\x07\x61nswers\x18\x07 \x03(\x0b\x32%.api.commons.ScorecardQuestion.AnswerR\x07\x61nswers\x12M\n\x0cmulti_select\x18\x08 \x01(\x0b\x32*.api.commons.ScorecardQuestion.MultiSelectR\x0bmultiSelect\x12!\n\x0cscorecard_id\x18\t \x01(\x03R\x0bscorecardId\x12\x1d\n\nsection_id\x18\n \x01(\x03R\tsectionId\x12\x18\n\x07version\x18\x0b \x01(\x05R\x07version\x12\x1d\n\nsort_order\x18\x0c \x01(\x05R\tsortOrder\x1a\xb2\x01\n\x06\x41nswer\x12#\n\ranswer_option\x18\x01 \x01(\tR\x0c\x61nswerOption\x12\x1c\n\x06points\x18\x02 \x01(\rB\x02\x18\x01H\x00R\x06points\x12\x34\n\tfail_type\x18\x03 \x01(\x0e\x32\x15.api.commons.FailTypeH\x00R\x08\x66\x61ilType\x12%\n\ranswer_points\x18\x04 \x01(\x05H\x00R\x0c\x61nswerPointsB\x08\n\x06result\x1a,\n\x0bMultiSelect\x12\x1d\n\nmax_points\x18\x01 \x01(\x03R\tmaxPoints\"\x99\x03\n\x07Section\x12\x1d\n\nsection_id\x18\x02 \x01(\x03R\tsectionId\x12!\n\x0cscorecard_id\x18\x03 \x01(\x03R\x0bscorecardId\x12\x14\n\x05title\x18\x04 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12\x16\n\x06weight\x18\x06 \x01(\rR\x06weight\x12<\n\tquestions\x18\x07 \x03(\x0b\x32\x1e.api.commons.ScorecardQuestionR\tquestions\x12\x18\n\x07version\x18\x08 \x01(\x05R\x07version\x12\x1d\n\nsort_order\x18\t \x01(\x05R\tsortOrder\x12@\n\x0e\x61uto_questions\x18\x0b \x03(\x0b\x32\x19.api.commons.AutoQuestionR\rautoQuestions\x12\x43\n\x0fsmart_questions\x18\x0c \x03(\x0b\x32\x1a.api.commons.SmartQuestionR\x0esmartQuestions\"\xa5\x07\n\tScorecard\x12!\n\x0cscorecard_id\x18\x02 \x01(\x03R\x0bscorecardId\x12\x1b\n\tauthor_id\x18\x03 \x01(\tR\x08\x61uthorId\x12\x14\n\x05title\x18\x04 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12\x1d\n\npass_score\x18\x06 \x01(\x01R\tpassScore\x12\x35\n\nscore_type\x18\x07 \x01(\x0e\x32\x16.api.commons.ScoreTypeR\tscoreType\x12\x44\n\x0f\x65valuation_type\x18\x08 \x01(\x0e\x32\x1b.api.commons.EvaluationTypeR\x0e\x65valuationType\x12%\n\x0e\x61llow_feedback\x18\n \x01(\x08R\rallowFeedback\x12-\n\x12\x64istribute_weights\x18\x0b \x01(\x08R\x11\x64istributeWeights\x12\x31\n\x08\x63\x61tegory\x18\x0c \x01(\x0b\x32\x15.api.commons.CategoryR\x08\x63\x61tegory\x12\x30\n\x08sections\x18\r \x03(\x0b\x32\x14.api.commons.SectionR\x08sections\x12\x18\n\x07version\x18\x0e \x01(\x05R\x07version\x12\x31\n\x05state\x18\x0f \x01(\x0e\x32\x1b.api.commons.ScorecardStateR\x05state\x12\x1e\n\tis_ad_hoc\x18\x10 \x01(\x08\x42\x02\x18\x01R\x07isAdHoc\x12*\n\x11\x63ustom_field_keys\x18\x13 \x03(\tR\x0f\x63ustomFieldKeys\x12\x39\n\ncall_types\x18\x14 \x03(\x0e\x32\x1a.api.commons.CallType.EnumR\tcallTypes\x12\x39\n\nupdated_at\x18\x15 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tupdatedAt\x12\x34\n\x08\x63hannels\x18\x16 \x03(\x0e\x32\x18.api.commons.ChannelTypeR\x08\x63hannels\x12I\n\x13minimum_call_length\x18\x17 \x01(\x0b\x32\x19.google.protobuf.DurationR\x11minimumCallLength\x12\x39\n\x19minimum_sms_message_count\x18\x18 \x01(\x05R\x16minimumSmsMessageCount\"\xad\x05\n\x0c\x41utoQuestion\x12(\n\x10\x61uto_question_id\x18\x02 \x01(\x03R\x0e\x61utoQuestionId\x12\x19\n\x08\x66lag_sid\x18\x03 \x01(\x03R\x07\x66lagSid\x12!\n\x0cscorecard_id\x18\x05 \x01(\x03R\x0bscorecardId\x12&\n\x0f\x61uto_section_id\x18\x06 \x01(\x03R\rautoSectionId\x12\x1d\n\nsort_order\x18\x07 \x01(\x05R\tsortOrder\x12K\n\x0f\x66lag_expression\x18\n \x01(\x0b\x32\".api.commons.AutoQuestion.FlagExprR\x0e\x66lagExpression\x12\x1a\n\x08question\x18\x0b \x01(\tR\x08question\x12 \n\x0b\x64\x65scription\x18\x0c \x01(\tR\x0b\x64\x65scription\x12\x1f\n\x0bquestion_id\x18\r \x01(\x03R\nquestionId\x12\x35\n\nrisk_level\x18\x0e \x01(\x0e\x32\x16.api.commons.RiskLevelR\triskLevel\x1a\x8a\x02\n\x08\x46lagExpr\x12\x34\n\x03\x61nd\x18\x01 \x03(\x0b\x32\".api.commons.AutoQuestion.FlagExprR\x03\x61nd\x12\x32\n\x02or\x18\x02 \x03(\x0b\x32\".api.commons.AutoQuestion.FlagExprR\x02or\x12;\n\x04\x66lag\x18\x03 \x01(\x0b\x32\'.api.commons.AutoQuestion.FlagExpr.FlagR\x04\x66lag\x12\x34\n\x03not\x18\x04 \x01(\x0b\x32\".api.commons.AutoQuestion.FlagExprR\x03not\x1a!\n\x04\x46lag\x12\x19\n\x08\x66lag_sid\x18\x01 \x01(\x03R\x07\x66lagSid\"\xe6\x03\n\rSmartQuestion\x12*\n\x11smart_question_id\x18\x02 \x01(\x03R\x0fsmartQuestionId\x12!\n\x0cscorecard_id\x18\x03 \x01(\x03R\x0bscorecardId\x12\x1d\n\nsection_id\x18\x04 \x01(\x03R\tsectionId\x12\x1f\n\x0bquestion_id\x18\x05 \x01(\x03R\nquestionId\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12\x1a\n\x08question\x18\x07 \x01(\tR\x08question\x12;\n\x07\x61nswers\x18\x08 \x03(\x0b\x32!.api.commons.SmartQuestion.AnswerR\x07\x61nswers\x12\x30\n\x05\x66ocus\x18\x0b \x01(\x0e\x32\x1a.api.commons.QuestionFocusR\x05\x66ocus\x12\x1d\n\nsort_order\x18\x0c \x01(\x05R\tsortOrder\x1az\n\x06\x41nswer\x12\x16\n\x06\x61nswer\x18\x01 \x01(\tR\x06\x61nswer\x12\x18\n\x06points\x18\x02 \x01(\x05H\x00R\x06points\x12\x34\n\tfail_type\x18\x03 \x01(\x0e\x32\x15.api.commons.FailTypeH\x00R\x08\x66\x61ilTypeB\x08\n\x06result\"\xcf\x05\n\x0fSmartEvaluation\x12.\n\x13smart_evaluation_id\x18\x02 \x01(\x03R\x11smartEvaluationId\x12!\n\x0cscorecard_id\x18\x03 \x01(\x03R\x0bscorecardId\x12%\n\x0etranscript_sid\x18\x04 \x01(\x03R\rtranscriptSid\x12\"\n\ragent_user_id\x18\x05 \x01(\tR\x0b\x61gentUserId\x12\x14\n\x05score\x18\x06 \x01(\x01R\x05score\x12\'\n\x0fscoring_version\x18\x07 \x01(\x05R\x0escoringVersion\x12+\n\x11scorecard_version\x18\x08 \x01(\x05R\x10scorecardVersion\x12?\n\rcomplete_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x63ompleteTime\x12;\n\x0b\x64\x65lete_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12_\n\x19smart_evaluation_sections\x18\x0b \x03(\x0b\x32#.api.commons.SmartEvaluationSectionR\x17smartEvaluationSections\x12;\n\x0c\x63hannel_type\x18\x0c \x01(\x0e\x32\x18.api.commons.ChannelTypeR\x0b\x63hannelType\x12>\n\rcall_metadata\x18\r \x01(\x0b\x32\x19.api.commons.CallMetadataR\x0c\x63\x61llMetadata\x12V\n\x15\x63onversation_metadata\x18\x0e \x01(\x0b\x32!.api.commons.ConversationMetadataR\x14\x63onversationMetadata\"b\n\x0c\x43\x61llMetadata\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x02 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\"E\n\x14\x43onversationMetadata\x12-\n\x10\x63onversation_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0f\x63onversationSid\"\xd6\x02\n\x16SmartEvaluationSection\x12\x1d\n\nsection_id\x18\x04 \x01(\x03R\tsectionId\x12\x16\n\x06points\x18\x05 \x01(\x05R\x06points\x12\'\n\x0fpossible_points\x18\x06 \x01(\x05R\x0epossiblePoints\x12;\n\x0b\x63reate_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0b\x64\x65lete_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x12\x62\n\x1asmart_evaluation_questions\x18\t \x03(\x0b\x32$.api.commons.SmartEvaluationQuestionR\x18smartEvaluationQuestions\"\xed\x03\n\x17SmartEvaluationQuestion\x12*\n\x11smart_question_id\x18\x05 \x01(\x03R\x0fsmartQuestionId\x12\x16\n\x06points\x18\x06 \x01(\x05R\x06points\x12\'\n\x0fpossible_points\x18\x07 \x01(\x05R\x0epossiblePoints\x12\x43\n\x06\x61nswer\x18\x08 \x01(\x0b\x32+.api.commons.SmartEvaluationQuestion.AnswerR\x06\x61nswer\x12;\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0b\x64\x65lete_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ndeleteTime\x1a\xa5\x01\n\x06\x41nswer\x12\x16\n\x06\x61nswer\x18\x01 \x01(\tR\x06\x61nswer\x12\x1c\n\x06points\x18\x02 \x01(\rB\x02\x18\x01H\x00R\x06points\x12\x34\n\tfail_type\x18\x03 \x01(\x0e\x32\x15.api.commons.FailTypeH\x00R\x08\x66\x61ilType\x12%\n\ranswer_points\x18\x04 \x01(\x05H\x00R\x0c\x61nswerPointsB\x08\n\x06result*=\n\x0c\x43\x61tegoryType\x12\x0b\n\x07INVALID\x10\x00\x12\x0f\n\x0bSKILL_CALLS\x10\x01\x12\x0f\n\x0bMANUAL_DIAL\x10\x02*L\n\x0e\x45valuationType\x12\x13\n\x0f\x45VALUATE_MANUAL\x10\x00\x12\x11\n\rEVALUATE_AUTO\x10\x01\x12\x12\n\x0e\x45VALUATE_SMART\x10\x02*V\n\tScoreType\x12\x14\n\x10SCORE_SIMPLE_SUM\x10\x00\x12\x16\n\x12SCORE_WEIGHTED_SUM\x10\x01\x12\x1b\n\x17SCORE_EVEN_WEIGHTED_SUM\x10\x02*C\n\x08\x46\x61ilType\x12\x11\n\rFAIL_QUESTION\x10\x00\x12\x10\n\x0c\x46\x41IL_SECTION\x10\x01\x12\x12\n\x0e\x46\x41IL_SCORECARD\x10\x02*f\n\rQuestionFocus\x12\x1e\n\x1aQUESTION_FOCUS_UNSPECIFIED\x10\x00\x12\x18\n\x14QUESTION_FOCUS_AGENT\x10\x01\x12\x1b\n\x17QUESTION_FOCUS_CUSTOMER\x10\x02*\xb7\x01\n\x0eScorecardState\x12\x16\n\x12SCORECARD_IS_DRAFT\x10\x00\x12\x16\n\x12SCORECARD_IS_READY\x10\x01\x12\x17\n\x13SCORECARD_IS_IN_USE\x10\x02\x12\x19\n\x15SCORECARD_IS_TEMPLATE\x10\x03\x12\x1f\n\x1bSCORECARD_IS_READY_DISABLED\x10\x04\x12 \n\x1cSCORECARD_IS_IN_USE_DISABLED\x10\x05*[\n\x0f\x45valuationState\x12\x1a\n\x16\x45VALUATION_IN_PROGRESS\x10\x00\x12\x15\n\x11\x45VALUATION_PASSED\x10\x01\x12\x15\n\x11\x45VALUATION_FAILED\x10\x02*z\n\tRiskLevel\x12\x13\n\x0fRISK_LEVEL_NONE\x10\x00\x12\x12\n\x0eRISK_LEVEL_LOW\x10\x01\x12\x15\n\x11RISK_LEVEL_MEDIUM\x10\x02\x12\x13\n\x0fRISK_LEVEL_HIGH\x10\x03\x12\x18\n\x14RISK_LEVEL_RISK_FREE\x10\x04\x42o\n\x0f\x63om.api.commonsB\x0fScorecardsProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.scorecards_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\017ScorecardsProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_CATEGORY'].fields_by_name['call_types']._loaded_options = None
  _globals['_CATEGORY'].fields_by_name['call_types']._serialized_options = b'\030\001'
  _globals['_EVALUATION'].fields_by_name['call_sid']._loaded_options = None
  _globals['_EVALUATION'].fields_by_name['call_sid']._serialized_options = b'\030\001'
  _globals['_EVALUATION'].fields_by_name['call_type']._loaded_options = None
  _globals['_EVALUATION'].fields_by_name['call_type']._serialized_options = b'\030\001'
  _globals['_EVALUATIONQUESTION_ANSWER'].fields_by_name['points']._loaded_options = None
  _globals['_EVALUATIONQUESTION_ANSWER'].fields_by_name['points']._serialized_options = b'\030\001'
  _globals['_AUTOEVALUATION'].fields_by_name['call_sid']._loaded_options = None
  _globals['_AUTOEVALUATION'].fields_by_name['call_sid']._serialized_options = b'\030\001'
  _globals['_AUTOEVALUATION'].fields_by_name['call_type']._loaded_options = None
  _globals['_AUTOEVALUATION'].fields_by_name['call_type']._serialized_options = b'\030\001'
  _globals['_SCORECARDQUESTION_ANSWER'].fields_by_name['points']._loaded_options = None
  _globals['_SCORECARDQUESTION_ANSWER'].fields_by_name['points']._serialized_options = b'\030\001'
  _globals['_SCORECARD'].fields_by_name['is_ad_hoc']._loaded_options = None
  _globals['_SCORECARD'].fields_by_name['is_ad_hoc']._serialized_options = b'\030\001'
  _globals['_CONVERSATIONMETADATA'].fields_by_name['conversation_sid']._loaded_options = None
  _globals['_CONVERSATIONMETADATA'].fields_by_name['conversation_sid']._serialized_options = b'0\001'
  _globals['_SMARTEVALUATIONQUESTION_ANSWER'].fields_by_name['points']._loaded_options = None
  _globals['_SMARTEVALUATIONQUESTION_ANSWER'].fields_by_name['points']._serialized_options = b'\030\001'
  _globals['_CATEGORYTYPE']._serialized_start=10091
  _globals['_CATEGORYTYPE']._serialized_end=10152
  _globals['_EVALUATIONTYPE']._serialized_start=10154
  _globals['_EVALUATIONTYPE']._serialized_end=10230
  _globals['_SCORETYPE']._serialized_start=10232
  _globals['_SCORETYPE']._serialized_end=10318
  _globals['_FAILTYPE']._serialized_start=10320
  _globals['_FAILTYPE']._serialized_end=10387
  _globals['_QUESTIONFOCUS']._serialized_start=10389
  _globals['_QUESTIONFOCUS']._serialized_end=10491
  _globals['_SCORECARDSTATE']._serialized_start=10494
  _globals['_SCORECARDSTATE']._serialized_end=10677
  _globals['_EVALUATIONSTATE']._serialized_start=10679
  _globals['_EVALUATIONSTATE']._serialized_end=10770
  _globals['_RISKLEVEL']._serialized_start=10772
  _globals['_RISKLEVEL']._serialized_end=10894
  _globals['_TIMEFILTER']._serialized_start=165
  _globals['_TIMEFILTER']._serialized_end=401
  _globals['_CATEGORY']._serialized_start=404
  _globals['_CATEGORY']._serialized_end=810
  _globals['_EVALUATION']._serialized_start=813
  _globals['_EVALUATION']._serialized_end=1803
  _globals['_EVALUATION_CUSTOMFIELD']._serialized_start=1750
  _globals['_EVALUATION_CUSTOMFIELD']._serialized_end=1803
  _globals['_EVALUATIONSECTION']._serialized_start=1806
  _globals['_EVALUATIONSECTION']._serialized_end=2366
  _globals['_EVALUATIONQUESTION']._serialized_start=2369
  _globals['_EVALUATIONQUESTION']._serialized_end=2938
  _globals['_EVALUATIONQUESTION_ANSWER']._serialized_start=2760
  _globals['_EVALUATIONQUESTION_ANSWER']._serialized_end=2938
  _globals['_AUTOEVALUATION']._serialized_start=2941
  _globals['_AUTOEVALUATION']._serialized_end=4007
  _globals['_AUTOEVALUATION_SCORECARDINFO']._serialized_start=3932
  _globals['_AUTOEVALUATION_SCORECARDINFO']._serialized_end=3969
  _globals['_AUTOEVALUATION_CATEGORYINFO']._serialized_start=3971
  _globals['_AUTOEVALUATION_CATEGORYINFO']._serialized_end=4007
  _globals['_AUTOEVALUATIONQUESTION']._serialized_start=4010
  _globals['_AUTOEVALUATIONQUESTION']._serialized_end=4429
  _globals['_AUTOEVALUATIONSECTION']._serialized_start=4432
  _globals['_AUTOEVALUATIONSECTION']._serialized_end=4894
  _globals['_QUESTION']._serialized_start=4897
  _globals['_QUESTION']._serialized_end=5136
  _globals['_SCORECARDQUESTION']._serialized_start=5139
  _globals['_SCORECARDQUESTION']._serialized_end=5830
  _globals['_SCORECARDQUESTION_ANSWER']._serialized_start=2760
  _globals['_SCORECARDQUESTION_ANSWER']._serialized_end=2938
  _globals['_SCORECARDQUESTION_MULTISELECT']._serialized_start=5786
  _globals['_SCORECARDQUESTION_MULTISELECT']._serialized_end=5830
  _globals['_SECTION']._serialized_start=5833
  _globals['_SECTION']._serialized_end=6242
  _globals['_SCORECARD']._serialized_start=6245
  _globals['_SCORECARD']._serialized_end=7178
  _globals['_AUTOQUESTION']._serialized_start=7181
  _globals['_AUTOQUESTION']._serialized_end=7866
  _globals['_AUTOQUESTION_FLAGEXPR']._serialized_start=7600
  _globals['_AUTOQUESTION_FLAGEXPR']._serialized_end=7866
  _globals['_AUTOQUESTION_FLAGEXPR_FLAG']._serialized_start=7833
  _globals['_AUTOQUESTION_FLAGEXPR_FLAG']._serialized_end=7866
  _globals['_SMARTQUESTION']._serialized_start=7869
  _globals['_SMARTQUESTION']._serialized_end=8355
  _globals['_SMARTQUESTION_ANSWER']._serialized_start=8233
  _globals['_SMARTQUESTION_ANSWER']._serialized_end=8355
  _globals['_SMARTEVALUATION']._serialized_start=8358
  _globals['_SMARTEVALUATION']._serialized_end=9077
  _globals['_CALLMETADATA']._serialized_start=9079
  _globals['_CALLMETADATA']._serialized_end=9177
  _globals['_CONVERSATIONMETADATA']._serialized_start=9179
  _globals['_CONVERSATIONMETADATA']._serialized_end=9248
  _globals['_SMARTEVALUATIONSECTION']._serialized_start=9251
  _globals['_SMARTEVALUATIONSECTION']._serialized_end=9593
  _globals['_SMARTEVALUATIONQUESTION']._serialized_start=9596
  _globals['_SMARTEVALUATIONQUESTION']._serialized_end=10089
  _globals['_SMARTEVALUATIONQUESTION_ANSWER']._serialized_start=9924
  _globals['_SMARTEVALUATIONQUESTION_ANSWER']._serialized_end=10089
# @@protoc_insertion_point(module_scope)
