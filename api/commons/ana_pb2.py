# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/ana.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/commons/ana.proto\x12\x0b\x61pi.commons*\xab\x0c\n\x0b\x41naTimeZone\x12\x19\n\x15\x41NA_TIME_ZONE_UNKNOWN\x10\x00\x12#\n\x1f\x41NA_TIME_ZONE_AMERICA_ANCHORAGE\x10\x01\x12!\n\x1d\x41NA_TIME_ZONE_AMERICA_CHICAGO\x10\x02\x12 \n\x1c\x41NA_TIME_ZONE_AMERICA_DENVER\x10\x03\x12&\n\"ANA_TIME_ZONE_AMERICA_INDIANAPOLIS\x10\x04\x12%\n!ANA_TIME_ZONE_AMERICA_LOS_ANGELES\x10\x05\x12%\n!ANA_TIME_ZONE_AMERICA_MEXICO_CITY\x10\x06\x12\"\n\x1e\x41NA_TIME_ZONE_AMERICA_NEW_YORK\x10\x07\x12!\n\x1d\x41NA_TIME_ZONE_AMERICA_PHOENIX\x10\x08\x12%\n!ANA_TIME_ZONE_AMERICA_PUERTO_RICO\x10\t\x12\x1f\n\x1b\x41NA_TIME_ZONE_ASIA_CALCUTTA\x10\n\x12\x1e\n\x1a\x41NA_TIME_ZONE_ASIA_COLOMBO\x10\x0b\x12\x1d\n\x19\x41NA_TIME_ZONE_ASIA_MANILA\x10\x0c\x12$\n ANA_TIME_ZONE_AUSTRALIA_ADELAIDE\x10\r\x12$\n ANA_TIME_ZONE_AUSTRALIA_BRISBANE\x10\x0e\x12\"\n\x1e\x41NA_TIME_ZONE_AUSTRALIA_DARWIN\x10\x0f\x12%\n!ANA_TIME_ZONE_AUSTRALIA_MELBOURNE\x10\x10\x12!\n\x1d\x41NA_TIME_ZONE_AUSTRALIA_PERTH\x10\x11\x12\"\n\x1e\x41NA_TIME_ZONE_AUSTRALIA_SYDNEY\x10\x12\x12\x1d\n\x19\x41NA_TIME_ZONE_BRAZIL_ACRE\x10\x13\x12\"\n\x1e\x41NA_TIME_ZONE_BRAZIL_DENORONHA\x10\x14\x12\x1d\n\x19\x41NA_TIME_ZONE_BRAZIL_EAST\x10\x15\x12\x1d\n\x19\x41NA_TIME_ZONE_BRAZIL_WEST\x10\x16\x12!\n\x1d\x41NA_TIME_ZONE_CANADA_ATLANTIC\x10\x17\x12 \n\x1c\x41NA_TIME_ZONE_CANADA_CENTRAL\x10\x18\x12*\n&ANA_TIME_ZONE_CANADA_EAST_SASKATCHEWAN\x10\x19\x12 \n\x1c\x41NA_TIME_ZONE_CANADA_EASTERN\x10\x1a\x12!\n\x1d\x41NA_TIME_ZONE_CANADA_MOUNTAIN\x10\x1b\x12%\n!ANA_TIME_ZONE_CANADA_NEWFOUNDLAND\x10\x1c\x12 \n\x1c\x41NA_TIME_ZONE_CANADA_PACIFIC\x10\x1d\x12%\n!ANA_TIME_ZONE_CANADA_SASKATCHEWAN\x10\x1e\x12\x1e\n\x1a\x41NA_TIME_ZONE_CANADA_YUKON\x10\x1f\x12\x1f\n\x1b\x41NA_TIME_ZONE_EUROPE_BERLIN\x10 \x12\"\n\x1e\x41NA_TIME_ZONE_EUROPE_BUCHAREST\x10!\x12\x1f\n\x1b\x41NA_TIME_ZONE_EUROPE_LONDON\x10\"\x12\x1f\n\x1b\x41NA_TIME_ZONE_EUROPE_MADRID\x10#\x12\x17\n\x13\x41NA_TIME_ZONE_JAPAN\x10$\x12\"\n\x1e\x41NA_TIME_ZONE_MEXICO_BAJANORTE\x10%\x12 \n\x1c\x41NA_TIME_ZONE_MEXICO_BAJASUR\x10&\x12\"\n\x1e\x41NA_TIME_ZONE_PACIFIC_AUCKLAND\x10\'\x12!\n\x1d\x41NA_TIME_ZONE_PACIFIC_CHATHAM\x10(\x12\"\n\x1e\x41NA_TIME_ZONE_PACIFIC_HONOLULU\x10)\x12\x1b\n\x17\x41NA_TIME_ZONE_SINGAPORE\x10*\x12\x1f\n\x1b\x41NA_TIME_ZONE_ETC_UNIVERSAL\x10+\x12\x1f\n\x1b\x41NA_TIME_ZONE_ETC_GREENWICH\x10,*\x8a\x01\n\x0eTimeFilterType\x12\x1e\n\x1aTIME_FILTER_TYPE_UNDEFINED\x10\x00\x12\x1a\n\x16TIME_FILTER_TYPE_QUICK\x10\x01\x12\x1d\n\x19TIME_FILTER_TYPE_ABSOLUTE\x10\x02\x12\x1d\n\x19TIME_FILTER_TYPE_RELATIVE\x10\x03*\x8d\x01\n\x0c\x44\x61shPageType\x12\x1c\n\x18\x44\x41SH_PAGE_TYPE_UNDEFINED\x10\x00\x12\x1c\n\x18\x44\x41SH_PAGE_TYPE_DASHBOARD\x10\x01\x12\'\n#DASH_PAGE_TYPE_VISUALIZATION_LEGACY\x10\x02\x12\x18\n\x14\x44\x41SH_PAGE_TYPE_CHART\x10\x03*\xa3\x01\n\x08\x46ilterBy\x12\x17\n\x13\x46ILTER_BY_UNDEFINED\x10\x00\x12\x15\n\x11\x46ILTER_BY_MINUTES\x10\x01\x12\x13\n\x0f\x46ILTER_BY_HOURS\x10\x02\x12\x12\n\x0e\x46ILTER_BY_DAYS\x10\x03\x12\x13\n\x0f\x46ILTER_BY_WEEKS\x10\x04\x12\x14\n\x10\x46ILTER_BY_MONTHS\x10\x05\x12\x13\n\x0f\x46ILTER_BY_YEARS\x10\x06*\xb7\x04\n\x0fWallaceDataType\x12\x1f\n\x1bWALLACE_DATA_TYPE_UNDEFINED\x10\x00\x12\x1d\n\x19WALLACE_DATA_TYPE_KEYWORD\x10\x01\x12\x1a\n\x16WALLACE_DATA_TYPE_LONG\x10\x02\x12\x1c\n\x18WALLACE_DATA_TYPE_DOUBLE\x10\x03\x12\x1d\n\x19WALLACE_DATA_TYPE_BOOLEAN\x10\x04\x12\x1a\n\x16WALLACE_DATA_TYPE_DATE\x10\x05\x12\x1c\n\x18WALLACE_DATA_TYPE_STRING\x10\x06\x12\x1c\n\x18WALLACE_DATA_TYPE_NESTED\x10\x07\x12\x1c\n\x18WALLACE_DATA_TYPE_OBJECT\x10\x08\x12\x1f\n\x1bWALLACE_DATA_TYPE_FLATTENED\x10\t\x12#\n\x1fWALLACE_DATA_TYPE_INTEGER_RANGE\x10\n\x12!\n\x1dWALLACE_DATA_TYPE_FLOAT_RANGE\x10\x0b\x12 \n\x1cWALLACE_DATA_TYPE_LONG_RANGE\x10\x0c\x12\"\n\x1eWALLACE_DATA_TYPE_DOUBLE_RANGE\x10\r\x12 \n\x1cWALLACE_DATA_TYPE_DATE_RANGE\x10\x0e\x12\x1e\n\x1aWALLACE_DATA_TYPE_IP_RANGE\x10\x0f\x12$\n WALLACE_DATA_TYPE_DOUBLE_KEYWORD\x10\x14*\xdc\x01\n\tTimeScope\x12\x0b\n\x07ONE_DAY\x10\x00\x12\x0c\n\x08ONE_WEEK\x10\x01\x12\r\n\tONE_MONTH\x10\x02\x12\x0c\n\x08ONE_YEAR\x10\x03\x12\x0e\n\nONE_MINUTE\x10\x04\x12\x10\n\x0c\x46IVE_MINUTES\x10\x05\x12\x0f\n\x0bTEN_MINUTES\x10\x06\x12\x12\n\x0eTWENTY_MINUTES\x10\x07\x12\x12\n\x0eTHIRTY_MINUTES\x10\x08\x12\x0c\n\x08ONE_HOUR\x10\t\x12\r\n\tTWO_HOURS\x10\n\x12\x0f\n\x0bTHREE_HOURS\x10\x0b\x12\x0e\n\nFOUR_HOURS\x10\x0c*\xa1\x06\n\x03Tag\x12\x0b\n\x07TAG_ALL\x10\x00\x12\x0e\n\nTAG_CUSTOM\x10\x01\x12\x0e\n\nTAG_LEGACY\x10\x02\x12\x0f\n\x0bTAG_DYNAMIC\x10\x03\x12\x1e\n\x1aP3_RJ_RECORDS_INBOUND_CALL\x10\x65\x12\x1d\n\x19P3_RJ_RECORDS_MANUAL_CALL\x10\x66\x12\x1f\n\x1bP3_RJ_RECORDS_OUTBOUND_CALL\x10g\x12\x1f\n\x1bP3_RJ_RECORDS_OUTBOUND_TASK\x10h\x12%\n!P3_RJ_RECORDS_AGENT_CALL_OUTBOUND\x10i\x12$\n P3_RJ_RECORDS_AGENT_CALL_INBOUND\x10j\x12#\n\x1fP3_RJ_RECORDS_AGENT_CALL_MANUAL\x10k\x12\x15\n\x11P3_RJ_RECORDS_SMS\x10l\x12\x17\n\x13P3_RJ_RECORDS_EMAIL\x10m\x12\x1c\n\x17P3_RJ_AGGREGATE_INBOUND\x10\xc9\x01\x12\x1d\n\x18P3_RJ_AGGREGATE_OUTBOUND\x10\xca\x01\x12\x1b\n\x16P3_RJ_AGGREGATE_MANUAL\x10\xcb\x01\x12\x1f\n\x1aP3_RJ_AGGREGATE_AGENT_CALL\x10\xcc\x01\x12\x1f\n\x1aP3_RJ_AGGREGATE_HUNT_GROUP\x10\xcd\x01\x12\"\n\x1dP3_RJ_AGGREGATE_AGENT_SESSION\x10\xce\x01\x12\x1b\n\x16P3_RJ_AGGREGATE_SKILLS\x10\xcf\x01\x12\x1b\n\x16P3_RJ_COLLATED_INBOUND\x10\xad\x02\x12\x1c\n\x17P3_RJ_COLLATED_OUTBOUND\x10\xae\x02\x12\x1a\n\x15P3_RJ_COLLATED_MANUAL\x10\xaf\x02\x12\x1e\n\x19P3_RJ_COLLATED_AGENT_CALL\x10\xb0\x02\x12\x1e\n\x19P3_RJ_COLLATED_HUNT_GROUP\x10\xb1\x02\x12!\n\x1cP3_RJ_COLLATED_AGENT_SESSION\x10\xb2\x02\x12\"\n\x1dP3_RJ_MISC_SCHEDULED_CALLBACK\x10\xe9\x07*9\n\x0c\x43svQuoteType\x12\x11\n\rNO_QUOTE_TYPE\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02*\xeb\x01\n\x10StringComparison\x12\r\n\tSTRING_EQ\x10\x00\x12\x0e\n\nSTRING_NEQ\x10\x01\x12\x16\n\x12STRING_STARTS_WITH\x10\x02\x12\x1a\n\x16STRING_NOT_STARTS_WITH\x10\x03\x12\x13\n\x0fSTRING_CONTAINS\x10\x04\x12\x17\n\x13STRING_NOT_CONTAINS\x10\x05\x12\x14\n\x10STRING_ENDS_WITH\x10\x06\x12\x18\n\x14STRING_NOT_ENDS_WITH\x10\x07\x12\x10\n\x0cSTRING_BLANK\x10\x08\x12\x14\n\x10STRING_NOT_BLANK\x10\t*v\n\x0f\x46loatComparison\x12\x0c\n\x08\x46LOAT_EQ\x10\x00\x12\r\n\tFLOAT_NEQ\x10\x01\x12\x06\n\x02LT\x10\x02\x12\x07\n\x03LTE\x10\x03\x12\x06\n\x02GT\x10\x04\x12\x07\n\x03GTE\x10\x05\x12\x0f\n\x0b\x46LOAT_BLANK\x10\x06\x12\x13\n\x0f\x46LOAT_NOT_BLANK\x10\x07*+\n\x0e\x42oolComparison\x12\x0b\n\x07\x42OOL_EQ\x10\x00\x12\x0c\n\x08\x42OOL_NEQ\x10\x01*\xa3\x01\n\x0e\x44\x61teComparison\x12\x16\n\x12\x44\x41TE_COMPARISON_EQ\x10\x00\x12\x17\n\x13\x44\x41TE_COMPARISON_NEQ\x10\x01\x12\x16\n\x12\x44\x41TE_COMPARISON_LT\x10\x02\x12\x17\n\x13\x44\x41TE_COMPARISON_LTE\x10\x03\x12\x16\n\x12\x44\x41TE_COMPARISON_GT\x10\x04\x12\x17\n\x13\x44\x41TE_COMPARISON_GTE\x10\x05*%\n\x12\x43ompoundFilterJoin\x12\x07\n\x03\x41ND\x10\x00\x12\x06\n\x02OR\x10\x01*_\n\rAnaExportType\x12\x19\n\x15\x41NA_EXPORT_TYPE_EMAIL\x10\x00\x12\x18\n\x14\x41NA_EXPORT_TYPE_SFTP\x10\x01\x12\x19\n\x15\x41NA_EXPORT_TYPE_HTTPS\x10\x02*S\n\x19\x45xporterDataSelectionType\x12\x1b\n\x17\x43HART_ID_SELECTION_TYPE\x10\x00\x12\x19\n\x15\x43USTOM_SELECTION_TYPE\x10\x01*\x9c\x02\n\x12NumericAggregation\x12\x1e\n\x1a\x46LOAT_AGGREGATION_TOP_HITS\x10\x00\x12\x1d\n\x19\x46LOAT_AGGREGATION_AVERAGE\x10\x01\x12\x19\n\x15\x46LOAT_AGGREGATION_SUM\x10\x02\x12\x19\n\x15\x46LOAT_AGGREGATION_MIN\x10\x03\x12\x19\n\x15\x46LOAT_AGGREGATION_MAX\x10\x04\x12\x1b\n\x17\x46LOAT_AGGREGATION_TERMS\x10\x05\x12 \n\x1c\x46LOAT_AGGREGATION_PERCENTILE\x10\x06\x12\x1b\n\x17\x46LOAT_AGGREGATION_COUNT\x10\x07\x12\x1a\n\x16\x46LOAT_AGGREGATION_NONE\x10\x64*\x91\x01\n\x15NonNumericAggregation\x12\x1f\n\x1bSTRING_AGGREGATION_TOP_HITS\x10\x00\x12\x1c\n\x18STRING_AGGREGATION_TERMS\x10\x05\x12\x1c\n\x18STRING_AGGREGATION_COUNT\x10\x07\x12\x1b\n\x17STRING_AGGREGATION_NONE\x10\x64*\xa8\x01\n\tOperation\x12\x11\n\rOPERATION_ADD\x10\x00\x12\x1b\n\x17OPERATION_SUBTRACT_LEFT\x10\x01\x12\x1c\n\x18OPERATION_SUBTRACT_RIGHT\x10\x02\x12\x16\n\x12OPERATION_MULTIPLY\x10\x03\x12\x19\n\x15OPERATION_DIVIDE_LEFT\x10\x04\x12\x1a\n\x16OPERATION_DIVIDE_RIGHT\x10\x05*7\n\x13\x43ustomDataSeleciton\x12 \n\x1c\x43USTOM_DATA_SELECTION_UKNOWN\x10\x00*~\n\rDataPointType\x12\x1a\n\x16\x44\x41TA_POINT_TYPE_NUMBER\x10\x00\x12\x1a\n\x16\x44\x41TA_POINT_TYPE_STRING\x10\x01\x12\x1b\n\x17\x44\x41TA_POINT_TYPE_BOOLEAN\x10\x02\x12\x18\n\x14\x44\x41TA_POINT_TYPE_DATE\x10\x03*&\n\x0c\x45xportStatus\x12\x0c\n\x08NOT_SENT\x10\x00\x12\x08\n\x04SENT\x10\x01\x42h\n\x0f\x63om.api.commonsB\x08\x41naProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.ana_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\010AnaProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_ANATIMEZONE']._serialized_start=39
  _globals['_ANATIMEZONE']._serialized_end=1618
  _globals['_TIMEFILTERTYPE']._serialized_start=1621
  _globals['_TIMEFILTERTYPE']._serialized_end=1759
  _globals['_DASHPAGETYPE']._serialized_start=1762
  _globals['_DASHPAGETYPE']._serialized_end=1903
  _globals['_FILTERBY']._serialized_start=1906
  _globals['_FILTERBY']._serialized_end=2069
  _globals['_WALLACEDATATYPE']._serialized_start=2072
  _globals['_WALLACEDATATYPE']._serialized_end=2639
  _globals['_TIMESCOPE']._serialized_start=2642
  _globals['_TIMESCOPE']._serialized_end=2862
  _globals['_TAG']._serialized_start=2865
  _globals['_TAG']._serialized_end=3666
  _globals['_CSVQUOTETYPE']._serialized_start=3668
  _globals['_CSVQUOTETYPE']._serialized_end=3725
  _globals['_STRINGCOMPARISON']._serialized_start=3728
  _globals['_STRINGCOMPARISON']._serialized_end=3963
  _globals['_FLOATCOMPARISON']._serialized_start=3965
  _globals['_FLOATCOMPARISON']._serialized_end=4083
  _globals['_BOOLCOMPARISON']._serialized_start=4085
  _globals['_BOOLCOMPARISON']._serialized_end=4128
  _globals['_DATECOMPARISON']._serialized_start=4131
  _globals['_DATECOMPARISON']._serialized_end=4294
  _globals['_COMPOUNDFILTERJOIN']._serialized_start=4296
  _globals['_COMPOUNDFILTERJOIN']._serialized_end=4333
  _globals['_ANAEXPORTTYPE']._serialized_start=4335
  _globals['_ANAEXPORTTYPE']._serialized_end=4430
  _globals['_EXPORTERDATASELECTIONTYPE']._serialized_start=4432
  _globals['_EXPORTERDATASELECTIONTYPE']._serialized_end=4515
  _globals['_NUMERICAGGREGATION']._serialized_start=4518
  _globals['_NUMERICAGGREGATION']._serialized_end=4802
  _globals['_NONNUMERICAGGREGATION']._serialized_start=4805
  _globals['_NONNUMERICAGGREGATION']._serialized_end=4950
  _globals['_OPERATION']._serialized_start=4953
  _globals['_OPERATION']._serialized_end=5121
  _globals['_CUSTOMDATASELECITON']._serialized_start=5123
  _globals['_CUSTOMDATASELECITON']._serialized_end=5178
  _globals['_DATAPOINTTYPE']._serialized_start=5180
  _globals['_DATAPOINTTYPE']._serialized_end=5306
  _globals['_EXPORTSTATUS']._serialized_start=5308
  _globals['_EXPORTSTATUS']._serialized_end=5346
# @@protoc_insertion_point(module_scope)
