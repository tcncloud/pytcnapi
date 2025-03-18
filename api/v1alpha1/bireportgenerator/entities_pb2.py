# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/bireportgenerator/entities.proto
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
    'api/v1alpha1/bireportgenerator/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import bireportgenerator_pb2 as api_dot_commons_dot_bireportgenerator__pb2
from api.commons import enums_pb2 as api_dot_commons_dot_enums__pb2
from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from api.commons import types_pb2 as api_dot_commons_dot_types__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/v1alpha1/bireportgenerator/entities.proto\x12\x1e\x61pi.v1alpha1.bireportgenerator\x1a#api/commons/bireportgenerator.proto\x1a\x17\x61pi/commons/enums.proto\x1a\x15\x61pi/commons/org.proto\x1a\x17\x61pi/commons/types.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xdf\x07\n\tReportJob\x12\"\n\rreport_job_id\x18\x01 \x01(\tR\x0breportJobId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12%\n\x0c\x64\x61shboard_id\x18\x04 \x01(\tB\x02\x18\x01R\x0b\x64\x61shboardId\x12\x1f\n\ttime_zone\x18\x05 \x01(\tB\x02\x18\x01R\x08timeZone\x12\x38\n\x0btime_period\x18\x06 \x01(\x0e\x32\x17.api.commons.TimePeriodR\ntimePeriod\x12\x45\n\x0e\x64\x65livery_times\x18\x07 \x01(\x0b\x32\x1a.api.commons.DeliveryTimesB\x02\x18\x01R\rdeliveryTimes\x12\x39\n\nday_filter\x18\x08 \x01(\x0b\x32\x16.api.commons.DayFilterB\x02\x18\x01R\tdayFilter\x12.\n\x06months\x18\t \x03(\x0e\x32\x12.api.commons.MonthB\x02\x18\x01R\x06months\x12\x45\n\x0e\x66ormat_options\x18\n \x01(\x0b\x32\x1a.api.commons.FormatOptionsB\x02\x18\x01R\rformatOptions\x12K\n\x10\x64\x65livery_options\x18\x0b \x01(\x0b\x32\x1c.api.commons.DeliveryOptionsB\x02\x18\x01R\x0f\x64\x65liveryOptions\x12\x1b\n\tis_active\x18\x0c \x01(\x08R\x08isActive\x12*\n\x11send_empty_report\x18\r \x01(\x08R\x0fsendEmptyReport\x12\x32\n\x15\x64\x61shboard_resource_id\x18\x0e \x01(\tR\x13\x64\x61shboardResourceId\x12H\n\x11time_zone_wrapper\x18\x0f \x01(\x0b\x32\x1c.api.commons.TimeZoneWrapperR\x0ftimeZoneWrapper\x12&\n\x0fhide_csv_footer\x18\x10 \x01(\x08R\rhideCsvFooter\x12\x32\n\x13transfer_config_sid\x18\x11 \x01(\x03\x42\x02\x18\x01R\x11transferConfigSid\x12\x44\n\x0f\x63ron_expression\x18\x12 \x01(\x0b\x32\x1b.api.commons.CronExpressionR\x0e\x63ronExpression\x12G\n\x10transfer_options\x18\x13 \x01(\x0b\x32\x1c.api.commons.TransferOptionsR\x0ftransferOptions\"\xa2\t\n\tReportLog\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\"\n\rreport_log_id\x18\x02 \x01(\x03R\x0breportLogId\x12&\n\rreport_job_id\x18\x03 \x01(\x03\x42\x02\x30\x01R\x0breportJobId\x12!\n\x0c\x65xecution_id\x18\x04 \x01(\tR\x0b\x65xecutionId\x12\x1f\n\x0breport_name\x18\x05 \x01(\tR\nreportName\x12L\n\x12job_requested_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x10jobRequestedTime\x12L\n\x12job_completed_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x02\x18\x01R\x10jobCompletedTime\x12\x18\n\x07success\x18\x08 \x01(\x08R\x07success\x12)\n\x0e\x66\x61ilure_reason\x18\t \x01(\tB\x02\x18\x01R\rfailureReason\x12%\n\x0e\x61ttempt_number\x18\n \x01(\x03R\rattemptNumber\x12%\n\x0cmax_attempts\x18\x0b \x01(\x03\x42\x02\x18\x01R\x0bmaxAttempts\x12;\n\x0b\x63reate_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ncreateTime\x12;\n\x0bupdate_time\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nupdateTime\x12\'\n\x0f\x64\x61shboard_title\x18\x0e \x01(\tR\x0e\x64\x61shboardTitle\x12\x41\n\x0escheduled_time\x18\x0f \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rscheduledTime\x12L\n\x14\x65xecution_start_time\x18\x10 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x12\x65xecutionStartTime\x12H\n\x12\x65xecution_end_time\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x10\x65xecutionEndTime\x12\x46\n\x11report_start_date\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0freportStartDate\x12\x42\n\x0freport_end_date\x18\x13 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rreportEndDate\x12\x1a\n\x08\x63omments\x18\x14 \x03(\tR\x08\x63omments\x12\x1a\n\x08timezone\x18\x15 \x01(\tR\x08timezone\x12\x1c\n\tfilenames\x18\x16 \x03(\tR\tfilenames\x12#\n\rinsight_count\x18\x17 \x01(\x03R\x0cinsightCount\x12:\n\x19\x64\x65livery_definition_title\x18\x18 \x01(\tR\x17\x64\x65liveryDefinitionTitleB\xcd\x01\n\"com.api.v1alpha1.bireportgeneratorB\rEntitiesProtoP\x01\xa2\x02\x03\x41VB\xaa\x02\x1e\x41pi.V1alpha1.Bireportgenerator\xca\x02\x1e\x41pi\\V1alpha1\\Bireportgenerator\xe2\x02*Api\\V1alpha1\\Bireportgenerator\\GPBMetadata\xea\x02 Api::V1alpha1::Bireportgeneratorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.bireportgenerator.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.api.v1alpha1.bireportgeneratorB\rEntitiesProtoP\001\242\002\003AVB\252\002\036Api.V1alpha1.Bireportgenerator\312\002\036Api\\V1alpha1\\Bireportgenerator\342\002*Api\\V1alpha1\\Bireportgenerator\\GPBMetadata\352\002 Api::V1alpha1::Bireportgenerator'
  _globals['_REPORTJOB'].fields_by_name['dashboard_id']._loaded_options = None
  _globals['_REPORTJOB'].fields_by_name['dashboard_id']._serialized_options = b'\030\001'
  _globals['_REPORTJOB'].fields_by_name['time_zone']._loaded_options = None
  _globals['_REPORTJOB'].fields_by_name['time_zone']._serialized_options = b'\030\001'
  _globals['_REPORTJOB'].fields_by_name['delivery_times']._loaded_options = None
  _globals['_REPORTJOB'].fields_by_name['delivery_times']._serialized_options = b'\030\001'
  _globals['_REPORTJOB'].fields_by_name['day_filter']._loaded_options = None
  _globals['_REPORTJOB'].fields_by_name['day_filter']._serialized_options = b'\030\001'
  _globals['_REPORTJOB'].fields_by_name['months']._loaded_options = None
  _globals['_REPORTJOB'].fields_by_name['months']._serialized_options = b'\030\001'
  _globals['_REPORTJOB'].fields_by_name['format_options']._loaded_options = None
  _globals['_REPORTJOB'].fields_by_name['format_options']._serialized_options = b'\030\001'
  _globals['_REPORTJOB'].fields_by_name['delivery_options']._loaded_options = None
  _globals['_REPORTJOB'].fields_by_name['delivery_options']._serialized_options = b'\030\001'
  _globals['_REPORTJOB'].fields_by_name['transfer_config_sid']._loaded_options = None
  _globals['_REPORTJOB'].fields_by_name['transfer_config_sid']._serialized_options = b'\030\001'
  _globals['_REPORTLOG'].fields_by_name['report_job_id']._loaded_options = None
  _globals['_REPORTLOG'].fields_by_name['report_job_id']._serialized_options = b'0\001'
  _globals['_REPORTLOG'].fields_by_name['job_requested_time']._loaded_options = None
  _globals['_REPORTLOG'].fields_by_name['job_requested_time']._serialized_options = b'\030\001'
  _globals['_REPORTLOG'].fields_by_name['job_completed_time']._loaded_options = None
  _globals['_REPORTLOG'].fields_by_name['job_completed_time']._serialized_options = b'\030\001'
  _globals['_REPORTLOG'].fields_by_name['failure_reason']._loaded_options = None
  _globals['_REPORTLOG'].fields_by_name['failure_reason']._serialized_options = b'\030\001'
  _globals['_REPORTLOG'].fields_by_name['max_attempts']._loaded_options = None
  _globals['_REPORTLOG'].fields_by_name['max_attempts']._serialized_options = b'\030\001'
  _globals['_REPORTJOB']._serialized_start=225
  _globals['_REPORTJOB']._serialized_end=1216
  _globals['_REPORTLOG']._serialized_start=1219
  _globals['_REPORTLOG']._serialized_end=2405
# @@protoc_insertion_point(module_scope)
