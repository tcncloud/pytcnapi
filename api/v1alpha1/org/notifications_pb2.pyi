from api.commons.audit import event_types_pb2 as _event_types_pb2
from api.commons import notifications_pb2 as _notifications_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserSubscription(_message.Message):
    __slots__ = ("subscription_id", "event_type", "user_id", "room303", "delivery", "filters", "version")
    class Room303(_message.Message):
        __slots__ = ("room_name",)
        ROOM_NAME_FIELD_NUMBER: _ClassVar[int]
        room_name: str
        def __init__(self, room_name: _Optional[str] = ...) -> None: ...
    class Delivery(_message.Message):
        __slots__ = ("transfer_config_name",)
        TRANSFER_CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
        transfer_config_name: str
        def __init__(self, transfer_config_name: _Optional[str] = ...) -> None: ...
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROOM303_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    event_type: _event_types_pb2.EventType
    user_id: str
    room303: UserSubscription.Room303
    delivery: UserSubscription.Delivery
    filters: _containers.RepeatedCompositeFieldContainer[_notifications_pb2.FieldValueFilter]
    version: int
    def __init__(self, subscription_id: _Optional[str] = ..., event_type: _Optional[_Union[_event_types_pb2.EventType, str]] = ..., user_id: _Optional[str] = ..., room303: _Optional[_Union[UserSubscription.Room303, _Mapping]] = ..., delivery: _Optional[_Union[UserSubscription.Delivery, _Mapping]] = ..., filters: _Optional[_Iterable[_Union[_notifications_pb2.FieldValueFilter, _Mapping]]] = ..., version: _Optional[int] = ...) -> None: ...

class AddUserSubscriptionRequest(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class AddUserSubscriptionResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class AddUserSubscriptionByUserIdRequest(_message.Message):
    __slots__ = ("user_id", "subscription")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    subscription: UserSubscription
    def __init__(self, user_id: _Optional[str] = ..., subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class AddUserSubscriptionByUserIdResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class GetUserSubscriptionRequest(_message.Message):
    __slots__ = ("subscription_id",)
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    def __init__(self, subscription_id: _Optional[str] = ...) -> None: ...

class GetUserSubscriptionResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class GetUserSubscriptionByUserIdRequest(_message.Message):
    __slots__ = ("user_id", "subscription_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    subscription_id: str
    def __init__(self, user_id: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class GetUserSubscriptionByUserIdResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class UpdateUserSubscriptionRequest(_message.Message):
    __slots__ = ("subscription", "field_mask")
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateUserSubscriptionResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class UpdateUserSubscriptionByUserIdRequest(_message.Message):
    __slots__ = ("subscription", "field_mask")
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    field_mask: _field_mask_pb2.FieldMask
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateUserSubscriptionByUserIdResponse(_message.Message):
    __slots__ = ("subscription",)
    SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    subscription: UserSubscription
    def __init__(self, subscription: _Optional[_Union[UserSubscription, _Mapping]] = ...) -> None: ...

class RemoveUserSubscriptionRequest(_message.Message):
    __slots__ = ("subscription_id",)
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    subscription_id: str
    def __init__(self, subscription_id: _Optional[str] = ...) -> None: ...

class RemoveUserSubscriptionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveUserSubscriptionByUserIdRequest(_message.Message):
    __slots__ = ("user_id", "subscription_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    subscription_id: str
    def __init__(self, user_id: _Optional[str] = ..., subscription_id: _Optional[str] = ...) -> None: ...

class RemoveUserSubscriptionByUserIdResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListUserSubscriptionsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListUserSubscriptionsResponse(_message.Message):
    __slots__ = ("subscriptions",)
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[UserSubscription]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[UserSubscription, _Mapping]]] = ...) -> None: ...

class ListUserSubscriptionsByUserIdRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class ListUserSubscriptionsByUserIdResponse(_message.Message):
    __slots__ = ("subscriptions",)
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[UserSubscription]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[UserSubscription, _Mapping]]] = ...) -> None: ...

class ListOrgSubscriptionsRequest(_message.Message):
    __slots__ = ("org_id", "event_type")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    event_type: _event_types_pb2.EventType
    def __init__(self, org_id: _Optional[str] = ..., event_type: _Optional[_Union[_event_types_pb2.EventType, str]] = ...) -> None: ...

class ListOrgSubscriptionsResponse(_message.Message):
    __slots__ = ("subscriptions",)
    SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    subscriptions: _containers.RepeatedCompositeFieldContainer[UserSubscription]
    def __init__(self, subscriptions: _Optional[_Iterable[_Union[UserSubscription, _Mapping]]] = ...) -> None: ...
