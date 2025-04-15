# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v1alpha1/integrationspublic/service.proto
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
    'api/v1alpha1/integrationspublic/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.commons import acd_pb2 as api_dot_commons_dot_acd__pb2
from api.commons.integrations import integrations_pb2 as api_dot_commons_dot_integrations_dot_integrations__pb2
from api.v1alpha1.integrations import portals_pb2 as api_dot_v1alpha1_dot_integrations_dot_portals__pb2
from api.v1alpha1.integrations import service_pb2 as api_dot_v1alpha1_dot_integrations_dot_service__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.type import money_pb2 as google_dot_type_dot_money__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/v1alpha1/integrationspublic/service.proto\x12\x1f\x61pi.v1alpha1.integrationspublic\x1a\x15\x61pi/commons/acd.proto\x1a+api/commons/integrations/integrations.proto\x1a\'api/v1alpha1/integrations/portals.proto\x1a\'api/v1alpha1/integrations/service.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/type/money.proto\"\xb8\x01\n\x06Values\x12K\n\x06values\x18\x01 \x03(\x0b\x32\x33.api.v1alpha1.integrationspublic.Values.ValuesEntryR\x06values\x1a\x61\n\x0bValuesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.integrationspublic.ValueR\x05value:\x02\x38\x01\"\xe5\x02\n\x05Value\x12\x19\n\x07str_val\x18\x01 \x01(\tH\x00R\x06strVal\x12\x19\n\x07num_val\x18\x02 \x01(\x01H\x00R\x06numVal\x12\x1b\n\x08\x62ool_val\x18\x03 \x01(\x08H\x00R\x07\x62oolVal\x12\x37\n\x08time_val\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\x07timeVal\x12J\n\x08\x63omp_val\x18\x06 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.CompositeValH\x00R\x07\x63ompVal\x12\x19\n\x07int_val\x18\x07 \x01(\x03H\x00R\x06intVal\x12\x1c\n\tsensitive\x18\x05 \x01(\x08R\tsensitive\x12\x44\n\nvalidation\x18\x08 \x01(\x0e\x32$.api.commons.integrations.ValidationR\nvalidationB\x05\n\x03val\"Q\n\x0c\x43ompositeVal\x12\x41\n\x05parts\x18\x01 \x03(\x0b\x32+.api.v1alpha1.integrationspublic.FieldOrStrR\x05parts\"F\n\nFieldOrStr\x12\x16\n\x05\x66ield\x18\x01 \x01(\tH\x00R\x05\x66ield\x12\x19\n\x07str_val\x18\x02 \x01(\tH\x00R\x06strValB\x05\n\x03val\" \n\x0ePortalConfigId\x12\x0e\n\x02id\x18\x03 \x01(\tR\x02id\"\xc5\x03\n\x0cPortalConfig\x12\x0e\n\x02id\x18\x15 \x01(\tR\x02id\x12\x12\n\x04name\x18\x16 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x17 \x01(\tR\x0b\x64\x65scription\x12(\n\x10\x63hat_client_link\x18\x02 \x01(\tR\x0e\x63hatClientLink\x12#\n\rcontact_email\x18\x03 \x01(\tR\x0c\x63ontactEmail\x12#\n\rcontact_phone\x18\x04 \x01(\tR\x0c\x63ontactPhone\x12\x1f\n\x0bpostal_code\x18\x05 \x01(\tR\npostalCode\x12\x12\n\x04\x63ity\x18\x06 \x01(\tR\x04\x63ity\x12\x14\n\x05state\x18\x07 \x01(\tR\x05state\x12!\n\x0c\x63ompany_name\x18\x08 \x01(\tR\x0b\x63ompanyName\x12\x12\n\x04logo\x18\r \x01(\x0cR\x04logo\x12#\n\rprimary_color\x18\x0e \x01(\tR\x0cprimaryColor\x12\'\n\x0fsecondary_color\x18\x0f \x01(\tR\x0esecondaryColor\x12%\n\x0estreet_address\x18\x13 \x01(\tR\rstreetAddressJ\x04\x08\t\x10\r\"\x1e\n\x0cPortalLinkId\x12\x0e\n\x02id\x18\x03 \x01(\tR\x02id\"W\n\x0eGetLinkDataReq\x12\x45\n\x06\x65ntity\x18\x01 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.PortalLinkIdR\x06\x65ntity\"\xbe\x05\n\x0eGetLinkDataRes\x12\x1a\n\x08\x63omplete\x18\x02 \x01(\x08R\x08\x63omplete\x12\x18\n\x07\x65xpired\x18\x03 \x01(\x08R\x07\x65xpired\x12R\n\rportal_config\x18\x04 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.PortalConfigR\x0cportalConfig\x12N\n\x0cverification\x18\x05 \x01(\x0b\x32*.api.commons.integrations.VerificationFlowR\x0cverification\x12?\n\x07invoice\x18\x06 \x01(\x0b\x32%.api.commons.integrations.InvoiceFlowR\x07invoice\x12\x41\n\x08payments\x18\x07 \x03(\x0b\x32%.api.commons.integrations.PaymentFlowR\x08payments\x12Y\n\nflow_forms\x18\t \x03(\x0b\x32:.api.v1alpha1.integrationspublic.GetLinkDataRes.FieldNamesR\tflowForms\x12L\n\x0bportal_text\x18\x0f \x01(\x0b\x32+.api.v1alpha1.integrationspublic.PortalTextR\nportalText\x1a\xa4\x01\n\nFieldNames\x12\x32\n\x04\x66low\x18\x08 \x01(\x0b\x32\x1e.api.commons.integrations.FlowR\x04\x66low\x12\x1f\n\x0b\x66ield_names\x18\t \x03(\tR\nfieldNames\x12\x41\n\x06\x66ields\x18\n \x03(\x0b\x32).api.commons.integrations.FieldDefinitionR\x06\x66ields\"\xd8\x02\n\nPortalText\x12/\n\x13verification_header\x18\x01 \x01(\tR\x12verificationHeader\x12/\n\x13verification_footer\x18\x02 \x01(\tR\x12verificationFooter\x12%\n\x0epayment_header\x18\x03 \x01(\tR\rpaymentHeader\x12%\n\x0epayment_footer\x18\x04 \x01(\tR\rpaymentFooter\x12%\n\x0ereceipt_header\x18\x05 \x01(\tR\rreceiptHeader\x12%\n\x0ereceipt_footer\x18\x06 \x01(\tR\rreceiptFooter\x12%\n\x0einvoice_header\x18\x07 \x01(\tR\rinvoiceHeader\x12%\n\x0einvoice_footer\x18\x08 \x01(\tR\rinvoiceFooter\"\xce\x02\n\x15SubmitVerificationReq\x12\x45\n\x06\x65ntity\x18\x01 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.PortalLinkIdR\x06\x65ntity\x12\x7f\n\x13verification_fields\x18\x02 \x03(\x0b\x32N.api.v1alpha1.integrationspublic.SubmitVerificationReq.VerificationFieldsEntryR\x12verificationFields\x1am\n\x17VerificationFieldsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.integrationspublic.ValueR\x05value:\x02\x38\x01\"R\n\x15SubmitVerificationRes\x12\x1a\n\x08verified\x18\x01 \x01(\x08R\x08verified\x12\x1d\n\nsession_id\x18\x02 \x01(\tR\tsessionId\"{\n\x13SessionKeepAliveReq\x12\x45\n\x06\x65ntity\x18\x01 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.PortalLinkIdR\x06\x65ntity\x12\x1d\n\nsession_id\x18\x02 \x01(\tR\tsessionId\"D\n\x13SessionKeepAliveRes\x12\x0e\n\x02ok\x18\x01 \x01(\x08R\x02ok\x12\x1d\n\nsession_id\x18\x02 \x01(\tR\tsessionId\"u\n\rGetInvoiceReq\x12\x45\n\x06\x65ntity\x18\x01 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.PortalLinkIdR\x06\x65ntity\x12\x1d\n\nsession_id\x18\x02 \x01(\tR\tsessionId\"\xcb\x02\n\rGetInvoiceRes\x12R\n\x06\x66ields\x18\x01 \x03(\x0b\x32:.api.v1alpha1.integrationspublic.GetInvoiceRes.FieldsEntryR\x06\x66ields\x12\x1d\n\namount_due\x18\x02 \x01(\x01R\tamountDue\x12$\n\x0e\x61mount_due_key\x18\x03 \x01(\tR\x0c\x61mountDueKey\x12>\n\x08invoices\x18\x04 \x01(\x0b\x32\".api.commons.integrations.InvoicesR\x08invoices\x1a\x61\n\x0b\x46ieldsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.integrationspublic.ValueR\x05value:\x02\x38\x01\"\x99\x03\n\x10SubmitPaymentReq\x12\x45\n\x06\x65ntity\x18\x01 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.PortalLinkIdR\x06\x65ntity\x12\x1d\n\nsession_id\x18\x02 \x01(\tR\tsessionId\x12k\n\x0epayment_fields\x18\x03 \x03(\x0b\x32\x44.api.v1alpha1.integrationspublic.SubmitPaymentReq.PaymentFieldsEntryR\rpaymentFields\x12H\n\x0cpayment_flow\x18\x04 \x01(\x0b\x32%.api.commons.integrations.PaymentFlowR\x0bpaymentFlow\x1ah\n\x12PaymentFieldsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.integrationspublic.ValueR\x05value:\x02\x38\x01\"\x95\x02\n\x10SubmitPaymentRes\x12U\n\x06\x66ields\x18\x01 \x03(\x0b\x32=.api.v1alpha1.integrationspublic.SubmitPaymentRes.FieldsEntryR\x06\x66ields\x12\x1f\n\x0b\x61mount_paid\x18\x02 \x01(\x01R\namountPaid\x12&\n\x0f\x61mount_paid_key\x18\x03 \x01(\tR\ramountPaidKey\x1a\x61\n\x0b\x46ieldsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.integrationspublic.ValueR\x05value:\x02\x38\x01\"u\n\rGetReceiptReq\x12\x45\n\x06\x65ntity\x18\x01 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.PortalLinkIdR\x06\x65ntity\x12\x1d\n\nsession_id\x18\x02 \x01(\tR\tsessionId\"\xbb\x04\n\rGetReceiptRes\x12\x1d\n\nreceipt_id\x18\x01 \x01(\tR\treceiptId\x12U\n\x07request\x18\x02 \x03(\x0b\x32;.api.v1alpha1.integrationspublic.GetReceiptRes.RequestEntryR\x07request\x12X\n\x08response\x18\x03 \x03(\x0b\x32<.api.v1alpha1.integrationspublic.GetReceiptRes.ResponseEntryR\x08response\x12\x1f\n\x0b\x61mount_paid\x18\x04 \x01(\x01R\namountPaid\x12&\n\x0f\x61mount_paid_key\x18\x05 \x01(\tR\ramountPaidKey\x12H\n\x0cpayment_flow\x18\x06 \x01(\x0b\x32%.api.commons.integrations.PaymentFlowR\x0bpaymentFlow\x1a\x62\n\x0cRequestEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.integrationspublic.ValueR\x05value:\x02\x38\x01\x1a\x63\n\rResponseEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.integrationspublic.ValueR\x05value:\x02\x38\x01\"\xb4\x03\n\x12ProcessWorkflowReq\x12$\n\x0eportal_link_id\x18\x01 \x01(\tR\x0cportalLinkId\x12\x1b\n\tportal_id\x18\x02 \x01(\tR\x08portalId\x12\x18\n\x07segment\x18\x03 \x01(\x05R\x07segment\x12\x16\n\x06\x63hoice\x18\x04 \x01(\x05R\x06\x63hoice\x12W\n\x06params\x18\x05 \x03(\x0b\x32?.api.v1alpha1.integrationspublic.ProcessWorkflowReq.ParamsEntryR\x06params\x12N\n\x0erequest_origin\x18\x06 \x01(\x0e\x32\'.api.commons.integrations.RequestOriginR\rrequestOrigin\x12\x1d\n\nsession_id\x18\x07 \x01(\tR\tsessionId\x1a\x61\n\x0bParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.integrationspublic.ValueR\x05value:\x02\x38\x01\"\x81\x02\n\x12ProcessWorkflowRes\x12\x18\n\x07success\x18\x01 \x01(\x08R\x07success\x12Q\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32=.api.v1alpha1.integrationspublic.ProcessWorkflowRes.DataEntryR\x04\x64\x61ta\x12\x1d\n\nsession_id\x18\x03 \x01(\tR\tsessionId\x1a_\n\tDataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.integrationspublic.ValueR\x05value:\x02\x38\x01\"Z\n\x11GetLinkDetailsReq\x12\x45\n\x06\x65ntity\x18\x01 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.PortalLinkIdR\x06\x65ntity\"\xb4\x02\n\x11GetLinkDetailsRes\x12\x39\n\x06portal\x18\x01 \x01(\x0b\x32!.api.v1alpha1.integrations.PortalR\x06portal\x12R\n\rportal_config\x18\x02 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.PortalConfigR\x0cportalConfig\x12\x18\n\x07\x65xpired\x18\x03 \x01(\x08R\x07\x65xpired\x12\x1c\n\tcompleted\x18\x04 \x01(\x08R\tcompleted\x12X\n\x11portal_definition\x18\x05 \x01(\x0b\x32+.api.v1alpha1.integrations.PortalDefinitionR\x10portalDefinition\"\xea\x03\n\x10\x43\x61lculateFeesReq\x12\x45\n\x06\x65ntity\x18\x01 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.PortalLinkIdR\x06\x65ntity\x12\x31\n\x04\x66\x65\x65s\x18\x02 \x03(\x0b\x32\x1d.api.commons.integrations.FeeR\x04\x66\x65\x65s\x12U\n\x06params\x18\x03 \x03(\x0b\x32=.api.v1alpha1.integrationspublic.CalculateFeesReq.ParamsEntryR\x06params\x12\x19\n\x08\x63\x61ll_sid\x18\x04 \x01(\x03R\x07\x63\x61llSid\x12\x37\n\tcall_type\x18\x05 \x01(\x0e\x32\x1a.api.commons.CallType.EnumR\x08\x63\x61llType\x12N\n\x0erequest_origin\x18\x06 \x01(\x0e\x32\'.api.commons.integrations.RequestOriginR\rrequestOrigin\x1a\x61\n\x0bParamsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\x05value\x18\x02 \x01(\x0b\x32&.api.v1alpha1.integrationspublic.ValueR\x05value:\x02\x38\x01\"\x97\x02\n\x10\x43\x61lculateFeesRes\x12n\n\x0f\x63\x61lculated_fees\x18\x01 \x03(\x0b\x32\x45.api.v1alpha1.integrationspublic.CalculateFeesRes.CalculatedFeesEntryR\x0e\x63\x61lculatedFees\x12<\n\x10total_amount_due\x18\x02 \x01(\x0b\x32\x12.google.type.MoneyR\x0etotalAmountDue\x1aU\n\x13\x43\x61lculatedFeesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x12.google.type.MoneyR\x05value:\x02\x38\x01\"\x9b\x01\n\x11\x44\x65liverReceiptReq\x12T\n\remail_receipt\x18\x03 \x01(\x0b\x32-.api.v1alpha1.integrationspublic.EmailReceiptH\x00R\x0c\x65mailReceipt\x12\x1d\n\nreceipt_id\x18\x06 \x01(\tR\treceiptIdB\x11\n\x0f\x64\x65livery_method\"\'\n\x0c\x45mailReceipt\x12\x17\n\x07to_addr\x18\x01 \x01(\tR\x06toAddr\"\x13\n\x11\x44\x65liverReceiptRes2\xa2\x0e\n\x12IntegrationsPublic\x12\xa8\x01\n\x0bGetLinkData\x12/.api.v1alpha1.integrationspublic.GetLinkDataReq\x1a/.api.v1alpha1.integrationspublic.GetLinkDataRes\"7\x82\xd3\xe4\x93\x02\x31\",/api/v1alpha1/integrationspublic/getlinkdata:\x01*\x12\xc4\x01\n\x12SubmitVerification\x12\x36.api.v1alpha1.integrationspublic.SubmitVerificationReq\x1a\x36.api.v1alpha1.integrationspublic.SubmitVerificationRes\">\x82\xd3\xe4\x93\x02\x38\"3/api/v1alpha1/integrationspublic/submitverification:\x01*\x12\xbc\x01\n\x10SessionKeepAlive\x12\x34.api.v1alpha1.integrationspublic.SessionKeepAliveReq\x1a\x34.api.v1alpha1.integrationspublic.SessionKeepAliveRes\"<\x82\xd3\xe4\x93\x02\x36\"1/api/v1alpha1/integrationspublic/sessionkeepalive:\x01*\x12\xa4\x01\n\nGetInvoice\x12..api.v1alpha1.integrationspublic.GetInvoiceReq\x1a..api.v1alpha1.integrationspublic.GetInvoiceRes\"6\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/integrationspublic/getinvoice:\x01*\x12\xb0\x01\n\rSubmitPayment\x12\x31.api.v1alpha1.integrationspublic.SubmitPaymentReq\x1a\x31.api.v1alpha1.integrationspublic.SubmitPaymentRes\"9\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/integrationspublic/submitpayment:\x01*\x12\xa4\x01\n\nGetReceipt\x12..api.v1alpha1.integrationspublic.GetReceiptReq\x1a..api.v1alpha1.integrationspublic.GetReceiptRes\"6\x82\xd3\xe4\x93\x02\x30\"+/api/v1alpha1/integrationspublic/getreceipt:\x01*\x12\xb8\x01\n\x0fProcessWorkflow\x12\x33.api.v1alpha1.integrationspublic.ProcessWorkflowReq\x1a\x33.api.v1alpha1.integrationspublic.ProcessWorkflowRes\";\x82\xd3\xe4\x93\x02\x35\"0/api/v1alpha1/integrationspublic/processworkflow:\x01*\x12\xb4\x01\n\x0eGetLinkDetails\x12\x32.api.v1alpha1.integrationspublic.GetLinkDetailsReq\x1a\x32.api.v1alpha1.integrationspublic.GetLinkDetailsRes\":\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/integrationspublic/getlinkdetails:\x01*\x12\xb0\x01\n\rCalculateFees\x12\x31.api.v1alpha1.integrationspublic.CalculateFeesReq\x1a\x31.api.v1alpha1.integrationspublic.CalculateFeesRes\"9\x82\xd3\xe4\x93\x02\x33\"./api/v1alpha1/integrationspublic/calculatefees:\x01*\x12\xb4\x01\n\x0e\x44\x65liverReceipt\x12\x32.api.v1alpha1.integrationspublic.DeliverReceiptReq\x1a\x32.api.v1alpha1.integrationspublic.DeliverReceiptRes\":\x82\xd3\xe4\x93\x02\x34\"//api/v1alpha1/integrationspublic/deliverreceipt:\x01*B\xd1\x01\n#com.api.v1alpha1.integrationspublicB\x0cServiceProtoP\x01\xa2\x02\x03\x41VI\xaa\x02\x1f\x41pi.V1alpha1.Integrationspublic\xca\x02\x1f\x41pi\\V1alpha1\\Integrationspublic\xe2\x02+Api\\V1alpha1\\Integrationspublic\\GPBMetadata\xea\x02!Api::V1alpha1::Integrationspublicb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v1alpha1.integrationspublic.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.api.v1alpha1.integrationspublicB\014ServiceProtoP\001\242\002\003AVI\252\002\037Api.V1alpha1.Integrationspublic\312\002\037Api\\V1alpha1\\Integrationspublic\342\002+Api\\V1alpha1\\Integrationspublic\\GPBMetadata\352\002!Api::V1alpha1::Integrationspublic'
  _globals['_VALUES_VALUESENTRY']._loaded_options = None
  _globals['_VALUES_VALUESENTRY']._serialized_options = b'8\001'
  _globals['_SUBMITVERIFICATIONREQ_VERIFICATIONFIELDSENTRY']._loaded_options = None
  _globals['_SUBMITVERIFICATIONREQ_VERIFICATIONFIELDSENTRY']._serialized_options = b'8\001'
  _globals['_GETINVOICERES_FIELDSENTRY']._loaded_options = None
  _globals['_GETINVOICERES_FIELDSENTRY']._serialized_options = b'8\001'
  _globals['_SUBMITPAYMENTREQ_PAYMENTFIELDSENTRY']._loaded_options = None
  _globals['_SUBMITPAYMENTREQ_PAYMENTFIELDSENTRY']._serialized_options = b'8\001'
  _globals['_SUBMITPAYMENTRES_FIELDSENTRY']._loaded_options = None
  _globals['_SUBMITPAYMENTRES_FIELDSENTRY']._serialized_options = b'8\001'
  _globals['_GETRECEIPTRES_REQUESTENTRY']._loaded_options = None
  _globals['_GETRECEIPTRES_REQUESTENTRY']._serialized_options = b'8\001'
  _globals['_GETRECEIPTRES_RESPONSEENTRY']._loaded_options = None
  _globals['_GETRECEIPTRES_RESPONSEENTRY']._serialized_options = b'8\001'
  _globals['_PROCESSWORKFLOWREQ_PARAMSENTRY']._loaded_options = None
  _globals['_PROCESSWORKFLOWREQ_PARAMSENTRY']._serialized_options = b'8\001'
  _globals['_PROCESSWORKFLOWRES_DATAENTRY']._loaded_options = None
  _globals['_PROCESSWORKFLOWRES_DATAENTRY']._serialized_options = b'8\001'
  _globals['_CALCULATEFEESREQ_PARAMSENTRY']._loaded_options = None
  _globals['_CALCULATEFEESREQ_PARAMSENTRY']._serialized_options = b'8\001'
  _globals['_CALCULATEFEESRES_CALCULATEDFEESENTRY']._loaded_options = None
  _globals['_CALCULATEFEESRES_CALCULATEDFEESENTRY']._serialized_options = b'8\001'
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['GetLinkData']._loaded_options = None
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['GetLinkData']._serialized_options = b'\202\323\344\223\0021\",/api/v1alpha1/integrationspublic/getlinkdata:\001*'
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['SubmitVerification']._loaded_options = None
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['SubmitVerification']._serialized_options = b'\202\323\344\223\0028\"3/api/v1alpha1/integrationspublic/submitverification:\001*'
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['SessionKeepAlive']._loaded_options = None
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['SessionKeepAlive']._serialized_options = b'\202\323\344\223\0026\"1/api/v1alpha1/integrationspublic/sessionkeepalive:\001*'
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['GetInvoice']._loaded_options = None
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['GetInvoice']._serialized_options = b'\202\323\344\223\0020\"+/api/v1alpha1/integrationspublic/getinvoice:\001*'
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['SubmitPayment']._loaded_options = None
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['SubmitPayment']._serialized_options = b'\202\323\344\223\0023\"./api/v1alpha1/integrationspublic/submitpayment:\001*'
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['GetReceipt']._loaded_options = None
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['GetReceipt']._serialized_options = b'\202\323\344\223\0020\"+/api/v1alpha1/integrationspublic/getreceipt:\001*'
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['ProcessWorkflow']._loaded_options = None
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['ProcessWorkflow']._serialized_options = b'\202\323\344\223\0025\"0/api/v1alpha1/integrationspublic/processworkflow:\001*'
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['GetLinkDetails']._loaded_options = None
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['GetLinkDetails']._serialized_options = b'\202\323\344\223\0024\"//api/v1alpha1/integrationspublic/getlinkdetails:\001*'
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['CalculateFees']._loaded_options = None
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['CalculateFees']._serialized_options = b'\202\323\344\223\0023\"./api/v1alpha1/integrationspublic/calculatefees:\001*'
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['DeliverReceipt']._loaded_options = None
  _globals['_INTEGRATIONSPUBLIC'].methods_by_name['DeliverReceipt']._serialized_options = b'\202\323\344\223\0024\"//api/v1alpha1/integrationspublic/deliverreceipt:\001*'
  _globals['_VALUES']._serialized_start=321
  _globals['_VALUES']._serialized_end=505
  _globals['_VALUES_VALUESENTRY']._serialized_start=408
  _globals['_VALUES_VALUESENTRY']._serialized_end=505
  _globals['_VALUE']._serialized_start=508
  _globals['_VALUE']._serialized_end=865
  _globals['_COMPOSITEVAL']._serialized_start=867
  _globals['_COMPOSITEVAL']._serialized_end=948
  _globals['_FIELDORSTR']._serialized_start=950
  _globals['_FIELDORSTR']._serialized_end=1020
  _globals['_PORTALCONFIGID']._serialized_start=1022
  _globals['_PORTALCONFIGID']._serialized_end=1054
  _globals['_PORTALCONFIG']._serialized_start=1057
  _globals['_PORTALCONFIG']._serialized_end=1510
  _globals['_PORTALLINKID']._serialized_start=1512
  _globals['_PORTALLINKID']._serialized_end=1542
  _globals['_GETLINKDATAREQ']._serialized_start=1544
  _globals['_GETLINKDATAREQ']._serialized_end=1631
  _globals['_GETLINKDATARES']._serialized_start=1634
  _globals['_GETLINKDATARES']._serialized_end=2336
  _globals['_GETLINKDATARES_FIELDNAMES']._serialized_start=2172
  _globals['_GETLINKDATARES_FIELDNAMES']._serialized_end=2336
  _globals['_PORTALTEXT']._serialized_start=2339
  _globals['_PORTALTEXT']._serialized_end=2683
  _globals['_SUBMITVERIFICATIONREQ']._serialized_start=2686
  _globals['_SUBMITVERIFICATIONREQ']._serialized_end=3020
  _globals['_SUBMITVERIFICATIONREQ_VERIFICATIONFIELDSENTRY']._serialized_start=2911
  _globals['_SUBMITVERIFICATIONREQ_VERIFICATIONFIELDSENTRY']._serialized_end=3020
  _globals['_SUBMITVERIFICATIONRES']._serialized_start=3022
  _globals['_SUBMITVERIFICATIONRES']._serialized_end=3104
  _globals['_SESSIONKEEPALIVEREQ']._serialized_start=3106
  _globals['_SESSIONKEEPALIVEREQ']._serialized_end=3229
  _globals['_SESSIONKEEPALIVERES']._serialized_start=3231
  _globals['_SESSIONKEEPALIVERES']._serialized_end=3299
  _globals['_GETINVOICEREQ']._serialized_start=3301
  _globals['_GETINVOICEREQ']._serialized_end=3418
  _globals['_GETINVOICERES']._serialized_start=3421
  _globals['_GETINVOICERES']._serialized_end=3752
  _globals['_GETINVOICERES_FIELDSENTRY']._serialized_start=3655
  _globals['_GETINVOICERES_FIELDSENTRY']._serialized_end=3752
  _globals['_SUBMITPAYMENTREQ']._serialized_start=3755
  _globals['_SUBMITPAYMENTREQ']._serialized_end=4164
  _globals['_SUBMITPAYMENTREQ_PAYMENTFIELDSENTRY']._serialized_start=4060
  _globals['_SUBMITPAYMENTREQ_PAYMENTFIELDSENTRY']._serialized_end=4164
  _globals['_SUBMITPAYMENTRES']._serialized_start=4167
  _globals['_SUBMITPAYMENTRES']._serialized_end=4444
  _globals['_SUBMITPAYMENTRES_FIELDSENTRY']._serialized_start=3655
  _globals['_SUBMITPAYMENTRES_FIELDSENTRY']._serialized_end=3752
  _globals['_GETRECEIPTREQ']._serialized_start=4446
  _globals['_GETRECEIPTREQ']._serialized_end=4563
  _globals['_GETRECEIPTRES']._serialized_start=4566
  _globals['_GETRECEIPTRES']._serialized_end=5137
  _globals['_GETRECEIPTRES_REQUESTENTRY']._serialized_start=4938
  _globals['_GETRECEIPTRES_REQUESTENTRY']._serialized_end=5036
  _globals['_GETRECEIPTRES_RESPONSEENTRY']._serialized_start=5038
  _globals['_GETRECEIPTRES_RESPONSEENTRY']._serialized_end=5137
  _globals['_PROCESSWORKFLOWREQ']._serialized_start=5140
  _globals['_PROCESSWORKFLOWREQ']._serialized_end=5576
  _globals['_PROCESSWORKFLOWREQ_PARAMSENTRY']._serialized_start=5479
  _globals['_PROCESSWORKFLOWREQ_PARAMSENTRY']._serialized_end=5576
  _globals['_PROCESSWORKFLOWRES']._serialized_start=5579
  _globals['_PROCESSWORKFLOWRES']._serialized_end=5836
  _globals['_PROCESSWORKFLOWRES_DATAENTRY']._serialized_start=5741
  _globals['_PROCESSWORKFLOWRES_DATAENTRY']._serialized_end=5836
  _globals['_GETLINKDETAILSREQ']._serialized_start=5838
  _globals['_GETLINKDETAILSREQ']._serialized_end=5928
  _globals['_GETLINKDETAILSRES']._serialized_start=5931
  _globals['_GETLINKDETAILSRES']._serialized_end=6239
  _globals['_CALCULATEFEESREQ']._serialized_start=6242
  _globals['_CALCULATEFEESREQ']._serialized_end=6732
  _globals['_CALCULATEFEESREQ_PARAMSENTRY']._serialized_start=5479
  _globals['_CALCULATEFEESREQ_PARAMSENTRY']._serialized_end=5576
  _globals['_CALCULATEFEESRES']._serialized_start=6735
  _globals['_CALCULATEFEESRES']._serialized_end=7014
  _globals['_CALCULATEFEESRES_CALCULATEDFEESENTRY']._serialized_start=6929
  _globals['_CALCULATEFEESRES_CALCULATEDFEESENTRY']._serialized_end=7014
  _globals['_DELIVERRECEIPTREQ']._serialized_start=7017
  _globals['_DELIVERRECEIPTREQ']._serialized_end=7172
  _globals['_EMAILRECEIPT']._serialized_start=7174
  _globals['_EMAILRECEIPT']._serialized_end=7213
  _globals['_DELIVERRECEIPTRES']._serialized_start=7215
  _globals['_DELIVERRECEIPTRES']._serialized_end=7234
  _globals['_INTEGRATIONSPUBLIC']._serialized_start=7237
  _globals['_INTEGRATIONSPUBLIC']._serialized_end=9063
# @@protoc_insertion_point(module_scope)
