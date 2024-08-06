# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/v0alpha/callqueue.proto
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
    'api/v0alpha/callqueue.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from annotations import authz_pb2 as annotations_dot_authz__pb2
from api.commons import call_pb2 as api_dot_commons_dot_call__pb2
from api.commons import sms_pb2 as api_dot_commons_dot_sms__pb2
from api.v0alpha import p3api_pb2 as api_dot_v0alpha_dot_p3api__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x61pi/v0alpha/callqueue.proto\x12\x0b\x61pi.v0alpha\x1a\x17\x61nnotations/authz.proto\x1a\x16\x61pi/commons/call.proto\x1a\x15\x61pi/commons/sms.proto\x1a\x17\x61pi/v0alpha/p3api.proto\x1a\x1cgoogle/api/annotations.proto\"t\n\x1d\x44\x65queuePreviewRecordOrCallReq\x12\'\n\x0ftimeout_minutes\x18\x01 \x01(\x05R\x0etimeoutMinutes\x12*\n\x11\x61gent_session_sid\x18\x02 \x01(\x03R\x0f\x61gentSessionSid\"\xa6\x01\n\x1d\x44\x65queuePreviewRecordOrCallRes\x12\x1d\n\nqueue_name\x18\x01 \x01(\tR\tqueueName\x12/\n\x04\x63\x61ll\x18\x02 \x01(\x0b\x32\x1b.api.commons.SimpleCallDataR\x04\x63\x61ll\x12\x35\n\x06record\x18\x03 \x01(\x0b\x32\x1d.api.commons.SimpleRecordDataR\x06record\"o\n\x17\x45nqueuePreviewRecordReq\x12\x35\n\x06record\x18\x01 \x01(\x0b\x32\x1d.api.commons.SimpleRecordDataR\x06record\x12\x1d\n\nqueue_name\x18\x02 \x01(\tR\tqueueName\"\x19\n\x17\x45nqueuePreviewRecordRes\"\xda\x01\n&DequeueScrubbedCallForPreviewRecordReq\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12!\n\x0cphone_number\x18\x02 \x01(\tR\x0bphoneNumber\x12&\n\x0fphone_num_index\x18\x03 \x01(\x05R\rphoneNumIndex\x12$\n\x0etask_group_sid\x18\x04 \x01(\x03R\x0ctaskGroupSid\x12\x19\n\x08task_sid\x18\x05 \x01(\x03R\x07taskSid\"Y\n&DequeueScrubbedCallForPreviewRecordRes\x12/\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x1b.api.commons.SimpleCallDataR\x04\x63\x61ll\"\"\n ClearPreviewRecordReturnQueueReq\"\"\n ClearPreviewRecordReturnQueueRes\"k\n\x19\x45nqueuePreviewDialCallReq\x12/\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x1b.api.commons.SimpleCallDataR\x04\x63\x61ll\x12\x1d\n\nqueue_name\x18\x02 \x01(\tR\tqueueName\"\x1b\n\x19\x45nqueuePreviewDialCallRes\"\x19\n\x17\x43learManualDialQueueReq\"\x19\n\x17\x43learManualDialQueueRes\"K\n\x18ProcessManualDialCallReq\x12/\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x1b.api.commons.SimpleCallDataR\x04\x63\x61ll\"\\\n\x18ProcessManualDialCallRes\x12@\n\rscrubbed_call\x18\x01 \x01(\x0b\x32\x1b.api.commons.SimpleCallDataR\x0cscrubbedCall\"\x9c\x01\n\x1f\x44\x65queueCallForManualApprovalReq\x12$\n\x0ehunt_group_sid\x18\x01 \x01(\x03R\x0chuntGroupSid\x12*\n\x11\x61gent_session_sid\x18\x02 \x01(\x03R\x0f\x61gentSessionSid\x12\'\n\x0ftimeout_minutes\x18\x03 \x01(\x05R\x0etimeoutMinutes\"\x8c\x02\n\x1f\x44\x65queueCallForManualApprovalRes\x12/\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x1b.api.commons.SimpleCallDataR\x04\x63\x61ll\x12\x14\n\x05queue\x18\x02 \x01(\tR\x05queue\x12\x42\n\x0b\x63lient_info\x18\x03 \x01(\x0b\x32!.api.v0alpha.GetClientInfoDataResR\nclientInfo\x12^\n\x14\x63lient_info_template\x18\x04 \x01(\x0b\x32,.api.v0alpha.GetClientInfoDisplayTemplateResR\x12\x63lientInfoTemplate\"Q\n\x1e\x45nqueueManuallyApprovedCallReq\x12/\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x1b.api.commons.SimpleCallDataR\x04\x63\x61ll\" \n\x1e\x45nqueueManuallyApprovedCallRes\"Q\n\x1e\x45nqueueManuallyRejectedCallReq\x12/\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x1b.api.commons.SimpleCallDataR\x04\x63\x61ll\" \n\x1e\x45nqueueManuallyRejectedCallRes\"p\n\x1eRequeueManuallyApprovedCallReq\x12/\n\x04\x63\x61ll\x18\x01 \x01(\x0b\x32\x1b.api.commons.SimpleCallDataR\x04\x63\x61ll\x12\x1d\n\nqueue_name\x18\x02 \x01(\tR\tqueueName\" \n\x1eRequeueManuallyApprovedCallRes\"P\n\x1d\x45nqueueManuallyApprovedSmsReq\x12/\n\x03sms\x18\x01 \x01(\x0b\x32\x1d.api.commons.SimpleSmsMamDataR\x03sms\"\x1f\n\x1d\x45nqueueManuallyApprovedSmsRes\"P\n\x1d\x45nqueueManuallyRejectedSmsReq\x12/\n\x03sms\x18\x01 \x01(\x0b\x32\x1d.api.commons.SimpleSmsMamDataR\x03sms\"\x1f\n\x1d\x45nqueueManuallyRejectedSmsRes\"o\n\x1dRequeueManuallyApprovedSmsReq\x12/\n\x03sms\x18\x01 \x01(\x0b\x32\x1d.api.commons.SimpleSmsMamDataR\x03sms\x12\x1d\n\nqueue_name\x18\x02 \x01(\tR\tqueueName\"\x1f\n\x1dRequeueManuallyApprovedSmsRes\"I\n!DequeueSmsMamForManualApprovalReq\x12$\n\x0ehunt_group_sid\x18\x02 \x01(\x03R\x0chuntGroupSid\"j\n!DequeueSmsMamForManualApprovalRes\x12/\n\x03sms\x18\x01 \x01(\x0b\x32\x1d.api.commons.SimpleSmsMamDataR\x03sms\x12\x14\n\x05queue\x18\x02 \x01(\tR\x05queue2\x8f\x16\n\tCallQueue\x12\xb9\x01\n\x1a\x44\x65queuePreviewRecordOrCall\x12*.api.v0alpha.DequeuePreviewRecordOrCallReq\x1a*.api.v0alpha.DequeuePreviewRecordOrCallRes\"C\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x36\"1/api/v0alpha/callqueue/dequeuepreviewrecordorcall:\x01*\x12\xa1\x01\n\x14\x45nqueuePreviewRecord\x12$.api.v0alpha.EnqueuePreviewRecordReq\x1a$.api.v0alpha.EnqueuePreviewRecordRes\"=\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x30\"+/api/v0alpha/callqueue/enqueuepreviewrecord:\x01*\x12\xdd\x01\n#DequeueScrubbedCallForPreviewRecord\x12\x33.api.v0alpha.DequeueScrubbedCallForPreviewRecordReq\x1a\x33.api.v0alpha.DequeueScrubbedCallForPreviewRecordRes\"L\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02?\":/api/v0alpha/callqueue/dequeuescrubbedcallforpreviewrecord:\x01*\x12\xc5\x01\n\x1d\x43learPreviewRecordReturnQueue\x12-.api.v0alpha.ClearPreviewRecordReturnQueueReq\x1a-.api.v0alpha.ClearPreviewRecordReturnQueueRes\"F\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x39\"4/api/v0alpha/callqueue/clearpreviewrecordreturnqueue:\x01*\x12\xa9\x01\n\x16\x45nqueuePreviewDialCall\x12&.api.v0alpha.EnqueuePreviewDialCallReq\x1a&.api.v0alpha.EnqueuePreviewDialCallRes\"?\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x32\"-/api/v0alpha/callqueue/enqueuepreviewdialcall:\x01*\x12\xa1\x01\n\x14\x43learManualDialQueue\x12$.api.v0alpha.ClearManualDialQueueReq\x1a$.api.v0alpha.ClearManualDialQueueRes\"=\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x30\"+/api/v0alpha/callqueue/clearmanualdialqueue:\x01*\x12\xa5\x01\n\x15ProcessManualDialCall\x12%.api.v0alpha.ProcessManualDialCallReq\x1a%.api.v0alpha.ProcessManualDialCallRes\">\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x31\",/api/v0alpha/callqueue/processmanualdialcall:\x01*\x12\xc1\x01\n\x1c\x44\x65queueCallForManualApproval\x12,.api.v0alpha.DequeueCallForManualApprovalReq\x1a,.api.v0alpha.DequeueCallForManualApprovalRes\"E\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x38\"3/api/v0alpha/callqueue/dequeuecallformanualapproval:\x01*\x12\xbd\x01\n\x1b\x45nqueueManuallyApprovedCall\x12+.api.v0alpha.EnqueueManuallyApprovedCallReq\x1a+.api.v0alpha.EnqueueManuallyApprovedCallRes\"D\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x37\"2/api/v0alpha/callqueue/enqueuemanuallyapprovedcall:\x01*\x12\xbd\x01\n\x1b\x45nqueueManuallyRejectedCall\x12+.api.v0alpha.EnqueueManuallyRejectedCallReq\x1a+.api.v0alpha.EnqueueManuallyRejectedCallRes\"D\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x37\"2/api/v0alpha/callqueue/enqueuemanuallyrejectedcall:\x01*\x12\xbd\x01\n\x1bRequeueManuallyApprovedCall\x12+.api.v0alpha.RequeueManuallyApprovedCallReq\x1a+.api.v0alpha.RequeueManuallyApprovedCallRes\"D\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x37\"2/api/v0alpha/callqueue/requeuemanuallyapprovedcall:\x01*\x12\xb9\x01\n\x1a\x45nqueueManuallyApprovedSms\x12*.api.v0alpha.EnqueueManuallyApprovedSmsReq\x1a*.api.v0alpha.EnqueueManuallyApprovedSmsRes\"C\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x36\"1/api/v0alpha/callqueue/enqueuemanuallyapprovedsms:\x01*\x12\xb9\x01\n\x1a\x45nqueueManuallyRejectedSms\x12*.api.v0alpha.EnqueueManuallyRejectedSmsReq\x1a*.api.v0alpha.EnqueueManuallyRejectedSmsRes\"C\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x36\"1/api/v0alpha/callqueue/enqueuemanuallyrejectedsms:\x01*\x12\xb9\x01\n\x1aRequeueManuallyApprovedSms\x12*.api.v0alpha.RequeueManuallyApprovedSmsReq\x1a*.api.v0alpha.RequeueManuallyApprovedSmsRes\"C\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02\x36\"1/api/v0alpha/callqueue/requeuemanuallyapprovedsms:\x01*\x12\xc9\x01\n\x1e\x44\x65queueSmsMamForManualApproval\x12..api.v0alpha.DequeueSmsMamForManualApprovalReq\x1a..api.v0alpha.DequeueSmsMamForManualApprovalRes\"G\xba\xb8\x91\x02\x02\x18\x01\x82\xd3\xe4\x93\x02:\"5/api/v0alpha/callqueue/dequeuesmsmamformanualapproval:\x01*Bn\n\x0f\x63om.api.v0alphaB\x0e\x43\x61llqueueProtoP\x01\xa2\x02\x03\x41VX\xaa\x02\x0b\x41pi.V0alpha\xca\x02\x0b\x41pi\\V0alpha\xe2\x02\x17\x41pi\\V0alpha\\GPBMetadata\xea\x02\x0c\x41pi::V0alphab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.v0alpha.callqueue_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\017com.api.v0alphaB\016CallqueueProtoP\001\242\002\003AVX\252\002\013Api.V0alpha\312\002\013Api\\V0alpha\342\002\027Api\\V0alpha\\GPBMetadata\352\002\014Api::V0alpha'
  _globals['_CALLQUEUE'].methods_by_name['DequeuePreviewRecordOrCall']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['DequeuePreviewRecordOrCall']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0026\"1/api/v0alpha/callqueue/dequeuepreviewrecordorcall:\001*'
  _globals['_CALLQUEUE'].methods_by_name['EnqueuePreviewRecord']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['EnqueuePreviewRecord']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0020\"+/api/v0alpha/callqueue/enqueuepreviewrecord:\001*'
  _globals['_CALLQUEUE'].methods_by_name['DequeueScrubbedCallForPreviewRecord']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['DequeueScrubbedCallForPreviewRecord']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002?\":/api/v0alpha/callqueue/dequeuescrubbedcallforpreviewrecord:\001*'
  _globals['_CALLQUEUE'].methods_by_name['ClearPreviewRecordReturnQueue']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['ClearPreviewRecordReturnQueue']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0029\"4/api/v0alpha/callqueue/clearpreviewrecordreturnqueue:\001*'
  _globals['_CALLQUEUE'].methods_by_name['EnqueuePreviewDialCall']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['EnqueuePreviewDialCall']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0022\"-/api/v0alpha/callqueue/enqueuepreviewdialcall:\001*'
  _globals['_CALLQUEUE'].methods_by_name['ClearManualDialQueue']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['ClearManualDialQueue']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0020\"+/api/v0alpha/callqueue/clearmanualdialqueue:\001*'
  _globals['_CALLQUEUE'].methods_by_name['ProcessManualDialCall']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['ProcessManualDialCall']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0021\",/api/v0alpha/callqueue/processmanualdialcall:\001*'
  _globals['_CALLQUEUE'].methods_by_name['DequeueCallForManualApproval']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['DequeueCallForManualApproval']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0028\"3/api/v0alpha/callqueue/dequeuecallformanualapproval:\001*'
  _globals['_CALLQUEUE'].methods_by_name['EnqueueManuallyApprovedCall']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['EnqueueManuallyApprovedCall']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0027\"2/api/v0alpha/callqueue/enqueuemanuallyapprovedcall:\001*'
  _globals['_CALLQUEUE'].methods_by_name['EnqueueManuallyRejectedCall']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['EnqueueManuallyRejectedCall']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0027\"2/api/v0alpha/callqueue/enqueuemanuallyrejectedcall:\001*'
  _globals['_CALLQUEUE'].methods_by_name['RequeueManuallyApprovedCall']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['RequeueManuallyApprovedCall']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0027\"2/api/v0alpha/callqueue/requeuemanuallyapprovedcall:\001*'
  _globals['_CALLQUEUE'].methods_by_name['EnqueueManuallyApprovedSms']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['EnqueueManuallyApprovedSms']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0026\"1/api/v0alpha/callqueue/enqueuemanuallyapprovedsms:\001*'
  _globals['_CALLQUEUE'].methods_by_name['EnqueueManuallyRejectedSms']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['EnqueueManuallyRejectedSms']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0026\"1/api/v0alpha/callqueue/enqueuemanuallyrejectedsms:\001*'
  _globals['_CALLQUEUE'].methods_by_name['RequeueManuallyApprovedSms']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['RequeueManuallyApprovedSms']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\0026\"1/api/v0alpha/callqueue/requeuemanuallyapprovedsms:\001*'
  _globals['_CALLQUEUE'].methods_by_name['DequeueSmsMamForManualApproval']._loaded_options = None
  _globals['_CALLQUEUE'].methods_by_name['DequeueSmsMamForManualApproval']._serialized_options = b'\272\270\221\002\002\030\001\202\323\344\223\002:\"5/api/v0alpha/callqueue/dequeuesmsmamformanualapproval:\001*'
  _globals['_DEQUEUEPREVIEWRECORDORCALLREQ']._serialized_start=171
  _globals['_DEQUEUEPREVIEWRECORDORCALLREQ']._serialized_end=287
  _globals['_DEQUEUEPREVIEWRECORDORCALLRES']._serialized_start=290
  _globals['_DEQUEUEPREVIEWRECORDORCALLRES']._serialized_end=456
  _globals['_ENQUEUEPREVIEWRECORDREQ']._serialized_start=458
  _globals['_ENQUEUEPREVIEWRECORDREQ']._serialized_end=569
  _globals['_ENQUEUEPREVIEWRECORDRES']._serialized_start=571
  _globals['_ENQUEUEPREVIEWRECORDRES']._serialized_end=596
  _globals['_DEQUEUESCRUBBEDCALLFORPREVIEWRECORDREQ']._serialized_start=599
  _globals['_DEQUEUESCRUBBEDCALLFORPREVIEWRECORDREQ']._serialized_end=817
  _globals['_DEQUEUESCRUBBEDCALLFORPREVIEWRECORDRES']._serialized_start=819
  _globals['_DEQUEUESCRUBBEDCALLFORPREVIEWRECORDRES']._serialized_end=908
  _globals['_CLEARPREVIEWRECORDRETURNQUEUEREQ']._serialized_start=910
  _globals['_CLEARPREVIEWRECORDRETURNQUEUEREQ']._serialized_end=944
  _globals['_CLEARPREVIEWRECORDRETURNQUEUERES']._serialized_start=946
  _globals['_CLEARPREVIEWRECORDRETURNQUEUERES']._serialized_end=980
  _globals['_ENQUEUEPREVIEWDIALCALLREQ']._serialized_start=982
  _globals['_ENQUEUEPREVIEWDIALCALLREQ']._serialized_end=1089
  _globals['_ENQUEUEPREVIEWDIALCALLRES']._serialized_start=1091
  _globals['_ENQUEUEPREVIEWDIALCALLRES']._serialized_end=1118
  _globals['_CLEARMANUALDIALQUEUEREQ']._serialized_start=1120
  _globals['_CLEARMANUALDIALQUEUEREQ']._serialized_end=1145
  _globals['_CLEARMANUALDIALQUEUERES']._serialized_start=1147
  _globals['_CLEARMANUALDIALQUEUERES']._serialized_end=1172
  _globals['_PROCESSMANUALDIALCALLREQ']._serialized_start=1174
  _globals['_PROCESSMANUALDIALCALLREQ']._serialized_end=1249
  _globals['_PROCESSMANUALDIALCALLRES']._serialized_start=1251
  _globals['_PROCESSMANUALDIALCALLRES']._serialized_end=1343
  _globals['_DEQUEUECALLFORMANUALAPPROVALREQ']._serialized_start=1346
  _globals['_DEQUEUECALLFORMANUALAPPROVALREQ']._serialized_end=1502
  _globals['_DEQUEUECALLFORMANUALAPPROVALRES']._serialized_start=1505
  _globals['_DEQUEUECALLFORMANUALAPPROVALRES']._serialized_end=1773
  _globals['_ENQUEUEMANUALLYAPPROVEDCALLREQ']._serialized_start=1775
  _globals['_ENQUEUEMANUALLYAPPROVEDCALLREQ']._serialized_end=1856
  _globals['_ENQUEUEMANUALLYAPPROVEDCALLRES']._serialized_start=1858
  _globals['_ENQUEUEMANUALLYAPPROVEDCALLRES']._serialized_end=1890
  _globals['_ENQUEUEMANUALLYREJECTEDCALLREQ']._serialized_start=1892
  _globals['_ENQUEUEMANUALLYREJECTEDCALLREQ']._serialized_end=1973
  _globals['_ENQUEUEMANUALLYREJECTEDCALLRES']._serialized_start=1975
  _globals['_ENQUEUEMANUALLYREJECTEDCALLRES']._serialized_end=2007
  _globals['_REQUEUEMANUALLYAPPROVEDCALLREQ']._serialized_start=2009
  _globals['_REQUEUEMANUALLYAPPROVEDCALLREQ']._serialized_end=2121
  _globals['_REQUEUEMANUALLYAPPROVEDCALLRES']._serialized_start=2123
  _globals['_REQUEUEMANUALLYAPPROVEDCALLRES']._serialized_end=2155
  _globals['_ENQUEUEMANUALLYAPPROVEDSMSREQ']._serialized_start=2157
  _globals['_ENQUEUEMANUALLYAPPROVEDSMSREQ']._serialized_end=2237
  _globals['_ENQUEUEMANUALLYAPPROVEDSMSRES']._serialized_start=2239
  _globals['_ENQUEUEMANUALLYAPPROVEDSMSRES']._serialized_end=2270
  _globals['_ENQUEUEMANUALLYREJECTEDSMSREQ']._serialized_start=2272
  _globals['_ENQUEUEMANUALLYREJECTEDSMSREQ']._serialized_end=2352
  _globals['_ENQUEUEMANUALLYREJECTEDSMSRES']._serialized_start=2354
  _globals['_ENQUEUEMANUALLYREJECTEDSMSRES']._serialized_end=2385
  _globals['_REQUEUEMANUALLYAPPROVEDSMSREQ']._serialized_start=2387
  _globals['_REQUEUEMANUALLYAPPROVEDSMSREQ']._serialized_end=2498
  _globals['_REQUEUEMANUALLYAPPROVEDSMSRES']._serialized_start=2500
  _globals['_REQUEUEMANUALLYAPPROVEDSMSRES']._serialized_end=2531
  _globals['_DEQUEUESMSMAMFORMANUALAPPROVALREQ']._serialized_start=2533
  _globals['_DEQUEUESMSMAMFORMANUALAPPROVALREQ']._serialized_end=2606
  _globals['_DEQUEUESMSMAMFORMANUALAPPROVALRES']._serialized_start=2608
  _globals['_DEQUEUESMSMAMFORMANUALAPPROVALRES']._serialized_end=2714
  _globals['_CALLQUEUE']._serialized_start=2717
  _globals['_CALLQUEUE']._serialized_end=5548
# @@protoc_insertion_point(module_scope)
