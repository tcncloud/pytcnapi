# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/lms/entities.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.v0alpha import lms_pb2 as api_dot_v0alpha_dot_lms__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x61pi/v1alpha1/lms/entities.proto\x12\x10\x61pi.v1alpha1.lms\x1a\x15\x61pi/v0alpha/lms.proto\"\xa9\x01\n\x0e\x46ileTemplateV2\x12\x44\n\x0flegacy_template\x18\x01 \x01(\x0b\x32\x19.api.v0alpha.FileTemplateH\x00R\x0elegacyTemplate\x12\x45\n\rdock_template\x18\x02 \x01(\x0b\x32\x1e.api.v1alpha1.lms.FileTemplateH\x00R\x0c\x64ockTemplateB\n\n\x08template\"O\n\rFileTemplates\x12>\n\ttemplates\x18\x01 \x03(\x0b\x32 .api.v1alpha1.lms.FileTemplateV2R\ttemplates\"\xec\x01\n\x0c\x46ileTemplate\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12(\n\x10\x66ile_template_id\x18\x02 \x01(\x03R\x0e\x66ileTemplateId\x12\x1a\n\x08\x66ilename\x18\x03 \x01(\tR\x08\x66ilename\x12/\n\x06\x66ields\x18\x04 \x03(\x0b\x32\x17.api.v1alpha1.lms.FieldR\x06\x66ields\x12:\n\nparse_opts\x18\x05 \x01(\x0b\x32\x1b.api.v1alpha1.lms.ParseOptsR\tparseOpts\x12\x12\n\x04\x66oid\x18\x06 \x01(\x03R\x04\x66oid\"\x90\x01\n\x05\x46ield\x12\x1f\n\x0bsyntax_type\x18\x01 \x01(\tR\nsyntaxType\x12\x1d\n\npresi_type\x18\x02 \x01(\tR\tpresiType\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x16\n\x06\x66ormat\x18\x04 \x01(\tR\x06\x66ormat\x12\x1b\n\traw_value\x18\x05 \x01(\tR\x08rawValue\"\x9a\x02\n\tParseOpts\x12-\n\x03\x63sv\x18\x01 \x01(\x0b\x32\x19.api.v1alpha1.lms.OptsCsvH\x00R\x03\x63sv\x12\x30\n\x04json\x18\x02 \x01(\x0b\x32\x1a.api.v1alpha1.lms.OptsJsonH\x00R\x04json\x12\x33\n\x05jsonl\x18\x03 \x01(\x0b\x32\x1b.api.v1alpha1.lms.OptsJsonLH\x00R\x05jsonl\x12\x33\n\x05\x66ixed\x18\x04 \x01(\x0b\x32\x1b.api.v1alpha1.lms.OptsFixedH\x00R\x05\x66ixed\x12\x39\n\x07parquet\x18\x05 \x01(\x0b\x32\x1d.api.v1alpha1.lms.OptsParquetH\x00R\x07parquetB\x07\n\x05\x66type\"{\n\x07OptsCsv\x12\x1d\n\nhas_header\x18\x01 \x01(\x08R\thasHeader\x12\x1b\n\tskip_rows\x18\x02 \x01(\x03R\x08skipRows\x12\x16\n\x06header\x18\x03 \x03(\tR\x06header\x12\x1c\n\tseparator\x18\x04 \x01(\tR\tseparator\"-\n\x08OptsJson\x12!\n\x0crecords_root\x18\x01 \x01(\tR\x0brecordsRoot\"\x0b\n\tOptsJsonL\"\xbe\x01\n\tOptsFixed\x12\x1d\n\nhas_header\x18\x01 \x01(\x08R\thasHeader\x12\x39\n\x06header\x18\x02 \x03(\x0b\x32!.api.v1alpha1.lms.OptsFixed.FieldR\x06header\x1aW\n\x05\x46ield\x12+\n\x11starting_position\x18\r \x01(\x05R\x10startingPosition\x12!\n\x0c\x66ield_length\x18\x0e \x01(\x05R\x0b\x66ieldLength\"\r\n\x0bOptsParquet\"T\n\x0bNewTemplate\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1a\n\x08\x66ilename\x18\x02 \x01(\tR\x08\x66ilename\x12\x12\n\x04\x64\x61ta\x18\x03 \x01(\x0cR\x04\x64\x61ta\"x\n\x10\x45xistingTemplate\x12(\n\x10\x66ile_template_id\x18\x01 \x01(\x03R\x0e\x66ileTemplateId\x12:\n\nparse_opts\x18\x02 \x01(\x0b\x32\x1b.api.v1alpha1.lms.ParseOptsR\tparseOptsB\x87\x01\n\x14\x63om.api.v1alpha1.lmsB\rEntitiesProtoP\x01\xa2\x02\x03\x41VL\xaa\x02\x10\x41pi.V1alpha1.Lms\xca\x02\x10\x41pi\\V1alpha1\\Lms\xe2\x02\x1c\x41pi\\V1alpha1\\Lms\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Lmsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.lms.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.lmsB\rEntitiesProtoP\001\242\002\003AVL\252\002\020Api.V1alpha1.Lms\312\002\020Api\\V1alpha1\\Lms\342\002\034Api\\V1alpha1\\Lms\\GPBMetadata\352\002\022Api::V1alpha1::Lms'
  _globals['_FILETEMPLATEV2']._serialized_start=77
  _globals['_FILETEMPLATEV2']._serialized_end=246
  _globals['_FILETEMPLATES']._serialized_start=248
  _globals['_FILETEMPLATES']._serialized_end=327
  _globals['_FILETEMPLATE']._serialized_start=330
  _globals['_FILETEMPLATE']._serialized_end=566
  _globals['_FIELD']._serialized_start=569
  _globals['_FIELD']._serialized_end=713
  _globals['_PARSEOPTS']._serialized_start=716
  _globals['_PARSEOPTS']._serialized_end=998
  _globals['_OPTSCSV']._serialized_start=1000
  _globals['_OPTSCSV']._serialized_end=1123
  _globals['_OPTSJSON']._serialized_start=1125
  _globals['_OPTSJSON']._serialized_end=1170
  _globals['_OPTSJSONL']._serialized_start=1172
  _globals['_OPTSJSONL']._serialized_end=1183
  _globals['_OPTSFIXED']._serialized_start=1186
  _globals['_OPTSFIXED']._serialized_end=1376
  _globals['_OPTSFIXED_FIELD']._serialized_start=1289
  _globals['_OPTSFIXED_FIELD']._serialized_end=1376
  _globals['_OPTSPARQUET']._serialized_start=1378
  _globals['_OPTSPARQUET']._serialized_end=1391
  _globals['_NEWTEMPLATE']._serialized_start=1393
  _globals['_NEWTEMPLATE']._serialized_end=1477
  _globals['_EXISTINGTEMPLATE']._serialized_start=1479
  _globals['_EXISTINGTEMPLATE']._serialized_end=1599
# @@protoc_insertion_point(module_scope)