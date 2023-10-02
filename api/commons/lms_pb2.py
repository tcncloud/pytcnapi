# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/lms.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/commons/lms.proto\x12\x0b\x61pi.commons\x1a\x1egoogle/protobuf/wrappers.proto\"N\n\x0bRecordField\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12+\n\x04type\x18\x02 \x01(\x0e\x32\x17.api.commons.RecordTypeR\x04type\"\xce\x02\n\x0b\x46ilePattern\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\x1c.api.commons.FilePatternTypeR\x04type\x12\x1c\n\tdirectory\x18\x02 \x01(\tR\tdirectory\x12\x1a\n\x08\x66ilename\x18\x03 \x01(\tR\x08\x66ilename\x12\x1a\n\x08prefixes\x18\x04 \x03(\tR\x08prefixes\x12\x1f\n\x0b\x64\x61te_format\x18\x05 \x01(\tR\ndateFormat\x12\x16\n\x06suffix\x18\x06 \x01(\tR\x06suffix\x12%\n\x0e\x66ile_extension\x18\x07 \x01(\tR\rfileExtension\x12\x1f\n\x0b\x64\x61te_prefix\x18\x08 \x01(\x08R\ndatePrefix\x12\x36\n\nday_to_use\x18\t \x01(\x0e\x32\x18.api.commons.RelativeDayR\x08\x64\x61yToUse\"\xd0\x02\n\x13\x43onstructedFilename\x12I\n\x11override_filename\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x10overrideFilename\x12\x16\n\x06prefix\x18\x04 \x01(\tR\x06prefix\x12\x1f\n\x0b\x64\x61te_format\x18\x05 \x01(\tR\ndateFormat\x12\x16\n\x06suffix\x18\x06 \x01(\tR\x06suffix\x12%\n\x0e\x66ile_extension\x18\x07 \x01(\tR\rfileExtension\x12>\n\rdate_position\x18\x08 \x01(\x0e\x32\x19.api.commons.DatePositionR\x0c\x64\x61tePosition\x12\x36\n\nday_to_use\x18\t \x01(\x0e\x32\x18.api.commons.RelativeDayR\x08\x64\x61yToUse\"\xf1\x02\n\x14PaginationTerminator\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x16\n\x06negate\x18\x02 \x01(\x08R\x06negate\x12#\n\x0c\x65xists_check\x18\x03 \x01(\x08H\x00R\x0b\x65xistsCheck\x12*\n\x10num_greater_than\x18\x04 \x01(\x01H\x00R\x0enumGreaterThan\x12$\n\rnum_less_than\x18\x05 \x01(\x01H\x00R\x0bnumLessThan\x12\x1f\n\nnum_equals\x18\x06 \x01(\x01H\x00R\tnumEquals\x12(\n\x0f\x63ount_less_than\x18\x07 \x01(\x03H\x00R\rcountLessThan\x12\x1f\n\nstr_equals\x18\x08 \x01(\tH\x00R\tstrEquals\x12#\n\x0cstr_contains\x18\t \x01(\tH\x00R\x0bstrContains\x12!\n\x0b\x62ool_equals\x18\n \x01(\x08H\x00R\nboolEqualsB\x04\n\x02op\"U\n\nExpiration\x12+\n\x05units\x18\x01 \x01(\x0e\x32\x15.api.commons.TimeUnitR\x05units\x12\x1a\n\x08quantity\x18\x02 \x01(\x03R\x08quantity*4\n\x08\x43ronType\x12\x11\n\rCRON_TYPE_LMS\x10\x00\x12\x15\n\x11\x43RON_TYPE_JOURNEY\x10\x01*\x8d\x01\n\x0e\x45nrichmentType\x12\x16\n\x12\x45NRICHMENT_TYPE_OR\x10\x00\x12\x17\n\x13\x45NRICHMENT_TYPE_XOR\x10\x01\x12\x17\n\x13\x45NRICHMENT_TYPE_AND\x10\x02\x12\x18\n\x14\x45NRICHMENT_TYPE_JOIN\x10\x03\x12\x17\n\x13\x45NRICHMENT_TYPE_NOT\x10\x04*?\n\rPrimarySource\x12\x16\n\x12PRIMARY_SOURCE_LMS\x10\x00\x12\x16\n\x12PRIMARY_SOURCE_CJS\x10\x01*=\n\x0e\x44\x65\x64upKeyPolicy\x12\x0e\n\nKEEP_FIRST\x10\x00\x12\r\n\tKEEP_LAST\x10\x01\x12\x0c\n\x08KEEP_ALL\x10\x02*I\n\x07RunType\x12\x14\n\x10RUN_TYPE_ENABLED\x10\x00\x12\x15\n\x11RUN_TYPE_DISABLED\x10\x01\x12\x11\n\rRUN_TYPE_TEST\x10\x02*P\n\x11\x43onsentActionType\x12\x1b\n\x17\x43ONSENT_ACTION_TYPE_ADD\x10\x00\x12\x1e\n\x1a\x43ONSENT_ACTION_TYPE_REVOKE\x10\x01*\xbb\x05\n\nRecordType\x12\x13\n\x0fRECORD_TYPE_ALL\x10\x00\x12\x16\n\x12RECORD_TYPE_STRING\x10\x01\x12\x16\n\x12RECORD_TYPE_NUMBER\x10\x02\x12\x14\n\x10RECORD_TYPE_BOOL\x10\x03\x12\x15\n\x11RECORD_TYPE_PHONE\x10\x04\x12\x18\n\x14RECORD_TYPE_CURRENCY\x10\x05\x12\x1e\n\x1aRECORD_TYPE_ENRICHED_PHONE\x10\x06\x12\x1c\n\x18RECORD_TYPE_ENRICHED_ZIP\x10\x12\x12\x1b\n\x17RECORD_TYPE_POSTAL_CODE\x10\x07\x12\x15\n\x11RECORD_TYPE_EMAIL\x10\x08\x12\x1c\n\x18RECORD_TYPE_DATETIME_NOW\x10\t\x12\"\n\x1eRECORD_TYPE_DATETIME_TIMESTAMP\x10\n\x12\x1d\n\x19RECORD_TYPE_DATETIME_DATE\x10\x0b\x12&\n\"RECORD_TYPE_DATETIME_MONTH_AND_DAY\x10\x0c\x12$\n RECORD_TYPE_DATETIME_TIME_OF_DAY\x10\r\x12 \n\x1cRECORD_TYPE_REPEATED_RECORDS\x10\x0f\x12\x1a\n\x16RECORD_TYPE_RECORD_MAP\x10\x10\x12\x15\n\x11RECORD_TYPE_ERROR\x10\x11\x12\x16\n\x12RECORD_TYPE_SOCIAL\x10\x13\x12\x1d\n\x19RECORD_TYPE_DATE_OF_BIRTH\x10\x14\x12\x19\n\x15RECORD_TYPE_FULL_NAME\x10\x15\x12\x1e\n\x1aRECORD_TYPE_ACCOUNT_NUMBER\x10\x16\x12\x1c\n\x18RECORD_TYPE_STRUCT_VALUE\x10\x17\x12\x1b\n\x17RECORD_TYPE_EHR_DETAILS\x10\x18*\xd5\x04\n\tFieldType\x12\x15\n\x11\x46IELD_TYPE_STRING\x10\x00\x12\x15\n\x11\x46IELD_TYPE_NUMBER\x10\x01\x12\x16\n\x12\x46IELD_TYPE_BOOLEAN\x10\x02\x12\x14\n\x10\x46IELD_TYPE_PHONE\x10\x03\x12\x17\n\x13\x46IELD_TYPE_CURRENCY\x10\x04\x12\x14\n\x10\x46IELD_TYPE_EMAIL\x10\x05\x12\x1b\n\x17\x46IELD_TYPE_DATETIME_NOW\x10\x06\x12!\n\x1d\x46IELD_TYPE_DATETIME_TIMESTAMP\x10\x07\x12\x1c\n\x18\x46IELD_TYPE_DATETIME_DATE\x10\x08\x12%\n!FIELD_TYPE_DATETIME_MONTH_AND_DAY\x10\t\x12#\n\x1f\x46IELD_TYPE_DATETIME_TIME_OF_DAY\x10\n\x12\x1a\n\x16\x46IELD_TYPE_POSTAL_CODE\x10\x0c\x12\x1d\n\x19\x46IELD_TYPE_ENRICHED_PHONE\x10\r\x12\x1b\n\x17\x46IELD_TYPE_ENRICHED_ZIP\x10\x0e\x12\x15\n\x11\x46IELD_TYPE_SOCIAL\x10\x0f\x12\x1c\n\x18\x46IELD_TYPE_DATE_OF_BIRTH\x10\x10\x12\x18\n\x14\x46IELD_TYPE_FULL_NAME\x10\x11\x12\x1d\n\x19\x46IELD_TYPE_ACCOUNT_NUMBER\x10\x12\x12\x14\n\x10\x46IELD_TYPE_ERROR\x10\x13\x12\x1b\n\x17\x46IELD_TYPE_STRUCT_VALUE\x10\x14\x12\x1a\n\x16\x46IELD_TYPE_EHR_DETAILS\x10\x15*\x88\x01\n\nFileFormat\x12\x13\n\x0f\x46ILE_FORMAT_CSV\x10\x00\x12\x1c\n\x18\x46ILE_FORMAT_CUSTOM_DELIM\x10\x01\x12\x1c\n\x18\x46ILE_FORMAT_FIXED_FORMAT\x10\x02\x12\x13\n\x0f\x46ILE_FORMAT_TAB\x10\x03\x12\x14\n\x10\x46ILE_FORMAT_JSON\x10\x04*\xc6\x01\n\x19PipelineElementStatusType\x12,\n(PIPELINE_ELEMENT_STATUS_TYPE_INITIALIZED\x10\x00\x12(\n$PIPELINE_ELEMENT_STATUS_TYPE_RUNNING\x10\x01\x12(\n$PIPELINE_ELEMENT_STATUS_TYPE_STOPPED\x10\x02\x12\'\n#PIPELINE_ELEMENT_STATUS_TYPE_FAILED\x10\x03*\\\n\x0e\x45ntrypointType\x12\x17\n\x13\x45NTRYPOINT_TYPE_NON\x10\x00\x12\x17\n\x13\x45NTRYPOINT_TYPE_API\x10\x01\x12\x18\n\x14\x45NTRYPOINT_TYPE_SFTP\x10\x02*\xd3\x01\n\x13\x44uplicatePolicyType\x12\x34\n0DUPLICATE_POLICY_TYPE_KEEP_RECORD_DISCARD_NUMBER\x10\x00\x12\x32\n.DUPLICATE_POLICY_TYPE_ALLOW_RECORD_KEEP_NUMBER\x10\x01\x12(\n$DUPLICATE_POLICY_TYPE_DISCARD_RECORD\x10\x02\x12(\n$DUPLICATE_POLICY_TYPE_DUPLICATE_LIST\x10\x03*O\n\x10\x41\x62sentPolicyType\x12\x1b\n\x17\x41\x42SENT_POLICY_TYPE_KEEP\x10\x00\x12\x1e\n\x1a\x41\x42SENT_POLICY_TYPE_DISCARD\x10\x01*c\n\rDialOrderType\x12\x19\n\x15\x44IAL_ORDER_TYPE_FIRST\x10\x00\x12\x1b\n\x17\x44IAL_ORDER_TYPE_NATURAL\x10\x01\x12\x1a\n\x16\x44IAL_ORDER_TYPE_CUSTOM\x10\x02*<\n\nExportType\x12\x18\n\x14\x45XPORT_TYPE_FILENAME\x10\x00\x12\x14\n\x10\x45XPORT_TYPE_SFTP\x10\x01*@\n\tSortOrder\x12\x18\n\x14SORT_ORDER_ASCENDING\x10\x00\x12\x19\n\x15SORT_ORDER_DESCENDING\x10\x01*V\n\x0b\x43ompareType\x12\x17\n\x13\x43OMPARE_TYPE_STRING\x10\x00\x12\x17\n\x13\x43OMPARE_TYPE_NUMBER\x10\x01\x12\x15\n\x11\x43OMPARE_TYPE_BOOL\x10\x02*\x8f\x02\n\x0f\x43ompareOperator\x12\x1d\n\x19\x43OMPARE_OPERATOR_EQUAL_TO\x10\x00\x12\x1c\n\x18\x43OMPARE_OPERATOR_GREATER\x10\x01\x12\"\n\x1e\x43OMPARE_OPERATOR_GREATER_EQUAL\x10\x02\x12\x19\n\x15\x43OMPARE_OPERATOR_LESS\x10\x03\x12\x1f\n\x1b\x43OMPARE_OPERATOR_LESS_EQUAL\x10\x04\x12 \n\x1c\x43OMPARE_OPERATOR_STARTS_WITH\x10\x05\x12\x1e\n\x1a\x43OMPARE_OPERATOR_ENDS_WITH\x10\x06\x12\x1d\n\x19\x43OMPARE_OPERATOR_CONTAINS\x10\x07*>\n\rChainOperator\x12\x16\n\x12\x43HAIN_OPERATOR_AND\x10\x00\x12\x15\n\x11\x43HAIN_OPERATOR_OR\x10\x01*\x8a\x01\n\x0c\x44\x65\x44upActions\x12\x1d\n\x19\x44\x45_DUP_ACTIONS_KEEP_FIRST\x10\x00\x12\x1c\n\x18\x44\x45_DUP_ACTIONS_KEEP_BOTH\x10\x03\x12\x1c\n\x18\x44\x45_DUP_ACTIONS_KEEP_LAST\x10\x04\x12\x1f\n\x1b\x44\x45_DUP_ACTIONS_KEEP_NEITHER\x10\x05*\x84\x01\n\x0c\x44\x61tePosition\x12\x17\n\x13\x44\x41TE_POSITION_FIRST\x10\x00\x12!\n\x1d\x44\x41TE_POSITION_BEFORE_FILENAME\x10\x01\x12 \n\x1c\x44\x41TE_POSITION_AFTER_FILENAME\x10\x02\x12\x16\n\x12\x44\x41TE_POSITION_LAST\x10\x03*_\n\x0bRelativeDay\x12\x16\n\x12RELATIVE_DAY_TODAY\x10\x00\x12\x1a\n\x16RELATIVE_DAY_YESTERDAY\x10\x01\x12\x1c\n\x18RELATIVE_DAY_LAST_FRIDAY\x10\x02*p\n\x0f\x46ilePatternType\x12\x1a\n\x16\x46ILE_PATTERN_TYPE_GLOB\x10\x00\x12!\n\x1d\x46ILE_PATTERN_TYPE_CONSTRUCTED\x10\x01\x12\x1e\n\x1a\x46ILE_PATTERN_TYPE_ORIGINAL\x10\x02*\xb8\x01\n\x11\x44\x61teTimePrecision\x12\x1a\n\x16\x44\x41TETIME_PRECISION_NOW\x10\x00\x12 \n\x1c\x44\x41TETIME_PRECISION_TIMESTAMP\x10\x01\x12\x1b\n\x17\x44\x41TETIME_PRECISION_DATE\x10\x02\x12$\n DATETIME_PRECISION_MONTH_AND_DAY\x10\x03\x12\"\n\x1e\x44\x41TETIME_PRECISION_TIME_OF_DAY\x10\x04*1\n\x08HttpVerb\x12\x11\n\rHTTP_VERB_GET\x10\x00\x12\x12\n\x0eHTTP_VERB_POST\x10\x01*V\n\x12\x43omplianceListType\x12\x1e\n\x1a\x43OMPLIANCE_LIST_TYPE_SCRUB\x10\x00\x12 \n\x1c\x43OMPLIANCE_LIST_TYPE_CONSENT\x10\x01*\x9e\x01\n\nEventState\x12\x14\n\x10\x45VENT_STATE_NONE\x10\x00\x12\x17\n\x13\x45VENT_STATE_KICKOFF\x10\x01\x12\x15\n\x11\x45VENT_STATE_CHECK\x10\x02\x12\x17\n\x13\x45VENT_STATE_PROCESS\x10\x03\x12\x17\n\x13\x45VENT_STATE_CLEANUP\x10\x04\x12\x18\n\x14\x45VENT_STATE_FINISHED\x10\x05*F\n\x08TimeUnit\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0e\n\nTIME_WEEKS\x10\x01\x12\r\n\tTIME_DAYS\x10\x02\x12\x0e\n\nTIME_HOURS\x10\x03\x42h\n\x0f\x63om.api.commonsB\x08LmsProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.lms_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\017com.api.commonsB\010LmsProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_CRONTYPE']._serialized_start=1285
  _globals['_CRONTYPE']._serialized_end=1337
  _globals['_ENRICHMENTTYPE']._serialized_start=1340
  _globals['_ENRICHMENTTYPE']._serialized_end=1481
  _globals['_PRIMARYSOURCE']._serialized_start=1483
  _globals['_PRIMARYSOURCE']._serialized_end=1546
  _globals['_DEDUPKEYPOLICY']._serialized_start=1548
  _globals['_DEDUPKEYPOLICY']._serialized_end=1609
  _globals['_RUNTYPE']._serialized_start=1611
  _globals['_RUNTYPE']._serialized_end=1684
  _globals['_CONSENTACTIONTYPE']._serialized_start=1686
  _globals['_CONSENTACTIONTYPE']._serialized_end=1766
  _globals['_RECORDTYPE']._serialized_start=1769
  _globals['_RECORDTYPE']._serialized_end=2468
  _globals['_FIELDTYPE']._serialized_start=2471
  _globals['_FIELDTYPE']._serialized_end=3068
  _globals['_FILEFORMAT']._serialized_start=3071
  _globals['_FILEFORMAT']._serialized_end=3207
  _globals['_PIPELINEELEMENTSTATUSTYPE']._serialized_start=3210
  _globals['_PIPELINEELEMENTSTATUSTYPE']._serialized_end=3408
  _globals['_ENTRYPOINTTYPE']._serialized_start=3410
  _globals['_ENTRYPOINTTYPE']._serialized_end=3502
  _globals['_DUPLICATEPOLICYTYPE']._serialized_start=3505
  _globals['_DUPLICATEPOLICYTYPE']._serialized_end=3716
  _globals['_ABSENTPOLICYTYPE']._serialized_start=3718
  _globals['_ABSENTPOLICYTYPE']._serialized_end=3797
  _globals['_DIALORDERTYPE']._serialized_start=3799
  _globals['_DIALORDERTYPE']._serialized_end=3898
  _globals['_EXPORTTYPE']._serialized_start=3900
  _globals['_EXPORTTYPE']._serialized_end=3960
  _globals['_SORTORDER']._serialized_start=3962
  _globals['_SORTORDER']._serialized_end=4026
  _globals['_COMPARETYPE']._serialized_start=4028
  _globals['_COMPARETYPE']._serialized_end=4114
  _globals['_COMPAREOPERATOR']._serialized_start=4117
  _globals['_COMPAREOPERATOR']._serialized_end=4388
  _globals['_CHAINOPERATOR']._serialized_start=4390
  _globals['_CHAINOPERATOR']._serialized_end=4452
  _globals['_DEDUPACTIONS']._serialized_start=4455
  _globals['_DEDUPACTIONS']._serialized_end=4593
  _globals['_DATEPOSITION']._serialized_start=4596
  _globals['_DATEPOSITION']._serialized_end=4728
  _globals['_RELATIVEDAY']._serialized_start=4730
  _globals['_RELATIVEDAY']._serialized_end=4825
  _globals['_FILEPATTERNTYPE']._serialized_start=4827
  _globals['_FILEPATTERNTYPE']._serialized_end=4939
  _globals['_DATETIMEPRECISION']._serialized_start=4942
  _globals['_DATETIMEPRECISION']._serialized_end=5126
  _globals['_HTTPVERB']._serialized_start=5128
  _globals['_HTTPVERB']._serialized_end=5177
  _globals['_COMPLIANCELISTTYPE']._serialized_start=5179
  _globals['_COMPLIANCELISTTYPE']._serialized_end=5265
  _globals['_EVENTSTATE']._serialized_start=5268
  _globals['_EVENTSTATE']._serialized_end=5426
  _globals['_TIMEUNIT']._serialized_start=5428
  _globals['_TIMEUNIT']._serialized_end=5498
  _globals['_RECORDFIELD']._serialized_start=70
  _globals['_RECORDFIELD']._serialized_end=148
  _globals['_FILEPATTERN']._serialized_start=151
  _globals['_FILEPATTERN']._serialized_end=485
  _globals['_CONSTRUCTEDFILENAME']._serialized_start=488
  _globals['_CONSTRUCTEDFILENAME']._serialized_end=824
  _globals['_PAGINATIONTERMINATOR']._serialized_start=827
  _globals['_PAGINATIONTERMINATOR']._serialized_end=1196
  _globals['_EXPIRATION']._serialized_start=1198
  _globals['_EXPIRATION']._serialized_end=1283
# @@protoc_insertion_point(module_scope)
