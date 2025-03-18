# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/classifier/entities.proto
# Protobuf Python Version: 6.30.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    1,
    '',
    'api/v1alpha1/classifier/entities.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import classifier_pb2 as api_dot_commons_dot_classifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&api/v1alpha1/classifier/entities.proto\x12\x17\x61pi.v1alpha1.classifier\x1a\x1c\x61pi/commons/classifier.proto\"P\n\x15\x43lassifierEntityTypes\x12\x37\n\x05types\x18\x01 \x03(\x0e\x32!.api.commons.ClassifierEntityTypeR\x05types\"\xaf\x04\n\x0c\x46ileTemplate\x12,\n\x10\x66ile_template_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x0e\x66ileTemplateId\x12\x1a\n\x08\x66ilename\x18\x02 \x01(\tR\x08\x66ilename\x12\x43\n\x06\x66ields\x18\x03 \x03(\x0b\x32+.api.v1alpha1.classifier.FileTemplate.FieldR\x06\x66ields\x12\x45\n\nparse_opts\x18\x04 \x01(\x0b\x32\".api.v1alpha1.classifier.ParseOptsB\x02\x18\x01R\tparseOpts\x12J\n\x0b\x63onstraints\x18\x05 \x01(\x0b\x32$.api.v1alpha1.classifier.ConstraintsB\x02\x18\x01R\x0b\x63onstraints\x12\x12\n\x04\x66oid\x18\x06 \x01(\x03R\x04\x66oid\x12\x31\n\x04opts\x18\x07 \x01(\x0b\x32\x1d.api.v1alpha1.classifier.OptsR\x04opts\x1a\xb5\x01\n\x05\x46ield\x12\x1f\n\x0bsyntax_type\x18\x01 \x01(\tR\nsyntaxType\x12\x42\n\x0b\x65ntity_type\x18\x02 \x01(\x0e\x32!.api.commons.ClassifierEntityTypeR\nentityType\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x16\n\x06\x66ormat\x18\x04 \x01(\tR\x06\x66ormat\x12\x1b\n\traw_value\x18\x05 \x01(\tR\x08rawValue\"\xbb\x03\n\x04Opts\x12Q\n\x0c\x64\x61te_formats\x18\x01 \x03(\x0b\x32..api.v1alpha1.classifier.Opts.DateFormatsEntryR\x0b\x64\x61teFormats\x12T\n\rrename_fields\x18\x02 \x03(\x0b\x32/.api.v1alpha1.classifier.Opts.RenameFieldsEntryR\x0crenameFields\x12\x41\n\nparse_opts\x18\x03 \x01(\x0b\x32\".api.v1alpha1.classifier.ParseOptsR\tparseOpts\x12\x46\n\x0b\x63onstraints\x18\x04 \x01(\x0b\x32$.api.v1alpha1.classifier.ConstraintsR\x0b\x63onstraints\x1a>\n\x10\x44\x61teFormatsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x1a?\n\x11RenameFieldsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\xbd\x02\n\tParseOpts\x12\x34\n\x03\x63sv\x18\x01 \x01(\x0b\x32 .api.v1alpha1.classifier.OptsCsvH\x00R\x03\x63sv\x12\x37\n\x04json\x18\x02 \x01(\x0b\x32!.api.v1alpha1.classifier.OptsJsonH\x00R\x04json\x12:\n\x05jsonl\x18\x03 \x01(\x0b\x32\".api.v1alpha1.classifier.OptsJsonLH\x00R\x05jsonl\x12:\n\x05\x66ixed\x18\x04 \x01(\x0b\x32\".api.v1alpha1.classifier.OptsFixedH\x00R\x05\x66ixed\x12@\n\x07parquet\x18\x05 \x01(\x0b\x32$.api.v1alpha1.classifier.OptsParquetH\x00R\x07parquetB\x07\n\x05\x66type\"{\n\x07OptsCsv\x12\x1d\n\nhas_header\x18\x01 \x01(\x08R\thasHeader\x12\x1b\n\tskip_rows\x18\x02 \x01(\x03R\x08skipRows\x12\x16\n\x06header\x18\x03 \x03(\tR\x06header\x12\x1c\n\tseparator\x18\x04 \x01(\tR\tseparator\"-\n\x08OptsJson\x12!\n\x0crecords_root\x18\x01 \x01(\tR\x0brecordsRoot\"\x0b\n\tOptsJsonL\"\xc4\x02\n\tOptsFixed\x12O\n\tpositions\x18\x01 \x03(\x0b\x32\x31.api.v1alpha1.classifier.OptsFixed.PositionsEntryR\tpositions\x12\x1d\n\nhas_header\x18\x02 \x01(\x08R\thasHeader\x1a[\n\tFieldOpts\x12+\n\x11starting_position\x18\r \x01(\x05R\x10startingPosition\x12!\n\x0c\x66ield_length\x18\x0e \x01(\x05R\x0b\x66ieldLength\x1aj\n\x0ePositionsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x42\n\x05value\x18\x02 \x01(\x0b\x32,.api.v1alpha1.classifier.OptsFixed.FieldOptsR\x05value:\x02\x38\x01\"\r\n\x0bOptsParquet\"\xf3\x02\n\x0b\x43onstraints\x12H\n\x06\x66orbid\x18\x01 \x03(\x0b\x32\x30.api.v1alpha1.classifier.Constraints.ForbidEntryR\x06\x66orbid\x12\x45\n\x05\x61llow\x18\x02 \x03(\x0b\x32/.api.v1alpha1.classifier.Constraints.AllowEntryR\x05\x61llow\x1ai\n\x0b\x46orbidEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x44\n\x05value\x18\x02 \x01(\x0b\x32..api.v1alpha1.classifier.ClassifierEntityTypesR\x05value:\x02\x38\x01\x1ah\n\nAllowEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x44\n\x05value\x18\x02 \x01(\x0b\x32..api.v1alpha1.classifier.ClassifierEntityTypesR\x05value:\x02\x38\x01\"\x97\x01\n\nParseHints\x12\x41\n\nparse_opts\x18\x01 \x01(\x0b\x32\".api.v1alpha1.classifier.ParseOptsR\tparseOpts\x12\x46\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32$.api.v1alpha1.classifier.ConstraintsR\x0b\x63onstraintsB\xaa\x01\n\x1b\x63om.api.v1alpha1.classifierB\rEntitiesProtoP\x01\xa2\x02\x03\x41VC\xaa\x02\x17\x41pi.V1alpha1.Classifier\xca\x02\x17\x41pi\\V1alpha1\\Classifier\xe2\x02#Api\\V1alpha1\\Classifier\\GPBMetadata\xea\x02\x19\x41pi::V1alpha1::Classifierb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.classifier.entities_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.api.v1alpha1.classifierB\rEntitiesProtoP\001\242\002\003AVC\252\002\027Api.V1alpha1.Classifier\312\002\027Api\\V1alpha1\\Classifier\342\002#Api\\V1alpha1\\Classifier\\GPBMetadata\352\002\031Api::V1alpha1::Classifier'
  _globals['_FILETEMPLATE'].fields_by_name['file_template_id']._loaded_options = None
  _globals['_FILETEMPLATE'].fields_by_name['file_template_id']._serialized_options = b'0\001'
  _globals['_FILETEMPLATE'].fields_by_name['parse_opts']._loaded_options = None
  _globals['_FILETEMPLATE'].fields_by_name['parse_opts']._serialized_options = b'\030\001'
  _globals['_FILETEMPLATE'].fields_by_name['constraints']._loaded_options = None
  _globals['_FILETEMPLATE'].fields_by_name['constraints']._serialized_options = b'\030\001'
  _globals['_OPTS_DATEFORMATSENTRY']._loaded_options = None
  _globals['_OPTS_DATEFORMATSENTRY']._serialized_options = b'8\001'
  _globals['_OPTS_RENAMEFIELDSENTRY']._loaded_options = None
  _globals['_OPTS_RENAMEFIELDSENTRY']._serialized_options = b'8\001'
  _globals['_OPTSFIXED_POSITIONSENTRY']._loaded_options = None
  _globals['_OPTSFIXED_POSITIONSENTRY']._serialized_options = b'8\001'
  _globals['_CONSTRAINTS_FORBIDENTRY']._loaded_options = None
  _globals['_CONSTRAINTS_FORBIDENTRY']._serialized_options = b'8\001'
  _globals['_CONSTRAINTS_ALLOWENTRY']._loaded_options = None
  _globals['_CONSTRAINTS_ALLOWENTRY']._serialized_options = b'8\001'
  _globals['_CLASSIFIERENTITYTYPES']._serialized_start=97
  _globals['_CLASSIFIERENTITYTYPES']._serialized_end=177
  _globals['_FILETEMPLATE']._serialized_start=180
  _globals['_FILETEMPLATE']._serialized_end=739
  _globals['_FILETEMPLATE_FIELD']._serialized_start=558
  _globals['_FILETEMPLATE_FIELD']._serialized_end=739
  _globals['_OPTS']._serialized_start=742
  _globals['_OPTS']._serialized_end=1185
  _globals['_OPTS_DATEFORMATSENTRY']._serialized_start=1058
  _globals['_OPTS_DATEFORMATSENTRY']._serialized_end=1120
  _globals['_OPTS_RENAMEFIELDSENTRY']._serialized_start=1122
  _globals['_OPTS_RENAMEFIELDSENTRY']._serialized_end=1185
  _globals['_PARSEOPTS']._serialized_start=1188
  _globals['_PARSEOPTS']._serialized_end=1505
  _globals['_OPTSCSV']._serialized_start=1507
  _globals['_OPTSCSV']._serialized_end=1630
  _globals['_OPTSJSON']._serialized_start=1632
  _globals['_OPTSJSON']._serialized_end=1677
  _globals['_OPTSJSONL']._serialized_start=1679
  _globals['_OPTSJSONL']._serialized_end=1690
  _globals['_OPTSFIXED']._serialized_start=1693
  _globals['_OPTSFIXED']._serialized_end=2017
  _globals['_OPTSFIXED_FIELDOPTS']._serialized_start=1818
  _globals['_OPTSFIXED_FIELDOPTS']._serialized_end=1909
  _globals['_OPTSFIXED_POSITIONSENTRY']._serialized_start=1911
  _globals['_OPTSFIXED_POSITIONSENTRY']._serialized_end=2017
  _globals['_OPTSPARQUET']._serialized_start=2019
  _globals['_OPTSPARQUET']._serialized_end=2032
  _globals['_CONSTRAINTS']._serialized_start=2035
  _globals['_CONSTRAINTS']._serialized_end=2406
  _globals['_CONSTRAINTS_FORBIDENTRY']._serialized_start=2195
  _globals['_CONSTRAINTS_FORBIDENTRY']._serialized_end=2300
  _globals['_CONSTRAINTS_ALLOWENTRY']._serialized_start=2302
  _globals['_CONSTRAINTS_ALLOWENTRY']._serialized_end=2406
  _globals['_PARSEHINTS']._serialized_start=2409
  _globals['_PARSEHINTS']._serialized_end=2560
# @@protoc_insertion_point(module_scope)
