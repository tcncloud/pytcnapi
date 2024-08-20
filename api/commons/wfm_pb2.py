# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/wfm.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'api/commons/wfm.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/commons/wfm.proto\x12\x0b\x61pi.commons\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"k\n\tSkillType\"^\n\x04\x45num\x12\x0f\n\x0b\x41GENT_SKILL\x10\x00\x12\x0e\n\nHUNT_GROUP\x10\x01\x12\r\n\tAGENT_PBX\x10\x02\x12\x12\n\x0eHUNT_GROUP_PBX\x10\x03\x12\x07\n\x03PBX\x10\x04\x12\t\n\x05\x41GENT\x10\x05\"\x91\x01\n\rDatetimeRange\x12\x41\n\x0estart_datetime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rstartDatetime\x12=\n\x0c\x65nd_datetime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x65ndDatetime\"\xa4\x06\n\x15\x46orecastingParameters\x12\x39\n\x19interval_width_in_minutes\x18\x01 \x01(\x05R\x16intervalWidthInMinutes\x12\x46\n\x1fhistorical_data_range_in_months\x18\x06 \x01(\x05H\x00R\x1bhistoricalDataRangeInMonths\x12l\n$historical_data_range_start_datetime\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R historicalDataRangeStartDatetime\x12>\n\x1c\x66orecast_test_range_in_weeks\x18\x08 \x01(\x05R\x18\x66orecastTestRangeInWeeks\x12\x37\n\x17\x66orecast_range_in_weeks\x18\t \x01(\x05H\x01R\x14\x66orecastRangeInWeeks\x12T\n\x17\x66orecast_datetime_range\x18\n \x01(\x0b\x32\x1a.api.commons.DatetimeRangeH\x01R\x15\x66orecastDatetimeRange\x12\x42\n\x1dtraining_data_range_in_months\x18\x0b \x01(\x05H\x02R\x19trainingDataRangeInMonths\x12]\n\x1ctraining_data_datetime_range\x18\x0c \x01(\x0b\x32\x1a.api.commons.DatetimeRangeH\x02R\x19trainingDataDatetimeRange\x12N\n$averages_calculation_range_in_months\x18\r \x01(\x05R averagesCalculationRangeInMonthsB\x17\n\x15historical_data_rangeB\x10\n\x0e\x66orecast_rangeB\x15\n\x13training_data_rangeJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06\"\xc4\x01\n\nProfileTOD\x12\x16\n\x06sunday\x18\x01 \x03(\x02R\x06sunday\x12\x16\n\x06monday\x18\x02 \x03(\x02R\x06monday\x12\x18\n\x07tuesday\x18\x03 \x03(\x02R\x07tuesday\x12\x1c\n\twednesday\x18\x04 \x03(\x02R\twednesday\x12\x1a\n\x08thursday\x18\x05 \x03(\x02R\x08thursday\x12\x16\n\x06\x66riday\x18\x06 \x03(\x02R\x06\x66riday\x12\x1a\n\x08saturday\x18\x07 \x03(\x02R\x08saturday\"\xb1\x02\n\x0bProfileWOMS\x12\x18\n\x07january\x18\x01 \x03(\x02R\x07january\x12\x1a\n\x08\x66\x65\x62ruary\x18\x02 \x03(\x02R\x08\x66\x65\x62ruary\x12\x14\n\x05march\x18\x03 \x03(\x02R\x05march\x12\x14\n\x05\x61pril\x18\x04 \x03(\x02R\x05\x61pril\x12\x10\n\x03may\x18\x05 \x03(\x02R\x03may\x12\x12\n\x04june\x18\x06 \x03(\x02R\x04june\x12\x12\n\x04july\x18\x07 \x03(\x02R\x04july\x12\x16\n\x06\x61ugust\x18\x08 \x03(\x02R\x06\x61ugust\x12\x1c\n\tseptember\x18\t \x03(\x02R\tseptember\x12\x18\n\x07october\x18\n \x03(\x02R\x07october\x12\x1a\n\x08november\x18\x0b \x03(\x02R\x08november\x12\x1a\n\x08\x64\x65\x63\x65mber\x18\x0c \x03(\x02R\x08\x64\x65\x63\x65mber\"\xc4\x01\n\nProfileDOW\x12\x16\n\x06sunday\x18\x01 \x01(\x02R\x06sunday\x12\x16\n\x06monday\x18\x02 \x01(\x02R\x06monday\x12\x18\n\x07tuesday\x18\x03 \x01(\x02R\x07tuesday\x12\x1c\n\twednesday\x18\x04 \x01(\x02R\twednesday\x12\x1a\n\x08thursday\x18\x05 \x01(\x02R\x08thursday\x12\x16\n\x06\x66riday\x18\x06 \x01(\x02R\x06\x66riday\x12\x1a\n\x08saturday\x18\x07 \x01(\x02R\x08saturday\"\xb0\x02\n\nProfileMOY\x12\x18\n\x07january\x18\x01 \x01(\x02R\x07january\x12\x1a\n\x08\x66\x65\x62ruary\x18\x02 \x01(\x02R\x08\x66\x65\x62ruary\x12\x14\n\x05march\x18\x03 \x01(\x02R\x05march\x12\x14\n\x05\x61pril\x18\x04 \x01(\x02R\x05\x61pril\x12\x10\n\x03may\x18\x05 \x01(\x02R\x03may\x12\x12\n\x04june\x18\x06 \x01(\x02R\x04june\x12\x12\n\x04july\x18\x07 \x01(\x02R\x04july\x12\x16\n\x06\x61ugust\x18\x08 \x01(\x02R\x06\x61ugust\x12\x1c\n\tseptember\x18\t \x01(\x02R\tseptember\x12\x18\n\x07october\x18\n \x01(\x02R\x07october\x12\x1a\n\x08november\x18\x0b \x01(\x02R\x08november\x12\x1a\n\x08\x64\x65\x63\x65mber\x18\x0c \x01(\x02R\x08\x64\x65\x63\x65mber\"\x80\x02\n\x13\x44istributionProfile\x12\x38\n\x0bprofile_tod\x18\x01 \x01(\x0b\x32\x17.api.commons.ProfileTODR\nprofileTod\x12;\n\x0cprofile_woms\x18\x02 \x01(\x0b\x32\x18.api.commons.ProfileWOMSR\x0bprofileWoms\x12\x38\n\x0bprofile_dow\x18\x03 \x01(\x0b\x32\x17.api.commons.ProfileDOWR\nprofileDow\x12\x38\n\x0bprofile_moy\x18\x04 \x01(\x0b\x32\x17.api.commons.ProfileMOYR\nprofileMoy\"\x8d\x01\n\x15\x43\x61llProfileGroupCalls\x12\x1f\n\x0btotal_calls\x18\x01 \x01(\x05R\ntotalCalls\x12S\n\x14\x64istribution_profile\x18\x02 \x01(\x0b\x32 .api.commons.DistributionProfileR\x13\x64istributionProfile\"\xad\x01\n\x14\x43\x61llProfileGroupAvgs\x12\x1f\n\x0bmin_average\x18\x01 \x01(\x02R\nminAverage\x12\x1f\n\x0bmax_average\x18\x02 \x01(\x02R\nmaxAverage\x12S\n\x14\x64istribution_profile\x18\x03 \x01(\x0b\x32 .api.commons.DistributionProfileR\x13\x64istributionProfile\"\xbf\x01\n\x0bOptionTypes\x12J\n\x11open_times_option\x18\x01 \x01(\x0e\x32\x1c.api.commons.OpenTimesOptionH\x00R\x0fopenTimesOption\x12R\n\x13\x61vailability_option\x18\x02 \x01(\x0e\x32\x1f.api.commons.AvailabilityOptionH\x00R\x12\x61vailabilityOptionB\x10\n\x0e\x64\x65sired_option\"u\n\x10ScheduleSelector\x12!\n\x0cschedule_sid\x18\x01 \x01(\x03R\x0bscheduleSid\x12>\n\rschedule_type\x18\x02 \x01(\x0e\x32\x19.api.commons.ScheduleTypeR\x0cscheduleType\"\x89\x02\n\x14SkillProfileCategory\x12?\n\x1askill_profile_category_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x17skillProfileCategorySid\x12m\n\x1bskill_profile_category_type\x18\x02 \x01(\x0e\x32..api.commons.SkillProfileCategory.CategoryTypeR\x18skillProfileCategoryType\"A\n\x0c\x43\x61tegoryType\x12\x18\n\x14SINGLE_SKILL_PROFILE\x10\x00\x12\x17\n\x13SKILL_PROFILE_GROUP\x10\x01\"\xaf\x03\n(SchedulingResultMetricForSkillCollection\x12\x38\n\x18total_internal_intervals\x18\x01 \x01(\x05R\x16totalInternalIntervals\x12H\n!total_intervals_with_fte_required\x18\x02 \x01(\x05R\x1dtotalIntervalsWithFteRequired\x12L\n#total_intervals_with_ftes_remaining\x18\x03 \x01(\x05R\x1ftotalIntervalsWithFtesRemaining\x12\x1a\n\x08\x63overage\x18\x04 \x01(\x02R\x08\x63overage\x12(\n\x10root_mean_square\x18\x05 \x01(\x02R\x0erootMeanSquare\x12\x1d\n\nhas_result\x18\x06 \x01(\x08R\thasResult\x12L\n\x10skill_collection\x18\x07 \x01(\x0b\x32!.api.commons.SkillProfileCategoryR\x0fskillCollection\"\xc5\x03\n\x16SchedulingResultMetric\x12\x38\n\x18total_internal_intervals\x18\x01 \x01(\x05R\x16totalInternalIntervals\x12H\n!total_intervals_with_fte_required\x18\x02 \x01(\x05R\x1dtotalIntervalsWithFteRequired\x12L\n#total_intervals_with_ftes_remaining\x18\x03 \x01(\x05R\x1ftotalIntervalsWithFtesRemaining\x12\x1a\n\x08\x63overage\x18\x04 \x01(\x02R\x08\x63overage\x12(\n\x10root_mean_square\x18\x05 \x01(\x02R\x0erootMeanSquare\x12\x1d\n\nhas_result\x18\x06 \x01(\x08R\thasResult\x12t\n\x1bmetrics_by_skill_collection\x18\x07 \x03(\x0b\x32\x35.api.commons.SchedulingResultMetricForSkillCollectionR\x18metricsBySkillCollection\"\x7f\n\x16\x43lientHistoryCacheInfo\x12\x34\n\x05state\x18\x01 \x01(\x0e\x32\x1e.api.commons.HistoryCacheStateR\x05state\x12/\n\x13progress_percentage\x18\x02 \x01(\x05R\x12progressPercentage\"2\n\nErrorTrace\x12$\n\x0egrpc_trace_bin\x18\x01 \x01(\tR\x0cgrpcTraceBin\"\x95\x01\n\x12InitialSetupStatus\x12\x34\n\x05state\x18\x01 \x01(\x0e\x32\x1e.api.commons.InitialSetupStateR\x05state\x12/\n\x13progress_percentage\x18\x02 \x01(\x05R\x12progressPercentage\x12\x18\n\x07message\x18\x03 \x01(\tR\x07message\"\xcb\x01\n\x11\x41gentStateSegment\x12 \n\x0corder_in_rts\x18\x01 \x01(\x05R\norderInRts\x12<\n\x06states\x18\x02 \x03(\x0e\x32$.api.commons.RealTimeManagementStateR\x06states\x12,\n\x10width_in_minutes\x18\x03 \x01(\x05\x42\x02\x18\x01R\x0ewidthInMinutes\x12(\n\x10width_in_seconds\x18\x04 \x01(\x05R\x0ewidthInSeconds\"\xc2\x01\n\x12\x41gentStateSequence\x12\"\n\rwfm_agent_sid\x18\x01 \x01(\x03R\x0bwfmAgentSid\x12\x41\n\x0estart_datetime\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rstartDatetime\x12\x45\n\x0estate_segments\x18\x03 \x03(\x0b\x32\x1e.api.commons.AgentStateSegmentR\rstateSegments\"\x8d\x05\n\x12\x41gentLeavePetition\x12\x35\n\x17\x61gent_leave_petition_id\x18\x01 \x01(\x03R\x14\x61gentLeavePetitionId\x12\"\n\rwfm_agent_sid\x18\x02 \x01(\x03R\x0bwfmAgentSid\x12N\n\x0fpetition_status\x18\x03 \x01(\x0e\x32%.api.commons.AgentLeavePetitionStatusR\x0epetitionStatus\x12)\n\x10petition_comment\x18\x04 \x01(\tR\x0fpetitionComment\x12)\n\x10response_comment\x18\x05 \x01(\tR\x0fresponseComment\x12V\n\x19requested_datetime_ranges\x18\x06 \x03(\x0b\x32\x1a.api.commons.DatetimeRangeR\x17requestedDatetimeRanges\x12=\n\x0c\x63reated_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x63reatedTime\x12?\n\rarchived_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x61rchivedTime\x12?\n\rresolved_time\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cresolvedTime\x12-\n\x13resolved_by_user_id\x18\n \x01(\tR\x10resolvedByUserId\x12.\n\x13requested_hours_off\x18\x0b \x01(\x02R\x11requestedHoursOff\"q\n\x0c\x43onfigEntity\x12!\n\nentity_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\tentitySid\x12>\n\x0b\x65ntity_type\x18\x02 \x01(\x0e\x32\x1d.api.commons.ConfigEntityTypeR\nentityType\"\x8b\x01\n\x1f\x41\x64herenceRuleNotificationConfig\x12T\n%adherence_rule_notification_config_id\x18\x01 \x01(\x03\x42\x02\x30\x01R!adherenceRuleNotificationConfigId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"\xad\x03\n$AdherenceRuleNotificationConfigEntry\x12_\n+adherence_rule_notification_config_entry_id\x18\x01 \x01(\x03\x42\x02\x30\x01R&adherenceRuleNotificationConfigEntryId\x12T\n%adherence_rule_notification_config_id\x18\x02 \x01(\x03\x42\x02\x30\x01R!adherenceRuleNotificationConfigId\x12*\n\x11recipient_user_id\x18\x03 \x01(\tR\x0frecipientUserId\x12]\n\x13notification_medium\x18\x04 \x01(\x0e\x32,.api.commons.AdherenceRuleNotificationMediumR\x12notificationMedium\x12\x43\n\x1fseconds_to_wait_for_no_response\x18\x05 \x01(\x05R\x1asecondsToWaitForNoResponse\"t\n\x1f\x41\x64herenceDepartmentalRuleAction\x12Q\n\x0b\x61\x63tion_type\x18\x01 \x01(\x0e\x32\x30.api.commons.AdherenceDepartmentalRuleActionTypeR\nactionType\"\xf0\x03\n\x19\x41\x64herenceDepartmentalRule\x12G\n\x1e\x61\x64herence_departmental_rule_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x1b\x61\x64herenceDepartmentalRuleId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x42\n\x0fselected_entity\x18\x03 \x01(\x0b\x32\x19.api.commons.ConfigEntityR\x0eselectedEntity\x12]\n\x15rule_requirement_type\x18\x04 \x01(\x0e\x32).api.commons.AdherenceRuleRequirementTypeR\x13ruleRequirementType\x12T\n%adherence_rule_notification_config_id\x18\x05 \x01(\x03\x42\x02\x30\x01R!adherenceRuleNotificationConfigId\x12>\n\nrule_range\x18\x06 \x01(\x0e\x32\x1f.api.commons.AdherenceRuleRangeR\truleRange\x12=\n\x0c\x63ustom_range\x18\x07 \x01(\x0b\x32\x1a.api.commons.DatetimeRangeR\x0b\x63ustomRange\"\x8c\x04\n\x1f\x41\x64herenceDepartmentalRuleClause\x12T\n%adherence_departmental_rule_clause_id\x18\x01 \x01(\x03\x42\x02\x30\x01R!adherenceDepartmentalRuleClauseId\x12G\n\x1e\x61\x64herence_departmental_rule_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\x1b\x61\x64herenceDepartmentalRuleId\x12\x44\n\x06\x61\x63tion\x18\x03 \x01(\x0b\x32,.api.commons.AdherenceDepartmentalRuleActionR\x06\x61\x63tion\x12\x41\n\tcondition\x18\x04 \x01(\x0e\x32#.api.commons.AdherenceRuleConditionR\tcondition\x12\x16\n\x06\x61mount\x18\x05 \x01(\x05R\x06\x61mount\x12\x32\n\x04unit\x18\x06 \x01(\x0e\x32\x1e.api.commons.AdherenceRuleUnitR\x04unit\x12:\n\nper_amount\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\tperAmount\x12\x39\n\x08per_unit\x18\x08 \x01(\x0e\x32\x1e.api.commons.AdherenceRuleUnitR\x07perUnit\"\xdc\x02\n\x12\x41\x64herenceAgentRule\x12\x39\n\x17\x61\x64herence_agent_rule_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x14\x61\x64herenceAgentRuleId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x42\n\x0fselected_entity\x18\x03 \x01(\x0b\x32\x19.api.commons.ConfigEntityR\x0eselectedEntity\x12]\n\x15rule_requirement_type\x18\x04 \x01(\x0e\x32).api.commons.AdherenceRuleRequirementTypeR\x13ruleRequirementType\x12T\n%adherence_rule_notification_config_id\x18\x05 \x01(\x03\x42\x02\x30\x01R!adherenceRuleNotificationConfigId\"f\n\x18\x41\x64herenceAgentRuleAction\x12J\n\x0b\x61\x63tion_type\x18\x01 \x01(\x0e\x32).api.commons.AdherenceAgentRuleActionTypeR\nactionType\"\xeb\x02\n\x18\x41\x64herenceAgentRuleClause\x12\x46\n\x1e\x61\x64herence_agent_rule_clause_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x1a\x61\x64herenceAgentRuleClauseId\x12\x39\n\x17\x61\x64herence_agent_rule_id\x18\x02 \x01(\x03\x42\x02\x30\x01R\x14\x61\x64herenceAgentRuleId\x12=\n\x06\x61\x63tion\x18\x03 \x01(\x0b\x32%.api.commons.AdherenceAgentRuleActionR\x06\x61\x63tion\x12\x41\n\tcondition\x18\x04 \x01(\x0e\x32#.api.commons.AdherenceRuleConditionR\tcondition\x12\x16\n\x06\x61mount\x18\x05 \x01(\x05R\x06\x61mount\x12\x32\n\x04unit\x18\x06 \x01(\x0e\x32\x1e.api.commons.AdherenceRuleUnitR\x04unit*\xa8\x01\n\x1eRegressionForecasterModelTypes\x12\x11\n\rRANDOM_FOREST\x10\x00\x12\x0c\n\x08\x41\x44\x41\x42OOST\x10\x01\x12\x15\n\x11GRADIENT_BOOSTING\x10\x02\x12\x15\n\x11LINEAR_REGRESSION\x10\x03\x12\x0e\n\nLINEAR_AVG\x10\x04\x12\x14\n\x10SEGMENTED_LINEAR\x10\x05\x12\x07\n\x03MLP\x10\x06\x12\x08\n\x04\x41UTO\x10\x07*X\n&RegressionForecasterAvgsProcessingType\x12\x0c\n\x08\x46ORECAST\x10\x00\x12\x0c\n\x08\x41VERAGES\x10\x01\x12\x12\n\x0e\x46IXED_AVERAGES\x10\x02*d\n\x12\x43onstraintTimeUnit\x12\x0b\n\x07MINUTES\x10\x00\x12\t\n\x05HOURS\x10\x01\x12\n\n\x06SHIFTS\x10\x02\x12\x08\n\x04\x44\x41YS\x10\x03\x12\t\n\x05WEEKS\x10\x04\x12\n\n\x06MONTHS\x10\x05\x12\t\n\x05YEARS\x10\x06*\xd0\x03\n\x10\x43onfigEntityType\x12\x14\n\x10\x43\x41LL_CENTER_NODE\x10\x00\x12\x0f\n\x0b\x43LIENT_NODE\x10\x01\x12\x11\n\rLOCATION_NODE\x10\x02\x12\x10\n\x0cPROGRAM_NODE\x10\x03\x12\x0f\n\x0b\x41GENT_GROUP\x10\x04\x12\x12\n\x0eSHIFT_TEMPLATE\x10\x05\x12\r\n\tWFM_AGENT\x10\x06\x12\x12\n\x0ePLACEMENT_RULE\x10\x07\x12\x13\n\x0f\x43ONSTRAINT_RULE\x10\x08\x12\x16\n\x12NON_SKILL_ACTIVITY\x10\t\x12\x16\n\x12\x41GENT_AVAILABILITY\x10\n\x12\x0e\n\nOPEN_TIMES\x10\x0b\x12\x17\n\x13SCHEDULING_ACTIVITY\x10\x0c\x12\x15\n\x11SKILL_PROFICIENCY\x10\r\x12\x15\n\x11SCHEDULE_SCENARIO\x10\x0e\x12\t\n\x05SKILL\x10\x0f\x12\x10\n\x0cTOUR_PATTERN\x10\x10\x12\x15\n\x11TOUR_WEEK_PATTERN\x10\x11\x12\x1e\n\x1aTOUR_SHIFT_INSTANCE_CONFIG\x10\x12\x12\x1d\n\x19TOUR_SHIFT_SEGMENT_CONFIG\x10\x13\x12\x19\n\x15TOUR_AGENT_COLLECTION\x10\x14*\xc1\x01\n\x12\x43onstraintRuleType\x12\x11\n\rMIN_CONSEC_ON\x10\x00\x12\x11\n\rMAX_CONSEC_ON\x10\x01\x12\x12\n\x0eMIN_CONSEC_OFF\x10\x02\x12\x12\n\x0eMAX_CONSEC_OFF\x10\x03\x12\x10\n\x0cMIN_TOTAL_ON\x10\x04\x12\x10\n\x0cMAX_TOTAL_ON\x10\x05\x12\x11\n\rMIN_TOTAL_OFF\x10\x06\x12\x11\n\rMAX_TOTAL_OFF\x10\x07\x12\x13\n\x0fMIN_SKILL_LEVEL\x10\x08*3\n\x10\x44OWPlacementType\x12\x0c\n\x08MUST_NOT\x10\x00\x12\x07\n\x03MAY\x10\x01\x12\x08\n\x04MUST\x10\x02*\'\n\x0fOpenTimesOption\x12\n\n\x06\x43LOSED\x10\x00\x12\x08\n\x04OPEN\x10\x01*P\n\x12\x41vailabilityOption\x12\r\n\tAVAILABLE\x10\x00\x12\x11\n\rNOT_AVAILABLE\x10\x01\x12\x18\n\x14PREFER_NOT_AVAILABLE\x10\x02*J\n\tDayOfWeek\x12\x07\n\x03MON\x10\x00\x12\x07\n\x03TUE\x10\x01\x12\x07\n\x03WED\x10\x02\x12\x07\n\x03THU\x10\x03\x12\x07\n\x03\x46RI\x10\x04\x12\x07\n\x03SAT\x10\x05\x12\x07\n\x03SUN\x10\x06*^\n\x16\x43onfigRelationshipType\x12\x16\n\x12IS_ASSOCIATED_WITH\x10\x00\x12\x1a\n\x16IS_NOT_ASSOCIATED_WITH\x10\x01\x12\x10\n\x0cIS_MEMBER_OF\x10\x02*i\n\x0f\x44iagnosticLevel\x12\x0f\n\x0bINFORMATION\x10\x00\x12\x0e\n\nSUGGESTION\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\x14\n\x10\x44IAGNOSTIC_ERROR\x10\x03\x12\x12\n\x0eINTERNAL_ERROR\x10\x04*\xe7\x18\n\x0e\x44iagnosticCode\x12\x0b\n\x07GENERAL\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x1b\n\x17NO_SKILLS_IN_DICTIONARY\x10\x02\x12$\n AGENT_HAS_NO_SKILL_PROFICIENCIES\x10\x03\x12\x17\n\x13\x41GENT_HAS_NO_SKILLS\x10\x04\x12\x31\n-NO_SCHEDULING_ACTIVITIES_FOR_CONSTRAINT_RULES\x10\x05\x12\x35\n1SCHEDULING_ACTIVITY_FOR_CONSTRAINT_RULE_NOT_FOUND\x10\x06\x12!\n\x1dSHIFT_TEMPLATE_CANNOT_BE_NONE\x10\x07\x12)\n%SHIFT_TEMPLATE_HAS_NO_PLACEMENT_RULES\x10\x08\x12/\n+NO_ONCALL_IN_SHIFT_TEMPLATE_PLACEMENT_RULES\x10\t\x12\x39\n5MIN_GT_MAX_DURATION_IN_SHIFT_TEMPLATE_PLACEMENT_RULES\x10\n\x12\'\n#MIN_GT_MAX_AGENTS_IN_SHIFT_TEMPLATE\x10\x0b\x12)\n%NO_PLACEMENT_RULES_FOR_SHIFT_TEMPLATE\x10\x0c\x12!\n\x1d\x41\x43TIVITIES_SHORTER_THAN_SHIFT\x10\r\x12\x1f\n\x1bNOT_ENOUGH_AGENTS_FOR_SHIFT\x10\x0e\x12\x1f\n\x1bPROGRAM_HAS_NO_AGENT_GROUPS\x10\x0f\x12\"\n\x1ePROGRAM_HAS_NO_SHIFT_TEMPLATES\x10\x10\x12\x1c\n\x18LOCATION_HAS_NO_PROGRAMS\x10\x11\x12\x1b\n\x17\x43LIENT_HAS_NO_LOCATIONS\x10\x12\x12\x1e\n\x1a\x43\x41LL_CENTER_HAS_NO_CLIENTS\x10\x13\x12\'\n#PROGRAM_HAS_INVALID_PARENT_LOCATION\x10\x14\x12&\n\"LOCATION_HAS_INVALID_PARENT_CLIENT\x10\x15\x12)\n%CLIENT_HAS_INVALID_PARENT_CALL_CENTER\x10\x16\x12\'\n#AGENT_GROUP_HAS_INVALID_PARENT_NODE\x10\x17\x12-\n)SHIFT_TEMPLATE_HAS_INVALID_PARENT_PROGRAM\x10\x18\x12\x42\n>NO_SKILL_PROFICIENCY_FOR_MIN_SKILL_PROFICIENCY_CONSTRAINT_RULE\x10\x19\x12\x35\n1TOO_MANY_AGENTS_WITH_LOCKED_SHIFTS_FOR_MIN_AGENTS\x10\x1a\x12+\n\'AGENT_DOES_NOT_BELONG_TO_AN_AGENT_GROUP\x10\x1b\x12 \n\x1cINVALID_CONSTRAINT_VAL_UNITS\x10\x1c\x12\x1e\n\x1a\x43ONSTRAINT_GENERAL_FAILURE\x10\x1d\x12&\n\"CANDIDATE_SHIFT_COLLISION_DETECTED\x10\x1e\x12\'\n#CANDIDATE_SHIFT_AGENT_NOT_AVAILABLE\x10\x1f\x12\x14\n\x10\x43\x41NDIDATE_CLOSED\x10 \x12!\n\x1d\x43ONSTRAINT_ACTIVITY_NOT_FOUND\x10!\x12.\n*CONSTRAINT_AGENT_DOES_NOT_HAVE_PROFICIENCY\x10\"\x12(\n$CONSTRAINT_AGENT_PROFICIENCY_TOO_LOW\x10#\x12#\n\x1f\x43ONSTRAINT_MAX_TOTAL_ON_FAILURE\x10$\x12#\n\x1f\x43ONSTRAINT_MIN_TOTAL_ON_FAILURE\x10%\x12$\n CONSTRAINT_MAX_TOTAL_OFF_FAILURE\x10&\x12$\n CONSTRAINT_MIN_TOTAL_OFF_FAILURE\x10\'\x12$\n CONSTRAINT_MAX_CONSEC_ON_FAILURE\x10(\x12$\n CONSTRAINT_MIN_CONSEC_ON_FAILURE\x10)\x12%\n!CONSTRAINT_MAX_CONSEC_OFF_FAILURE\x10*\x12%\n!CONSTRAINT_MIN_CONSEC_OFF_FAILURE\x10+\x12?\n;CONSTRAINT_CANNOT_HAVE_DAY_WEEK_MONTH_YEAR_SHIFT__PER_SHIFT\x10,\x12\x41\n=CONSTRAINT_CANNOT_HAVE_DAY_WEEK_MONTH_YEAR__PER_MINUTES_HOURS\x10-\x12\x32\n.CONSTRAINT_CONSECUTIVE_SHIFTS_RULE_NOT_ALLOWED\x10.\x12>\n:CONSTRAINT_WITH_LARGER_PERIOD_PER_SMALL_PERIOD_NOT_ALLOWED\x10/\x12\x36\n2CONSTRAINT_MIN_MAX_OFF_TIME_FOR_SHIFTS_NOT_ALLOWED\x10\x30\x12?\n;CONSTRAINT_CANNOT_HAVE_CONSECUTIVE_TIME_PER_MULTIPLE_SHIFTS\x10\x31\x12=\n9CANNOT_GENERATE_TOUR_PATTERNS_FOR_NON_TOUR_SHIFT_TEMPLATE\x10\x32\x12)\n%TOUR_PATTERNS_NEEDED_TO_SCHEDULE_TOUR\x10\x33\x12K\nGSHIFT_TEMPLATE_ACTIVITY_PLACEMENT_MIN_MAX_MUST_BE_MULTIPLE_OF_5_MINUTES\x10\x34\x12L\nHNO_SHIFT_TEMPLATE_ACTIVITY_PLACEMENT_SEQUENCES_MATCH_SHIFT_MIN_MAX_WIDTH\x10\x35\x12\x18\n\x14INVALID_TOUR_PATTERN\x10\x36\x12!\n\x1dINVALID_TOUR_AGENT_COLLECTION\x10\x37\x12&\n\"INVALID_TOUR_SHIFT_INSTANCE_CONFIG\x10\x38\x12%\n!INVALID_TOUR_SHIFT_SEGMENT_CONFIG\x10\x39\x12%\n!TOUR_SHIFT_SEGMENT_CONFIG_OVERLAP\x10:\x12*\n&TOUR_SHIFT_SEGMENT_CONFIG_DOES_NOT_FIT\x10;\x12&\n\"TOUR_SHIFT_INSTANCE_CONFIG_OVERLAP\x10<\x12\x39\n5WEEK_PATTERN_NUMBERS_NOT_UNIQUE_IN_TOUR_WEEK_PATTERNS\x10=\x12\x37\n3WFM_AGENT_SIDS_NOT_UNIQUE_IN_TOUR_AGENT_COLLECTIONS\x10>\x12\x42\n>FIST_WEEK_PATTERN_NUMBERS_NOT_UNIQUE_IN_TOUR_AGENT_COLLECTIONS\x10?\x12>\n:FIRST_WEEK_PATTERN_NUMBERS_NOT_FOUND_IN_TOUR_WEEK_PATTERNS\x10@\x12<\n8SHIFT_TEMPLATE_HAS_NO_ASSOCIATED_SCHEDULING_AGENT_GROUPS\x10\x41\x12\x36\n2ATTEMPT_TO_BUILD_SCHEDULES_FOR_INVALID_PARENT_NODE\x10\x42\x12\x33\n/SCHEDULABLE_AGENTS_DO_NOT_MEET_TEMPLATE_MINIMUM\x10\x43\x12\x33\n/SCHEDULABLE_AGENTS_DO_NOT_MEET_TEMPLATE_MAXIMUM\x10\x44\x12-\n)NO_OPEN_TIMES_SET_OR_INHERITED_BY_PROGRAM\x10\x45\x12\x32\n.TOUR_AGENT_COLLECTIONS_NEEDED_TO_SCHEDULE_TOUR\x10\x46*\xca\x01\n\x15PerformanceMetricType\x12#\n\x1f\x46TE_REQUIRED_VS_ACHIEVED_SIMPLE\x10\x00\x12%\n!FTE_REQUIRED_VS_ACHIEVED_EXTENDED\x10\x01\x12\x1a\n\x16SERVICE_LEVEL_ANALYSIS\x10\x02\x12\x18\n\x14SERVICE_LEVEL_MATRIX\x10\x03\x12\x1c\n\x18\x43ONTACT_HANDLING_METRICS\x10\x04\x12\x11\n\rLOAD_FORECAST\x10\x05*|\n\x15ScheduleShouldInclude\x12\x18\n\x14ONLY_SHIFT_INSTANCES\x10\x00\x12\x1c\n\x18ONLY_PERFORMANCE_METRICS\x10\x01\x12+\n\'SHIFT_INSTANCES_AND_PERFORMANCE_METRICS\x10\x02*(\n\x0cScheduleType\x12\t\n\x05\x44RAFT\x10\x00\x12\r\n\tPUBLISHED\x10\x01*7\n\x14SchedulingTargetType\x12\x0c\n\x08\x43OVERAGE\x10\x00\x12\x11\n\rSERVICE_LEVEL\x10\x01*F\n\nBitmapType\x12\x0c\n\x08\x43OMPLETE\x10\x00\x12\x11\n\rONLY_WEEKMAPS\x10\x01\x12\x17\n\x13ONLY_CALENDAR_ITEMS\x10\x02*Z\n\x11HistoryCacheState\x12\x0e\n\nNOT_LOADED\x10\x00\x12\x0b\n\x07LOADING\x10\x01\x12\x14\n\x10LOADING_COMPLETE\x10\x02\x12\x12\n\x0eLOADING_FAILED\x10\x03*S\n\x11InitialSetupState\x12\r\n\tNOT_SETUP\x10\x00\x12\x0e\n\nSETTING_UP\x10\x01\x12\x12\n\x0eSETUP_COMPLETE\x10\x02\x12\x0b\n\x07\x46\x41ILURE\x10\x03*\xb3\x01\n\x17RealTimeManagementState\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\r\n\tLOGGED_IN\x10\x01\x12\x10\n\x0c\x43\x41LL_ON_HOLD\x10\x04\x12\x11\n\rOUTBOUND_CALL\x10\x05\x12\x0c\n\x08TRANSFER\x10\x07\x12\x0e\n\nCONFERENCE\x10\x08\x12\t\n\x05READY\x10\t\x12\r\n\tNOT_READY\x10\n\x12\x0b\n\x07WRAP_UP\x10\x0b\x12\x0e\n\nLOGGED_OUT\x10\r*\x95\x01\n\x18\x41gentLeavePetitionStatus\x12\x1f\n\x1bUNSPECIFIED_PETITION_STATUS\x10\x00\x12\x14\n\x10PENDING_PETITION\x10\x01\x12\x15\n\x11\x41PPROVED_PETITION\x10\x02\x12\x13\n\x0f\x44\x45NIED_PETITION\x10\x03\x12\x16\n\x12\x43\x41NCELLED_PETITION\x10\x04*\x87\x01\n SchedulingActivityClassification\x12 \n\x1cSTANDARD_SCHEDULING_ACTIVITY\x10\x00\x12\x14\n\x10ON_CALL_ACTIVITY\x10\x01\x12\x15\n\x11TIME_OFF_ACTIVITY\x10\x02\x12\x14\n\x10MEETING_ACTIVITY\x10\x03*\x82\x01\n\x1f\x41\x64herenceRuleNotificationMedium\x12\x31\n-ADHERENCE_RULE_NOTIFICATION_MEDIUM_IN_PRODUCT\x10\x00\x12,\n(ADHERENCE_RULE_NOTIFICATION_MEDIUM_EMAIL\x10\x01*\xa9\x01\n\x1c\x41\x64herenceRuleRequirementType\x12,\n(ADHERENCE_RULE_REQUIREMENT_TYPE_NOT_USED\x10\x00\x12,\n(ADHERENCE_RULE_REQUIREMENT_TYPE_OPTIONAL\x10\x01\x12-\n)ADHERENCE_RULE_REQUIREMENT_TYPE_MANDATORY\x10\x02*\xde\x01\n\x12\x41\x64herenceRuleRange\x12%\n!ADHERENCE_RULE_RANGE_START_OF_DAY\x10\x00\x12&\n\"ADHERENCE_RULE_RANGE_START_OF_WEEK\x10\x01\x12\'\n#ADHERENCE_RULE_RANGE_START_OF_MONTH\x10\x02\x12$\n ADHERENCE_RULE_RANGE_REST_OF_DAY\x10\x03\x12*\n&ADHERENCE_RULE_RANGE_CUSTOM_DATE_RANGE\x10\x04*a\n#AdherenceDepartmentalRuleActionType\x12:\n6ADHERENCE_DEPARTMENTAL_RULE_ACTION_TYPE_CALLS_ANSWERED\x10\x00*\xca\x01\n\x16\x41\x64herenceRuleCondition\x12)\n%ADHERENCE_RULE_CONDITION_GREATER_THAN\x10\x00\x12/\n+ADHERENCE_RULE_CONDITION_GREATER_THAN_EQUAL\x10\x01\x12&\n\"ADHERENCE_RULE_CONDITION_LESS_THAN\x10\x02\x12,\n(ADHERENCE_RULE_CONDITION_LESS_THAN_EQUAL\x10\x03*\x98\x01\n\x11\x41\x64herenceRuleUnit\x12\x1f\n\x1b\x41\x44HERENCE_RULE_UNIT_SECONDS\x10\x00\x12\x1f\n\x1b\x41\x44HERENCE_RULE_UNIT_MINUTES\x10\x01\x12\x1d\n\x19\x41\x44HERENCE_RULE_UNIT_CALLS\x10\x02\x12\"\n\x1e\x41\x44HERENCE_RULE_UNIT_PERCENTAGE\x10\x03*\x8d\x04\n\x1c\x41\x64herenceAgentRuleActionType\x12,\n(ADHERENCE_AGENT_RULE_ACTION_TYPE_WRAP_UP\x10\x00\x12,\n(ADHERENCE_AGENT_RULE_ACTION_TYPE_WAITING\x10\x01\x12\x30\n,ADHERENCE_AGENT_RULE_ACTION_TYPE_MANUAL_DIAL\x10\x02\x12\x31\n-ADHERENCE_AGENT_RULE_ACTION_TYPE_PREVIEW_DIAL\x10\x03\x12\x31\n-ADHERENCE_AGENT_RULE_ACTION_TYPE_ANSWER_CALLS\x10\x04\x12,\n(ADHERENCE_AGENT_RULE_ACTION_TYPE_ON_CALL\x10\x05\x12,\n(ADHERENCE_AGENT_RULE_ACTION_TYPE_ON_HOLD\x10\x06\x12\x30\n,ADHERENCE_AGENT_RULE_ACTION_TYPE_SHIFT_START\x10\x07\x12\x35\n1ADHERENCE_AGENT_RULE_ACTION_TYPE_SHIFT_START_LATE\x10\x08\x12\x34\n0ADHERENCE_AGENT_RULE_ACTION_TYPE_SHIFT_END_EARLY\x10\tBh\n\x0f\x63om.api.commonsB\x08WfmProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.wfm_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\010WfmProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_SKILLPROFILECATEGORY'].fields_by_name['skill_profile_category_sid']._loaded_options = None
  _globals['_SKILLPROFILECATEGORY'].fields_by_name['skill_profile_category_sid']._serialized_options = b'0\001'
  _globals['_AGENTSTATESEGMENT'].fields_by_name['width_in_minutes']._loaded_options = None
  _globals['_AGENTSTATESEGMENT'].fields_by_name['width_in_minutes']._serialized_options = b'\030\001'
  _globals['_CONFIGENTITY'].fields_by_name['entity_sid']._loaded_options = None
  _globals['_CONFIGENTITY'].fields_by_name['entity_sid']._serialized_options = b'0\001'
  _globals['_ADHERENCERULENOTIFICATIONCONFIG'].fields_by_name['adherence_rule_notification_config_id']._loaded_options = None
  _globals['_ADHERENCERULENOTIFICATIONCONFIG'].fields_by_name['adherence_rule_notification_config_id']._serialized_options = b'0\001'
  _globals['_ADHERENCERULENOTIFICATIONCONFIGENTRY'].fields_by_name['adherence_rule_notification_config_entry_id']._loaded_options = None
  _globals['_ADHERENCERULENOTIFICATIONCONFIGENTRY'].fields_by_name['adherence_rule_notification_config_entry_id']._serialized_options = b'0\001'
  _globals['_ADHERENCERULENOTIFICATIONCONFIGENTRY'].fields_by_name['adherence_rule_notification_config_id']._loaded_options = None
  _globals['_ADHERENCERULENOTIFICATIONCONFIGENTRY'].fields_by_name['adherence_rule_notification_config_id']._serialized_options = b'0\001'
  _globals['_ADHERENCEDEPARTMENTALRULE'].fields_by_name['adherence_departmental_rule_id']._loaded_options = None
  _globals['_ADHERENCEDEPARTMENTALRULE'].fields_by_name['adherence_departmental_rule_id']._serialized_options = b'0\001'
  _globals['_ADHERENCEDEPARTMENTALRULE'].fields_by_name['adherence_rule_notification_config_id']._loaded_options = None
  _globals['_ADHERENCEDEPARTMENTALRULE'].fields_by_name['adherence_rule_notification_config_id']._serialized_options = b'0\001'
  _globals['_ADHERENCEDEPARTMENTALRULECLAUSE'].fields_by_name['adherence_departmental_rule_clause_id']._loaded_options = None
  _globals['_ADHERENCEDEPARTMENTALRULECLAUSE'].fields_by_name['adherence_departmental_rule_clause_id']._serialized_options = b'0\001'
  _globals['_ADHERENCEDEPARTMENTALRULECLAUSE'].fields_by_name['adherence_departmental_rule_id']._loaded_options = None
  _globals['_ADHERENCEDEPARTMENTALRULECLAUSE'].fields_by_name['adherence_departmental_rule_id']._serialized_options = b'0\001'
  _globals['_ADHERENCEAGENTRULE'].fields_by_name['adherence_agent_rule_id']._loaded_options = None
  _globals['_ADHERENCEAGENTRULE'].fields_by_name['adherence_agent_rule_id']._serialized_options = b'0\001'
  _globals['_ADHERENCEAGENTRULE'].fields_by_name['adherence_rule_notification_config_id']._loaded_options = None
  _globals['_ADHERENCEAGENTRULE'].fields_by_name['adherence_rule_notification_config_id']._serialized_options = b'0\001'
  _globals['_ADHERENCEAGENTRULECLAUSE'].fields_by_name['adherence_agent_rule_clause_id']._loaded_options = None
  _globals['_ADHERENCEAGENTRULECLAUSE'].fields_by_name['adherence_agent_rule_clause_id']._serialized_options = b'0\001'
  _globals['_ADHERENCEAGENTRULECLAUSE'].fields_by_name['adherence_agent_rule_id']._loaded_options = None
  _globals['_ADHERENCEAGENTRULECLAUSE'].fields_by_name['adherence_agent_rule_id']._serialized_options = b'0\001'
  _globals['_REGRESSIONFORECASTERMODELTYPES']._serialized_start=8277
  _globals['_REGRESSIONFORECASTERMODELTYPES']._serialized_end=8445
  _globals['_REGRESSIONFORECASTERAVGSPROCESSINGTYPE']._serialized_start=8447
  _globals['_REGRESSIONFORECASTERAVGSPROCESSINGTYPE']._serialized_end=8535
  _globals['_CONSTRAINTTIMEUNIT']._serialized_start=8537
  _globals['_CONSTRAINTTIMEUNIT']._serialized_end=8637
  _globals['_CONFIGENTITYTYPE']._serialized_start=8640
  _globals['_CONFIGENTITYTYPE']._serialized_end=9104
  _globals['_CONSTRAINTRULETYPE']._serialized_start=9107
  _globals['_CONSTRAINTRULETYPE']._serialized_end=9300
  _globals['_DOWPLACEMENTTYPE']._serialized_start=9302
  _globals['_DOWPLACEMENTTYPE']._serialized_end=9353
  _globals['_OPENTIMESOPTION']._serialized_start=9355
  _globals['_OPENTIMESOPTION']._serialized_end=9394
  _globals['_AVAILABILITYOPTION']._serialized_start=9396
  _globals['_AVAILABILITYOPTION']._serialized_end=9476
  _globals['_DAYOFWEEK']._serialized_start=9478
  _globals['_DAYOFWEEK']._serialized_end=9552
  _globals['_CONFIGRELATIONSHIPTYPE']._serialized_start=9554
  _globals['_CONFIGRELATIONSHIPTYPE']._serialized_end=9648
  _globals['_DIAGNOSTICLEVEL']._serialized_start=9650
  _globals['_DIAGNOSTICLEVEL']._serialized_end=9755
  _globals['_DIAGNOSTICCODE']._serialized_start=9758
  _globals['_DIAGNOSTICCODE']._serialized_end=12933
  _globals['_PERFORMANCEMETRICTYPE']._serialized_start=12936
  _globals['_PERFORMANCEMETRICTYPE']._serialized_end=13138
  _globals['_SCHEDULESHOULDINCLUDE']._serialized_start=13140
  _globals['_SCHEDULESHOULDINCLUDE']._serialized_end=13264
  _globals['_SCHEDULETYPE']._serialized_start=13266
  _globals['_SCHEDULETYPE']._serialized_end=13306
  _globals['_SCHEDULINGTARGETTYPE']._serialized_start=13308
  _globals['_SCHEDULINGTARGETTYPE']._serialized_end=13363
  _globals['_BITMAPTYPE']._serialized_start=13365
  _globals['_BITMAPTYPE']._serialized_end=13435
  _globals['_HISTORYCACHESTATE']._serialized_start=13437
  _globals['_HISTORYCACHESTATE']._serialized_end=13527
  _globals['_INITIALSETUPSTATE']._serialized_start=13529
  _globals['_INITIALSETUPSTATE']._serialized_end=13612
  _globals['_REALTIMEMANAGEMENTSTATE']._serialized_start=13615
  _globals['_REALTIMEMANAGEMENTSTATE']._serialized_end=13794
  _globals['_AGENTLEAVEPETITIONSTATUS']._serialized_start=13797
  _globals['_AGENTLEAVEPETITIONSTATUS']._serialized_end=13946
  _globals['_SCHEDULINGACTIVITYCLASSIFICATION']._serialized_start=13949
  _globals['_SCHEDULINGACTIVITYCLASSIFICATION']._serialized_end=14084
  _globals['_ADHERENCERULENOTIFICATIONMEDIUM']._serialized_start=14087
  _globals['_ADHERENCERULENOTIFICATIONMEDIUM']._serialized_end=14217
  _globals['_ADHERENCERULEREQUIREMENTTYPE']._serialized_start=14220
  _globals['_ADHERENCERULEREQUIREMENTTYPE']._serialized_end=14389
  _globals['_ADHERENCERULERANGE']._serialized_start=14392
  _globals['_ADHERENCERULERANGE']._serialized_end=14614
  _globals['_ADHERENCEDEPARTMENTALRULEACTIONTYPE']._serialized_start=14616
  _globals['_ADHERENCEDEPARTMENTALRULEACTIONTYPE']._serialized_end=14713
  _globals['_ADHERENCERULECONDITION']._serialized_start=14716
  _globals['_ADHERENCERULECONDITION']._serialized_end=14918
  _globals['_ADHERENCERULEUNIT']._serialized_start=14921
  _globals['_ADHERENCERULEUNIT']._serialized_end=15073
  _globals['_ADHERENCEAGENTRULEACTIONTYPE']._serialized_start=15076
  _globals['_ADHERENCEAGENTRULEACTIONTYPE']._serialized_end=15601
  _globals['_SKILLTYPE']._serialized_start=103
  _globals['_SKILLTYPE']._serialized_end=210
  _globals['_SKILLTYPE_ENUM']._serialized_start=116
  _globals['_SKILLTYPE_ENUM']._serialized_end=210
  _globals['_DATETIMERANGE']._serialized_start=213
  _globals['_DATETIMERANGE']._serialized_end=358
  _globals['_FORECASTINGPARAMETERS']._serialized_start=361
  _globals['_FORECASTINGPARAMETERS']._serialized_end=1165
  _globals['_PROFILETOD']._serialized_start=1168
  _globals['_PROFILETOD']._serialized_end=1364
  _globals['_PROFILEWOMS']._serialized_start=1367
  _globals['_PROFILEWOMS']._serialized_end=1672
  _globals['_PROFILEDOW']._serialized_start=1675
  _globals['_PROFILEDOW']._serialized_end=1871
  _globals['_PROFILEMOY']._serialized_start=1874
  _globals['_PROFILEMOY']._serialized_end=2178
  _globals['_DISTRIBUTIONPROFILE']._serialized_start=2181
  _globals['_DISTRIBUTIONPROFILE']._serialized_end=2437
  _globals['_CALLPROFILEGROUPCALLS']._serialized_start=2440
  _globals['_CALLPROFILEGROUPCALLS']._serialized_end=2581
  _globals['_CALLPROFILEGROUPAVGS']._serialized_start=2584
  _globals['_CALLPROFILEGROUPAVGS']._serialized_end=2757
  _globals['_OPTIONTYPES']._serialized_start=2760
  _globals['_OPTIONTYPES']._serialized_end=2951
  _globals['_SCHEDULESELECTOR']._serialized_start=2953
  _globals['_SCHEDULESELECTOR']._serialized_end=3070
  _globals['_SKILLPROFILECATEGORY']._serialized_start=3073
  _globals['_SKILLPROFILECATEGORY']._serialized_end=3338
  _globals['_SKILLPROFILECATEGORY_CATEGORYTYPE']._serialized_start=3273
  _globals['_SKILLPROFILECATEGORY_CATEGORYTYPE']._serialized_end=3338
  _globals['_SCHEDULINGRESULTMETRICFORSKILLCOLLECTION']._serialized_start=3341
  _globals['_SCHEDULINGRESULTMETRICFORSKILLCOLLECTION']._serialized_end=3772
  _globals['_SCHEDULINGRESULTMETRIC']._serialized_start=3775
  _globals['_SCHEDULINGRESULTMETRIC']._serialized_end=4228
  _globals['_CLIENTHISTORYCACHEINFO']._serialized_start=4230
  _globals['_CLIENTHISTORYCACHEINFO']._serialized_end=4357
  _globals['_ERRORTRACE']._serialized_start=4359
  _globals['_ERRORTRACE']._serialized_end=4409
  _globals['_INITIALSETUPSTATUS']._serialized_start=4412
  _globals['_INITIALSETUPSTATUS']._serialized_end=4561
  _globals['_AGENTSTATESEGMENT']._serialized_start=4564
  _globals['_AGENTSTATESEGMENT']._serialized_end=4767
  _globals['_AGENTSTATESEQUENCE']._serialized_start=4770
  _globals['_AGENTSTATESEQUENCE']._serialized_end=4964
  _globals['_AGENTLEAVEPETITION']._serialized_start=4967
  _globals['_AGENTLEAVEPETITION']._serialized_end=5620
  _globals['_CONFIGENTITY']._serialized_start=5622
  _globals['_CONFIGENTITY']._serialized_end=5735
  _globals['_ADHERENCERULENOTIFICATIONCONFIG']._serialized_start=5738
  _globals['_ADHERENCERULENOTIFICATIONCONFIG']._serialized_end=5877
  _globals['_ADHERENCERULENOTIFICATIONCONFIGENTRY']._serialized_start=5880
  _globals['_ADHERENCERULENOTIFICATIONCONFIGENTRY']._serialized_end=6309
  _globals['_ADHERENCEDEPARTMENTALRULEACTION']._serialized_start=6311
  _globals['_ADHERENCEDEPARTMENTALRULEACTION']._serialized_end=6427
  _globals['_ADHERENCEDEPARTMENTALRULE']._serialized_start=6430
  _globals['_ADHERENCEDEPARTMENTALRULE']._serialized_end=6926
  _globals['_ADHERENCEDEPARTMENTALRULECLAUSE']._serialized_start=6929
  _globals['_ADHERENCEDEPARTMENTALRULECLAUSE']._serialized_end=7453
  _globals['_ADHERENCEAGENTRULE']._serialized_start=7456
  _globals['_ADHERENCEAGENTRULE']._serialized_end=7804
  _globals['_ADHERENCEAGENTRULEACTION']._serialized_start=7806
  _globals['_ADHERENCEAGENTRULEACTION']._serialized_end=7908
  _globals['_ADHERENCEAGENTRULECLAUSE']._serialized_start=7911
  _globals['_ADHERENCEAGENTRULECLAUSE']._serialized_end=8274
# @@protoc_insertion_point(module_scope)
