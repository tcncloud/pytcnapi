from api.commons import results_pb2 as _results_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CallStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CALL_UNKNOWN: _ClassVar[CallStatus]
    CALL_SCHEDULED: _ClassVar[CallStatus]
    CALL_RUNNING: _ClassVar[CallStatus]
    CALL_COMPLETED: _ClassVar[CallStatus]
CALL_UNKNOWN: CallStatus
CALL_SCHEDULED: CallStatus
CALL_RUNNING: CallStatus
CALL_COMPLETED: CallStatus

class SimpleCallData(_message.Message):
    __slots__ = ("task_sid", "call_sid", "task_group_sid", "client_sid", "country_sid", "agent_sid", "start_time", "caller_id", "phone_number", "country_code", "delivery_duration", "link_call_duration", "result", "sip_code", "do_record", "recording_file_name", "is_dial_validation_ok", "is_time_zone_scrub_ok", "is_cell_phone_scrub_ok", "is_custom_calling_rules_scrub_ok", "is_dncl_scrub_ok", "use_global_time_zone_scrub", "do_cell_phone_scrub", "do_dncl_scrub", "call_data_type", "caller_id_country_code", "caller_id_country_sid", "zip_code", "is_preview_by_record", "rule_set_name", "is_natural_compliance_ok", "simple_meta_data", "simple_result_meta_data")
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    CALL_SID_FIELD_NUMBER: _ClassVar[int]
    TASK_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_SID_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_DURATION_FIELD_NUMBER: _ClassVar[int]
    LINK_CALL_DURATION_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SIP_CODE_FIELD_NUMBER: _ClassVar[int]
    DO_RECORD_FIELD_NUMBER: _ClassVar[int]
    RECORDING_FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DIAL_VALIDATION_OK_FIELD_NUMBER: _ClassVar[int]
    IS_TIME_ZONE_SCRUB_OK_FIELD_NUMBER: _ClassVar[int]
    IS_CELL_PHONE_SCRUB_OK_FIELD_NUMBER: _ClassVar[int]
    IS_CUSTOM_CALLING_RULES_SCRUB_OK_FIELD_NUMBER: _ClassVar[int]
    IS_DNCL_SCRUB_OK_FIELD_NUMBER: _ClassVar[int]
    USE_GLOBAL_TIME_ZONE_SCRUB_FIELD_NUMBER: _ClassVar[int]
    DO_CELL_PHONE_SCRUB_FIELD_NUMBER: _ClassVar[int]
    DO_DNCL_SCRUB_FIELD_NUMBER: _ClassVar[int]
    CALL_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    CALLER_ID_COUNTRY_SID_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    IS_PREVIEW_BY_RECORD_FIELD_NUMBER: _ClassVar[int]
    RULE_SET_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_NATURAL_COMPLIANCE_OK_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_META_DATA_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_RESULT_META_DATA_FIELD_NUMBER: _ClassVar[int]
    task_sid: int
    call_sid: int
    task_group_sid: int
    client_sid: int
    country_sid: int
    agent_sid: int
    start_time: int
    caller_id: str
    phone_number: str
    country_code: str
    delivery_duration: int
    link_call_duration: int
    result: _results_pb2.CallResult
    sip_code: int
    do_record: bool
    recording_file_name: str
    is_dial_validation_ok: bool
    is_time_zone_scrub_ok: bool
    is_cell_phone_scrub_ok: bool
    is_custom_calling_rules_scrub_ok: bool
    is_dncl_scrub_ok: bool
    use_global_time_zone_scrub: bool
    do_cell_phone_scrub: bool
    do_dncl_scrub: bool
    call_data_type: str
    caller_id_country_code: str
    caller_id_country_sid: int
    zip_code: str
    is_preview_by_record: bool
    rule_set_name: str
    is_natural_compliance_ok: bool
    simple_meta_data: _containers.RepeatedCompositeFieldContainer[SimpleKeyValue]
    simple_result_meta_data: _containers.RepeatedCompositeFieldContainer[SimpleKeyValue]
    def __init__(self, task_sid: _Optional[int] = ..., call_sid: _Optional[int] = ..., task_group_sid: _Optional[int] = ..., client_sid: _Optional[int] = ..., country_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., start_time: _Optional[int] = ..., caller_id: _Optional[str] = ..., phone_number: _Optional[str] = ..., country_code: _Optional[str] = ..., delivery_duration: _Optional[int] = ..., link_call_duration: _Optional[int] = ..., result: _Optional[_Union[_results_pb2.CallResult, str]] = ..., sip_code: _Optional[int] = ..., do_record: bool = ..., recording_file_name: _Optional[str] = ..., is_dial_validation_ok: bool = ..., is_time_zone_scrub_ok: bool = ..., is_cell_phone_scrub_ok: bool = ..., is_custom_calling_rules_scrub_ok: bool = ..., is_dncl_scrub_ok: bool = ..., use_global_time_zone_scrub: bool = ..., do_cell_phone_scrub: bool = ..., do_dncl_scrub: bool = ..., call_data_type: _Optional[str] = ..., caller_id_country_code: _Optional[str] = ..., caller_id_country_sid: _Optional[int] = ..., zip_code: _Optional[str] = ..., is_preview_by_record: bool = ..., rule_set_name: _Optional[str] = ..., is_natural_compliance_ok: bool = ..., simple_meta_data: _Optional[_Iterable[_Union[SimpleKeyValue, _Mapping]]] = ..., simple_result_meta_data: _Optional[_Iterable[_Union[SimpleKeyValue, _Mapping]]] = ...) -> None: ...

class SimpleKeyValue(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class SimpleRecordData(_message.Message):
    __slots__ = ("task_sid", "task_group_sid", "agent_sid", "start_time", "stop_time")
    TASK_SID_FIELD_NUMBER: _ClassVar[int]
    TASK_GROUP_SID_FIELD_NUMBER: _ClassVar[int]
    AGENT_SID_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STOP_TIME_FIELD_NUMBER: _ClassVar[int]
    task_sid: int
    task_group_sid: int
    agent_sid: int
    start_time: _timestamp_pb2.Timestamp
    stop_time: _timestamp_pb2.Timestamp
    def __init__(self, task_sid: _Optional[int] = ..., task_group_sid: _Optional[int] = ..., agent_sid: _Optional[int] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., stop_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
