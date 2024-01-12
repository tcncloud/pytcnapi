# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/integrations/portals.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons.integrations import integrations_pb2 as api_dot_commons_dot_integrations_dot_integrations__pb2
from api.commons import perms_pb2 as api_dot_commons_dot_perms__pb2
from api.v1alpha1.integrations import service_pb2 as api_dot_v1alpha1_dot_integrations_dot_service__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'api/v1alpha1/integrations/portals.proto\x12\x19\x61pi.v1alpha1.integrations\x1a\x17\x61nnotations/authz.proto\x1a+api/commons/integrations/integrations.proto\x1a\x17\x61pi/commons/perms.proto\x1a\'api/v1alpha1/integrations/service.proto\x1a\x1cgoogle/api/annotations.proto\x1a google/protobuf/field_mask.proto\"\x88\x01\n\x15UpsertPortalConfigReq\x12?\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\'.api.v1alpha1.integrations.PortalConfigR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"Z\n\x15UpsertPortalConfigRes\x12\x41\n\x06\x65ntity\x18\x01 \x01(\x0b\x32).api.v1alpha1.integrations.PortalConfigIdR\x06\x65ntity\"U\n\x12GetPortalConfigRes\x12?\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\'.api.v1alpha1.integrations.PortalConfigR\x06\x65ntity\"\x17\n\x15\x44\x65letePortalConfigRes\"\x83\x01\n\x14ListPortalConfigsRes\x12\x43\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\'.api.v1alpha1.integrations.PortalConfigR\x08\x65ntities\x12&\n\x0fnext_page_token\x18\x02 \x01(\tR\rnextPageToken\"\\\n\x19UpdatePortalConfigLogoReq\x12?\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\'.api.v1alpha1.integrations.PortalConfigR\x06\x65ntity\"\x1b\n\x19UpdatePortalConfigLogoRes\"[\n\x16GetPortalConfigLogoReq\x12\x41\n\x06\x65ntity\x18\x01 \x01(\x0b\x32).api.v1alpha1.integrations.PortalConfigIdR\x06\x65ntity\"0\n\x16GetPortalConfigLogoRes\x12\x16\n\x06\x65ntity\x18\x01 \x01(\x0cR\x06\x65ntity\"|\n\x0fUpsertPortalReq\x12\x39\n\x06\x65ntity\x18\x01 \x01(\x0b\x32!.api.v1alpha1.integrations.PortalR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"N\n\x0fUpsertPortalRes\x12;\n\x06\x65ntity\x18\x01 \x01(\x0b\x32#.api.v1alpha1.integrations.PortalIdR\x06\x65ntity\"{\n\x0cGetPortalReq\x12;\n\x06\x65ntity\x18\x01 \x01(\x0b\x32#.api.v1alpha1.integrations.PortalIdR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"I\n\x0cGetPortalRes\x12\x39\n\x06\x65ntity\x18\x01 \x01(\x0b\x32!.api.v1alpha1.integrations.PortalR\x06\x65ntity\"N\n\x0f\x44\x65letePortalReq\x12;\n\x06\x65ntity\x18\x01 \x01(\x0b\x32#.api.v1alpha1.integrations.PortalIdR\x06\x65ntity\"\x11\n\x0f\x44\x65letePortalRes\"\xed\x01\n\x0eListPortalsReq\x12;\n\x06\x65ntity\x18\x01 \x01(\x0b\x32#.api.v1alpha1.integrations.PortalIdR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x12\n\x04page\x18\x04 \x01(\x05R\x04page\x12=\n\x06ptypes\x18\x05 \x03(\x0b\x32%.api.v1alpha1.integrations.PortalTypeR\x06ptypes\"O\n\x0eListPortalsRes\x12=\n\x08\x65ntities\x18\x01 \x03(\x0b\x32!.api.v1alpha1.integrations.PortalR\x08\x65ntities\"\x9a\x03\n\x16ListDetailedPortalsReq\x12;\n\x06\x65ntity\x18\x01 \x01(\x0b\x32#.api.v1alpha1.integrations.PortalIdR\x06\x65ntity\x12;\n\x0bportal_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nportalMask\x12H\n\x12portal_config_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x10portalConfigMask\x12L\n\x14plugin_instance_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x12pluginInstanceMask\x12\x1b\n\tpage_size\x18\x05 \x01(\x05R\x08pageSize\x12\x12\n\x04page\x18\x06 \x01(\x05R\x04page\x12=\n\x06ptypes\x18\x07 \x03(\x0b\x32%.api.v1alpha1.integrations.PortalTypeR\x06ptypes\"\xd8\x02\n\x16ListDetailedPortalsRes\x12T\n\x08\x65ntities\x18\x04 \x03(\x0b\x32\x38.api.v1alpha1.integrations.ListDetailedPortalsRes.EntityR\x08\x65ntities\x1a\xe7\x01\n\x06\x45ntity\x12\x39\n\x06portal\x18\x01 \x01(\x0b\x32!.api.v1alpha1.integrations.PortalR\x06portal\x12L\n\rportal_config\x18\x02 \x01(\x0b\x32\'.api.v1alpha1.integrations.PortalConfigR\x0cportalConfig\x12T\n\x10plugin_instances\x18\x03 \x03(\x0b\x32).api.v1alpha1.integrations.PluginInstanceR\x0fpluginInstances\"\xa8\x02\n\x14GetDetailedPortalReq\x12;\n\x06\x65ntity\x18\x01 \x01(\x0b\x32#.api.v1alpha1.integrations.PortalIdR\x06\x65ntity\x12;\n\x0bportal_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\nportalMask\x12H\n\x12portal_config_mask\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x10portalConfigMask\x12L\n\x14plugin_instance_mask\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x12pluginInstanceMask\"\xd0\x02\n\x14GetDetailedPortalRes\x12N\n\x06\x65ntity\x18\x04 \x01(\x0b\x32\x36.api.v1alpha1.integrations.GetDetailedPortalRes.EntityR\x06\x65ntity\x1a\xe7\x01\n\x06\x45ntity\x12\x39\n\x06portal\x18\x01 \x01(\x0b\x32!.api.v1alpha1.integrations.PortalR\x06portal\x12L\n\rportal_config\x18\x02 \x01(\x0b\x32\'.api.v1alpha1.integrations.PortalConfigR\x0cportalConfig\x12T\n\x10plugin_instances\x18\x03 \x03(\x0b\x32).api.v1alpha1.integrations.PluginInstanceR\x0fpluginInstances\"\x8c\x01\n\x17UpsertPluginInstanceReq\x12\x41\n\x06\x65ntity\x18\x01 \x01(\x0b\x32).api.v1alpha1.integrations.PluginInstanceR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"^\n\x17UpsertPluginInstanceRes\x12\x43\n\x06\x65ntity\x18\x01 \x01(\x0b\x32+.api.v1alpha1.integrations.PluginInstanceIdR\x06\x65ntity\"\x8b\x01\n\x14GetPluginInstanceReq\x12\x43\n\x06\x65ntity\x18\x01 \x01(\x0b\x32+.api.v1alpha1.integrations.PluginInstanceIdR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"Y\n\x14GetPluginInstanceRes\x12\x41\n\x06\x65ntity\x18\x01 \x01(\x0b\x32).api.v1alpha1.integrations.PluginInstanceR\x06\x65ntity\"^\n\x17\x44\x65letePluginInstanceReq\x12\x43\n\x06\x65ntity\x18\x01 \x01(\x0b\x32+.api.v1alpha1.integrations.PluginInstanceIdR\x06\x65ntity\"\x19\n\x17\x44\x65letePluginInstanceRes\"\xbb\x01\n\x15ListPluginInstanceReq\x12\x41\n\x06\x65ntity\x18\x01 \x01(\x0b\x32).api.v1alpha1.integrations.PluginInstanceR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x12\n\x04page\x18\x04 \x01(\x05R\x04page\"^\n\x15ListPluginInstanceRes\x12\x45\n\x08\x65ntities\x18\x01 \x03(\x0b\x32).api.v1alpha1.integrations.PluginInstanceR\x08\x65ntities\"\x10\n\x0eListPluginsReq\"\x10\n\x0eListPluginsRes\"\xb6\x01\n\x12ListPortalLinksReq\x12?\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\'.api.v1alpha1.integrations.PortalLinkIdR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\x12\x1b\n\tpage_size\x18\x03 \x01(\x05R\x08pageSize\x12\x12\n\x04page\x18\x04 \x01(\x05R\x04page\"W\n\x12ListPortalLinksRes\x12\x41\n\x08\x65ntities\x18\x01 \x03(\x0b\x32%.api.v1alpha1.integrations.PortalLinkR\x08\x65ntities\"\x83\x01\n\x10GetPortalLinkReq\x12?\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\'.api.v1alpha1.integrations.PortalLinkIdR\x06\x65ntity\x12.\n\x04mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\x04mask\"Q\n\x10GetPortalLinkRes\x12=\n\x06\x65ntity\x18\x01 \x01(\x0b\x32%.api.v1alpha1.integrations.PortalLinkR\x06\x65ntity\"V\n\x13\x44\x65letePortalLinkReq\x12?\n\x06\x65ntity\x18\x01 \x01(\x0b\x32\'.api.v1alpha1.integrations.PortalLinkIdR\x06\x65ntity\"\x15\n\x13\x44\x65letePortalLinkRes\"\x93\x01\n\x14\x43reatePortalLinksReq\x12;\n\x06\x65ntity\x18\x01 \x01(\x0b\x32#.api.v1alpha1.integrations.PortalIdR\x06\x65ntity\x12>\n\nlink_datas\x18\x02 \x03(\x0b\x32\x1f.api.v1alpha1.integrations.TaskR\tlinkDatas\"*\n\x14\x43reatePortalLinksRes\x12\x12\n\x04urls\x18\x01 \x03(\tR\x04urls\"\xe0\x01\n\x15ListFlowFieldNamesReq\x12O\n\x06\x65ntity\x18\x05 \x01(\x0b\x32\x37.api.v1alpha1.integrations.ListFlowFieldNamesReq.EntityR\x06\x65ntity\x1av\n\x06\x45ntity\x12\x32\n\x04\x66low\x18\x03 \x01(\x0b\x32\x1e.api.commons.integrations.FlowR\x04\x66low\x12\x38\n\x03loc\x18\x04 \x01(\x0e\x32&.api.commons.integrations.FlowFieldLocR\x03loc\"8\n\x15ListFlowFieldNamesRes\x12\x1f\n\x0b\x66ield_names\x18\x01 \x03(\tR\nfieldNames\"t\n\"ListAvailableVerificationFieldsReq\x12N\n\x0cverification\x18\x01 \x01(\x0b\x32*.api.commons.integrations.VerificationFlowR\x0cverification\"\x80\x01\n\"ListAvailableVerificationFieldsRes\x12Z\n\x13verification_fields\x18\x02 \x03(\x0b\x32).api.commons.integrations.FieldDefinitionR\x12verificationFields\"`\n\x1dListAvailablePaymentFieldsReq\x12?\n\x07payment\x18\x01 \x01(\x0b\x32%.api.commons.integrations.PaymentFlowR\x07payment\"q\n\x1dListAvailablePaymentFieldsRes\x12P\n\x0epayment_fields\x18\x02 \x03(\x0b\x32).api.commons.integrations.FieldDefinitionR\rpaymentFields2\xda\"\n\x10PortalManagerApi\x12\xbd\x01\n\x12UpsertPortalConfig\x12\x30.api.v1alpha1.integrations.UpsertPortalConfigReq\x1a\x30.api.v1alpha1.integrations.UpsertPortalConfigRes\"C\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/portalmanager/upsertportalconfig:\x01*\x12\xb9\x01\n\x11ListPortalConfigs\x12/.api.v1alpha1.integrations.ListPortalConfigsReq\x1a/.api.v1alpha1.integrations.ListPortalConfigsRes\"B\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/portalmanager/listportalconfigs:\x01*\x12\xb1\x01\n\x0fGetPortalConfig\x12-.api.v1alpha1.integrations.GetPortalConfigReq\x1a-.api.v1alpha1.integrations.GetPortalConfigRes\"@\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/portalmanager/getportalconfig:\x01*\x12\xbd\x01\n\x12\x44\x65letePortalConfig\x12\x30.api.v1alpha1.integrations.DeletePortalConfigReq\x1a\x30.api.v1alpha1.integrations.DeletePortalConfigRes\"C\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/portalmanager/deleteportalconfig:\x01*\x12\xcd\x01\n\x16UpdatePortalConfigLogo\x12\x34.api.v1alpha1.integrations.UpdatePortalConfigLogoReq\x1a\x34.api.v1alpha1.integrations.UpdatePortalConfigLogoRes\"G\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x37\"2/api/v1alpha1/portalmanager/updateportalconfiglogo:\x01*\x12\xc1\x01\n\x13GetPortalConfigLogo\x12\x31.api.v1alpha1.integrations.GetPortalConfigLogoReq\x1a\x31.api.v1alpha1.integrations.GetPortalConfigLogoRes\"D\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/portalmanager/getportalconfiglogo:\x01*\x12\xb1\x01\n\x0fListPortalLinks\x12-.api.v1alpha1.integrations.ListPortalLinksReq\x1a-.api.v1alpha1.integrations.ListPortalLinksRes\"@\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/portalmanager/listportallinks:\x01*\x12\xa9\x01\n\rGetPortalLink\x12+.api.v1alpha1.integrations.GetPortalLinkReq\x1a+.api.v1alpha1.integrations.GetPortalLinkRes\">\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02.\")/api/v1alpha1/portalmanager/getportallink:\x01*\x12\xb5\x01\n\x10\x44\x65letePortalLink\x12..api.v1alpha1.integrations.DeletePortalLinkReq\x1a..api.v1alpha1.integrations.DeletePortalLinkRes\"A\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/portalmanager/deleteportallink:\x01*\x12\xc3\x01\n\x11\x43reatePortalLinks\x12/.api.v1alpha1.integrations.CreatePortalLinksReq\x1a/.api.v1alpha1.integrations.CreatePortalLinksRes\"L\xba\xb8\x91\x02\x0f\n\x03\x08\x94\n\n\x03\x08\xd4\x02\n\x03\x08\xba\t\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/portalmanager/createportallinks:\x01*\x12\xa5\x01\n\x0cUpsertPortal\x12*.api.v1alpha1.integrations.UpsertPortalReq\x1a*.api.v1alpha1.integrations.UpsertPortalRes\"=\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/portalmanager/upsertportal:\x01*\x12\xa3\x01\n\tGetPortal\x12\'.api.v1alpha1.integrations.GetPortalReq\x1a\'.api.v1alpha1.integrations.GetPortalRes\"D\xba\xb8\x91\x02\x0f\n\x03\x08\x94\n\n\x03\x08\xd4\x02\n\x03\x08\xba\t\x82\xd3\xe4\x93\x02*\"%/api/v1alpha1/portalmanager/getportal:\x01*\x12\xa5\x01\n\x0c\x44\x65letePortal\x12*.api.v1alpha1.integrations.DeletePortalReq\x1a*.api.v1alpha1.integrations.DeletePortalRes\"=\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02-\"(/api/v1alpha1/portalmanager/deleteportal:\x01*\x12\xab\x01\n\x0bListPortals\x12).api.v1alpha1.integrations.ListPortalsReq\x1a).api.v1alpha1.integrations.ListPortalsRes\"F\xba\xb8\x91\x02\x0f\n\x03\x08\x94\n\n\x03\x08\xd4\x02\n\x03\x08\xba\t\x82\xd3\xe4\x93\x02,\"\'/api/v1alpha1/portalmanager/listportals:\x01*\x12\xcb\x01\n\x13ListDetailedPortals\x12\x31.api.v1alpha1.integrations.ListDetailedPortalsReq\x1a\x31.api.v1alpha1.integrations.ListDetailedPortalsRes\"N\xba\xb8\x91\x02\x0f\n\x03\x08\x94\n\n\x03\x08\xd4\x02\n\x03\x08\xba\t\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/portalmanager/listdetailedportals:\x01*\x12\xc3\x01\n\x11GetDetailedPortal\x12/.api.v1alpha1.integrations.GetDetailedPortalReq\x1a/.api.v1alpha1.integrations.GetDetailedPortalRes\"L\xba\xb8\x91\x02\x0f\n\x03\x08\x94\n\n\x03\x08\xd4\x02\n\x03\x08\xba\t\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/portalmanager/getdetailedportal:\x01*\x12\xc5\x01\n\x14UpsertPluginInstance\x12\x32.api.v1alpha1.integrations.UpsertPluginInstanceReq\x1a\x32.api.v1alpha1.integrations.UpsertPluginInstanceRes\"E\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/portalmanager/upsertplugininstance:\x01*\x12\xb9\x01\n\x11GetPluginInstance\x12/.api.v1alpha1.integrations.GetPluginInstanceReq\x1a/.api.v1alpha1.integrations.GetPluginInstanceRes\"B\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x32\"-/api/v1alpha1/portalmanager/getplugininstance:\x01*\x12\xc5\x01\n\x14\x44\x65letePluginInstance\x12\x32.api.v1alpha1.integrations.DeletePluginInstanceReq\x1a\x32.api.v1alpha1.integrations.DeletePluginInstanceRes\"E\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/portalmanager/deleteplugininstance:\x01*\x12\xc3\x01\n\x12ListPluginInstance\x12\x30.api.v1alpha1.integrations.ListPluginInstanceReq\x1a\x30.api.v1alpha1.integrations.ListPluginInstanceRes\"I\xba\xb8\x91\x02\n\n\x03\x08\x94\n\n\x03\x08\xd6\x02\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/portalmanager/listplugininstances:\x01*\x12\xc7\x01\n\x12ListFlowFieldNames\x12\x30.api.v1alpha1.integrations.ListFlowFieldNamesReq\x1a\x30.api.v1alpha1.integrations.ListFlowFieldNamesRes\"M\xba\xb8\x91\x02\x0f\n\x03\x08\x94\n\n\x03\x08\xd4\x02\n\x03\x08\xba\t\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/portalmanager/listflowfieldnames:\x01*\x12\xf0\x01\n\x1fListAvailableVerificationFields\x12=.api.v1alpha1.integrations.ListAvailableVerificationFieldsReq\x1a=.api.v1alpha1.integrations.ListAvailableVerificationFieldsRes\"O\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02?\":/api/v1alpha1/integrations/listavailableverificationfields:\x01*\x12\xdc\x01\n\x1aListAvailablePaymentFields\x12\x38.api.v1alpha1.integrations.ListAvailablePaymentFieldsReq\x1a\x38.api.v1alpha1.integrations.ListAvailablePaymentFieldsRes\"J\xba\xb8\x91\x02\x05\n\x03\x08\x94\n\x82\xd3\xe4\x93\x02:\"5/api/v1alpha1/integrations/listavailablePaymentfields:\x01*B\xb3\x01\n\x1d\x63om.api.v1alpha1.integrationsB\x0cPortalsProtoP\x01\xa2\x02\x03\x41VI\xaa\x02\x19\x41pi.V1alpha1.Integrations\xca\x02\x19\x41pi\\V1alpha1\\Integrations\xe2\x02%Api\\V1alpha1\\Integrations\\GPBMetadata\xea\x02\x1b\x41pi::V1alpha1::Integrationsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.integrations.portals_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.api.v1alpha1.integrationsB\014PortalsProtoP\001\242\002\003AVI\252\002\031Api.V1alpha1.Integrations\312\002\031Api\\V1alpha1\\Integrations\342\002%Api\\V1alpha1\\Integrations\\GPBMetadata\352\002\033Api::V1alpha1::Integrations'
  _globals['_PORTALMANAGERAPI'].methods_by_name['UpsertPortalConfig']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['UpsertPortalConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0023\"./api/v1alpha1/portalmanager/upsertportalconfig:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListPortalConfigs']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListPortalConfigs']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0022\"-/api/v1alpha1/portalmanager/listportalconfigs:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetPortalConfig']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetPortalConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0020\"+/api/v1alpha1/portalmanager/getportalconfig:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['DeletePortalConfig']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['DeletePortalConfig']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0023\"./api/v1alpha1/portalmanager/deleteportalconfig:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['UpdatePortalConfigLogo']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['UpdatePortalConfigLogo']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0027\"2/api/v1alpha1/portalmanager/updateportalconfiglogo:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetPortalConfigLogo']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetPortalConfigLogo']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0024\"//api/v1alpha1/portalmanager/getportalconfiglogo:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListPortalLinks']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListPortalLinks']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0020\"+/api/v1alpha1/portalmanager/listportallinks:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetPortalLink']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetPortalLink']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\002.\")/api/v1alpha1/portalmanager/getportallink:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['DeletePortalLink']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['DeletePortalLink']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0021\",/api/v1alpha1/portalmanager/deleteportallink:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['CreatePortalLinks']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['CreatePortalLinks']._serialized_options = b'\272\270\221\002\017\n\003\010\224\n\n\003\010\324\002\n\003\010\272\t\202\323\344\223\0022\"-/api/v1alpha1/portalmanager/createportallinks:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['UpsertPortal']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['UpsertPortal']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\002-\"(/api/v1alpha1/portalmanager/upsertportal:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetPortal']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetPortal']._serialized_options = b'\272\270\221\002\017\n\003\010\224\n\n\003\010\324\002\n\003\010\272\t\202\323\344\223\002*\"%/api/v1alpha1/portalmanager/getportal:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['DeletePortal']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['DeletePortal']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\002-\"(/api/v1alpha1/portalmanager/deleteportal:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListPortals']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListPortals']._serialized_options = b'\272\270\221\002\017\n\003\010\224\n\n\003\010\324\002\n\003\010\272\t\202\323\344\223\002,\"\'/api/v1alpha1/portalmanager/listportals:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListDetailedPortals']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListDetailedPortals']._serialized_options = b'\272\270\221\002\017\n\003\010\224\n\n\003\010\324\002\n\003\010\272\t\202\323\344\223\0024\"//api/v1alpha1/portalmanager/listdetailedportals:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetDetailedPortal']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetDetailedPortal']._serialized_options = b'\272\270\221\002\017\n\003\010\224\n\n\003\010\324\002\n\003\010\272\t\202\323\344\223\0022\"-/api/v1alpha1/portalmanager/getdetailedportal:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['UpsertPluginInstance']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['UpsertPluginInstance']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0025\"0/api/v1alpha1/portalmanager/upsertplugininstance:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetPluginInstance']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['GetPluginInstance']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0022\"-/api/v1alpha1/portalmanager/getplugininstance:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['DeletePluginInstance']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['DeletePluginInstance']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\0025\"0/api/v1alpha1/portalmanager/deleteplugininstance:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListPluginInstance']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListPluginInstance']._serialized_options = b'\272\270\221\002\n\n\003\010\224\n\n\003\010\326\002\202\323\344\223\0024\"//api/v1alpha1/portalmanager/listplugininstances:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListFlowFieldNames']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListFlowFieldNames']._serialized_options = b'\272\270\221\002\017\n\003\010\224\n\n\003\010\324\002\n\003\010\272\t\202\323\344\223\0023\"./api/v1alpha1/portalmanager/listflowfieldnames:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListAvailableVerificationFields']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListAvailableVerificationFields']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\002?\":/api/v1alpha1/integrations/listavailableverificationfields:\001*'
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListAvailablePaymentFields']._options = None
  _globals['_PORTALMANAGERAPI'].methods_by_name['ListAvailablePaymentFields']._serialized_options = b'\272\270\221\002\005\n\003\010\224\n\202\323\344\223\002:\"5/api/v1alpha1/integrations/listavailablePaymentfields:\001*'
  _globals['_UPSERTPORTALCONFIGREQ']._serialized_start=271
  _globals['_UPSERTPORTALCONFIGREQ']._serialized_end=407
  _globals['_UPSERTPORTALCONFIGRES']._serialized_start=409
  _globals['_UPSERTPORTALCONFIGRES']._serialized_end=499
  _globals['_GETPORTALCONFIGRES']._serialized_start=501
  _globals['_GETPORTALCONFIGRES']._serialized_end=586
  _globals['_DELETEPORTALCONFIGRES']._serialized_start=588
  _globals['_DELETEPORTALCONFIGRES']._serialized_end=611
  _globals['_LISTPORTALCONFIGSRES']._serialized_start=614
  _globals['_LISTPORTALCONFIGSRES']._serialized_end=745
  _globals['_UPDATEPORTALCONFIGLOGOREQ']._serialized_start=747
  _globals['_UPDATEPORTALCONFIGLOGOREQ']._serialized_end=839
  _globals['_UPDATEPORTALCONFIGLOGORES']._serialized_start=841
  _globals['_UPDATEPORTALCONFIGLOGORES']._serialized_end=868
  _globals['_GETPORTALCONFIGLOGOREQ']._serialized_start=870
  _globals['_GETPORTALCONFIGLOGOREQ']._serialized_end=961
  _globals['_GETPORTALCONFIGLOGORES']._serialized_start=963
  _globals['_GETPORTALCONFIGLOGORES']._serialized_end=1011
  _globals['_UPSERTPORTALREQ']._serialized_start=1013
  _globals['_UPSERTPORTALREQ']._serialized_end=1137
  _globals['_UPSERTPORTALRES']._serialized_start=1139
  _globals['_UPSERTPORTALRES']._serialized_end=1217
  _globals['_GETPORTALREQ']._serialized_start=1219
  _globals['_GETPORTALREQ']._serialized_end=1342
  _globals['_GETPORTALRES']._serialized_start=1344
  _globals['_GETPORTALRES']._serialized_end=1417
  _globals['_DELETEPORTALREQ']._serialized_start=1419
  _globals['_DELETEPORTALREQ']._serialized_end=1497
  _globals['_DELETEPORTALRES']._serialized_start=1499
  _globals['_DELETEPORTALRES']._serialized_end=1516
  _globals['_LISTPORTALSREQ']._serialized_start=1519
  _globals['_LISTPORTALSREQ']._serialized_end=1756
  _globals['_LISTPORTALSRES']._serialized_start=1758
  _globals['_LISTPORTALSRES']._serialized_end=1837
  _globals['_LISTDETAILEDPORTALSREQ']._serialized_start=1840
  _globals['_LISTDETAILEDPORTALSREQ']._serialized_end=2250
  _globals['_LISTDETAILEDPORTALSRES']._serialized_start=2253
  _globals['_LISTDETAILEDPORTALSRES']._serialized_end=2597
  _globals['_LISTDETAILEDPORTALSRES_ENTITY']._serialized_start=2366
  _globals['_LISTDETAILEDPORTALSRES_ENTITY']._serialized_end=2597
  _globals['_GETDETAILEDPORTALREQ']._serialized_start=2600
  _globals['_GETDETAILEDPORTALREQ']._serialized_end=2896
  _globals['_GETDETAILEDPORTALRES']._serialized_start=2899
  _globals['_GETDETAILEDPORTALRES']._serialized_end=3235
  _globals['_GETDETAILEDPORTALRES_ENTITY']._serialized_start=2366
  _globals['_GETDETAILEDPORTALRES_ENTITY']._serialized_end=2597
  _globals['_UPSERTPLUGININSTANCEREQ']._serialized_start=3238
  _globals['_UPSERTPLUGININSTANCEREQ']._serialized_end=3378
  _globals['_UPSERTPLUGININSTANCERES']._serialized_start=3380
  _globals['_UPSERTPLUGININSTANCERES']._serialized_end=3474
  _globals['_GETPLUGININSTANCEREQ']._serialized_start=3477
  _globals['_GETPLUGININSTANCEREQ']._serialized_end=3616
  _globals['_GETPLUGININSTANCERES']._serialized_start=3618
  _globals['_GETPLUGININSTANCERES']._serialized_end=3707
  _globals['_DELETEPLUGININSTANCEREQ']._serialized_start=3709
  _globals['_DELETEPLUGININSTANCEREQ']._serialized_end=3803
  _globals['_DELETEPLUGININSTANCERES']._serialized_start=3805
  _globals['_DELETEPLUGININSTANCERES']._serialized_end=3830
  _globals['_LISTPLUGININSTANCEREQ']._serialized_start=3833
  _globals['_LISTPLUGININSTANCEREQ']._serialized_end=4020
  _globals['_LISTPLUGININSTANCERES']._serialized_start=4022
  _globals['_LISTPLUGININSTANCERES']._serialized_end=4116
  _globals['_LISTPLUGINSREQ']._serialized_start=4118
  _globals['_LISTPLUGINSREQ']._serialized_end=4134
  _globals['_LISTPLUGINSRES']._serialized_start=4136
  _globals['_LISTPLUGINSRES']._serialized_end=4152
  _globals['_LISTPORTALLINKSREQ']._serialized_start=4155
  _globals['_LISTPORTALLINKSREQ']._serialized_end=4337
  _globals['_LISTPORTALLINKSRES']._serialized_start=4339
  _globals['_LISTPORTALLINKSRES']._serialized_end=4426
  _globals['_GETPORTALLINKREQ']._serialized_start=4429
  _globals['_GETPORTALLINKREQ']._serialized_end=4560
  _globals['_GETPORTALLINKRES']._serialized_start=4562
  _globals['_GETPORTALLINKRES']._serialized_end=4643
  _globals['_DELETEPORTALLINKREQ']._serialized_start=4645
  _globals['_DELETEPORTALLINKREQ']._serialized_end=4731
  _globals['_DELETEPORTALLINKRES']._serialized_start=4733
  _globals['_DELETEPORTALLINKRES']._serialized_end=4754
  _globals['_CREATEPORTALLINKSREQ']._serialized_start=4757
  _globals['_CREATEPORTALLINKSREQ']._serialized_end=4904
  _globals['_CREATEPORTALLINKSRES']._serialized_start=4906
  _globals['_CREATEPORTALLINKSRES']._serialized_end=4948
  _globals['_LISTFLOWFIELDNAMESREQ']._serialized_start=4951
  _globals['_LISTFLOWFIELDNAMESREQ']._serialized_end=5175
  _globals['_LISTFLOWFIELDNAMESREQ_ENTITY']._serialized_start=5057
  _globals['_LISTFLOWFIELDNAMESREQ_ENTITY']._serialized_end=5175
  _globals['_LISTFLOWFIELDNAMESRES']._serialized_start=5177
  _globals['_LISTFLOWFIELDNAMESRES']._serialized_end=5233
  _globals['_LISTAVAILABLEVERIFICATIONFIELDSREQ']._serialized_start=5235
  _globals['_LISTAVAILABLEVERIFICATIONFIELDSREQ']._serialized_end=5351
  _globals['_LISTAVAILABLEVERIFICATIONFIELDSRES']._serialized_start=5354
  _globals['_LISTAVAILABLEVERIFICATIONFIELDSRES']._serialized_end=5482
  _globals['_LISTAVAILABLEPAYMENTFIELDSREQ']._serialized_start=5484
  _globals['_LISTAVAILABLEPAYMENTFIELDSREQ']._serialized_end=5580
  _globals['_LISTAVAILABLEPAYMENTFIELDSRES']._serialized_start=5582
  _globals['_LISTAVAILABLEPAYMENTFIELDSRES']._serialized_end=5695
  _globals['_PORTALMANAGERAPI']._serialized_start=5698
  _globals['_PORTALMANAGERAPI']._serialized_end=10140
# @@protoc_insertion_point(module_scope)
