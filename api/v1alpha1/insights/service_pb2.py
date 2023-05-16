# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/insights/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.v1alpha1.insights import insight_pb2 as api_dot_v1alpha1_dot_insights_dot_insight__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/insights/service.proto\x12\x15\x61pi.v1alpha1.insights\x1a\x17\x61nnotations/authz.proto\x1a#api/v1alpha1/insights/insight.proto\x1a\x1cgoogle/api/annotations.proto2\xfa\r\n\x08Insights\x12\xae\x01\n\rCreateInsight\x12+.api.v1alpha1.insights.CreateInsightRequest\x1a,.api.v1alpha1.insights.CreateInsightResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xdc\x04\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/insights/insights/createinsight:\x01*\x12\xaa\x01\n\x0cListInsights\x12*.api.v1alpha1.insights.ListInsightsRequest\x1a+.api.v1alpha1.insights.ListInsightsResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xdc\x04\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/insights/insights/listinsights:\x01*\x12\xae\x01\n\rUpdateInsight\x12+.api.v1alpha1.insights.UpdateInsightRequest\x1a,.api.v1alpha1.insights.UpdateInsightResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xdc\x04\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/insights/insights/updateinsight:\x01*\x12\xae\x01\n\rDeleteInsight\x12+.api.v1alpha1.insights.DeleteInsightRequest\x1a,.api.v1alpha1.insights.DeleteInsightResponse\"B\xba\xb8\x91\x02\x05\n\x03\x08\xdc\x04\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/insights/insights/deleteinsight:\x01*\x12\xa2\x01\n\nGetInsight\x12(.api.v1alpha1.insights.GetInsightRequest\x1a).api.v1alpha1.insights.GetInsightResponse\"?\xba\xb8\x91\x02\x05\n\x03\x08\xdc\x04\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/insights/insights/getinsight:\x01*\x12\xbc\x01\n\x14\x43reateCommonsInsight\x12+.api.v1alpha1.insights.CreateInsightRequest\x1a,.api.v1alpha1.insights.CreateInsightResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xdb\x04\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/insights/insights/createcommonsinsight:\x01*\x12\xbc\x01\n\x14UpdateCommonsInsight\x12+.api.v1alpha1.insights.UpdateInsightRequest\x1a,.api.v1alpha1.insights.UpdateInsightResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xdb\x04\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/insights/insights/updatecommonsinsight:\x01*\x12\xbc\x01\n\x14\x44\x65leteCommonsInsight\x12+.api.v1alpha1.insights.DeleteInsightRequest\x1a,.api.v1alpha1.insights.DeleteInsightResponse\"I\xba\xb8\x91\x02\x05\n\x03\x08\xdb\x04\x82\xd3\xe4\x93\x02\x39\"4/api/v1alpha1/insights/insights/deletecommonsinsight:\x01*\x12\xaa\x01\n\x0cGetVfsSchema\x12*.api.v1alpha1.insights.GetVfsSchemaRequest\x1a+.api.v1alpha1.insights.GetVfsSchemaResponse\"A\xba\xb8\x91\x02\x05\n\x03\x08\xdc\x04\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/insights/insights/getvfsschema:\x01*\x12\x9e\x01\n\tListVfses\x12\'.api.v1alpha1.insights.ListVfsesRequest\x1a(.api.v1alpha1.insights.ListVfsesResponse\">\xba\xb8\x91\x02\x05\n\x03\x08\xdc\x04\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/insights/insights/listvfses:\x01*B\x9f\x01\n\x19\x63om.api.v1alpha1.insightsB\x0cServiceProtoP\x01\xa2\x02\x03\x41VI\xaa\x02\x15\x41pi.V1alpha1.Insights\xca\x02\x15\x41pi\\V1alpha1\\Insights\xe2\x02!Api\\V1alpha1\\Insights\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Insightsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.insights.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.api.v1alpha1.insightsB\014ServiceProtoP\001\242\002\003AVI\252\002\025Api.V1alpha1.Insights\312\002\025Api\\V1alpha1\\Insights\342\002!Api\\V1alpha1\\Insights\\GPBMetadata\352\002\027Api::V1alpha1::Insights'
  _INSIGHTS.methods_by_name['CreateInsight']._options = None
  _INSIGHTS.methods_by_name['CreateInsight']._serialized_options = b'\272\270\221\002\005\n\003\010\334\004\202\323\344\223\0022\"-/api/v1alpha1/insights/insights/createinsight:\001*'
  _INSIGHTS.methods_by_name['ListInsights']._options = None
  _INSIGHTS.methods_by_name['ListInsights']._serialized_options = b'\272\270\221\002\005\n\003\010\334\004\202\323\344\223\0021\",/api/v1alpha1/insights/insights/listinsights:\001*'
  _INSIGHTS.methods_by_name['UpdateInsight']._options = None
  _INSIGHTS.methods_by_name['UpdateInsight']._serialized_options = b'\272\270\221\002\005\n\003\010\334\004\202\323\344\223\0022\"-/api/v1alpha1/insights/insights/updateinsight:\001*'
  _INSIGHTS.methods_by_name['DeleteInsight']._options = None
  _INSIGHTS.methods_by_name['DeleteInsight']._serialized_options = b'\272\270\221\002\005\n\003\010\334\004\202\323\344\223\0022\"-/api/v1alpha1/insights/insights/deleteinsight:\001*'
  _INSIGHTS.methods_by_name['GetInsight']._options = None
  _INSIGHTS.methods_by_name['GetInsight']._serialized_options = b'\272\270\221\002\005\n\003\010\334\004\202\323\344\223\002/\"*/api/v1alpha1/insights/insights/getinsight:\001*'
  _INSIGHTS.methods_by_name['CreateCommonsInsight']._options = None
  _INSIGHTS.methods_by_name['CreateCommonsInsight']._serialized_options = b'\272\270\221\002\005\n\003\010\333\004\202\323\344\223\0029\"4/api/v1alpha1/insights/insights/createcommonsinsight:\001*'
  _INSIGHTS.methods_by_name['UpdateCommonsInsight']._options = None
  _INSIGHTS.methods_by_name['UpdateCommonsInsight']._serialized_options = b'\272\270\221\002\005\n\003\010\333\004\202\323\344\223\0029\"4/api/v1alpha1/insights/insights/updatecommonsinsight:\001*'
  _INSIGHTS.methods_by_name['DeleteCommonsInsight']._options = None
  _INSIGHTS.methods_by_name['DeleteCommonsInsight']._serialized_options = b'\272\270\221\002\005\n\003\010\333\004\202\323\344\223\0029\"4/api/v1alpha1/insights/insights/deletecommonsinsight:\001*'
  _INSIGHTS.methods_by_name['GetVfsSchema']._options = None
  _INSIGHTS.methods_by_name['GetVfsSchema']._serialized_options = b'\272\270\221\002\005\n\003\010\334\004\202\323\344\223\0021\",/api/v1alpha1/insights/insights/getvfsschema:\001*'
  _INSIGHTS.methods_by_name['ListVfses']._options = None
  _INSIGHTS.methods_by_name['ListVfses']._serialized_options = b'\272\270\221\002\005\n\003\010\334\004\202\323\344\223\002.\")/api/v1alpha1/insights/insights/listvfses:\001*'
  _globals['_INSIGHTS']._serialized_start=155
  _globals['_INSIGHTS']._serialized_end=1941
# @@protoc_insertion_point(module_scope)
