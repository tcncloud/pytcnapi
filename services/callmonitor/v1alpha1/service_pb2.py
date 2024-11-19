# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: services/callmonitor/v1alpha1/service.proto
# Protobuf Python Version: 5.28.3
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
    3,
    '',
    'services/callmonitor/v1alpha1/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import callmonitor_pb2 as api_dot_commons_dot_callmonitor__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+services/callmonitor/v1alpha1/service.proto\x12\x1dservices.callmonitor.v1alpha1\x1a\x17\x61nnotations/authz.proto\x1a\x1d\x61pi/commons/callmonitor.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe3\x02\n\x18GetHoldQueueStatsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x39\n\nstart_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12V\n\x06\x66ilter\x18\x04 \x01(\x0b\x32>.services.callmonitor.v1alpha1.GetHoldQueueStatsRequest.FilterR\x06\x66ilter\x1a\x66\n\x06\x46ilter\x12;\n\x06status\x18\x01 \x01(\x0e\x32#.api.commons.HoldQueueMonitorStatusR\x06status\x12\x1f\n\x0b\x63\x61mpaign_id\x18\x03 \x01(\tR\ncampaignId\"\xbf\x02\n\x19GetHoldQueueStatsResponse\x12\x35\n\x05stats\x18\x01 \x03(\x0b\x32\x1f.api.commons.HoldQueueCallStatsR\x05stats\x12&\n\x0ftotal_num_calls\x18\x02 \x01(\x05R\rtotalNumCalls\x12\x30\n\x14total_num_successful\x18\x03 \x01(\x05R\x12totalNumSuccessful\x12(\n\x10total_num_failed\x18\x04 \x01(\x05R\x0etotalNumFailed\x12\x35\n\x17\x61vg_monitor_duration_ms\x18\x05 \x01(\x03R\x14\x61vgMonitorDurationMs\x12\x30\n\x14total_num_monitoring\x18\x06 \x01(\x05R\x12totalNumMonitoring2\xe4\x01\n\x12\x43\x61llMonitorService\x12\xcd\x01\n\x11GetHoldQueueStats\x12\x37.services.callmonitor.v1alpha1.GetHoldQueueStatsRequest\x1a\x38.services.callmonitor.v1alpha1.GetHoldQueueStatsResponse\"E\xba\xb8\x91\x02\x05\n\x03\x08\xb0\t\x82\xd3\xe4\x93\x02\x35\"0/services/callmonitor/v1alpha1/getholdqueuestats:\x01*B\xc7\x01\n!com.services.callmonitor.v1alpha1B\x0cServiceProtoP\x01\xa2\x02\x03SCX\xaa\x02\x1dServices.Callmonitor.V1alpha1\xca\x02\x1dServices\\Callmonitor\\V1alpha1\xe2\x02)Services\\Callmonitor\\V1alpha1\\GPBMetadata\xea\x02\x1fServices::Callmonitor::V1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'services.callmonitor.v1alpha1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.services.callmonitor.v1alpha1B\014ServiceProtoP\001\242\002\003SCX\252\002\035Services.Callmonitor.V1alpha1\312\002\035Services\\Callmonitor\\V1alpha1\342\002)Services\\Callmonitor\\V1alpha1\\GPBMetadata\352\002\037Services::Callmonitor::V1alpha1'
  _globals['_CALLMONITORSERVICE'].methods_by_name['GetHoldQueueStats']._loaded_options = None
  _globals['_CALLMONITORSERVICE'].methods_by_name['GetHoldQueueStats']._serialized_options = b'\272\270\221\002\005\n\003\010\260\t\202\323\344\223\0025\"0/services/callmonitor/v1alpha1/getholdqueuestats:\001*'
  _globals['_GETHOLDQUEUESTATSREQUEST']._serialized_start=198
  _globals['_GETHOLDQUEUESTATSREQUEST']._serialized_end=553
  _globals['_GETHOLDQUEUESTATSREQUEST_FILTER']._serialized_start=451
  _globals['_GETHOLDQUEUESTATSREQUEST_FILTER']._serialized_end=553
  _globals['_GETHOLDQUEUESTATSRESPONSE']._serialized_start=556
  _globals['_GETHOLDQUEUESTATSRESPONSE']._serialized_end=875
  _globals['_CALLMONITORSERVICE']._serialized_start=878
  _globals['_CALLMONITORSERVICE']._serialized_end=1106
# @@protoc_insertion_point(module_scope)
