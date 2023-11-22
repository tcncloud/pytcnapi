# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/call.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import results_pb2 as api_dot_commons_dot_results__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pi/commons/call.proto\x12\x0b\x61pi.commons\x1a\x19\x61pi/commons/results.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb5\x0b\n\x0eSimpleCallData\x12\x19\n\x08task_sid\x18\x01 \x01(\x03R\x07taskSid\x12\x19\n\x08\x63\x61ll_sid\x18\x02 \x01(\x03R\x07\x63\x61llSid\x12$\n\x0etask_group_sid\x18\x03 \x01(\x03R\x0ctaskGroupSid\x12\x1d\n\nclient_sid\x18\x04 \x01(\x03R\tclientSid\x12\x1f\n\x0b\x63ountry_sid\x18\x05 \x01(\x03R\ncountrySid\x12\x1b\n\tagent_sid\x18\x06 \x01(\x03R\x08\x61gentSid\x12\x1d\n\nstart_time\x18\x07 \x01(\x03R\tstartTime\x12\x1b\n\tcaller_id\x18\x08 \x01(\tR\x08\x63\x61llerId\x12!\n\x0cphone_number\x18\t \x01(\tR\x0bphoneNumber\x12!\n\x0c\x63ountry_code\x18\n \x01(\tR\x0b\x63ountryCode\x12+\n\x11\x64\x65livery_duration\x18\x0b \x01(\x05R\x10\x64\x65liveryDuration\x12,\n\x12link_call_duration\x18\x0c \x01(\x05R\x10linkCallDuration\x12/\n\x06result\x18\r \x01(\x0e\x32\x17.api.commons.CallResultR\x06result\x12\x19\n\x08sip_code\x18\x0e \x01(\x05R\x07sipCode\x12\x1b\n\tdo_record\x18\x0f \x01(\x08R\x08\x64oRecord\x12.\n\x13recording_file_name\x18\x10 \x01(\tR\x11recordingFileName\x12\x31\n\x15is_dial_validation_ok\x18\x11 \x01(\x08R\x12isDialValidationOk\x12\x30\n\x15is_time_zone_scrub_ok\x18\x12 \x01(\x08R\x11isTimeZoneScrubOk\x12\x32\n\x16is_cell_phone_scrub_ok\x18\x13 \x01(\x08R\x12isCellPhoneScrubOk\x12\x45\n is_custom_calling_rules_scrub_ok\x18\x14 \x01(\x08R\x1bisCustomCallingRulesScrubOk\x12\'\n\x10is_dncl_scrub_ok\x18\x15 \x01(\x08R\risDnclScrubOk\x12:\n\x1ause_global_time_zone_scrub\x18\x16 \x01(\x08R\x16useGlobalTimeZoneScrub\x12-\n\x13\x64o_cell_phone_scrub\x18\x17 \x01(\x08R\x10\x64oCellPhoneScrub\x12\"\n\rdo_dncl_scrub\x18\x19 \x01(\x08R\x0b\x64oDnclScrub\x12$\n\x0e\x63\x61ll_data_type\x18\x1a \x01(\tR\x0c\x63\x61llDataType\x12\x33\n\x16\x63\x61ller_id_country_code\x18\x1c \x01(\tR\x13\x63\x61llerIdCountryCode\x12\x31\n\x15\x63\x61ller_id_country_sid\x18\x1d \x01(\x03R\x12\x63\x61llerIdCountrySid\x12\x19\n\x08zip_code\x18\x1e \x01(\tR\x07zipCode\x12/\n\x14is_preview_by_record\x18\x1f \x01(\x08R\x11isPreviewByRecord\x12\"\n\rrule_set_name\x18  \x01(\tR\x0bruleSetName\x12\x37\n\x18is_natural_compliance_ok\x18! \x01(\x08R\x15isNaturalComplianceOk\x12\x45\n\x10simple_meta_data\x18\" \x03(\x0b\x32\x1b.api.commons.SimpleKeyValueR\x0esimpleMetaData\x12R\n\x17simple_result_meta_data\x18# \x03(\x0b\x32\x1b.api.commons.SimpleKeyValueR\x14simpleResultMetaDataJ\x04\x08\x18\x10\x19J\x04\x08\x1b\x10\x1c\"8\n\x0eSimpleKeyValue\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"\xe4\x01\n\x10SimpleRecordData\x12\x19\n\x08task_sid\x18\x01 \x01(\x03R\x07taskSid\x12$\n\x0etask_group_sid\x18\x02 \x01(\x03R\x0ctaskGroupSid\x12\x1b\n\tagent_sid\x18\x03 \x01(\x03R\x08\x61gentSid\x12\x39\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tstartTime\x12\x37\n\tstop_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08stopTime*[\n\nCallStatus\x12\x10\n\x0c\x43\x41LL_UNKNOWN\x10\x00\x12\x13\n\x0e\x43\x41LL_SCHEDULED\x10\x9c\x18\x12\x11\n\x0c\x43\x41LL_RUNNING\x10\x80\x19\x12\x13\n\x0e\x43\x41LL_COMPLETED\x10\xe4\x19\x42i\n\x0f\x63om.api.commonsB\tCallProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.call_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\tCallProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_CALLSTATUS']._serialized_start=1852
  _globals['_CALLSTATUS']._serialized_end=1943
  _globals['_SIMPLECALLDATA']._serialized_start=100
  _globals['_SIMPLECALLDATA']._serialized_end=1561
  _globals['_SIMPLEKEYVALUE']._serialized_start=1563
  _globals['_SIMPLEKEYVALUE']._serialized_end=1619
  _globals['_SIMPLERECORDDATA']._serialized_start=1622
  _globals['_SIMPLERECORDDATA']._serialized_end=1850
# @@protoc_insertion_point(module_scope)
