from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Product(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCT_UNSPECIFIED: _ClassVar[Product]
    PRODUCT_AGENT_SEATS: _ClassVar[Product]
    PRODUCT_OMNI: _ClassVar[Product]
    PRODUCT_OMNI_CHAT_SENT: _ClassVar[Product]
    PRODUCT_OMNI_CHAT_RECEIVED: _ClassVar[Product]
    PRODUCT_OMNI_EMAILS_SENT: _ClassVar[Product]
    PRODUCT_OMNI_EMAILS_RECEIVED: _ClassVar[Product]
    PRODUCT_OMNI_SMS_SENT: _ClassVar[Product]
    PRODUCT_OMNI_SMS_RECEIVED: _ClassVar[Product]
    PRODUCT_COMPLIANCE: _ClassVar[Product]
PRODUCT_UNSPECIFIED: Product
PRODUCT_AGENT_SEATS: Product
PRODUCT_OMNI: Product
PRODUCT_OMNI_CHAT_SENT: Product
PRODUCT_OMNI_CHAT_RECEIVED: Product
PRODUCT_OMNI_EMAILS_SENT: Product
PRODUCT_OMNI_EMAILS_RECEIVED: Product
PRODUCT_OMNI_SMS_SENT: Product
PRODUCT_OMNI_SMS_RECEIVED: Product
PRODUCT_COMPLIANCE: Product
