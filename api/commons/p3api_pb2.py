# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/commons/p3api.proto
# Protobuf Python Version: 5.28.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    2,
    '',
    'api/commons/p3api.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61pi/commons/p3api.proto\x12\x0b\x61pi.commons\"\xd8\x01\n\x11\x43lientInfoDataRow\x12\x1f\n\x0b\x66ield_label\x18\x01 \x01(\tR\nfieldLabel\x12\x1f\n\x0b\x66ield_value\x18\x02 \x01(\tR\nfieldValue\x12\x19\n\x08is_phone\x18\x03 \x01(\x08R\x07isPhone\x12#\n\rdialed_number\x18\x04 \x01(\x08R\x0c\x64ialedNumber\x12\x41\n\x1d\x63ontact_field_description_sid\x18\x05 \x01(\x03R\x1a\x63ontactFieldDescriptionSid\"F\n\x08RGBColor\x12\x10\n\x03red\x18\x01 \x01(\x05R\x03red\x12\x14\n\x05green\x18\x02 \x01(\x05R\x05green\x12\x12\n\x04\x62lue\x18\x03 \x01(\x05R\x04\x62lue\"\xcb\x01\n\x19\x44ialedNumberFieldSettings\x12%\n\x0eshould_display\x18\x01 \x01(\x08R\rshouldDisplay\x12+\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x15.api.commons.RGBColorR\x05\x63olor\x12\x30\n\x08\x62g_color\x18\x03 \x01(\x0b\x32\x15.api.commons.RGBColorR\x07\x62gColor\x12(\n\x10\x61llow_agent_copy\x18\x04 \x01(\x08R\x0e\x61llowAgentCopy\"\x8b\x02\n\x1c\x43lientInfoDisplayTemplateRow\x12\x1f\n\x0b\x66ield_label\x18\x01 \x01(\tR\nfieldLabel\x12+\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x15.api.commons.RGBColorR\x05\x63olor\x12\x30\n\x08\x62g_color\x18\x03 \x01(\x0b\x32\x15.api.commons.RGBColorR\x07\x62gColor\x12\x41\n\x1d\x63ontact_field_description_sid\x18\x04 \x01(\x03R\x1a\x63ontactFieldDescriptionSid\x12(\n\x10\x61llow_agent_copy\x18\x05 \x01(\x08R\x0e\x61llowAgentCopy\"F\n\x15\x43\x61llHistorySearchType\"-\n\x04\x45num\x12\x0c\n\x08STANDARD\x10\x00\x12\t\n\x05\x42Y_ID\x10\x01\x12\x0c\n\x08\x42Y_AGENT\x10\x02\"\x83\x02\n\x16\x43\x61llHistorySearchScope\"\xe8\x01\n\x04\x45num\x12\x07\n\x03\x41LL\x10\x00\x12\x15\n\x11TWENTY_FOUR_HOURS\x10\x01\x12\x0c\n\x08TWO_DAYS\x10\x02\x12\x0e\n\nTHREE_DAYS\x10\x03\x12\r\n\tFIVE_DAYS\x10\x04\x12\x0e\n\nSEVEN_DAYS\x10\x05\x12\x0f\n\x0bTHIRTY_DAYS\x10\x06\x12\x0e\n\nSIXTY_DAYS\x10\x07\x12\x0f\n\x0bNINETY_DAYS\x10\x08\x12\x1a\n\x16ONEHUNDRED_TWENTY_DAYS\x10\t\x12\x19\n\x15ONEHUNDRED_FIFTY_DAYS\x10\n\x12\x1a\n\x16ONEHUNDRED_EIGHTY_DAYS\x10\x0b\"\xb9\x01\n\x14ListPhoneBookOrderBy\"\xa0\x01\n\x04\x45num\x12\x12\n\x0ePHONE_BOOK_SID\x10\x00\x12\x0e\n\nENTRY_TYPE\x10\x01\x12\x0e\n\nENTRY_NAME\x10\x02\x12\x0e\n\nCLIENT_SID\x10\x03\x12\x12\n\x0eHUNT_GROUP_SID\x10\x04\x12\x10\n\x0cPHONE_NUMBER\x10\x05\x12\x15\n\x11PHONE_NUMBER_TYPE\x10\x06\x12\x17\n\x13PHONE_NUMBER_HIDDEN\x10\x07*a\n\x18InterruptedPeeringStatus\x12!\n\x1dInterruptPeeringStatus_MANUAL\x10\x00\x12\"\n\x1eInterruptPeeringStatus_PREVIEW\x10\x01*h\n\x17RecalculateBillingMonth\x12%\n!RECALCULATE_BILLING_MONTH_CURRENT\x10\x00\x12&\n\"RECALCULATE_BILLING_MONTH_PREVIOUS\x10\x01*\xb9\x02\n\x16RecalculateBillingType\x12+\n\'RECALCULATE_BILLING_TYPE_OUTBOUND_CALLS\x10\x00\x12*\n&RECALCULATE_BILLING_TYPE_INBOUND_CALLS\x10\x01\x12#\n\x1fRECALCULATE_BILLING_TYPE_AGENTS\x10\x02\x12 \n\x1cRECALCULATE_BILLING_TYPE_SMS\x10\x03\x12\"\n\x1eRECALCULATE_BILLING_TYPE_EMAIL\x10\x04\x12.\n*RECALCULATE_BILLING_TYPE_MANUAL_DIAL_CALLS\x10\x06\"\x04\x08\x05\x10\x05*%RECALCULATE_BILLING_TYPE_VOCAL_DIRECT*V\n\x10PhoneBookSIPType\x12 \n\x1cPHONE_BOOK_SIP_TYPE_OUTBOUND\x10\x00\x12 \n\x1cPHONE_BOOK_SIP_TYPE_TRANSFER\x10\x01*\x9c\x01\n\x18PhoneBookPhoneNumberType\x12*\n&PHONE_BOOK_PHONE_NUMBER_TYPE_CALLER_ID\x10\x00\x12)\n%PHONE_BOOK_PHONE_NUMBER_TYPE_OUTBOUND\x10\x01\x12)\n%PHONE_BOOK_PHONE_NUMBER_TYPE_TRANSFER\x10\x02\x42j\n\x0f\x63om.api.commonsB\nP3apiProtoP\x01\xa2\x02\x03\x41\x43X\xaa\x02\x0b\x41pi.Commons\xca\x02\x0b\x41pi\\Commons\xe2\x02\x17\x41pi\\Commons\\GPBMetadata\xea\x02\x0c\x41pi::Commonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.p3api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.commonsB\nP3apiProtoP\001\242\002\003ACX\252\002\013Api.Commons\312\002\013Api\\Commons\342\002\027Api\\Commons\\GPBMetadata\352\002\014Api::Commons'
  _globals['_INTERRUPTEDPEERINGSTATUS']._serialized_start=1329
  _globals['_INTERRUPTEDPEERINGSTATUS']._serialized_end=1426
  _globals['_RECALCULATEBILLINGMONTH']._serialized_start=1428
  _globals['_RECALCULATEBILLINGMONTH']._serialized_end=1532
  _globals['_RECALCULATEBILLINGTYPE']._serialized_start=1535
  _globals['_RECALCULATEBILLINGTYPE']._serialized_end=1848
  _globals['_PHONEBOOKSIPTYPE']._serialized_start=1850
  _globals['_PHONEBOOKSIPTYPE']._serialized_end=1936
  _globals['_PHONEBOOKPHONENUMBERTYPE']._serialized_start=1939
  _globals['_PHONEBOOKPHONENUMBERTYPE']._serialized_end=2095
  _globals['_CLIENTINFODATAROW']._serialized_start=41
  _globals['_CLIENTINFODATAROW']._serialized_end=257
  _globals['_RGBCOLOR']._serialized_start=259
  _globals['_RGBCOLOR']._serialized_end=329
  _globals['_DIALEDNUMBERFIELDSETTINGS']._serialized_start=332
  _globals['_DIALEDNUMBERFIELDSETTINGS']._serialized_end=535
  _globals['_CLIENTINFODISPLAYTEMPLATEROW']._serialized_start=538
  _globals['_CLIENTINFODISPLAYTEMPLATEROW']._serialized_end=805
  _globals['_CALLHISTORYSEARCHTYPE']._serialized_start=807
  _globals['_CALLHISTORYSEARCHTYPE']._serialized_end=877
  _globals['_CALLHISTORYSEARCHTYPE_ENUM']._serialized_start=832
  _globals['_CALLHISTORYSEARCHTYPE_ENUM']._serialized_end=877
  _globals['_CALLHISTORYSEARCHSCOPE']._serialized_start=880
  _globals['_CALLHISTORYSEARCHSCOPE']._serialized_end=1139
  _globals['_CALLHISTORYSEARCHSCOPE_ENUM']._serialized_start=907
  _globals['_CALLHISTORYSEARCHSCOPE_ENUM']._serialized_end=1139
  _globals['_LISTPHONEBOOKORDERBY']._serialized_start=1142
  _globals['_LISTPHONEBOOKORDERBY']._serialized_end=1327
  _globals['_LISTPHONEBOOKORDERBY_ENUM']._serialized_start=1167
  _globals['_LISTPHONEBOOKORDERBY_ENUM']._serialized_end=1327
# @@protoc_insertion_point(module_scope)
