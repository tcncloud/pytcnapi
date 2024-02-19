# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/soundboard/entities.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&api/v1alpha1/soundboard/entities.proto\x12\x17\x61pi.v1alpha1.soundboard\x1a\x15\x61pi/commons/org.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x96\x03\n\x11SoundboardDetails\x12\'\n\rsoundboard_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0csoundboardId\x12\x1b\n\tfile_name\x18\x02 \x01(\tR\x08\x66ileName\x12;\n\tfile_type\x18\x03 \x01(\x0e\x32\x1e.api.commons.RecordingFileTypeR\x08\x66ileType\x12\x14\n\x05title\x18\x04 \x01(\tR\x05title\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12=\n\x0c\x64\x61te_created\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated\x12?\n\rlast_modified\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0clastModified\x12\x1b\n\tfile_size\x18\x08 \x01(\x03R\x08\x66ileSize\x12)\n\x10recording_length\x18\t \x01(\x03R\x0frecordingLength\"?\n\x14GetSoundboardFileReq\x12\'\n\rsoundboard_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0csoundboardId\"?\n\x14GetSoundboardFileRes\x12\'\n\x0fsoundboard_file\x18\x01 \x01(\x0cR\x0esoundboardFile\";\n\x10GetSoundboardReq\x12\'\n\rsoundboard_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0csoundboardId\"^\n\x10GetSoundboardRes\x12J\n\nsoundboard\x18\x01 \x01(\x0b\x32*.api.v1alpha1.soundboard.SoundboardDetailsR\nsoundboard\"x\n\x13\x43reateSoundboardReq\x12J\n\nsoundboard\x18\x01 \x01(\x0b\x32*.api.v1alpha1.soundboard.SoundboardDetailsR\nsoundboard\x12\x15\n\x06\x66ts_id\x18\x02 \x01(\tR\x05\x66tsId\"U\n\x13\x43reateSoundboardRes\x12\'\n\rsoundboard_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0csoundboardId\x12\x15\n\x06\x66ts_id\x18\x02 \x01(\tR\x05\x66tsId\"\x14\n\x12ListSoundboardsReq\"b\n\x12ListSoundboardsRes\x12L\n\x0bsoundboards\x18\x01 \x03(\x0b\x32*.api.v1alpha1.soundboard.SoundboardDetailsR\x0bsoundboards\"a\n\x13UpdateSoundboardReq\x12J\n\nsoundboard\x18\x01 \x01(\x0b\x32*.api.v1alpha1.soundboard.SoundboardDetailsR\nsoundboard\">\n\x13UpdateSoundboardRes\x12\'\n\rsoundboard_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0csoundboardId\">\n\x13\x44\x65leteSoundboardReq\x12\'\n\rsoundboard_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0csoundboardId\"\x15\n\x13\x44\x65leteSoundboardResB\xaa\x01\n\x1b\x63om.api.v1alpha1.soundboardB\rEntitiesProtoP\x01\xa2\x02\x03\x41VS\xaa\x02\x17\x41pi.V1alpha1.Soundboard\xca\x02\x17\x41pi\\V1alpha1\\Soundboard\xe2\x02#Api\\V1alpha1\\Soundboard\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Soundboardb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.soundboard.entities_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.soundboardB\rEntitiesProtoP\001\242\002\003AVS\252\002\027Api.V1alpha1.Soundboard\312\002\027Api\\V1alpha1\\Soundboard\342\002#Api\\V1alpha1\\Soundboard\\GPBMetadata\352\002\031Api::V1alpha1::Soundboard'
  _globals['_SOUNDBOARDDETAILS'].fields_by_name['soundboard_id']._options = None
  _globals['_SOUNDBOARDDETAILS'].fields_by_name['soundboard_id']._serialized_options = b'0\001'
  _globals['_GETSOUNDBOARDFILEREQ'].fields_by_name['soundboard_id']._options = None
  _globals['_GETSOUNDBOARDFILEREQ'].fields_by_name['soundboard_id']._serialized_options = b'0\001'
  _globals['_GETSOUNDBOARDREQ'].fields_by_name['soundboard_id']._options = None
  _globals['_GETSOUNDBOARDREQ'].fields_by_name['soundboard_id']._serialized_options = b'0\001'
  _globals['_CREATESOUNDBOARDRES'].fields_by_name['soundboard_id']._options = None
  _globals['_CREATESOUNDBOARDRES'].fields_by_name['soundboard_id']._serialized_options = b'0\001'
  _globals['_UPDATESOUNDBOARDRES'].fields_by_name['soundboard_id']._options = None
  _globals['_UPDATESOUNDBOARDRES'].fields_by_name['soundboard_id']._serialized_options = b'0\001'
  _globals['_DELETESOUNDBOARDREQ'].fields_by_name['soundboard_id']._options = None
  _globals['_DELETESOUNDBOARDREQ'].fields_by_name['soundboard_id']._serialized_options = b'0\001'
  _globals['_SOUNDBOARDDETAILS']._serialized_start=124
  _globals['_SOUNDBOARDDETAILS']._serialized_end=530
  _globals['_GETSOUNDBOARDFILEREQ']._serialized_start=532
  _globals['_GETSOUNDBOARDFILEREQ']._serialized_end=595
  _globals['_GETSOUNDBOARDFILERES']._serialized_start=597
  _globals['_GETSOUNDBOARDFILERES']._serialized_end=660
  _globals['_GETSOUNDBOARDREQ']._serialized_start=662
  _globals['_GETSOUNDBOARDREQ']._serialized_end=721
  _globals['_GETSOUNDBOARDRES']._serialized_start=723
  _globals['_GETSOUNDBOARDRES']._serialized_end=817
  _globals['_CREATESOUNDBOARDREQ']._serialized_start=819
  _globals['_CREATESOUNDBOARDREQ']._serialized_end=939
  _globals['_CREATESOUNDBOARDRES']._serialized_start=941
  _globals['_CREATESOUNDBOARDRES']._serialized_end=1026
  _globals['_LISTSOUNDBOARDSREQ']._serialized_start=1028
  _globals['_LISTSOUNDBOARDSREQ']._serialized_end=1048
  _globals['_LISTSOUNDBOARDSRES']._serialized_start=1050
  _globals['_LISTSOUNDBOARDSRES']._serialized_end=1148
  _globals['_UPDATESOUNDBOARDREQ']._serialized_start=1150
  _globals['_UPDATESOUNDBOARDREQ']._serialized_end=1247
  _globals['_UPDATESOUNDBOARDRES']._serialized_start=1249
  _globals['_UPDATESOUNDBOARDRES']._serialized_end=1311
  _globals['_DELETESOUNDBOARDREQ']._serialized_start=1313
  _globals['_DELETESOUNDBOARDREQ']._serialized_end=1375
  _globals['_DELETESOUNDBOARDRES']._serialized_start=1377
  _globals['_DELETESOUNDBOARDRES']._serialized_end=1398
# @@protoc_insertion_point(module_scope)
