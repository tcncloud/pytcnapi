# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/delivery/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import delivery_pb2 as api_dot_commons_dot_delivery__pb2
from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#api/v1alpha1/delivery/service.proto\x12\x15\x61pi.v1alpha1.delivery\x1a\x17\x61nnotations/authz.proto\x1a\x1a\x61pi/commons/delivery.proto\x1a\x15\x61pi/commons/org.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x88\x01\n\x17\x43reateTransferConfigReq\x12=\n\x06\x65ntity\x18\x01 \x01(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"L\n\x17\x43reateTransferConfigRes\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x19.api.v1alpha1.delivery.IDR\x06\x65ntity\"\xc2\x01\n\x16ListTransferConfigsReq\x12=\n\x06\x65ntity\x18\x01 \x01(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\x12\x39\n\x08list_req\x18\x03 \x01(\x0b\x32\x1e.api.v1alpha1.delivery.ListReqR\x07listReq\"[\n\x16ListTransferConfigsRes\x12\x41\n\x08\x65ntities\x18\x01 \x03(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x08\x65ntities\"\x92\x02\n$ListTransferConfigsByCredentialIDReq\x12=\n\x06\x65ntity\x18\x01 \x01(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\x12@\n\x0e\x63redential_sid\x18\x03 \x01(\x0b\x32\x19.api.v1alpha1.delivery.IDR\rcredentialSid\x12\x39\n\x08list_req\x18\x04 \x01(\x0b\x32\x1e.api.v1alpha1.delivery.ListReqR\x07listReq\"i\n$ListTransferConfigsByCredentialIDRes\x12\x41\n\x08\x65ntities\x18\x01 \x03(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x08\x65ntities\"\x88\x01\n\x17UpdateTransferConfigReq\x12=\n\x06\x65ntity\x18\x01 \x01(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"L\n\x17UpdateTransferConfigRes\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x19.api.v1alpha1.delivery.IDR\x06\x65ntity\"\x88\x01\n\x17\x44\x65leteTransferConfigReq\x12=\n\x06\x65ntity\x18\x01 \x01(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"\x19\n\x17\x44\x65leteTransferConfigRes\"\x85\x01\n\x14GetTransferConfigReq\x12=\n\x06\x65ntity\x18\x01 \x01(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"U\n\x14GetTransferConfigRes\x12=\n\x06\x65ntity\x18\x01 \x01(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x06\x65ntity\"\x9f\x01\n\x1aGetTransferConfigByNameReq\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\x12=\n\x06\x65ntity\x18\x03 \x01(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x06\x65ntity\"[\n\x1aGetTransferConfigByNameRes\x12=\n\x06\x65ntity\x18\x01 \x01(\x0b\x32%.api.v1alpha1.delivery.TransferConfigR\x06\x65ntity\"\xb3\x01\n\x0eListHistoryReq\x12\x36\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.delivery.HistoryR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\x12\x39\n\x08list_req\x18\x03 \x01(\x0b\x32\x1e.api.v1alpha1.delivery.ListReqR\x07listReq\"L\n\x0eListHistoryRes\x12:\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x1e.api.v1alpha1.delivery.HistoryR\x08\x65ntities\"\x8c\x01\n\x1eListHistoryByTransferConfigReq\x12:\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\".api.v1alpha1.delivery.ListByIDReqR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"\\\n\x1eListHistoryByTransferConfigRes\x12:\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x1e.api.v1alpha1.delivery.HistoryR\x08\x65ntities\"z\n\x10\x43reateHistoryReq\x12\x36\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.delivery.HistoryR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"E\n\x10\x43reateHistoryRes\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x19.api.v1alpha1.delivery.IDR\x06\x65ntity\"r\n\rGetHistoryReq\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x19.api.v1alpha1.delivery.IDR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"G\n\rGetHistoryRes\x12\x36\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.delivery.HistoryR\x06\x65ntity\"\xa6\x03\n\x0eTransferConfig\x12\x14\n\x03sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x03sid\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x10\n\x03ttl\x18\x07 \x01(\x05R\x03ttl\x12\x41\n\ncredential\x18\x08 \x01(\x0b\x32!.api.v1alpha1.delivery.CredentialR\ncredential\x12\x44\n\x0b\x64\x65stination\x18\t \x01(\x0b\x32\".api.v1alpha1.delivery.DestinationR\x0b\x64\x65stination\x12\x35\n\x06source\x18\n \x01(\x0b\x32\x1d.api.v1alpha1.delivery.SourceR\x06source\x12\x39\n\ncreated_on\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedOn\x12;\n\x0blast_edited\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastEdited\"\x1a\n\x02ID\x12\x14\n\x03sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x03sid\">\n\x07ListReq\x12\x1d\n\nbefore_sid\x18\x02 \x01(\x03R\tbeforeSid\x12\x14\n\x05limit\x18\x03 \x01(\x03R\x05limit\"\xdc\x03\n\x07History\x12\x14\n\x03sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x03sid\x12\x30\n\x14transfer_config_name\x18\x03 \x01(\tR\x12transferConfigName\x12\x32\n\x13transfer_config_sid\x18\x04 \x01(\x03\x42\x02\x30\x01R\x11transferConfigSid\x12#\n\rdelivery_type\x18\x05 \x01(\tR\x0c\x64\x65liveryType\x12\x14\n\x05\x65rror\x18\x06 \x01(\tR\x05\x65rror\x12\x18\n\x07success\x18\x07 \x01(\x08R\x07success\x12\x39\n\ncreated_on\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedOn\x12\x41\n\x0etransfer_start\x18\t \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rtransferStart\x12G\n\x11transfer_complete\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x10transferComplete\x12\x39\n\x06origin\x18\x0b \x01(\x0e\x32!.api.commons.OperatorApplicationsR\x06origin\"_\n\x0bListByIDReq\x12\x1d\n\nbefore_sid\x18\x02 \x01(\x03R\tbeforeSid\x12\x14\n\x05limit\x18\x03 \x01(\x03R\x05limit\x12\x1b\n\tother_sid\x18\x04 \x01(\x03R\x08otherSid\"\x8b\x02\n\nCredential\x12\x14\n\x03sid\x18\x01 \x01(\x03\x42\x02\x30\x01R\x03sid\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\x12\x39\n\x04\x64\x61ta\x18\x05 \x01(\x0b\x32%.api.v1alpha1.delivery.CredentialDataR\x04\x64\x61ta\x12\x39\n\ncreated_on\x18\n \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedOn\x12;\n\x0blast_edited\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.TimestampR\nlastEdited\"\xd0\x02\n\x0b\x44\x65stination\x12\x37\n\nencryption\x18\x01 \x01(\x0b\x32\x17.api.commons.EncryptionR\nencryption\x12?\n\x05\x65mail\x18\x02 \x01(\x0b\x32\'.api.v1alpha1.delivery.EmailDestinationH\x00R\x05\x65mail\x12\x45\n\x07room303\x18\x03 \x01(\x0b\x32).api.v1alpha1.delivery.Room303DestinationH\x00R\x07room303\x12\x39\n\x03sms\x18\x04 \x01(\x0b\x32%.api.v1alpha1.delivery.SmsDestinationH\x00R\x03sms\x12<\n\x04sftp\x18\x05 \x01(\x0b\x32&.api.v1alpha1.delivery.SftpDestinationH\x00R\x04sftpB\x07\n\x05value\"f\n\x0fSftpDestination\x12%\n\x0e\x62\x61se_directory\x18\x02 \x01(\tR\rbaseDirectory\x12\x18\n\x07\x61\x64\x64ress\x18\x03 \x01(\tR\x07\x61\x64\x64ress\x12\x12\n\x04port\x18\x04 \x01(\x05R\x04port\"D\n\x12Room303Destination\x12\x12\n\x04room\x18\x01 \x01(\tR\x04room\x12\x1a\n\x08username\x18\x02 \x01(\tR\x08username\"`\n\x0eSmsDestination\x12+\n\x11\x64\x65stination_phone\x18\x01 \x01(\tR\x10\x64\x65stinationPhone\x12!\n\x0csource_phone\x18\x02 \x01(\tR\x0bsourcePhone\"c\n\x10\x45mailDestination\x12\x17\n\x07to_addr\x18\x01 \x01(\tR\x06toAddr\x12\x19\n\x08\x63\x63_addrs\x18\x02 \x03(\tR\x07\x63\x63\x41\x64\x64rs\x12\x1b\n\tfrom_addr\x18\x03 \x01(\tR\x08\x66romAddr\"\xfa\x02\n\x0e\x43redentialData\x12J\n\ruser_password\x18\x01 \x01(\x0b\x32#.api.v1alpha1.delivery.UserPasswordH\x00R\x0cuserPassword\x12=\n\x08password\x18\x02 \x01(\x0b\x32\x1f.api.v1alpha1.delivery.PasswordH\x00R\x08password\x12\x45\n\x0cssh_key_pair\x18\x03 \x01(\x0b\x32!.api.v1alpha1.delivery.SSHKeyPairH\x00R\nsshKeyPair\x12\x45\n\x0cpgp_key_pair\x18\x04 \x01(\x0b\x32!.api.v1alpha1.delivery.PGPKeyPairH\x00R\npgpKeyPair\x12G\n\x0c\x61\x65s_password\x18\x05 \x01(\x0b\x32\".api.v1alpha1.delivery.AESPasswordH\x00R\x0b\x61\x65sPasswordB\x06\n\x04\x64\x61ta\"F\n\x0cUserPassword\x12\x1a\n\x08username\x18\x01 \x01(\tR\x08username\x12\x1a\n\x08password\x18\x02 \x01(\tR\x08password\"&\n\x08Password\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password\"L\n\nSSHKeyPair\x12\x1d\n\npublic_key\x18\x01 \x01(\tR\tpublicKey\x12\x1f\n\x0bprivate_key\x18\x02 \x01(\tR\nprivateKey\"L\n\nPGPKeyPair\x12\x1d\n\npublic_key\x18\x01 \x01(\tR\tpublicKey\x12\x1f\n\x0bprivate_key\x18\x02 \x01(\tR\nprivateKey\")\n\x0b\x41\x45SPassword\x12\x1a\n\x08password\x18\x01 \x01(\tR\x08password\"\x83\x01\n\x06Source\x12\x37\n\nencryption\x18\x01 \x01(\x0b\x32\x17.api.commons.EncryptionR\nencryption\x12\x37\n\x04sftp\x18\x02 \x01(\x0b\x32!.api.v1alpha1.delivery.SftpSourceH\x00R\x04sftpB\x07\n\x05value\"*\n\nSftpSource\x12\x1c\n\tdirectory\x18\x02 \x01(\tR\tdirectory\"}\n\x10GetCredentialReq\x12\x39\n\x06\x65ntity\x18\x01 \x01(\x0b\x32!.api.v1alpha1.delivery.CredentialR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"U\n\x10GetCredentialRes\x12\x41\n\ncredential\x18\x01 \x01(\x0b\x32!.api.v1alpha1.delivery.CredentialR\ncredential\"|\n\x12ListCredentialsReq\x12\x36\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x1e.api.v1alpha1.delivery.ListReqR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"Z\n\x12ListCredentialsRes\x12\x44\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32\".api.v1alpha1.delivery.CredentialsR\x0b\x63redentials\"\x80\x01\n\x13\x43reateCredentialReq\x12\x39\n\x06\x65ntity\x18\x01 \x01(\x0b\x32!.api.v1alpha1.delivery.CredentialR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"H\n\x13\x43reateCredentialRes\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x19.api.v1alpha1.delivery.IDR\x06\x65ntity\"x\n\x13\x44\x65leteCredentialReq\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x19.api.v1alpha1.delivery.IDR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"\x15\n\x13\x44\x65leteCredentialRes\"\x80\x01\n\x13UpdateCredentialReq\x12\x39\n\x06\x65ntity\x18\x01 \x01(\x0b\x32!.api.v1alpha1.delivery.CredentialR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"H\n\x13UpdateCredentialRes\x12\x31\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\x19.api.v1alpha1.delivery.IDR\x06\x65ntity\"L\n\x0b\x43redentials\x12=\n\x08\x65ntities\x18\x01 \x03(\x0b\x32!.api.v1alpha1.delivery.CredentialR\x08\x65ntities2\x8e\x14\n\x0b\x44\x65liveryApi\x12\xb8\x01\n\x14\x43reateTransferConfig\x12..api.v1alpha1.delivery.CreateTransferConfigReq\x1a..api.v1alpha1.delivery.CreateTransferConfigRes\"@\xba\xb8\x91\x02\x05\n\x03\x08\xd1\x0f\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/delivery/createtransferconfig:\x01*\x12\xb4\x01\n\x13ListTransferConfigs\x12-.api.v1alpha1.delivery.ListTransferConfigsReq\x1a-.api.v1alpha1.delivery.ListTransferConfigsRes\"?\xba\xb8\x91\x02\x05\n\x03\x08\xd0\x0f\x82\xd3\xe4\x93\x02/\"*/api/v1alpha1/delivery/listtransferconfigs:\x01*\x12\xec\x01\n!ListTransferConfigsByCredentialID\x12;.api.v1alpha1.delivery.ListTransferConfigsByCredentialIDReq\x1a;.api.v1alpha1.delivery.ListTransferConfigsByCredentialIDRes\"M\xba\xb8\x91\x02\x05\n\x03\x08\xd0\x0f\x82\xd3\xe4\x93\x02=\"8/api/v1alpha1/delivery/listtransferconfigsbycredentialid:\x01*\x12\xb8\x01\n\x14UpdateTransferConfig\x12..api.v1alpha1.delivery.UpdateTransferConfigReq\x1a..api.v1alpha1.delivery.UpdateTransferConfigRes\"@\xba\xb8\x91\x02\x05\n\x03\x08\xd1\x0f\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/delivery/updatetransferconfig:\x01*\x12\xb8\x01\n\x14\x44\x65leteTransferConfig\x12..api.v1alpha1.delivery.DeleteTransferConfigReq\x1a..api.v1alpha1.delivery.DeleteTransferConfigRes\"@\xba\xb8\x91\x02\x05\n\x03\x08\xd1\x0f\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/delivery/deletetransferconfig:\x01*\x12\xac\x01\n\x11GetTransferConfig\x12+.api.v1alpha1.delivery.GetTransferConfigReq\x1a+.api.v1alpha1.delivery.GetTransferConfigRes\"=\xba\xb8\x91\x02\x05\n\x03\x08\xd0\x0f\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/delivery/gettransferconfig:\x01*\x12\xc4\x01\n\x17GetTransferConfigByName\x12\x31.api.v1alpha1.delivery.GetTransferConfigByNameReq\x1a\x31.api.v1alpha1.delivery.GetTransferConfigByNameRes\"C\xba\xb8\x91\x02\x05\n\x03\x08\xd0\x0f\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/delivery/gettransferconfigbyname:\x01*\x12\x94\x01\n\x0bListHistory\x12%.api.v1alpha1.delivery.ListHistoryReq\x1a%.api.v1alpha1.delivery.ListHistoryRes\"7\xba\xb8\x91\x02\x05\n\x03\x08\xd0\x0f\x82\xd3\xe4\x93\x02\'\"\"/api/v1alpha1/delivery/listhistory:\x01*\x12\xd4\x01\n\x1bListHistoryByTransferConfig\x12\x35.api.v1alpha1.delivery.ListHistoryByTransferConfigReq\x1a\x35.api.v1alpha1.delivery.ListHistoryByTransferConfigRes\"G\xba\xb8\x91\x02\x05\n\x03\x08\xd0\x0f\x82\xd3\xe4\x93\x02\x37\"2/api/v1alpha1/delivery/listhistorybytransferconfig:\x01*\x12\xa3\x01\n\x0fListCredentials\x12).api.v1alpha1.delivery.ListCredentialsReq\x1a).api.v1alpha1.delivery.ListCredentialsRes\":\xba\xb8\x91\x02\x05\n\x03\x08\xd0\x0f\x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/delivery/listcredential:\x01*\x12\x9c\x01\n\rGetCredential\x12\'.api.v1alpha1.delivery.GetCredentialReq\x1a\'.api.v1alpha1.delivery.GetCredentialRes\"9\xba\xb8\x91\x02\x05\n\x03\x08\xd0\x0f\x82\xd3\xe4\x93\x02)\"$/api/v1alpha1/delivery/getcredential:\x01*\x12\xa8\x01\n\x10\x43reateCredential\x12*.api.v1alpha1.delivery.CreateCredentialReq\x1a*.api.v1alpha1.delivery.CreateCredentialRes\"<\xba\xb8\x91\x02\x05\n\x03\x08\xd1\x0f\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/delivery/createcredential:\x01*\x12\xa8\x01\n\x10\x44\x65leteCredential\x12*.api.v1alpha1.delivery.DeleteCredentialReq\x1a*.api.v1alpha1.delivery.DeleteCredentialRes\"<\xba\xb8\x91\x02\x05\n\x03\x08\xd1\x0f\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/delivery/deletecredential:\x01*\x12\xa8\x01\n\x10UpdateCredential\x12*.api.v1alpha1.delivery.UpdateCredentialReq\x1a*.api.v1alpha1.delivery.UpdateCredentialRes\"<\xba\xb8\x91\x02\x05\n\x03\x08\xd1\x0f\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/delivery/updatecredential:\x01*B\x9f\x01\n\x19\x63om.api.v1alpha1.deliveryB\x0cServiceProtoP\x01\xa2\x02\x03\x41VD\xaa\x02\x15\x41pi.V1alpha1.Delivery\xca\x02\x15\x41pi\\V1alpha1\\Delivery\xe2\x02!Api\\V1alpha1\\Delivery\\GPBMetadata\xea\x02\x17\x41pi::V1alpha1::Deliveryb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.delivery.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.api.v1alpha1.deliveryB\014ServiceProtoP\001\242\002\003AVD\252\002\025Api.V1alpha1.Delivery\312\002\025Api\\V1alpha1\\Delivery\342\002!Api\\V1alpha1\\Delivery\\GPBMetadata\352\002\027Api::V1alpha1::Delivery'
  _TRANSFERCONFIG.fields_by_name['sid']._options = None
  _TRANSFERCONFIG.fields_by_name['sid']._serialized_options = b'0\001'
  _ID.fields_by_name['sid']._options = None
  _ID.fields_by_name['sid']._serialized_options = b'0\001'
  _HISTORY.fields_by_name['sid']._options = None
  _HISTORY.fields_by_name['sid']._serialized_options = b'0\001'
  _HISTORY.fields_by_name['transfer_config_sid']._options = None
  _HISTORY.fields_by_name['transfer_config_sid']._serialized_options = b'0\001'
  _CREDENTIAL.fields_by_name['sid']._options = None
  _CREDENTIAL.fields_by_name['sid']._serialized_options = b'0\001'
  _DELIVERYAPI.methods_by_name['CreateTransferConfig']._options = None
  _DELIVERYAPI.methods_by_name['CreateTransferConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\321\017\202\323\344\223\0020\"+/api/v1alpha1/delivery/createtransferconfig:\001*'
  _DELIVERYAPI.methods_by_name['ListTransferConfigs']._options = None
  _DELIVERYAPI.methods_by_name['ListTransferConfigs']._serialized_options = b'\272\270\221\002\005\n\003\010\320\017\202\323\344\223\002/\"*/api/v1alpha1/delivery/listtransferconfigs:\001*'
  _DELIVERYAPI.methods_by_name['ListTransferConfigsByCredentialID']._options = None
  _DELIVERYAPI.methods_by_name['ListTransferConfigsByCredentialID']._serialized_options = b'\272\270\221\002\005\n\003\010\320\017\202\323\344\223\002=\"8/api/v1alpha1/delivery/listtransferconfigsbycredentialid:\001*'
  _DELIVERYAPI.methods_by_name['UpdateTransferConfig']._options = None
  _DELIVERYAPI.methods_by_name['UpdateTransferConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\321\017\202\323\344\223\0020\"+/api/v1alpha1/delivery/updatetransferconfig:\001*'
  _DELIVERYAPI.methods_by_name['DeleteTransferConfig']._options = None
  _DELIVERYAPI.methods_by_name['DeleteTransferConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\321\017\202\323\344\223\0020\"+/api/v1alpha1/delivery/deletetransferconfig:\001*'
  _DELIVERYAPI.methods_by_name['GetTransferConfig']._options = None
  _DELIVERYAPI.methods_by_name['GetTransferConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\320\017\202\323\344\223\002-\"(/api/v1alpha1/delivery/gettransferconfig:\001*'
  _DELIVERYAPI.methods_by_name['GetTransferConfigByName']._options = None
  _DELIVERYAPI.methods_by_name['GetTransferConfigByName']._serialized_options = b'\272\270\221\002\005\n\003\010\320\017\202\323\344\223\0023\"./api/v1alpha1/delivery/gettransferconfigbyname:\001*'
  _DELIVERYAPI.methods_by_name['ListHistory']._options = None
  _DELIVERYAPI.methods_by_name['ListHistory']._serialized_options = b'\272\270\221\002\005\n\003\010\320\017\202\323\344\223\002\'\"\"/api/v1alpha1/delivery/listhistory:\001*'
  _DELIVERYAPI.methods_by_name['ListHistoryByTransferConfig']._options = None
  _DELIVERYAPI.methods_by_name['ListHistoryByTransferConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\320\017\202\323\344\223\0027\"2/api/v1alpha1/delivery/listhistorybytransferconfig:\001*'
  _DELIVERYAPI.methods_by_name['ListCredentials']._options = None
  _DELIVERYAPI.methods_by_name['ListCredentials']._serialized_options = b'\272\270\221\002\005\n\003\010\320\017\202\323\344\223\002*\"%/api/v1alpha1/delivery/listcredential:\001*'
  _DELIVERYAPI.methods_by_name['GetCredential']._options = None
  _DELIVERYAPI.methods_by_name['GetCredential']._serialized_options = b'\272\270\221\002\005\n\003\010\320\017\202\323\344\223\002)\"$/api/v1alpha1/delivery/getcredential:\001*'
  _DELIVERYAPI.methods_by_name['CreateCredential']._options = None
  _DELIVERYAPI.methods_by_name['CreateCredential']._serialized_options = b'\272\270\221\002\005\n\003\010\321\017\202\323\344\223\002,\"\'/api/v1alpha1/delivery/createcredential:\001*'
  _DELIVERYAPI.methods_by_name['DeleteCredential']._options = None
  _DELIVERYAPI.methods_by_name['DeleteCredential']._serialized_options = b'\272\270\221\002\005\n\003\010\321\017\202\323\344\223\002,\"\'/api/v1alpha1/delivery/deletecredential:\001*'
  _DELIVERYAPI.methods_by_name['UpdateCredential']._options = None
  _DELIVERYAPI.methods_by_name['UpdateCredential']._serialized_options = b'\272\270\221\002\005\n\003\010\321\017\202\323\344\223\002,\"\'/api/v1alpha1/delivery/updatecredential:\001*'
  _globals['_CREATETRANSFERCONFIGREQ']._serialized_start=236
  _globals['_CREATETRANSFERCONFIGREQ']._serialized_end=372
  _globals['_CREATETRANSFERCONFIGRES']._serialized_start=374
  _globals['_CREATETRANSFERCONFIGRES']._serialized_end=450
  _globals['_LISTTRANSFERCONFIGSREQ']._serialized_start=453
  _globals['_LISTTRANSFERCONFIGSREQ']._serialized_end=647
  _globals['_LISTTRANSFERCONFIGSRES']._serialized_start=649
  _globals['_LISTTRANSFERCONFIGSRES']._serialized_end=740
  _globals['_LISTTRANSFERCONFIGSBYCREDENTIALIDREQ']._serialized_start=743
  _globals['_LISTTRANSFERCONFIGSBYCREDENTIALIDREQ']._serialized_end=1017
  _globals['_LISTTRANSFERCONFIGSBYCREDENTIALIDRES']._serialized_start=1019
  _globals['_LISTTRANSFERCONFIGSBYCREDENTIALIDRES']._serialized_end=1124
  _globals['_UPDATETRANSFERCONFIGREQ']._serialized_start=1127
  _globals['_UPDATETRANSFERCONFIGREQ']._serialized_end=1263
  _globals['_UPDATETRANSFERCONFIGRES']._serialized_start=1265
  _globals['_UPDATETRANSFERCONFIGRES']._serialized_end=1341
  _globals['_DELETETRANSFERCONFIGREQ']._serialized_start=1344
  _globals['_DELETETRANSFERCONFIGREQ']._serialized_end=1480
  _globals['_DELETETRANSFERCONFIGRES']._serialized_start=1482
  _globals['_DELETETRANSFERCONFIGRES']._serialized_end=1507
  _globals['_GETTRANSFERCONFIGREQ']._serialized_start=1510
  _globals['_GETTRANSFERCONFIGREQ']._serialized_end=1643
  _globals['_GETTRANSFERCONFIGRES']._serialized_start=1645
  _globals['_GETTRANSFERCONFIGRES']._serialized_end=1730
  _globals['_GETTRANSFERCONFIGBYNAMEREQ']._serialized_start=1733
  _globals['_GETTRANSFERCONFIGBYNAMEREQ']._serialized_end=1892
  _globals['_GETTRANSFERCONFIGBYNAMERES']._serialized_start=1894
  _globals['_GETTRANSFERCONFIGBYNAMERES']._serialized_end=1985
  _globals['_LISTHISTORYREQ']._serialized_start=1988
  _globals['_LISTHISTORYREQ']._serialized_end=2167
  _globals['_LISTHISTORYRES']._serialized_start=2169
  _globals['_LISTHISTORYRES']._serialized_end=2245
  _globals['_LISTHISTORYBYTRANSFERCONFIGREQ']._serialized_start=2248
  _globals['_LISTHISTORYBYTRANSFERCONFIGREQ']._serialized_end=2388
  _globals['_LISTHISTORYBYTRANSFERCONFIGRES']._serialized_start=2390
  _globals['_LISTHISTORYBYTRANSFERCONFIGRES']._serialized_end=2482
  _globals['_CREATEHISTORYREQ']._serialized_start=2484
  _globals['_CREATEHISTORYREQ']._serialized_end=2606
  _globals['_CREATEHISTORYRES']._serialized_start=2608
  _globals['_CREATEHISTORYRES']._serialized_end=2677
  _globals['_GETHISTORYREQ']._serialized_start=2679
  _globals['_GETHISTORYREQ']._serialized_end=2793
  _globals['_GETHISTORYRES']._serialized_start=2795
  _globals['_GETHISTORYRES']._serialized_end=2866
  _globals['_TRANSFERCONFIG']._serialized_start=2869
  _globals['_TRANSFERCONFIG']._serialized_end=3291
  _globals['_ID']._serialized_start=3293
  _globals['_ID']._serialized_end=3319
  _globals['_LISTREQ']._serialized_start=3321
  _globals['_LISTREQ']._serialized_end=3383
  _globals['_HISTORY']._serialized_start=3386
  _globals['_HISTORY']._serialized_end=3862
  _globals['_LISTBYIDREQ']._serialized_start=3864
  _globals['_LISTBYIDREQ']._serialized_end=3959
  _globals['_CREDENTIAL']._serialized_start=3962
  _globals['_CREDENTIAL']._serialized_end=4229
  _globals['_DESTINATION']._serialized_start=4232
  _globals['_DESTINATION']._serialized_end=4568
  _globals['_SFTPDESTINATION']._serialized_start=4570
  _globals['_SFTPDESTINATION']._serialized_end=4672
  _globals['_ROOM303DESTINATION']._serialized_start=4674
  _globals['_ROOM303DESTINATION']._serialized_end=4742
  _globals['_SMSDESTINATION']._serialized_start=4744
  _globals['_SMSDESTINATION']._serialized_end=4840
  _globals['_EMAILDESTINATION']._serialized_start=4842
  _globals['_EMAILDESTINATION']._serialized_end=4941
  _globals['_CREDENTIALDATA']._serialized_start=4944
  _globals['_CREDENTIALDATA']._serialized_end=5322
  _globals['_USERPASSWORD']._serialized_start=5324
  _globals['_USERPASSWORD']._serialized_end=5394
  _globals['_PASSWORD']._serialized_start=5396
  _globals['_PASSWORD']._serialized_end=5434
  _globals['_SSHKEYPAIR']._serialized_start=5436
  _globals['_SSHKEYPAIR']._serialized_end=5512
  _globals['_PGPKEYPAIR']._serialized_start=5514
  _globals['_PGPKEYPAIR']._serialized_end=5590
  _globals['_AESPASSWORD']._serialized_start=5592
  _globals['_AESPASSWORD']._serialized_end=5633
  _globals['_SOURCE']._serialized_start=5636
  _globals['_SOURCE']._serialized_end=5767
  _globals['_SFTPSOURCE']._serialized_start=5769
  _globals['_SFTPSOURCE']._serialized_end=5811
  _globals['_GETCREDENTIALREQ']._serialized_start=5813
  _globals['_GETCREDENTIALREQ']._serialized_end=5938
  _globals['_GETCREDENTIALRES']._serialized_start=5940
  _globals['_GETCREDENTIALRES']._serialized_end=6025
  _globals['_LISTCREDENTIALSREQ']._serialized_start=6027
  _globals['_LISTCREDENTIALSREQ']._serialized_end=6151
  _globals['_LISTCREDENTIALSRES']._serialized_start=6153
  _globals['_LISTCREDENTIALSRES']._serialized_end=6243
  _globals['_CREATECREDENTIALREQ']._serialized_start=6246
  _globals['_CREATECREDENTIALREQ']._serialized_end=6374
  _globals['_CREATECREDENTIALRES']._serialized_start=6376
  _globals['_CREATECREDENTIALRES']._serialized_end=6448
  _globals['_DELETECREDENTIALREQ']._serialized_start=6450
  _globals['_DELETECREDENTIALREQ']._serialized_end=6570
  _globals['_DELETECREDENTIALRES']._serialized_start=6572
  _globals['_DELETECREDENTIALRES']._serialized_end=6593
  _globals['_UPDATECREDENTIALREQ']._serialized_start=6596
  _globals['_UPDATECREDENTIALREQ']._serialized_end=6724
  _globals['_UPDATECREDENTIALRES']._serialized_start=6726
  _globals['_UPDATECREDENTIALRES']._serialized_end=6798
  _globals['_CREDENTIALS']._serialized_start=6800
  _globals['_CREDENTIALS']._serialized_end=6876
  _globals['_DELIVERYAPI']._serialized_start=6879
  _globals['_DELIVERYAPI']._serialized_end=9453
# @@protoc_insertion_point(module_scope)
