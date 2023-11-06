from annotations import authz_pb2 as _authz_pb2
from api.commons import acd_pb2 as _acd_pb2
from api.commons import cbs_pb2 as _cbs_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateServiceIdReq(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateServiceIdRes(_message.Message):
    __slots__ = ("service_id",)
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    service_id: str
    def __init__(self, service_id: _Optional[str] = ...) -> None: ...

class ScheduledCallback(_message.Message):
    __slots__ = ("scheduled_callback_id", "service_id", "status", "start_time", "end_time", "phone_number", "caller_id", "notes", "create_date", "last_update", "last_updated_by", "callback_skills")
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_SKILLS_FIELD_NUMBER: _ClassVar[int]
    scheduled_callback_id: str
    service_id: str
    status: _cbs_pb2.ScheduledCallbackStatus
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    phone_number: str
    caller_id: str
    notes: str
    create_date: _timestamp_pb2.Timestamp
    last_update: _timestamp_pb2.Timestamp
    last_updated_by: str
    callback_skills: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, scheduled_callback_id: _Optional[str] = ..., service_id: _Optional[str] = ..., status: _Optional[_Union[_cbs_pb2.ScheduledCallbackStatus, str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., notes: _Optional[str] = ..., create_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_update: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_updated_by: _Optional[str] = ..., callback_skills: _Optional[_Iterable[str]] = ...) -> None: ...

class ScheduledCallbackDetail(_message.Message):
    __slots__ = ("scheduled_callback_detail_id", "scheduled_callback_id", "key", "value")
    SCHEDULED_CALLBACK_DETAIL_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    scheduled_callback_detail_id: str
    scheduled_callback_id: str
    key: str
    value: str
    def __init__(self, scheduled_callback_detail_id: _Optional[str] = ..., scheduled_callback_id: _Optional[str] = ..., key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class UpdateScheduledCallbackToReadyReq(_message.Message):
    __slots__ = ("scheduled_callback_id", "is_auto_return", "service_id")
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    IS_AUTO_RETURN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    scheduled_callback_id: str
    is_auto_return: bool
    service_id: str
    def __init__(self, scheduled_callback_id: _Optional[str] = ..., is_auto_return: bool = ..., service_id: _Optional[str] = ...) -> None: ...

class UpdateScheduledCallbackToReadyRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateScheduledCallbackToCanceledReq(_message.Message):
    __slots__ = ("scheduled_callback_id", "service_id")
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    scheduled_callback_id: str
    service_id: str
    def __init__(self, scheduled_callback_id: _Optional[str] = ..., service_id: _Optional[str] = ...) -> None: ...

class UpdateScheduledCallbackToCanceledRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateScheduledCallbackToClosedReq(_message.Message):
    __slots__ = ("scheduled_callback_id", "manual_dial_call_sid", "service_id")
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    MANUAL_DIAL_CALL_SID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    scheduled_callback_id: str
    manual_dial_call_sid: int
    service_id: str
    def __init__(self, scheduled_callback_id: _Optional[str] = ..., manual_dial_call_sid: _Optional[int] = ..., service_id: _Optional[str] = ...) -> None: ...

class UpdateScheduledCallbackToClosedRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreateCallbackWithDetailsReq(_message.Message):
    __slots__ = ("callback", "callback_details", "name", "former_call_type", "former_call_sid", "country_sid", "manager_login")
    CALLBACK_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORMER_CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMER_CALL_SID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    MANAGER_LOGIN_FIELD_NUMBER: _ClassVar[int]
    callback: ScheduledCallback
    callback_details: _containers.RepeatedCompositeFieldContainer[ScheduledCallbackDetail]
    name: str
    former_call_type: _acd_pb2.CallType.Enum
    former_call_sid: int
    country_sid: _wrappers_pb2.Int64Value
    manager_login: bool
    def __init__(self, callback: _Optional[_Union[ScheduledCallback, _Mapping]] = ..., callback_details: _Optional[_Iterable[_Union[ScheduledCallbackDetail, _Mapping]]] = ..., name: _Optional[str] = ..., former_call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., former_call_sid: _Optional[int] = ..., country_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., manager_login: bool = ...) -> None: ...

class CreateCallbackWithDetailsRes(_message.Message):
    __slots__ = ("scheduled_callback_id",)
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    scheduled_callback_id: str
    def __init__(self, scheduled_callback_id: _Optional[str] = ...) -> None: ...

class UpdateScheduledCallbackReq(_message.Message):
    __slots__ = ("scheduled_callback_id", "new_status", "start_time", "end_time", "phone_number", "caller_id", "skills", "last_updated_by", "notes", "callback_details", "name")
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    scheduled_callback_id: str
    new_status: _cbs_pb2.ScheduledCallbackStatus
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    phone_number: str
    caller_id: str
    skills: _containers.RepeatedScalarFieldContainer[str]
    last_updated_by: str
    notes: str
    callback_details: _containers.RepeatedCompositeFieldContainer[ScheduledCallbackDetail]
    name: str
    def __init__(self, scheduled_callback_id: _Optional[str] = ..., new_status: _Optional[_Union[_cbs_pb2.ScheduledCallbackStatus, str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., skills: _Optional[_Iterable[str]] = ..., last_updated_by: _Optional[str] = ..., notes: _Optional[str] = ..., callback_details: _Optional[_Iterable[_Union[ScheduledCallbackDetail, _Mapping]]] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateScheduledCallbackRes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ScheduledCallbackWithDetails(_message.Message):
    __slots__ = ("scheduled_callback_id", "service_id", "status", "start_time", "end_time", "phone_number", "caller_id", "skills", "notes", "create_date", "last_update", "created_by", "last_updated_by", "name", "former_call_sid", "former_call_type", "callback_details", "country_sid")
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_BY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORMER_CALL_SID_FIELD_NUMBER: _ClassVar[int]
    FORMER_CALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALLBACK_DETAILS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    scheduled_callback_id: str
    service_id: str
    status: _cbs_pb2.ScheduledCallbackStatus
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    phone_number: str
    caller_id: str
    skills: _containers.RepeatedScalarFieldContainer[str]
    notes: str
    create_date: _timestamp_pb2.Timestamp
    last_update: _timestamp_pb2.Timestamp
    created_by: str
    last_updated_by: str
    name: str
    former_call_sid: int
    former_call_type: _acd_pb2.CallType.Enum
    callback_details: _containers.RepeatedCompositeFieldContainer[ScheduledCallbackDetail]
    country_sid: _wrappers_pb2.Int64Value
    def __init__(self, scheduled_callback_id: _Optional[str] = ..., service_id: _Optional[str] = ..., status: _Optional[_Union[_cbs_pb2.ScheduledCallbackStatus, str]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., skills: _Optional[_Iterable[str]] = ..., notes: _Optional[str] = ..., create_date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_update: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_by: _Optional[str] = ..., last_updated_by: _Optional[str] = ..., name: _Optional[str] = ..., former_call_sid: _Optional[int] = ..., former_call_type: _Optional[_Union[_acd_pb2.CallType.Enum, str]] = ..., callback_details: _Optional[_Iterable[_Union[ScheduledCallbackDetail, _Mapping]]] = ..., country_sid: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class GetScheduledCallbackWithDetailsReq(_message.Message):
    __slots__ = ("service_id", "scheduled_callback_id")
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_CALLBACK_ID_FIELD_NUMBER: _ClassVar[int]
    service_id: str
    scheduled_callback_id: str
    def __init__(self, service_id: _Optional[str] = ..., scheduled_callback_id: _Optional[str] = ...) -> None: ...

class GetScheduledCallbackWithDetailsRes(_message.Message):
    __slots__ = ("callback",)
    CALLBACK_FIELD_NUMBER: _ClassVar[int]
    callback: ScheduledCallbackWithDetails
    def __init__(self, callback: _Optional[_Union[ScheduledCallbackWithDetails, _Mapping]] = ...) -> None: ...

class ListScheduledCallbacksWithDetailsRes(_message.Message):
    __slots__ = ("callbacks",)
    CALLBACKS_FIELD_NUMBER: _ClassVar[int]
    callbacks: _containers.RepeatedCompositeFieldContainer[ScheduledCallbackWithDetails]
    def __init__(self, callbacks: _Optional[_Iterable[_Union[ScheduledCallbackWithDetails, _Mapping]]] = ...) -> None: ...

class GetNextScheduledCallbackWithDetailsReq(_message.Message):
    __slots__ = ("service_id", "agent_skills")
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SKILLS_FIELD_NUMBER: _ClassVar[int]
    service_id: str
    agent_skills: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, service_id: _Optional[str] = ..., agent_skills: _Optional[_Iterable[str]] = ...) -> None: ...

class GetNextScheduledCallbackWithDetailsRes(_message.Message):
    __slots__ = ("scheduled_callback",)
    SCHEDULED_CALLBACK_FIELD_NUMBER: _ClassVar[int]
    scheduled_callback: ScheduledCallbackWithDetails
    def __init__(self, scheduled_callback: _Optional[_Union[ScheduledCallbackWithDetails, _Mapping]] = ...) -> None: ...

class ListScheduledCallbacksWithDetailsReq(_message.Message):
    __slots__ = ("phone_number", "caller_id", "from_start_time", "to_start_time", "skills")
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    FROM_START_TIME_FIELD_NUMBER: _ClassVar[int]
    TO_START_TIME_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    caller_id: str
    from_start_time: _timestamp_pb2.Timestamp
    to_start_time: _timestamp_pb2.Timestamp
    skills: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, phone_number: _Optional[str] = ..., caller_id: _Optional[str] = ..., from_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., to_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., skills: _Optional[_Iterable[str]] = ...) -> None: ...

class ListScheduledCallbacksWithDetailsBySkillsReq(_message.Message):
    __slots__ = ("service_id", "skills")
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SKILLS_FIELD_NUMBER: _ClassVar[int]
    service_id: str
    skills: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, service_id: _Optional[str] = ..., skills: _Optional[_Iterable[str]] = ...) -> None: ...
