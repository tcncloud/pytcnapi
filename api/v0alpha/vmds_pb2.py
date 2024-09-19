# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v0alpha/vmds.proto
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
    'api/v0alpha/vmds.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pi/v0alpha/vmds.proto\x12\x0b\x61pi.v0alpha\x1a\x17\x61nnotations/authz.proto\x1a\x15\x61pi/commons/acd.proto\x1a\x1cgoogle/api/annotations.proto\"8\n\x17GetVoicemailMetadataReq\x12\x1d\n\nmail_boxes\x18\x02 \x03(\tR\tmailBoxes\"\xf2\x02\n\x17GetVoicemailMetadataRes\x12\x1b\n\tcaller_id\x18\x01 \x01(\tR\x08\x63\x61llerId\x12\x1d\n\ncaller_sid\x18\x02 \x01(\tR\tcallerSid\x12;\n\x0b\x63\x61ller_type\x18\x03 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\ncallerType\x12#\n\rdialed_number\x18\x04 \x01(\tR\x0c\x64ialedNumber\x12)\n\x10\x64uration_seconds\x18\x05 \x01(\x05R\x0f\x64urationSeconds\x12\x1b\n\tflag_read\x18\x06 \x01(\x08R\x08\x66lagRead\x12\x19\n\x08mail_box\x18\x07 \x01(\tR\x07mailBox\x12-\n\x12recording_filename\x18\t \x01(\tR\x11recordingFilename\x12\'\n\x0frecording_start\x18\n \x01(\x05R\x0erecordingStart\"\x8b\x01\n\x12\x44\x65leteVoicemailReq\x12\x19\n\x08mail_box\x18\x02 \x01(\tR\x07mailBox\x12\x1d\n\ncaller_sid\x18\x03 \x01(\tR\tcallerSid\x12;\n\x0b\x63\x61ller_type\x18\x04 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\ncallerType\"\x14\n\x12\x44\x65leteVoicemailRes\"/\n\x11\x44\x65leteGreetingReq\x12\x1a\n\x08\x66ilename\x18\x02 \x01(\tR\x08\x66ilename\"\x13\n\x11\x44\x65leteGreetingRes\"e\n\x13UpdateUploadNameReq\x12*\n\x11\x63urrent_file_name\x18\x01 \x01(\tR\x0f\x63urrentFileName\x12\"\n\rnew_file_name\x18\x02 \x01(\tR\x0bnewFileName\"\x15\n\x13UpdateUploadNameRes\"5\n\x14GetVoicemailCountReq\x12\x1d\n\nmail_boxes\x18\x02 \x03(\tR\tmailBoxes\"F\n\x14GetVoicemailCountRes\x12\x14\n\x05total\x18\x01 \x01(\x05R\x05total\x12\x18\n\x07unheard\x18\x02 \x01(\x05R\x07unheard\"\xb0\x01\n\x1aUpdateVoicemailFlagReadReq\x12\x19\n\x08mail_box\x18\x02 \x01(\tR\x07mailBox\x12\x1d\n\ncaller_sid\x18\x03 \x01(\tR\tcallerSid\x12;\n\x0b\x63\x61ller_type\x18\x04 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\ncallerType\x12\x1b\n\tflag_read\x18\x05 \x01(\x08R\x08\x66lagRead\"9\n\x1aUpdateVoicemailFlagReadRes\x12\x1b\n\tflag_read\x18\x01 \x01(\x08R\x08\x66lagRead\"\x8b\x01\n\x12\x44ownloadMessageReq\x12\x19\n\x08mail_box\x18\x02 \x01(\tR\x07mailBox\x12\x1d\n\ncaller_sid\x18\x03 \x01(\tR\tcallerSid\x12;\n\x0b\x63\x61ller_type\x18\x04 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\ncallerType\"&\n\x12\x44ownloadMessageRes\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"Z\n\x17GetUploadGreetingUrlReq\x12#\n\rpbx_extension\x18\x02 \x01(\tR\x0cpbxExtension\x12\x1a\n\x08\x66ilename\x18\x03 \x01(\tR\x08\x66ilename\"+\n\x17GetUploadGreetingUrlRes\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"W\n\x13\x44ownloadMessagesReq\x12\x1d\n\nmail_boxes\x18\x02 \x03(\tR\tmailBoxes\x12!\n\x0cunheard_only\x18\x03 \x01(\x08R\x0bunheardOnly\"\'\n\x13\x44ownloadMessagesRes\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"<\n\x1f\x44ownloadGreetingForExtensionReq\x12\x19\n\x08mail_box\x18\x02 \x01(\tR\x07mailBox\"3\n\x1f\x44ownloadGreetingForExtensionRes\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"1\n\x13\x44ownloadGreetingReq\x12\x1a\n\x08\x66ilename\x18\x02 \x01(\tR\x08\x66ilename\"\'\n\x13\x44ownloadGreetingRes\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\"[\n\x18ProcessGreetingUploadReq\x12#\n\rpbx_extension\x18\x02 \x01(\tR\x0cpbxExtension\x12\x1a\n\x08\x66ilename\x18\x03 \x01(\tR\x08\x66ilename\"\x1a\n\x18ProcessGreetingUploadRes\"`\n\x1dUpdateGreetingForExtensionReq\x12#\n\rpbx_extension\x18\x02 \x01(\tR\x0cpbxExtension\x12\x1a\n\x08\x66ilename\x18\x03 \x01(\tR\x08\x66ilename\"\x1f\n\x1dUpdateGreetingForExtensionRes\"\x1b\n\x19ListAvailableGreetingsReq\"\xa6\x01\n\x19ListAvailableGreetingsRes\x12M\n\tgreetings\x18\x01 \x03(\x0b\x32/.api.v0alpha.ListAvailableGreetingsRes.FileInfoR\tgreetings\x1a:\n\x08\x46ileInfo\x12\x1a\n\x08\x66ilename\x18\x01 \x01(\tR\x08\x66ilename\x12\x12\n\x04size\x18\x02 \x01(\x03R\x04size2\xa3\x11\n\x04Vmds\x12\x9e\x01\n\x14GetVoicemailMetadata\x12$.api.v0alpha.GetVoicemailMetadataReq\x1a$.api.v0alpha.GetVoicemailMetadataRes\"8\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02+\"&/api/v0alpha/vmds/getvoicemailmetadata:\x01*0\x01\x12\x9e\x01\n\x18GetVoicemailMessageCount\x12!.api.v0alpha.GetVoicemailCountReq\x1a!.api.v0alpha.GetVoicemailCountRes\"<\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02/\"*/api/v0alpha/vmds/getvoicemailmessagecount:\x01*\x12\x88\x01\n\x0f\x44\x65leteVoicemail\x12\x1f.api.v0alpha.DeleteVoicemailReq\x1a\x1f.api.v0alpha.DeleteVoicemailRes\"3\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02&\"!/api/v0alpha/vmds/deletevoicemail:\x01*\x12\x84\x01\n\x0e\x44\x65leteGreeting\x12\x1e.api.v0alpha.DeleteGreetingReq\x1a\x1e.api.v0alpha.DeleteGreetingRes\"2\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02%\" /api/v0alpha/vmds/deletegreeting:\x01*\x12\x8c\x01\n\x10UpdateUploadName\x12 .api.v0alpha.UpdateUploadNameReq\x1a .api.v0alpha.UpdateUploadNameRes\"4\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\'\"\"/api/v0alpha/vmds/updateuploadname:\x01*\x12\xa8\x01\n\x17UpdateVoicemailFlagRead\x12\'.api.v0alpha.UpdateVoicemailFlagReadReq\x1a\'.api.v0alpha.UpdateVoicemailFlagReadRes\";\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02.\")/api/v0alpha/vmds/updatevoicemailflagread:\x01*\x12\x88\x01\n\x0f\x44ownloadMessage\x12\x1f.api.v0alpha.DownloadMessageReq\x1a\x1f.api.v0alpha.DownloadMessageRes\"3\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02&\"!/api/v0alpha/vmds/downloadmessage:\x01*\x12\x8c\x01\n\x10\x44ownloadMessages\x12 .api.v0alpha.DownloadMessagesReq\x1a .api.v0alpha.DownloadMessagesRes\"4\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\'\"\"/api/v0alpha/vmds/downloadmessages:\x01*\x12\xc3\x01\n\x1c\x44ownloadGreetingForExtension\x12,.api.v0alpha.DownloadGreetingForExtensionReq\x1a,.api.v0alpha.DownloadGreetingForExtensionRes\"G\xba\xb8\x91\x02\t\n\x03\x08\xac\x02\n\x02\x08\x65\x82\xd3\xe4\x93\x02\x33\"./api/v0alpha/vmds/downloadgreetingforextension:\x01*\x12\x8c\x01\n\x10\x44ownloadGreeting\x12 .api.v0alpha.DownloadGreetingReq\x1a .api.v0alpha.DownloadGreetingRes\"4\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\'\"\"/api/v0alpha/vmds/downloadgreeting:\x01*\x12\x9c\x01\n\x14GetUploadGreetingUrl\x12$.api.v0alpha.GetUploadGreetingUrlReq\x1a$.api.v0alpha.GetUploadGreetingUrlRes\"8\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02+\"&/api/v0alpha/vmds/getuploadgreetingurl:\x01*\x12\xa0\x01\n\x15ProcessGreetingUpload\x12%.api.v0alpha.ProcessGreetingUploadReq\x1a%.api.v0alpha.ProcessGreetingUploadRes\"9\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02,\"\'/api/v0alpha/vmds/processgreetingupload:\x01*\x12\xb4\x01\n\x1aUpdateGreetingForExtension\x12*.api.v0alpha.UpdateGreetingForExtensionReq\x1a*.api.v0alpha.UpdateGreetingForExtensionRes\">\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x31\",/api/v0alpha/vmds/updategreetingforextension:\x01*\x12\xa4\x01\n\x16ListAvailableGreetings\x12&.api.v0alpha.ListAvailableGreetingsReq\x1a&.api.v0alpha.ListAvailableGreetingsRes\":\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02-\"(/api/v0alpha/vmds/listavailablegreetings:\x01*Bi\n\x0f\x63om.api.v0alphaB\tVmdsProtoP\x01\xa2\x02\x03\x41VX\xaa\x02\x0b\x41pi.V0alpha\xca\x02\x0b\x41pi\\V0alpha\xe2\x02\x17\x41pi\\V0alpha\\GPBMetadata\xea\x02\x0c\x41pi::V0alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v0alpha.vmds_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.v0alphaB\tVmdsProtoP\001\242\002\003AVX\252\002\013Api.V0alpha\312\002\013Api\\V0alpha\342\002\027Api\\V0alpha\\GPBMetadata\352\002\014Api::V0alpha'
  _globals['_VMDS'].methods_by_name['GetVoicemailMetadata']._loaded_options = None
  _globals['_VMDS'].methods_by_name['GetVoicemailMetadata']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002+\"&/api/v0alpha/vmds/getvoicemailmetadata:\001*'
  _globals['_VMDS'].methods_by_name['GetVoicemailMessageCount']._loaded_options = None
  _globals['_VMDS'].methods_by_name['GetVoicemailMessageCount']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002/\"*/api/v0alpha/vmds/getvoicemailmessagecount:\001*'
  _globals['_VMDS'].methods_by_name['DeleteVoicemail']._loaded_options = None
  _globals['_VMDS'].methods_by_name['DeleteVoicemail']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002&\"!/api/v0alpha/vmds/deletevoicemail:\001*'
  _globals['_VMDS'].methods_by_name['DeleteGreeting']._loaded_options = None
  _globals['_VMDS'].methods_by_name['DeleteGreeting']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002%\" /api/v0alpha/vmds/deletegreeting:\001*'
  _globals['_VMDS'].methods_by_name['UpdateUploadName']._loaded_options = None
  _globals['_VMDS'].methods_by_name['UpdateUploadName']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\'\"\"/api/v0alpha/vmds/updateuploadname:\001*'
  _globals['_VMDS'].methods_by_name['UpdateVoicemailFlagRead']._loaded_options = None
  _globals['_VMDS'].methods_by_name['UpdateVoicemailFlagRead']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002.\")/api/v0alpha/vmds/updatevoicemailflagread:\001*'
  _globals['_VMDS'].methods_by_name['DownloadMessage']._loaded_options = None
  _globals['_VMDS'].methods_by_name['DownloadMessage']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002&\"!/api/v0alpha/vmds/downloadmessage:\001*'
  _globals['_VMDS'].methods_by_name['DownloadMessages']._loaded_options = None
  _globals['_VMDS'].methods_by_name['DownloadMessages']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\'\"\"/api/v0alpha/vmds/downloadmessages:\001*'
  _globals['_VMDS'].methods_by_name['DownloadGreetingForExtension']._loaded_options = None
  _globals['_VMDS'].methods_by_name['DownloadGreetingForExtension']._serialized_options = b'\272\270\221\002\t\n\003\010\254\002\n\002\010e\202\323\344\223\0023\"./api/v0alpha/vmds/downloadgreetingforextension:\001*'
  _globals['_VMDS'].methods_by_name['DownloadGreeting']._loaded_options = None
  _globals['_VMDS'].methods_by_name['DownloadGreeting']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002\'\"\"/api/v0alpha/vmds/downloadgreeting:\001*'
  _globals['_VMDS'].methods_by_name['GetUploadGreetingUrl']._loaded_options = None
  _globals['_VMDS'].methods_by_name['GetUploadGreetingUrl']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002+\"&/api/v0alpha/vmds/getuploadgreetingurl:\001*'
  _globals['_VMDS'].methods_by_name['ProcessGreetingUpload']._loaded_options = None
  _globals['_VMDS'].methods_by_name['ProcessGreetingUpload']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002,\"\'/api/v0alpha/vmds/processgreetingupload:\001*'
  _globals['_VMDS'].methods_by_name['UpdateGreetingForExtension']._loaded_options = None
  _globals['_VMDS'].methods_by_name['UpdateGreetingForExtension']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0021\",/api/v0alpha/vmds/updategreetingforextension:\001*'
  _globals['_VMDS'].methods_by_name['ListAvailableGreetings']._loaded_options = None
  _globals['_VMDS'].methods_by_name['ListAvailableGreetings']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002-\"(/api/v0alpha/vmds/listavailablegreetings:\001*'
  _globals['_GETVOICEMAILMETADATAREQ']._serialized_start=117
  _globals['_GETVOICEMAILMETADATAREQ']._serialized_end=173
  _globals['_GETVOICEMAILMETADATARES']._serialized_start=176
  _globals['_GETVOICEMAILMETADATARES']._serialized_end=546
  _globals['_DELETEVOICEMAILREQ']._serialized_start=549
  _globals['_DELETEVOICEMAILREQ']._serialized_end=688
  _globals['_DELETEVOICEMAILRES']._serialized_start=690
  _globals['_DELETEVOICEMAILRES']._serialized_end=710
  _globals['_DELETEGREETINGREQ']._serialized_start=712
  _globals['_DELETEGREETINGREQ']._serialized_end=759
  _globals['_DELETEGREETINGRES']._serialized_start=761
  _globals['_DELETEGREETINGRES']._serialized_end=780
  _globals['_UPDATEUPLOADNAMEREQ']._serialized_start=782
  _globals['_UPDATEUPLOADNAMEREQ']._serialized_end=883
  _globals['_UPDATEUPLOADNAMERES']._serialized_start=885
  _globals['_UPDATEUPLOADNAMERES']._serialized_end=906
  _globals['_GETVOICEMAILCOUNTREQ']._serialized_start=908
  _globals['_GETVOICEMAILCOUNTREQ']._serialized_end=961
  _globals['_GETVOICEMAILCOUNTRES']._serialized_start=963
  _globals['_GETVOICEMAILCOUNTRES']._serialized_end=1033
  _globals['_UPDATEVOICEMAILFLAGREADREQ']._serialized_start=1036
  _globals['_UPDATEVOICEMAILFLAGREADREQ']._serialized_end=1212
  _globals['_UPDATEVOICEMAILFLAGREADRES']._serialized_start=1214
  _globals['_UPDATEVOICEMAILFLAGREADRES']._serialized_end=1271
  _globals['_DOWNLOADMESSAGEREQ']._serialized_start=1274
  _globals['_DOWNLOADMESSAGEREQ']._serialized_end=1413
  _globals['_DOWNLOADMESSAGERES']._serialized_start=1415
  _globals['_DOWNLOADMESSAGERES']._serialized_end=1453
  _globals['_GETUPLOADGREETINGURLREQ']._serialized_start=1455
  _globals['_GETUPLOADGREETINGURLREQ']._serialized_end=1545
  _globals['_GETUPLOADGREETINGURLRES']._serialized_start=1547
  _globals['_GETUPLOADGREETINGURLRES']._serialized_end=1590
  _globals['_DOWNLOADMESSAGESREQ']._serialized_start=1592
  _globals['_DOWNLOADMESSAGESREQ']._serialized_end=1679
  _globals['_DOWNLOADMESSAGESRES']._serialized_start=1681
  _globals['_DOWNLOADMESSAGESRES']._serialized_end=1720
  _globals['_DOWNLOADGREETINGFOREXTENSIONREQ']._serialized_start=1722
  _globals['_DOWNLOADGREETINGFOREXTENSIONREQ']._serialized_end=1782
  _globals['_DOWNLOADGREETINGFOREXTENSIONRES']._serialized_start=1784
  _globals['_DOWNLOADGREETINGFOREXTENSIONRES']._serialized_end=1835
  _globals['_DOWNLOADGREETINGREQ']._serialized_start=1837
  _globals['_DOWNLOADGREETINGREQ']._serialized_end=1886
  _globals['_DOWNLOADGREETINGRES']._serialized_start=1888
  _globals['_DOWNLOADGREETINGRES']._serialized_end=1927
  _globals['_PROCESSGREETINGUPLOADREQ']._serialized_start=1929
  _globals['_PROCESSGREETINGUPLOADREQ']._serialized_end=2020
  _globals['_PROCESSGREETINGUPLOADRES']._serialized_start=2022
  _globals['_PROCESSGREETINGUPLOADRES']._serialized_end=2048
  _globals['_UPDATEGREETINGFOREXTENSIONREQ']._serialized_start=2050
  _globals['_UPDATEGREETINGFOREXTENSIONREQ']._serialized_end=2146
  _globals['_UPDATEGREETINGFOREXTENSIONRES']._serialized_start=2148
  _globals['_UPDATEGREETINGFOREXTENSIONRES']._serialized_end=2179
  _globals['_LISTAVAILABLEGREETINGSREQ']._serialized_start=2181
  _globals['_LISTAVAILABLEGREETINGSREQ']._serialized_end=2208
  _globals['_LISTAVAILABLEGREETINGSRES']._serialized_start=2211
  _globals['_LISTAVAILABLEGREETINGSRES']._serialized_end=2377
  _globals['_LISTAVAILABLEGREETINGSRES_FILEINFO']._serialized_start=2319
  _globals['_LISTAVAILABLEGREETINGSRES_FILEINFO']._serialized_end=2377
  _globals['_VMDS']._serialized_start=2380
  _globals['_VMDS']._serialized_end=4591
# @@protoc_insertion_point(module_scope)
