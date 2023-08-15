# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/insights/insight.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import insights_pb2 as api_dot_commons_dot_insights__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/insights/insight.proto\x12\x15\x61pi.v1alpha1.insights\x1a\x1a\x61pi/commons/insights.proto\x1a google/protobuf/field_mask.proto\"\xb8\x02\n\x07Insight\x12!\n\ninsight_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\tinsightId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12;\n\x0cinsight_type\x18\x05 \x01(\x0e\x32\x18.api.commons.InsightTypeR\x0binsightType\x12\'\n\x0finsight_version\x18\x06 \x01(\rR\x0einsightVersion\x12\x12\n\x04\x62ody\x18\x07 \x01(\tR\x04\x62ody\x12Z\n\x17insight_permission_type\x18\x08 \x01(\x0e\x32\".api.commons.InsightPermissionTypeR\x15insightPermissionType\"P\n\x14\x43reateInsightRequest\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"Q\n\x15\x43reateInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"s\n\x13ListInsightsRequest\x12\\\n\x18insight_permission_types\x18\x02 \x03(\x0e\x32\".api.commons.InsightPermissionTypeR\x16insightPermissionTypes\"R\n\x14ListInsightsResponse\x12:\n\x08insights\x18\x01 \x03(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x08insights\"\x8d\x01\n\x14UpdateInsightRequest\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"Q\n\x15UpdateInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"9\n\x14\x44\x65leteInsightRequest\x12!\n\ninsight_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\tinsightId\"Q\n\x15\x44\x65leteInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"6\n\x11GetInsightRequest\x12!\n\ninsight_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\tinsightId\"N\n\x12GetInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"4\n\x13GetVfsSchemaRequest\x12\x1d\n\nalias_name\x18\x01 \x01(\tR\taliasName\"\xa8\x02\n\x14GetVfsSchemaResponse\x12I\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x31.api.v1alpha1.insights.GetVfsSchemaResponse.FieldR\x06\x66ields\x12\'\n\x0fvfs_description\x18\x02 \x01(\tR\x0evfsDescription\x1a\x9b\x01\n\x05\x46ield\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12\x42\n\x0b\x63olumn_type\x18\x02 \x01(\x0e\x32!.api.commons.InsightVfsSchemaTypeR\ncolumnType\x12-\n\x12\x63olumn_description\x18\x03 \x01(\tR\x11\x63olumnDescription\"\x12\n\x10ListVfsesRequest\"-\n\x11ListVfsesResponse\x12\x18\n\x07\x61liases\x18\x01 \x03(\tR\x07\x61liasesB\x9f\x01\n\x19\x63om.api.v1alpha1.insightsB\x0cInsightProtoP\x01\xa2\x02\x03\x41VI\xaa\x02\x15\x41pi.V1alpha1.Insights\xca\x02\x15\x41pi\\V1alpha1\\Insights\xe2\x02!Api\\V1alpha1\\Insights\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Insightsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.insights.insight_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.api.v1alpha1.insightsB\014InsightProtoP\001\242\002\003AVI\252\002\025Api.V1alpha1.Insights\312\002\025Api\\V1alpha1\\Insights\342\002!Api\\V1alpha1\\Insights\\GPBMetadata\352\002\027Api::V1alpha1::Insights'
  _INSIGHT.fields_by_name['insight_id']._options = None
  _INSIGHT.fields_by_name['insight_id']._serialized_options = b'0\001'
  _DELETEINSIGHTREQUEST.fields_by_name['insight_id']._options = None
  _DELETEINSIGHTREQUEST.fields_by_name['insight_id']._serialized_options = b'0\001'
  _GETINSIGHTREQUEST.fields_by_name['insight_id']._options = None
  _GETINSIGHTREQUEST.fields_by_name['insight_id']._serialized_options = b'0\001'
  _globals['_INSIGHT']._serialized_start=125
  _globals['_INSIGHT']._serialized_end=437
  _globals['_CREATEINSIGHTREQUEST']._serialized_start=439
  _globals['_CREATEINSIGHTREQUEST']._serialized_end=519
  _globals['_CREATEINSIGHTRESPONSE']._serialized_start=521
  _globals['_CREATEINSIGHTRESPONSE']._serialized_end=602
  _globals['_LISTINSIGHTSREQUEST']._serialized_start=604
  _globals['_LISTINSIGHTSREQUEST']._serialized_end=719
  _globals['_LISTINSIGHTSRESPONSE']._serialized_start=721
  _globals['_LISTINSIGHTSRESPONSE']._serialized_end=803
  _globals['_UPDATEINSIGHTREQUEST']._serialized_start=806
  _globals['_UPDATEINSIGHTREQUEST']._serialized_end=947
  _globals['_UPDATEINSIGHTRESPONSE']._serialized_start=949
  _globals['_UPDATEINSIGHTRESPONSE']._serialized_end=1030
  _globals['_DELETEINSIGHTREQUEST']._serialized_start=1032
  _globals['_DELETEINSIGHTREQUEST']._serialized_end=1089
  _globals['_DELETEINSIGHTRESPONSE']._serialized_start=1091
  _globals['_DELETEINSIGHTRESPONSE']._serialized_end=1172
  _globals['_GETINSIGHTREQUEST']._serialized_start=1174
  _globals['_GETINSIGHTREQUEST']._serialized_end=1228
  _globals['_GETINSIGHTRESPONSE']._serialized_start=1230
  _globals['_GETINSIGHTRESPONSE']._serialized_end=1308
  _globals['_GETVFSSCHEMAREQUEST']._serialized_start=1310
  _globals['_GETVFSSCHEMAREQUEST']._serialized_end=1362
  _globals['_GETVFSSCHEMARESPONSE']._serialized_start=1365
  _globals['_GETVFSSCHEMARESPONSE']._serialized_end=1661
  _globals['_GETVFSSCHEMARESPONSE_FIELD']._serialized_start=1506
  _globals['_GETVFSSCHEMARESPONSE_FIELD']._serialized_end=1661
  _globals['_LISTVFSESREQUEST']._serialized_start=1663
  _globals['_LISTVFSESREQUEST']._serialized_end=1681
  _globals['_LISTVFSESRESPONSE']._serialized_start=1683
  _globals['_LISTVFSESRESPONSE']._serialized_end=1728
# @@protoc_insertion_point(module_scope)
