from services.billing.entities.v1alpha4 import modules_pb2 as _modules_pb2
from services.billing.entities.v1alpha4 import omni_pb2 as _omni_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProductConfig(_message.Message):
    __slots__ = ("communications_omni_chat_agent_message_unit", "communications_omni_chat_agent_attachment", "communications_omni_chat_agent_accumulated_attachments", "communications_omni_chat_customer_message_unit", "communications_omni_chat_customer_attachment", "communications_omni_chat_customer_accumulated_attachments", "communications_omni_chat_manager_message_unit", "communications_omni_chat_manager_attachment", "communications_omni_chat_manager_accumulated_attachments", "communications_omni_chat_system_message_unit", "communications_omni_chat_system_attachment", "communications_omni_chat_system_accumulated_attachments", "communications_omni_email_agent_message_unit", "communications_omni_email_agent_size", "communications_omni_email_agent_accumulated_size", "communications_omni_email_customer_message_unit", "communications_omni_email_customer_size", "communications_omni_email_customer_accumulated_size", "communications_omni_email_manager_message_unit", "communications_omni_email_manager_size", "communications_omni_email_manager_accumulated_size", "communications_omni_email_system_message_unit", "communications_omni_email_system_size", "communications_omni_email_system_accumulated_size", "communications_omni_sms_agent_message_unit", "communications_omni_sms_agent_attachment", "communications_omni_sms_agent_accumulated_attachments", "communications_omni_sms_customer_message_unit", "communications_omni_sms_customer_attachment", "communications_omni_sms_customer_accumulated_attachments", "communications_omni_sms_manager_message_unit", "communications_omni_sms_manager_attachment", "communications_omni_sms_manager_accumulated_attachments", "communications_omni_sms_system_message_unit", "communications_omni_sms_system_attachment", "communications_omni_sms_system_accumulated_attachments", "communications_omni_agent_seats", "communications_omni_resources_connected_inbox_poll", "communications_omni_resources_connected_inbox_created", "data_management_compliance_compliance_rnd_query", "data_management_compliance_compliance_rnd_query_cached", "workforce_engagement_workforce_optimization_voice_analytics_call_transcripts", "workforce_engagement_workforce_optimization_voice_analytics_accumulated_call_transcripts")
    COMMUNICATIONS_OMNI_CHAT_AGENT_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_AGENT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_AGENT_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_CUSTOMER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_CUSTOMER_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_CUSTOMER_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_MANAGER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_MANAGER_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_MANAGER_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_SYSTEM_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_SYSTEM_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_CHAT_SYSTEM_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_AGENT_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_AGENT_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_AGENT_ACCUMULATED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_CUSTOMER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_CUSTOMER_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_CUSTOMER_ACCUMULATED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_MANAGER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_MANAGER_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_MANAGER_ACCUMULATED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_SYSTEM_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_SYSTEM_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_EMAIL_SYSTEM_ACCUMULATED_SIZE_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_AGENT_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_AGENT_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_AGENT_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_CUSTOMER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_CUSTOMER_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_CUSTOMER_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_MANAGER_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_MANAGER_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_MANAGER_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_SYSTEM_MESSAGE_UNIT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_SYSTEM_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_SMS_SYSTEM_ACCUMULATED_ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_AGENT_SEATS_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_RESOURCES_CONNECTED_INBOX_POLL_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_OMNI_RESOURCES_CONNECTED_INBOX_CREATED_FIELD_NUMBER: _ClassVar[int]
    DATA_MANAGEMENT_COMPLIANCE_COMPLIANCE_RND_QUERY_FIELD_NUMBER: _ClassVar[int]
    DATA_MANAGEMENT_COMPLIANCE_COMPLIANCE_RND_QUERY_CACHED_FIELD_NUMBER: _ClassVar[int]
    WORKFORCE_ENGAGEMENT_WORKFORCE_OPTIMIZATION_VOICE_ANALYTICS_CALL_TRANSCRIPTS_FIELD_NUMBER: _ClassVar[int]
    WORKFORCE_ENGAGEMENT_WORKFORCE_OPTIMIZATION_VOICE_ANALYTICS_ACCUMULATED_CALL_TRANSCRIPTS_FIELD_NUMBER: _ClassVar[int]
    communications_omni_chat_agent_message_unit: _modules_pb2.BasicConfig
    communications_omni_chat_agent_attachment: _modules_pb2.BasicUnitConfig
    communications_omni_chat_agent_accumulated_attachments: _modules_pb2.BasicUnitConfig
    communications_omni_chat_customer_message_unit: _modules_pb2.BasicConfig
    communications_omni_chat_customer_attachment: _modules_pb2.BasicUnitConfig
    communications_omni_chat_customer_accumulated_attachments: _modules_pb2.BasicUnitConfig
    communications_omni_chat_manager_message_unit: _modules_pb2.BasicConfig
    communications_omni_chat_manager_attachment: _modules_pb2.BasicUnitConfig
    communications_omni_chat_manager_accumulated_attachments: _modules_pb2.BasicUnitConfig
    communications_omni_chat_system_message_unit: _modules_pb2.BasicConfig
    communications_omni_chat_system_attachment: _modules_pb2.BasicUnitConfig
    communications_omni_chat_system_accumulated_attachments: _modules_pb2.BasicUnitConfig
    communications_omni_email_agent_message_unit: _modules_pb2.BasicConfig
    communications_omni_email_agent_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_agent_accumulated_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_customer_message_unit: _modules_pb2.BasicConfig
    communications_omni_email_customer_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_customer_accumulated_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_manager_message_unit: _modules_pb2.BasicConfig
    communications_omni_email_manager_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_manager_accumulated_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_system_message_unit: _modules_pb2.BasicConfig
    communications_omni_email_system_size: _modules_pb2.BasicUnitConfig
    communications_omni_email_system_accumulated_size: _modules_pb2.BasicUnitConfig
    communications_omni_sms_agent_message_unit: _omni_pb2.OmniSmsConfig
    communications_omni_sms_agent_attachment: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_agent_accumulated_attachments: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_customer_message_unit: _omni_pb2.OmniSmsConfig
    communications_omni_sms_customer_attachment: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_customer_accumulated_attachments: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_manager_message_unit: _omni_pb2.OmniSmsConfig
    communications_omni_sms_manager_attachment: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_manager_accumulated_attachments: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_system_message_unit: _omni_pb2.OmniSmsConfig
    communications_omni_sms_system_attachment: _omni_pb2.OmniSmsUnitConfig
    communications_omni_sms_system_accumulated_attachments: _omni_pb2.OmniSmsUnitConfig
    communications_omni_agent_seats: _modules_pb2.BasicConfig
    communications_omni_resources_connected_inbox_poll: _modules_pb2.BasicConfig
    communications_omni_resources_connected_inbox_created: _modules_pb2.BasicConfig
    data_management_compliance_compliance_rnd_query: _modules_pb2.BasicConfig
    data_management_compliance_compliance_rnd_query_cached: _modules_pb2.BasicConfig
    workforce_engagement_workforce_optimization_voice_analytics_call_transcripts: _modules_pb2.BasicConfig
    workforce_engagement_workforce_optimization_voice_analytics_accumulated_call_transcripts: _modules_pb2.BasicConfig
    def __init__(self, communications_omni_chat_agent_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_chat_agent_attachment: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_agent_accumulated_attachments: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_customer_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_chat_customer_attachment: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_customer_accumulated_attachments: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_manager_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_chat_manager_attachment: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_manager_accumulated_attachments: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_system_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_chat_system_attachment: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_chat_system_accumulated_attachments: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_agent_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_email_agent_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_agent_accumulated_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_customer_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_email_customer_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_customer_accumulated_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_manager_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_email_manager_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_manager_accumulated_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_system_message_unit: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_email_system_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_email_system_accumulated_size: _Optional[_Union[_modules_pb2.BasicUnitConfig, _Mapping]] = ..., communications_omni_sms_agent_message_unit: _Optional[_Union[_omni_pb2.OmniSmsConfig, _Mapping]] = ..., communications_omni_sms_agent_attachment: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_agent_accumulated_attachments: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_customer_message_unit: _Optional[_Union[_omni_pb2.OmniSmsConfig, _Mapping]] = ..., communications_omni_sms_customer_attachment: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_customer_accumulated_attachments: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_manager_message_unit: _Optional[_Union[_omni_pb2.OmniSmsConfig, _Mapping]] = ..., communications_omni_sms_manager_attachment: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_manager_accumulated_attachments: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_system_message_unit: _Optional[_Union[_omni_pb2.OmniSmsConfig, _Mapping]] = ..., communications_omni_sms_system_attachment: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_sms_system_accumulated_attachments: _Optional[_Union[_omni_pb2.OmniSmsUnitConfig, _Mapping]] = ..., communications_omni_agent_seats: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_resources_connected_inbox_poll: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., communications_omni_resources_connected_inbox_created: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., data_management_compliance_compliance_rnd_query: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., data_management_compliance_compliance_rnd_query_cached: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., workforce_engagement_workforce_optimization_voice_analytics_call_transcripts: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ..., workforce_engagement_workforce_optimization_voice_analytics_accumulated_call_transcripts: _Optional[_Union[_modules_pb2.BasicConfig, _Mapping]] = ...) -> None: ...
