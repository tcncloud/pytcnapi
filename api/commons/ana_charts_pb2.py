# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/ana_charts.proto
# Protobuf Python Version: 6.30.1
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
    1,
    '',
    'api/commons/ana_charts.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/commons/ana_charts.proto\x12\x0b\x61pi.commons*V\n\x13\x42\x61rChartOrientation\x12\x1d\n\x19\x42\x41R_CHART_ORIENTATION_BAR\x10\x00\x12 \n\x1c\x42\x41R_CHART_ORIENTATION_COLUMN\x10\x01*T\n\x10\x43hartOrientation\x12 \n\x1c\x43HART_ORIENTATION_HORIZONTAL\x10\x00\x12\x1e\n\x1a\x43HART_ORIENTATION_VERTICAL\x10\x01*O\n\x0f\x41reaChartChoice\x12\x1a\n\x16\x41REA_CHART_CHOICE_AREA\x10\x00\x12 \n\x1c\x41REA_CHART_CHOICE_AREASPLINE\x10\x01*|\n\rLineChartStep\x12\x18\n\x14LINE_CHART_STEP_LEFT\x10\x00\x12\x1a\n\x16LINE_CHART_STEP_CENTER\x10\x01\x12\x19\n\x15LINE_CHART_STEP_RIGHT\x10\x02\x12\x1a\n\x16LINE_CHART_STEP_NOLINE\x10\x03*U\n\x12\x43hartDisplayLabels\x12\x1e\n\x1a\x43HART_DISPLAY_LABELS_NEVER\x10\x00\x12\x1f\n\x1b\x43HART_DISPLAY_LABELS_ALWAYS\x10\x01*e\n\rThresholdType\x12\x19\n\x15THRESHOLD_TYPE_STATIC\x10\x00\x12\x1d\n\x19THRESHOLD_TYPE_DATA_POINT\x10\x01\x12\x1a\n\x16THRESHOLD_TYPE_NOT_SET\x10\x02*U\n\x12PackedBubbleChoice\x12\x1f\n\x1bPACKED_BUBBLE_CHOICE_PACKED\x10\x00\x12\x1e\n\x1aPACKED_BUBBLE_CHOICE_SPLIT\x10\x01*g\n\rSuffixChoices\x12\x1b\n\x17SUFFIX_CHOICES_NOSUFFIX\x10\x00\x12\x1a\n\x16SUFFIX_CHOICES_DOLLARS\x10\x01\x12\x1d\n\x19SUFFIX_CHOICES_PERCENTAGE\x10\x02\x42n\n\x0f\x63om.api.commonsB\x0e\x41naChartsProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.ana_charts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\016AnaChartsProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_BARCHARTORIENTATION']._serialized_start=45
  _globals['_BARCHARTORIENTATION']._serialized_end=131
  _globals['_CHARTORIENTATION']._serialized_start=133
  _globals['_CHARTORIENTATION']._serialized_end=217
  _globals['_AREACHARTCHOICE']._serialized_start=219
  _globals['_AREACHARTCHOICE']._serialized_end=298
  _globals['_LINECHARTSTEP']._serialized_start=300
  _globals['_LINECHARTSTEP']._serialized_end=424
  _globals['_CHARTDISPLAYLABELS']._serialized_start=426
  _globals['_CHARTDISPLAYLABELS']._serialized_end=511
  _globals['_THRESHOLDTYPE']._serialized_start=513
  _globals['_THRESHOLDTYPE']._serialized_end=614
  _globals['_PACKEDBUBBLECHOICE']._serialized_start=616
  _globals['_PACKEDBUBBLECHOICE']._serialized_end=701
  _globals['_SUFFIXCHOICES']._serialized_start=703
  _globals['_SUFFIXCHOICES']._serialized_end=806
# @@protoc_insertion_point(module_scope)
