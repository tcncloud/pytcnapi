# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/compliance.proto
# Protobuf Python Version: 5.27.1
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
    1,
    '',
    'api/commons/compliance.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import communication_pb2 as api_dot_commons_dot_communication__pb2
from api.commons import enums_pb2 as api_dot_commons_dot_enums__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/commons/compliance.proto\x12\x0b\x61pi.commons\x1a\x1f\x61pi/commons/communication.proto\x1a\x17\x61pi/commons/enums.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\xe3\x01\n\x04Rule\x12%\n\x04verb\x18\x01 \x01(\x0e\x32\x11.api.commons.VerbR\x04verb\x12+\n\x06\x65ntity\x18\x02 \x01(\x0e\x32\x13.api.commons.EntityR\x06\x65ntity\x12\x35\n\nsub_entity\x18\x03 \x01(\x0e\x32\x16.api.commons.SubEntityR\tsubEntity\x12\x33\n\tselectors\x18\x04 \x03(\x0b\x32\x15.api.commons.SelectorR\tselectors\x12\x1b\n\trule_text\x18\x06 \x01(\tR\x08ruleText\"\xc5\x04\n\x08Selector\x12*\n\x04time\x18\x01 \x01(\x0b\x32\x14.api.commons.TimeExpH\x00R\x04time\x12-\n\x04week\x18\x02 \x01(\x0b\x32\x17.api.commons.WeekdayExpH\x00R\x04week\x12*\n\x04\x64ncl\x18\x03 \x01(\x0b\x32\x14.api.commons.DnclExpH\x00R\x04\x64ncl\x12\x39\n\tfrequency\x18\x04 \x01(\x0b\x32\x19.api.commons.FrequencyExpH\x00R\tfrequency\x12\x36\n\x08location\x18\x05 \x01(\x0b\x32\x18.api.commons.LocationExpH\x00R\x08location\x12:\n\nphone_type\x18\x06 \x01(\x0b\x32\x19.api.commons.PhoneTypeExpH\x00R\tphoneType\x12-\n\x05month\x18\x07 \x01(\x0b\x32\x15.api.commons.MonthExpH\x00R\x05month\x12*\n\x04\x64\x61te\x18\x08 \x01(\x0b\x32\x14.api.commons.DateExpH\x00R\x04\x64\x61te\x12\x33\n\x07holiday\x18\t \x01(\x0b\x32\x17.api.commons.HolidayExpH\x00R\x07holiday\x12/\n\x04meta\x18\n \x01(\x0b\x32\x19.api.commons.MetaFieldExpH\x00R\x04meta\x12\x30\n\x06plugin\x18\x0b \x01(\x0b\x32\x16.api.commons.PluginExpH\x00R\x06pluginB\x10\n\x0eselection_rule\"C\n\x07TimeExp\x12\x1d\n\nstart_hour\x18\x01 \x01(\tR\tstartHour\x12\x19\n\x08\x65nd_hour\x18\x02 \x01(\tR\x07\x65ndHour\"M\n\nWeekdayExp\x12+\n\x03\x64\x61y\x18\x01 \x01(\x0e\x32\x19.api.commons.Weekday.EnumR\x03\x64\x61y\x12\x12\n\x04text\x18\x02 \x01(\tR\x04text\"c\n\x07\x44nclExp\x12\x1b\n\tlist_name\x18\x01 \x01(\tR\x08listName\x12;\n\x0b\x66ield_names\x18\x02 \x01(\x0b\x32\x1a.api.commons.FieldNamesModR\nfieldNames\"\xec\x02\n\x0c\x46requencyExp\x12\x14\n\x05\x63ount\x18\x01 \x01(\x03R\x05\x63ount\x12\x1a\n\x08\x64uration\x18\x02 \x01(\x03R\x08\x64uration\x12\x31\n\x07results\x18\x03 \x01(\x0b\x32\x17.api.commons.ResultsModR\x07results\x12?\n\x0c\x64ispositions\x18\x04 \x01(\x0b\x32\x1b.api.commons.DispositionModR\x0c\x64ispositions\x12;\n\x0b\x66ield_names\x18\x05 \x01(\x0b\x32\x1a.api.commons.FieldNamesModR\nfieldNames\x12\x43\n\x11\x63hecking_entities\x18\x06 \x03(\x0b\x32\x16.api.commons.EntityExpR\x10\x63heckingEntities\x12\x34\n\x08matching\x18\x07 \x01(\x0b\x32\x18.api.commons.MatchingModR\x08matching\"\x92\x01\n\x0bMatchingMod\x12*\n\x03\x61nd\x18\x01 \x03(\x0b\x32\x18.api.commons.MatchingModR\x03\x61nd\x12(\n\x02or\x18\x02 \x03(\x0b\x32\x18.api.commons.MatchingModR\x02or\x12-\n\x03mod\x18\x03 \x01(\x0b\x32\x1b.api.commons.MatchingEntityR\x03mod\"\x92\x01\n\x0eMatchingEntity\x12\x33\n\x07results\x18\x01 \x01(\x0b\x32\x17.api.commons.ResultsModH\x00R\x07results\x12\x41\n\x0c\x64ispositions\x18\x02 \x01(\x0b\x32\x1b.api.commons.DispositionModH\x00R\x0c\x64ispositionsB\x08\n\x06\x65ntity\"\xc7\x01\n\x0bLocationExp\x12\x18\n\x07\x63ountry\x18\x01 \x01(\tR\x07\x63ountry\x12\x14\n\x05state\x18\x02 \x01(\tR\x05state\x12\x16\n\x06\x63ounty\x18\x03 \x01(\tR\x06\x63ounty\x12\x12\n\x04\x63ity\x18\x04 \x01(\tR\x04\x63ity\x12\x1a\n\x08province\x18\x05 \x01(\tR\x08province\x12!\n\x0cpostal_codes\x18\x06 \x03(\tR\x0bpostalCodes\x12\x1d\n\narea_codes\x18\x07 \x03(\tR\tareaCodes\"E\n\x0cPhoneTypeExp\x12\x35\n\nphone_type\x18\x01 \x01(\x0e\x32\x16.api.commons.PhoneTypeR\tphoneType\"H\n\x08MonthExp\x12(\n\x05month\x18\x01 \x01(\x0e\x32\x12.api.commons.MonthR\x05month\x12\x12\n\x04text\x18\x02 \x01(\tR\x04text\"Y\n\x07\x44\x61teExp\x12(\n\x05month\x18\x01 \x01(\x0e\x32\x12.api.commons.MonthR\x05month\x12\x10\n\x03\x64\x61y\x18\x02 \x01(\x03R\x03\x64\x61y\x12\x12\n\x04year\x18\x03 \x01(\x03R\x04year\"N\n\nHolidayExp\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x18\n\x07\x63ountry\x18\x02 \x01(\tR\x07\x63ountry\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\"$\n\x0cMetaFieldExp\x12\x14\n\x05\x66ield\x18\x01 \x01(\tR\x05\x66ield\"\x93\x04\n\tPluginExp\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x17.api.commons.PluginTypeR\x04type\x12\x1d\n\ntcn_strict\x18\x04 \x01(\x08R\ttcnStrict\x12\x1d\n\nlicense_id\x18\x02 \x01(\tR\tlicenseId\x12#\n\rreference_key\x18\x03 \x01(\tR\x0creferenceKey\x12\x1f\n\x0b\x66rom_number\x18\x05 \x01(\tR\nfromNumber\x12*\n\x03\x65nv\x18\x06 \x01(\x0e\x32\x18.api.commons.EnvironmentR\x03\x65nv\x12!\n\x0cprofile_name\x18\x07 \x01(\tR\x0bprofileName\x12#\n\rcontent_field\x18\x08 \x01(\tR\x0c\x63ontentField\x12\x14\n\x05topic\x18\t \x01(\tR\x05topic\x12\x45\n\rabsent_action\x18\x0b \x01(\x0e\x32 .api.commons.ConsentAbsentActionR\x0c\x61\x62sentAction\x12*\n\x11\x64\x61te_last_contact\x18\n \x01(\tR\x0f\x64\x61teLastContact\x12\x0e\n\x02lu\x18\x0c \x01(\tR\x02lu\x12\x18\n\x07\x61\x63\x63ount\x18\r \x01(\tR\x07\x61\x63\x63ount\x12\x16\n\x06master\x18\x0e \x01(\tR\x06master\x12\x16\n\x06\x63lient\x18\x0f \x01(\tR\x06\x63lient\"o\n\tEntityExp\x12\x35\n\nsub_entity\x18\x01 \x01(\x0e\x32\x16.api.commons.SubEntityR\tsubEntity\x12+\n\x06\x65ntity\x18\x02 \x01(\x0e\x32\x13.api.commons.EntityR\x06\x65ntity\"D\n\rFieldNamesMod\x12\x33\n\x0b\x66ield_names\x18\x01 \x03(\x0b\x32\x12.api.commons.FieldR\nfieldNames\"&\n\nResultsMod\x12\x18\n\x07results\x18\x01 \x03(\tR\x07results\"S\n\x0e\x44ispositionMod\x12\x41\n\x0c\x64ispositions\x18\x01 \x03(\x0b\x32\x1d.api.commons.DispositionFieldR\x0c\x64ispositions\"n\n\x10\x44ispositionField\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x32\n\x05pairs\x18\x03 \x03(\x0b\x32\x1c.api.commons.DispositionPairR\x05pairs\"9\n\x0f\x44ispositionPair\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"7\n\x05\x46ield\x12\x14\n\x05\x46ield\x18\x01 \x01(\tR\x05\x46ield\x12\x18\n\x07\x43ontent\x18\x02 \x01(\tR\x07\x43ontent\"\xe3\x02\n\x10\x43onsentCondition\x12\x30\n\x14\x63onsent_condition_id\x18\x01 \x01(\x03R\x12\x63onsentConditionId\x12\x1d\n\nconsent_id\x18\x02 \x01(\x03R\tconsentId\x12\x42\n\x10\x64\x61ys_of_the_week\x18\n \x03(\x0e\x32\x19.api.commons.Weekday.EnumR\rdaysOfTheWeek\x12\'\n\x10time_of_day_from\x18\x0b \x01(\tR\rtimeOfDayFrom\x12#\n\x0etime_of_day_to\x18\x0c \x01(\tR\x0btimeOfDayTo\x12\x37\n\tfrom_date\x18\r \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08\x66romDate\x12\x33\n\x07to_date\x18\x0e \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x06toDate\"\x9a\x06\n\x0cScenarioData\x12\x32\n\tcomm_type\x18\x01 \x01(\x0b\x32\x15.api.commons.CommTypeR\x08\x63ommType\x12!\n\x0cphone_number\x18\x02 \x01(\tR\x0bphoneNumber\x12%\n\x0c\x63ountry_code\x18\x03 \x01(\tB\x02\x18\x01R\x0b\x63ountryCode\x12\x14\n\x05\x65mail\x18\x04 \x01(\tR\x05\x65mail\x12P\n\rcall_metadata\x18\x05 \x03(\x0b\x32+.api.commons.ScenarioData.CallMetadataEntryR\x0c\x63\x61llMetadata\x12<\n\x0ctime_of_call\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ntimeOfCall\x12\'\n\x0f\x66requency_count\x18\x07 \x01(\x03R\x0e\x66requencyCount\x12-\n\x12\x66requency_duration\x18\x08 \x01(\x03R\x11\x66requencyDuration\x12\x1f\n\x0b\x64ncl_blocks\x18\t \x01(\x08R\ndnclBlocks\x12\x18\n\x07\x63ountry\x18\n \x01(\tR\x07\x63ountry\x12\x14\n\x05state\x18\x0b \x01(\tR\x05state\x12\x16\n\x06\x63ounty\x18\x0c \x01(\tR\x06\x63ounty\x12\x12\n\x04\x63ity\x18\r \x01(\tR\x04\x63ity\x12\x1a\n\x08province\x18\x0e \x01(\tR\x08province\x12\x35\n\nphone_type\x18\x0f \x01(\x0e\x32\x16.api.commons.PhoneTypeR\tphoneType\x12\x1b\n\ttime_zone\x18\x10 \x01(\tR\x08timeZone\x12\x1a\n\x08holidays\x18\x11 \x03(\tR\x08holidays\x12\x44\n\x11\x63ountry_code_data\x18\x12 \x01(\x0b\x32\x18.api.commons.CountryCodeR\x0f\x63ountryCodeData\x1a?\n\x11\x43\x61llMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"r\n\x0b\x43ountryCode\x12!\n\x0c\x63ountry_code\x18\x01 \x01(\x03R\x0b\x63ountryCode\x12!\n\x0c\x63ountry_name\x18\x02 \x01(\tR\x0b\x63ountryName\x12\x1d\n\ncountry_id\x18\x03 \x01(\tR\tcountryId\"\x8e\x02\n\x0eScenarioResult\x12!\n\x0cpassed_value\x18\x05 \x01(\x08R\x0bpassedValue\x12W\n\x16should_allow_responses\x18\x02 \x03(\x0b\x32!.api.commons.ScenarioRuleResponseR\x14shouldAllowResponses\x12U\n\x15should_deny_responses\x18\x03 \x03(\x0b\x32!.api.commons.ScenarioRuleResponseR\x13shouldDenyResponses\x12#\n\rscenario_name\x18\x04 \x01(\tR\x0cscenarioNameJ\x04\x08\x01\x10\x02\"\\\n\x14ScenarioRuleResponse\x12\x1b\n\trule_text\x18\x01 \x01(\tR\x08ruleText\x12!\n\x0cpermit_value\x18\x03 \x01(\x08R\x0bpermitValueJ\x04\x08\x02\x10\x03\"\xa6\x01\n\x11ScrubEntryDetails\x12\x18\n\x07\x63ontent\x18\x01 \x01(\tR\x07\x63ontent\x12\x43\n\x0f\x65xpiration_date\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0e\x65xpirationDate\x12\x32\n\x05notes\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x05notes\"l\n\x0cRuleResponse\x12\x1b\n\trule_text\x18\x01 \x01(\tR\x08ruleText\x12\x16\n\x06permit\x18\x02 \x01(\x08R\x06permit\x12\'\n\x0fplugin_response\x18\x03 \x01(\tR\x0epluginResponse*K\n\x04Verb\x12\r\n\tV_UNKNOWN\x10\x00\x12\x0b\n\x07V_ALLOW\x10\x01\x12\n\n\x06V_DENY\x10\x02\x12\x0b\n\x07V_SCRUB\x10\x03\x12\x0e\n\nV_OVERRIDE\x10\x04*K\n\x06\x45ntity\x12\r\n\tE_UNKNOWN\x10\x00\x12\n\n\x06\x45_CALL\x10\x01\x12\x0b\n\x07\x45_EMAIL\x10\x02\x12\t\n\x05\x45_SMS\x10\x03\x12\x0e\n\nE_WHATSAPP\x10\x04*u\n\tSubEntity\x12\n\n\x06SE_ALL\x10\x00\x12\x0e\n\nSE_INBOUND\x10\x01\x12\x0f\n\x0bSE_OUTBOUND\x10\x02\x12\r\n\tSE_MANUAL\x10\x03\x12\x0e\n\nSE_PREVIEW\x10\x04\x12\n\n\x06SE_MAC\x10\x05\x12\x10\n\x0cSE_BROADCAST\x10\x06*.\n\tPhoneType\x12\x08\n\x04\x43\x45LL\x10\x00\x12\x08\n\x04LAND\x10\x01\x12\r\n\tTOLL_FREE\x10\x02*r\n\x0b\x43ontentType\x12\x13\n\x0f\x43T_PHONE_NUMBER\x10\x00\x12\x0c\n\x08\x43T_EMAIL\x10\x01\x12\n\n\x06\x43T_SMS\x10\x02\x12\x0c\n\x08\x43T_OTHER\x10\x03\x12\x15\n\x11\x43T_ACCOUNT_NUMBER\x10\x04\x12\x0f\n\x0b\x43T_WHATSAPP\x10\x05*U\n\x07\x43hannel\x12\x10\n\x0c\x43HANNEL_CALL\x10\x00\x12\x11\n\rCHANNEL_EMAIL\x10\x01\x12\x0f\n\x0b\x43HANNEL_SMS\x10\x02\x12\x14\n\x10\x43HANNEL_WHATSAPP\x10\x03*[\n\nPluginType\x12\x12\n\x0eUNKNOWN_PLUGIN\x10\x00\x12\x0b\n\x07GRYPHON\x10\x01\x12\x0f\n\x0bTCN_CONSENT\x10\x02\x12\x07\n\x03RND\x10\x03\x12\x12\n\x0eMRS_COMPLIANCE\x10\x04*8\n\x0b\x45nvironment\x12\x0f\n\x0bINVALID_ENV\x10\x00\x12\x08\n\x04TEST\x10\x01\x12\x0e\n\nPRODUCTION\x10\x02*V\n\x13\x43onsentAbsentAction\x12\x1f\n\x1b\x43ONSENT_ABSENT_ACTION_ALLOW\x10\x00\x12\x1e\n\x1a\x43ONSENT_ABSENT_ACTION_DENY\x10\x01\x42o\n\x0f\x63om.api.commonsB\x0f\x43omplianceProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.compliance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\017ComplianceProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_SCENARIODATA_CALLMETADATAENTRY']._loaded_options = None
  _globals['_SCENARIODATA_CALLMETADATAENTRY']._serialized_options = b'8\001'
  _globals['_SCENARIODATA'].fields_by_name['country_code']._loaded_options = None
  _globals['_SCENARIODATA'].fields_by_name['country_code']._serialized_options = b'\030\001'
  _globals['_VERB']._serialized_start=5439
  _globals['_VERB']._serialized_end=5514
  _globals['_ENTITY']._serialized_start=5516
  _globals['_ENTITY']._serialized_end=5591
  _globals['_SUBENTITY']._serialized_start=5593
  _globals['_SUBENTITY']._serialized_end=5710
  _globals['_PHONETYPE']._serialized_start=5712
  _globals['_PHONETYPE']._serialized_end=5758
  _globals['_CONTENTTYPE']._serialized_start=5760
  _globals['_CONTENTTYPE']._serialized_end=5874
  _globals['_CHANNEL']._serialized_start=5876
  _globals['_CHANNEL']._serialized_end=5961
  _globals['_PLUGINTYPE']._serialized_start=5963
  _globals['_PLUGINTYPE']._serialized_end=6054
  _globals['_ENVIRONMENT']._serialized_start=6056
  _globals['_ENVIRONMENT']._serialized_end=6112
  _globals['_CONSENTABSENTACTION']._serialized_start=6114
  _globals['_CONSENTABSENTACTION']._serialized_end=6200
  _globals['_RULE']._serialized_start=169
  _globals['_RULE']._serialized_end=396
  _globals['_SELECTOR']._serialized_start=399
  _globals['_SELECTOR']._serialized_end=980
  _globals['_TIMEEXP']._serialized_start=982
  _globals['_TIMEEXP']._serialized_end=1049
  _globals['_WEEKDAYEXP']._serialized_start=1051
  _globals['_WEEKDAYEXP']._serialized_end=1128
  _globals['_DNCLEXP']._serialized_start=1130
  _globals['_DNCLEXP']._serialized_end=1229
  _globals['_FREQUENCYEXP']._serialized_start=1232
  _globals['_FREQUENCYEXP']._serialized_end=1596
  _globals['_MATCHINGMOD']._serialized_start=1599
  _globals['_MATCHINGMOD']._serialized_end=1745
  _globals['_MATCHINGENTITY']._serialized_start=1748
  _globals['_MATCHINGENTITY']._serialized_end=1894
  _globals['_LOCATIONEXP']._serialized_start=1897
  _globals['_LOCATIONEXP']._serialized_end=2096
  _globals['_PHONETYPEEXP']._serialized_start=2098
  _globals['_PHONETYPEEXP']._serialized_end=2167
  _globals['_MONTHEXP']._serialized_start=2169
  _globals['_MONTHEXP']._serialized_end=2241
  _globals['_DATEEXP']._serialized_start=2243
  _globals['_DATEEXP']._serialized_end=2332
  _globals['_HOLIDAYEXP']._serialized_start=2334
  _globals['_HOLIDAYEXP']._serialized_end=2412
  _globals['_METAFIELDEXP']._serialized_start=2414
  _globals['_METAFIELDEXP']._serialized_end=2450
  _globals['_PLUGINEXP']._serialized_start=2453
  _globals['_PLUGINEXP']._serialized_end=2984
  _globals['_ENTITYEXP']._serialized_start=2986
  _globals['_ENTITYEXP']._serialized_end=3097
  _globals['_FIELDNAMESMOD']._serialized_start=3099
  _globals['_FIELDNAMESMOD']._serialized_end=3167
  _globals['_RESULTSMOD']._serialized_start=3169
  _globals['_RESULTSMOD']._serialized_end=3207
  _globals['_DISPOSITIONMOD']._serialized_start=3209
  _globals['_DISPOSITIONMOD']._serialized_end=3292
  _globals['_DISPOSITIONFIELD']._serialized_start=3294
  _globals['_DISPOSITIONFIELD']._serialized_end=3404
  _globals['_DISPOSITIONPAIR']._serialized_start=3406
  _globals['_DISPOSITIONPAIR']._serialized_end=3463
  _globals['_FIELD']._serialized_start=3465
  _globals['_FIELD']._serialized_end=3520
  _globals['_CONSENTCONDITION']._serialized_start=3523
  _globals['_CONSENTCONDITION']._serialized_end=3878
  _globals['_SCENARIODATA']._serialized_start=3881
  _globals['_SCENARIODATA']._serialized_end=4675
  _globals['_SCENARIODATA_CALLMETADATAENTRY']._serialized_start=4612
  _globals['_SCENARIODATA_CALLMETADATAENTRY']._serialized_end=4675
  _globals['_COUNTRYCODE']._serialized_start=4677
  _globals['_COUNTRYCODE']._serialized_end=4791
  _globals['_SCENARIORESULT']._serialized_start=4794
  _globals['_SCENARIORESULT']._serialized_end=5064
  _globals['_SCENARIORULERESPONSE']._serialized_start=5066
  _globals['_SCENARIORULERESPONSE']._serialized_end=5158
  _globals['_SCRUBENTRYDETAILS']._serialized_start=5161
  _globals['_SCRUBENTRYDETAILS']._serialized_end=5327
  _globals['_RULERESPONSE']._serialized_start=5329
  _globals['_RULERESPONSE']._serialized_end=5437
# @@protoc_insertion_point(module_scope)
