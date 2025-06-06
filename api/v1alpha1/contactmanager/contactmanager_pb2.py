# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/contactmanager/contactmanager.proto
# Protobuf Python Version: 6.30.2
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
    2,
    '',
    'api/v1alpha1/contactmanager/contactmanager.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons.audit import audit_pb2 as api_dot_commons_dot_audit_dot_audit__pb2
from api.commons import classifier_pb2 as api_dot_commons_dot_classifier__pb2
from api.commons import contactmanager_pb2 as api_dot_commons_dot_contactmanager__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0api/v1alpha1/contactmanager/contactmanager.proto\x12\x1b\x61pi.v1alpha1.contactmanager\x1a\x1d\x61pi/commons/audit/audit.proto\x1a\x1c\x61pi/commons/classifier.proto\x1a api/commons/contactmanager.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x90\x01\n\x15GetContactListRequest\x12=\n\x0crequest_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x0brequestMask\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12!\n\nproject_id\x18\x03 \x01(\x03\x42\x02\x30\x01R\tprojectId\"\x8f\x01\n\x16GetContactListResponse\x12\x61\n\x14\x63ontact_manager_list\x18\x02 \x03(\x0b\x32/.api.v1alpha1.contactmanager.ContactManagerListR\x12\x63ontactManagerListJ\x04\x08\x01\x10\x02R\x0c\x63ontact_list\"\xef\x01\n\x1bListContactEntryListRequest\x12>\n\x17\x63ontact_manager_list_id\x18\x01 \x01(\x03\x42\x02\x30\x01H\x00R\x14\x63ontactManagerListId\x88\x01\x01\x12\x19\n\x06org_id\x18\x02 \x01(\tB\x02\x18\x01R\x05orgId\x12\x1d\n\nproject_id\x18\x03 \x01(\tR\tprojectId\x12\x1b\n\tpage_size\x18\x04 \x01(\x05R\x08pageSize\x12\x1d\n\npage_token\x18\x05 \x01(\tR\tpageTokenB\x1a\n\x18_contact_manager_list_id\"\x92\x02\n\x1cListContactEntryListResponse\x12h\n\x15\x63ontact_manager_entry\x18\x02 \x03(\x0b\x32\x30.api.v1alpha1.contactmanager.ContactManagerEntryB\x02\x18\x01R\x13\x63ontactManagerEntry\x12&\n\x0fnext_page_token\x18\x03 \x01(\tR\rnextPageToken\x12K\n\x08\x63m_entry\x18\x04 \x03(\x0b\x32\x30.api.v1alpha1.contactmanager.ContactManagerEntryR\x07\x63mEntryJ\x04\x08\x01\x10\x02R\rcontact_entry\"X\n\x19GetEncContactEntryRequest\x12;\n\x18\x63ontact_manager_entry_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x15\x63ontactManagerEntryId\"\x97\x01\n\x1aGetEncContactEntryResponse\x12\x64\n\x15\x63ontact_manager_entry\x18\x02 \x03(\x0b\x32\x30.api.v1alpha1.contactmanager.ContactManagerEntryR\x13\x63ontactManagerEntryJ\x04\x08\x01\x10\x02R\rcontact_entry\"\xbf\x01\n\x1cGetKYCEncContactEntryRequest\x12!\n\nproject_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\tprojectId\x12V\n\x0ckyc_response\x18\x04 \x03(\x0b\x32\x33.api.v1alpha1.contactmanager.ContactManagerEntryValR\x0bkycResponseJ\x04\x08\x02\x10\x03J\x04\x08\x03\x10\x04R\tentry_valR\rmin_kyc_limit\"\x92\x01\n\x1dGetKYCEncContactEntryResponse\x12\x1a\n\x08verified\x18\x01 \x01(\x08R\x08verified\x12U\n\rcontact_entry\x18\x02 \x03(\x0b\x32\x30.api.v1alpha1.contactmanager.ContactManagerEntryR\x0c\x63ontactEntry\"8\n\x11GetKYCKeysRequest\x12#\n\x0bproject_sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\nprojectSid\"D\n\x12GetKYCKeysResponse\x12\x1d\n\nentry_type\x18\x01 \x03(\tR\tentryTypeJ\x04\x08\x02\x10\x03R\tkyc_limit\"\xc8\x04\n\x13\x43ontactManagerEntry\x12;\n\x18\x63ontact_manager_entry_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x15\x63ontactManagerEntryId\x12\x46\n\x1d\x63ontact_manager_entry_list_id\x18\x02 \x01(\x03\x42\x04\x18\x01\x30\x01R\x19\x63ontactManagerEntryListId\x12\x14\n\x03key\x18\x03 \x01(\tB\x02\x18\x01R\x03key\x12\x18\n\x05value\x18\x04 \x01(\tB\x02\x18\x01R\x05value\x12\x16\n\x04type\x18\x05 \x01(\tB\x02\x18\x01R\x04type\x12=\n\x0c\x64\x61te_created\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated\x12\x37\n\x06status\x18\x07 \x01(\x0e\x32\x1f.api.commons.ContactEntryStatusR\x06status\x12?\n\rdate_modified\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0c\x64\x61teModified\x12\x10\n\x03ttl\x18\t \x01(\x03R\x03ttl\x12\x1b\n\tfile_name\x18\n \x03(\tR\x08\x66ileName\x12?\n\x05\x66ield\x18\x0b \x03(\x0b\x32).api.v1alpha1.contactmanager.ContactFieldR\x05\x66ield\x12;\n\x0b\x65xpiry_date\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nexpiryDate\"\xdc\x03\n\x12\x43ontactManagerList\x12\x39\n\x17\x63ontact_manager_list_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\x14\x63ontactManagerListId\x12\x15\n\x06org_id\x18\x02 \x01(\tR\x05orgId\x12!\n\nproject_id\x18\x03 \x01(\x03\x42\x02\x30\x01R\tprojectId\x12\x1f\n\tfile_name\x18\x04 \x01(\tB\x02\x18\x01R\x08\x66ileName\x12 \n\x0b\x64\x65scription\x18\x05 \x01(\tR\x0b\x64\x65scription\x12%\n\x0clist_details\x18\x06 \x03(\tB\x02\x18\x01R\x0blistDetails\x12\x16\n\x03ttl\x18\x07 \x01(\x03\x42\x04\x18\x01\x30\x01R\x03ttl\x12=\n\x0c\x64\x61te_created\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x64\x61teCreated\x12\x1d\n\nis_deleted\x18\t \x01(\x08R\tisDeleted\x12\x36\n\x06status\x18\n \x01(\x0e\x32\x1e.api.commons.ContactListStatusR\x06status\x12\x39\n\x19\x63ontact_manager_list_name\x18\x0b \x01(\tR\x16\x63ontactManagerListName\"B\n\x16\x43ontactManagerEntryVal\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\"\xbb\x02\n\x16\x41\x64\x64\x43ontactEntryRequest\x12>\n\x17\x63ontact_manager_list_id\x18\x01 \x01(\x03\x42\x02\x30\x01H\x00R\x14\x63ontactManagerListId\x88\x01\x01\x12<\n\x05\x65ntry\x18\x02 \x03(\x0b\x32\".api.v1alpha1.contactmanager.EntryB\x02\x18\x01R\x05\x65ntry\x12#\n\x0bproject_sid\x18\x03 \x01(\x03\x42\x02\x30\x01R\nprojectSid\x12?\n\x05\x66ield\x18\x04 \x03(\x0b\x32).api.v1alpha1.contactmanager.ContactFieldR\x05\x66ield\x12!\n\x0c\x63ountry_code\x18\x05 \x01(\tR\x0b\x63ountryCodeB\x1a\n\x18_contact_manager_list_id\"I\n\x05\x45ntry\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type:\x02\x18\x01\"<\n\x17\x41\x64\x64\x43ontactEntryResponse\x12!\n\ncontact_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\tcontactId\"\xbc\x02\n\x17\x45\x64itContactEntryRequest\x12:\n\x17\x63ontact_manager_list_id\x18\x01 \x01(\x03H\x00R\x14\x63ontactManagerListId\x88\x01\x01\x12\x37\n\x18\x63ontact_manager_entry_id\x18\x02 \x01(\x03R\x15\x63ontactManagerEntryId\x12O\n\x0c\x65\x64ited_entry\x18\x03 \x03(\x0b\x32(.api.v1alpha1.contactmanager.EditedEntryB\x02\x18\x01R\x0b\x65\x64itedEntry\x12?\n\x05\x66ield\x18\x04 \x03(\x0b\x32).api.v1alpha1.contactmanager.ContactFieldR\x05\x66ieldB\x1a\n\x18_contact_manager_list_id\"\x91\x01\n\x0b\x45\x64itedEntry\x12@\n\x1d\x63ontact_manager_entry_list_id\x18\x01 \x01(\x03R\x19\x63ontactManagerEntryListId\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x14\n\x05value\x18\x03 \x01(\tR\x05value\x12\x12\n\x04type\x18\x04 \x01(\tR\x04type:\x02\x18\x01\"L\n\x0c\x43ontactField\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value\x12\x12\n\x04type\x18\x03 \x01(\tR\x04type\"[\n\x18\x45\x64itContactEntryResponse\x12?\n\x05\x66ield\x18\x01 \x03(\x0b\x32).api.v1alpha1.contactmanager.ContactFieldR\x05\x66ield\"]\n\x1bListContactsByEntityRequest\x12!\n\nproject_id\x18\x01 \x01(\x03\x42\x02\x30\x01R\tprojectId\x12\x1b\n\tentity_id\x18\x02 \x01(\tR\x08\x65ntityId\"\x84\x01\n\x1cListContactsByEntityResponse\x12\x64\n\x15\x63ontact_manager_entry\x18\x01 \x03(\x0b\x32\x30.api.v1alpha1.contactmanager.ContactManagerEntryR\x13\x63ontactManagerEntry\"\xb2\x01\n\x1aGetContactFieldTypeRequest\x12\x1d\n\nfield_name\x18\x01 \x01(\tR\tfieldName\x12\x1f\n\x0b\x66ield_value\x18\x02 \x01(\tR\nfieldValue\x12\x45\n\nfield_type\x18\x03 \x01(\x0e\x32!.api.commons.ClassifierEntityTypeH\x00R\tfieldType\x88\x01\x01\x42\r\n\x0b_field_type\"_\n\x1bGetContactFieldTypeResponse\x12@\n\nfield_type\x18\x01 \x01(\x0e\x32!.api.commons.ClassifierEntityTypeR\tfieldType\"\x92\x01\n\x1dListContactActivityLogRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12;\n\x18\x63ontact_manager_entry_id\x18\x03 \x01(\x03\x42\x02\x30\x01R\x15\x63ontactManagerEntryId\"\x83\x01\n\x1eListContactActivityLogResponse\x12\x61\n\x14\x63ontact_activity_log\x18\x01 \x03(\x0b\x32/.api.v1alpha1.contactmanager.ContactActivityLogR\x12\x63ontactActivityLog\"\xdb\x01\n\x12\x43ontactActivityLog\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x1d\n\nproject_id\x18\x02 \x01(\tR\tprojectId\x12;\n\x18\x63ontact_manager_entry_id\x18\x03 \x01(\x03\x42\x02\x30\x01R\x15\x63ontactManagerEntryId\x12\x1d\n\nevent_user\x18\x04 \x01(\tR\teventUser\x12\x33\n\x05\x65vent\x18\x05 \x01(\x0b\x32\x1d.api.commons.audit.AuditEventR\x05\x65ventB\xc4\x01\n\x1f\x63om.api.v1alpha1.contactmanagerB\x13\x43ontactmanagerProtoP\x01\xa2\x02\x03\x41VC\xaa\x02\x1b\x41pi.V1alpha1.Contactmanager\xca\x02\x1b\x41pi\\V1alpha1\\Contactmanager\xe2\x02\'Api\\V1alpha1\\Contactmanager\\GPBMetadata\xea\x02\x1d\x41pi::V1alpha1::Contactmanagerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.contactmanager.contactmanager_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.api.v1alpha1.contactmanagerB\023ContactmanagerProtoP\001\242\002\003AVC\252\002\033Api.V1alpha1.Contactmanager\312\002\033Api\\V1alpha1\\Contactmanager\342\002\'Api\\V1alpha1\\Contactmanager\\GPBMetadata\352\002\035Api::V1alpha1::Contactmanager'
  _globals['_GETCONTACTLISTREQUEST'].fields_by_name['project_id']._loaded_options = None
  _globals['_GETCONTACTLISTREQUEST'].fields_by_name['project_id']._serialized_options = b'0\001'
  _globals['_LISTCONTACTENTRYLISTREQUEST'].fields_by_name['contact_manager_list_id']._loaded_options = None
  _globals['_LISTCONTACTENTRYLISTREQUEST'].fields_by_name['contact_manager_list_id']._serialized_options = b'0\001'
  _globals['_LISTCONTACTENTRYLISTREQUEST'].fields_by_name['org_id']._loaded_options = None
  _globals['_LISTCONTACTENTRYLISTREQUEST'].fields_by_name['org_id']._serialized_options = b'\030\001'
  _globals['_LISTCONTACTENTRYLISTRESPONSE'].fields_by_name['contact_manager_entry']._loaded_options = None
  _globals['_LISTCONTACTENTRYLISTRESPONSE'].fields_by_name['contact_manager_entry']._serialized_options = b'\030\001'
  _globals['_GETENCCONTACTENTRYREQUEST'].fields_by_name['contact_manager_entry_id']._loaded_options = None
  _globals['_GETENCCONTACTENTRYREQUEST'].fields_by_name['contact_manager_entry_id']._serialized_options = b'0\001'
  _globals['_GETKYCENCCONTACTENTRYREQUEST'].fields_by_name['project_id']._loaded_options = None
  _globals['_GETKYCENCCONTACTENTRYREQUEST'].fields_by_name['project_id']._serialized_options = b'0\001'
  _globals['_GETKYCKEYSREQUEST'].fields_by_name['project_sid']._loaded_options = None
  _globals['_GETKYCKEYSREQUEST'].fields_by_name['project_sid']._serialized_options = b'0\001'
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['contact_manager_entry_id']._loaded_options = None
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['contact_manager_entry_id']._serialized_options = b'0\001'
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['contact_manager_entry_list_id']._loaded_options = None
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['contact_manager_entry_list_id']._serialized_options = b'\030\0010\001'
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['key']._loaded_options = None
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['key']._serialized_options = b'\030\001'
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['value']._loaded_options = None
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['value']._serialized_options = b'\030\001'
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['type']._loaded_options = None
  _globals['_CONTACTMANAGERENTRY'].fields_by_name['type']._serialized_options = b'\030\001'
  _globals['_CONTACTMANAGERLIST'].fields_by_name['contact_manager_list_id']._loaded_options = None
  _globals['_CONTACTMANAGERLIST'].fields_by_name['contact_manager_list_id']._serialized_options = b'0\001'
  _globals['_CONTACTMANAGERLIST'].fields_by_name['project_id']._loaded_options = None
  _globals['_CONTACTMANAGERLIST'].fields_by_name['project_id']._serialized_options = b'0\001'
  _globals['_CONTACTMANAGERLIST'].fields_by_name['file_name']._loaded_options = None
  _globals['_CONTACTMANAGERLIST'].fields_by_name['file_name']._serialized_options = b'\030\001'
  _globals['_CONTACTMANAGERLIST'].fields_by_name['list_details']._loaded_options = None
  _globals['_CONTACTMANAGERLIST'].fields_by_name['list_details']._serialized_options = b'\030\001'
  _globals['_CONTACTMANAGERLIST'].fields_by_name['ttl']._loaded_options = None
  _globals['_CONTACTMANAGERLIST'].fields_by_name['ttl']._serialized_options = b'\030\0010\001'
  _globals['_ADDCONTACTENTRYREQUEST'].fields_by_name['contact_manager_list_id']._loaded_options = None
  _globals['_ADDCONTACTENTRYREQUEST'].fields_by_name['contact_manager_list_id']._serialized_options = b'0\001'
  _globals['_ADDCONTACTENTRYREQUEST'].fields_by_name['entry']._loaded_options = None
  _globals['_ADDCONTACTENTRYREQUEST'].fields_by_name['entry']._serialized_options = b'\030\001'
  _globals['_ADDCONTACTENTRYREQUEST'].fields_by_name['project_sid']._loaded_options = None
  _globals['_ADDCONTACTENTRYREQUEST'].fields_by_name['project_sid']._serialized_options = b'0\001'
  _globals['_ENTRY']._loaded_options = None
  _globals['_ENTRY']._serialized_options = b'\030\001'
  _globals['_ADDCONTACTENTRYRESPONSE'].fields_by_name['contact_id']._loaded_options = None
  _globals['_ADDCONTACTENTRYRESPONSE'].fields_by_name['contact_id']._serialized_options = b'0\001'
  _globals['_EDITCONTACTENTRYREQUEST'].fields_by_name['edited_entry']._loaded_options = None
  _globals['_EDITCONTACTENTRYREQUEST'].fields_by_name['edited_entry']._serialized_options = b'\030\001'
  _globals['_EDITEDENTRY']._loaded_options = None
  _globals['_EDITEDENTRY']._serialized_options = b'\030\001'
  _globals['_LISTCONTACTSBYENTITYREQUEST'].fields_by_name['project_id']._loaded_options = None
  _globals['_LISTCONTACTSBYENTITYREQUEST'].fields_by_name['project_id']._serialized_options = b'0\001'
  _globals['_LISTCONTACTACTIVITYLOGREQUEST'].fields_by_name['contact_manager_entry_id']._loaded_options = None
  _globals['_LISTCONTACTACTIVITYLOGREQUEST'].fields_by_name['contact_manager_entry_id']._serialized_options = b'0\001'
  _globals['_CONTACTACTIVITYLOG'].fields_by_name['contact_manager_entry_id']._loaded_options = None
  _globals['_CONTACTACTIVITYLOG'].fields_by_name['contact_manager_entry_id']._serialized_options = b'0\001'
  _globals['_GETCONTACTLISTREQUEST']._serialized_start=244
  _globals['_GETCONTACTLISTREQUEST']._serialized_end=388
  _globals['_GETCONTACTLISTRESPONSE']._serialized_start=391
  _globals['_GETCONTACTLISTRESPONSE']._serialized_end=534
  _globals['_LISTCONTACTENTRYLISTREQUEST']._serialized_start=537
  _globals['_LISTCONTACTENTRYLISTREQUEST']._serialized_end=776
  _globals['_LISTCONTACTENTRYLISTRESPONSE']._serialized_start=779
  _globals['_LISTCONTACTENTRYLISTRESPONSE']._serialized_end=1053
  _globals['_GETENCCONTACTENTRYREQUEST']._serialized_start=1055
  _globals['_GETENCCONTACTENTRYREQUEST']._serialized_end=1143
  _globals['_GETENCCONTACTENTRYRESPONSE']._serialized_start=1146
  _globals['_GETENCCONTACTENTRYRESPONSE']._serialized_end=1297
  _globals['_GETKYCENCCONTACTENTRYREQUEST']._serialized_start=1300
  _globals['_GETKYCENCCONTACTENTRYREQUEST']._serialized_end=1491
  _globals['_GETKYCENCCONTACTENTRYRESPONSE']._serialized_start=1494
  _globals['_GETKYCENCCONTACTENTRYRESPONSE']._serialized_end=1640
  _globals['_GETKYCKEYSREQUEST']._serialized_start=1642
  _globals['_GETKYCKEYSREQUEST']._serialized_end=1698
  _globals['_GETKYCKEYSRESPONSE']._serialized_start=1700
  _globals['_GETKYCKEYSRESPONSE']._serialized_end=1768
  _globals['_CONTACTMANAGERENTRY']._serialized_start=1771
  _globals['_CONTACTMANAGERENTRY']._serialized_end=2355
  _globals['_CONTACTMANAGERLIST']._serialized_start=2358
  _globals['_CONTACTMANAGERLIST']._serialized_end=2834
  _globals['_CONTACTMANAGERENTRYVAL']._serialized_start=2836
  _globals['_CONTACTMANAGERENTRYVAL']._serialized_end=2902
  _globals['_ADDCONTACTENTRYREQUEST']._serialized_start=2905
  _globals['_ADDCONTACTENTRYREQUEST']._serialized_end=3220
  _globals['_ENTRY']._serialized_start=3222
  _globals['_ENTRY']._serialized_end=3295
  _globals['_ADDCONTACTENTRYRESPONSE']._serialized_start=3297
  _globals['_ADDCONTACTENTRYRESPONSE']._serialized_end=3357
  _globals['_EDITCONTACTENTRYREQUEST']._serialized_start=3360
  _globals['_EDITCONTACTENTRYREQUEST']._serialized_end=3676
  _globals['_EDITEDENTRY']._serialized_start=3679
  _globals['_EDITEDENTRY']._serialized_end=3824
  _globals['_CONTACTFIELD']._serialized_start=3826
  _globals['_CONTACTFIELD']._serialized_end=3902
  _globals['_EDITCONTACTENTRYRESPONSE']._serialized_start=3904
  _globals['_EDITCONTACTENTRYRESPONSE']._serialized_end=3995
  _globals['_LISTCONTACTSBYENTITYREQUEST']._serialized_start=3997
  _globals['_LISTCONTACTSBYENTITYREQUEST']._serialized_end=4090
  _globals['_LISTCONTACTSBYENTITYRESPONSE']._serialized_start=4093
  _globals['_LISTCONTACTSBYENTITYRESPONSE']._serialized_end=4225
  _globals['_GETCONTACTFIELDTYPEREQUEST']._serialized_start=4228
  _globals['_GETCONTACTFIELDTYPEREQUEST']._serialized_end=4406
  _globals['_GETCONTACTFIELDTYPERESPONSE']._serialized_start=4408
  _globals['_GETCONTACTFIELDTYPERESPONSE']._serialized_end=4503
  _globals['_LISTCONTACTACTIVITYLOGREQUEST']._serialized_start=4506
  _globals['_LISTCONTACTACTIVITYLOGREQUEST']._serialized_end=4652
  _globals['_LISTCONTACTACTIVITYLOGRESPONSE']._serialized_start=4655
  _globals['_LISTCONTACTACTIVITYLOGRESPONSE']._serialized_end=4786
  _globals['_CONTACTACTIVITYLOG']._serialized_start=4789
  _globals['_CONTACTACTIVITYLOG']._serialized_end=5008
# @@protoc_insertion_point(module_scope)
