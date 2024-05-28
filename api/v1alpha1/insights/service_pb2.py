# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/insights/service.proto
# Protobuf Python Version: 5.27.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    0,
    '',
    'api/v1alpha1/insights/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.insights import insight_pb2 as api_dot_v1alpha1_dot_insights_dot_insight__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/insights/service.proto\x12\x15\x61pi.v1alpha1.insights\x1a\x17\x61nnotations/authz.proto\x1a#api/v1alpha1/insights/insight.proto\x1a\x1cgoogle/api/annotations.proto2\xe3\x12\n\x08Insights\x12\xb3\x01\n\rCreateInsight\x12+.api.v1alpha1.insights.CreateInsightRequest\x1a,.api.v1alpha1.insights.CreateInsightResponse\"G\xba\xb8\x91\x02\n\n\x03\x08\xfa\x01\n\x03\x08\xde\x04\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/insights/insights/createinsight:\x01*\x12\xb4\x01\n\x0cListInsights\x12*.api.v1alpha1.insights.ListInsightsRequest\x1a+.api.v1alpha1.insights.ListInsightsResponse\"K\xba\xb8\x91\x02\x0f\n\x03\x08\xfa\x01\n\x03\x08\xd9\x04\n\x03\x08\xda\x04\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/insights/insights/listinsights:\x01*\x12\xb9\x01\n\x0fListOrgInsights\x12-.api.v1alpha1.insights.ListOrgInsightsRequest\x1a..api.v1alpha1.insights.ListOrgInsightsResponse\"G\xba\xb8\x91\x02\x08\n\x06\x08\xfa\x01\x08\xd9\x04\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/insights/insights/listorginsights:\x01*\x12\xb3\x01\n\rUpdateInsight\x12+.api.v1alpha1.insights.UpdateInsightRequest\x1a,.api.v1alpha1.insights.UpdateInsightResponse\"G\xba\xb8\x91\x02\n\n\x03\x08\xfa\x01\n\x03\x08\xde\x04\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/insights/insights/updateinsight:\x01*\x12\xb3\x01\n\rDeleteInsight\x12+.api.v1alpha1.insights.DeleteInsightRequest\x1a,.api.v1alpha1.insights.DeleteInsightResponse\"G\xba\xb8\x91\x02\n\n\x03\x08\xfa\x01\n\x03\x08\xde\x04\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/insights/insights/deleteinsight:\x01*\x12\xac\x01\n\nGetInsight\x12(.api.v1alpha1.insights.GetInsightRequest\x1a).api.v1alpha1.insights.GetInsightResponse\"I\xba\xb8\x91\x02\x0f\n\x03\x08\xfa\x01\n\x03\x08\xd9\x04\n\x03\x08\xda\x04\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/insights/insights/getinsight:\x01*\x12\xbf\x01\n\x14\x43reateCommonsInsight\x12+.api.v1alpha1.insights.CreateInsightRequest\x1a,.api.v1alpha1.insights.CreateInsightResponse\"L\xba\xb8\x91\x02\x08\n\x06\x08\xfa\x01\x08\xde\x04\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/insights/insights/createcommonsinsight:\x01*\x12\xbf\x01\n\x14UpdateCommonsInsight\x12+.api.v1alpha1.insights.UpdateInsightRequest\x1a,.api.v1alpha1.insights.UpdateInsightResponse\"L\xba\xb8\x91\x02\x08\n\x06\x08\xfa\x01\x08\xde\x04\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/insights/insights/updatecommonsinsight:\x01*\x12\xbf\x01\n\x14\x44\x65leteCommonsInsight\x12+.api.v1alpha1.insights.DeleteInsightRequest\x1a,.api.v1alpha1.insights.DeleteInsightResponse\"L\xba\xb8\x91\x02\x08\n\x06\x08\xfa\x01\x08\xde\x04\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/insights/insights/deletecommonsinsight:\x01*\x12\xaf\x01\n\x0cGetVfsSchema\x12*.api.v1alpha1.insights.GetVfsSchemaRequest\x1a+.api.v1alpha1.insights.GetVfsSchemaResponse\"F\xba\xb8\x91\x02\n\n\x03\x08\xfa\x01\n\x03\x08\xde\x04\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/insights/insights/getvfsschema:\x01*\x12\xa3\x01\n\tListVfses\x12\'.api.v1alpha1.insights.ListVfsesRequest\x1a(.api.v1alpha1.insights.ListVfsesResponse\"C\xba\xb8\x91\x02\n\n\x03\x08\xfa\x01\n\x03\x08\xde\x04\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/insights/insights/listvfses:\x01*\x12\xbc\x01\n\x0eListVfsSchemas\x12,.api.v1alpha1.insights.ListVfsSchemasRequest\x1a-.api.v1alpha1.insights.ListVfsSchemasResponse\"M\xba\xb8\x91\x02\x0f\n\x03\x08\xfa\x01\n\x03\x08\xde\x04\n\x03\x08\xd9\x04\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/insights/insights/listvfsschemas:\x01*\x12\xb5\x01\n\x0ePublishInsight\x12,.api.v1alpha1.insights.PublishInsightRequest\x1a-.api.v1alpha1.insights.PublishInsightResponse\"F\xba\xb8\x91\x02\x08\n\x06\x08\xfa\x01\x08\xde\x04\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/insights/insights/publishinsight:\x01*B\x9f\x01\n\x19\x63om.api.v1alpha1.insightsB\x0cServiceProtoP\x01\xa2\x02\x03\x41VI\xaa\x02\x15\x41pi.V1alpha1.Insights\xca\x02\x15\x41pi\\V1alpha1\\Insights\xe2\x02!Api\\V1alpha1\\Insights\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Insightsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.insights.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.api.v1alpha1.insightsB\014ServiceProtoP\001\242\002\003AVI\252\002\025Api.V1alpha1.Insights\312\002\025Api\\V1alpha1\\Insights\342\002!Api\\V1alpha1\\Insights\\GPBMetadata\352\002\027Api::V1alpha1::Insights'
  _globals['_INSIGHTS'].methods_by_name['CreateInsight']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['CreateInsight']._serialized_options = b'\272\270\221\002\n\n\003\010\372\001\n\003\010\336\004\202\323\344\223\0022\"-/api/v1alpha1/insights/insights/createinsight:\001*'
  _globals['_INSIGHTS'].methods_by_name['ListInsights']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['ListInsights']._serialized_options = b'\272\270\221\002\017\n\003\010\372\001\n\003\010\331\004\n\003\010\332\004\202\323\344\223\0021\",/api/v1alpha1/insights/insights/listinsights:\001*'
  _globals['_INSIGHTS'].methods_by_name['ListOrgInsights']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['ListOrgInsights']._serialized_options = b'\272\270\221\002\010\n\006\010\372\001\010\331\004\202\323\344\223\0024\"//api/v1alpha1/insights/insights/listorginsights:\001*'
  _globals['_INSIGHTS'].methods_by_name['UpdateInsight']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['UpdateInsight']._serialized_options = b'\272\270\221\002\n\n\003\010\372\001\n\003\010\336\004\202\323\344\223\0022\"-/api/v1alpha1/insights/insights/updateinsight:\001*'
  _globals['_INSIGHTS'].methods_by_name['DeleteInsight']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['DeleteInsight']._serialized_options = b'\272\270\221\002\n\n\003\010\372\001\n\003\010\336\004\202\323\344\223\0022\"-/api/v1alpha1/insights/insights/deleteinsight:\001*'
  _globals['_INSIGHTS'].methods_by_name['GetInsight']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['GetInsight']._serialized_options = b'\272\270\221\002\017\n\003\010\372\001\n\003\010\331\004\n\003\010\332\004\202\323\344\223\002/\"*/api/v1alpha1/insights/insights/getinsight:\001*'
  _globals['_INSIGHTS'].methods_by_name['CreateCommonsInsight']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['CreateCommonsInsight']._serialized_options = b'\272\270\221\002\010\n\006\010\372\001\010\336\004\202\323\344\223\0029\"4/api/v1alpha1/insights/insights/createcommonsinsight:\001*'
  _globals['_INSIGHTS'].methods_by_name['UpdateCommonsInsight']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['UpdateCommonsInsight']._serialized_options = b'\272\270\221\002\010\n\006\010\372\001\010\336\004\202\323\344\223\0029\"4/api/v1alpha1/insights/insights/updatecommonsinsight:\001*'
  _globals['_INSIGHTS'].methods_by_name['DeleteCommonsInsight']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['DeleteCommonsInsight']._serialized_options = b'\272\270\221\002\010\n\006\010\372\001\010\336\004\202\323\344\223\0029\"4/api/v1alpha1/insights/insights/deletecommonsinsight:\001*'
  _globals['_INSIGHTS'].methods_by_name['GetVfsSchema']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['GetVfsSchema']._serialized_options = b'\272\270\221\002\n\n\003\010\372\001\n\003\010\336\004\202\323\344\223\0021\",/api/v1alpha1/insights/insights/getvfsschema:\001*'
  _globals['_INSIGHTS'].methods_by_name['ListVfses']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['ListVfses']._serialized_options = b'\272\270\221\002\n\n\003\010\372\001\n\003\010\336\004\202\323\344\223\002.\")/api/v1alpha1/insights/insights/listvfses:\001*'
  _globals['_INSIGHTS'].methods_by_name['ListVfsSchemas']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['ListVfsSchemas']._serialized_options = b'\272\270\221\002\017\n\003\010\372\001\n\003\010\336\004\n\003\010\331\004\202\323\344\223\0023\"./api/v1alpha1/insights/insights/listvfsschemas:\001*'
  _globals['_INSIGHTS'].methods_by_name['PublishInsight']._loaded_options = None
  _globals['_INSIGHTS'].methods_by_name['PublishInsight']._serialized_options = b'\272\270\221\002\010\n\006\010\372\001\010\336\004\202\323\344\223\0023\"./api/v1alpha1/insights/insights/publishinsight:\001*'
  _globals['_INSIGHTS']._serialized_start=155
  _globals['_INSIGHTS']._serialized_end=2558
# @@protoc_insertion_point(module_scope)
