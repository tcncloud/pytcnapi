# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/explorer/entities.proto
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
    'api/v1alpha1/explorer/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$api/v1alpha1/explorer/entities.proto\x12\x15\x61pi.v1alpha1.explorer\"\xe9\x02\n\x0bSchemaField\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x42\n\x0b\x63olumn_type\x18\x02 \x01(\x0e\x32!.api.v1alpha1.explorer.SchemaTypeR\ncolumnType\x12$\n\x0eis_primary_key\x18\x03 \x01(\x08R\x0cisPrimaryKey\x12,\n\x12is_low_cardinality\x18\x04 \x01(\x08R\x10isLowCardinality\x12-\n\x12\x63olumn_description\x18\x05 \x01(\tR\x11\x63olumnDescription\x12$\n\x0eis_time_filter\x18\x06 \x01(\x08R\x0cisTimeFilter\x12\x33\n\x16is_default_time_filter\x18\x07 \x01(\x08R\x13isDefaultTimeFilter\x12$\n\x0eis_join_column\x18\x08 \x01(\x08R\x0cisJoinColumn\"\x94\x02\n\x06Schema\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12N\n\x0f\x64\x61tasource_type\x18\x02 \x01(\x0e\x32%.api.v1alpha1.explorer.DatasourceTypeR\x0e\x64\x61tasourceType\x12:\n\x06\x66ields\x18\x03 \x03(\x0b\x32\".api.v1alpha1.explorer.SchemaFieldR\x06\x66ields\x12+\n\x11table_description\x18\x04 \x01(\tR\x10tableDescription\x12\x1a\n\x08\x63\x61tegory\x18\x05 \x01(\tR\x08\x63\x61tegory\x12!\n\x0csub_category\x18\x06 \x01(\tR\x0bsubCategory\"\x8b\x02\n\nParameters\x12Q\n\nparameters\x18\x01 \x03(\x0b\x32\x31.api.v1alpha1.explorer.Parameters.ParametersEntryR\nparameters\x1a>\n\tParameter\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x1b\n\tdata_type\x18\x03 \x01(\tR\x08\x64\x61taType\x1aj\n\x0fParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32+.api.v1alpha1.explorer.Parameters.ParameterR\x05value:\x02\x38\x01\"=\n\nResultFile\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x1d\n\nsize_bytes\x18\x02 \x01(\x03R\tsizeBytes\"\xe4\x01\n\rExportOptions\x12\x1c\n\tdelimiter\x18\x01 \x01(\tR\tdelimiter\x12N\n\x0fquote_character\x18\x02 \x01(\x0e\x32%.api.v1alpha1.explorer.QuoteCharacterR\x0equoteCharacter\x12\x1b\n\tno_header\x18\x03 \x01(\x08R\x08noHeader\x12H\n\rexport_format\x18\x04 \x01(\x0e\x32#.api.v1alpha1.explorer.ExportFormatR\x0c\x65xportFormat*\x8d\x01\n\x0c\x45xportFormat\x12\x1d\n\x19REPORT_FORMAT_UNSPECIFIED\x10\x00\x12\x15\n\x11REPORT_FORMAT_CSV\x10\x01\x12\x19\n\x15REPORT_FORMAT_PARQUET\x10\x02\x12\x15\n\x11REPORT_FORMAT_TSV\x10\x03\x12\x15\n\x11REPORT_FORMAT_TXT\x10\x04*\xa5\x02\n\nSchemaType\x12\x1b\n\x17SCHEMA_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fSCHEMA_TYPE_INT\x10\x02\x12\x15\n\x11SCHEMA_TYPE_FLOAT\x10\x03\x12\x16\n\x12SCHEMA_TYPE_STRING\x10\x05\x12\x14\n\x10SCHEMA_TYPE_BOOL\x10\x06\x12\x19\n\x15SCHEMA_TYPE_TIMESTAMP\x10\x07\x12\x19\n\x15SCHEMA_TYPE_INT_ARRAY\x10\x08\x12\x1b\n\x17SCHEMA_TYPE_FLOAT_ARRAY\x10\t\x12\x1c\n\x18SCHEMA_TYPE_STRING_ARRAY\x10\n\x12\x1a\n\x16SCHEMA_TYPE_BOOL_ARRAY\x10\x0b\x12\x13\n\x0fSCHEMA_TYPE_MAP\x10\x0c*\x8c\x01\n\x0e\x44\x61tasourceType\x12\x1f\n\x1b\x44\x41TASOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13\x44\x41TASOURCE_TYPE_VFS\x10\x01\x12\x1e\n\x1a\x44\x41TASOURCE_TYPE_CLICKHOUSE\x10\x02\x12 \n\x1c\x44\x41TASOURCE_TYPE_INSTANT_DATA\x10\x03*r\n\nResultType\x12\x1b\n\x17RESULT_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12RESULT_TYPE_FORMAT\x10\x01\x12\x17\n\x13RESULT_TYPE_SUMMARY\x10\x02\x12\x16\n\x12RESULT_TYPE_REPORT\x10\x03*u\n\x0eQuoteCharacter\x12\x1f\n\x1bQUOTE_CHARACTER_UNSPECIFIED\x10\x00\x12 \n\x1cQUOTE_CHARACTER_DOUBLE_QUOTE\x10\x01\x12 \n\x1cQUOTE_CHARACTER_SINGLE_QUOTE\x10\x02\x42\xa0\x01\n\x19\x63om.api.v1alpha1.explorerB\rEntitiesProtoP\x01\xa2\x02\x03\x41VE\xaa\x02\x15\x41pi.V1alpha1.Explorer\xca\x02\x15\x41pi\\V1alpha1\\Explorer\xe2\x02!Api\\V1alpha1\\Explorer\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Explorerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.explorer.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.api.v1alpha1.explorerB\rEntitiesProtoP\001\242\002\003AVE\252\002\025Api.V1alpha1.Explorer\312\002\025Api\\V1alpha1\\Explorer\342\002!Api\\V1alpha1\\Explorer\\GPBMetadata\352\002\027Api::V1alpha1::Explorer'
  _globals['_PARAMETERS_PARAMETERSENTRY']._loaded_options = None
  _globals['_PARAMETERS_PARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_EXPORTFORMAT']._serialized_start=1271
  _globals['_EXPORTFORMAT']._serialized_end=1412
  _globals['_SCHEMATYPE']._serialized_start=1415
  _globals['_SCHEMATYPE']._serialized_end=1708
  _globals['_DATASOURCETYPE']._serialized_start=1711
  _globals['_DATASOURCETYPE']._serialized_end=1851
  _globals['_RESULTTYPE']._serialized_start=1853
  _globals['_RESULTTYPE']._serialized_end=1967
  _globals['_QUOTECHARACTER']._serialized_start=1969
  _globals['_QUOTECHARACTER']._serialized_end=2086
  _globals['_SCHEMAFIELD']._serialized_start=64
  _globals['_SCHEMAFIELD']._serialized_end=425
  _globals['_SCHEMA']._serialized_start=428
  _globals['_SCHEMA']._serialized_end=704
  _globals['_PARAMETERS']._serialized_start=707
  _globals['_PARAMETERS']._serialized_end=974
  _globals['_PARAMETERS_PARAMETER']._serialized_start=804
  _globals['_PARAMETERS_PARAMETER']._serialized_end=866
  _globals['_PARAMETERS_PARAMETERSENTRY']._serialized_start=868
  _globals['_PARAMETERS_PARAMETERSENTRY']._serialized_end=974
  _globals['_RESULTFILE']._serialized_start=976
  _globals['_RESULTFILE']._serialized_end=1037
  _globals['_EXPORTOPTIONS']._serialized_start=1040
  _globals['_EXPORTOPTIONS']._serialized_end=1268
# @@protoc_insertion_point(module_scope)
