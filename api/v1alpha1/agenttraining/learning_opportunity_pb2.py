# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/agenttraining/learning_opportunity.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import agent_training_pb2 as api_dot_commons_dot_agent__training__pb2
from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5api/v1alpha1/agenttraining/learning_opportunity.proto\x12\x1a\x61pi.v1alpha1.agenttraining\x1a api/commons/agent_training.proto\x1a\x1c\x61pi/commons/scorecards.proto\x1a google/protobuf/field_mask.proto\"w\n CreateLearningOpportunityRequest\x12S\n\x14learning_opportunity\x18\x01 \x01(\x0b\x32 .api.commons.LearningOpportunityR\x13learningOpportunity\"x\n!CreateLearningOpportunityResponse\x12S\n\x14learning_opportunity\x18\x01 \x01(\x0b\x32 .api.commons.LearningOpportunityR\x13learningOpportunity\"\xf1\x01\n ListLearningOpportunitiesRequest\x12\x46\n\x10\x63\x61ll_identifiers\x18\x02 \x03(\x0b\x32\x1b.api.commons.CallIdentifierR\x0f\x63\x61llIdentifiers\x12\'\n\x0ftranscript_sids\x18\x03 \x03(\x03R\x0etranscriptSids\x12$\n\x0e\x61gent_user_ids\x18\x04 \x03(\tR\x0c\x61gentUserIds\x12\x36\n\ncreated_at\x18\x05 \x01(\x0b\x32\x17.api.commons.TimeFilterR\tcreatedAt\"|\n!ListLearningOpportunitiesResponse\x12W\n\x16learning_opportunities\x18\x01 \x03(\x0b\x32 .api.commons.LearningOpportunityR\x15learningOpportunities\"\xd0\x01\n%ListAgentLearningOpportunitiesRequest\x12\x46\n\x10\x63\x61ll_identifiers\x18\x02 \x03(\x0b\x32\x1b.api.commons.CallIdentifierR\x0f\x63\x61llIdentifiers\x12\'\n\x0ftranscript_sids\x18\x03 \x03(\x03R\x0etranscriptSids\x12\x36\n\ncreated_at\x18\x04 \x01(\x0b\x32\x17.api.commons.TimeFilterR\tcreatedAt\"\x81\x01\n&ListAgentLearningOpportunitiesResponse\x12W\n\x16learning_opportunities\x18\x01 \x03(\x0b\x32 .api.commons.LearningOpportunityR\x15learningOpportunities\"\xb4\x01\n UpdateLearningOpportunityRequest\x12S\n\x14learning_opportunity\x18\x02 \x01(\x0b\x32 .api.commons.LearningOpportunityR\x13learningOpportunity\x12;\n\x0bupdate_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"x\n!UpdateLearningOpportunityResponse\x12S\n\x14learning_opportunity\x18\x01 \x01(\x0b\x32 .api.commons.LearningOpportunityR\x13learningOpportunity\"a\n\'CompleteAgentLearningOpportunityRequest\x12\x36\n\x17learning_opportunity_id\x18\x03 \x01(\x03R\x15learningOpportunityId\"\x7f\n(CompleteAgentLearningOpportunityResponse\x12S\n\x14learning_opportunity\x18\x01 \x01(\x0b\x32 .api.commons.LearningOpportunityR\x13learningOpportunity\"Z\n DeleteLearningOpportunityRequest\x12\x36\n\x17learning_opportunity_id\x18\x03 \x01(\x03R\x15learningOpportunityId\"x\n!DeleteLearningOpportunityResponse\x12S\n\x14learning_opportunity\x18\x01 \x01(\x0b\x32 .api.commons.LearningOpportunityR\x13learningOpportunity\"R\n\x1dGetLearningOpportunityRequest\x12\x31\n\x14learning_opportunity\x18\x02 \x01(\x03R\x13learningOpportunity\"u\n\x1eGetLearningOpportunityResponse\x12S\n\x14learning_opportunity\x18\x01 \x01(\x0b\x32 .api.commons.LearningOpportunityR\x13learningOpportunity\"\x8f\x02\n\'ListLearningOpportunitiesByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x46\n\x10\x63\x61ll_identifiers\x18\x02 \x03(\x0b\x32\x1b.api.commons.CallIdentifierR\x0f\x63\x61llIdentifiers\x12\'\n\x0ftranscript_sids\x18\x03 \x03(\x03R\x0etranscriptSids\x12$\n\x0e\x61gent_user_ids\x18\x04 \x03(\tR\x0c\x61gentUserIds\x12\x36\n\ncreated_at\x18\x05 \x01(\x0b\x32\x17.api.commons.TimeFilterR\tcreatedAt\"x\n\'DeleteLearningOpportunityByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x36\n\x17learning_opportunity_id\x18\x03 \x01(\x03R\x15learningOpportunityIdB\xc4\x01\n\x1e\x63om.api.v1alpha1.agenttrainingB\x18LearningOpportunityProtoP\x01\xa2\x02\x03\x41VA\xaa\x02\x1a\x41pi.V1alpha1.Agenttraining\xca\x02\x1a\x41pi\\V1alpha1\\Agenttraining\xe2\x02&Api\\V1alpha1\\Agenttraining\\GPBMetadata\xea\x02\x1c\x41pi::V1alpha1::Agenttrainingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.agenttraining.learning_opportunity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.api.v1alpha1.agenttrainingB\030LearningOpportunityProtoP\001\242\002\003AVA\252\002\032Api.V1alpha1.Agenttraining\312\002\032Api\\V1alpha1\\Agenttraining\342\002&Api\\V1alpha1\\Agenttraining\\GPBMetadata\352\002\034Api::V1alpha1::Agenttraining'
  _globals['_CREATELEARNINGOPPORTUNITYREQUEST']._serialized_start=183
  _globals['_CREATELEARNINGOPPORTUNITYREQUEST']._serialized_end=302
  _globals['_CREATELEARNINGOPPORTUNITYRESPONSE']._serialized_start=304
  _globals['_CREATELEARNINGOPPORTUNITYRESPONSE']._serialized_end=424
  _globals['_LISTLEARNINGOPPORTUNITIESREQUEST']._serialized_start=427
  _globals['_LISTLEARNINGOPPORTUNITIESREQUEST']._serialized_end=668
  _globals['_LISTLEARNINGOPPORTUNITIESRESPONSE']._serialized_start=670
  _globals['_LISTLEARNINGOPPORTUNITIESRESPONSE']._serialized_end=794
  _globals['_LISTAGENTLEARNINGOPPORTUNITIESREQUEST']._serialized_start=797
  _globals['_LISTAGENTLEARNINGOPPORTUNITIESREQUEST']._serialized_end=1005
  _globals['_LISTAGENTLEARNINGOPPORTUNITIESRESPONSE']._serialized_start=1008
  _globals['_LISTAGENTLEARNINGOPPORTUNITIESRESPONSE']._serialized_end=1137
  _globals['_UPDATELEARNINGOPPORTUNITYREQUEST']._serialized_start=1140
  _globals['_UPDATELEARNINGOPPORTUNITYREQUEST']._serialized_end=1320
  _globals['_UPDATELEARNINGOPPORTUNITYRESPONSE']._serialized_start=1322
  _globals['_UPDATELEARNINGOPPORTUNITYRESPONSE']._serialized_end=1442
  _globals['_COMPLETEAGENTLEARNINGOPPORTUNITYREQUEST']._serialized_start=1444
  _globals['_COMPLETEAGENTLEARNINGOPPORTUNITYREQUEST']._serialized_end=1541
  _globals['_COMPLETEAGENTLEARNINGOPPORTUNITYRESPONSE']._serialized_start=1543
  _globals['_COMPLETEAGENTLEARNINGOPPORTUNITYRESPONSE']._serialized_end=1670
  _globals['_DELETELEARNINGOPPORTUNITYREQUEST']._serialized_start=1672
  _globals['_DELETELEARNINGOPPORTUNITYREQUEST']._serialized_end=1762
  _globals['_DELETELEARNINGOPPORTUNITYRESPONSE']._serialized_start=1764
  _globals['_DELETELEARNINGOPPORTUNITYRESPONSE']._serialized_end=1884
  _globals['_GETLEARNINGOPPORTUNITYREQUEST']._serialized_start=1886
  _globals['_GETLEARNINGOPPORTUNITYREQUEST']._serialized_end=1968
  _globals['_GETLEARNINGOPPORTUNITYRESPONSE']._serialized_start=1970
  _globals['_GETLEARNINGOPPORTUNITYRESPONSE']._serialized_end=2087
  _globals['_LISTLEARNINGOPPORTUNITIESBYORGIDREQUEST']._serialized_start=2090
  _globals['_LISTLEARNINGOPPORTUNITIESBYORGIDREQUEST']._serialized_end=2361
  _globals['_DELETELEARNINGOPPORTUNITYBYORGIDREQUEST']._serialized_start=2363
  _globals['_DELETELEARNINGOPPORTUNITYBYORGIDREQUEST']._serialized_end=2483
# @@protoc_insertion_point(module_scope)
