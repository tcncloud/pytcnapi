# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/bireportgenerator.proto
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
    'api/commons/bireportgenerator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import enums_pb2 as api_dot_commons_dot_enums__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/commons/bireportgenerator.proto\x12\x0b\x61pi.commons\x1a\x17\x61pi/commons/enums.proto\"\x83\x01\n\rDeliveryTimes\x12%\n\x0e\x64\x65livery_times\x18\x02 \x03(\x05R\rdeliveryTimes\x12G\n\x10repeat_frequency\x18\x03 \x01(\x0e\x32\x1c.api.commons.RepeatFrequencyR\x0frepeatFrequency:\x02\x18\x01\"|\n\x0f\x44\x61yOfWeekFilter\x12=\n\rdays_of_weeks\x18\x01 \x03(\x0e\x32\x19.api.commons.Weekday.EnumR\x0b\x64\x61ysOfWeeks\x12&\n\x0fweeks_of_months\x18\x02 \x03(\x05R\rweeksOfMonths:\x02\x18\x01\"j\n\x10\x44\x61yOfMonthFilter\x12\"\n\rday_of_months\x18\x01 \x03(\x05R\x0b\x64\x61yOfMonths\x12.\n\x14is_last_day_of_month\x18\x02 \x01(\x08R\x10isLastDayOfMonth:\x02\x18\x01\"\xe6\x01\n\tDayFilter\x12.\n\x04type\x18\x01 \x01(\x0e\x32\x1a.api.commons.DayFilterTypeR\x04type\x12K\n\x12\x64\x61y_of_week_filter\x18\x02 \x01(\x0b\x32\x1c.api.commons.DayOfWeekFilterH\x00R\x0f\x64\x61yOfWeekFilter\x12N\n\x13\x64\x61y_of_month_filter\x18\x03 \x01(\x0b\x32\x1d.api.commons.DayOfMonthFilterH\x00R\x10\x64\x61yOfMonthFilter:\x02\x18\x01\x42\x08\n\x06\x66ilter\"z\n\rFormatOptions\x12>\n\rreport_format\x18\x01 \x01(\x0e\x32\x19.api.commons.ReportFormatR\x0creportFormat\x12%\n\x0e\x66ilename_parts\x18\x02 \x03(\tR\rfilenameParts:\x02\x18\x01\"\x89\x01\n\x0f\x44\x65liveryOptions\x12.\n\x13transfer_config_sid\x18\x01 \x01(\x03R\x11transferConfigSid\x12\x42\n\x1b\x66\x61ilure_notification_emails\x18\x02 \x03(\tB\x02\x18\x01R\x19\x66\x61ilureNotificationEmails:\x02\x18\x01\"\x81\x01\n\x0c\x46ilenamePart\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32\x1d.api.commons.FilenamePartTypeR\x04type\x12\x1f\n\x0bstatic_text\x18\x02 \x01(\tR\nstaticText\x12\x1d\n\ndate_parts\x18\x03 \x03(\tR\tdateParts\"\x83\x01\n\x0fTransferOptions\x12.\n\x13transfer_config_sid\x18\x01 \x01(\tR\x11transferConfigSid\x12@\n\x0e\x66ilename_parts\x18\x02 \x03(\x0b\x32\x19.api.commons.FilenamePartR\rfilenameParts*\x97\x01\n\x0fRepeatFrequency\x12 \n\x1cREPEAT_FREQUENCY_UNSPECIFIED\x10\x00\x12\x1c\n\x18REPEAT_FREQUENCY_ON_HOUR\x10\x01\x12\x1f\n\x1bREPEAT_FREQUENCY_15_MINUTES\x10\x02\x12\x1f\n\x1bREPEAT_FREQUENCY_30_MINUTES\x10\x03\x1a\x02\x18\x01*\x96\x01\n\rDayFilterType\x12\x1f\n\x1b\x44\x41Y_FILTER_TYPE_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x44\x41Y_FILTER_TYPE_EVERY_DAY\x10\x01\x12\x1f\n\x1b\x44\x41Y_FILTER_TYPE_DAY_OF_WEEK\x10\x02\x12 \n\x1c\x44\x41Y_FILTER_TYPE_DAY_OF_MONTH\x10\x03\x1a\x02\x18\x01*H\n\x0cReportFormat\x12\x1d\n\x19REPORT_FORMAT_UNSPECIFIED\x10\x00\x12\x15\n\x11REPORT_FORMAT_CSV\x10\x01\x1a\x02\x18\x01*\xac\x08\n\nTimePeriod\x12\x1b\n\x17TIME_PERIOD_UNSPECIFIED\x10\x00\x12\x15\n\x11TIME_PERIOD_TODAY\x10\x01\x12\x19\n\x15TIME_PERIOD_THIS_WEEK\x10\x02\x12\x1a\n\x16TIME_PERIOD_THIS_MONTH\x10\x03\x12\x19\n\x15TIME_PERIOD_THIS_YEAR\x10\x04\x12\x1e\n\x1aTIME_PERIOD_THE_DAY_SO_FAR\x10\x05\x12\x1c\n\x18TIME_PERIOD_WEEK_TO_DATE\x10\x06\x12\x1d\n\x19TIME_PERIOD_MONTH_TO_DATE\x10\x07\x12\x1c\n\x18TIME_PERIOD_YEAR_TO_DATE\x10\x08\x12\x19\n\x15TIME_PERIOD_YESTERDAY\x10\t\x12$\n TIME_PERIOD_DAY_BEFORE_YESTERDAY\x10\n\x12\"\n\x1eTIME_PERIOD_THIS_DAY_LAST_WEEK\x10\x0b\x12\x1d\n\x19TIME_PERIOD_PREVIOUS_WEEK\x10\x0c\x12\x1e\n\x1aTIME_PERIOD_PREVIOUS_MONTH\x10\r\x12\x1d\n\x19TIME_PERIOD_PREVIOUS_YEAR\x10\x0e\x12\x1f\n\x1bTIME_PERIOD_LAST_15_MINUTES\x10\x0f\x12\x1f\n\x1bTIME_PERIOD_LAST_30_MINUTES\x10\x10\x12\x1b\n\x17TIME_PERIOD_LAST_1_HOUR\x10\x11\x12\x1c\n\x18TIME_PERIOD_LAST_2_HOURS\x10\x12\x12\x1c\n\x18TIME_PERIOD_LAST_3_HOURS\x10\x13\x12\x1c\n\x18TIME_PERIOD_LAST_4_HOURS\x10\x14\x12\x1c\n\x18TIME_PERIOD_LAST_6_HOURS\x10\x15\x12\x1d\n\x19TIME_PERIOD_LAST_12_HOURS\x10\x16\x12\x1d\n\x19TIME_PERIOD_LAST_24_HOURS\x10\x17\x12\x1b\n\x17TIME_PERIOD_LAST_2_DAYS\x10\x18\x12\x1b\n\x17TIME_PERIOD_LAST_3_DAYS\x10\x19\x12\x1b\n\x17TIME_PERIOD_LAST_7_DAYS\x10\x1a\x12\x1c\n\x18TIME_PERIOD_LAST_2_WEEKS\x10\x1b\x12\x1c\n\x18TIME_PERIOD_LAST_30_DAYS\x10\x1c\x12\x1c\n\x18TIME_PERIOD_LAST_60_DAYS\x10\x1d\x12\x1c\n\x18TIME_PERIOD_LAST_90_DAYS\x10\x1e\x12\x1d\n\x19TIME_PERIOD_LAST_6_MONTHS\x10\x1f\x12\x1b\n\x17TIME_PERIOD_LAST_1_YEAR\x10 \x12\x1c\n\x18TIME_PERIOD_LAST_2_YEARS\x10!\x12\x1c\n\x18TIME_PERIOD_LAST_5_YEARS\x10\"*\xec\x02\n\x10\x46ilenamePartType\x12\"\n\x1e\x46ILENAME_PART_TYPE_UNSPECIFIED\x10\x00\x12%\n!FILENAME_PART_TYPE_DASHBOARD_NAME\x10\x01\x12\x1f\n\x1b\x46ILENAME_PART_TYPE_JOB_NAME\x10\x02\x12#\n\x1f\x46ILENAME_PART_TYPE_INSIGHT_NAME\x10\x03\x12,\n(FILENAME_PART_TYPE_DATE_TIME_FILTER_TEXT\x10\x04\x12&\n\"FILENAME_PART_TYPE_START_DATE_TIME\x10\x05\x12$\n FILENAME_PART_TYPE_END_DATE_TIME\x10\x06\x12\'\n#FILENAME_PART_TYPE_REPORT_DATE_TIME\x10\x07\x12\"\n\x1e\x46ILENAME_PART_TYPE_STATIC_TEXT\x10\x08\x42v\n\x0f\x63om.api.commonsB\x16\x42ireportgeneratorProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.bireportgenerator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\026BireportgeneratorProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_REPEATFREQUENCY']._loaded_options = None
  _globals['_REPEATFREQUENCY']._serialized_options = b'\030\001'
  _globals['_DAYFILTERTYPE']._loaded_options = None
  _globals['_DAYFILTERTYPE']._serialized_options = b'\030\001'
  _globals['_REPORTFORMAT']._loaded_options = None
  _globals['_REPORTFORMAT']._serialized_options = b'\030\001'
  _globals['_DELIVERYTIMES']._loaded_options = None
  _globals['_DELIVERYTIMES']._serialized_options = b'\030\001'
  _globals['_DAYOFWEEKFILTER']._loaded_options = None
  _globals['_DAYOFWEEKFILTER']._serialized_options = b'\030\001'
  _globals['_DAYOFMONTHFILTER']._loaded_options = None
  _globals['_DAYOFMONTHFILTER']._serialized_options = b'\030\001'
  _globals['_DAYFILTER']._loaded_options = None
  _globals['_DAYFILTER']._serialized_options = b'\030\001'
  _globals['_FORMATOPTIONS']._loaded_options = None
  _globals['_FORMATOPTIONS']._serialized_options = b'\030\001'
  _globals['_DELIVERYOPTIONS'].fields_by_name['failure_notification_emails']._loaded_options = None
  _globals['_DELIVERYOPTIONS'].fields_by_name['failure_notification_emails']._serialized_options = b'\030\001'
  _globals['_DELIVERYOPTIONS']._loaded_options = None
  _globals['_DELIVERYOPTIONS']._serialized_options = b'\030\001'
  _globals['_REPEATFREQUENCY']._serialized_start=1209
  _globals['_REPEATFREQUENCY']._serialized_end=1360
  _globals['_DAYFILTERTYPE']._serialized_start=1363
  _globals['_DAYFILTERTYPE']._serialized_end=1513
  _globals['_REPORTFORMAT']._serialized_start=1515
  _globals['_REPORTFORMAT']._serialized_end=1587
  _globals['_TIMEPERIOD']._serialized_start=1590
  _globals['_TIMEPERIOD']._serialized_end=2658
  _globals['_FILENAMEPARTTYPE']._serialized_start=2661
  _globals['_FILENAMEPARTTYPE']._serialized_end=3025
  _globals['_DELIVERYTIMES']._serialized_start=78
  _globals['_DELIVERYTIMES']._serialized_end=209
  _globals['_DAYOFWEEKFILTER']._serialized_start=211
  _globals['_DAYOFWEEKFILTER']._serialized_end=335
  _globals['_DAYOFMONTHFILTER']._serialized_start=337
  _globals['_DAYOFMONTHFILTER']._serialized_end=443
  _globals['_DAYFILTER']._serialized_start=446
  _globals['_DAYFILTER']._serialized_end=676
  _globals['_FORMATOPTIONS']._serialized_start=678
  _globals['_FORMATOPTIONS']._serialized_end=800
  _globals['_DELIVERYOPTIONS']._serialized_start=803
  _globals['_DELIVERYOPTIONS']._serialized_end=940
  _globals['_FILENAMEPART']._serialized_start=943
  _globals['_FILENAMEPART']._serialized_end=1072
  _globals['_TRANSFEROPTIONS']._serialized_start=1075
  _globals['_TRANSFEROPTIONS']._serialized_end=1206
# @@protoc_insertion_point(module_scope)
