# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/org/huntgroup.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'api/v1alpha1/org/huntgroup.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import broadcasts_pb2 as api_dot_commons_dot_broadcasts__pb2
from api.commons import org_pb2 as api_dot_commons_dot_org__pb2
from api.commons.org import huntgroup_pb2 as api_dot_commons_dot_org_dot_huntgroup__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n api/v1alpha1/org/huntgroup.proto\x12\x10\x61pi.v1alpha1.org\x1a\x1c\x61pi/commons/broadcasts.proto\x1a\x15\x61pi/commons/org.proto\x1a\x1f\x61pi/commons/org/huntgroup.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"~\n\x1bGetHuntGroupSettingsRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x39\n\nfield_mask\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"\x88\x05\n\x1cGetHuntGroupSettingsResponse\x12K\n\x10general_settings\x18\x01 \x01(\x0b\x32 .api.commons.org.GeneralSettingsR\x0fgeneralSettings\x12]\n\x16\x63ommunication_settings\x18\x02 \x01(\x0b\x32&.api.commons.org.CommunicationSettingsR\x15\x63ommunicationSettings\x12N\n\x11\x63\x61llback_settings\x18\x03 \x01(\x0b\x32!.api.commons.org.CallbackSettingsR\x10\x63\x61llbackSettings\x12X\n\x15preview_dial_settings\x18\x04 \x01(\x0b\x32$.api.commons.org.PreviewDialSettingsR\x13previewDialSettings\x12U\n\x14manual_dial_settings\x18\x05 \x01(\x0b\x32#.api.commons.org.ManualDialSettingsR\x12manualDialSettings\x12[\n\x16transfer_call_settings\x18\x06 \x01(\x0b\x32%.api.commons.org.TransferCallSettingsR\x14transferCallSettings\x12^\n\x17number_history_settings\x18\x07 \x01(\x0b\x32&.api.commons.org.NumberHistorySettingsR\x15numberHistorySettings\"\xeb\x05\n\x1eUpdateHuntGroupSettingsRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12K\n\x10general_settings\x18\x02 \x01(\x0b\x32 .api.commons.org.GeneralSettingsR\x0fgeneralSettings\x12]\n\x16\x63ommunication_settings\x18\x03 \x01(\x0b\x32&.api.commons.org.CommunicationSettingsR\x15\x63ommunicationSettings\x12N\n\x11\x63\x61llback_settings\x18\x04 \x01(\x0b\x32!.api.commons.org.CallbackSettingsR\x10\x63\x61llbackSettings\x12X\n\x15preview_dial_settings\x18\x05 \x01(\x0b\x32$.api.commons.org.PreviewDialSettingsR\x13previewDialSettings\x12U\n\x14manual_dial_settings\x18\x06 \x01(\x0b\x32#.api.commons.org.ManualDialSettingsR\x12manualDialSettings\x12[\n\x16transfer_call_settings\x18\x07 \x01(\x0b\x32%.api.commons.org.TransferCallSettingsR\x14transferCallSettings\x12^\n\x17number_history_settings\x18\x08 \x01(\x0b\x32&.api.commons.org.NumberHistorySettingsR\x15numberHistorySettings\x12\x39\n\nfield_mask\x18\x64 \x01(\x0b\x32\x1a.google.protobuf.FieldMaskR\tfieldMask\"!\n\x1fUpdateHuntGroupSettingsResponse\"\x82\x01\n\x16\x43reateHuntGroupRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x32\n\x04type\x18\x03 \x01(\x0e\x32\x1e.api.commons.org.HuntGroupTypeR\x04type\"?\n\x17\x43reateHuntGroupResponse\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"\xb6\x01\n$UpdateHuntGroupGeneralDetailsRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x32\n\x04type\x18\x04 \x01(\x0e\x32\x1e.api.commons.org.HuntGroupTypeR\x04type\"\'\n%UpdateHuntGroupGeneralDetailsResponse\">\n\x16\x44\x65leteHuntGroupRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"\x19\n\x17\x44\x65leteHuntGroupResponse\"B\n\x1aGetHuntGroupDetailsRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"n\n\x1bGetHuntGroupDetailsResponse\x12O\n\x12hunt_group_details\x18\x01 \x01(\x0b\x32!.api.commons.org.HuntGroupDetailsR\x10huntGroupDetails\"\x1c\n\x1aListCallerIdBucketsRequest\"u\n\x1bListCallerIdBucketsResponse\x12V\n\x15\x63\x61ller_id_bucket_data\x18\x01 \x03(\x0b\x32#.api.commons.org.CallerIdBucketDataR\x12\x63\x61llerIdBucketData\"R\n\x19GetDataDipTemplateRequest\x12\x35\n\x17xml_client_property_sid\x18\x01 \x01(\x03R\x14xmlClientPropertySid\"X\n\x1aGetDataDipTemplateResponse\x12:\n\x08template\x18\x01 \x01(\x0b\x32\x1e.api.commons.org.DataDipConfigR\x08template\"]\n\x1bListDataDipTemplatesRequest\x12>\n\x06\x66ilter\x18\x01 \x01(\x0e\x32&.api.commons.DataDipTemplateFilterTypeR\x06\x66ilter\"\\\n\x1cListDataDipTemplatesResponse\x12<\n\ttemplates\x18\x01 \x03(\x0b\x32\x1e.api.commons.org.DataDipConfigR\ttemplates\"Z\n\x1c\x43reateDataDipTemplateRequest\x12:\n\x08template\x18\x01 \x01(\x0b\x32\x1e.api.commons.org.DataDipConfigR\x08template\"V\n\x1d\x43reateDataDipTemplateResponse\x12\x35\n\x17xml_client_property_sid\x18\x01 \x01(\x03R\x14xmlClientPropertySid\"q\n\x1cUpdateDataDipTemplateRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12:\n\x08template\x18\x02 \x01(\x0b\x32\x1e.api.commons.org.DataDipConfigR\x08template\"\x1f\n\x1dUpdateDataDipTemplateResponse\"l\n\x1c\x44\x65leteDataDipTemplateRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x35\n\x17xml_client_property_sid\x18\x02 \x01(\x03R\x14xmlClientPropertySid\"\x1f\n\x1d\x44\x65leteDataDipTemplateResponse\"\x8b\x01\n\x1a\x43opyDataDipTemplateRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x35\n\x17xml_client_property_sid\x18\x02 \x01(\x03R\x14xmlClientPropertySid\x12\x1f\n\x0b\x63onfig_name\x18\x03 \x01(\tR\nconfigName\"T\n\x1b\x43opyDataDipTemplateResponse\x12\x35\n\x17xml_client_property_sid\x18\x01 \x01(\x03R\x14xmlClientPropertySid\"\xc7\x01\n(CopyDataDipTemplateToOrganizationRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12\x35\n\x17xml_client_property_sid\x18\x02 \x01(\x03R\x14xmlClientPropertySid\x12\x1f\n\x0b\x63onfig_name\x18\x03 \x01(\tR\nconfigName\x12,\n\x12\x64\x65stination_org_id\x18\x04 \x01(\tR\x10\x64\x65stinationOrgId\"+\n)CopyDataDipTemplateToOrganizationResponse\",\n*ListBroadcastTemplateGeneralDetailsRequest\"\xde\x02\n+ListBroadcastTemplateGeneralDetailsResponse\x12`\n\ttemplates\x18\x01 \x03(\x0b\x32\x42.api.v1alpha1.org.ListBroadcastTemplateGeneralDetailsResponse.DataR\ttemplates\x1a\xcc\x01\n\x04\x44\x61ta\x12!\n\x0ctemplate_sid\x18\x01 \x01(\x03R\x0btemplateSid\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x41\n\x0e\x62roadcast_type\x18\x03 \x01(\x0e\x32\x1a.api.commons.BroadcastTypeR\rbroadcastType\x12J\n\x13last_scheduled_date\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x11lastScheduledDate\"#\n!ListAgentResponseAutoRulesRequest\"k\n\"ListAgentResponseAutoRulesResponse\x12\x45\n\x08rulesets\x18\x01 \x03(\x0b\x32).api.commons.org.AgentResponseAutoRuleSetR\x08rulesets\"j\n#CreateAgentResponseAutoRulesRequest\x12\x43\n\x07ruleset\x18\x01 \x01(\x0b\x32).api.commons.org.AgentResponseAutoRuleSetR\x07ruleset\"&\n$CreateAgentResponseAutoRulesResponse\"\x8a\x01\n#UpdateAgentResponseAutoRulesRequest\x12\x1e\n\nrulesetSid\x18\x01 \x01(\x03R\nrulesetSid\x12\x43\n\x07ruleset\x18\x02 \x01(\x0b\x32).api.commons.org.AgentResponseAutoRuleSetR\x07ruleset\"&\n$UpdateAgentResponseAutoRulesResponse\"E\n#DeleteAgentResponseAutoRulesRequest\x12\x1e\n\nrulesetSid\x18\x01 \x01(\x03R\nrulesetSid\"&\n$DeleteAgentResponseAutoRulesResponse\"T\n,GetHuntGroupClientInfoDisplayTemplateRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"w\n-GetHuntGroupClientInfoDisplayTemplateResponse\x12\x46\n\x08template\x18\x01 \x01(\x0b\x32*.api.commons.org.ClientInfoDisplayTemplateR\x08template\"\x9f\x01\n/CreateHuntGroupClientInfoDisplayTemplateRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x46\n\x08template\x18\x02 \x01(\x0b\x32*.api.commons.org.ClientInfoDisplayTemplateR\x08template\"U\n0CreateHuntGroupClientInfoDisplayTemplateResponse\x12!\n\x0ctemplate_sid\x18\x01 \x01(\x03R\x0btemplateSid\"\x9f\x01\n/UpdateHuntGroupClientInfoDisplayTemplateRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x46\n\x08template\x18\x02 \x01(\x0b\x32*.api.commons.org.ClientInfoDisplayTemplateR\x08template\"2\n0UpdateHuntGroupClientInfoDisplayTemplateResponse\"z\n/DeleteHuntGroupClientInfoDisplayTemplateRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12!\n\x0ctemplate_sid\x18\x02 \x01(\x03R\x0btemplateSid\"2\n0DeleteHuntGroupClientInfoDisplayTemplateResponse\"\xa2\x01\n-CopyHuntGroupClientInfoDisplayTemplateRequest\x12)\n\x11to_hunt_group_sid\x18\x01 \x01(\x03R\x0etoHuntGroupSid\x12\x46\n\x08template\x18\x02 \x01(\x0b\x32*.api.commons.org.ClientInfoDisplayTemplateR\x08template\"0\n.CopyHuntGroupClientInfoDisplayTemplateResponse\"x\n.CreateCampaignClientInfoDisplayTemplateRequest\x12\x46\n\x08template\x18\x01 \x01(\x0b\x32*.api.commons.org.ClientInfoDisplayTemplateR\x08template\"T\n/CreateCampaignClientInfoDisplayTemplateResponse\x12!\n\x0ctemplate_sid\x18\x01 \x01(\x03R\x0btemplateSid\"\x94\x02\n/ListHuntGroupsWithClientInfoTemplateDataRequest\x12`\n\x06\x66ilter\x18\x01 \x01(\x0e\x32H.api.v1alpha1.org.ListHuntGroupsWithClientInfoTemplateDataRequest.FilterR\x06\x66ilter\"\x7f\n\x06\x46ilter\x12\x16\n\x12\x46ILTER_UNSPECIFIED\x10\x00\x12\x0e\n\nFILTER_ALL\x10\x01\x12$\n FILTER_HUNT_GROUPS_WITH_TEMPLATE\x10\x02\x12\'\n#FILTER_HUNT_GROUPS_WITHOUT_TEMPLATE\x10\x03\"\xac\x01\n0ListHuntGroupsWithClientInfoTemplateDataResponse\x12x\n\x1ehunt_groups_with_template_data\x18\x01 \x03(\x0b\x32\x34.api.commons.org.HuntGroupWithClientInfoTemplateDataR\x1ahuntGroupsWithTemplateData\"D\n\x1cListHuntGroupWebLinksRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\"V\n\x1dListHuntGroupWebLinksResponse\x12\x35\n\tweb_links\x18\x01 \x03(\x0b\x32\x18.api.commons.org.WebLinkR\x08webLinks\"\xac\x01\n\x1b\x43opyHuntGroupWebLinkRequest\x12-\n\x13\x66rom_hunt_group_sid\x18\x01 \x01(\x03R\x10\x66romHuntGroupSid\x12)\n\x11to_hunt_group_sid\x18\x02 \x01(\x03R\x0etoHuntGroupSid\x12\x33\n\x08web_link\x18\x03 \x01(\x0b\x32\x18.api.commons.org.WebLinkR\x07webLink\"\x1e\n\x1c\x43opyHuntGroupWebLinkResponse\"}\n\x1eUpdateHuntGroupWebLinksRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x35\n\tweb_links\x18\x02 \x03(\x0b\x32\x18.api.commons.org.WebLinkR\x08webLinks\"!\n\x1fUpdateHuntGroupWebLinksResponse\"c\n$ListHuntGroupIntegrationLinksRequest\x12\x15\n\x06org_id\x18\x01 \x01(\tR\x05orgId\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\"_\n%ListHuntGroupIntegrationLinksResponse\x12\x36\n\x05links\x18\x01 \x03(\x0b\x32 .api.commons.org.IntegrationLinkR\x05links\"\x86\x01\n#CopyHuntGroupIntegrationLinkRequest\x12)\n\x11to_hunt_group_sid\x18\x01 \x01(\x03R\x0etoHuntGroupSid\x12\x34\n\x04link\x18\x02 \x01(\x0b\x32 .api.commons.org.IntegrationLinkR\x04link\"&\n$CopyHuntGroupIntegrationLinkResponse\"\x86\x01\n&UpdateHuntGroupIntegrationLinksRequest\x12\x36\n\x05links\x18\x01 \x03(\x0b\x32 .api.commons.org.IntegrationLinkR\x05links\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\")\n\'UpdateHuntGroupIntegrationLinksResponse\"D\n\x18ListAgentTriggersRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid:\x02\x18\x01\"e\n\x19ListAgentTriggersResponse\x12\x44\n\x0e\x61gent_triggers\x18\x01 \x03(\x0b\x32\x1d.api.commons.org.AgentTriggerR\ragentTriggers:\x02\x18\x01\"\xbb\x01\n\x17\x43opyAgentTriggerRequest\x12-\n\x13\x66rom_hunt_group_sid\x18\x01 \x01(\x03R\x10\x66romHuntGroupSid\x12)\n\x11to_hunt_group_sid\x18\x02 \x01(\x03R\x0etoHuntGroupSid\x12\x42\n\ragent_trigger\x18\x03 \x01(\x0b\x32\x1d.api.commons.org.AgentTriggerR\x0c\x61gentTrigger:\x02\x18\x01\"\x1e\n\x18\x43opyAgentTriggerResponse:\x02\x18\x01\"\x8c\x01\n\x1aUpdateAgentTriggersRequest\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12\x44\n\x0e\x61gent_triggers\x18\x02 \x03(\x0b\x32\x1d.api.commons.org.AgentTriggerR\ragentTriggers:\x02\x18\x01\"!\n\x1bUpdateAgentTriggersResponse:\x02\x18\x01\"\x1d\n\x1bListHuntGroupScriptsRequest\"Z\n\x1cListHuntGroupScriptsResponse\x12:\n\x07scripts\x18\x01 \x03(\x0b\x32 .api.commons.org.HuntGroupScriptR\x07scripts\"d\n\x19GetHuntGroupScriptRequest\x12(\n\x0ehunt_group_sid\x18\x01 \x01(\x03\x42\x02\x18\x01R\x0chuntGroupSid\x12\x1d\n\nscript_sid\x18\x02 \x01(\x03R\tscriptSid\"\xe7\x03\n\x1aGetHuntGroupScriptResponse\x12P\n\x11hunt_group_script\x18\x01 \x01(\x0b\x32 .api.commons.org.HuntGroupScriptB\x02\x18\x01R\x0fhuntGroupScript\x12j\n\x0escript_details\x18\x02 \x01(\x0b\x32\x43.api.v1alpha1.org.GetHuntGroupScriptResponse.HuntGroupScriptDetailsR\rscriptDetails\x1a\x8a\x02\n\x16HuntGroupScriptDetails\x12\x38\n\x06script\x18\x01 \x01(\x0b\x32 .api.commons.org.HuntGroupScriptR\x06script\x12&\n\x0fhunt_group_sids\x18\x02 \x03(\x03R\rhuntGroupSids\x12G\n outbound_broadcast_template_sids\x18\x03 \x03(\x03R\x1doutboundBroadcastTemplateSids\x12\x45\n\x1finbound_broadcast_template_sids\x18\x04 \x03(\x03R\x1cinboundBroadcastTemplateSids\"\x96\x01\n\x1c\x43reateHuntGroupScriptRequest\x12(\n\x0ehunt_group_sid\x18\x01 \x01(\x03\x42\x02\x18\x01R\x0chuntGroupSid\x12L\n\x11hunt_group_script\x18\x02 \x01(\x0b\x32 .api.commons.org.HuntGroupScriptR\x0fhuntGroupScript\"\x1f\n\x1d\x43reateHuntGroupScriptResponse\"\xb5\x01\n\x1cUpdateHuntGroupScriptRequest\x12(\n\x0ehunt_group_sid\x18\x01 \x01(\x03\x42\x02\x18\x01R\x0chuntGroupSid\x12L\n\x11hunt_group_script\x18\x02 \x01(\x0b\x32 .api.commons.org.HuntGroupScriptR\x0fhuntGroupScript\x12\x1d\n\nscript_sid\x18\x03 \x01(\x03R\tscriptSid\"\x1f\n\x1dUpdateHuntGroupScriptResponse\"g\n\x1c\x44\x65leteHuntGroupScriptRequest\x12(\n\x0ehunt_group_sid\x18\x01 \x01(\x03\x42\x02\x18\x01R\x0chuntGroupSid\x12\x1d\n\nscript_sid\x18\x02 \x01(\x03R\tscriptSid\"\x1f\n\x1d\x44\x65leteHuntGroupScriptResponse\"h\n\x1f\x41ssignScriptToHuntGroupsRequest\x12\x1d\n\nscript_sid\x18\x01 \x01(\x03R\tscriptSid\x12&\n\x0fhunt_group_sids\x18\x02 \x03(\x03R\rhuntGroupSids\"\"\n AssignScriptToHuntGroupsResponse\"l\n#UnassignScriptFromHuntGroupsRequest\x12\x1d\n\nscript_sid\x18\x01 \x01(\x03R\tscriptSid\x12&\n\x0fhunt_group_sids\x18\x02 \x03(\x03R\rhuntGroupSids\"&\n$UnassignScriptFromHuntGroupsResponse\"\x1f\n\x1dListResponseEvaluatorsRequest\"d\n\x1eListResponseEvaluatorsResponse\x12\x42\n\nevaluators\x18\x01 \x03(\x0b\x32\".api.commons.org.ResponseEvaluatorR\nevaluators\"@\n\x1bGetResponseEvaluatorRequest\x12!\n\x0c\x65valuator_id\x18\x01 \x01(\tR\x0b\x65valuatorId\"`\n\x1cGetResponseEvaluatorResponse\x12@\n\tevaluator\x18\x01 \x01(\x0b\x32\".api.commons.org.ResponseEvaluatorR\tevaluator\"b\n\x1e\x43reateResponseEvaluatorRequest\x12@\n\tevaluator\x18\x01 \x01(\x0b\x32\".api.commons.org.ResponseEvaluatorR\tevaluator\"c\n\x1f\x43reateResponseEvaluatorResponse\x12@\n\tevaluator\x18\x01 \x01(\x0b\x32\".api.commons.org.ResponseEvaluatorR\tevaluator\"b\n\x1eUpdateResponseEvaluatorRequest\x12@\n\tevaluator\x18\x01 \x01(\x0b\x32\".api.commons.org.ResponseEvaluatorR\tevaluator\"c\n\x1fUpdateResponseEvaluatorResponse\x12@\n\tevaluator\x18\x01 \x01(\x0b\x32\".api.commons.org.ResponseEvaluatorR\tevaluator\"C\n\x1e\x44\x65leteResponseEvaluatorRequest\x12!\n\x0c\x65valuator_id\x18\x01 \x01(\tR\x0b\x65valuatorId\"!\n\x1f\x44\x65leteResponseEvaluatorResponseB\x88\x01\n\x14\x63om.api.v1alpha1.orgB\x0eHuntgroupProtoP\x01\xa2\x02\x03\x41VO\xaa\x02\x10\x41pi.V1alpha1.Org\xca\x02\x10\x41pi\\V1alpha1\\Org\xe2\x02\x1c\x41pi\\V1alpha1\\Org\\GPBMetadata\xea\x02\x12\x41pi::V1alpha1::Orgb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.org.huntgroup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\024com.api.v1alpha1.orgB\016HuntgroupProtoP\001\242\002\003AVO\252\002\020Api.V1alpha1.Org\312\002\020Api\\V1alpha1\\Org\342\002\034Api\\V1alpha1\\Org\\GPBMetadata\352\002\022Api::V1alpha1::Org'
  _globals['_LISTAGENTTRIGGERSREQUEST']._loaded_options = None
  _globals['_LISTAGENTTRIGGERSREQUEST']._serialized_options = b'\030\001'
  _globals['_LISTAGENTTRIGGERSRESPONSE']._loaded_options = None
  _globals['_LISTAGENTTRIGGERSRESPONSE']._serialized_options = b'\030\001'
  _globals['_COPYAGENTTRIGGERREQUEST']._loaded_options = None
  _globals['_COPYAGENTTRIGGERREQUEST']._serialized_options = b'\030\001'
  _globals['_COPYAGENTTRIGGERRESPONSE']._loaded_options = None
  _globals['_COPYAGENTTRIGGERRESPONSE']._serialized_options = b'\030\001'
  _globals['_UPDATEAGENTTRIGGERSREQUEST']._loaded_options = None
  _globals['_UPDATEAGENTTRIGGERSREQUEST']._serialized_options = b'\030\001'
  _globals['_UPDATEAGENTTRIGGERSRESPONSE']._loaded_options = None
  _globals['_UPDATEAGENTTRIGGERSRESPONSE']._serialized_options = b'\030\001'
  _globals['_GETHUNTGROUPSCRIPTREQUEST'].fields_by_name['hunt_group_sid']._loaded_options = None
  _globals['_GETHUNTGROUPSCRIPTREQUEST'].fields_by_name['hunt_group_sid']._serialized_options = b'\030\001'
  _globals['_GETHUNTGROUPSCRIPTRESPONSE'].fields_by_name['hunt_group_script']._loaded_options = None
  _globals['_GETHUNTGROUPSCRIPTRESPONSE'].fields_by_name['hunt_group_script']._serialized_options = b'\030\001'
  _globals['_CREATEHUNTGROUPSCRIPTREQUEST'].fields_by_name['hunt_group_sid']._loaded_options = None
  _globals['_CREATEHUNTGROUPSCRIPTREQUEST'].fields_by_name['hunt_group_sid']._serialized_options = b'\030\001'
  _globals['_UPDATEHUNTGROUPSCRIPTREQUEST'].fields_by_name['hunt_group_sid']._loaded_options = None
  _globals['_UPDATEHUNTGROUPSCRIPTREQUEST'].fields_by_name['hunt_group_sid']._serialized_options = b'\030\001'
  _globals['_DELETEHUNTGROUPSCRIPTREQUEST'].fields_by_name['hunt_group_sid']._loaded_options = None
  _globals['_DELETEHUNTGROUPSCRIPTREQUEST'].fields_by_name['hunt_group_sid']._serialized_options = b'\030\001'
  _globals['_GETHUNTGROUPSETTINGSREQUEST']._serialized_start=207
  _globals['_GETHUNTGROUPSETTINGSREQUEST']._serialized_end=333
  _globals['_GETHUNTGROUPSETTINGSRESPONSE']._serialized_start=336
  _globals['_GETHUNTGROUPSETTINGSRESPONSE']._serialized_end=984
  _globals['_UPDATEHUNTGROUPSETTINGSREQUEST']._serialized_start=987
  _globals['_UPDATEHUNTGROUPSETTINGSREQUEST']._serialized_end=1734
  _globals['_UPDATEHUNTGROUPSETTINGSRESPONSE']._serialized_start=1736
  _globals['_UPDATEHUNTGROUPSETTINGSRESPONSE']._serialized_end=1769
  _globals['_CREATEHUNTGROUPREQUEST']._serialized_start=1772
  _globals['_CREATEHUNTGROUPREQUEST']._serialized_end=1902
  _globals['_CREATEHUNTGROUPRESPONSE']._serialized_start=1904
  _globals['_CREATEHUNTGROUPRESPONSE']._serialized_end=1967
  _globals['_UPDATEHUNTGROUPGENERALDETAILSREQUEST']._serialized_start=1970
  _globals['_UPDATEHUNTGROUPGENERALDETAILSREQUEST']._serialized_end=2152
  _globals['_UPDATEHUNTGROUPGENERALDETAILSRESPONSE']._serialized_start=2154
  _globals['_UPDATEHUNTGROUPGENERALDETAILSRESPONSE']._serialized_end=2193
  _globals['_DELETEHUNTGROUPREQUEST']._serialized_start=2195
  _globals['_DELETEHUNTGROUPREQUEST']._serialized_end=2257
  _globals['_DELETEHUNTGROUPRESPONSE']._serialized_start=2259
  _globals['_DELETEHUNTGROUPRESPONSE']._serialized_end=2284
  _globals['_GETHUNTGROUPDETAILSREQUEST']._serialized_start=2286
  _globals['_GETHUNTGROUPDETAILSREQUEST']._serialized_end=2352
  _globals['_GETHUNTGROUPDETAILSRESPONSE']._serialized_start=2354
  _globals['_GETHUNTGROUPDETAILSRESPONSE']._serialized_end=2464
  _globals['_LISTCALLERIDBUCKETSREQUEST']._serialized_start=2466
  _globals['_LISTCALLERIDBUCKETSREQUEST']._serialized_end=2494
  _globals['_LISTCALLERIDBUCKETSRESPONSE']._serialized_start=2496
  _globals['_LISTCALLERIDBUCKETSRESPONSE']._serialized_end=2613
  _globals['_GETDATADIPTEMPLATEREQUEST']._serialized_start=2615
  _globals['_GETDATADIPTEMPLATEREQUEST']._serialized_end=2697
  _globals['_GETDATADIPTEMPLATERESPONSE']._serialized_start=2699
  _globals['_GETDATADIPTEMPLATERESPONSE']._serialized_end=2787
  _globals['_LISTDATADIPTEMPLATESREQUEST']._serialized_start=2789
  _globals['_LISTDATADIPTEMPLATESREQUEST']._serialized_end=2882
  _globals['_LISTDATADIPTEMPLATESRESPONSE']._serialized_start=2884
  _globals['_LISTDATADIPTEMPLATESRESPONSE']._serialized_end=2976
  _globals['_CREATEDATADIPTEMPLATEREQUEST']._serialized_start=2978
  _globals['_CREATEDATADIPTEMPLATEREQUEST']._serialized_end=3068
  _globals['_CREATEDATADIPTEMPLATERESPONSE']._serialized_start=3070
  _globals['_CREATEDATADIPTEMPLATERESPONSE']._serialized_end=3156
  _globals['_UPDATEDATADIPTEMPLATEREQUEST']._serialized_start=3158
  _globals['_UPDATEDATADIPTEMPLATEREQUEST']._serialized_end=3271
  _globals['_UPDATEDATADIPTEMPLATERESPONSE']._serialized_start=3273
  _globals['_UPDATEDATADIPTEMPLATERESPONSE']._serialized_end=3304
  _globals['_DELETEDATADIPTEMPLATEREQUEST']._serialized_start=3306
  _globals['_DELETEDATADIPTEMPLATEREQUEST']._serialized_end=3414
  _globals['_DELETEDATADIPTEMPLATERESPONSE']._serialized_start=3416
  _globals['_DELETEDATADIPTEMPLATERESPONSE']._serialized_end=3447
  _globals['_COPYDATADIPTEMPLATEREQUEST']._serialized_start=3450
  _globals['_COPYDATADIPTEMPLATEREQUEST']._serialized_end=3589
  _globals['_COPYDATADIPTEMPLATERESPONSE']._serialized_start=3591
  _globals['_COPYDATADIPTEMPLATERESPONSE']._serialized_end=3675
  _globals['_COPYDATADIPTEMPLATETOORGANIZATIONREQUEST']._serialized_start=3678
  _globals['_COPYDATADIPTEMPLATETOORGANIZATIONREQUEST']._serialized_end=3877
  _globals['_COPYDATADIPTEMPLATETOORGANIZATIONRESPONSE']._serialized_start=3879
  _globals['_COPYDATADIPTEMPLATETOORGANIZATIONRESPONSE']._serialized_end=3922
  _globals['_LISTBROADCASTTEMPLATEGENERALDETAILSREQUEST']._serialized_start=3924
  _globals['_LISTBROADCASTTEMPLATEGENERALDETAILSREQUEST']._serialized_end=3968
  _globals['_LISTBROADCASTTEMPLATEGENERALDETAILSRESPONSE']._serialized_start=3971
  _globals['_LISTBROADCASTTEMPLATEGENERALDETAILSRESPONSE']._serialized_end=4321
  _globals['_LISTBROADCASTTEMPLATEGENERALDETAILSRESPONSE_DATA']._serialized_start=4117
  _globals['_LISTBROADCASTTEMPLATEGENERALDETAILSRESPONSE_DATA']._serialized_end=4321
  _globals['_LISTAGENTRESPONSEAUTORULESREQUEST']._serialized_start=4323
  _globals['_LISTAGENTRESPONSEAUTORULESREQUEST']._serialized_end=4358
  _globals['_LISTAGENTRESPONSEAUTORULESRESPONSE']._serialized_start=4360
  _globals['_LISTAGENTRESPONSEAUTORULESRESPONSE']._serialized_end=4467
  _globals['_CREATEAGENTRESPONSEAUTORULESREQUEST']._serialized_start=4469
  _globals['_CREATEAGENTRESPONSEAUTORULESREQUEST']._serialized_end=4575
  _globals['_CREATEAGENTRESPONSEAUTORULESRESPONSE']._serialized_start=4577
  _globals['_CREATEAGENTRESPONSEAUTORULESRESPONSE']._serialized_end=4615
  _globals['_UPDATEAGENTRESPONSEAUTORULESREQUEST']._serialized_start=4618
  _globals['_UPDATEAGENTRESPONSEAUTORULESREQUEST']._serialized_end=4756
  _globals['_UPDATEAGENTRESPONSEAUTORULESRESPONSE']._serialized_start=4758
  _globals['_UPDATEAGENTRESPONSEAUTORULESRESPONSE']._serialized_end=4796
  _globals['_DELETEAGENTRESPONSEAUTORULESREQUEST']._serialized_start=4798
  _globals['_DELETEAGENTRESPONSEAUTORULESREQUEST']._serialized_end=4867
  _globals['_DELETEAGENTRESPONSEAUTORULESRESPONSE']._serialized_start=4869
  _globals['_DELETEAGENTRESPONSEAUTORULESRESPONSE']._serialized_end=4907
  _globals['_GETHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=4909
  _globals['_GETHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=4993
  _globals['_GETHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=4995
  _globals['_GETHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=5114
  _globals['_CREATEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=5117
  _globals['_CREATEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=5276
  _globals['_CREATEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=5278
  _globals['_CREATEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=5363
  _globals['_UPDATEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=5366
  _globals['_UPDATEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=5525
  _globals['_UPDATEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=5527
  _globals['_UPDATEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=5577
  _globals['_DELETEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=5579
  _globals['_DELETEHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=5701
  _globals['_DELETEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=5703
  _globals['_DELETEHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=5753
  _globals['_COPYHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=5756
  _globals['_COPYHUNTGROUPCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=5918
  _globals['_COPYHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=5920
  _globals['_COPYHUNTGROUPCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=5968
  _globals['_CREATECAMPAIGNCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_start=5970
  _globals['_CREATECAMPAIGNCLIENTINFODISPLAYTEMPLATEREQUEST']._serialized_end=6090
  _globals['_CREATECAMPAIGNCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_start=6092
  _globals['_CREATECAMPAIGNCLIENTINFODISPLAYTEMPLATERESPONSE']._serialized_end=6176
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATAREQUEST']._serialized_start=6179
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATAREQUEST']._serialized_end=6455
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATAREQUEST_FILTER']._serialized_start=6328
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATAREQUEST_FILTER']._serialized_end=6455
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATARESPONSE']._serialized_start=6458
  _globals['_LISTHUNTGROUPSWITHCLIENTINFOTEMPLATEDATARESPONSE']._serialized_end=6630
  _globals['_LISTHUNTGROUPWEBLINKSREQUEST']._serialized_start=6632
  _globals['_LISTHUNTGROUPWEBLINKSREQUEST']._serialized_end=6700
  _globals['_LISTHUNTGROUPWEBLINKSRESPONSE']._serialized_start=6702
  _globals['_LISTHUNTGROUPWEBLINKSRESPONSE']._serialized_end=6788
  _globals['_COPYHUNTGROUPWEBLINKREQUEST']._serialized_start=6791
  _globals['_COPYHUNTGROUPWEBLINKREQUEST']._serialized_end=6963
  _globals['_COPYHUNTGROUPWEBLINKRESPONSE']._serialized_start=6965
  _globals['_COPYHUNTGROUPWEBLINKRESPONSE']._serialized_end=6995
  _globals['_UPDATEHUNTGROUPWEBLINKSREQUEST']._serialized_start=6997
  _globals['_UPDATEHUNTGROUPWEBLINKSREQUEST']._serialized_end=7122
  _globals['_UPDATEHUNTGROUPWEBLINKSRESPONSE']._serialized_start=7124
  _globals['_UPDATEHUNTGROUPWEBLINKSRESPONSE']._serialized_end=7157
  _globals['_LISTHUNTGROUPINTEGRATIONLINKSREQUEST']._serialized_start=7159
  _globals['_LISTHUNTGROUPINTEGRATIONLINKSREQUEST']._serialized_end=7258
  _globals['_LISTHUNTGROUPINTEGRATIONLINKSRESPONSE']._serialized_start=7260
  _globals['_LISTHUNTGROUPINTEGRATIONLINKSRESPONSE']._serialized_end=7355
  _globals['_COPYHUNTGROUPINTEGRATIONLINKREQUEST']._serialized_start=7358
  _globals['_COPYHUNTGROUPINTEGRATIONLINKREQUEST']._serialized_end=7492
  _globals['_COPYHUNTGROUPINTEGRATIONLINKRESPONSE']._serialized_start=7494
  _globals['_COPYHUNTGROUPINTEGRATIONLINKRESPONSE']._serialized_end=7532
  _globals['_UPDATEHUNTGROUPINTEGRATIONLINKSREQUEST']._serialized_start=7535
  _globals['_UPDATEHUNTGROUPINTEGRATIONLINKSREQUEST']._serialized_end=7669
  _globals['_UPDATEHUNTGROUPINTEGRATIONLINKSRESPONSE']._serialized_start=7671
  _globals['_UPDATEHUNTGROUPINTEGRATIONLINKSRESPONSE']._serialized_end=7712
  _globals['_LISTAGENTTRIGGERSREQUEST']._serialized_start=7714
  _globals['_LISTAGENTTRIGGERSREQUEST']._serialized_end=7782
  _globals['_LISTAGENTTRIGGERSRESPONSE']._serialized_start=7784
  _globals['_LISTAGENTTRIGGERSRESPONSE']._serialized_end=7885
  _globals['_COPYAGENTTRIGGERREQUEST']._serialized_start=7888
  _globals['_COPYAGENTTRIGGERREQUEST']._serialized_end=8075
  _globals['_COPYAGENTTRIGGERRESPONSE']._serialized_start=8077
  _globals['_COPYAGENTTRIGGERRESPONSE']._serialized_end=8107
  _globals['_UPDATEAGENTTRIGGERSREQUEST']._serialized_start=8110
  _globals['_UPDATEAGENTTRIGGERSREQUEST']._serialized_end=8250
  _globals['_UPDATEAGENTTRIGGERSRESPONSE']._serialized_start=8252
  _globals['_UPDATEAGENTTRIGGERSRESPONSE']._serialized_end=8285
  _globals['_LISTHUNTGROUPSCRIPTSREQUEST']._serialized_start=8287
  _globals['_LISTHUNTGROUPSCRIPTSREQUEST']._serialized_end=8316
  _globals['_LISTHUNTGROUPSCRIPTSRESPONSE']._serialized_start=8318
  _globals['_LISTHUNTGROUPSCRIPTSRESPONSE']._serialized_end=8408
  _globals['_GETHUNTGROUPSCRIPTREQUEST']._serialized_start=8410
  _globals['_GETHUNTGROUPSCRIPTREQUEST']._serialized_end=8510
  _globals['_GETHUNTGROUPSCRIPTRESPONSE']._serialized_start=8513
  _globals['_GETHUNTGROUPSCRIPTRESPONSE']._serialized_end=9000
  _globals['_GETHUNTGROUPSCRIPTRESPONSE_HUNTGROUPSCRIPTDETAILS']._serialized_start=8734
  _globals['_GETHUNTGROUPSCRIPTRESPONSE_HUNTGROUPSCRIPTDETAILS']._serialized_end=9000
  _globals['_CREATEHUNTGROUPSCRIPTREQUEST']._serialized_start=9003
  _globals['_CREATEHUNTGROUPSCRIPTREQUEST']._serialized_end=9153
  _globals['_CREATEHUNTGROUPSCRIPTRESPONSE']._serialized_start=9155
  _globals['_CREATEHUNTGROUPSCRIPTRESPONSE']._serialized_end=9186
  _globals['_UPDATEHUNTGROUPSCRIPTREQUEST']._serialized_start=9189
  _globals['_UPDATEHUNTGROUPSCRIPTREQUEST']._serialized_end=9370
  _globals['_UPDATEHUNTGROUPSCRIPTRESPONSE']._serialized_start=9372
  _globals['_UPDATEHUNTGROUPSCRIPTRESPONSE']._serialized_end=9403
  _globals['_DELETEHUNTGROUPSCRIPTREQUEST']._serialized_start=9405
  _globals['_DELETEHUNTGROUPSCRIPTREQUEST']._serialized_end=9508
  _globals['_DELETEHUNTGROUPSCRIPTRESPONSE']._serialized_start=9510
  _globals['_DELETEHUNTGROUPSCRIPTRESPONSE']._serialized_end=9541
  _globals['_ASSIGNSCRIPTTOHUNTGROUPSREQUEST']._serialized_start=9543
  _globals['_ASSIGNSCRIPTTOHUNTGROUPSREQUEST']._serialized_end=9647
  _globals['_ASSIGNSCRIPTTOHUNTGROUPSRESPONSE']._serialized_start=9649
  _globals['_ASSIGNSCRIPTTOHUNTGROUPSRESPONSE']._serialized_end=9683
  _globals['_UNASSIGNSCRIPTFROMHUNTGROUPSREQUEST']._serialized_start=9685
  _globals['_UNASSIGNSCRIPTFROMHUNTGROUPSREQUEST']._serialized_end=9793
  _globals['_UNASSIGNSCRIPTFROMHUNTGROUPSRESPONSE']._serialized_start=9795
  _globals['_UNASSIGNSCRIPTFROMHUNTGROUPSRESPONSE']._serialized_end=9833
  _globals['_LISTRESPONSEEVALUATORSREQUEST']._serialized_start=9835
  _globals['_LISTRESPONSEEVALUATORSREQUEST']._serialized_end=9866
  _globals['_LISTRESPONSEEVALUATORSRESPONSE']._serialized_start=9868
  _globals['_LISTRESPONSEEVALUATORSRESPONSE']._serialized_end=9968
  _globals['_GETRESPONSEEVALUATORREQUEST']._serialized_start=9970
  _globals['_GETRESPONSEEVALUATORREQUEST']._serialized_end=10034
  _globals['_GETRESPONSEEVALUATORRESPONSE']._serialized_start=10036
  _globals['_GETRESPONSEEVALUATORRESPONSE']._serialized_end=10132
  _globals['_CREATERESPONSEEVALUATORREQUEST']._serialized_start=10134
  _globals['_CREATERESPONSEEVALUATORREQUEST']._serialized_end=10232
  _globals['_CREATERESPONSEEVALUATORRESPONSE']._serialized_start=10234
  _globals['_CREATERESPONSEEVALUATORRESPONSE']._serialized_end=10333
  _globals['_UPDATERESPONSEEVALUATORREQUEST']._serialized_start=10335
  _globals['_UPDATERESPONSEEVALUATORREQUEST']._serialized_end=10433
  _globals['_UPDATERESPONSEEVALUATORRESPONSE']._serialized_start=10435
  _globals['_UPDATERESPONSEEVALUATORRESPONSE']._serialized_end=10534
  _globals['_DELETERESPONSEEVALUATORREQUEST']._serialized_start=10536
  _globals['_DELETERESPONSEEVALUATORREQUEST']._serialized_end=10603
  _globals['_DELETERESPONSEEVALUATORRESPONSE']._serialized_start=10605
  _globals['_DELETERESPONSEEVALUATORRESPONSE']._serialized_end=10638
# @@protoc_insertion_point(module_scope)
