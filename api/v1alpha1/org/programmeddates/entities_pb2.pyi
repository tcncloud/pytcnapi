from api.commons import org_pb2 as _org_pb2
from api.commons.org import preferences_pb2 as _preferences_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListProgrammedDatesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListProgrammedDatesResponse(_message.Message):
    __slots__ = ("programmed_dates",)
    PROGRAMMED_DATES_FIELD_NUMBER: _ClassVar[int]
    programmed_dates: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.ProgrammedDates]
    def __init__(self, programmed_dates: _Optional[_Iterable[_Union[_preferences_pb2.ProgrammedDates, _Mapping]]] = ...) -> None: ...

class GetProgrammedDatesRequest(_message.Message):
    __slots__ = ("programmed_dates_id",)
    PROGRAMMED_DATES_ID_FIELD_NUMBER: _ClassVar[int]
    programmed_dates_id: str
    def __init__(self, programmed_dates_id: _Optional[str] = ...) -> None: ...

class GetProgrammedDatesResponse(_message.Message):
    __slots__ = ("dates",)
    DATES_FIELD_NUMBER: _ClassVar[int]
    dates: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.ProgrammedDates]
    def __init__(self, dates: _Optional[_Iterable[_Union[_preferences_pb2.ProgrammedDates, _Mapping]]] = ...) -> None: ...

class SetProgrammedDatesRequest(_message.Message):
    __slots__ = ("programmed_dates_name", "description", "timezone", "days")
    PROGRAMMED_DATES_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    programmed_dates_name: str
    description: str
    timezone: _org_pb2.TimeZone
    days: _containers.RepeatedCompositeFieldContainer[_preferences_pb2.ProgrammedDay]
    def __init__(self, programmed_dates_name: _Optional[str] = ..., description: _Optional[str] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., days: _Optional[_Iterable[_Union[_preferences_pb2.ProgrammedDay, _Mapping]]] = ...) -> None: ...

class SetProgrammedDatesResponse(_message.Message):
    __slots__ = ("programmed_dates_id",)
    PROGRAMMED_DATES_ID_FIELD_NUMBER: _ClassVar[int]
    programmed_dates_id: str
    def __init__(self, programmed_dates_id: _Optional[str] = ...) -> None: ...

class AddToProgrammedDatesRequest(_message.Message):
    __slots__ = ("programmed_dates_id", "day")
    PROGRAMMED_DATES_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    programmed_dates_id: str
    day: _preferences_pb2.ProgrammedDay
    def __init__(self, programmed_dates_id: _Optional[str] = ..., day: _Optional[_Union[_preferences_pb2.ProgrammedDay, _Mapping]] = ...) -> None: ...

class AddToProgrammedDatesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveFromProgrammedDatesRequest(_message.Message):
    __slots__ = ("programmed_dates_id", "day")
    PROGRAMMED_DATES_ID_FIELD_NUMBER: _ClassVar[int]
    DAY_FIELD_NUMBER: _ClassVar[int]
    programmed_dates_id: str
    day: _preferences_pb2.ProgrammedDay
    def __init__(self, programmed_dates_id: _Optional[str] = ..., day: _Optional[_Union[_preferences_pb2.ProgrammedDay, _Mapping]] = ...) -> None: ...

class RemoveFromProgrammedDatesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateProgrammedDatesInfoRequest(_message.Message):
    __slots__ = ("programmed_dates_id", "programmed_dates_name", "description", "timezone", "field_mask")
    PROGRAMMED_DATES_ID_FIELD_NUMBER: _ClassVar[int]
    PROGRAMMED_DATES_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMEZONE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    programmed_dates_id: str
    programmed_dates_name: str
    description: str
    timezone: _org_pb2.TimeZone
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, programmed_dates_id: _Optional[str] = ..., programmed_dates_name: _Optional[str] = ..., description: _Optional[str] = ..., timezone: _Optional[_Union[_org_pb2.TimeZone, str]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateProgrammedDatesInfoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteProgrammedDatesRequest(_message.Message):
    __slots__ = ("programmed_dates_id",)
    PROGRAMMED_DATES_ID_FIELD_NUMBER: _ClassVar[int]
    programmed_dates_id: str
    def __init__(self, programmed_dates_id: _Optional[str] = ...) -> None: ...

class DeleteProgrammedDatesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class EvaluateProgrammedDatesRequest(_message.Message):
    __slots__ = ("programmed_dates_id",)
    PROGRAMMED_DATES_ID_FIELD_NUMBER: _ClassVar[int]
    programmed_dates_id: str
    def __init__(self, programmed_dates_id: _Optional[str] = ...) -> None: ...

class EvaluateProgrammedDatesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
