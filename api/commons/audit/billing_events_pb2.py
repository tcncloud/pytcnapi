# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/commons/audit/billing_events.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&api/commons/audit/billing_events.proto\x12\x11\x61pi.commons.audit\"`\n\x1d\x42illingCommitBillingPlanEvent\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"[\n\x1d\x42illingCreateBillingPlanEvent\x12!\n\x0c\x62illing_plan\x18\x01 \x01(\tR\x0b\x62illingPlan\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"Z\n\x19\x42illingCreateInvoiceEvent\x12\x1c\n\x07invoice\x18\x01 \x01(\tB\x02\x18\x01R\x07invoice\x12\x1b\n\x07user_id\x18\x02 \x01(\tB\x02\x18\x01R\x06userId:\x02\x18\x01\"d\n BillingCreateRateDefinitionEvent\x12\'\n\x0frate_definition\x18\x01 \x01(\tR\x0erateDefinition\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"`\n\x1d\x42illingDeleteBillingPlanEvent\x12&\n\x0f\x62illing_plan_id\x18\x01 \x01(\tR\rbillingPlanId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"_\n\x19\x42illingDeleteInvoiceEvent\x12!\n\ninvoice_id\x18\x01 \x01(\tB\x02\x18\x01R\tinvoiceId\x12\x1b\n\x07user_id\x18\x02 \x01(\tB\x02\x18\x01R\x06userId:\x02\x18\x01\"i\n BillingDeleteRateDefinitionEvent\x12,\n\x12rate_definition_id\x18\x01 \x01(\tR\x10rateDefinitionId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"S\n\x19\x42illingExportInvoiceEvent\x12\x1d\n\ninvoice_id\x18\x01 \x01(\tR\tinvoiceId\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"[\n\x1d\x42illingUpdateBillingPlanEvent\x12!\n\x0c\x62illing_plan\x18\x01 \x01(\tR\x0b\x62illingPlan\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userId\"Z\n\x19\x42illingUpdateInvoiceEvent\x12\x1c\n\x07invoice\x18\x01 \x01(\tB\x02\x18\x01R\x07invoice\x12\x1b\n\x07user_id\x18\x02 \x01(\tB\x02\x18\x01R\x06userId:\x02\x18\x01\"d\n BillingUpdateRateDefinitionEvent\x12\'\n\x0frate_definition\x18\x01 \x01(\tR\x0erateDefinition\x12\x17\n\x07user_id\x18\x02 \x01(\tR\x06userIdB\x91\x01\n\x15\x63om.api.commons.auditB\x12\x42illingEventsProtoP\x01\xa2\x02\x03\x41\x43\x41\xaa\x02\x11\x41pi.Commons.Audit\xca\x02\x11\x41pi\\Commons\\Audit\xe2\x02\x1d\x41pi\\Commons\\Audit\\GPBMetadata\xea\x02\x13\x41pi::Commons::Auditb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.commons.audit.billing_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025com.api.commons.auditB\022BillingEventsProtoP\001\242\002\003ACA\252\002\021Api.Commons.Audit\312\002\021Api\\Commons\\Audit\342\002\035Api\\Commons\\Audit\\GPBMetadata\352\002\023Api::Commons::Audit'
  _globals['_BILLINGCREATEINVOICEEVENT'].fields_by_name['invoice']._loaded_options = None
  _globals['_BILLINGCREATEINVOICEEVENT'].fields_by_name['invoice']._serialized_options = b'\030\001'
  _globals['_BILLINGCREATEINVOICEEVENT'].fields_by_name['user_id']._loaded_options = None
  _globals['_BILLINGCREATEINVOICEEVENT'].fields_by_name['user_id']._serialized_options = b'\030\001'
  _globals['_BILLINGCREATEINVOICEEVENT']._loaded_options = None
  _globals['_BILLINGCREATEINVOICEEVENT']._serialized_options = b'\030\001'
  _globals['_BILLINGDELETEINVOICEEVENT'].fields_by_name['invoice_id']._loaded_options = None
  _globals['_BILLINGDELETEINVOICEEVENT'].fields_by_name['invoice_id']._serialized_options = b'\030\001'
  _globals['_BILLINGDELETEINVOICEEVENT'].fields_by_name['user_id']._loaded_options = None
  _globals['_BILLINGDELETEINVOICEEVENT'].fields_by_name['user_id']._serialized_options = b'\030\001'
  _globals['_BILLINGDELETEINVOICEEVENT']._loaded_options = None
  _globals['_BILLINGDELETEINVOICEEVENT']._serialized_options = b'\030\001'
  _globals['_BILLINGUPDATEINVOICEEVENT'].fields_by_name['invoice']._loaded_options = None
  _globals['_BILLINGUPDATEINVOICEEVENT'].fields_by_name['invoice']._serialized_options = b'\030\001'
  _globals['_BILLINGUPDATEINVOICEEVENT'].fields_by_name['user_id']._loaded_options = None
  _globals['_BILLINGUPDATEINVOICEEVENT'].fields_by_name['user_id']._serialized_options = b'\030\001'
  _globals['_BILLINGUPDATEINVOICEEVENT']._loaded_options = None
  _globals['_BILLINGUPDATEINVOICEEVENT']._serialized_options = b'\030\001'
  _globals['_BILLINGCOMMITBILLINGPLANEVENT']._serialized_start=61
  _globals['_BILLINGCOMMITBILLINGPLANEVENT']._serialized_end=157
  _globals['_BILLINGCREATEBILLINGPLANEVENT']._serialized_start=159
  _globals['_BILLINGCREATEBILLINGPLANEVENT']._serialized_end=250
  _globals['_BILLINGCREATEINVOICEEVENT']._serialized_start=252
  _globals['_BILLINGCREATEINVOICEEVENT']._serialized_end=342
  _globals['_BILLINGCREATERATEDEFINITIONEVENT']._serialized_start=344
  _globals['_BILLINGCREATERATEDEFINITIONEVENT']._serialized_end=444
  _globals['_BILLINGDELETEBILLINGPLANEVENT']._serialized_start=446
  _globals['_BILLINGDELETEBILLINGPLANEVENT']._serialized_end=542
  _globals['_BILLINGDELETEINVOICEEVENT']._serialized_start=544
  _globals['_BILLINGDELETEINVOICEEVENT']._serialized_end=639
  _globals['_BILLINGDELETERATEDEFINITIONEVENT']._serialized_start=641
  _globals['_BILLINGDELETERATEDEFINITIONEVENT']._serialized_end=746
  _globals['_BILLINGEXPORTINVOICEEVENT']._serialized_start=748
  _globals['_BILLINGEXPORTINVOICEEVENT']._serialized_end=831
  _globals['_BILLINGUPDATEBILLINGPLANEVENT']._serialized_start=833
  _globals['_BILLINGUPDATEBILLINGPLANEVENT']._serialized_end=924
  _globals['_BILLINGUPDATEINVOICEEVENT']._serialized_start=926
  _globals['_BILLINGUPDATEINVOICEEVENT']._serialized_end=1016
  _globals['_BILLINGUPDATERATEDEFINITIONEVENT']._serialized_start=1018
  _globals['_BILLINGUPDATERATEDEFINITIONEVENT']._serialized_end=1118
# @@protoc_insertion_point(module_scope)
