# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/insights/insight.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import insights_pb2 as api_dot_commons_dot_insights__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/insights/insight.proto\x12\x15\x61pi.v1alpha1.insights\x1a\x1a\x61pi/commons/insights.proto\x1a google/protobuf/field_mask.proto\"\x84\x03\n\x07Insight\x12!\n\ninsight_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\tinsightId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12;\n\x0cinsight_type\x18\x05 \x01(\x0e\x32\x18.api.commons.InsightTypeR\x0binsightType\x12\'\n\x0finsight_version\x18\x06 \x01(\rR\x0einsightVersion\x12\x12\n\x04\x62ody\x18\x07 \x01(\tR\x04\x62ody\x12Z\n\x17insight_permission_type\x18\x08 \x01(\x0e\x32\".api.commons.InsightPermissionTypeR\x15insightPermissionType\x12\x1f\n\x0bresource_id\x18\t \x01(\tR\nresourceId\x12)\n\x10standard_insight\x18\n \x01(\x08R\x0fstandardInsight\"p\n\x15PublishInsightRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x36\n\x17\x64\x65stination_resource_id\x18\x02 \x01(\tR\x15\x64\x65stinationResourceId\"R\n\x16PublishInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"P\n\x14\x43reateInsightRequest\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"Q\n\x15\x43reateInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"s\n\x13ListInsightsRequest\x12\\\n\x18insight_permission_types\x18\x02 \x03(\x0e\x32\".api.commons.InsightPermissionTypeR\x16insightPermissionTypes\"R\n\x14ListInsightsResponse\x12:\n\x08insights\x18\x01 \x03(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x08insights\"\x8d\x01\n\x14UpdateInsightRequest\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"Q\n\x15UpdateInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"Z\n\x14\x44\x65leteInsightRequest\x12!\n\ninsight_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\tinsightId\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\"Q\n\x15\x44\x65leteInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"W\n\x11GetInsightRequest\x12!\n\ninsight_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\tinsightId\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\"N\n\x12GetInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"4\n\x13GetVfsSchemaRequest\x12\x1d\n\nalias_name\x18\x01 \x01(\tR\taliasName\"\xc7\x02\n\x14GetVfsSchemaResponse\x12I\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x31.api.v1alpha1.insights.GetVfsSchemaResponse.FieldR\x06\x66ields\x12\'\n\x0fvfs_description\x18\x02 \x01(\tR\x0evfsDescription\x12\x1d\n\nalias_name\x18\x03 \x01(\tR\taliasName\x1a\x9b\x01\n\x05\x46ield\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12\x42\n\x0b\x63olumn_type\x18\x02 \x01(\x0e\x32!.api.commons.InsightVfsSchemaTypeR\ncolumnType\x12-\n\x12\x63olumn_description\x18\x03 \x01(\tR\x11\x63olumnDescription\"\x12\n\x10ListVfsesRequest\"-\n\x11ListVfsesResponse\x12\x18\n\x07\x61liases\x18\x01 \x03(\tR\x07\x61liases\"\x17\n\x15ListVfsSchemasRequest\"f\n\x16ListVfsSchemasResponse\x12L\n\x0bvfs_schemas\x18\x01 \x03(\x0b\x32+.api.v1alpha1.insights.GetVfsSchemaResponseR\nvfsSchemasB\x9f\x01\n\x19\x63om.api.v1alpha1.insightsB\x0cInsightProtoP\x01\xa2\x02\x03\x41VI\xaa\x02\x15\x41pi.V1alpha1.Insights\xca\x02\x15\x41pi\\V1alpha1\\Insights\xe2\x02!Api\\V1alpha1\\Insights\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Insightsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.insights.insight_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.api.v1alpha1.insightsB\014InsightProtoP\001\242\002\003AVI\252\002\025Api.V1alpha1.Insights\312\002\025Api\\V1alpha1\\Insights\342\002!Api\\V1alpha1\\Insights\\GPBMetadata\352\002\027Api::V1alpha1::Insights'
  _globals['_INSIGHT'].fields_by_name['insight_id']._options = None
  _globals['_INSIGHT'].fields_by_name['insight_id']._serialized_options = b'0\001'
  _globals['_DELETEINSIGHTREQUEST'].fields_by_name['insight_id']._options = None
  _globals['_DELETEINSIGHTREQUEST'].fields_by_name['insight_id']._serialized_options = b'0\001'
  _globals['_GETINSIGHTREQUEST'].fields_by_name['insight_id']._options = None
  _globals['_GETINSIGHTREQUEST'].fields_by_name['insight_id']._serialized_options = b'0\001'
  _globals['_INSIGHT']._serialized_start=125
  _globals['_INSIGHT']._serialized_end=513
  _globals['_PUBLISHINSIGHTREQUEST']._serialized_start=515
  _globals['_PUBLISHINSIGHTREQUEST']._serialized_end=627
  _globals['_PUBLISHINSIGHTRESPONSE']._serialized_start=629
  _globals['_PUBLISHINSIGHTRESPONSE']._serialized_end=711
  _globals['_CREATEINSIGHTREQUEST']._serialized_start=713
  _globals['_CREATEINSIGHTREQUEST']._serialized_end=793
  _globals['_CREATEINSIGHTRESPONSE']._serialized_start=795
  _globals['_CREATEINSIGHTRESPONSE']._serialized_end=876
  _globals['_LISTINSIGHTSREQUEST']._serialized_start=878
  _globals['_LISTINSIGHTSREQUEST']._serialized_end=993
  _globals['_LISTINSIGHTSRESPONSE']._serialized_start=995
  _globals['_LISTINSIGHTSRESPONSE']._serialized_end=1077
  _globals['_UPDATEINSIGHTREQUEST']._serialized_start=1080
  _globals['_UPDATEINSIGHTREQUEST']._serialized_end=1221
  _globals['_UPDATEINSIGHTRESPONSE']._serialized_start=1223
  _globals['_UPDATEINSIGHTRESPONSE']._serialized_end=1304
  _globals['_DELETEINSIGHTREQUEST']._serialized_start=1306
  _globals['_DELETEINSIGHTREQUEST']._serialized_end=1396
  _globals['_DELETEINSIGHTRESPONSE']._serialized_start=1398
  _globals['_DELETEINSIGHTRESPONSE']._serialized_end=1479
  _globals['_GETINSIGHTREQUEST']._serialized_start=1481
  _globals['_GETINSIGHTREQUEST']._serialized_end=1568
  _globals['_GETINSIGHTRESPONSE']._serialized_start=1570
  _globals['_GETINSIGHTRESPONSE']._serialized_end=1648
  _globals['_GETVFSSCHEMAREQUEST']._serialized_start=1650
  _globals['_GETVFSSCHEMAREQUEST']._serialized_end=1702
  _globals['_GETVFSSCHEMARESPONSE']._serialized_start=1705
  _globals['_GETVFSSCHEMARESPONSE']._serialized_end=2032
  _globals['_GETVFSSCHEMARESPONSE_FIELD']._serialized_start=1877
  _globals['_GETVFSSCHEMARESPONSE_FIELD']._serialized_end=2032
  _globals['_LISTVFSESREQUEST']._serialized_start=2034
  _globals['_LISTVFSESREQUEST']._serialized_end=2052
  _globals['_LISTVFSESRESPONSE']._serialized_start=2054
  _globals['_LISTVFSESRESPONSE']._serialized_end=2099
  _globals['_LISTVFSSCHEMASREQUEST']._serialized_start=2101
  _globals['_LISTVFSSCHEMASREQUEST']._serialized_end=2124
  _globals['_LISTVFSSCHEMASRESPONSE']._serialized_start=2126
  _globals['_LISTVFSSCHEMASRESPONSE']._serialized_end=2228
# @@protoc_insertion_point(module_scope)
