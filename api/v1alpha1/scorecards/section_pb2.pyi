from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSectionRequest(_message.Message):
    __slots__ = ("section",)
    SECTION_FIELD_NUMBER: _ClassVar[int]
    section: _scorecards_pb2.Section
    def __init__(self, section: _Optional[_Union[_scorecards_pb2.Section, _Mapping]] = ...) -> None: ...

class CreateSectionResponse(_message.Message):
    __slots__ = ("section",)
    SECTION_FIELD_NUMBER: _ClassVar[int]
    section: _scorecards_pb2.Section
    def __init__(self, section: _Optional[_Union[_scorecards_pb2.Section, _Mapping]] = ...) -> None: ...

class ListSectionsRequest(_message.Message):
    __slots__ = ("scorecard_id",)
    SCORECARD_ID_FIELD_NUMBER: _ClassVar[int]
    scorecard_id: int
    def __init__(self, scorecard_id: _Optional[int] = ...) -> None: ...

class ListSectionsResponse(_message.Message):
    __slots__ = ("sections",)
    SECTIONS_FIELD_NUMBER: _ClassVar[int]
    sections: _containers.RepeatedCompositeFieldContainer[_scorecards_pb2.Section]
    def __init__(self, sections: _Optional[_Iterable[_Union[_scorecards_pb2.Section, _Mapping]]] = ...) -> None: ...

class UpdateSectionRequest(_message.Message):
    __slots__ = ("section", "update_mask")
    SECTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    section: _scorecards_pb2.Section
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, section: _Optional[_Union[_scorecards_pb2.Section, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSectionResponse(_message.Message):
    __slots__ = ("section",)
    SECTION_FIELD_NUMBER: _ClassVar[int]
    section: _scorecards_pb2.Section
    def __init__(self, section: _Optional[_Union[_scorecards_pb2.Section, _Mapping]] = ...) -> None: ...

class DeleteSectionRequest(_message.Message):
    __slots__ = ("section_id",)
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    section_id: int
    def __init__(self, section_id: _Optional[int] = ...) -> None: ...

class DeleteSectionResponse(_message.Message):
    __slots__ = ("section",)
    SECTION_FIELD_NUMBER: _ClassVar[int]
    section: _scorecards_pb2.Section
    def __init__(self, section: _Optional[_Union[_scorecards_pb2.Section, _Mapping]] = ...) -> None: ...

class GetSectionRequest(_message.Message):
    __slots__ = ("section_id",)
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    section_id: int
    def __init__(self, section_id: _Optional[int] = ...) -> None: ...

class GetSectionResponse(_message.Message):
    __slots__ = ("section",)
    SECTION_FIELD_NUMBER: _ClassVar[int]
    section: _scorecards_pb2.Section
    def __init__(self, section: _Optional[_Union[_scorecards_pb2.Section, _Mapping]] = ...) -> None: ...
