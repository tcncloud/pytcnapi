from api.commons.audit import event_types_pb2 as _event_types_pb2
from api.commons.billing.modules import modules_pb2 as _modules_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetailConfigType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DETAIL_CONFIG_TYPE_UNSPECIFIED: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_NOOP: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_AGENT_SEATS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_MESSAGE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_MESSAGE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CONNECTED_INBOX_POLL: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_MESSAGE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_MESSAGE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CONNECTED_INBOX_CREATED: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS_SIZE: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_AGENT_CHAT_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_AGENT_EMAIL_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_AGENT_SMS_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_MANAGER_CHAT_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_MANAGER_EMAIL_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_MANAGER_SMS_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CUSTOMER_CHAT_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CUSTOMER_EMAIL_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_CUSTOMER_SMS_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_SYSTEM_CHAT_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_SYSTEM_EMAIL_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    DETAIL_CONFIG_TYPE_SYSTEM_SMS_MESSAGE_UNITS: _ClassVar[DetailConfigType]
    BillingDetailConfigType_COMPLIANCE_RND_QUERY: _ClassVar[DetailConfigType]
    BillingDetailConfigType_COMPLIANCE_RND_QUERY_CACHED: _ClassVar[DetailConfigType]
DETAIL_CONFIG_TYPE_UNSPECIFIED: DetailConfigType
DETAIL_CONFIG_TYPE_NOOP: DetailConfigType
DETAIL_CONFIG_TYPE_AGENT_SEATS: DetailConfigType
DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT: DetailConfigType
DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_MESSAGE: DetailConfigType
DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_EMAIL_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS: DetailConfigType
DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_MESSAGE: DetailConfigType
DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_EMAIL_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS: DetailConfigType
DETAIL_CONFIG_TYPE_CONNECTED_INBOX_POLL: DetailConfigType
DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT: DetailConfigType
DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_MESSAGE: DetailConfigType
DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_EMAIL_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS: DetailConfigType
DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT: DetailConfigType
DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_MESSAGE: DetailConfigType
DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_EMAIL_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS: DetailConfigType
DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_CHAT_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_CHAT_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_CHAT_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_CONNECTED_INBOX_CREATED: DetailConfigType
DETAIL_CONFIG_TYPE_AGENT_TEXT_MESSAGE_SMS_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_MANAGER_TEXT_MESSAGE_SMS_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_CUSTOMER_TEXT_MESSAGE_SMS_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_TASK_MESSAGE_SENT_SMS_SIZE: DetailConfigType
DETAIL_CONFIG_TYPE_AGENT_CHAT_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_AGENT_EMAIL_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_AGENT_SMS_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_MANAGER_CHAT_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_MANAGER_EMAIL_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_MANAGER_SMS_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_CUSTOMER_CHAT_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_CUSTOMER_EMAIL_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_CUSTOMER_SMS_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_SYSTEM_CHAT_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_SYSTEM_EMAIL_MESSAGE_UNITS: DetailConfigType
DETAIL_CONFIG_TYPE_SYSTEM_SMS_MESSAGE_UNITS: DetailConfigType
BillingDetailConfigType_COMPLIANCE_RND_QUERY: DetailConfigType
BillingDetailConfigType_COMPLIANCE_RND_QUERY_CACHED: DetailConfigType

class Plan(_message.Message):
    __slots__ = ["details"]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[Detail]
    def __init__(self, details: _Optional[_Iterable[_Union[Detail, _Mapping]]] = ...) -> None: ...

