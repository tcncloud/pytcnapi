from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SMSStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SMS_UNKWNON: _ClassVar[SMSStatus]
    SMS_PREPARING: _ClassVar[SMSStatus]
    SMS_SCHEDULED: _ClassVar[SMSStatus]
    SMS_RESUME: _ClassVar[SMSStatus]
    SMS_RUNNING: _ClassVar[SMSStatus]
    SMS_COMPLETED: _ClassVar[SMSStatus]
    SMS_CANCELLED: _ClassVar[SMSStatus]
    SMS_CANCELLED_ADMIN: _ClassVar[SMSStatus]
    SMS_SUMMED_COMPLETED: _ClassVar[SMSStatus]
    SMS_SUMMED_CANCELLED: _ClassVar[SMSStatus]
    SMS_SUMMED_CANCELLED_ADMIN: _ClassVar[SMSStatus]
    SMS_PAUSED: _ClassVar[SMSStatus]
    SMS_TASK_WAITING: _ClassVar[SMSStatus]
    SMS_TASK_PROCESSING: _ClassVar[SMSStatus]
    SMS_TASK_DNC: _ClassVar[SMSStatus]
    SMS_TASK_INVALID: _ClassVar[SMSStatus]
    SMS_TASK_QUEUED: _ClassVar[SMSStatus]
    SMS_TASK_SENT: _ClassVar[SMSStatus]
    SMS_TASK_DELIVERED: _ClassVar[SMSStatus]
    SMS_TASK_NOT_DELIVERED: _ClassVar[SMSStatus]
    SMS_TASK_CANCELED: _ClassVar[SMSStatus]

class SMSIBGroupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IB_SMS_GROUP_UNKNOWN: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_PREPARING: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_SCHEDULED: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_RUNNING: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_PAUSED: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_RESUME: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_COMPLETED: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_CANCELLED_USER: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_CANCELLED_ADMIN: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_SUMMED_COMPLETED: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_SUMMED_CANCELLED_USER: _ClassVar[SMSIBGroupStatus]
    IB_SMS_GROUP_SUMMED_CANCELLED_ADMIN: _ClassVar[SMSIBGroupStatus]

class SMSIBTaskStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    IB_SMS_TASK_UNKNOWN: _ClassVar[SMSIBTaskStatus]
    IB_SMS_TASK_COMPLETED: _ClassVar[SMSIBTaskStatus]

class SMSConversationAuditAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SMS_AUDIT_ACTION_CONVERSATION_START: _ClassVar[SMSConversationAuditAction]
    SMS_AUDIT_ACTION_CONVERSATION_MSG_SENT: _ClassVar[SMSConversationAuditAction]
    SMS_AUDIT_ACTION_CONVERSATION_MSG_READ: _ClassVar[SMSConversationAuditAction]
    SMS_AUDIT_ACTION_CONVERSATION_UNASSIGNED: _ClassVar[SMSConversationAuditAction]
    SMS_AUDIT_ACTION_CONVERSATION_ASSIGNED: _ClassVar[SMSConversationAuditAction]
    SMS_AUDIT_ACTION_CONVERSATION_TRANSFERRED: _ClassVar[SMSConversationAuditAction]

class SMSMamStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUEUED: _ClassVar[SMSMamStatus]
    APPROVED: _ClassVar[SMSMamStatus]
    REJECTED: _ClassVar[SMSMamStatus]
