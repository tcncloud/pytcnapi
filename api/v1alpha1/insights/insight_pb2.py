# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/insights/insight.proto
# Protobuf Python Version: 5.29.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    2,
    '',
    'api/v1alpha1/insights/insight.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import insights_pb2 as api_dot_commons_dot_insights__pb2
from api.v1alpha1.explorer import entities_pb2 as api_dot_v1alpha1_dot_explorer_dot_entities__pb2
from api.v1alpha1.insights import insight_content_pb2 as api_dot_v1alpha1_dot_insights_dot_insight__content__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/insights/insight.proto\x12\x15\x61pi.v1alpha1.insights\x1a\x1a\x61pi/commons/insights.proto\x1a$api/v1alpha1/explorer/entities.proto\x1a+api/v1alpha1/insights/insight_content.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc9\x05\n\x07Insight\x12!\n\ninsight_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\tinsightId\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12;\n\x0cinsight_type\x18\x05 \x01(\x0e\x32\x18.api.commons.InsightTypeR\x0binsightType\x12\'\n\x0finsight_version\x18\x06 \x01(\rR\x0einsightVersion\x12\x12\n\x04\x62ody\x18\x07 \x01(\tR\x04\x62ody\x12Z\n\x17insight_permission_type\x18\x08 \x01(\x0e\x32\".api.commons.InsightPermissionTypeR\x15insightPermissionType\x12\x1f\n\x0bresource_id\x18\t \x01(\tR\nresourceId\x12)\n\x10standard_insight\x18\n \x01(\x08R\x0fstandardInsight\x12N\n\x0f\x64\x61tasource_type\x18\x0b \x01(\x0e\x32%.api.v1alpha1.explorer.DatasourceTypeR\x0e\x64\x61tasourceType\x12\'\n\x0f\x64\x61tasource_name\x18\x0c \x01(\tR\x0e\x64\x61tasourceName\x12;\n\x0b\x63reate_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12=\n\x08pipeline\x18\x10 \x01(\x0b\x32\x1f.api.v1alpha1.insights.PipelineH\x00R\x08pipelineB\x11\n\x0finsight_content\"p\n\x15PublishInsightRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12\x36\n\x17\x64\x65stination_resource_id\x18\x02 \x01(\tR\x15\x64\x65stinationResourceId\"R\n\x16PublishInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"P\n\x14\x43reateInsightRequest\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"Q\n\x15\x43reateInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"s\n\x13ListInsightsRequest\x12\\\n\x18insight_permission_types\x18\x02 \x03(\x0e\x32\".api.commons.InsightPermissionTypeR\x16insightPermissionTypes\"X\n\x1aListInsightsStreamResponse\x12:\n\x08insights\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x08insights\"R\n\x14ListInsightsResponse\x12:\n\x08insights\x18\x01 \x03(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x08insights\"/\n\x16ListOrgInsightsRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\"U\n\x17ListOrgInsightsResponse\x12:\n\x08insights\x18\x01 \x03(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x08insights\"\x8d\x01\n\x14UpdateInsightRequest\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\"Q\n\x15UpdateInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"Z\n\x14\x44\x65leteInsightRequest\x12!\n\ninsight_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\tinsightId\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\"Q\n\x15\x44\x65leteInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"W\n\x11GetInsightRequest\x12!\n\ninsight_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\tinsightId\x12\x1f\n\x0bresource_id\x18\x02 \x01(\tR\nresourceId\"N\n\x12GetInsightResponse\x12\x38\n\x07insight\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.insights.InsightR\x07insight\"4\n\x13GetVfsSchemaRequest\x12\x1d\n\nalias_name\x18\x01 \x01(\tR\taliasName\"\xc7\x02\n\x14GetVfsSchemaResponse\x12I\n\x06\x66ields\x18\x01 \x03(\x0b\x32\x31.api.v1alpha1.insights.GetVfsSchemaResponse.FieldR\x06\x66ields\x12\'\n\x0fvfs_description\x18\x02 \x01(\tR\x0evfsDescription\x12\x1d\n\nalias_name\x18\x03 \x01(\tR\taliasName\x1a\x9b\x01\n\x05\x46ield\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12\x42\n\x0b\x63olumn_type\x18\x02 \x01(\x0e\x32!.api.commons.InsightVfsSchemaTypeR\ncolumnType\x12-\n\x12\x63olumn_description\x18\x03 \x01(\tR\x11\x63olumnDescription\"\x12\n\x10ListVfsesRequest\"-\n\x11ListVfsesResponse\x12\x18\n\x07\x61liases\x18\x01 \x03(\tR\x07\x61liases\"\x17\n\x15ListVfsSchemasRequest\"f\n\x16ListVfsSchemasResponse\x12L\n\x0bvfs_schemas\x18\x01 \x03(\x0b\x32+.api.v1alpha1.insights.GetVfsSchemaResponseR\nvfsSchemas\"\xfb\x01\n\x12TableVisualization\x12Z\n\x14table_column_details\x18\x01 \x03(\x0b\x32(.api.v1alpha1.insights.TableColumnConfigR\x12tableColumnDetails\x12\x1c\n\tdelimiter\x18\x02 \x01(\tR\tdelimiter\x12N\n\x0fquote_character\x18\x03 \x01(\x0e\x32%.api.v1alpha1.insights.QuoteCharacterR\x0equoteCharacter\x12\x1b\n\tno_header\x18\x04 \x01(\x08R\x08noHeader\"V\n\x11\x43\x61rdVisualization\x12\x41\n\x0btext_values\x18\x01 \x03(\x0b\x32 .api.v1alpha1.insights.TextValueR\ntextValues\"V\n\tTextValue\x12I\n\nconditions\x18\x01 \x03(\x0b\x32).api.v1alpha1.insights.TextValueConditionR\nconditions\"\xe9\x02\n\x12TextValueCondition\x12\x45\n\nexpression\x18\x01 \x01(\x0b\x32%.api.v1alpha1.insights.ExpressionNodeR\nexpression\x12\x12\n\x04size\x18\x02 \x01(\x03R\x04size\x12\x46\n\noperations\x18\x03 \x03(\x0b\x32&.api.v1alpha1.insights.ColumnOperationR\noperations\x12\x1b\n\ticon_name\x18\x04 \x01(\tR\x08iconName\x12N\n\nicon_color\x18\x05 \x01(\x0b\x32/.api.v1alpha1.insights.TextValueCondition.ColorR\ticonColor\x1a\x43\n\x05\x43olor\x12\x10\n\x03red\x18\x01 \x01(\x03R\x03red\x12\x14\n\x05green\x18\x02 \x01(\x03R\x05green\x12\x12\n\x04\x62lue\x18\x03 \x01(\x03R\x04\x62lue\"\x9b\x04\n\x11TableColumnConfig\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12!\n\x0c\x63olumn_width\x18\x02 \x01(\x03R\x0b\x63olumnWidth\x12\x1f\n\x0bhide_column\x18\x03 \x01(\x08R\nhideColumn\x12\x1d\n\nrenamed_as\x18\x04 \x01(\tR\trenamedAs\x12\x46\n\noperations\x18\x05 \x03(\x0b\x32&.api.v1alpha1.insights.ColumnOperationR\noperations\x12\x62\n\x0e\x63olumn_summary\x18\x06 \x01(\x0e\x32;.api.v1alpha1.insights.OutputConfigurationColumnSummaryTypeR\rcolumnSummary\x12 \n\x0b\x64\x65scription\x18\x07 \x01(\tR\x0b\x64\x65scription\x12H\n\x0esort_direction\x18\x08 \x01(\x0e\x32!.api.v1alpha1.insights.ColumnSortR\rsortDirection\x12j\n\x19insight_contextual_action\x18\t \x01(\x0b\x32..api.v1alpha1.insights.InsightContextualActionR\x17insightContextualAction\"1\n\x0c\x46ormatSeries\x12!\n\x0c\x66ormat_parts\x18\x01 \x03(\tR\x0b\x66ormatParts\"i\n\x0cPadOperation\x12#\n\rpad_character\x18\x01 \x01(\tR\x0cpadCharacter\x12\x19\n\x08pad_left\x18\x02 \x01(\x08R\x07padLeft\x12\x19\n\x08pad_size\x18\x03 \x01(\x05R\x07padSize\"\xac\x02\n\x0f\x43olumnOperation\x12K\n\x0eoperation_type\x18\x01 \x01(\x0e\x32$.api.v1alpha1.insights.OperationTypeR\roperationType\x12!\n\x0b\x66loat_value\x18\x02 \x01(\x01H\x00R\nfloatValue\x12J\n\rformat_series\x18\x03 \x01(\x0b\x32#.api.v1alpha1.insights.FormatSeriesH\x00R\x0c\x66ormatSeries\x12J\n\rpad_operation\x18\x04 \x01(\x0b\x32#.api.v1alpha1.insights.PadOperationH\x00R\x0cpadOperationB\x11\n\x0foperation_value\"\xbe\x02\n\x17InsightContextualAction\x12\x46\n\x04type\x18\x01 \x01(\x0e\x32\x32.api.v1alpha1.insights.InsightContextualActionTypeR\x04type\x12\x37\n\x04link\x18\x02 \x01(\x0b\x32!.api.v1alpha1.insights.LinkActionH\x00R\x04link\x12\x46\n\tcomponent\x18\x03 \x01(\x0b\x32&.api.v1alpha1.insights.ComponentActionH\x00R\tcomponent\x12P\n\rdrill_through\x18\x04 \x01(\x0b\x32).api.v1alpha1.insights.DrillThroughActionH\x00R\x0c\x64rillThroughB\x08\n\x06\x61\x63tion\"\xd4\x01\n\nLinkAction\x12#\n\rlink_elements\x18\x01 \x03(\tR\x0clinkElements\x12^\n\x0f\x63omponent_value\x18\x02 \x03(\x0b\x32\x35.api.v1alpha1.insights.LinkAction.ComponentValueEntryR\x0e\x63omponentValue\x1a\x41\n\x13\x43omponentValueEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xe0\x01\n\x0f\x43omponentAction\x12%\n\x0e\x63omponent_name\x18\x01 \x01(\tR\rcomponentName\x12\x63\n\x0f\x63omponent_value\x18\x02 \x03(\x0b\x32:.api.v1alpha1.insights.ComponentAction.ComponentValueEntryR\x0e\x63omponentValue\x1a\x41\n\x13\x43omponentValueEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xac\x01\n\x12\x44rillThroughAction\x12.\n\x13insight_resource_id\x18\x01 \x01(\tR\x11insightResourceId\x12\x66\n\x18\x64rill_through_parameters\x18\x02 \x03(\x0b\x32,.api.v1alpha1.insights.DrillThroughParameterR\x16\x64rillThroughParameters\"_\n\x15\x44rillThroughParameter\x12%\n\x0eparameter_name\x18\x01 \x01(\tR\rparameterName\x12\x1f\n\x0b\x63olumn_name\x18\x02 \x01(\tR\ncolumnName\"\x80\x05\n\x13OutputConfiguration\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12<\n\x1aoutput_configuration_title\x18\x03 \x01(\tR\x18outputConfigurationTitle\x12j\n\x19output_configuration_type\x18\x04 \x01(\x0e\x32..api.v1alpha1.insights.OutputConfigurationTypeR\x17outputConfigurationType\x12.\n\x13insight_resource_id\x18\x05 \x01(\tR\x11insightResourceId\x12\x1d\n\nis_default\x18\x06 \x01(\x08R\tisDefault\x12\x14\n\x04\x62lob\x18\x07 \x01(\tH\x00R\x04\x62lob\x12\\\n\x13table_visualization\x18\x08 \x01(\x0b\x32).api.v1alpha1.insights.TableVisualizationH\x00R\x12tableVisualization\x12Y\n\x12\x63\x61rd_visualization\x18\x0b \x01(\x0b\x32(.api.v1alpha1.insights.CardVisualizationH\x00R\x11\x63\x61rdVisualization\x12;\n\x0b\x63reate_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTimeB\x06\n\x04\x62ody\"\x81\x01\n CreateOutputConfigurationRequest\x12]\n\x14output_configuration\x18\x01 \x01(\x0b\x32*.api.v1alpha1.insights.OutputConfigurationR\x13outputConfiguration\"\x82\x01\n!CreateOutputConfigurationResponse\x12]\n\x14output_configuration\x18\x01 \x01(\x0b\x32*.api.v1alpha1.insights.OutputConfigurationR\x13outputConfiguration\"Q\n\x1fListOutputConfigurationsRequest\x12.\n\x13insight_resource_id\x18\x01 \x01(\tR\x11insightResourceId\"\x83\x01\n ListOutputConfigurationsResponse\x12_\n\x15output_configurations\x18\x01 \x03(\x0b\x32*.api.v1alpha1.insights.OutputConfigurationR\x14outputConfigurations\"\xbe\x01\n UpdateOutputConfigurationRequest\x12;\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nupdateMask\x12]\n\x14output_configuration\x18\x03 \x01(\x0b\x32*.api.v1alpha1.insights.OutputConfigurationR\x13outputConfiguration\"\x82\x01\n!UpdateOutputConfigurationResponse\x12]\n\x14output_configuration\x18\x01 \x01(\x0b\x32*.api.v1alpha1.insights.OutputConfigurationR\x13outputConfiguration\"C\n DeleteOutputConfigurationRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\"#\n!DeleteOutputConfigurationResponse\"@\n\x1dGetOutputConfigurationRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\"\x7f\n\x1eGetOutputConfigurationResponse\x12]\n\x14output_configuration\x18\x01 \x01(\x0b\x32*.api.v1alpha1.insights.OutputConfigurationR\x13outputConfiguration\"w\n$SetDefaultOutputConfigurationRequest\x12\x1f\n\x0bresource_id\x18\x01 \x01(\tR\nresourceId\x12.\n\x13insight_resource_id\x18\x02 \x01(\tR\x11insightResourceId\"\'\n%SetDefaultOutputConfigurationResponse\"V\n$GetDefaultOutputConfigurationRequest\x12.\n\x13insight_resource_id\x18\x01 \x01(\tR\x11insightResourceId\"\x86\x01\n%GetDefaultOutputConfigurationResponse\x12]\n\x14output_configuration\x18\x01 \x01(\x0b\x32*.api.v1alpha1.insights.OutputConfigurationR\x13outputConfiguration*\xbc\x02\n\x17OutputConfigurationType\x12)\n%OUTPUT_CONFIGURATION_TYPE_UNSPECIFIED\x10\x00\x12#\n\x1fOUTPUT_CONFIGURATION_TYPE_TABLE\x10\x01\x12*\n&OUTPUT_CONFIGURATION_TYPE_MULTI_SERIES\x10\x02\x12\'\n#OUTPUT_CONFIGURATION_TYPE_PIE_CHART\x10\x03\x12)\n%OUTPUT_CONFIGURATION_TYPE_FIXED_WIDTH\x10\x04\x12&\n\"OUTPUT_CONFIGURATION_TYPE_TIMELINE\x10\x05\x12)\n%OUTPUT_CONFIGURATION_TYPE_TEXT_VALUES\x10\x06*\xe0\x02\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13OPERATION_TYPE_DATE\x10\x01\x12\x19\n\x15OPERATION_TYPE_PREFIX\x10\x02\x12\x19\n\x15OPERATION_TYPE_SUFFIX\x10\x03\x12\x1b\n\x17OPERATION_TYPE_DURATION\x10\x04\x12\x16\n\x12OPERATION_TYPE_ADD\x10\x05\x12\x1b\n\x17OPERATION_TYPE_SUBTRACT\x10\x06\x12\x1b\n\x17OPERATION_TYPE_MULTIPLY\x10\x07\x12\x19\n\x15OPERATION_TYPE_DIVIDE\x10\x08\x12 \n\x1cOPERATION_TYPE_FORMAT_NUMBER\x10\t\x12\x1c\n\x18OPERATION_TYPE_PRECISION\x10\n\x12\x16\n\x12OPERATION_TYPE_PAD\x10\x0b*`\n\nColumnSort\x12\x1b\n\x17\x43OLUMN_SORT_UNSPECIFIED\x10\x00\x12\x19\n\x15\x43OLUMN_SORT_ASCENDING\x10\x01\x12\x1a\n\x16\x43OLUMN_SORT_DESCENDING\x10\x02*\xa8\x02\n$OutputConfigurationColumnSummaryType\x12\x38\n4OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_UNSPECIFIED\x10\x00\x12\x30\n,OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_AVG\x10\x01\x12\x30\n,OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_SUM\x10\x02\x12\x30\n,OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_MIN\x10\x03\x12\x30\n,OUTPUT_CONFIGURATION_COLUMN_SUMMARY_TYPE_MAX\x10\x04*\xd6\x01\n\x1bInsightContextualActionType\x12.\n*INSIGHT_CONTEXTUAL_ACTION_TYPE_UNSPECIFIED\x10\x00\x12\'\n#INSIGHT_CONTEXTUAL_ACTION_TYPE_LINK\x10\x01\x12,\n(INSIGHT_CONTEXTUAL_ACTION_TYPE_COMPONENT\x10\x02\x12\x30\n,INSIGHT_CONTEXTUAL_ACTION_TYPE_DRILL_THROUGH\x10\x03*u\n\x0eQuoteCharacter\x12\x1f\n\x1bQUOTE_CHARACTER_UNSPECIFIED\x10\x00\x12 \n\x1cQUOTE_CHARACTER_DOUBLE_QUOTE\x10\x01\x12 \n\x1cQUOTE_CHARACTER_SINGLE_QUOTE\x10\x02\x42\x9f\x01\n\x19\x63om.api.v1alpha1.insightsB\x0cInsightProtoP\x01\xa2\x02\x03\x41VI\xaa\x02\x15\x41pi.V1alpha1.Insights\xca\x02\x15\x41pi\\V1alpha1\\Insights\xe2\x02!Api\\V1alpha1\\Insights\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Insightsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.insights.insight_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.api.v1alpha1.insightsB\014InsightProtoP\001\242\002\003AVI\252\002\025Api.V1alpha1.Insights\312\002\025Api\\V1alpha1\\Insights\342\002!Api\\V1alpha1\\Insights\\GPBMetadata\352\002\027Api::V1alpha1::Insights'
  _globals['_INSIGHT'].fields_by_name['insight_id']._loaded_options = None
  _globals['_INSIGHT'].fields_by_name['insight_id']._serialized_options = b'0\001'
  _globals['_DELETEINSIGHTREQUEST'].fields_by_name['insight_id']._loaded_options = None
  _globals['_DELETEINSIGHTREQUEST'].fields_by_name['insight_id']._serialized_options = b'0\001'
  _globals['_GETINSIGHTREQUEST'].fields_by_name['insight_id']._loaded_options = None
  _globals['_GETINSIGHTREQUEST'].fields_by_name['insight_id']._serialized_options = b'0\001'
  _globals['_LINKACTION_COMPONENTVALUEENTRY']._loaded_options = None
  _globals['_LINKACTION_COMPONENTVALUEENTRY']._serialized_options = b'8\001'
  _globals['_COMPONENTACTION_COMPONENTVALUEENTRY']._loaded_options = None
  _globals['_COMPONENTACTION_COMPONENTVALUEENTRY']._serialized_options = b'8\001'
  _globals['_OUTPUTCONFIGURATIONTYPE']._serialized_start=7869
  _globals['_OUTPUTCONFIGURATIONTYPE']._serialized_end=8185
  _globals['_OPERATIONTYPE']._serialized_start=8188
  _globals['_OPERATIONTYPE']._serialized_end=8540
  _globals['_COLUMNSORT']._serialized_start=8542
  _globals['_COLUMNSORT']._serialized_end=8638
  _globals['_OUTPUTCONFIGURATIONCOLUMNSUMMARYTYPE']._serialized_start=8641
  _globals['_OUTPUTCONFIGURATIONCOLUMNSUMMARYTYPE']._serialized_end=8937
  _globals['_INSIGHTCONTEXTUALACTIONTYPE']._serialized_start=8940
  _globals['_INSIGHTCONTEXTUALACTIONTYPE']._serialized_end=9154
  _globals['_QUOTECHARACTER']._serialized_start=9156
  _globals['_QUOTECHARACTER']._serialized_end=9273
  _globals['_INSIGHT']._serialized_start=241
  _globals['_INSIGHT']._serialized_end=954
  _globals['_PUBLISHINSIGHTREQUEST']._serialized_start=956
  _globals['_PUBLISHINSIGHTREQUEST']._serialized_end=1068
  _globals['_PUBLISHINSIGHTRESPONSE']._serialized_start=1070
  _globals['_PUBLISHINSIGHTRESPONSE']._serialized_end=1152
  _globals['_CREATEINSIGHTREQUEST']._serialized_start=1154
  _globals['_CREATEINSIGHTREQUEST']._serialized_end=1234
  _globals['_CREATEINSIGHTRESPONSE']._serialized_start=1236
  _globals['_CREATEINSIGHTRESPONSE']._serialized_end=1317
  _globals['_LISTINSIGHTSREQUEST']._serialized_start=1319
  _globals['_LISTINSIGHTSREQUEST']._serialized_end=1434
  _globals['_LISTINSIGHTSSTREAMRESPONSE']._serialized_start=1436
  _globals['_LISTINSIGHTSSTREAMRESPONSE']._serialized_end=1524
  _globals['_LISTINSIGHTSRESPONSE']._serialized_start=1526
  _globals['_LISTINSIGHTSRESPONSE']._serialized_end=1608
  _globals['_LISTORGINSIGHTSREQUEST']._serialized_start=1610
  _globals['_LISTORGINSIGHTSREQUEST']._serialized_end=1657
  _globals['_LISTORGINSIGHTSRESPONSE']._serialized_start=1659
  _globals['_LISTORGINSIGHTSRESPONSE']._serialized_end=1744
  _globals['_UPDATEINSIGHTREQUEST']._serialized_start=1747
  _globals['_UPDATEINSIGHTREQUEST']._serialized_end=1888
  _globals['_UPDATEINSIGHTRESPONSE']._serialized_start=1890
  _globals['_UPDATEINSIGHTRESPONSE']._serialized_end=1971
  _globals['_DELETEINSIGHTREQUEST']._serialized_start=1973
  _globals['_DELETEINSIGHTREQUEST']._serialized_end=2063
  _globals['_DELETEINSIGHTRESPONSE']._serialized_start=2065
  _globals['_DELETEINSIGHTRESPONSE']._serialized_end=2146
  _globals['_GETINSIGHTREQUEST']._serialized_start=2148
  _globals['_GETINSIGHTREQUEST']._serialized_end=2235
  _globals['_GETINSIGHTRESPONSE']._serialized_start=2237
  _globals['_GETINSIGHTRESPONSE']._serialized_end=2315
  _globals['_GETVFSSCHEMAREQUEST']._serialized_start=2317
  _globals['_GETVFSSCHEMAREQUEST']._serialized_end=2369
  _globals['_GETVFSSCHEMARESPONSE']._serialized_start=2372
  _globals['_GETVFSSCHEMARESPONSE']._serialized_end=2699
  _globals['_GETVFSSCHEMARESPONSE_FIELD']._serialized_start=2544
  _globals['_GETVFSSCHEMARESPONSE_FIELD']._serialized_end=2699
  _globals['_LISTVFSESREQUEST']._serialized_start=2701
  _globals['_LISTVFSESREQUEST']._serialized_end=2719
  _globals['_LISTVFSESRESPONSE']._serialized_start=2721
  _globals['_LISTVFSESRESPONSE']._serialized_end=2766
  _globals['_LISTVFSSCHEMASREQUEST']._serialized_start=2768
  _globals['_LISTVFSSCHEMASREQUEST']._serialized_end=2791
  _globals['_LISTVFSSCHEMASRESPONSE']._serialized_start=2793
  _globals['_LISTVFSSCHEMASRESPONSE']._serialized_end=2895
  _globals['_TABLEVISUALIZATION']._serialized_start=2898
  _globals['_TABLEVISUALIZATION']._serialized_end=3149
  _globals['_CARDVISUALIZATION']._serialized_start=3151
  _globals['_CARDVISUALIZATION']._serialized_end=3237
  _globals['_TEXTVALUE']._serialized_start=3239
  _globals['_TEXTVALUE']._serialized_end=3325
  _globals['_TEXTVALUECONDITION']._serialized_start=3328
  _globals['_TEXTVALUECONDITION']._serialized_end=3689
  _globals['_TEXTVALUECONDITION_COLOR']._serialized_start=3622
  _globals['_TEXTVALUECONDITION_COLOR']._serialized_end=3689
  _globals['_TABLECOLUMNCONFIG']._serialized_start=3692
  _globals['_TABLECOLUMNCONFIG']._serialized_end=4231
  _globals['_FORMATSERIES']._serialized_start=4233
  _globals['_FORMATSERIES']._serialized_end=4282
  _globals['_PADOPERATION']._serialized_start=4284
  _globals['_PADOPERATION']._serialized_end=4389
  _globals['_COLUMNOPERATION']._serialized_start=4392
  _globals['_COLUMNOPERATION']._serialized_end=4692
  _globals['_INSIGHTCONTEXTUALACTION']._serialized_start=4695
  _globals['_INSIGHTCONTEXTUALACTION']._serialized_end=5013
  _globals['_LINKACTION']._serialized_start=5016
  _globals['_LINKACTION']._serialized_end=5228
  _globals['_LINKACTION_COMPONENTVALUEENTRY']._serialized_start=5163
  _globals['_LINKACTION_COMPONENTVALUEENTRY']._serialized_end=5228
  _globals['_COMPONENTACTION']._serialized_start=5231
  _globals['_COMPONENTACTION']._serialized_end=5455
  _globals['_COMPONENTACTION_COMPONENTVALUEENTRY']._serialized_start=5163
  _globals['_COMPONENTACTION_COMPONENTVALUEENTRY']._serialized_end=5228
  _globals['_DRILLTHROUGHACTION']._serialized_start=5458
  _globals['_DRILLTHROUGHACTION']._serialized_end=5630
  _globals['_DRILLTHROUGHPARAMETER']._serialized_start=5632
  _globals['_DRILLTHROUGHPARAMETER']._serialized_end=5727
  _globals['_OUTPUTCONFIGURATION']._serialized_start=5730
  _globals['_OUTPUTCONFIGURATION']._serialized_end=6370
  _globals['_CREATEOUTPUTCONFIGURATIONREQUEST']._serialized_start=6373
  _globals['_CREATEOUTPUTCONFIGURATIONREQUEST']._serialized_end=6502
  _globals['_CREATEOUTPUTCONFIGURATIONRESPONSE']._serialized_start=6505
  _globals['_CREATEOUTPUTCONFIGURATIONRESPONSE']._serialized_end=6635
  _globals['_LISTOUTPUTCONFIGURATIONSREQUEST']._serialized_start=6637
  _globals['_LISTOUTPUTCONFIGURATIONSREQUEST']._serialized_end=6718
  _globals['_LISTOUTPUTCONFIGURATIONSRESPONSE']._serialized_start=6721
  _globals['_LISTOUTPUTCONFIGURATIONSRESPONSE']._serialized_end=6852
  _globals['_UPDATEOUTPUTCONFIGURATIONREQUEST']._serialized_start=6855
  _globals['_UPDATEOUTPUTCONFIGURATIONREQUEST']._serialized_end=7045
  _globals['_UPDATEOUTPUTCONFIGURATIONRESPONSE']._serialized_start=7048
  _globals['_UPDATEOUTPUTCONFIGURATIONRESPONSE']._serialized_end=7178
  _globals['_DELETEOUTPUTCONFIGURATIONREQUEST']._serialized_start=7180
  _globals['_DELETEOUTPUTCONFIGURATIONREQUEST']._serialized_end=7247
  _globals['_DELETEOUTPUTCONFIGURATIONRESPONSE']._serialized_start=7249
  _globals['_DELETEOUTPUTCONFIGURATIONRESPONSE']._serialized_end=7284
  _globals['_GETOUTPUTCONFIGURATIONREQUEST']._serialized_start=7286
  _globals['_GETOUTPUTCONFIGURATIONREQUEST']._serialized_end=7350
  _globals['_GETOUTPUTCONFIGURATIONRESPONSE']._serialized_start=7352
  _globals['_GETOUTPUTCONFIGURATIONRESPONSE']._serialized_end=7479
  _globals['_SETDEFAULTOUTPUTCONFIGURATIONREQUEST']._serialized_start=7481
  _globals['_SETDEFAULTOUTPUTCONFIGURATIONREQUEST']._serialized_end=7600
  _globals['_SETDEFAULTOUTPUTCONFIGURATIONRESPONSE']._serialized_start=7602
  _globals['_SETDEFAULTOUTPUTCONFIGURATIONRESPONSE']._serialized_end=7641
  _globals['_GETDEFAULTOUTPUTCONFIGURATIONREQUEST']._serialized_start=7643
  _globals['_GETDEFAULTOUTPUTCONFIGURATIONREQUEST']._serialized_end=7729
  _globals['_GETDEFAULTOUTPUTCONFIGURATIONRESPONSE']._serialized_start=7732
  _globals['_GETDEFAULTOUTPUTCONFIGURATIONRESPONSE']._serialized_end=7866
# @@protoc_insertion_point(module_scope)
