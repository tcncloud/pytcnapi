# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/scorecards/category.proto
# Protobuf Python Version: 5.28.1
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
    1,
    '',
    'api/v1alpha1/scorecards/category.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from api.commons import scorecards_pb2 as api_dot_commons_dot_scorecards__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&api/v1alpha1/scorecards/category.proto\x12\x17\x61pi.v1alpha1.scorecards\x1a\x15\x61pi/commons/acd.proto\x1a\x1c\x61pi/commons/scorecards.proto\x1a\x1egoogle/protobuf/duration.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"J\n\x15\x43reateCategoryRequest\x12\x31\n\x08\x63\x61tegory\x18\x01 \x01(\x0b\x32\x15.api.commons.CategoryR\x08\x63\x61tegory\"K\n\x16\x43reateCategoryResponse\x12\x31\n\x08\x63\x61tegory\x18\x01 \x01(\x0b\x32\x15.api.commons.CategoryR\x08\x63\x61tegory\"\xad\x02\n\x15ListCategoriesRequest\x12\x1d\n\nauthor_ids\x18\x02 \x03(\tR\tauthorIds\x12%\n\x0eskill_profiles\x18\x03 \x03(\x03R\rskillProfiles\x12=\n\ncall_types\x18\x04 \x03(\x0e\x32\x1a.api.commons.CallType.EnumB\x02\x18\x01R\tcallTypes\x12`\n\rcategory_type\x18\x05 \x01(\x0e\x32;.api.v1alpha1.scorecards.ListCategoriesRequest.CategoryTypeR\x0c\x63\x61tegoryType\"-\n\x0c\x43\x61tegoryType\x12\x07\n\x03\x41NY\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\x08\n\x04USER\x10\x02\"O\n\x16ListCategoriesResponse\x12\x35\n\ncategories\x18\x01 \x03(\x0b\x32\x15.api.commons.CategoryR\ncategories\"\x87\x01\n\x15UpdateCategoryRequest\x12\x31\n\x08\x63\x61tegory\x18\x01 \x01(\x0b\x32\x15.api.commons.CategoryR\x08\x63\x61tegory\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"K\n\x16UpdateCategoryResponse\x12\x31\n\x08\x63\x61tegory\x18\x01 \x01(\x0b\x32\x15.api.commons.CategoryR\x08\x63\x61tegory\"8\n\x15\x44\x65leteCategoryRequest\x12\x1f\n\x0b\x63\x61tegory_id\x18\x02 \x01(\x03R\ncategoryId\"K\n\x16\x44\x65leteCategoryResponse\x12\x31\n\x08\x63\x61tegory\x18\x01 \x01(\x0b\x32\x15.api.commons.CategoryR\x08\x63\x61tegory\"K\n\x12GetCategoryRequest\x12\x1f\n\x0b\x63\x61tegory_id\x18\x02 \x01(\x03R\ncategoryId\x12\x14\n\x05title\x18\x03 \x01(\tR\x05title\"H\n\x13GetCategoryResponse\x12\x31\n\x08\x63\x61tegory\x18\x01 \x01(\x0b\x32\x15.api.commons.CategoryR\x08\x63\x61tegory\"\xdd\x02\n\x1cSampleCallsByCategoryRequest\x12\x1f\n\x0b\x63\x61tegory_id\x18\x02 \x01(\x03R\ncategoryId\x12\x39\n\nstart_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x34\n\x16scorer_max_evaluations\x18\x05 \x01(\x05R\x14scorerMaxEvaluations\x12+\n\x11sample_percentage\x18\x06 \x01(\x05R\x10samplePercentage\x12$\n\x0e\x61gent_user_ids\x18\x07 \x03(\tR\x0c\x61gentUserIds\x12!\n\x0cscorecard_id\x18\n \x01(\x03R\x0bscorecardId\"j\n\x1dSampleCallsByCategoryResponse\x12I\n\x0b\x61gent_calls\x18\x01 \x03(\x0b\x32(.api.v1alpha1.scorecards.SampleAgentCallR\nagentCalls\"\xec\x02\n\x0fSampleAgentCall\x12\x19\n\x08\x63\x61ll_sid\x18\x01 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x02 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12\x39\n\ncall_start\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcallStart\x12>\n\rcall_duration\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x0c\x63\x61llDuration\x12\x31\n\x06speech\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x06speech\x12\x33\n\x07silence\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationR\x07silence\x12\"\n\ragent_user_id\x18\x07 \x01(\tR\x0b\x61gentUserId\"\x93\x02\n\x1cListCategoriesByOrgIdRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nauthor_ids\x18\x02 \x03(\tR\tauthorIds\x12%\n\x0eskill_profiles\x18\x03 \x03(\x03R\rskillProfiles\x12g\n\rcategory_type\x18\x04 \x01(\x0e\x32\x42.api.v1alpha1.scorecards.ListCategoriesByOrgIdRequest.CategoryTypeR\x0c\x63\x61tegoryType\"-\n\x0c\x43\x61tegoryType\x12\x07\n\x03\x41NY\x10\x00\x12\n\n\x06SYSTEM\x10\x01\x12\x08\n\x04USER\x10\x02\x42\xaa\x01\n\x1b\x63om.api.v1alpha1.scorecardsB\rCategoryProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Scorecards\xca\x02\x17\x41pi\\V1alpha1\\Scorecards\xe2\x02#Api\\V1alpha1\\Scorecards\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Scorecardsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.scorecards.category_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.scorecardsB\rCategoryProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Scorecards\312\002\027Api\\V1alpha1\\Scorecards\342\002#Api\\V1alpha1\\Scorecards\\GPBMetadata\352\002\031Api::V1alpha1::Scorecards'
  _globals['_LISTCATEGORIESREQUEST'].fields_by_name['call_types']._loaded_options = None
  _globals['_LISTCATEGORIESREQUEST'].fields_by_name['call_types']._serialized_options = b'\030\001'
  _globals['_CREATECATEGORYREQUEST']._serialized_start=219
  _globals['_CREATECATEGORYREQUEST']._serialized_end=293
  _globals['_CREATECATEGORYRESPONSE']._serialized_start=295
  _globals['_CREATECATEGORYRESPONSE']._serialized_end=370
  _globals['_LISTCATEGORIESREQUEST']._serialized_start=373
  _globals['_LISTCATEGORIESREQUEST']._serialized_end=674
  _globals['_LISTCATEGORIESREQUEST_CATEGORYTYPE']._serialized_start=629
  _globals['_LISTCATEGORIESREQUEST_CATEGORYTYPE']._serialized_end=674
  _globals['_LISTCATEGORIESRESPONSE']._serialized_start=676
  _globals['_LISTCATEGORIESRESPONSE']._serialized_end=755
  _globals['_UPDATECATEGORYREQUEST']._serialized_start=758
  _globals['_UPDATECATEGORYREQUEST']._serialized_end=893
  _globals['_UPDATECATEGORYRESPONSE']._serialized_start=895
  _globals['_UPDATECATEGORYRESPONSE']._serialized_end=970
  _globals['_DELETECATEGORYREQUEST']._serialized_start=972
  _globals['_DELETECATEGORYREQUEST']._serialized_end=1028
  _globals['_DELETECATEGORYRESPONSE']._serialized_start=1030
  _globals['_DELETECATEGORYRESPONSE']._serialized_end=1105
  _globals['_GETCATEGORYREQUEST']._serialized_start=1107
  _globals['_GETCATEGORYREQUEST']._serialized_end=1182
  _globals['_GETCATEGORYRESPONSE']._serialized_start=1184
  _globals['_GETCATEGORYRESPONSE']._serialized_end=1256
  _globals['_SAMPLECALLSBYCATEGORYREQUEST']._serialized_start=1259
  _globals['_SAMPLECALLSBYCATEGORYREQUEST']._serialized_end=1608
  _globals['_SAMPLECALLSBYCATEGORYRESPONSE']._serialized_start=1610
  _globals['_SAMPLECALLSBYCATEGORYRESPONSE']._serialized_end=1716
  _globals['_SAMPLEAGENTCALL']._serialized_start=1719
  _globals['_SAMPLEAGENTCALL']._serialized_end=2083
  _globals['_LISTCATEGORIESBYORGIDREQUEST']._serialized_start=2086
  _globals['_LISTCATEGORIESBYORGIDREQUEST']._serialized_end=2361
  _globals['_LISTCATEGORIESBYORGIDREQUEST_CATEGORYTYPE']._serialized_start=629
  _globals['_LISTCATEGORIESBYORGIDREQUEST_CATEGORYTYPE']._serialized_end=674
# @@protoc_insertion_point(module_scope)
