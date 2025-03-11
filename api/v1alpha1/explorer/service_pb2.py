# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/explorer/service.proto
# Protobuf Python Version: 6.30.0
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
    0,
    '',
    'api/v1alpha1/explorer/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import bireportgenerator_pb2 as api_dot_commons_dot_bireportgenerator__pb2
from api.v1alpha1.explorer import entities_pb2 as api_dot_v1alpha1_dot_explorer_dot_entities__pb2
from api.v1alpha1.explorer import pipeline_pb2 as api_dot_v1alpha1_dot_explorer_dot_pipeline__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/explorer/service.proto\x12\x15\x61pi.v1alpha1.explorer\x1a\x17\x61nnotations/authz.proto\x1a#api/commons/bireportgenerator.proto\x1a$api/v1alpha1/explorer/entities.proto\x1a$api/v1alpha1/explorer/pipeline.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\".\n\x15GetWeeksOfDataRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"\x84\x01\n\x16GetWeeksOfDataResponse\x12\"\n\rweeks_of_data\x18\x01 \x01(\x05R\x0bweeksOfData\x12\x46\n\x11\x61\x63\x63\x65ss_start_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0f\x61\x63\x63\x65ssStartDate\"\x99\x01\n\x1cListDatasourceSchemasRequest\x12)\n\x10\x64\x61tasource_names\x18\x01 \x03(\tR\x0f\x64\x61tasourceNames\x12N\n\x0f\x64\x61tasource_type\x18\x02 \x01(\x0e\x32%.api.v1alpha1.explorer.DatasourceTypeR\x0e\x64\x61tasourceType\"X\n\x1dListDatasourceSchemasResponse\x12\x37\n\x07schemas\x18\x01 \x03(\x0b\x32\x1d.api.v1alpha1.explorer.SchemaR\x07schemas\"\x8b\x06\n\x0cQueryRequest\x12\'\n\x0f\x64\x61tasource_name\x18\x01 \x01(\tR\x0e\x64\x61tasourceName\x12N\n\x0f\x64\x61tasource_type\x18\x02 \x01(\x0e\x32%.api.v1alpha1.explorer.DatasourceTypeR\x0e\x64\x61tasourceType\x12\x1c\n\x08pipeline\x18\x03 \x01(\tH\x00R\x08pipeline\x12\x14\n\x04prql\x18\x04 \x01(\tH\x00R\x04prql\x12H\n\x0equery_pipeline\x18\x10 \x01(\x0b\x32\x1f.api.v1alpha1.explorer.PipelineH\x00R\rqueryPipeline\x12\x17\n\x07org_ids\x18\x05 \x03(\tR\x06orgIds\x12\x39\n\nstart_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x35\n\x08\x65nd_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x07\x65ndTime\x12\x1a\n\x08timezone\x18\x08 \x01(\tR\x08timezone\x12R\n\x13pipeline_parameters\x18\t \x01(\x0b\x32!.api.v1alpha1.explorer.ParametersR\x12pipelineParameters\x12\x1e\n\x0bui_trace_id\x18\n \x01(\tR\tuiTraceId\x12\x18\n\x07\x63omment\x18\x0b \x01(\tR\x07\x63omment\x12;\n\x06\x66ormat\x18\x0c \x01(\x0e\x32#.api.v1alpha1.explorer.ExportFormatR\x06\x66ormat\x12\x38\n\x0btime_period\x18\x0f \x01(\x0e\x32\x17.api.commons.TimePeriodR\ntimePeriod\x12;\n\x0breport_date\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nreportDateB\x07\n\x05queryJ\x04\x08\r\x10\x0eR\x0cinsight_body\"\xa5\x02\n\rQueryResponse\x12\x1d\n\nresult_url\x18\x01 \x01(\tR\tresultUrl\x12*\n\x11result_size_bytes\x18\x02 \x01(\x03R\x0fresultSizeBytes\x12}\n\x19time_filtered_datasources\x18\x03 \x03(\x0b\x32\x41.api.v1alpha1.explorer.QueryResponse.TimeFilteredDatasourcesEntryR\x17timeFilteredDatasources\x1aJ\n\x1cTimeFilteredDatasourcesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\"u\n\x13SupportQueryRequest\x12H\n\rquery_request\x18\x01 \x01(\x0b\x32#.api.v1alpha1.explorer.QueryRequestR\x0cqueryRequest\x12\x14\n\x05\x64\x65\x62ug\x18\x02 \x01(\x08R\x05\x64\x65\x62ug\"\xf4\x02\n\x14SupportQueryResponse\x12\x1d\n\nresult_url\x18\x01 \x01(\tR\tresultUrl\x12*\n\x11result_size_bytes\x18\x02 \x01(\x03R\x0fresultSizeBytes\x12\x12\n\x04prql\x18\x03 \x01(\tR\x04prql\x12\x10\n\x03sql\x18\x04 \x01(\tR\x03sql\x12\x18\n\x07\x65xplain\x18\x05 \x01(\tR\x07\x65xplain\x12\x84\x01\n\x19time_filtered_datasources\x18\x06 \x03(\x0b\x32H.api.v1alpha1.explorer.SupportQueryResponse.TimeFilteredDatasourcesEntryR\x17timeFilteredDatasources\x1aJ\n\x1cTimeFilteredDatasourcesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\"_\n\x13QueryExplainRequest\x12H\n\rquery_request\x18\x01 \x01(\x0b\x32#.api.v1alpha1.explorer.QueryRequestR\x0cqueryRequest\"\xf4\x02\n\x14QueryExplainResponse\x12\x1d\n\nresult_url\x18\x01 \x01(\tR\tresultUrl\x12*\n\x11result_size_bytes\x18\x02 \x01(\x03R\x0fresultSizeBytes\x12\x12\n\x04prql\x18\x03 \x01(\tR\x04prql\x12\x10\n\x03sql\x18\x04 \x01(\tR\x03sql\x12\x18\n\x07\x65xplain\x18\x05 \x01(\tR\x07\x65xplain\x12\x84\x01\n\x19time_filtered_datasources\x18\x06 \x03(\x0b\x32H.api.v1alpha1.explorer.QueryExplainResponse.TimeFilteredDatasourcesEntryR\x17timeFilteredDatasources\x1aJ\n\x1cTimeFilteredDatasourcesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\x08R\x05value:\x02\x38\x01\x32\x85\x07\n\x0f\x45xplorerService\x12\xcb\x01\n\x15ListDatasourceSchemas\x12\x33.api.v1alpha1.explorer.ListDatasourceSchemasRequest\x1a\x34.api.v1alpha1.explorer.ListDatasourceSchemasResponse\"G\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02:\"5/api/v1alpha1/explorer/explorer/listdatasourceschemas:\x01*\x12\x8b\x01\n\x05Query\x12#.api.v1alpha1.explorer.QueryRequest\x1a$.api.v1alpha1.explorer.QueryResponse\"7\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/explorer/explorer/query:\x01*\x12\xb0\x01\n\x0fGetSupportQuery\x12*.api.v1alpha1.explorer.SupportQueryRequest\x1a+.api.v1alpha1.explorer.SupportQueryResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xfa\x01\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/explorer/explorer/getsupportquery:\x01*\x12\xb0\x01\n\x0fGetQueryExplain\x12*.api.v1alpha1.explorer.QueryExplainRequest\x1a+.api.v1alpha1.explorer.QueryExplainResponse\"D\xba\xb8\x91\x02\x05\n\x03\x08\xc8\x01\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/explorer/explorer/getqueryexplain:\x01*\x12\xaf\x01\n\x0eGetWeeksOfData\x12,.api.v1alpha1.explorer.GetWeeksOfDataRequest\x1a-.api.v1alpha1.explorer.GetWeeksOfDataResponse\"@\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/explorer/explorer/getweeksofdata:\x01*B\x9f\x01\n\x19\x63om.api.v1alpha1.explorerB\x0cServiceProtoP\x01\xa2\x02\x03\x41VE\xaa\x02\x15\x41pi.V1alpha1.Explorer\xca\x02\x15\x41pi\\V1alpha1\\Explorer\xe2\x02!Api\\V1alpha1\\Explorer\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Explorerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.explorer.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.api.v1alpha1.explorerB\014ServiceProtoP\001\242\002\003AVE\252\002\025Api.V1alpha1.Explorer\312\002\025Api\\V1alpha1\\Explorer\342\002!Api\\V1alpha1\\Explorer\\GPBMetadata\352\002\027Api::V1alpha1::Explorer'
  _globals['_QUERYRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._loaded_options = None
  _globals['_QUERYRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._serialized_options = b'8\001'
  _globals['_SUPPORTQUERYRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._loaded_options = None
  _globals['_SUPPORTQUERYRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._serialized_options = b'8\001'
  _globals['_QUERYEXPLAINRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._loaded_options = None
  _globals['_QUERYEXPLAINRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._serialized_options = b'8\001'
  _globals['_EXPLORERSERVICE'].methods_by_name['ListDatasourceSchemas']._loaded_options = None
  _globals['_EXPLORERSERVICE'].methods_by_name['ListDatasourceSchemas']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002:\"5/api/v1alpha1/explorer/explorer/listdatasourceschemas:\001*'
  _globals['_EXPLORERSERVICE'].methods_by_name['Query']._loaded_options = None
  _globals['_EXPLORERSERVICE'].methods_by_name['Query']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002*\"%/api/v1alpha1/explorer/explorer/query:\001*'
  _globals['_EXPLORERSERVICE'].methods_by_name['GetSupportQuery']._loaded_options = None
  _globals['_EXPLORERSERVICE'].methods_by_name['GetSupportQuery']._serialized_options = b'\272\270\221\002\005\n\003\010\372\001\202\323\344\223\0024\"//api/v1alpha1/explorer/explorer/getsupportquery:\001*'
  _globals['_EXPLORERSERVICE'].methods_by_name['GetQueryExplain']._loaded_options = None
  _globals['_EXPLORERSERVICE'].methods_by_name['GetQueryExplain']._serialized_options = b'\272\270\221\002\005\n\003\010\310\001\202\323\344\223\0024\"//api/v1alpha1/explorer/explorer/getqueryexplain:\001*'
  _globals['_EXPLORERSERVICE'].methods_by_name['GetWeeksOfData']._loaded_options = None
  _globals['_EXPLORERSERVICE'].methods_by_name['GetWeeksOfData']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0023\"./api/v1alpha1/explorer/explorer/getweeksofdata:\001*'
  _globals['_GETWEEKSOFDATAREQUEST']._serialized_start=263
  _globals['_GETWEEKSOFDATAREQUEST']._serialized_end=309
  _globals['_GETWEEKSOFDATARESPONSE']._serialized_start=312
  _globals['_GETWEEKSOFDATARESPONSE']._serialized_end=444
  _globals['_LISTDATASOURCESCHEMASREQUEST']._serialized_start=447
  _globals['_LISTDATASOURCESCHEMASREQUEST']._serialized_end=600
  _globals['_LISTDATASOURCESCHEMASRESPONSE']._serialized_start=602
  _globals['_LISTDATASOURCESCHEMASRESPONSE']._serialized_end=690
  _globals['_QUERYREQUEST']._serialized_start=693
  _globals['_QUERYREQUEST']._serialized_end=1472
  _globals['_QUERYRESPONSE']._serialized_start=1475
  _globals['_QUERYRESPONSE']._serialized_end=1768
  _globals['_QUERYRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._serialized_start=1694
  _globals['_QUERYRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._serialized_end=1768
  _globals['_SUPPORTQUERYREQUEST']._serialized_start=1770
  _globals['_SUPPORTQUERYREQUEST']._serialized_end=1887
  _globals['_SUPPORTQUERYRESPONSE']._serialized_start=1890
  _globals['_SUPPORTQUERYRESPONSE']._serialized_end=2262
  _globals['_SUPPORTQUERYRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._serialized_start=1694
  _globals['_SUPPORTQUERYRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._serialized_end=1768
  _globals['_QUERYEXPLAINREQUEST']._serialized_start=2264
  _globals['_QUERYEXPLAINREQUEST']._serialized_end=2359
  _globals['_QUERYEXPLAINRESPONSE']._serialized_start=2362
  _globals['_QUERYEXPLAINRESPONSE']._serialized_end=2734
  _globals['_QUERYEXPLAINRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._serialized_start=1694
  _globals['_QUERYEXPLAINRESPONSE_TIMEFILTEREDDATASOURCESENTRY']._serialized_end=1768
  _globals['_EXPLORERSERVICE']._serialized_start=2737
  _globals['_EXPLORERSERVICE']._serialized_end=3638
# @@protoc_insertion_point(module_scope)