SMS_UNKWNON: SMSStatus
SMS_PREPARING: SMSStatus
SMS_SCHEDULED: SMSStatus
SMS_RESUME: SMSStatus
SMS_RUNNING: SMSStatus
SMS_COMPLETED: SMSStatus
SMS_CANCELLED: SMSStatus
SMS_CANCELLED_ADMIN: SMSStatus
SMS_SUMMED_COMPLETED: SMSStatus
SMS_SUMMED_CANCELLED: SMSStatus
SMS_SUMMED_CANCELLED_ADMIN: SMSStatus
SMS_PAUSED: SMSStatus
SMS_TASK_WAITING: SMSStatus
SMS_TASK_PROCESSING: SMSStatus
SMS_TASK_DNC: SMSStatus
SMS_TASK_INVALID: SMSStatus
SMS_TASK_QUEUED: SMSStatus
SMS_TASK_SENT: SMSStatus
SMS_TASK_DELIVERED: SMSStatus
SMS_TASK_NOT_DELIVERED: SMSStatus
SMS_TASK_CANCELED: SMSStatus
IB_SMS_GROUP_UNKNOWN: SMSIBGroupStatus
IB_SMS_GROUP_PREPARING: SMSIBGroupStatus
IB_SMS_GROUP_SCHEDULED: SMSIBGroupStatus
IB_SMS_GROUP_RUNNING: SMSIBGroupStatus
IB_SMS_GROUP_PAUSED: SMSIBGroupStatus
IB_SMS_GROUP_RESUME: SMSIBGroupStatus
IB_SMS_GROUP_COMPLETED: SMSIBGroupStatus
IB_SMS_GROUP_CANCELLED_USER: SMSIBGroupStatus
IB_SMS_GROUP_CANCELLED_ADMIN: SMSIBGroupStatus
IB_SMS_GROUP_SUMMED_COMPLETED: SMSIBGroupStatus
IB_SMS_GROUP_SUMMED_CANCELLED_USER: SMSIBGroupStatus
IB_SMS_GROUP_SUMMED_CANCELLED_ADMIN: SMSIBGroupStatus
IB_SMS_TASK_UNKNOWN: SMSIBTaskStatus
IB_SMS_TASK_COMPLETED: SMSIBTaskStatus
SMS_AUDIT_ACTION_CONVERSATION_START: SMSConversationAuditAction
SMS_AUDIT_ACTION_CONVERSATION_MSG_SENT: SMSConversationAuditAction
SMS_AUDIT_ACTION_CONVERSATION_MSG_READ: SMSConversationAuditAction
SMS_AUDIT_ACTION_CONVERSATION_UNASSIGNED: SMSConversationAuditAction
SMS_AUDIT_ACTION_CONVERSATION_ASSIGNED: SMSConversationAuditAction
SMS_AUDIT_ACTION_CONVERSATION_TRANSFERRED: SMSConversationAuditAction
QUEUED: SMSMamStatus
APPROVED: SMSMamStatus
REJECTED: SMSMamStatus

class SimpleSmsMamData(_message.Message):
    __slots__ = ()
    SRC_FIELD_NUMBER: _ClassVar[int]
    DST_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    SMS_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    SMS_TASK_SID_FIELD_NUMBER: _ClassVar[int]
    IS_TOLL_FREE_FIELD_NUMBER: _ClassVar[int]
    IS_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    HUNT_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_SMS_MAM_META_DATA_FIELD_NUMBER: _ClassVar[int]
    DST_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    src: str
    dst: str
    msg: str
    sms_group_sid: int
    sms_task_sid: int
    is_toll_free: str
    is_time_zone: str
    provider_name: str
    hunt_group_sid: int
    client_sid: int
    simple_sms_mam_meta_data: _containers.RepeatedCompositeFieldContainer[SimpleSmsMamKeyValue]
    dst_country_code: int
    def __init__(self, src: _Optional[str] = ..., dst: _Optional[str] = ..., msg: _Optional[str] = ..., sms_group_sid: _Optional[int] = ..., sms_task_sid: _Optional[int] = ..., is_toll_free: _Optional[str] = ..., is_time_zone: _Optional[str] = ..., provider_name: _Optional[str] = ..., hunt_group_sid: _Optional[int] = ..., client_sid: _Optional[int] = ..., simple_sms_mam_meta_data: _Optional[_Iterable[_Union[SimpleSmsMamKeyValue, _Mapping]]] = ..., dst_country_code: _Optional[int] = ...) -> None: ...

class SimpleSmsMamKeyValue(_message.Message):
    __slots__ = ()
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
