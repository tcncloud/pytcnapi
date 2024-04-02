from api.commons import org_pb2 as _org_pb2
from api.commons.org import preferences_pb2 as _preferences_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListObservedHolidaysRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListObservedHolidaysResponse(_message.Message):
    __slots__ = ("observed_holidays",)
    OBSERVED_HOLIDAYS_FIELD_NUMBER: _ClassVar[int]
    observed_holidays: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.ObservedHolidays]
    def __init__(self, observed_holidays: _Optional[_Iterable[_Union[_preferences_pb2.ObservedHolidays, _Mapping]]] = ...) -> None: ...

class GetObservedHolidaysRequest(_message.Message):
    __slots__ = ("observed_holidays_id",)
    OBSERVED_HOLIDAYS_ID_FIELD_NUMBER: _ClassVar[int]
    observed_holidays_id: str
    def __init__(self, observed_holidays_id: _Optional[str] = ...) -> None: ...

class GetObservedHolidaysResponse(_message.Message):
    __slots__ = ("observed_holidays",)
    OBSERVED_HOLIDAYS_FIELD_NUMBER: _ClassVar[int]
    observed_holidays: _preferences_pb2.ObservedHolidays
    def __init__(self, observed_holidays: _Optional[_Union[_preferences_pb2.ObservedHolidays, _Mapping]] = ...) -> None: ...

class SetObservedHolidaysRequest(_message.Message):
    __slots__ = ("observed_holidays_name", "description", "timezone", "days")
    OBSERVED_HOLIDAYS_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    observed_holidays_name: str
    description: str
    timezone: _org_pb2.TimeZone
    days: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.ObservedHoliday]
    def __init__(self, observed_holidays_name: _Optional[str] = ..., description: _Optional[str] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., days: _Optional[_Iterable[_Union[_preferences_pb2.ObservedHoliday, _Mapping]]] = ...) -> None: ...

class SetObservedHolidaysResponse(_message.Message):
    __slots__ = ("observed_holidays_id",)
    OBSERVED_HOLIDAYS_ID_FIELD_NUMBER: _ClassVar[int]
    observed_holidays_id: str
    def __init__(self, observed_holidays_id: _Optional[str] = ...) -> None: ...

class AddToObservedHolidaysRequest(_message.Message):
    __slots__ = ("observed_holidays_id", "day")
    OBSERVED_HOLIDAYS_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    observed_holidays_id: str
    day: _preferences_pb2.ObservedHoliday
    def __init__(self, observed_holidays_id: _Optional[str] = ..., day: _Optional[_Union[_preferences_pb2.ObservedHoliday, _Mapping]] = ...) -> None: ...

class AddToObservedHolidaysResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveFromObservedHolidaysRequest(_message.Message):
    __slots__ = ("observed_holidays_id", "day")
    OBSERVED_HOLIDAYS_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    observed_holidays_id: str
    day: _preferences_pb2.ObservedHoliday
    def __init__(self, observed_holidays_id: _Optional[str] = ..., day: _Optional[_Union[_preferences_pb2.ObservedHoliday, _Mapping]] = ...) -> None: ...

class RemoveFromObservedHolidaysResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateObservedHolidaysInfoRequest(_message.Message):
    __slots__ = ("observed_holidays_id", "observed_holidays_name", "description", "timezone", "field_mask")
    OBSERVED_HOLIDAYS_ID_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_HOLIDAYS_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    observed_holidays_id: str
    observed_holidays_name: str
    description: str
    timezone: _org_pb2.TimeZone
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, observed_holidays_id: _Optional[str] = ..., observed_holidays_name: _Optional[str] = ..., description: _Optional[str] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateObservedHolidaysInfoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteObservedHolidaysRequest(_message.Message):
    __slots__ = ("observed_holidays_id",)
    OBSERVED_HOLIDAYS_ID_FIELD_NUMBER: _ClassVar[int]
    observed_holidays_id: str
    def __init__(self, observed_holidays_id: _Optional[str] = ...) -> None: ...

class DeleteObservedHolidaysResponse(_message.Message):
    __slots__ = ("observed_holidays_id",)
    OBSERVED_HOLIDAYS_ID_FIELD_NUMBER: _ClassVar[int]
    observed_holidays_id: str
    def __init__(self, observed_holidays_id: _Optional[str] = ...) -> None: ...

class EvaluateObservedHolidaysRequest(_message.Message):
    __slots__ = ("observed_holidays_id",)
    OBSERVED_HOLIDAYS_ID_FIELD_NUMBER: _ClassVar[int]
    observed_holidays_id: str
    def __init__(self, observed_holidays_id: _Optional[str] = ...) -> None: ...

class EvaluateObservedHolidaysResponse(_message.Message):
    __slots__ = ("date_matched",)
    DATE_MATCHED_FIELD_NUMBER: _ClassVar[int]
    date_matched: bool
    def __init__(self, date_matched: bool = ...) -> None: ...
