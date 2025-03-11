# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/insights/insight_content.proto
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
    'api/v1alpha1/insights/insight_content.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+api/v1alpha1/insights/insight_content.proto\x12\x15\x61pi.v1alpha1.insights\"A\n\x08Pipeline\x12\x31\n\x05nodes\x18\x01 \x03(\x0b\x32\x1b.api.v1alpha1.insights.NodeR\x05nodes:\x02\x18\x01\"\xa6\x08\n\x04Node\x12\x17\n\x07node_id\x18\x01 \x01(\tR\x06nodeId\x12\x12\n\x04type\x18\x02 \x01(\tR\x04type\x12\x14\n\x05title\x18\x03 \x01(\tR\x05title\x12\x1b\n\tinput_ids\x18\x04 \x03(\tR\x08inputIds\x12\x1d\n\noutput_ids\x18\x05 \x03(\tR\toutputIds\x12>\n\tfrom_node\x18\x06 \x01(\x0b\x32\x1f.api.v1alpha1.insights.FromNodeH\x00R\x08\x66romNode\x12\x44\n\x0b\x66ilter_node\x18\x07 \x01(\x0b\x32!.api.v1alpha1.insights.FilterNodeH\x00R\nfilterNode\x12\x44\n\x0b\x64\x65rive_node\x18\x08 \x01(\x0b\x32!.api.v1alpha1.insights.DeriveNodeH\x00R\nderiveNode\x12\x41\n\ngroup_node\x18\t \x01(\x0b\x32 .api.v1alpha1.insights.GroupNodeH\x00R\tgroupNode\x12>\n\tjoin_node\x18\n \x01(\x0b\x32\x1f.api.v1alpha1.insights.JoinNodeH\x00R\x08joinNode\x12\x44\n\x0bselect_node\x18\x0b \x01(\x0b\x32!.api.v1alpha1.insights.SelectNodeH\x00R\nselectNode\x12M\n\x0e\x61ggregate_node\x18\x0c \x01(\x0b\x32$.api.v1alpha1.insights.AggregateNodeH\x00R\raggregateNode\x12>\n\ttake_node\x18\r \x01(\x0b\x32\x1f.api.v1alpha1.insights.TakeNodeH\x00R\x08takeNode\x12>\n\tjson_node\x18\x0e \x01(\x0b\x32\x1f.api.v1alpha1.insights.JsonNodeH\x00R\x08jsonNode\x12;\n\x08map_node\x18\x0f \x01(\x0b\x32\x1e.api.v1alpha1.insights.MapNodeH\x00R\x07mapNode\x12G\n\x0creplace_node\x18\x10 \x01(\x0b\x32\".api.v1alpha1.insights.ReplaceNodeH\x00R\x0breplaceNode\x12>\n\tsort_node\x18\x11 \x01(\x0b\x32\x1f.api.v1alpha1.insights.SortNodeH\x00R\x08sortNode\x12i\n\x18string_manipulation_node\x18\x12 \x01(\x0b\x32-.api.v1alpha1.insights.StringManipulationNodeH\x00R\x16stringManipulationNode:\x02\x18\x01\x42\x06\n\x04\x62ody\"(\n\x08\x46romNode\x12\x18\n\x07\x64\x61taset\x18\x01 \x01(\tR\x07\x64\x61taset:\x02\x18\x01\"W\n\nFilterNode\x12\x45\n\nexpression\x18\x03 \x01(\x0b\x32%.api.v1alpha1.insights.ExpressionNodeR\nexpression:\x02\x18\x01\"x\n\nDeriveNode\x12\x1f\n\x0b\x63olumn_name\x18\x03 \x01(\tR\ncolumnName\x12\x45\n\nexpression\x18\x04 \x01(\x0b\x32%.api.v1alpha1.insights.ExpressionNodeR\nexpression:\x02\x18\x01\"\x94\x01\n\tGroupNode\x12(\n\x10group_by_columns\x18\x01 \x03(\tR\x0egroupByColumns\x12Y\n\x13\x61ggregation_columns\x18\x02 \x03(\x0b\x32(.api.v1alpha1.insights.AggregationColumnR\x12\x61ggregationColumns:\x02\x18\x01\"$\n\x08TakeNode\x12\x14\n\x05limit\x18\x01 \x01(\x05R\x05limit:\x02\x18\x01\"n\n\rAggregateNode\x12Y\n\x13\x61ggregation_columns\x18\x02 \x03(\x0b\x32(.api.v1alpha1.insights.AggregationColumnR\x12\x61ggregationColumns:\x02\x18\x01\"\xb8\x01\n\x11\x41ggregationColumn\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12(\n\x10group_by_columns\x18\x02 \x03(\tR\x0egroupByColumns\x12.\n\x13\x63olumn_to_aggregate\x18\x03 \x01(\tR\x11\x63olumnToAggregate\x12\x31\n\x14\x61ggregation_function\x18\x04 \x01(\tR\x13\x61ggregationFunction:\x02\x18\x01\";\n\x06\x43olumn\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x1b\n\tdata_type\x18\x02 \x01(\tR\x08\x64\x61taType:\x02\x18\x01\"\x81\x01\n\x0e\x45xpressionNode\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x41\n\x08\x63hildren\x18\x03 \x03(\x0b\x32%.api.v1alpha1.insights.ExpressionNodeR\x08\x63hildren:\x02\x18\x01\"\xcd\x03\n\x07MapNode\x12<\n\nnew_column\x18\x01 \x01(\x0b\x32\x1d.api.v1alpha1.insights.ColumnR\tnewColumn\x12\x41\n\rcolumn_to_map\x18\x02 \x01(\x0b\x32\x1d.api.v1alpha1.insights.ColumnR\x0b\x63olumnToMap\x12\x42\n\x08mappings\x18\x03 \x03(\x0b\x32&.api.v1alpha1.insights.MapNode.MappingR\x08mappings\x12J\n\rdefault_value\x18\x04 \x01(\x0b\x32%.api.v1alpha1.insights.ExpressionNodeR\x0c\x64\x65\x66\x61ultValue\x12\x1d\n\nis_complex\x18\x05 \x01(\x08R\tisComplex\x1a\x8d\x01\n\x07Mapping\x12\x43\n\tcondition\x18\x01 \x01(\x0b\x32%.api.v1alpha1.insights.ExpressionNodeR\tcondition\x12=\n\x06result\x18\x02 \x01(\x0b\x32%.api.v1alpha1.insights.ExpressionNodeR\x06result:\x02\x18\x01\"\xee\x01\n\x08JoinNode\x12\x12\n\x04side\x18\x01 \x01(\tR\x04side\x12\x44\n\x0cjoin_columns\x18\x02 \x03(\x0b\x32!.api.v1alpha1.insights.JoinColumnR\x0bjoinColumns\x12@\n\x0c\x66irst_parent\x18\x03 \x01(\x0b\x32\x1d.api.v1alpha1.insights.ParentR\x0b\x66irstParent\x12\x42\n\rsecond_parent\x18\x04 \x01(\x0b\x32\x1d.api.v1alpha1.insights.ParentR\x0csecondParent:\x02\x18\x01\"r\n\nJoinColumn\x12.\n\x13\x66irst_parent_column\x18\x01 \x01(\tR\x11\x66irstParentColumn\x12\x30\n\x14second_parent_column\x18\x02 \x01(\tR\x12secondParentColumn:\x02\x18\x01\"\xde\x01\n\x06Parent\x12\x1b\n\tparent_id\x18\x01 \x01(\tR\x08parentId\x12\x14\n\x05title\x18\x02 \x01(\tR\x05title\x12Z\n\x0frenamed_columns\x18\x03 \x03(\x0b\x32\x31.api.v1alpha1.insights.Parent.RenamedColumnsEntryR\x0erenamedColumns\x1a\x41\n\x13RenamedColumnsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:\x02\x18\x01\"\xcd\x01\n\nSelectNode\x12\x18\n\x07\x63olumns\x18\x01 \x03(\tR\x07\x63olumns\x12^\n\x0frenamed_columns\x18\x02 \x03(\x0b\x32\x35.api.v1alpha1.insights.SelectNode.RenamedColumnsEntryR\x0erenamedColumns\x1a\x41\n\x13RenamedColumnsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01:\x02\x18\x01\"q\n\nJsonTarget\x12\x1d\n\npath_parts\x18\x01 \x03(\tR\tpathParts\x12\x1f\n\x0b\x63olumn_name\x18\x02 \x01(\tR\ncolumnName\x12\x1f\n\x0bresult_type\x18\x03 \x01(\tR\nresultType:\x02\x18\x01\"\xe1\x01\n\x08JsonNode\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x1f\n\x0bjson_column\x18\x02 \x01(\tR\njsonColumn\x12;\n\x07targets\x18\x03 \x03(\x0b\x32!.api.v1alpha1.insights.JsonTargetR\x07targets\x12_\n\x16unnest_to_columns_node\x18\x04 \x01(\x0b\x32*.api.v1alpha1.insights.UnnestToColumnsNodeR\x13unnestToColumnsNode:\x02\x18\x01\"\xe8\x02\n\x13UnnestToColumnsNode\x12\x46\n\runnest_target\x18\x01 \x01(\x0b\x32!.api.v1alpha1.insights.JsonTargetR\x0cunnestTarget\x12@\n\nkey_target\x18\x02 \x01(\x0b\x32!.api.v1alpha1.insights.JsonTargetR\tkeyTarget\x12\x44\n\x0cvalue_target\x18\x03 \x01(\x0b\x32!.api.v1alpha1.insights.JsonTargetR\x0bvalueTarget\x12\x18\n\x07\x63olumns\x18\x04 \x03(\tR\x07\x63olumns\x12!\n\x0cprimary_keys\x18\x05 \x03(\tR\x0bprimaryKeys\x12@\n\x0cjson_columns\x18\x06 \x03(\x0b\x32\x1d.api.v1alpha1.insights.ColumnR\x0bjsonColumns:\x02\x18\x01\"\x93\x02\n\nParameters\x12Q\n\nparameters\x18\x01 \x03(\x0b\x32\x31.api.v1alpha1.insights.Parameters.ParametersEntryR\nparameters\x1a\x42\n\tParameter\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x1b\n\tdata_type\x18\x03 \x01(\tR\x08\x64\x61taType:\x02\x18\x01\x1aj\n\x0fParametersEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x41\n\x05value\x18\x02 \x01(\x0b\x32+.api.v1alpha1.insights.Parameters.ParameterR\x05value:\x02\x38\x01:\x02\x18\x01\"\xb8\x01\n\x11ValuesReplacement\x12!\n\x0ctarget_value\x18\x01 \x01(\tR\x0btargetValue\x12(\n\x10target_data_type\x18\x02 \x01(\tR\x0etargetDataType\x12R\n\x11replacement_value\x18\x03 \x01(\x0b\x32%.api.v1alpha1.insights.ExpressionNodeR\x10replacementValue:\x02\x18\x01\"\x95\x01\n\x11\x43olumnReplacement\x12!\n\x0c\x63olumn_names\x18\x01 \x03(\tR\x0b\x63olumnNames\x12Y\n\x13values_replacements\x18\x02 \x03(\x0b\x32(.api.v1alpha1.insights.ValuesReplacementR\x12valuesReplacements:\x02\x18\x01\"\x8b\x01\n\x0bReplaceNode\x12Y\n\x13\x63olumn_replacements\x18\x01 \x03(\x0b\x32(.api.v1alpha1.insights.ColumnReplacementR\x12\x63olumnReplacements\x12\x1d\n\nis_complex\x18\x02 \x01(\x08R\tisComplex:\x02\x18\x01\"O\n\nSortColumn\x12\x1f\n\x0b\x63olumn_name\x18\x01 \x01(\tR\ncolumnName\x12\x1c\n\tascending\x18\x02 \x01(\x08R\tascending:\x02\x18\x01\"T\n\x08SortNode\x12\x44\n\x0csort_columns\x18\x01 \x03(\x0b\x32!.api.v1alpha1.insights.SortColumnR\x0bsortColumns:\x02\x18\x01\"\x93\x01\n\x17StringManipulationSplit\x12\x19\n\x08split_by\x18\x02 \x01(\tR\x07splitBy\x12.\n\x13is_index_extraction\x18\x03 \x01(\x08R\x11isIndexExtraction\x12)\n\x10index_extraction\x18\x04 \x01(\x05R\x0findexExtraction:\x02\x18\x01\"M\n\x19StringManipulationReplace\x12\x16\n\x06target\x18\x01 \x01(\tR\x06target\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x18\x01\"\xea\x02\n\x16StringManipulationNode\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12,\n\x12source_column_name\x18\x02 \x01(\tR\x10sourceColumnName\x12,\n\x12target_column_name\x18\x03 \x01(\tR\x10targetColumnName\x12j\n\x19string_manipulation_split\x18\x04 \x01(\x0b\x32..api.v1alpha1.insights.StringManipulationSplitR\x17stringManipulationSplit\x12p\n\x1bstring_manipulation_replace\x18\x05 \x01(\x0b\x32\x30.api.v1alpha1.insights.StringManipulationReplaceR\x19stringManipulationReplace:\x02\x18\x01\x42\xa6\x01\n\x19\x63om.api.v1alpha1.insightsB\x13InsightContentProtoP\x01\xa2\x02\x03\x41VI\xaa\x02\x15\x41pi.V1alpha1.Insights\xca\x02\x15\x41pi\\V1alpha1\\Insights\xe2\x02!Api\\V1alpha1\\Insights\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Insightsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.insights.insight_content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.api.v1alpha1.insightsB\023InsightContentProtoP\001\242\002\003AVI\252\002\025Api.V1alpha1.Insights\312\002\025Api\\V1alpha1\\Insights\342\002!Api\\V1alpha1\\Insights\\GPBMetadata\352\002\027Api::V1alpha1::Insights'
  _globals['_PIPELINE']._loaded_options = None
  _globals['_PIPELINE']._serialized_options = b'\030\001'
  _globals['_NODE']._loaded_options = None
  _globals['_NODE']._serialized_options = b'\030\001'
  _globals['_FROMNODE']._loaded_options = None
  _globals['_FROMNODE']._serialized_options = b'\030\001'
  _globals['_FILTERNODE']._loaded_options = None
  _globals['_FILTERNODE']._serialized_options = b'\030\001'
  _globals['_DERIVENODE']._loaded_options = None
  _globals['_DERIVENODE']._serialized_options = b'\030\001'
  _globals['_GROUPNODE']._loaded_options = None
  _globals['_GROUPNODE']._serialized_options = b'\030\001'
  _globals['_TAKENODE']._loaded_options = None
  _globals['_TAKENODE']._serialized_options = b'\030\001'
  _globals['_AGGREGATENODE']._loaded_options = None
  _globals['_AGGREGATENODE']._serialized_options = b'\030\001'
  _globals['_AGGREGATIONCOLUMN']._loaded_options = None
  _globals['_AGGREGATIONCOLUMN']._serialized_options = b'\030\001'
  _globals['_COLUMN']._loaded_options = None
  _globals['_COLUMN']._serialized_options = b'\030\001'
  _globals['_EXPRESSIONNODE']._loaded_options = None
  _globals['_EXPRESSIONNODE']._serialized_options = b'\030\001'
  _globals['_MAPNODE']._loaded_options = None
  _globals['_MAPNODE']._serialized_options = b'\030\001'
  _globals['_JOINNODE']._loaded_options = None
  _globals['_JOINNODE']._serialized_options = b'\030\001'
  _globals['_JOINCOLUMN']._loaded_options = None
  _globals['_JOINCOLUMN']._serialized_options = b'\030\001'
  _globals['_PARENT_RENAMEDCOLUMNSENTRY']._loaded_options = None
  _globals['_PARENT_RENAMEDCOLUMNSENTRY']._serialized_options = b'8\001'
  _globals['_PARENT']._loaded_options = None
  _globals['_PARENT']._serialized_options = b'\030\001'
  _globals['_SELECTNODE_RENAMEDCOLUMNSENTRY']._loaded_options = None
  _globals['_SELECTNODE_RENAMEDCOLUMNSENTRY']._serialized_options = b'8\001'
  _globals['_SELECTNODE']._loaded_options = None
  _globals['_SELECTNODE']._serialized_options = b'\030\001'
  _globals['_JSONTARGET']._loaded_options = None
  _globals['_JSONTARGET']._serialized_options = b'\030\001'
  _globals['_JSONNODE']._loaded_options = None
  _globals['_JSONNODE']._serialized_options = b'\030\001'
  _globals['_UNNESTTOCOLUMNSNODE']._loaded_options = None
  _globals['_UNNESTTOCOLUMNSNODE']._serialized_options = b'\030\001'
  _globals['_PARAMETERS_PARAMETER']._loaded_options = None
  _globals['_PARAMETERS_PARAMETER']._serialized_options = b'\030\001'
  _globals['_PARAMETERS_PARAMETERSENTRY']._loaded_options = None
  _globals['_PARAMETERS_PARAMETERSENTRY']._serialized_options = b'8\001'
  _globals['_PARAMETERS']._loaded_options = None
  _globals['_PARAMETERS']._serialized_options = b'\030\001'
  _globals['_VALUESREPLACEMENT']._loaded_options = None
  _globals['_VALUESREPLACEMENT']._serialized_options = b'\030\001'
  _globals['_COLUMNREPLACEMENT']._loaded_options = None
  _globals['_COLUMNREPLACEMENT']._serialized_options = b'\030\001'
  _globals['_REPLACENODE']._loaded_options = None
  _globals['_REPLACENODE']._serialized_options = b'\030\001'
  _globals['_SORTCOLUMN']._loaded_options = None
  _globals['_SORTCOLUMN']._serialized_options = b'\030\001'
  _globals['_SORTNODE']._loaded_options = None
  _globals['_SORTNODE']._serialized_options = b'\030\001'
  _globals['_STRINGMANIPULATIONSPLIT']._loaded_options = None
  _globals['_STRINGMANIPULATIONSPLIT']._serialized_options = b'\030\001'
  _globals['_STRINGMANIPULATIONREPLACE']._loaded_options = None
  _globals['_STRINGMANIPULATIONREPLACE']._serialized_options = b'\030\001'
  _globals['_STRINGMANIPULATIONNODE']._loaded_options = None
  _globals['_STRINGMANIPULATIONNODE']._serialized_options = b'\030\001'
  _globals['_PIPELINE']._serialized_start=70
  _globals['_PIPELINE']._serialized_end=135
  _globals['_NODE']._serialized_start=138
  _globals['_NODE']._serialized_end=1200
  _globals['_FROMNODE']._serialized_start=1202
  _globals['_FROMNODE']._serialized_end=1242
  _globals['_FILTERNODE']._serialized_start=1244
  _globals['_FILTERNODE']._serialized_end=1331
  _globals['_DERIVENODE']._serialized_start=1333
  _globals['_DERIVENODE']._serialized_end=1453
  _globals['_GROUPNODE']._serialized_start=1456
  _globals['_GROUPNODE']._serialized_end=1604
  _globals['_TAKENODE']._serialized_start=1606
  _globals['_TAKENODE']._serialized_end=1642
  _globals['_AGGREGATENODE']._serialized_start=1644
  _globals['_AGGREGATENODE']._serialized_end=1754
  _globals['_AGGREGATIONCOLUMN']._serialized_start=1757
  _globals['_AGGREGATIONCOLUMN']._serialized_end=1941
  _globals['_COLUMN']._serialized_start=1943
  _globals['_COLUMN']._serialized_end=2002
  _globals['_EXPRESSIONNODE']._serialized_start=2005
  _globals['_EXPRESSIONNODE']._serialized_end=2134
  _globals['_MAPNODE']._serialized_start=2137
  _globals['_MAPNODE']._serialized_end=2598
  _globals['_MAPNODE_MAPPING']._serialized_start=2453
  _globals['_MAPNODE_MAPPING']._serialized_end=2594
  _globals['_JOINNODE']._serialized_start=2601
  _globals['_JOINNODE']._serialized_end=2839
  _globals['_JOINCOLUMN']._serialized_start=2841
  _globals['_JOINCOLUMN']._serialized_end=2955
  _globals['_PARENT']._serialized_start=2958
  _globals['_PARENT']._serialized_end=3180
  _globals['_PARENT_RENAMEDCOLUMNSENTRY']._serialized_start=3111
  _globals['_PARENT_RENAMEDCOLUMNSENTRY']._serialized_end=3176
  _globals['_SELECTNODE']._serialized_start=3183
  _globals['_SELECTNODE']._serialized_end=3388
  _globals['_SELECTNODE_RENAMEDCOLUMNSENTRY']._serialized_start=3111
  _globals['_SELECTNODE_RENAMEDCOLUMNSENTRY']._serialized_end=3176
  _globals['_JSONTARGET']._serialized_start=3390
  _globals['_JSONTARGET']._serialized_end=3503
  _globals['_JSONNODE']._serialized_start=3506
  _globals['_JSONNODE']._serialized_end=3731
  _globals['_UNNESTTOCOLUMNSNODE']._serialized_start=3734
  _globals['_UNNESTTOCOLUMNSNODE']._serialized_end=4094
  _globals['_PARAMETERS']._serialized_start=4097
  _globals['_PARAMETERS']._serialized_end=4372
  _globals['_PARAMETERS_PARAMETER']._serialized_start=4194
  _globals['_PARAMETERS_PARAMETER']._serialized_end=4260
  _globals['_PARAMETERS_PARAMETERSENTRY']._serialized_start=4262
  _globals['_PARAMETERS_PARAMETERSENTRY']._serialized_end=4368
  _globals['_VALUESREPLACEMENT']._serialized_start=4375
  _globals['_VALUESREPLACEMENT']._serialized_end=4559
  _globals['_COLUMNREPLACEMENT']._serialized_start=4562
  _globals['_COLUMNREPLACEMENT']._serialized_end=4711
  _globals['_REPLACENODE']._serialized_start=4714
  _globals['_REPLACENODE']._serialized_end=4853
  _globals['_SORTCOLUMN']._serialized_start=4855
  _globals['_SORTCOLUMN']._serialized_end=4934
  _globals['_SORTNODE']._serialized_start=4936
  _globals['_SORTNODE']._serialized_end=5020
  _globals['_STRINGMANIPULATIONSPLIT']._serialized_start=5023
  _globals['_STRINGMANIPULATIONSPLIT']._serialized_end=5170
  _globals['_STRINGMANIPULATIONREPLACE']._serialized_start=5172
  _globals['_STRINGMANIPULATIONREPLACE']._serialized_end=5249
  _globals['_STRINGMANIPULATIONNODE']._serialized_start=5252
  _globals['_STRINGMANIPULATIONNODE']._serialized_end=5614
# @@protoc_insertion_point(module_scope)
