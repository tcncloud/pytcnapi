# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/wfm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/commons/wfm.proto\x12\x0b\x61pi.commons\x1a\x1fgoogle/protobuf/timestamp.proto\"k\n\tSkillType\"^\n\x04\x45num\x12\x0f\n\x0b\x41GENT_SKILL\x10\x00\x12\x0e\n\nHUNT_GROUP\x10\x01\x12\r\n\tAGENT_PBX\x10\x02\x12\x12\n\x0eHUNT_GROUP_PBX\x10\x03\x12\x07\n\x03PBX\x10\x04\x12\t\n\x05\x41GENT\x10\x05\"\x91\x01\n\rDatetimeRange\x12\x41\n\x0estart_datetime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rstartDatetime\x12=\n\x0c\x65nd_datetime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x65ndDatetime\"\xa4\x06\n\x15\x46orecastingParameters\x12\x39\n\x19interval_width_in_minutes\x18\x01 \x01(\x05R\x16intervalWidthInMinutes\x12\x46\n\x1fhistorical_data_range_in_months\x18\x06 \x01(\x05H\x00R\x1bhistoricalDataRangeInMonths\x12l\n$historical_data_range_start_datetime\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R historicalDataRangeStartDatetime\x12>\n\x1c\x66orecast_test_range_in_weeks\x18\x08 \x01(\x05R\x18\x66orecastTestRangeInWeeks\x12\x37\n\x17\x66orecast_range_in_weeks\x18\t \x01(\x05H\x01R\x14\x66orecastRangeInWeeks\x12T\n\x17\x66orecast_datetime_range\x18\n \x01(\x0b\x32\x1a.api.commons.DatetimeRangeH\x01R\x15\x66orecastDatetimeRange\x12\x42\n\x1dtraining_data_range_in_months\x18\x0b \x01(\x05H\x02R\x19trainingDataRangeInMonths\x12]\n\x1ctraining_data_datetime_range\x18\x0c \x01(\x0b\x32\x1a.api.commons.DatetimeRangeH\x02R\x19trainingDataDatetimeRange\x12N\n$averages_calculation_range_in_months\x18\r \x01(\x05R averagesCalculationRangeInMonthsB\x17\n\x15historical_data_rangeB\x10\n\x0e\x66orecast_rangeB\x15\n\x13training_data_rangeJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\"\xc4\x01\n\nProfileTOD\x12\x16\n\x06sunday\x18\x01 \x03(\x02R\x06sunday\x12\x16\n\x06monday\x18\x02 \x03(\x02R\x06monday\x12\x18\n\x07tuesday\x18\x03 \x03(\x02R\x07tuesday\x12\x1c\n\twednesday\x18\x04 \x03(\x02R\twednesday\x12\x1a\n\x08thursday\x18\x05 \x03(\x02R\x08thursday\x12\x16\n\x06\x66riday\x18\x06 \x03(\x02R\x06\x66riday\x12\x1a\n\x08saturday\x18\x07 \x03(\x02R\x08saturday\"\xb1\x02\n\x0bProfileWOMS\x12\x18\n\x07january\x18\x01 \x03(\x02R\x07january\x12\x1a\n\x08\x66\x65\x62ruary\x18\x02 \x03(\x02R\x08\x66\x65\x62ruary\x12\x14\n\x05march\x18\x03 \x03(\x02R\x05march\x12\x14\n\x05\x61pril\x18\x04 \x03(\x02R\x05\x61pril\x12\x10\n\x03may\x18\x05 \x03(\x02R\x03may\x12\x12\n\x04june\x18\x06 \x03(\x02R\x04june\x12\x12\n\x04july\x18\x07 \x03(\x02R\x04july\x12\x16\n\x06\x61ugust\x18\x08 \x03(\x02R\x06\x61ugust\x12\x1c\n\tseptember\x18\t \x03(\x02R\tseptember\x12\x18\n\x07october\x18\n \x03(\x02R\x07october\x12\x1a\n\x08november\x18\x0b \x03(\x02R\x08november\x12\x1a\n\x08\x64\x65\x63\x65mber\x18\x0c \x03(\x02R\x08\x64\x65\x63\x65mber\"\xc4\x01\n\nProfileDOW\x12\x16\n\x06sunday\x18\x01 \x01(\x02R\x06sunday\x12\x16\n\x06monday\x18\x02 \x01(\x02R\x06monday\x12\x18\n\x07tuesday\x18\x03 \x01(\x02R\x07tuesday\x12\x1c\n\twednesday\x18\x04 \x01(\x02R\twednesday\x12\x1a\n\x08thursday\x18\x05 \x01(\x02R\x08thursday\x12\x16\n\x06\x66riday\x18\x06 \x01(\x02R\x06\x66riday\x12\x1a\n\x08saturday\x18\x07 \x01(\x02R\x08saturday\"\xb0\x02\n\nProfileMOY\x12\x18\n\x07january\x18\x01 \x01(\x02R\x07january\x12\x1a\n\x08\x66\x65\x62ruary\x18\x02 \x01(\x02R\x08\x66\x65\x62ruary\x12\x14\n\x05march\x18\x03 \x01(\x02R\x05march\x12\x14\n\x05\x61pril\x18\x04 \x01(\x02R\x05\x61pril\x12\x10\n\x03may\x18\x05 \x01(\x02R\x03may\x12\x12\n\x04june\x18\x06 \x01(\x02R\x04june\x12\x12\n\x04july\x18\x07 \x01(\x02R\x04july\x12\x16\n\x06\x61ugust\x18\x08 \x01(\x02R\x06\x61ugust\x12\x1c\n\tseptember\x18\t \x01(\x02R\tseptember\x12\x18\n\x07october\x18\n \x01(\x02R\x07october\x12\x1a\n\x08november\x18\x0b \x01(\x02R\x08november\x12\x1a\n\x08\x64\x65\x63\x65mber\x18\x0c \x01(\x02R\x08\x64\x65\x63\x65mber\"\x80\x02\n\x13\x44istributionProfile\x12\x38\n\x0bprofile_tod\x18\x01 \x01(\x0b\x32\x17.api.commons.ProfileTODR\nprofileTod\x12;\n\x0cprofile_woms\x18\x02 \x01(\x0b\x32\x18.api.commons.ProfileWOMSR\x0bprofileWoms\x12\x38\n\x0bprofile_dow\x18\x03 \x01(\x0b\x32\x17.api.commons.ProfileDOWR\nprofileDow\x12\x38\n\x0bprofile_moy\x18\x04 \x01(\x0b\x32\x17.api.commons.ProfileMOYR\nprofileMoy\"\x8d\x01\n\x15\x43\x61llProfileGroupCalls\x12\x1f\n\x0btotal_calls\x18\x01 \x01(\x05R\ntotalCalls\x12S\n\x14\x64istribution_profile\x18\x02 \x01(\x0b\x32 .api.commons.DistributionProfileR\x13\x64istributionProfile\"\xad\x01\n\x14\x43\x61llProfileGroupAvgs\x12\x1f\n\x0bmin_average\x18\x01 \x01(\x02R\nminAverage\x12\x1f\n\x0bmax_average\x18\x02 \x01(\x02R\nmaxAverage\x12S\n\x14\x64istribution_profile\x18\x03 \x01(\x0b\x32 .api.commons.DistributionProfileR\x13\x64istributionProfile\"\xbf\x01\n\x0bOptionTypes\x12J\n\x11open_times_option\x18\x01 \x01(\x0e\x32\x1c.api.commons.OpenTimesOptionH\x00R\x0fopenTimesOption\x12R\n\x13\x61vailability_option\x18\x02 \x01(\x0e\x32\x1f.api.commons.AvailabilityOptionH\x00R\x12\x61vailabilityOptionB\x10\n\x0e\x64\x65sired_option\"u\n\x10ScheduleSelector\x12!\n\x0cschedule_sid\x18\x01 \x01(\x03R\x0bscheduleSid\x12>\n\rschedule_type\x18\x02 \x01(\x0e\x32\x19.api.commons.ScheduleTypeR\x0cscheduleType\"\x85\x02\n\x14SkillProfileCategory\x12;\n\x1askill_profile_category_sid\x18\x01 \x01(\x03R\x17skillProfileCategorySid\x12m\n\x1bskill_profile_category_type\x18\x02 \x01(\x0e\x32..api.commons.SkillProfileCategory.CategoryTypeR\x18skillProfileCategoryType\"A\n\x0c\x43\x61tegoryType\x12\x18\n\x14SINGLE_SKILL_PROFILE\x10\x00\x12\x17\n\x13SKILL_PROFILE_GROUP\x10\x01*\xa8\x01\n\x1eRegressionForecasterModelTypes\x12\x11\n\rRANDOM_FOREST\x10\x00\x12\x0c\n\x08\x41\x44\x41\x42OOST\x10\x01\x12\x15\n\x11GRADIENT_BOOSTING\x10\x02\x12\x15\n\x11LINEAR_REGRESSION\x10\x03\x12\x0e\n\nLINEAR_AVG\x10\x04\x12\x14\n\x10SEGMENTED_LINEAR\x10\x05\x12\x07\n\x03MLP\x10\x06\x12\x08\n\x04\x41UTO\x10\x07*X\n&RegressionForecasterAvgsProcessingType\x12\x0c\n\x08\x46ORECAST\x10\x00\x12\x0c\n\x08\x41VERAGES\x10\x01\x12\x12\n\x0e\x46IXED_AVERAGES\x10\x02*d\n\x12\x43onstraintTimeUnit\x12\x0b\n\x07MINUTES\x10\x00\x12\t\n\x05HOURS\x10\x01\x12\n\n\x06SHIFTS\x10\x02\x12\x08\n\x04\x44\x41YS\x10\x03\x12\t\n\x05WEEKS\x10\x04\x12\n\n\x06MONTHS\x10\x05\x12\t\n\x05YEARS\x10\x06*\xc2\x02\n\x10\x43onfigEntityType\x12\x14\n\x10\x43\x41LL_CENTER_NODE\x10\x00\x12\x0f\n\x0b\x43LIENT_NODE\x10\x01\x12\x11\n\rLOCATION_NODE\x10\x02\x12\x10\n\x0cPROGRAM_NODE\x10\x03\x12\x0f\n\x0b\x41GENT_GROUP\x10\x04\x12\x12\n\x0eSHIFT_TEMPLATE\x10\x05\x12\r\n\tWFM_AGENT\x10\x06\x12\x12\n\x0ePLACEMENT_RULE\x10\x07\x12\x13\n\x0f\x43ONSTRAINT_RULE\x10\x08\x12\x16\n\x12NON_SKILL_ACTIVITY\x10\t\x12\x16\n\x12\x41GENT_AVAILABILITY\x10\n\x12\x0e\n\nOPEN_TIMES\x10\x0b\x12\x17\n\x13SCHEDULING_ACTIVITY\x10\x0c\x12\x15\n\x11SKILL_PROFICIENCY\x10\r\x12\x15\n\x11SCHEDULE_SCENARIO\x10\x0e*\xc1\x01\n\x12\x43onstraintRuleType\x12\x11\n\rMIN_CONSEC_ON\x10\x00\x12\x11\n\rMAX_CONSEC_ON\x10\x01\x12\x12\n\x0eMIN_CONSEC_OFF\x10\x02\x12\x12\n\x0eMAX_CONSEC_OFF\x10\x03\x12\x10\n\x0cMIN_TOTAL_ON\x10\x04\x12\x10\n\x0cMAX_TOTAL_ON\x10\x05\x12\x11\n\rMIN_TOTAL_OFF\x10\x06\x12\x11\n\rMAX_TOTAL_OFF\x10\x07\x12\x13\n\x0fMIN_SKILL_LEVEL\x10\x08*3\n\x10\x44OWPlacementType\x12\x0c\n\x08MUST_NOT\x10\x00\x12\x07\n\x03MAY\x10\x01\x12\x08\n\x04MUST\x10\x02*\'\n\x0fOpenTimesOption\x12\n\n\x06\x43LOSED\x10\x00\x12\x08\n\x04OPEN\x10\x01*P\n\x12\x41vailabilityOption\x12\r\n\tAVAILABLE\x10\x00\x12\x11\n\rNOT_AVAILABLE\x10\x01\x12\x18\n\x14PREFER_NOT_AVAILABLE\x10\x02*J\n\tDayOfWeek\x12\x07\n\x03MON\x10\x00\x12\x07\n\x03TUE\x10\x01\x12\x07\n\x03WED\x10\x02\x12\x07\n\x03THU\x10\x03\x12\x07\n\x03\x46RI\x10\x04\x12\x07\n\x03SAT\x10\x05\x12\x07\n\x03SUN\x10\x06*^\n\x16\x43onfigRelationshipType\x12\x16\n\x12IS_ASSOCIATED_WITH\x10\x00\x12\x1a\n\x16IS_NOT_ASSOCIATED_WITH\x10\x01\x12\x10\n\x0cIS_MEMBER_OF\x10\x02*i\n\x0f\x44iagnosticLevel\x12\x0f\n\x0bINFORMATION\x10\x00\x12\x0e\n\nSUGGESTION\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\x14\n\x10\x44IAGNOSTIC_ERROR\x10\x03\x12\x12\n\x0eINTERNAL_ERROR\x10\x04*\xf5\x07\n\x0e\x44iagnosticCode\x12\x0b\n\x07GENERAL\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x1b\n\x17NO_SKILLS_IN_DICTIONARY\x10\x02\x12$\n AGENT_HAS_NO_SKILL_PROFICIENCIES\x10\x03\x12\x17\n\x13\x41GENT_HAS_NO_SKILLS\x10\x04\x12\x31\n-NO_SCHEDULING_ACTIVITIES_FOR_CONSTRAINT_RULES\x10\x05\x12\x35\n1SCHEDULING_ACTIVITY_FOR_CONSTRAINT_RULE_NOT_FOUND\x10\x06\x12!\n\x1dSHIFT_TEMPLATE_CANNOT_BE_NONE\x10\x07\x12)\n%SHIFT_TEMPLATE_HAS_NO_PLACEMENT_RULES\x10\x08\x12/\n+NO_ONCALL_IN_SHIFT_TEMPLATE_PLACEMENT_RULES\x10\t\x12\x39\n5MIN_GT_MAX_DURATION_IN_SHIFT_TEMPLATE_PLACEMENT_RULES\x10\n\x12\'\n#MIN_GT_MAX_AGENTS_IN_SHIFT_TEMPLATE\x10\x0b\x12)\n%NO_PLACEMENT_RULES_FOR_SHIFT_TEMPLATE\x10\x0c\x12!\n\x1d\x41\x43TIVITIES_SHORTER_THAN_SHIFT\x10\r\x12\x1f\n\x1bNOT_ENOUGH_AGENTS_FOR_SHIFT\x10\x0e\x12\x1f\n\x1bPROGRAM_HAS_NO_AGENT_GROUPS\x10\x0f\x12\"\n\x1ePROGRAM_HAS_NO_SHIFT_TEMPLATES\x10\x10\x12\x1c\n\x18LOCATION_HAS_NO_PROGRAMS\x10\x11\x12\x1b\n\x17\x43LIENT_HAS_NO_LOCATIONS\x10\x12\x12\x1e\n\x1a\x43\x41LL_CENTER_HAS_NO_CLIENTS\x10\x13\x12\'\n#PROGRAM_HAS_INVALID_PARENT_LOCATION\x10\x14\x12&\n\"LOCATION_HAS_INVALID_PARENT_CLIENT\x10\x15\x12)\n%CLIENT_HAS_INVALID_PARENT_CALL_CENTER\x10\x16\x12\'\n#AGENT_GROUP_HAS_INVALID_PARENT_NODE\x10\x17\x12-\n)SHIFT_TEMPLATE_HAS_INVALID_PARENT_PROGRAM\x10\x18\x12\x42\n>NO_SKILL_PROFICIENCY_FOR_MIN_SKILL_PROFICIENCY_CONSTRAINT_RULE\x10\x19*\xca\x01\n\x15PerformanceMetricType\x12#\n\x1f\x46TE_REQUIRED_VS_ACHIEVED_SIMPLE\x10\x00\x12%\n!FTE_REQUIRED_VS_ACHIEVED_EXTENDED\x10\x01\x12\x1a\n\x16SERVICE_LEVEL_ANALYSIS\x10\x02\x12\x18\n\x14SERVICE_LEVEL_MATRIX\x10\x03\x12\x1c\n\x18\x43ONTACT_HANDLING_METRICS\x10\x04\x12\x11\n\rLOAD_FORECAST\x10\x05*|\n\x15ScheduleShouldInclude\x12\x18\n\x14ONLY_SHIFT_INSTANCES\x10\x00\x12\x1c\n\x18ONLY_PERFORMANCE_METRICS\x10\x01\x12+\n\'SHIFT_INSTANCES_AND_PERFORMANCE_METRICS\x10\x02*(\n\x0cScheduleType\x12\t\n\x05\x44RAFT\x10\x00\x12\r\n\tPUBLISHED\x10\x01*7\n\x14SchedulingTargetType\x12\x0c\n\x08\x43OVERAGE\x10\x00\x12\x11\n\rSERVICE_LEVEL\x10\x01\x42h\n\x0f\x63om.api.commonsB\x08WfmProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.wfm_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.api.commonsB\010WfmProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_REGRESSIONFORECASTERMODELTYPES']._serialized_start=3305
  _globals['_REGRESSIONFORECASTERMODELTYPES']._serialized_end=3473
  _globals['_REGRESSIONFORECASTERAVGSPROCESSINGTYPE']._serialized_start=3475
  _globals['_REGRESSIONFORECASTERAVGSPROCESSINGTYPE']._serialized_end=3563
  _globals['_CONSTRAINTTIMEUNIT']._serialized_start=3565
  _globals['_CONSTRAINTTIMEUNIT']._serialized_end=3665
  _globals['_CONFIGENTITYTYPE']._serialized_start=3668
  _globals['_CONFIGENTITYTYPE']._serialized_end=3990
  _globals['_CONSTRAINTRULETYPE']._serialized_start=3993
  _globals['_CONSTRAINTRULETYPE']._serialized_end=4186
  _globals['_DOWPLACEMENTTYPE']._serialized_start=4188
  _globals['_DOWPLACEMENTTYPE']._serialized_end=4239
  _globals['_OPENTIMESOPTION']._serialized_start=4241
  _globals['_OPENTIMESOPTION']._serialized_end=4280
  _globals['_AVAILABILITYOPTION']._serialized_start=4282
  _globals['_AVAILABILITYOPTION']._serialized_end=4362
  _globals['_DAYOFWEEK']._serialized_start=4364
  _globals['_DAYOFWEEK']._serialized_end=4438
  _globals['_CONFIGRELATIONSHIPTYPE']._serialized_start=4440
  _globals['_CONFIGRELATIONSHIPTYPE']._serialized_end=4534
  _globals['_DIAGNOSTICLEVEL']._serialized_start=4536
  _globals['_DIAGNOSTICLEVEL']._serialized_end=4641
  _globals['_DIAGNOSTICCODE']._serialized_start=4644
  _globals['_DIAGNOSTICCODE']._serialized_end=5657
  _globals['_PERFORMANCEMETRICTYPE']._serialized_start=5660
  _globals['_PERFORMANCEMETRICTYPE']._serialized_end=5862
  _globals['_SCHEDULESHOULDINCLUDE']._serialized_start=5864
  _globals['_SCHEDULESHOULDINCLUDE']._serialized_end=5988
  _globals['_SCHEDULETYPE']._serialized_start=5990
  _globals['_SCHEDULETYPE']._serialized_end=6030
  _globals['_SCHEDULINGTARGETTYPE']._serialized_start=6032
  _globals['_SCHEDULINGTARGETTYPE']._serialized_end=6087
  _globals['_SKILLTYPE']._serialized_start=71
  _globals['_SKILLTYPE']._serialized_end=178
  _globals['_SKILLTYPE_ENUM']._serialized_start=84
  _globals['_SKILLTYPE_ENUM']._serialized_end=178
  _globals['_DATETIMERANGE']._serialized_start=181
  _globals['_DATETIMERANGE']._serialized_end=326
  _globals['_FORECASTINGPARAMETERS']._serialized_start=329
  _globals['_FORECASTINGPARAMETERS']._serialized_end=1133
  _globals['_PROFILETOD']._serialized_start=1136
  _globals['_PROFILETOD']._serialized_end=1332
  _globals['_PROFILEWOMS']._serialized_start=1335
  _globals['_PROFILEWOMS']._serialized_end=1640
  _globals['_PROFILEDOW']._serialized_start=1643
  _globals['_PROFILEDOW']._serialized_end=1839
  _globals['_PROFILEMOY']._serialized_start=1842
  _globals['_PROFILEMOY']._serialized_end=2146
  _globals['_DISTRIBUTIONPROFILE']._serialized_start=2149
  _globals['_DISTRIBUTIONPROFILE']._serialized_end=2405
  _globals['_CALLPROFILEGROUPCALLS']._serialized_start=2408
  _globals['_CALLPROFILEGROUPCALLS']._serialized_end=2549
  _globals['_CALLPROFILEGROUPAVGS']._serialized_start=2552
  _globals['_CALLPROFILEGROUPAVGS']._serialized_end=2725
  _globals['_OPTIONTYPES']._serialized_start=2728
  _globals['_OPTIONTYPES']._serialized_end=2919
  _globals['_SCHEDULESELECTOR']._serialized_start=2921
  _globals['_SCHEDULESELECTOR']._serialized_end=3038
  _globals['_SKILLPROFILECATEGORY']._serialized_start=3041
  _globals['_SKILLPROFILECATEGORY']._serialized_end=3302
  _globals['_SKILLPROFILECATEGORY_CATEGORYTYPE']._serialized_start=3237
  _globals['_SKILLPROFILECATEGORY_CATEGORYTYPE']._serialized_end=3302
# @@protoc_insertion_point(module_scope)
