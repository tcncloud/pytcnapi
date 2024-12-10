# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/org_preferences.proto
# Protobuf Python Version: 5.29.1
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
    1,
    '',
    'api/commons/org_preferences.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!api/commons/org_preferences.proto\x12\x0b\x61pi.commons\"/\n\x17OperatorDisplayLanguage\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\"\xfe\x02\n\x11LocalePreferences\x12%\n\x0clanguage_tag\x18\x01 \x01(\tB\x02\x18\x01R\x0blanguageTag\x12M\n\"use_script_direction_right_to_left\x18\x02 \x01(\x08\x42\x02\x18\x01R\x1duseScriptDirectionRightToLeft\x12)\n\x10\x64\x65\x66\x61ult_currency\x18\x03 \x01(\tR\x0f\x64\x65\x66\x61ultCurrency\x12`\n\x19operator_display_language\x18\x04 \x01(\x0b\x32$.api.commons.OperatorDisplayLanguageR\x17operatorDisplayLanguage\x12\x66\n\x1boperator_language_direction\x18\x05 \x01(\x0e\x32&.api.commons.OperatorLanguageDirectionR\x19operatorLanguageDirection*\xac\x01\n\x19\x42roadcastTemplateOrdering\x12\x0f\n\x0b\x42Y_NAME_ASC\x10\x00\x12\x10\n\x0c\x42Y_NAME_DESC\x10\x01\x12\x1a\n\x16\x42Y_TEMPLATE_NUMBER_ASC\x10\x02\x12\x1b\n\x17\x42Y_TEMPLATE_NUMBER_DESC\x10\x03\x12\x18\n\x14\x42Y_MODIFIED_DATE_ASC\x10\x04\x12\x19\n\x15\x42Y_MODIFIED_DATE_DESC\x10\x05*B\n\x17ScheduleByTimeZoneScope\x12\x08\n\x04\x42OTH\x10\x00\x12\r\n\tSTOP_DATE\x10\x01\x12\x0e\n\nSTART_DATE\x10\x02*\xa9\x01\n\x19\x41nsweringMachineDetection\x12\x1e\n\x1aOPTIMIZE_MACHINE_DETECTION\x10\x00\x12(\n$OPTIMIZE_MACHINE_DETECTION_SLOW_LIVE\x10\x01\x12\x1d\n\x19OPTIMIZE_MACHINE_DELIVERY\x10\x02\x12#\n\x1f\x42\x41LANCED_DETECTION_AND_DELIVERY\x10\x03*A\n\x1b\x44ialListPenetrationStrategy\x12\x0f\n\x0b\x44\x45PTH_FIRST\x10\x00\x12\x11\n\rBREADTH_FIRST\x10\x01*\x9b\x08\n\x14StandardReportFilter\x12\x11\n\rNO_PREFERENCE\x10\x00\x12\x1c\n\x18\x46ILTER_BY_ANSWERED_CALLS\x10\x01\x12\x1e\n\x1a\x46ILTER_BY_ANSWERED_HANGUPS\x10\x02\x12\x1f\n\x1b\x46ILTER_BY_ANSWERED_LINKCALL\x10\x03\x12\x1d\n\x19\x46ILTER_BY_ANY_KEY_PRESSED\x10\x04\x12\x12\n\x0e\x46ILTER_BY_BUSY\x10\x05\x12\x1c\n\x18\x46ILTER_BY_CANCELED_CALLS\x10\x06\x12&\n\"FILTER_BY_CONFIRM_KEYS_3_THROUGH_6\x10\x07\x12\x1d\n\x19\x46ILTER_BY_CONNECTED_CALLS\x10\x08\x12\x1b\n\x17\x46ILTER_BY_DNCL_CANCELED\x10\t\x12\x1a\n\x16\x46ILTER_BY_FAILED_CALLS\x10\n\x12\x1b\n\x17\x46ILTER_BY_INVALID_CALLS\x10\x0b\x12 \n\x1c\x46ILTER_BY_LINKCALL_ABANDONED\x10\x0c\x12\x1b\n\x17\x46ILTER_BY_MACHINE_CALLS\x10\r\x12\x1e\n\x1a\x46ILTER_BY_MACHINE_DELIVERY\x10\x0e\x12\x1c\n\x18\x46ILTER_BY_MACHINE_HANGUP\x10\x0f\x12!\n\x1d\x46ILTER_BY_MACHINE_AND_ANY_KEY\x10\x10\x12\x17\n\x13\x46ILTER_BY_NO_ANSWER\x10\x11\x12\x1d\n\x19\x46ILTER_BY_NO_KEYS_PRESSED\x10\x12\x12 \n\x1c\x46ILTER_BY_NOT_CANCELED_CALLS\x10\x13\x12\x1f\n\x1b\x46ILTER_BY_UNCONNECTED_CALLS\x10\x14\x12)\n%FILTER_BY_UNCONNECTED_EXCLUDE_INVALID\x10\x15\x12\x13\n\x0f\x46ILTER_BY_0_KEY\x10\x16\x12\x13\n\x0f\x46ILTER_BY_1_KEY\x10\x17\x12\x13\n\x0f\x46ILTER_BY_2_KEY\x10\x18\x12\x13\n\x0f\x46ILTER_BY_3_KEY\x10\x19\x12\x13\n\x0f\x46ILTER_BY_4_KEY\x10\x1a\x12\x13\n\x0f\x46ILTER_BY_5_KEY\x10\x1b\x12\x13\n\x0f\x46ILTER_BY_6_KEY\x10\x1c\x12\x13\n\x0f\x46ILTER_BY_7_KEY\x10\x1d\x12\x13\n\x0f\x46ILTER_BY_8_KEY\x10\x1e\x12\x13\n\x0f\x46ILTER_BY_9_KEY\x10\x1f\x12\x16\n\x12\x46ILTER_BY_STAR_KEY\x10 \x12\x17\n\x13\x46ILTER_BY_POUND_KEY\x10!\x12,\n(FILTER_BY_MACHINE_HANGUP_AND_UNCONNECTED\x10\"\x12,\n(FILTER_BY_EXCLUDING_CANCELED_AND_INVALID\x10#*\xcf\x01\n\x19OperatorLanguageDirection\x12+\n\'OPERATOR_LANGUAGE_DIRECTION_UNSPECIFIED\x10\x00\x12\'\n#OPERATOR_LANGUAGE_DIRECTION_DEFAULT\x10\x01\x12-\n)OPERATOR_LANGUAGE_DIRECTION_LEFT_TO_RIGHT\x10\x02\x12-\n)OPERATOR_LANGUAGE_DIRECTION_RIGHT_TO_LEFT\x10\x03\x42s\n\x0f\x63om.api.commonsB\x13OrgPreferencesProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.org_preferences_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\023OrgPreferencesProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_LOCALEPREFERENCES'].fields_by_name['language_tag']._loaded_options = None
  _globals['_LOCALEPREFERENCES'].fields_by_name['language_tag']._serialized_options = b'\030\001'
  _globals['_LOCALEPREFERENCES'].fields_by_name['use_script_direction_right_to_left']._loaded_options = None
  _globals['_LOCALEPREFERENCES'].fields_by_name['use_script_direction_right_to_left']._serialized_options = b'\030\001'
  _globals['_BROADCASTTEMPLATEORDERING']._serialized_start=485
  _globals['_BROADCASTTEMPLATEORDERING']._serialized_end=657
  _globals['_SCHEDULEBYTIMEZONESCOPE']._serialized_start=659
  _globals['_SCHEDULEBYTIMEZONESCOPE']._serialized_end=725
  _globals['_ANSWERINGMACHINEDETECTION']._serialized_start=728
  _globals['_ANSWERINGMACHINEDETECTION']._serialized_end=897
  _globals['_DIALLISTPENETRATIONSTRATEGY']._serialized_start=899
  _globals['_DIALLISTPENETRATIONSTRATEGY']._serialized_end=964
  _globals['_STANDARDREPORTFILTER']._serialized_start=967
  _globals['_STANDARDREPORTFILTER']._serialized_end=2018
  _globals['_OPERATORLANGUAGEDIRECTION']._serialized_start=2021
  _globals['_OPERATORLANGUAGEDIRECTION']._serialized_end=2228
  _globals['_OPERATORDISPLAYLANGUAGE']._serialized_start=50
  _globals['_OPERATORDISPLAYLANGUAGE']._serialized_end=97
  _globals['_LOCALEPREFERENCES']._serialized_start=100
  _globals['_LOCALEPREFERENCES']._serialized_end=482
# @@protoc_insertion_point(module_scope)