class Detail(_message.Message):
    __slots__ = ["billing_detail_sid", "event_type", "config_type", "config", "date_created", "date_modified", "deleted_on"]
    BILLING_DETAIL_SID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    DATE_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATE_MODIFIED_FIELD_NUMBER: _ClassVar[int]
    DELETED_ON_FIELD_NUMBER: _ClassVar[int]
    billing_detail_sid: int
    event_type: _event_types_pb2.EventType
    config_type: DetailConfigType
    config: DetailConfig
    date_created: _timestamp_pb2.Timestamp
    date_modified: _timestamp_pb2.Timestamp
    deleted_on: _timestamp_pb2.Timestamp
    def __init__(self, billing_detail_sid: _Optional[int] = ..., event_type: _Optional[_Union[_event_types_pb2.EventType, str]] = ..., config_type: _Optional[_Union[DetailConfigType, str]] = ..., config: _Optional[_Union[DetailConfig, _Mapping]] = ..., date_created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., date_modified: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., deleted_on: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DetailConfig(_message.Message):
    __slots__ = ["agent_seats_config", "agent_text_message_chat_config", "agent_text_message_email_message_config", "agent_text_message_email_size_config", "agent_text_message_sms_config", "task_message_sent_email_message_config", "task_message_sent_email_size_config", "task_message_sent_sms_config", "connected_inbox_poll_config", "manager_text_message_chat_config", "manager_text_message_email_message_config", "manager_text_message_email_size_config", "manager_text_message_sms_config", "customer_text_message_chat_config", "customer_text_message_email_message_config", "customer_text_message_email_size_config", "customer_text_message_sms_config", "agent_text_message_chat_size_config", "manager_text_message_chat_size_config", "customer_text_message_chat_size_config", "connected_inbox_created_config", "agent_text_message_sms_size_config", "manager_text_message_sms_size_config", "customer_text_message_sms_size_config", "task_message_sent_sms_size_config", "agent_chat_message_units_config", "agent_email_message_units_config", "agent_sms_message_units_config", "manager_chat_message_units_config", "manager_email_message_units_config", "manager_sms_message_units_config", "customer_chat_message_units_config", "customer_email_message_units_config", "customer_sms_message_units_config", "system_chat_message_units_config", "system_email_message_units_config", "system_sms_message_units_config", "compliance_rnd_query_config", "compliance_rnd_query_cached_config"]
    AGENT_SEATS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_CHAT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_EMAIL_MESSAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_EMAIL_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_SMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_MESSAGE_SENT_EMAIL_MESSAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_MESSAGE_SENT_EMAIL_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_MESSAGE_SENT_SMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_INBOX_POLL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_CHAT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_EMAIL_MESSAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_EMAIL_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_SMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_CHAT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_EMAIL_MESSAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_EMAIL_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_SMS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_CHAT_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_CHAT_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_CHAT_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_INBOX_CREATED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_TEXT_MESSAGE_SMS_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_TEXT_MESSAGE_SMS_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_TEXT_MESSAGE_SMS_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_MESSAGE_SENT_SMS_SIZE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_CHAT_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_EMAIL_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AGENT_SMS_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_CHAT_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_EMAIL_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    MANAGER_SMS_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_CHAT_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_EMAIL_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_SMS_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_CHAT_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_EMAIL_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_SMS_MESSAGE_UNITS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RND_QUERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COMPLIANCE_RND_QUERY_CACHED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    agent_seats_config: _modules_pb2.BasicConfig
    agent_text_message_chat_config: _modules_pb2.BasicConfig
    agent_text_message_email_message_config: _modules_pb2.BasicConfig
    agent_text_message_email_size_config: _modules_pb2.BasicAmountConfig
    agent_text_message_sms_config: _modules_pb2.BasicConfig
    task_message_sent_email_message_config: _modules_pb2.BasicConfig
    task_message_sent_email_size_config: _modules_pb2.BasicAmountConfig
    task_message_sent_sms_config: _modules_pb2.BasicConfig
    connected_inbox_poll_config: _modules_pb2.BasicConfig
    manager_text_message_chat_config: _modules_pb2.BasicConfig
    manager_text_message_email_message_config: _modules_pb2.BasicConfig
    manager_text_message_email_size_config: _modules_pb2.BasicAmountConfig
    manager_text_message_sms_config: _modules_pb2.BasicConfig
    customer_text_message_chat_config: _modules_pb2.BasicConfig
    customer_text_message_email_message_config: _modules_pb2.BasicConfig
    customer_text_message_email_size_config: _modules_pb2.BasicAmountConfig
    customer_text_message_sms_config: _modules_pb2.BasicConfig
    agent_text_message_chat_size_config: _modules_pb2.BasicAmountConfig
    manager_text_message_chat_size_config: _modules_pb2.BasicAmountConfig
    customer_text_message_chat_size_config: _modules_pb2.BasicAmountConfig
    connected_inbox_created_config: _modules_pb2.BasicConfig
    agent_text_message_sms_size_config: _modules_pb2.BasicAmountConfig
    manager_text_message_sms_size_config: _modules_pb2.BasicAmountConfig
    customer_text_message_sms_size_config: _modules_pb2.BasicAmountConfig
    task_message_sent_sms_size_config: _modules_pb2.BasicAmountConfig
    agent_chat_message_units_config: _modules_pb2.BasicConfig
    agent_email_message_units_config: _modules_pb2.BasicConfig
    agent_sms_message_units_config: _modules_pb2.BasicConfig
    manager_chat_message_units_config: _modules_pb2.BasicConfig
    manager_email_message_units_config: _modules_pb2.BasicConfig
    manager_sms_message_units_config: _modules_pb2.BasicConfig
    customer_chat_message_units_config: _modules_pb2.BasicConfig
    customer_email_message_units_config: _modules_pb2.BasicConfig
    customer_sms_message_units_config: _modules_pb2.BasicConfig
    system_chat_message_units_config: _modules_pb2.BasicConfig
    system_email_message_units_config: _modules_pb2.BasicConfig
    system_sms_message_units_config: _modules_pb2.BasicConfig
    compliance_rnd_query_config: _modules_pb2.BasicConfig
    compliance_rnd_query_cached_config: _modules_pb2.BasicConfig
    def __init__(self, agent_seats_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_text_message_chat_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_text_message_email_message_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_text_message_email_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., agent_text_message_sms_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., task_message_sent_email_message_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., task_message_sent_email_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., task_message_sent_sms_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., connected_inbox_poll_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_text_message_chat_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_text_message_email_message_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_text_message_email_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., manager_text_message_sms_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_text_message_chat_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_text_message_email_message_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_text_message_email_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., customer_text_message_sms_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_text_message_chat_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., manager_text_message_chat_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., customer_text_message_chat_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., connected_inbox_created_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_text_message_sms_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., manager_text_message_sms_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., customer_text_message_sms_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., task_message_sent_sms_size_config: _Optional[_Union[_modules_pb2.BasicAmountConfig, _Mapping]] = ..., agent_chat_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_email_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., agent_sms_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_chat_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_email_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., manager_sms_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_chat_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_email_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., customer_sms_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_chat_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_email_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., system_sms_message_units_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., compliance_rnd_query_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., compliance_rnd_query_cached_config: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ...) -> None: ...
