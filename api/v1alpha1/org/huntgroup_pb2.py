# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/v1alpha1/org/huntgroup.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from api.commons.org import huntgroup_pb2 as api_dot_commons_dot_org_dot_huntgroup__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n api/v1alpha1/org/huntgroup.proto\x12\x10\x61pi.v1alpha1.org\x1a\x15\x61pi/commons/org.proto\x1a\x1f\x61pi/commons/org/huntgroup.proto\x1a google/protobuf/field_mask.proto\"~\n\x1bGetHuntGroupSettingsRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x39\n\nfield_mask\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x88\x05\n\x1cGetHuntGroupSettingsResponse\x12K\n\x10general_settings\x18\x01 \x01(\x0b\x32 .api.commons.org.GeneralSettingsR\x0fgeneralSettings\x12]\n\x16\x63ommunication_settings\x18\x02 \x01(\x0b\x32&.api.commons.org.CommunicationSettingsR\x15\x63ommunicationSettings\x12N\n\x11\x63\x61llback_settings\x18\x03 \x01(\x0b\x32!.api.commons.org.CallbackSettingsR\x10\x63\x61llbackSettings\x12X\n\x15preview_dial_settings\x18\x04 \x01(\x0b\x32$.api.commons.org.PreviewDialSettingsR\x13previewDialSettings\x12U\n\x14manual_dial_settings\x18\x05 \x01(\x0b\x32#.api.commons.org.ManualDialSettingsR\x12manualDialSettings\x12[\n\x16transfer_call_settings\x18\x06 \x01(\x0b\x32%.api.commons.org.TransferCallSettingsR\x14transferCallSettings\x12^\n\x17number_history_settings\x18\x07 \x01(\x0b\x32&.api.commons.org.NumberHistorySettingsR\x15numberHistorySettings\"\xeb\x05\n\x1eUpdateHuntGroupSettingsRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12K\n\x10general_settings\x18\x02 \x01(\x0b\x32 .api.commons.org.GeneralSettingsR\x0fgeneralSettings\x12]\n\x16\x63ommunication_settings\x18\x03 \x01(\x0b\x32&.api.commons.org.CommunicationSettingsR\x15\x63ommunicationSettings\x12N\n\x11\x63\x61llback_settings\x18\x04 \x01(\x0b\x32!.api.commons.org.CallbackSettingsR\x10\x63\x61llbackSettings\x12X\n\x15preview_dial_settings\x18\x05 \x01(\x0b\x32$.api.commons.org.PreviewDialSettingsR\x13previewDialSettings\x12U\n\x14manual_dial_settings\x18\x06 \x01(\x0b\x32#.api.commons.org.ManualDialSettingsR\x12manualDialSettings\x12[\n\x16transfer_call_settings\x18\x07 \x01(\x0b\x32%.api.commons.org.TransferCallSettingsR\x14transferCallSettings\x12^\n\x17number_history_settings\x18\x08 \x01(\x0b\x32&.api.commons.org.NumberHistorySettingsR\x15numberHistorySettings\x12\x39\n\nfield_mask\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"!\n\x1fUpdateHuntGroupSettingsResponse\"\x82\x01\n\x16\x43reateHuntGroupRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x32\n\x04type\x18\x03 \x01(\x0e\x32\x1e.api.commons.org.HuntGroupTypeR\x04type\"?\n\x17\x43reateHuntGroupResponse\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"\xb6\x01\n$UpdateHuntGroupGeneralDetailsRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x32\n\x04type\x18\x04 \x01(\x0e\x32\x1e.api.commons.org.HuntGroupTypeR\x04type\"\'\n%UpdateHuntGroupGeneralDetailsResponse\">\n\x16\x44\x65leteHuntGroupRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"\x19\n\x17\x44\x65leteHuntGroupResponse\"B\n\x1aGetHuntGroupDetailsRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"n\n\x1bGetHuntGroupDetailsResponse\x12O\n\x12hunt_group_details\x18\x01 \x01(\x0b\x32!.api.commons.org.HuntGroupDetailsR\x10huntGroupDetails\"\x1c\n\x1aListCallerIdBucketsRequest\"u\n\x1bListCallerIdBucketsResponse\x12V\n\x15\x63\x61ller_id_bucket_data\x18\x01 \x03(\x0b\x32#.api.commons.org.CallerIdBucketDataR\x12\x63\x61llerIdBucketData\"R\n\x19GetDataDipTemplateRequest\x12\x35\n\x17xml_client_property_sid\x18\x01 \x01(\x03R\x14xmlClientPropertySid\"X\n\x1aGetDataDipTemplateResponse\x12:\n\x08template\x18\x01 \x01(\x0b\x32\x1e.api.commons.org.DataDipConfigR\x08template\"]\n\x1bListDataDipTemplatesRequest\x12>\n\x06\x66ilter\x18\x01 \x01(\x0e\x32&.api.commons.DataDipTemplateFilterTypeR\x06\x66ilter\"\\\n\x1cListDataDipTemplatesResponse\x12<\n\ttemplates\x18\x01 \x03(\x0b\x32\x1e.api.commons.org.DataDipConfigR\ttemplates\"Z\n\x1c\x43reateDataDipTemplateRequest\x12:\n\x08template\x18\x01 \x01(\x0b\x32\x1e.api.commons.org.DataDipConfigR\x08template\"V\n\x1d\x43reateDataDipTemplateResponse\x12\x35\n\x17xml_client_property_sid\x18\x01 \x01(\x03R\x14xmlClientPropertySid\"q\n\x1cUpdateDataDipTemplateRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12:\n\x08template\x18\x02 \x01(\x0b\x32\x1e.api.commons.org.DataDipConfigR\x08template\"\x1f\n\x1dUpdateDataDipTemplateResponse\"l\n\x1c\x44\x65leteDataDipTemplateRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x35\n\x17xml_client_property_sid\x18\x02 \x01(\x03R\x14xmlClientPropertySid\"\x1f\n\x1d\x44\x65leteDataDipTemplateResponse\"\x8b\x01\n\x1a\x43opyDataDipTemplateRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x35\n\x17xml_client_property_sid\x18\x02 \x01(\x03R\x14xmlClientPropertySid\x12\x1f\n\x0b\x63onfig_name\x18\x03 \x01(\tR\nconfigName\"T\n\x1b\x43opyDataDipTemplateResponse\x12\x35\n\x17xml_client_property_sid\x18\x01 \x01(\x03R\x14xmlClientPropertySid\"\xc7\x01\n(CopyDataDipTemplateToOrganizationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x35\n\x17xml_client_property_sid\x18\x02 \x01(\x03R\x14xmlClientPropertySid\x12\x1f\n\x0b\x63onfig_name\x18\x03 \x01(\tR\nconfigName\x12,\n\x12\x64\x65stination_org_id\x18\x04 \x01(\tR\x10\x64\x65stinationOrgId\"+\n)CopyDataDipTemplateToOrganizationResponse\"#\n!ListAgentResponseAutoRulesRequest\"k\n\"ListAgentResponseAutoRulesResponse\x12\x45\n\x08rulesets\x18\x01 \x03(\x0b\x32).api.commons.org.AgentResponseAutoRuleSetR\x08rulesets\"j\n#CreateAgentResponseAutoRulesRequest\x12\x43\n\x07ruleset\x18\x01 \x01(\x0b\x32).api.commons.org.AgentResponseAutoRuleSetR\x07ruleset\"&\n$CreateAgentResponseAutoRulesResponse\"\x8a\x01\n#UpdateAgentResponseAutoRulesRequest\x12\x1e\n\nrulesetSid\x18\x01 \x01(\x03R\nrulesetSid\x12\x43\n\x07ruleset\x18\x02 \x01(\x0b\x32).api.commons.org.AgentResponseAutoRuleSetR\x07ruleset\"&\n$UpdateAgentResponseAutoRulesResponse\"E\n#DeleteAgentResponseAutoRulesRequest\x12\x1e\n\nrulesetSid\x18\x01 \x01(\x03R\nrulesetSid\"&\n$DeleteAgentResponseAutoRulesResponse\"T\n,GetHuntGroupClientInfoDisplayTemplateRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"w\n-GetHuntGroupClientInfoDisplayTemplateResponse\x12\x46\n\x08template\x18\x01 \x01(\x0b\x32*.api.commons.org.ClientInfoDisplayTemplateR\x08template\"\x9f\x01\n/CreateHuntGroupClientInfoDisplayTemplateRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x46\n\x08template\x18\x02 \x01(\x0b\x32*.api.commons.org.ClientInfoDisplayTemplateR\x08template\"U\n0CreateHuntGroupClientInfoDisplayTemplateResponse\x12!\n\x0ctemplate_sid\x18\x01 \x01(\x03R\x0btemplateSid\"\x9f\x01\n/UpdateHuntGroupClientInfoDisplayTemplateRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x46\n\x08template\x18\x02 \x01(\x0b\x32*.api.commons.org.ClientInfoDisplayTemplateR\x08template\"2\n0UpdateHuntGroupClientInfoDisplayTemplateResponse\"z\n/DeleteHuntGroupClientInfoDisplayTemplateRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12!\n\x0ctemplate_sid\x18\x02 \x01(\x03R\x0btemplateSid\"2\n0DeleteHuntGroupClientInfoDisplayTemplateResponse\"\xa2\x01\n-CopyHuntGroupClientInfoDisplayTemplateRequest\x12)\n\x11to_hunt_group_sid\x18\x01 \x01(\x03R\x0etoHuntGroupSid\x12\x46\n\x08template\x18\x02 \x01(\x0b\x32*.api.commons.org.ClientInfoDisplayTemplateR\x08template\"0\n.CopyHuntGroupClientInfoDisplayTemplateResponse\"x\n.CreateCampaignClientInfoDisplayTemplateRequest\x12\x46\n\x08template\x18\x01 \x01(\x0b\x32*.api.commons.org.ClientInfoDisplayTemplateR\x08template\"T\n/CreateCampaignClientInfoDisplayTemplateResponse\x12!\n\x0ctemplate_sid\x18\x01 \x01(\x03R\x0btemplateSid\"\x94\x02\n/ListHuntGroupsWithClientInfoTemplateDataRequest\x12`\n\x06\x66ilter\x18\x01 \x01(\x0e\x32H.api.v1alpha1.org.ListHuntGroupsWithClientInfoTemplateDataRequest.FilterR\x06\x66ilter\"\x7f\n\x06\x46ilter\x12\x16\n\x12\x46ILTER_UNSPECIFIED\x10\x00\x12\x0e\n\nFILTER_ALL\x10\x01\x12$\n FILTER_HUNT_GROUPS_WITH_TEMPLATE\x10\x02\x12\'\n#FILTER_HUNT_GROUPS_WITHOUT_TEMPLATE\x10\x03\"\xac\x01\n0ListHuntGroupsWithClientInfoTemplateDataResponse\x12x\n\x1ehunt_groups_with_template_data\x18\x01 \x03(\x0b\x32\x34.api.commons.org.HuntGroupWithClientInfoTemplateDataR\x1ahuntGroupsWithTemplateData\"D\n\x1cListHuntGroupWebLinksRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"V\n\x1dListHuntGroupWebLinksResponse\x12\x35\n\tweb_links\x18\x01 \x03(\x0b\x32\x18.api.commons.org.WebLinkR\x08webLinks\"\xac\x01\n\x1b\x43opyHuntGroupWebLinkRequest\x12-\n\x13\x66rom_hunt_group_sid\x18\x01 \x01(\x03R\x10\x66romHuntGroupSid\x12)\n\x11to_hunt_group_sid\x18\x02 \x01(\x03R\x0etoHuntGroupSid\x12\x33\n\x08web_link\x18\x03 \x01(\x0b\x32\x18.api.commons.org.WebLinkR\x07webLink\"\x1e\n\x1c\x43opyHuntGroupWebLinkResponse\"}\n\x1eUpdateHuntGroupWebLinksRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x35\n\tweb_links\x18\x02 \x03(\x0b\x32\x18.api.commons.org.WebLinkR\x08webLinks\"!\n\x1fUpdateHuntGroupWebLinksResponse\"c\n$ListHuntGroupIntegrationLinksRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\"_\n%ListHuntGroupIntegrationLinksResponse\x12\x36\n\x05links\x18\x01 \x03(\x0b\x32 .api.commons.org.IntegrationLinkR\x05links\"\x86\x01\n#CopyHuntGroupIntegrationLinkRequest\x12)\n\x11to_hunt_group_sid\x18\x01 \x01(\x03R\x0etoHuntGroupSid\x12\x34\n\x04link\x18\x02 \x01(\x0b\x32 .api.commons.org.IntegrationLinkR\x04link\"&\n$CopyHuntGroupIntegrationLinkResponse\"\x86\x01\n&UpdateHuntGroupIntegrationLinksRequest\x12\x36\n\x05links\x18\x01 \x03(\x0b\x32 .api.commons.org.IntegrationLinkR\x05links\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\")\n\'UpdateHuntGroupIntegrationLinksResponse\"@\n\x18ListAgentTriggersRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"a\n\x19ListAgentTriggersResponse\x12\x44\n\x0e\x61gent_triggers\x18\x01 \x03(\x0b\x32\x1d.api.commons.org.AgentTriggerR\ragentTriggers\"\xb7\x01\n\x17\x43opyAgentTriggerRequest\x12-\n\x13\x66rom_hunt_group_sid\x18\x01 \x01(\x03R\x10\x66romHuntGroupSid\x12)\n\x11to_hunt_group_sid\x18\x02 \x01(\x03R\x0etoHuntGroupSid\x12\x42\n\ragent_trigger\x18\x03 \x01(\x0b\x32\x1d.api.commons.org.AgentTriggerR\x0c\x61gentTrigger\"\x1a\n\x18\x43opyAgentTriggerResponse\"\x88\x01\n\x1aUpdateAgentTriggersRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x44\n\x0e\x61gent_triggers\x18\x02 \x03(\x0b\x32\x1d.api.commons.org.AgentTriggerR\ragentTriggers\"\x1d\n\x1bUpdateAgentTriggersResponse\"A\n\x19GetHuntGroupScriptRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"j\n\x1aGetHuntGroupScriptResponse\x12L\n\x11hunt_group_script\x18\x01 \x01(\x0b\x32 .api.commons.org.HuntGroupScriptR\x0fhuntGroupScript\"\x92\x01\n\x1c\x43reateHuntGroupScriptRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12L\n\x11hunt_group_script\x18\x02 \x01(\x0b\x32 .api.commons.org.HuntGroupScriptR\x0fhuntGroupScript\"\x1f\n\x1d\x43reateHuntGroupScriptResponse\"\x92\x01\n\x1cUpdateHuntGroupScriptRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12L\n\x11hunt_group_script\x18\x02 \x01(\x0b\x32 .api.commons.org.HuntGroupScriptR\x0fhuntGroupScript\"\x1f\n\x1dUpdateHuntGroupScriptResponse\"c\n\x1c\x44\x65leteHuntGroupScriptRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x1d\n\nscript_sid\x18\x02 \x01(\x03R\tscriptSid\"\x1f\n\x1d\x44\x65leteHuntGroupScriptResponseB\x88\x01\n\x14\x63om.api.v1alpha1.orgB\x0eHuntgroupProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.huntgroup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\016HuntgroupProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_GETHUNTGROUPSETTINGSREQUEST']._serialized_start=144
  _globals['_GETHUNTGROUPSETTINGSREQUEST']._serialized_end=270
  _globals['_GETHUNTGROUPSETTINGSRESPONSE']._serialized_start=273
  _globals['_GETHUNTGROUPSETTINGSRESPONSE']._serialized_end=921
  _globals['_UPDATEHUNTGROUPSETTINGSREQUEST']._serialized_start=924
  _globals['_UPDATEHUNTGROUPSETTINGSREQUEST']._serialized_end=1671
  _globals['_UPDATEHUNTGROUPSETTINGSRESPONSE']._serialized_start=1673
  _globals['_UPDATEHUNTGROUPSETTINGSRESPONSE']._serialized_end=1706
  _globals['_CREATEHUNTGROUPREQUEST']._serialized_start=1709
  _globals['_CREATEHUNTGROUPREQUEST']._serialized_end=1839
  _globals['_CREATEHUNTGROUPRESPONSE']._serialized_start=1841
  _globals['_CREATEHUNTGROUPRESPONSE']._serialized_end=1904
  _globals['_UPDATEHUNTGROUPGENERALDETAILSREQUEST']._serialized_start=1907
  _globals['_UPDATEHUNTGROUPGENERALDETAILSREQUEST']._serialized_end=2089
  _globals['_UPDATEHUNTGROUPGENERALDETAILSRESPONSE']._serialized_start=2091
  _globals['_UPDATEHUNTGROUPGENERALDETAILSRESPONSE']._serialized_end=2130
  _globals['_DELETEHUNTGROUPREQUEST']._serialized_start=2132
  _globals['_DELETEHUNTGROUPREQUEST']._serialized_end=2194
  _globals['_DELETEHUNTGROUPRESPONSE']._serialized_start=2196
  _globals['_DELETEHUNTGROUPRESPONSE']._serialized_end=2221
  _globals['_GETHUNTGROUPDETAILSREQUEST']._serialized_start=2223
  _globals['_GETHUNTGROUPDETAILSREQUEST']._serialized_end=2289
  _globals['_GETHUNTGROUPDETAILSRESPONSE']._serialized_start=2291
  _globals['_GETHUNTGROUPDETAILSRESPONSE']._serialized_end=2401
  _globals['_LISTCALLERIDBUCKETSREQUEST']._serialized_start=2403
  _globals['_LISTCALLERIDBUCKETSREQUEST']._serialized_end=2431
  _globals['_LISTCALLERIDBUCKETSRESPONSE']._serialized_start=2433
  _globals['_LISTCALLERIDBUCKETSRESPONSE']._serialized_end=2550
  _globals['_GETDATADIPTEMPLATEREQUEST']._serialized_start=2552
  _globals['_GETDATADIPTEMPLATEREQUEST']._serialized_end=2634
  _globals['_GETDATADIPTEMPLATERESPONSE']._serialized_start=2636
  _globals['_GETDATADIPTEMPLATERESPONSE']._serialized_end=2724
  _globals['_LISTDATADIPTEMPLATESREQUEST']._serialized_start=2726
  _globals['_LISTDATADIPTEMPLATESREQUEST']._serialized_end=2819
  _globals['_LISTDATADIPTEMPLATESRESPONSE']._serialized_start=2821
  _globals['_LISTDATADIPTEMPLATESRESPONSE']._serialized_end=2913
  _globals['_CREATEDATADIPTEMPLATEREQUEST']._serialized_start=2915
  _globals['_CREATEDATADIPTEMPLATEREQUEST']._serialized_end=3005
  _globals['_CREATEDATADIPTEMPLATERESPONSE']._serialized_start=3007
  _globals['_CREATEDATADIPTEMPLATERESPONSE']._serialized_end=3093
  _globals['_UPDATEDATADIPTEMPLATEREQUEST']._serialized_start=3095
  _globals['_UPDATEDATADIPTEMPLATEREQUEST']._serialized_end=3208
  _globals['_UPDATEDATADIPTEMPLATERESPONSE']._serialized_start=3210
  _globals['_UPDATEDATADIPTEMPLATERESPONSE']._serialized_end=3241
  _globals['_DELETEDATADIPTEMPLATEREQUEST']._serialized_start=3243
  _globals['_DELETEDATADIPTEMPLATEREQUEST']._serialized_end=3351
  _globals['_DELETEDATADIPTEMPLATERESPONSE']._serialized_start=3353
  _globals['_DELETEDATADIPTEMPLATERESPONSE']._serialized_end=3384
  _globals['_COPYDATADIPTEMPLATEREQUEST']._serialized_start=3387
  _globals['_COPYDATADIPTEMPLATEREQUEST']._serialized_end=3526
  _globals['_COPYDATADIPTEMPLATERESPONSE']._serialized_start=3528
  _globals['_COPYDATADIPTEMPLATERESPONSE']._serialized_end=3612
  _globals['_COPYDATADIPTEMPLATETOORGANIZATIONREQUEST']._serialized_start=3615
  _globals['_COPYDATADIPTEMPLATETOORGANIZATIONREQUEST']._serialized_end=3814
  _globals['_COPYDATADIPTEMPLATETOORGANIZATIONRESPONSE']._serialized_start=3816
  _globals['_COPYDATADIPTEMPLATETOORGANIZATIONRESPONSE']._serialized_end=3859
  _globals['_LISTAGENTRESPONSEAUTORULESREQUEST']._serialized_start=3861
  _globals['_LISTAGENTRESPONSEAUTORULESREQUEST']._serialized_end=3896
  _globals['_LISTAGENTRESPONSEAUTORULESRESPONSE']._serialized_start=3898
  _globals['_LISTAGENTRESPONSEAUTORULESRESPONSE']._serialized_end=4005
  _globals['_CREATEAGENTRESPONSEAUTORULESREQUEST']._serialized_start=4007
  _globals['_CREATEAGENTRESPONSEAUTORULESREQUEST']._serialized_end=4113
  _globals['_CREATEAGENTRESPONSEAUTORULESRESPONSE']._serialized_start=4115
  _globals['_CREATEAGENTRESPONSEAUTORULESRESPONSE']._serialized_end=4153
  _globals['_UPDATEAGENTRESPONSEAUTORULESREQUEST']._serialized_start=4156
  _globals['_UPDATEAGENTRESPONSEAUTORULESREQUEST']._serialized_end=4294
  _globals['_UPDATEAGENTRESPONSEAUTORULESRESPONSE']._serialized_start=4296
  _globals['_UPDATEAGENTRESPONSEAUTORULESRESPONSE']._serialized_end=4334
  _globals['_DELETEAGENTRESPONSEAUTORULESREQUEST']._serialized_start=4336
  _globals['_DELETEAGENTRESPONSEAUTORULESREQUEST']._serialized_end=4405
  _globals['_DELETEAGENTRESPONSEAUTORULESRESPONSE']._serialized_start=4407
  _globals['_DELETEAGENTRESPONSEAUTORULESRESPONSE']._serialized_end=4445
  _globals['_GETHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=4447
  _globals['_GETHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=4531
  _globals['_GETHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=4533
  _globals['_GETHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=4652
  _globals['_CREATEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=4655
  _globals['_CREATEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=4814
  _globals['_CREATEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=4816
  _globals['_CREATEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=4901
  _globals['_UPDATEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=4904
  _globals['_UPDATEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=5063
  _globals['_UPDATEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=5065
  _globals['_UPDATEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=5115
  _globals['_DELETEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=5117
  _globals['_DELETEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=5239
  _globals['_DELETEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=5241
  _globals['_DELETEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=5291
  _globals['_COPYHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=5294
  _globals['_COPYHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=5456
  _globals['_COPYHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=5458
  _globals['_COPYHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=5506
  _globals['_CREATECAMPAIGNCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=5508
  _globals['_CREATECAMPAIGNCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=5628
  _globals['_CREATECAMPAIGNCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=5630
  _globals['_CREATECAMPAIGNCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=5714
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATAREQUEST']._serialized_start=5717
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATAREQUEST']._serialized_end=5993
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATAREQUEST_FILTER']._serialized_start=5866
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATAREQUEST_FILTER']._serialized_end=5993
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATARESPONSE']._serialized_start=5996
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATARESPONSE']._serialized_end=6168
  _globals['_LISTHUNTGROUPWEBLINKSREQUEST']._serialized_start=6170
  _globals['_LISTHUNTGROUPWEBLINKSREQUEST']._serialized_end=6238
  _globals['_LISTHUNTGROUPWEBLINKSRESPONSE']._serialized_start=6240
  _globals['_LISTHUNTGROUPWEBLINKSRESPONSE']._serialized_end=6326
  _globals['_COPYHUNTGROUPWEBLINKREQUEST']._serialized_start=6329
  _globals['_COPYHUNTGROUPWEBLINKREQUEST']._serialized_end=6501
  _globals['_COPYHUNTGROUPWEBLINKRESPONSE']._serialized_start=6503
  _globals['_COPYHUNTGROUPWEBLINKRESPONSE']._serialized_end=6533
  _globals['_UPDATEHUNTGROUPWEBLINKSREQUEST']._serialized_start=6535
  _globals['_UPDATEHUNTGROUPWEBLINKSREQUEST']._serialized_end=6660
  _globals['_UPDATEHUNTGROUPWEBLINKSRESPONSE']._serialized_start=6662
  _globals['_UPDATEHUNTGROUPWEBLINKSRESPONSE']._serialized_end=6695
  _globals['_LISTHUNTGROUPINTEGRATIONLINKSREQUEST']._serialized_start=6697
  _globals['_LISTHUNTGROUPINTEGRATIONLINKSREQUEST']._serialized_end=6796
  _globals['_LISTHUNTGROUPINTEGRATIONLINKSRESPONSE']._serialized_start=6798
  _globals['_LISTHUNTGROUPINTEGRATIONLINKSRESPONSE']._serialized_end=6893
  _globals['_COPYHUNTGROUPINTEGRATIONLINKREQUEST']._serialized_start=6896
  _globals['_COPYHUNTGROUPINTEGRATIONLINKREQUEST']._serialized_end=7030
  _globals['_COPYHUNTGROUPINTEGRATIONLINKRESPONSE']._serialized_start=7032
  _globals['_COPYHUNTGROUPINTEGRATIONLINKRESPONSE']._serialized_end=7070
  _globals['_UPDATEHUNTGROUPINTEGRATIONLINKSREQUEST']._serialized_start=7073
  _globals['_UPDATEHUNTGROUPINTEGRATIONLINKSREQUEST']._serialized_end=7207
  _globals['_UPDATEHUNTGROUPINTEGRATIONLINKSRESPONSE']._serialized_start=7209
  _globals['_UPDATEHUNTGROUPINTEGRATIONLINKSRESPONSE']._serialized_end=7250
  _globals['_LISTAGENTTRIGGERSREQUEST']._serialized_start=7252
  _globals['_LISTAGENTTRIGGERSREQUEST']._serialized_end=7316
  _globals['_LISTAGENTTRIGGERSRESPONSE']._serialized_start=7318
  _globals['_LISTAGENTTRIGGERSRESPONSE']._serialized_end=7415
  _globals['_COPYAGENTTRIGGERREQUEST']._serialized_start=7418
  _globals['_COPYAGENTTRIGGERREQUEST']._serialized_end=7601
  _globals['_COPYAGENTTRIGGERRESPONSE']._serialized_start=7603
  _globals['_COPYAGENTTRIGGERRESPONSE']._serialized_end=7629
  _globals['_UPDATEAGENTTRIGGERSREQUEST']._serialized_start=7632
  _globals['_UPDATEAGENTTRIGGERSREQUEST']._serialized_end=7768
  _globals['_UPDATEAGENTTRIGGERSRESPONSE']._serialized_start=7770
  _globals['_UPDATEAGENTTRIGGERSRESPONSE']._serialized_end=7799
  _globals['_GETHUNTGROUPSCRIPTREQUEST']._serialized_start=7801
  _globals['_GETHUNTGROUPSCRIPTREQUEST']._serialized_end=7866
  _globals['_GETHUNTGROUPSCRIPTRESPONSE']._serialized_start=7868
  _globals['_GETHUNTGROUPSCRIPTRESPONSE']._serialized_end=7974
  _globals['_CREATEHUNTGROUPSCRIPTREQUEST']._serialized_start=7977
  _globals['_CREATEHUNTGROUPSCRIPTREQUEST']._serialized_end=8123
  _globals['_CREATEHUNTGROUPSCRIPTRESPONSE']._serialized_start=8125
  _globals['_CREATEHUNTGROUPSCRIPTRESPONSE']._serialized_end=8156
  _globals['_UPDATEHUNTGROUPSCRIPTREQUEST']._serialized_start=8159
  _globals['_UPDATEHUNTGROUPSCRIPTREQUEST']._serialized_end=8305
  _globals['_UPDATEHUNTGROUPSCRIPTRESPONSE']._serialized_start=8307
  _globals['_UPDATEHUNTGROUPSCRIPTRESPONSE']._serialized_end=8338
  _globals['_DELETEHUNTGROUPSCRIPTREQUEST']._serialized_start=8340
  _globals['_DELETEHUNTGROUPSCRIPTREQUEST']._serialized_end=8439
  _globals['_DELETEHUNTGROUPSCRIPTRESPONSE']._serialized_start=8441
  _globals['_DELETEHUNTGROUPSCRIPTRESPONSE']._serialized_end=8472
# @@protoc_insertion_point(module_scope)
