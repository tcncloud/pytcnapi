from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InterruptedPeeringStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    InterruptPeeringStatus_MANUAL: _ClassVar[InterruptedPeeringStatus]
    InterruptPeeringStatus_PREVIEW: _ClassVar[InterruptedPeeringStatus]

class RecalculateBillingMonth(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RECALCULATE_BILLING_MONTH_CURRENT: _ClassVar[RecalculateBillingMonth]
    RECALCULATE_BILLING_MONTH_PREVIOUS: _ClassVar[RecalculateBillingMonth]

class RecalculateBillingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    RECALCULATE_BILLING_TYPE_OUTBOUND_CALLS: _ClassVar[RecalculateBillingType]
    RECALCULATE_BILLING_TYPE_INBOUND_CALLS: _ClassVar[RecalculateBillingType]
    RECALCULATE_BILLING_TYPE_AGENTS: _ClassVar[RecalculateBillingType]
    RECALCULATE_BILLING_TYPE_SMS: _ClassVar[RecalculateBillingType]
    RECALCULATE_BILLING_TYPE_EMAIL: _ClassVar[RecalculateBillingType]
    RECALCULATE_BILLING_TYPE_MANUAL_DIAL_CALLS: _ClassVar[RecalculateBillingType]

class PhoneBookSIPType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PHONE_BOOK_SIP_TYPE_OUTBOUND: _ClassVar[PhoneBookSIPType]
    PHONE_BOOK_SIP_TYPE_TRANSFER: _ClassVar[PhoneBookSIPType]

class PhoneBookPhoneNumberType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    PHONE_BOOK_PHONE_NUMBER_TYPE_CALLER_ID: _ClassVar[PhoneBookPhoneNumberType]
    PHONE_BOOK_PHONE_NUMBER_TYPE_OUTBOUND: _ClassVar[PhoneBookPhoneNumberType]
    PHONE_BOOK_PHONE_NUMBER_TYPE_TRANSFER: _ClassVar[PhoneBookPhoneNumberType]
InterruptPeeringStatus_MANUAL: InterruptedPeeringStatus
InterruptPeeringStatus_PREVIEW: InterruptedPeeringStatus
RECALCULATE_BILLING_MONTH_CURRENT: RecalculateBillingMonth
RECALCULATE_BILLING_MONTH_PREVIOUS: RecalculateBillingMonth
RECALCULATE_BILLING_TYPE_OUTBOUND_CALLS: RecalculateBillingType
RECALCULATE_BILLING_TYPE_INBOUND_CALLS: RecalculateBillingType
RECALCULATE_BILLING_TYPE_AGENTS: RecalculateBillingType
RECALCULATE_BILLING_TYPE_SMS: RecalculateBillingType
RECALCULATE_BILLING_TYPE_EMAIL: RecalculateBillingType
RECALCULATE_BILLING_TYPE_MANUAL_DIAL_CALLS: RecalculateBillingType
PHONE_BOOK_SIP_TYPE_OUTBOUND: PhoneBookSIPType
PHONE_BOOK_SIP_TYPE_TRANSFER: PhoneBookSIPType
PHONE_BOOK_PHONE_NUMBER_TYPE_CALLER_ID: PhoneBookPhoneNumberType
PHONE_BOOK_PHONE_NUMBER_TYPE_OUTBOUND: PhoneBookPhoneNumberType
PHONE_BOOK_PHONE_NUMBER_TYPE_TRANSFER: PhoneBookPhoneNumberType

class ClientInfoDataRow(_message.Message):
    __slots__ = ["field_label", "field_value", "is_phone", "dialed_number", "contact_field_description_sid"]
    FIELD_LABEL_FIELD_NUMBER: _ClassVar[int]
    FIELD_VALUE_FIELD_NUMBER: _ClassVar[int]
    IS_PHONE_FIELD_NUMBER: _ClassVar[int]
    DIALED_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_DESCRIPTION_SID_FIELD_NUMBER: _ClassVar[int]
    field_label: str
    field_value: str
    is_phone: bool
    dialed_number: bool
    contact_field_description_sid: int
    def __init__(self, field_label: _Optional[str] = ..., field_value: _Optional[str] = ..., is_phone: bool = ..., dialed_number: bool = ..., contact_field_description_sid: _Optional[int] = ...) -> None: ...

class RGBColor(_message.Message):
    __slots__ = ["red", "green", "blue"]
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    red: int
    green: int
    blue: int
    def __init__(self, red: _Optional[int] = ..., green: _Optional[int] = ..., blue: _Optional[int] = ...) -> None: ...

class DialedNumberFieldSettings(_message.Message):
    __slots__ = ["should_display", "color", "bg_color", "allow_agent_copy"]
    SHOULD_DISPLAY_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    BG_COLOR_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AGENT_COPY_FIELD_NUMBER: _ClassVar[int]
    should_display: bool
    color: RGBColor
    bg_color: RGBColor
    allow_agent_copy: bool
    def __init__(self, should_display: bool = ..., color: _Optional[_Union[RGBColor, _Mapping]] = ..., bg_color: _Optional[_Union[RGBColor, _Mapping]] = ..., allow_agent_copy: bool = ...) -> None: ...

class ClientInfoDisplayTemplateRow(_message.Message):
    __slots__ = ["field_label", "color", "bg_color", "contact_field_description_sid", "allow_agent_copy"]
    FIELD_LABEL_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    BG_COLOR_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_DESCRIPTION_SID_FIELD_NUMBER: _ClassVar[int]
    ALLOW_AGENT_COPY_FIELD_NUMBER: _ClassVar[int]
    field_label: str
    color: RGBColor
    bg_color: RGBColor
    contact_field_description_sid: int
    allow_agent_copy: bool
    def __init__(self, field_label: _Optional[str] = ..., color: _Optional[_Union[RGBColor, _Mapping]] = ..., bg_color: _Optional[_Union[RGBColor, _Mapping]] = ..., contact_field_description_sid: _Optional[int] = ..., allow_agent_copy: bool = ...) -> None: ...

class CallHistorySearchType(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        STANDARD: _ClassVar[CallHistorySearchType.Enum]
        BY_ID: _ClassVar[CallHistorySearchType.Enum]
        BY_AGENT: _ClassVar[CallHistorySearchType.Enum]
    STANDARD: CallHistorySearchType.Enum
    BY_ID: CallHistorySearchType.Enum
    BY_AGENT: CallHistorySearchType.Enum
    def __init__(self) -> None: ...

class CallHistorySearchScope(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        ALL: _ClassVar[CallHistorySearchScope.Enum]
        TWENTY_FOUR_HOURS: _ClassVar[CallHistorySearchScope.Enum]
        TWO_DAYS: _ClassVar[CallHistorySearchScope.Enum]
        THREE_DAYS: _ClassVar[CallHistorySearchScope.Enum]
        FIVE_DAYS: _ClassVar[CallHistorySearchScope.Enum]
        SEVEN_DAYS: _ClassVar[CallHistorySearchScope.Enum]
        THIRTY_DAYS: _ClassVar[CallHistorySearchScope.Enum]
        SIXTY_DAYS: _ClassVar[CallHistorySearchScope.Enum]
        NINETY_DAYS: _ClassVar[CallHistorySearchScope.Enum]
        ONEHUNDRED_TWENTY_DAYS: _ClassVar[CallHistorySearchScope.Enum]
        ONEHUNDRED_FIFTY_DAYS: _ClassVar[CallHistorySearchScope.Enum]
        ONEHUNDRED_EIGHTY_DAYS: _ClassVar[CallHistorySearchScope.Enum]
    ALL: CallHistorySearchScope.Enum
    TWENTY_FOUR_HOURS: CallHistorySearchScope.Enum
    TWO_DAYS: CallHistorySearchScope.Enum
    THREE_DAYS: CallHistorySearchScope.Enum
    FIVE_DAYS: CallHistorySearchScope.Enum
    SEVEN_DAYS: CallHistorySearchScope.Enum
    THIRTY_DAYS: CallHistorySearchScope.Enum
    SIXTY_DAYS: CallHistorySearchScope.Enum
    NINETY_DAYS: CallHistorySearchScope.Enum
    ONEHUNDRED_TWENTY_DAYS: CallHistorySearchScope.Enum
    ONEHUNDRED_FIFTY_DAYS: CallHistorySearchScope.Enum
    ONEHUNDRED_EIGHTY_DAYS: CallHistorySearchScope.Enum
    def __init__(self) -> None: ...

class ListPhoneBookOrderBy(_message.Message):
    __slots__ = []
    class Enum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        PHONE_BOOK_SID: _ClassVar[ListPhoneBookOrderBy.Enum]
        ENTRY_TYPE: _ClassVar[ListPhoneBookOrderBy.Enum]
        ENTRY_NAME: _ClassVar[ListPhoneBookOrderBy.Enum]
        CLIENT_SID: _ClassVar[ListPhoneBookOrderBy.Enum]
        HUNT_GROUP_SID: _ClassVar[ListPhoneBookOrderBy.Enum]
        PHONE_NUMBER: _ClassVar[ListPhoneBookOrderBy.Enum]
        PHONE_NUMBER_TYPE: _ClassVar[ListPhoneBookOrderBy.Enum]
        PHONE_NUMBER_HIDDEN: _ClassVar[ListPhoneBookOrderBy.Enum]
    PHONE_BOOK_SID: ListPhoneBookOrderBy.Enum
    ENTRY_TYPE: ListPhoneBookOrderBy.Enum
    ENTRY_NAME: ListPhoneBookOrderBy.Enum
    CLIENT_SID: ListPhoneBookOrderBy.Enum
    HUNT_GROUP_SID: ListPhoneBookOrderBy.Enum
    PHONE_NUMBER: ListPhoneBookOrderBy.Enum
    PHONE_NUMBER_TYPE: ListPhoneBookOrderBy.Enum
    PHONE_NUMBER_HIDDEN: ListPhoneBookOrderBy.Enum
    def __init__(self) -> None: ...
