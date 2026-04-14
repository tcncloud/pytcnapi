from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSmartEvaluationRequest(_message.Message):
    __slots__ = ("smart_evaluation",)
    SMART_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    smart_evaluation: _scorecards_pb2.SmartEvaluation
    def __init__(self, smart_evaluation: _Optional[_Union[_scorecards_pb2.SmartEvaluation, _Mapping]] = ...) -> None: ...

class CreateSmartEvaluationResponse(_message.Message):
    __slots__ = ("smart_evaluation",)
    SMART_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    smart_evaluation: _scorecards_pb2.SmartEvaluation
    def __init__(self, smart_evaluation: _Optional[_Union[_scorecards_pb2.SmartEvaluation, _Mapping]] = ...) -> None: ...

class ListSmartEvaluationsRequest(_message.Message):
    __slots__ = ("order_by", "page_size", "page_token", "return_fields", "filter")
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RETURN_FIELDS_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    order_by: str
    page_size: int
    page_token: str
    return_fields: _field_mask_pb2.FieldMask
    filter: str
    def __init__(self, order_by: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., return_fields: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., filter: _Optional[str] = ...) -> None: ...

class ListSmartEvaluationsResponse(_message.Message):
    __slots__ = ("smart_evaluations", "next_page_token")
    SMART_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    smart_evaluations: _containers.RepeatedCompositeFieldContainer[_scorecards_pb2.SmartEvaluation]
    next_page_token: str
    def __init__(self, smart_evaluations: _Optional[_Iterable[_Union[_scorecards_pb2.SmartEvaluation, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class UpdateSmartEvaluationRequest(_message.Message):
    __slots__ = ("smart_evaluation", "update_mask")
    SMART_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    smart_evaluation: _scorecards_pb2.SmartEvaluation
    update_mask: _field_mask_pb2.FieldMask
    def __init__(self, smart_evaluation: _Optional[_Union[_scorecards_pb2.SmartEvaluation, _Mapping]] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateSmartEvaluationResponse(_message.Message):
    __slots__ = ("smart_evaluation",)
    SMART_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    smart_evaluation: _scorecards_pb2.SmartEvaluation
    def __init__(self, smart_evaluation: _Optional[_Union[_scorecards_pb2.SmartEvaluation, _Mapping]] = ...) -> None: ...

class DeleteSmartEvaluationRequest(_message.Message):
    __slots__ = ("smart_evaluation_id",)
    SMART_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    smart_evaluation_id: int
    def __init__(self, smart_evaluation_id: _Optional[int] = ...) -> None: ...

class DeleteSmartEvaluationResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSmartEvaluationRequest(_message.Message):
    __slots__ = ("smart_evaluation_id",)
    SMART_EVALUATION_ID_FIELD_NUMBER: _ClassVar[int]
    smart_evaluation_id: int
    def __init__(self, smart_evaluation_id: _Optional[int] = ...) -> None: ...

class GetSmartEvaluationResponse(_message.Message):
    __slots__ = ("smart_evaluation",)
    SMART_EVALUATION_FIELD_NUMBER: _ClassVar[int]
    smart_evaluation: _scorecards_pb2.SmartEvaluation
    def __init__(self, smart_evaluation: _Optional[_Union[_scorecards_pb2.SmartEvaluation, _Mapping]] = ...) -> None: ...
