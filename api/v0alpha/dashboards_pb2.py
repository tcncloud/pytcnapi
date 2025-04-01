# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v0alpha/dashboards.proto
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
    'api/v0alpha/dashboards.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from annotations.perms import license_pb2 as annotations_dot_perms_dot_license__pb2
from api.commons import bireportgenerator_pb2 as api_dot_commons_dot_bireportgenerator__pb2
from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/v0alpha/dashboards.proto\x12\x0b\x61pi.v0alpha\x1a\x17\x61nnotations/authz.proto\x1a\x1f\x61nnotations/perms/license.proto\x1a#api/commons/bireportgenerator.proto\x1a\x15\x61pi/commons/org.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"r\n\x17PublishDashboardRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x36\n\x17\x64\x65stination_resource_id\x18\x02 \x01(\tR\x15\x64\x65stinationResourceId\";\n\x18PublishDashboardResponse\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\"\x17\n\x15ListDashboardsRequest\"h\n\x16ListDashboardsResponse\x12N\n\x13\x64\x61shboard_summaries\x18\x01 \x03(\x0b\x32\x1d.api.v0alpha.DashboardSummaryR\x12\x64\x61shboardSummaries\"\xde\x01\n\x10\x44\x61shboardSummary\x12!\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tR\x0b\x64\x61shboardId\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1f\n\x0bpanel_count\x18\x04 \x01(\x05R\npanelCount\x12\x1f\n\x0bresource_id\x18\x05 \x01(\tR\nresourceId\x12-\n\x12standard_dashboard\x18\x06 \x01(\x08R\x11standardDashboard\"\x1c\n\x1aGetDefaultDashboardRequest\"`\n\x1aSetDefaultDashboardRequest\x12!\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tR\x0b\x64\x61shboardId\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\"\x19\n\x17ListProductTypesRequest\"H\n\x16ListProductTypesResult\x12.\n\x05types\x18\x01 \x03(\x0b\x32\x18.api.v0alpha.ProductTypeR\x05types\"1\n\x0bProductType\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x0e\n\x02id\x18\x02 \x01(\tR\x02id\"\\\n\x16\x44\x65leteDashboardRequest\x12!\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tR\x0b\x64\x61shboardId\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\"\x9b\x01\n\x13GetDashboardRequest\x12!\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tR\x0b\x64\x61shboardId\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\x12@\n\x0b\x61pplication\x18\x03 \x01(\x0e\x32\x1e.annotations.perms.ApplicationR\x0b\x61pplication\"\xe6\x01\n\x16\x43reateDashboardRequest\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x34\n\x06layout\x18\x03 \x01(\x0b\x32\x1c.api.v0alpha.DashboardLayoutR\x06layout\x12.\n\x04view\x18\x04 \x01(\x0b\x32\x1a.api.v0alpha.DashboardViewR\x04view\x12.\n\x04type\x18\x05 \x01(\x0b\x32\x1a.api.v0alpha.DashboardTypeR\x04type\"]\n\x17\x43reateDashboardResponse\x12!\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tR\x0b\x64\x61shboardId\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\"F\n\x0f\x44\x61shboardLayout\x12\x33\n\x06panels\x18\x01 \x03(\x0b\x32\x1b.api.v0alpha.DashboardPanelR\x06panels\"\xd1\x01\n\x0e\x44\x61shboardPanel\x12;\n\x0cpanel_source\x18\x01 \x01(\x0b\x32\x18.api.v0alpha.PanelSourceR\x0bpanelSource\x12\x1d\n\nrow_length\x18\x02 \x01(\x03R\trowLength\x12#\n\rcolumn_length\x18\x03 \x01(\x03R\x0c\x63olumnLength\x12\x1b\n\trow_start\x18\x04 \x01(\x03R\x08rowStart\x12!\n\x0c\x63olumn_start\x18\x05 \x01(\x03R\x0b\x63olumnStart\"\xe9\x01\n\x0bPanelSource\x12#\n\ninsight_id\x18\x01 \x01(\tB\x02\x18\x01H\x00R\tinsightId\x12,\n\x11legacy_insight_id\x18\x02 \x01(\tH\x00R\x0flegacyInsightId\x12\x30\n\x13insight_resource_id\x18\x03 \x01(\tH\x00R\x11insightResourceId\x12G\n output_configuration_resource_id\x18\x04 \x01(\tR\x1doutputConfigurationResourceIdB\x0c\n\npanel_type\"\xcc\x02\n\tDashboard\x12!\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tR\x0b\x64\x61shboardId\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x34\n\x06layout\x18\x04 \x01(\x0b\x32\x1c.api.v0alpha.DashboardLayoutR\x06layout\x12.\n\x04view\x18\x05 \x01(\x0b\x32\x1a.api.v0alpha.DashboardViewR\x04view\x12.\n\x04type\x18\x06 \x01(\x0b\x32\x1a.api.v0alpha.DashboardTypeR\x04type\x12\x1f\n\x0bresource_id\x18\x07 \x01(\tR\nresourceId\x12-\n\x12standard_dashboard\x18\x08 \x01(\x08R\x11standardDashboard\"\x8e\x01\n\rDashboardType\x12\x39\n\x08historic\x18\x06 \x01(\x0b\x32\x1b.api.v0alpha.HistoricConfigH\x00R\x08historic\x12:\n\treal_time\x18\x07 \x01(\x0b\x32\x1b.api.v0alpha.RealTimeConfigH\x00R\x08realTimeB\x06\n\x04type\"\xa4\x02\n\x0eHistoricConfig\x12J\n\x10time_span_simple\x18\x01 \x01(\x0e\x32\x1e.api.v0alpha.TimeSpan.IntervalH\x00R\x0etimeSpanSimple\x12\x45\n\x0ftime_span_range\x18\x03 \x01(\x0b\x32\x1b.api.v0alpha.TimeSpan.RangeH\x00R\rtimeSpanRange\x12\x32\n\ttime_zone\x18\x04 \x01(\x0e\x32\x15.api.commons.TimeZoneR\x08timeZone\x12\x38\n\x0btime_period\x18\x05 \x01(\x0e\x32\x17.api.commons.TimePeriodR\ntimePeriodB\x0b\n\ttime_spanJ\x04\x08\x02\x10\x03\"\x10\n\x0eRealTimeConfig\"\xaa\x02\n\x16UpdateDashboardRequest\x12!\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tR\x0b\x64\x61shboardId\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x34\n\x06layout\x18\x04 \x01(\x0b\x32\x1c.api.v0alpha.DashboardLayoutR\x06layout\x12.\n\x04view\x18\x05 \x01(\x0b\x32\x1a.api.v0alpha.DashboardViewR\x04view\x12.\n\x04type\x18\x06 \x01(\x0b\x32\x1a.api.v0alpha.DashboardTypeR\x04type\x12\x1f\n\x0bresource_id\x18\x07 \x01(\tR\nresourceId\"\xa7\x01\n)UpdateDashboardTitleAndDescriptionRequest\x12!\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tR\x0b\x64\x61shboardId\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1f\n\x0bresource_id\x18\x04 \x01(\tR\nresourceId\"\x98\x01\n\x1cUpdateDashboardLayoutRequest\x12!\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tR\x0b\x64\x61shboardId\x12\x34\n\x06layout\x18\x02 \x01(\x0b\x32\x1c.api.v0alpha.DashboardLayoutR\x06layout\x12\x1f\n\x0bresource_id\x18\x03 \x01(\tR\nresourceId\"\x90\x01\n\x1aUpdateDashboardViewRequest\x12!\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tR\x0b\x64\x61shboardId\x12.\n\x04view\x18\x02 \x01(\x0b\x32\x1a.api.v0alpha.DashboardViewR\x04view\x12\x1f\n\x0bresource_id\x18\x03 \x01(\tR\nresourceId\"@\n\rDashboardView\x12\x17\n\x07org_ids\x18\x02 \x03(\tR\x06orgIdsJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\"\x9c\x02\n\x08TimeSpan\x1ag\n\x05Range\x12\x30\n\x05start\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x05start\x12,\n\x03\x65nd\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x03\x65nd\"\xa6\x01\n\x08Interval\x12\t\n\x05TODAY\x10\x00\x12\r\n\tYESTERDAY\x10\x01\x12\x10\n\x0cLAST_30_DAYS\x10\x02\x12\x11\n\rMONTH_TO_DATE\x10\x03\x12\x10\n\x0cLAST_2_WEEKS\x10\x04\x12\r\n\tTHIS_WEEK\x10\x05\x12\x0e\n\nTHIS_MONTH\x10\x06\x12\x16\n\x12THIS_DAY_LAST_WEEK\x10\x07\x12\x12\n\x0ePREVIOUS_MONTH\x10\x08\"\xb0\x01\n!CreateApplicationDashboardRequest\x12\x32\n\x15\x64\x61shboard_resource_id\x18\x01 \x01(\tR\x13\x64\x61shboardResourceId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12@\n\x0b\x61pplication\x18\x03 \x01(\x0e\x32\x1e.annotations.perms.ApplicationR\x0b\x61pplication\"$\n\"CreateApplicationDashboardResponse\"#\n!ListApplicationsDashboardsRequest\"\xa9\x01\n\x15\x41pplicationDashboards\x12@\n\x0b\x61pplication\x18\x01 \x01(\x0e\x32\x1e.annotations.perms.ApplicationR\x0b\x61pplication\x12N\n\x13\x64\x61shboard_summaries\x18\x02 \x03(\x0b\x32\x1d.api.v0alpha.DashboardSummaryR\x12\x64\x61shboardSummaries\"\x7f\n\"ListApplicationsDashboardsResponse\x12Y\n\x16\x61pplication_dashboards\x18\x01 \x03(\x0b\x32\".api.v0alpha.ApplicationDashboardsR\x15\x61pplicationDashboards\"\xb0\x01\n!DeleteApplicationDashboardRequest\x12@\n\x0b\x61pplication\x18\x01 \x01(\x0e\x32\x1e.annotations.perms.ApplicationR\x0b\x61pplication\x12\x32\n\x15\x64\x61shboard_resource_id\x18\x02 \x01(\tR\x13\x64\x61shboardResourceId\x12\x15\n\x06org_id\x18\x03 \x01(\tR\x05orgId\"$\n\"DeleteApplicationDashboardResponse2\xf4\x13\n\nDashboards\x12\x9d\x01\n\x0f\x43reateDashboard\x12#.api.v0alpha.CreateDashboardRequest\x1a$.api.v0alpha.CreateDashboardResponse\"?\xba\xb8\x91\x02\x08\n\x06\x08\xd9\x04\x08\xda\x04\x82\xd3\xe4\x93\x02,\"\'/api/v0alpha/dashboards/CreateDashboard:\x01*\x12\xa4\x01\n\x0cGetDashboard\x12 .api.v0alpha.GetDashboardRequest\x1a\x16.api.v0alpha.Dashboard\"Z\xba\xb8\x91\x02&\n\x03\x08\xd9\x04\n\t\x08\xd4\x02\x12\x04\x08\x03\x10\x01\n\t\x08\xc0\x0c\x12\x04\x08\x03\x10\x13\n\t\x08\xc1\x0c\x12\x04\x08\x03\x10\x13\x82\xd3\xe4\x93\x02)\"$/api/v0alpha/dashboards/GetDashboard:\x01*\x12\x98\x01\n\x13GetDefaultDashboard\x12\'.api.v0alpha.GetDefaultDashboardRequest\x1a\x16.api.v0alpha.Dashboard\"@\xba\xb8\x91\x02\x05\n\x03\x08\xd9\x04\x82\xd3\xe4\x93\x02\x30\"+/api/v0alpha/dashboards/GetDefaultDashboard:\x01*\x12\x96\x01\n\x0eListDashboards\x12\".api.v0alpha.ListDashboardsRequest\x1a#.api.v0alpha.ListDashboardsResponse\";\xba\xb8\x91\x02\x05\n\x03\x08\xd9\x04\x82\xd3\xe4\x93\x02+\"&/api/v0alpha/dashboards/ListDashboards:\x01*\x12\x9c\x01\n\x10ListProductTypes\x12$.api.v0alpha.ListProductTypesRequest\x1a#.api.v0alpha.ListProductTypesResult\"=\xba\xb8\x91\x02\x05\n\x03\x08\xd9\x04\x82\xd3\xe4\x93\x02-\"(/api/v0alpha/dashboards/ListProductTypes:\x01*\x12\x8f\x01\n\x0f\x44\x65leteDashboard\x12#.api.v0alpha.DeleteDashboardRequest\x1a\x16.google.protobuf.Empty\"?\xba\xb8\x91\x02\x08\n\x06\x08\xd9\x04\x08\xda\x04\x82\xd3\xe4\x93\x02,\"\'/api/v0alpha/dashboards/DeleteDashboard:\x01*\x12\x9b\x01\n\x13SetDefaultDashboard\x12\'.api.v0alpha.SetDefaultDashboardRequest\x1a\x16.google.protobuf.Empty\"C\xba\xb8\x91\x02\x08\n\x06\x08\xd9\x04\x08\xda\x04\x82\xd3\xe4\x93\x02\x30\"+/api/v0alpha/dashboards/SetDefaultDashboard:\x01*\x12\x8f\x01\n\x0fUpdateDashboard\x12#.api.v0alpha.UpdateDashboardRequest\x1a\x16.google.protobuf.Empty\"?\xba\xb8\x91\x02\x08\n\x06\x08\xd9\x04\x08\xda\x04\x82\xd3\xe4\x93\x02,\"\'/api/v0alpha/dashboards/UpdateDashboard:\x01*\x12\xc8\x01\n\"UpdateDashboardTitleAndDescription\x12\x36.api.v0alpha.UpdateDashboardTitleAndDescriptionRequest\x1a\x16.google.protobuf.Empty\"R\xba\xb8\x91\x02\x08\n\x06\x08\xd9\x04\x08\xda\x04\x82\xd3\xe4\x93\x02?\":/api/v0alpha/dashboards/UpdateDashboardTitleAndDescription:\x01*\x12\x9b\x01\n\x13UpdateDashboardView\x12\'.api.v0alpha.UpdateDashboardViewRequest\x1a\x16.google.protobuf.Empty\"C\xba\xb8\x91\x02\x08\n\x06\x08\xd9\x04\x08\xda\x04\x82\xd3\xe4\x93\x02\x30\"+/api/v0alpha/dashboards/UpdateDashboardView:\x01*\x12\xa1\x01\n\x15UpdateDashboardLayout\x12).api.v0alpha.UpdateDashboardLayoutRequest\x1a\x16.google.protobuf.Empty\"E\xba\xb8\x91\x02\x08\n\x06\x08\xd9\x04\x08\xda\x04\x82\xd3\xe4\x93\x02\x32\"-/api/v0alpha/dashboards/UpdateDashboardLayout:\x01*\x12\xa1\x01\n\x10PublishDashboard\x12$.api.v0alpha.PublishDashboardRequest\x1a%.api.v0alpha.PublishDashboardResponse\"@\xba\xb8\x91\x02\x08\n\x06\x08\xfb\x01\x08\xda\x04\x82\xd3\xe4\x93\x02-\"(/api/v0alpha/dashboards/PublishDashboard:\x01*\x12\xc6\x01\n\x1a\x43reateApplicationDashboard\x12..api.v0alpha.CreateApplicationDashboardRequest\x1a/.api.v0alpha.CreateApplicationDashboardResponse\"G\xba\xb8\x91\x02\x05\n\x03\x08\xda\x04\x82\xd3\xe4\x93\x02\x37\"2/api/v0alpha/dashboards/CreateApplicationDashboard:\x01*\x12\xc6\x01\n\x1aListApplicationsDashboards\x12..api.v0alpha.ListApplicationsDashboardsRequest\x1a/.api.v0alpha.ListApplicationsDashboardsResponse\"G\xba\xb8\x91\x02\x05\n\x03\x08\xda\x04\x82\xd3\xe4\x93\x02\x37\"2/api/v0alpha/dashboards/ListApplicationsDashboards:\x01*\x12\xc6\x01\n\x1a\x44\x65leteApplicationDashboard\x12..api.v0alpha.DeleteApplicationDashboardRequest\x1a/.api.v0alpha.DeleteApplicationDashboardResponse\"G\xba\xb8\x91\x02\x05\n\x03\x08\xda\x04\x82\xd3\xe4\x93\x02\x37\"2/api/v0alpha/dashboards/DeleteApplicationDashboard:\x01*Bo\n\x0f\x63om.api.v0alphaB\x0f\x44\x61shboardsProtoP\x01\xa2\x02\x03\x41VX\xaa\x02\x0b\x41pi.V0alpha\xca\x02\x0b\x41pi\\V0alpha\xe2\x02\x17\x41pi\\V0alpha\\GPBMetadata\xea\x02\x0c\x41pi::V0alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v0alpha.dashboards_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.v0alphaB\017DashboardsProtoP\001\242\002\003AVX\252\002\013Api.V0alpha\312\002\013Api\\V0alpha\342\002\027Api\\V0alpha\\GPBMetadata\352\002\014Api::V0alpha'
  _globals['_PANELSOURCE'].fields_by_name['insight_id']._loaded_options = None
  _globals['_PANELSOURCE'].fields_by_name['insight_id']._serialized_options = b'\030\001'
  _globals['_DASHBOARDS'].methods_by_name['CreateDashboard']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['CreateDashboard']._serialized_options = b'\272\270\221\002\010\n\006\010\331\004\010\332\004\202\323\344\223\002,\"\'/api/v0alpha/dashboards/CreateDashboard:\001*'
  _globals['_DASHBOARDS'].methods_by_name['GetDashboard']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['GetDashboard']._serialized_options = b'\272\270\221\002&\n\003\010\331\004\n\t\010\324\002\022\004\010\003\020\001\n\t\010\300\014\022\004\010\003\020\023\n\t\010\301\014\022\004\010\003\020\023\202\323\344\223\002)\"$/api/v0alpha/dashboards/GetDashboard:\001*'
  _globals['_DASHBOARDS'].methods_by_name['GetDefaultDashboard']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['GetDefaultDashboard']._serialized_options = b'\272\270\221\002\005\n\003\010\331\004\202\323\344\223\0020\"+/api/v0alpha/dashboards/GetDefaultDashboard:\001*'
  _globals['_DASHBOARDS'].methods_by_name['ListDashboards']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['ListDashboards']._serialized_options = b'\272\270\221\002\005\n\003\010\331\004\202\323\344\223\002+\"&/api/v0alpha/dashboards/ListDashboards:\001*'
  _globals['_DASHBOARDS'].methods_by_name['ListProductTypes']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['ListProductTypes']._serialized_options = b'\272\270\221\002\005\n\003\010\331\004\202\323\344\223\002-\"(/api/v0alpha/dashboards/ListProductTypes:\001*'
  _globals['_DASHBOARDS'].methods_by_name['DeleteDashboard']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['DeleteDashboard']._serialized_options = b'\272\270\221\002\010\n\006\010\331\004\010\332\004\202\323\344\223\002,\"\'/api/v0alpha/dashboards/DeleteDashboard:\001*'
  _globals['_DASHBOARDS'].methods_by_name['SetDefaultDashboard']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['SetDefaultDashboard']._serialized_options = b'\272\270\221\002\010\n\006\010\331\004\010\332\004\202\323\344\223\0020\"+/api/v0alpha/dashboards/SetDefaultDashboard:\001*'
  _globals['_DASHBOARDS'].methods_by_name['UpdateDashboard']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['UpdateDashboard']._serialized_options = b'\272\270\221\002\010\n\006\010\331\004\010\332\004\202\323\344\223\002,\"\'/api/v0alpha/dashboards/UpdateDashboard:\001*'
  _globals['_DASHBOARDS'].methods_by_name['UpdateDashboardTitleAndDescription']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['UpdateDashboardTitleAndDescription']._serialized_options = b'\272\270\221\002\010\n\006\010\331\004\010\332\004\202\323\344\223\002?\":/api/v0alpha/dashboards/UpdateDashboardTitleAndDescription:\001*'
  _globals['_DASHBOARDS'].methods_by_name['UpdateDashboardView']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['UpdateDashboardView']._serialized_options = b'\272\270\221\002\010\n\006\010\331\004\010\332\004\202\323\344\223\0020\"+/api/v0alpha/dashboards/UpdateDashboardView:\001*'
  _globals['_DASHBOARDS'].methods_by_name['UpdateDashboardLayout']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['UpdateDashboardLayout']._serialized_options = b'\272\270\221\002\010\n\006\010\331\004\010\332\004\202\323\344\223\0022\"-/api/v0alpha/dashboards/UpdateDashboardLayout:\001*'
  _globals['_DASHBOARDS'].methods_by_name['PublishDashboard']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['PublishDashboard']._serialized_options = b'\272\270\221\002\010\n\006\010\373\001\010\332\004\202\323\344\223\002-\"(/api/v0alpha/dashboards/PublishDashboard:\001*'
  _globals['_DASHBOARDS'].methods_by_name['CreateApplicationDashboard']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['CreateApplicationDashboard']._serialized_options = b'\272\270\221\002\005\n\003\010\332\004\202\323\344\223\0027\"2/api/v0alpha/dashboards/CreateApplicationDashboard:\001*'
  _globals['_DASHBOARDS'].methods_by_name['ListApplicationsDashboards']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['ListApplicationsDashboards']._serialized_options = b'\272\270\221\002\005\n\003\010\332\004\202\323\344\223\0027\"2/api/v0alpha/dashboards/ListApplicationsDashboards:\001*'
  _globals['_DASHBOARDS'].methods_by_name['DeleteApplicationDashboard']._loaded_options = None
  _globals['_DASHBOARDS'].methods_by_name['DeleteApplicationDashboard']._serialized_options = b'\272\270\221\002\005\n\003\010\332\004\202\323\344\223\0027\"2/api/v0alpha/dashboards/DeleteApplicationDashboard:\001*'
  _globals['_PUBLISHDASHBOARDREQUEST']._serialized_start=255
  _globals['_PUBLISHDASHBOARDREQUEST']._serialized_end=369
  _globals['_PUBLISHDASHBOARDRESPONSE']._serialized_start=371
  _globals['_PUBLISHDASHBOARDRESPONSE']._serialized_end=430
  _globals['_LISTDASHBOARDSREQUEST']._serialized_start=432
  _globals['_LISTDASHBOARDSREQUEST']._serialized_end=455
  _globals['_LISTDASHBOARDSRESPONSE']._serialized_start=457
  _globals['_LISTDASHBOARDSRESPONSE']._serialized_end=561
  _globals['_DASHBOARDSUMMARY']._serialized_start=564
  _globals['_DASHBOARDSUMMARY']._serialized_end=786
  _globals['_GETDEFAULTDASHBOARDREQUEST']._serialized_start=788
  _globals['_GETDEFAULTDASHBOARDREQUEST']._serialized_end=816
  _globals['_SETDEFAULTDASHBOARDREQUEST']._serialized_start=818
  _globals['_SETDEFAULTDASHBOARDREQUEST']._serialized_end=914
  _globals['_LISTPRODUCTTYPESREQUEST']._serialized_start=916
  _globals['_LISTPRODUCTTYPESREQUEST']._serialized_end=941
  _globals['_LISTPRODUCTTYPESRESULT']._serialized_start=943
  _globals['_LISTPRODUCTTYPESRESULT']._serialized_end=1015
  _globals['_PRODUCTTYPE']._serialized_start=1017
  _globals['_PRODUCTTYPE']._serialized_end=1066
  _globals['_DELETEDASHBOARDREQUEST']._serialized_start=1068
  _globals['_DELETEDASHBOARDREQUEST']._serialized_end=1160
  _globals['_GETDASHBOARDREQUEST']._serialized_start=1163
  _globals['_GETDASHBOARDREQUEST']._serialized_end=1318
  _globals['_CREATEDASHBOARDREQUEST']._serialized_start=1321
  _globals['_CREATEDASHBOARDREQUEST']._serialized_end=1551
  _globals['_CREATEDASHBOARDRESPONSE']._serialized_start=1553
  _globals['_CREATEDASHBOARDRESPONSE']._serialized_end=1646
  _globals['_DASHBOARDLAYOUT']._serialized_start=1648
  _globals['_DASHBOARDLAYOUT']._serialized_end=1718
  _globals['_DASHBOARDPANEL']._serialized_start=1721
  _globals['_DASHBOARDPANEL']._serialized_end=1930
  _globals['_PANELSOURCE']._serialized_start=1933
  _globals['_PANELSOURCE']._serialized_end=2166
  _globals['_DASHBOARD']._serialized_start=2169
  _globals['_DASHBOARD']._serialized_end=2501
  _globals['_DASHBOARDTYPE']._serialized_start=2504
  _globals['_DASHBOARDTYPE']._serialized_end=2646
  _globals['_HISTORICCONFIG']._serialized_start=2649
  _globals['_HISTORICCONFIG']._serialized_end=2941
  _globals['_REALTIMECONFIG']._serialized_start=2943
  _globals['_REALTIMECONFIG']._serialized_end=2959
  _globals['_UPDATEDASHBOARDREQUEST']._serialized_start=2962
  _globals['_UPDATEDASHBOARDREQUEST']._serialized_end=3260
  _globals['_UPDATEDASHBOARDTITLEANDDESCRIPTIONREQUEST']._serialized_start=3263
  _globals['_UPDATEDASHBOARDTITLEANDDESCRIPTIONREQUEST']._serialized_end=3430
  _globals['_UPDATEDASHBOARDLAYOUTREQUEST']._serialized_start=3433
  _globals['_UPDATEDASHBOARDLAYOUTREQUEST']._serialized_end=3585
  _globals['_UPDATEDASHBOARDVIEWREQUEST']._serialized_start=3588
  _globals['_UPDATEDASHBOARDVIEWREQUEST']._serialized_end=3732
  _globals['_DASHBOARDVIEW']._serialized_start=3734
  _globals['_DASHBOARDVIEW']._serialized_end=3798
  _globals['_TIMESPAN']._serialized_start=3801
  _globals['_TIMESPAN']._serialized_end=4085
  _globals['_TIMESPAN_RANGE']._serialized_start=3813
  _globals['_TIMESPAN_RANGE']._serialized_end=3916
  _globals['_TIMESPAN_INTERVAL']._serialized_start=3919
  _globals['_TIMESPAN_INTERVAL']._serialized_end=4085
  _globals['_CREATEAPPLICATIONDASHBOARDREQUEST']._serialized_start=4088
  _globals['_CREATEAPPLICATIONDASHBOARDREQUEST']._serialized_end=4264
  _globals['_CREATEAPPLICATIONDASHBOARDRESPONSE']._serialized_start=4266
  _globals['_CREATEAPPLICATIONDASHBOARDRESPONSE']._serialized_end=4302
  _globals['_LISTAPPLICATIONSDASHBOARDSREQUEST']._serialized_start=4304
  _globals['_LISTAPPLICATIONSDASHBOARDSREQUEST']._serialized_end=4339
  _globals['_APPLICATIONDASHBOARDS']._serialized_start=4342
  _globals['_APPLICATIONDASHBOARDS']._serialized_end=4511
  _globals['_LISTAPPLICATIONSDASHBOARDSRESPONSE']._serialized_start=4513
  _globals['_LISTAPPLICATIONSDASHBOARDSRESPONSE']._serialized_end=4640
  _globals['_DELETEAPPLICATIONDASHBOARDREQUEST']._serialized_start=4643
  _globals['_DELETEAPPLICATIONDASHBOARDREQUEST']._serialized_end=4819
  _globals['_DELETEAPPLICATIONDASHBOARDRESPONSE']._serialized_start=4821
  _globals['_DELETEAPPLICATIONDASHBOARDRESPONSE']._serialized_end=4857
  _globals['_DASHBOARDS']._serialized_start=4860
  _globals['_DASHBOARDS']._serialized_end=7408
# @@protoc_insertion_point(module_scope)
