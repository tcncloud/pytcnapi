from api.commons import scorecards_pb2 as _scorecards_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

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
    __slots__ = ()
    def __init__(self) -> None: ...

class ListSmartEvaluationsResponse(_message.Message):
    __slots__ = ("smart_evaluations",)
    SMART_EVALUATIONS_FIELD_NUMBER: _ClassVar[int]
    smart_evaluations: _containers.RepeatedCompositeFieldContainer[_scorecards_pb2.SmartEvaluation]
    def __init__(self, smart_evaluations: _Optional[_Iterable[_Union[_scorecards_pb2.SmartEvaluation, _Mapping]]] = ...) -> None: ...

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
