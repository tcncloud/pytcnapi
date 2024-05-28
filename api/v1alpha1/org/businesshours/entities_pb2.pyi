from api.commons import org_pb2 as _org_pb2
from api.commons.org import preferences_pb2 as _preferences_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListBusinessHoursRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListBusinessHoursResponse(_message.Message):
    __slots__ = ("business_hours",)
    BUSINESS_HOURS_FIELD_NUMBER: _ClassVar[int]
    business_hours: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.BusinessHours]
    def __init__(self, business_hours: _Optional[_Iterable[_Union[_preferences_pb2.BusinessHours, _Mapping]]] = ...) -> None: ...

class GetBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_id",)
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    def __init__(self, business_hours_id: _Optional[str] = ...) -> None: ...

class GetBusinessHoursResponse(_message.Message):
    __slots__ = ("business_hours",)
    BUSINESS_HOURS_FIELD_NUMBER: _ClassVar[int]
    business_hours: _preferences_pb2.BusinessHours
    def __init__(self, business_hours: _Optional[_Union[_preferences_pb2.BusinessHours, _Mapping]] = ...) -> None: ...

class SetBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_name", "description", "day_intervals", "timezone")
    BUSINESS_HOURS_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DAY_INTERVALS_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    business_hours_name: str
    description: str
    day_intervals: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.DayInterval]
    timezone: _org_pb2.TimeZone
    def __init__(self, business_hours_name: _Optional[str] = ..., description: _Optional[str] = ..., day_intervals: _Optional[_Iterable[_Union[_preferences_pb2.DayInterval, _Mapping]]] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ...) -> None: ...

class SetBusinessHoursResponse(_message.Message):
    __slots__ = ("business_hours_id",)
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    def __init__(self, business_hours_id: _Optional[str] = ...) -> None: ...

class AddIntervalToBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_id", "day_interval")
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    day_interval: _preferences_pb2.DayInterval
    def __init__(self, business_hours_id: _Optional[str] = ..., day_interval: _Optional[_Union[_preferences_pb2.DayInterval, _Mapping]] = ...) -> None: ...

class AddIntervalToBusinessHoursResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveIntervalFromBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_id", "day_interval")
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    day_interval: _preferences_pb2.DayInterval
    def __init__(self, business_hours_id: _Optional[str] = ..., day_interval: _Optional[_Union[_preferences_pb2.DayInterval, _Mapping]] = ...) -> None: ...

class RemoveIntervalFromBusinessHoursResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateBusinessHoursInfoRequest(_message.Message):
    __slots__ = ("business_hours_id", "business_hours_name", "description", "timezone", "field_mask")
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    BUSINESS_HOURS_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    business_hours_name: str
    description: str
    timezone: _org_pb2.TimeZone
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, business_hours_id: _Optional[str] = ..., business_hours_name: _Optional[str] = ..., description: _Optional[str] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateBusinessHoursInfoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_id",)
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    def __init__(self, business_hours_id: _Optional[str] = ...) -> None: ...

class DeleteBusinessHoursResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EvaluateBusinessHoursRequest(_message.Message):
    __slots__ = ("business_hours_id",)
    BUSINESS_HOURS_ID_FIELD_NUMBER: _ClassVar[int]
    business_hours_id: str
    def __init__(self, business_hours_id: _Optional[str] = ...) -> None: ...

class EvaluateBusinessHoursResponse(_message.Message):
    __slots__ = ("within_range", "result_expiration")
    WITHIN_RANGE_FIELD_NUMBER: _ClassVar[int]
    RESULT_EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    within_range: bool
    result_expiration: _timestamp_pb2.Timestamp
    def __init__(self, within_range: bool = ..., result_expiration: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
