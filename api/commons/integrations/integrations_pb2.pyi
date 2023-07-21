from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IntegrationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    INTEGRATION_TYPE_UNKNOWN: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_BRAINTREE: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_RELATIENT: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_CYBERSOURCE: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_CIRCPRO: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_AUTHORIZENET: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_EXPITRANS: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_AXIAMEDFUSION: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_INSTAMED: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_USAEPAY: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_EZIDEBIT: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_BAMBORA: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_REPAY: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_AXIA: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_SECURETRADING: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_PAYMENTVISION: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_INTERPROSE: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_DALLASNEWS: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_PAYWAY: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_BILLINGTREE: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_EXPERIAN: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_NEWSCYCLE: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_TRUSTCOMMERCE: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_VANTIV: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_JOURNEY: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_ATHENAHEALTH: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_BRAINWORKS: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_OSGCONNECT: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_NTVB: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_ELAVON: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_GLOBALPAYMENTS: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_PAY_SCOUT: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_I2C: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_OPAYO: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_SHIFT4: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_POSCORP: _ClassVar[IntegrationType]
    INTEGRATION_TYPE_PIANO: _ClassVar[IntegrationType]

class RequestMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REQUEST_METHOD_UNKNOWN: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINTREE_CREDITSALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINTREE_BANKSALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_RELATIENT_GETPATIENTBALANCE: _ClassVar[RequestMethod]
    REQUEST_METHOD_RELATIENT_GETPATIENTCCTOKENS: _ClassVar[RequestMethod]
    REQUEST_METHOD_RELATIENT_POSTPATIENTTOKEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_RELATIENT_POSTPATIENTBALANCE: _ClassVar[RequestMethod]
    REQUEST_METHOD_RELATIENT_GETPATIENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_RELATIENT_POSTBALANCEBYID: _ClassVar[RequestMethod]
    REQUEST_METHOD_RELATIENT_CREATE_FORTIS_ACHTOKEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_RELATIENT_CREATE_FORTIS_CCTOKEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_RELATIENT_FORTIS_TOKEN_ACH_DEBIT_PAYMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_RELATIENT_FORTIS_TOKEN_CC_PAYMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_CYBERSOURCE_CREDITPAYMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_CYBERSOURCE_ECHECKPAYMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_PHONELOOKUPWITHBUNDLE: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_PHONELOOKUP: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_VACATIONRESTARTINQUIRY: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_COMPLAINTINQUIRY: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_ACCOUNTINQUIRY: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_ACCOUNTINQUIRYWITHTAX: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_ACCOUNTINQUIRYWITHTAXBUNDLE: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_COMPLAINTCODES: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_COMPLAINTUPDATE: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_VACATIONUPDATE: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_RESTARTUPDATE: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_LAW_IMMEDIATEPAYMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_LAW_UPDATEDATAWITHPAC: _ClassVar[RequestMethod]
    REQUEST_METHOD_CIRCPRO_LAW_GETCUSTOMERS: _ClassVar[RequestMethod]
    REQUEST_METHOD_AUTHORIZENET_CHARGECREDITCARD: _ClassVar[RequestMethod]
    REQUEST_METHOD_AUTHORIZENET_DEBITBANKACCOUNT: _ClassVar[RequestMethod]
    REQUEST_METHOD_AUTHORIZENET_CREATECUSTOMERPAYMENTPROFILE: _ClassVar[RequestMethod]
    REQUEST_METHOD_AUTHORIZENET_PAYPALTRANSACTION: _ClassVar[RequestMethod]
    REQUEST_METHOD_AUTHORIZENET_GOOGLEPAYTRANSACTION: _ClassVar[RequestMethod]
    REQUEST_METHOD_AUTHORIZENET_APPLEPAYTRANSACTION: _ClassVar[RequestMethod]
    REQUEST_METHOD_AUTHORIZENET_PAYPALAUTHCAPTURE: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPITRANS_CCTRANSACTION: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPITRANS_ACHTRANSACTION: _ClassVar[RequestMethod]
    REQUEST_METHOD_AXIAMEDFUSION_CCTRANSACTION: _ClassVar[RequestMethod]
    REQUEST_METHOD_AXIAMEDFUSION_ACHTRANSACTION: _ClassVar[RequestMethod]
    REQUEST_METHOD_AXIAMEDFUSION_CARDVERIFY: _ClassVar[RequestMethod]
    REQUEST_METHOD_INSTAMED_PAYMENTSALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_INSTAMED_VOIDPAYMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_USAEPAY_SUBMITCCPAYMENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_USAEPAY_SUBMITACHPAYMENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_USAEPAY_GETCCTOKEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_EZIDEBIT_SUBMITCCPAYMENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_EZIDEBIT_SUBMITACHPAYMENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_BAMBORA_SUBMITCCPAYMENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_BAMBORA_SUBMITACHPAYMENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_REPAY_STORECARD: _ClassVar[RequestMethod]
    REQUEST_METHOD_REPAY_PAYMENTTOKEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_REPAY_ACHPAYMENTTOKEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_AXIA_SUBMITSALEREQUESTBYCC: _ClassVar[RequestMethod]
    REQUEST_METHOD_AXIA_SUBMITSALEREQUESTBYCHECK: _ClassVar[RequestMethod]
    REQUEST_METHOD_SECURETRADING_SENDPAYMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_PAYMENTVISION_SUBMITCARDSALEREQUESTBYCC: _ClassVar[RequestMethod]
    REQUEST_METHOD_PAYMENTVISION_SUBMITCARDSALEREQUESTBYACH: _ClassVar[RequestMethod]
    REQUEST_METHOD_INTERPROSE_LOOKUPACCOUNT: _ClassVar[RequestMethod]
    REQUEST_METHOD_INTERPROSE_SUBMITCARDSALEREQUESTBYCC: _ClassVar[RequestMethod]
    REQUEST_METHOD_INTERPROSE_SUBMITCARDSALEREQUESTBYACH: _ClassVar[RequestMethod]
    REQUEST_METHOD_INTERPROSE_LOOKUPPAYMENTID: _ClassVar[RequestMethod]
    REQUEST_METHOD_INTERPROSE_LOOKUPACCOUNTBYFORMID: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_SEARCHBYPHONE: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_SEARCHBYZIPSTREET: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_SEARCHBY: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_CREATEVACATION: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_GETVACATION: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_GETVACATIONDAYSBETWEEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_GETVACATIONWITHCUTOFF: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_DELETEVACATION: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_ADDCOMPLAINT: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_UPDATEPHONENUMBER: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_STOPACCOUNT: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_CCPAYMENTTOKEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_DALLASNEWS_ACHPAYMENTTOKEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_PAYWAY_SUBMITCARDSALEREQUEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_PAYWAY_CREATETOKENREQUEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_PAYWAY_SUBMITACHSALEREQUEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_BILLINGTREE_SUBMITCARDSALEREQUEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_CC_PAYMENT_REQUEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_CC_PAYMENTPLANREQUEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_BALANCEREQUEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_ACH_PAYMENT_REQUEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_ACH_PAYMENTPLANREQUEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_STELLA_CARD_ENTRY: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_STELLA_ECHECK: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_STELLA_CARD_DEVICE_TOKENIZATION: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_STELLA_TOKEN_PAYMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_STELLA_ACH_TOKENIZATION: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_STELLA_ADD_USA_EPAY_TOKEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_STELLA_PAYMENT_PLANS: _ClassVar[RequestMethod]
    REQUEST_METHOD_EXPERIAN_STELLA_AUTH: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_LOGIN: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_SEARCHPAGE: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_BILLINGINFO: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_SERVICEERRORINFO: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_SERVICEERRORTRANS: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_STOPINFO: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_STOPTRANS: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_RENEWINFO: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_AUTORENEWINFO: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_AUTOTRAN: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_PAYINFO: _ClassVar[RequestMethod]
    REQUEST_METHOD_NEWSCYCLE_PAYTRAN: _ClassVar[RequestMethod]
    REQUEST_METHOD_TRUSTCOMMERCE_CREDITSALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_TRUSTCOMMERCE_ACHSALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_VANTIV_CREDITSALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_VANTIV_ACHSALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_JOURNEY_LATEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_ATHENAHEALTH_GETPATIENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_ATHENAHEALTH_GETPATIENTSWITHID: _ClassVar[RequestMethod]
    REQUEST_METHOD_ATHENAHEALTH_CCPAYMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINWORKS_GETCUSTOMERSBYPHONE: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINWORKS_GETSUSPENDS: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINWORKS_GETCUSTOMERBYCUSTIDV2: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINWORKS_GETCOMPLAINTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINWORKS_GETCODESORTYPES: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINWORKS_STOPSUSPENDS: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINWORKS_STARTSUSPENDS: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINWORKS_SENDCOMPLAINT: _ClassVar[RequestMethod]
    REQUEST_METHOD_BRAINWORKS_GETCUSTOMERBYCUSTID: _ClassVar[RequestMethod]
    REQUEST_METHOD_OSGCONNECT_CCPAYMENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_OSGCONNECT_ACHPAYMENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_OSGCONNECT_VALIDATEACCOUNTNO: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_CREDIT_MISSED_DELIVERY: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_CUSTOMER_SEARCH: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_END_CALL: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_INTEGRATION_DEFINITION: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_MISSED_DELIVERY: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_REMOVE_AUTORENEWAL: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_RENEW_SUBSCRIPTION: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_RENEWAL_OFFERS: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_SET_AUTORENEWAL: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_START_INCOMING_CALL: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_START_OUTGOING_CALL: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_SUBSCRIPTION_INFO: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_VACATION_STOP: _ClassVar[RequestMethod]
    REQUEST_METHOD_NTVB_AUTHTEST: _ClassVar[RequestMethod]
    REQUEST_METHOD_ELAVON_CREDIT_CARD_SALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_ELAVON_ADD_RECURRING: _ClassVar[RequestMethod]
    REQUEST_METHOD_ELAVON_DCC_RESPONSE: _ClassVar[RequestMethod]
    REQUEST_METHOD_ELAVON_DELETE_RECURRING: _ClassVar[RequestMethod]
    REQUEST_METHOD_ELAVON_UPDATE_RECURRING: _ClassVar[RequestMethod]
    REQUEST_METHOD_ELAVON_HEALTH_CARE_CC_SALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_ELAVON_ADD_INSTALLMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_ELAVON_UPDATE_INSTALLMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_ELAVON_DELETE_INSTALLMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_ELAVON_MCC_CREDIT_CARD_SALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_GLOBALPAYMENTS_CARDSALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_GLOBALPAYMENTS_GET_TRANSACTION_BY_ID: _ClassVar[RequestMethod]
    REQUEST_METHOD_GLOBALPAYMENTS_LIST_TRANSACTIONS: _ClassVar[RequestMethod]
    REQUEST_METHOD_GLOBALPAYMENTS_REFUND_SALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_GLOBALPAYMENTS_REVERSE_SALE_OR_REFUND: _ClassVar[RequestMethod]
    REQUEST_METHOD_PAY_SCOUT_CREDIT_CARD_SALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_PAY_SCOUT_ECHECK_SALE: _ClassVar[RequestMethod]
    REQUEST_METHOD_I2C_ECHO: _ClassVar[RequestMethod]
    REQUEST_METHOD_I2C_BALANCE_INQUIRY: _ClassVar[RequestMethod]
    REQUEST_METHOD_I2C_VERIFY_USER: _ClassVar[RequestMethod]
    REQUEST_METHOD_I2C_SEARCH_CUSTOMER: _ClassVar[RequestMethod]
    REQUEST_METHOD_I2C_MAKE_PAYMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_I2C_GET_CARDHOLDER_PROFILE: _ClassVar[RequestMethod]
    REQUEST_METHOD_I2C_GET_CARDHOLDER_STATEMENT: _ClassVar[RequestMethod]
    REQUEST_METHOD_I2C_GET_CARDHOLDER_BALANCE: _ClassVar[RequestMethod]
    REQUEST_METHOD_I2C_GET_CREDITPAYMENT_INFO: _ClassVar[RequestMethod]
    REQUEST_METHOD_I2C_TRANSACTION_HISTORY: _ClassVar[RequestMethod]
    REQUEST_METHOD_OPAYO_CCPAYMENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_SHIFT4_CCPAYMENTS: _ClassVar[RequestMethod]
    REQUEST_METHOD_POSCORP_ACCESSTOKEN: _ClassVar[RequestMethod]
    REQUEST_METHOD_POSCORP_LOOKUP_GUARANTOR: _ClassVar[RequestMethod]
    REQUEST_METHOD_POSCORP_UPDATE_PAYMENT_STATUS: _ClassVar[RequestMethod]
    REQUEST_METHOD_PIANO_GET_USER: _ClassVar[RequestMethod]
    REQUEST_METHOD_PIANO_UPDATE_USER: _ClassVar[RequestMethod]

class TransactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TRANSACTION_TYPE_PAYMENT: _ClassVar[TransactionType]
    TRANSACTION_TYPE_DATA_INQUIRY: _ClassVar[TransactionType]
    TRANSACTION_TYPE_ACCOUNT_VERIFY: _ClassVar[TransactionType]

class RequestSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    REQUEST_SOURCE_IVR: _ClassVar[RequestSource]
    REQUEST_SOURCE_EMAIL: _ClassVar[RequestSource]
    REQUEST_SOURCE_WEB: _ClassVar[RequestSource]
    REQUEST_SOURCE_SMS: _ClassVar[RequestSource]
    REQUEST_SOURCE_CHAT: _ClassVar[RequestSource]
    REQUEST_SOURCE_LMS: _ClassVar[RequestSource]

class TransactionResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TRANSACTION_RESULT_SUCCESS: _ClassVar[TransactionResult]
    TRANSACTION_RESULT_FAILED: _ClassVar[TransactionResult]

class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    VALUE_TYPE_UNKNOWN: _ClassVar[ValueType]
    VALUE_TYPE_NUMBER: _ClassVar[ValueType]
    VALUE_TYPE_BOOL: _ClassVar[ValueType]
    VALUE_TYPE_MAP: _ClassVar[ValueType]
    VALUE_TYPE_ARRAY: _ClassVar[ValueType]
    VALUE_TYPE_INT: _ClassVar[ValueType]
    VALUE_TYPE_STRING: _ClassVar[ValueType]
    VALUE_TYPE_TIME: _ClassVar[ValueType]
    VALUE_TYPE_COMPOSITE_VAL: _ClassVar[ValueType]

class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    VISIBILITY_INVISIBLE: _ClassVar[Visibility]
    VISIBILITY_UNRESTRICTED: _ClassVar[Visibility]
    VISIBILITY_RUNTIME: _ClassVar[Visibility]
    VISIBILITY_BY_METHOD: _ClassVar[Visibility]
    VISIBILITY_PLUGIN: _ClassVar[Visibility]

class CompareOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    COMPARE_OPERATION_EQ: _ClassVar[CompareOperation]
    COMPARE_OPERATION_GT: _ClassVar[CompareOperation]
    COMPARE_OPERATION_LT: _ClassVar[CompareOperation]
    COMPARE_OPERATION_GE: _ClassVar[CompareOperation]
    COMPARE_OPERATION_LE: _ClassVar[CompareOperation]
    COMPARE_OPERATION_NE: _ClassVar[CompareOperation]

class FlowFieldLoc(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FFL_ANY: _ClassVar[FlowFieldLoc]
    FFL_LINK: _ClassVar[FlowFieldLoc]
    FFL_PLUGIN_INST: _ClassVar[FlowFieldLoc]
    FFL_SUBMIT: _ClassVar[FlowFieldLoc]

class Validation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    VALIDATION_NONE: _ClassVar[Validation]
    VALIDATION_CREDITCARD: _ClassVar[Validation]
    VALIDATION_CVC: _ClassVar[Validation]
    VALIDATION_MONTH_2_DIGIT: _ClassVar[Validation]
    VALIDATION_YEAR_4_DIGIT: _ClassVar[Validation]
    VALIDATION_LAST_4_SSN: _ClassVar[Validation]
    VALIDATION_US_ZIP: _ClassVar[Validation]
    VALIDATION_INTEGER: _ClassVar[Validation]
    VALIDATION_FLOAT: _ClassVar[Validation]
    VALIDATION_CURRENCY_USD: _ClassVar[Validation]
    VALIDATION_DATE: _ClassVar[Validation]
    VALIDATION_DOB: _ClassVar[Validation]
    VALIDATION_BOOL: _ClassVar[Validation]
    VALIDATION_REGEX: _ClassVar[Validation]

class InvoiceDisplayType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNSPECIFIED: _ClassVar[InvoiceDisplayType]
    AMOUNT_DUE: _ClassVar[InvoiceDisplayType]
    SERVICE_DATE: _ClassVar[InvoiceDisplayType]
    INVOICE_NUMBER: _ClassVar[InvoiceDisplayType]
    ITEM_QUANTITY: _ClassVar[InvoiceDisplayType]
    ITEM_NAME: _ClassVar[InvoiceDisplayType]
    ITEM_DESCRIPTION: _ClassVar[InvoiceDisplayType]
    ITEM_AMOUNT: _ClassVar[InvoiceDisplayType]
    PAYOR_ACCOUNT_NUMBER: _ClassVar[InvoiceDisplayType]
    PAYOR_FIRST_NAME: _ClassVar[InvoiceDisplayType]
    PAYOR_LAST_NAME: _ClassVar[InvoiceDisplayType]
    PAYOR_DATE_OF_BIRTH: _ClassVar[InvoiceDisplayType]
    PAYOR_SSN_R4: _ClassVar[InvoiceDisplayType]
    PAYOR_CELL_PHONE: _ClassVar[InvoiceDisplayType]
    PAYOR_HOME_PHONE: _ClassVar[InvoiceDisplayType]
    PAYOR_WORK_PHONE: _ClassVar[InvoiceDisplayType]
    PAYOR_ZIP_CODE: _ClassVar[InvoiceDisplayType]
    PATIENT_ACCOUNT_NUMBER: _ClassVar[InvoiceDisplayType]
    PATIENT_FIRST_NAME: _ClassVar[InvoiceDisplayType]
    PATIENT_LAST_NAME: _ClassVar[InvoiceDisplayType]
    PATIENT_DATE_OF_BIRTH: _ClassVar[InvoiceDisplayType]
    PATIENT_SSN_R4: _ClassVar[InvoiceDisplayType]
    PATIENT_CELL_PHONE: _ClassVar[InvoiceDisplayType]
    PATIENT_HOME_PHONE: _ClassVar[InvoiceDisplayType]
    PATIENT_WORK_PHONE: _ClassVar[InvoiceDisplayType]
    PATIENT_ZIP_CODE: _ClassVar[InvoiceDisplayType]

class FieldSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FIELD_SOURCE_NONE: _ClassVar[FieldSource]
    FIELD_SOURCE_LINK: _ClassVar[FieldSource]
    FIELD_SOURCE_VERIFICATION_DATA: _ClassVar[FieldSource]
    FIELD_SOURCE_VERIFICATION_API: _ClassVar[FieldSource]
    FIELD_SOURCE_INVOICE_DATA: _ClassVar[FieldSource]
    FIELD_SOURCE_INVOICE_API: _ClassVar[FieldSource]
    FIELD_SOURCE_PAYMENT_DATA: _ClassVar[FieldSource]
    FIELD_SOURCE_PAYMENT_API: _ClassVar[FieldSource]
    FIELD_SOURCE_PAYMENT_FORM: _ClassVar[FieldSource]

class FlowType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    FLOW_TYPE_UNKNOWN: _ClassVar[FlowType]
    FLOW_TYPE_INVOICE: _ClassVar[FlowType]
    FLOW_TYPE_PAYMENT: _ClassVar[FlowType]
    FLOW_TYPE_VERIFICATION: _ClassVar[FlowType]
    FLOW_TYPE_EXECUTE: _ClassVar[FlowType]
INTEGRATION_TYPE_UNKNOWN: IntegrationType
INTEGRATION_TYPE_BRAINTREE: IntegrationType
INTEGRATION_TYPE_RELATIENT: IntegrationType
INTEGRATION_TYPE_CYBERSOURCE: IntegrationType
INTEGRATION_TYPE_CIRCPRO: IntegrationType
INTEGRATION_TYPE_AUTHORIZENET: IntegrationType
INTEGRATION_TYPE_EXPITRANS: IntegrationType
INTEGRATION_TYPE_AXIAMEDFUSION: IntegrationType
INTEGRATION_TYPE_INSTAMED: IntegrationType
INTEGRATION_TYPE_USAEPAY: IntegrationType
INTEGRATION_TYPE_EZIDEBIT: IntegrationType
INTEGRATION_TYPE_BAMBORA: IntegrationType
INTEGRATION_TYPE_REPAY: IntegrationType
INTEGRATION_TYPE_AXIA: IntegrationType
INTEGRATION_TYPE_SECURETRADING: IntegrationType
INTEGRATION_TYPE_PAYMENTVISION: IntegrationType
INTEGRATION_TYPE_INTERPROSE: IntegrationType
INTEGRATION_TYPE_DALLASNEWS: IntegrationType
INTEGRATION_TYPE_PAYWAY: IntegrationType
INTEGRATION_TYPE_BILLINGTREE: IntegrationType
INTEGRATION_TYPE_EXPERIAN: IntegrationType
INTEGRATION_TYPE_NEWSCYCLE: IntegrationType
INTEGRATION_TYPE_TRUSTCOMMERCE: IntegrationType
INTEGRATION_TYPE_VANTIV: IntegrationType
INTEGRATION_TYPE_JOURNEY: IntegrationType
INTEGRATION_TYPE_ATHENAHEALTH: IntegrationType
INTEGRATION_TYPE_BRAINWORKS: IntegrationType
INTEGRATION_TYPE_OSGCONNECT: IntegrationType
INTEGRATION_TYPE_NTVB: IntegrationType
INTEGRATION_TYPE_ELAVON: IntegrationType
INTEGRATION_TYPE_GLOBALPAYMENTS: IntegrationType
INTEGRATION_TYPE_PAY_SCOUT: IntegrationType
INTEGRATION_TYPE_I2C: IntegrationType
INTEGRATION_TYPE_OPAYO: IntegrationType
INTEGRATION_TYPE_SHIFT4: IntegrationType
INTEGRATION_TYPE_POSCORP: IntegrationType
INTEGRATION_TYPE_PIANO: IntegrationType
REQUEST_METHOD_UNKNOWN: RequestMethod
REQUEST_METHOD_BRAINTREE_CREDITSALE: RequestMethod
REQUEST_METHOD_BRAINTREE_BANKSALE: RequestMethod
REQUEST_METHOD_RELATIENT_GETPATIENTBALANCE: RequestMethod
REQUEST_METHOD_RELATIENT_GETPATIENTCCTOKENS: RequestMethod
REQUEST_METHOD_RELATIENT_POSTPATIENTTOKEN: RequestMethod
REQUEST_METHOD_RELATIENT_POSTPATIENTBALANCE: RequestMethod
REQUEST_METHOD_RELATIENT_GETPATIENT: RequestMethod
REQUEST_METHOD_RELATIENT_POSTBALANCEBYID: RequestMethod
REQUEST_METHOD_RELATIENT_CREATE_FORTIS_ACHTOKEN: RequestMethod
REQUEST_METHOD_RELATIENT_CREATE_FORTIS_CCTOKEN: RequestMethod
REQUEST_METHOD_RELATIENT_FORTIS_TOKEN_ACH_DEBIT_PAYMENT: RequestMethod
REQUEST_METHOD_RELATIENT_FORTIS_TOKEN_CC_PAYMENT: RequestMethod
REQUEST_METHOD_CYBERSOURCE_CREDITPAYMENT: RequestMethod
REQUEST_METHOD_CYBERSOURCE_ECHECKPAYMENT: RequestMethod
REQUEST_METHOD_CIRCPRO_PHONELOOKUPWITHBUNDLE: RequestMethod
REQUEST_METHOD_CIRCPRO_PHONELOOKUP: RequestMethod
REQUEST_METHOD_CIRCPRO_VACATIONRESTARTINQUIRY: RequestMethod
REQUEST_METHOD_CIRCPRO_COMPLAINTINQUIRY: RequestMethod
REQUEST_METHOD_CIRCPRO_ACCOUNTINQUIRY: RequestMethod
REQUEST_METHOD_CIRCPRO_ACCOUNTINQUIRYWITHTAX: RequestMethod
REQUEST_METHOD_CIRCPRO_ACCOUNTINQUIRYWITHTAXBUNDLE: RequestMethod
REQUEST_METHOD_CIRCPRO_COMPLAINTCODES: RequestMethod
REQUEST_METHOD_CIRCPRO_COMPLAINTUPDATE: RequestMethod
REQUEST_METHOD_CIRCPRO_VACATIONUPDATE: RequestMethod
REQUEST_METHOD_CIRCPRO_RESTARTUPDATE: RequestMethod
REQUEST_METHOD_CIRCPRO_LAW_IMMEDIATEPAYMENT: RequestMethod
REQUEST_METHOD_CIRCPRO_LAW_UPDATEDATAWITHPAC: RequestMethod
REQUEST_METHOD_CIRCPRO_LAW_GETCUSTOMERS: RequestMethod
REQUEST_METHOD_AUTHORIZENET_CHARGECREDITCARD: RequestMethod
REQUEST_METHOD_AUTHORIZENET_DEBITBANKACCOUNT: RequestMethod
REQUEST_METHOD_AUTHORIZENET_CREATECUSTOMERPAYMENTPROFILE: RequestMethod
REQUEST_METHOD_AUTHORIZENET_PAYPALTRANSACTION: RequestMethod
REQUEST_METHOD_AUTHORIZENET_GOOGLEPAYTRANSACTION: RequestMethod
REQUEST_METHOD_AUTHORIZENET_APPLEPAYTRANSACTION: RequestMethod
REQUEST_METHOD_AUTHORIZENET_PAYPALAUTHCAPTURE: RequestMethod
REQUEST_METHOD_EXPITRANS_CCTRANSACTION: RequestMethod
REQUEST_METHOD_EXPITRANS_ACHTRANSACTION: RequestMethod
REQUEST_METHOD_AXIAMEDFUSION_CCTRANSACTION: RequestMethod
REQUEST_METHOD_AXIAMEDFUSION_ACHTRANSACTION: RequestMethod
REQUEST_METHOD_AXIAMEDFUSION_CARDVERIFY: RequestMethod
REQUEST_METHOD_INSTAMED_PAYMENTSALE: RequestMethod
REQUEST_METHOD_INSTAMED_VOIDPAYMENT: RequestMethod
REQUEST_METHOD_USAEPAY_SUBMITCCPAYMENTS: RequestMethod
REQUEST_METHOD_USAEPAY_SUBMITACHPAYMENTS: RequestMethod
REQUEST_METHOD_USAEPAY_GETCCTOKEN: RequestMethod
REQUEST_METHOD_EZIDEBIT_SUBMITCCPAYMENTS: RequestMethod
REQUEST_METHOD_EZIDEBIT_SUBMITACHPAYMENTS: RequestMethod
REQUEST_METHOD_BAMBORA_SUBMITCCPAYMENTS: RequestMethod
REQUEST_METHOD_BAMBORA_SUBMITACHPAYMENTS: RequestMethod
REQUEST_METHOD_REPAY_STORECARD: RequestMethod
REQUEST_METHOD_REPAY_PAYMENTTOKEN: RequestMethod
REQUEST_METHOD_REPAY_ACHPAYMENTTOKEN: RequestMethod
REQUEST_METHOD_AXIA_SUBMITSALEREQUESTBYCC: RequestMethod
REQUEST_METHOD_AXIA_SUBMITSALEREQUESTBYCHECK: RequestMethod
REQUEST_METHOD_SECURETRADING_SENDPAYMENT: RequestMethod
REQUEST_METHOD_PAYMENTVISION_SUBMITCARDSALEREQUESTBYCC: RequestMethod
REQUEST_METHOD_PAYMENTVISION_SUBMITCARDSALEREQUESTBYACH: RequestMethod
REQUEST_METHOD_INTERPROSE_LOOKUPACCOUNT: RequestMethod
REQUEST_METHOD_INTERPROSE_SUBMITCARDSALEREQUESTBYCC: RequestMethod
REQUEST_METHOD_INTERPROSE_SUBMITCARDSALEREQUESTBYACH: RequestMethod
REQUEST_METHOD_INTERPROSE_LOOKUPPAYMENTID: RequestMethod
REQUEST_METHOD_INTERPROSE_LOOKUPACCOUNTBYFORMID: RequestMethod
REQUEST_METHOD_DALLASNEWS_SEARCHBYPHONE: RequestMethod
REQUEST_METHOD_DALLASNEWS_SEARCHBYZIPSTREET: RequestMethod
REQUEST_METHOD_DALLASNEWS_SEARCHBY: RequestMethod
REQUEST_METHOD_DALLASNEWS_CREATEVACATION: RequestMethod
REQUEST_METHOD_DALLASNEWS_GETVACATION: RequestMethod
REQUEST_METHOD_DALLASNEWS_GETVACATIONDAYSBETWEEN: RequestMethod
REQUEST_METHOD_DALLASNEWS_GETVACATIONWITHCUTOFF: RequestMethod
REQUEST_METHOD_DALLASNEWS_DELETEVACATION: RequestMethod
REQUEST_METHOD_DALLASNEWS_ADDCOMPLAINT: RequestMethod
REQUEST_METHOD_DALLASNEWS_UPDATEPHONENUMBER: RequestMethod
REQUEST_METHOD_DALLASNEWS_STOPACCOUNT: RequestMethod
REQUEST_METHOD_DALLASNEWS_CCPAYMENTTOKEN: RequestMethod
REQUEST_METHOD_DALLASNEWS_ACHPAYMENTTOKEN: RequestMethod
REQUEST_METHOD_PAYWAY_SUBMITCARDSALEREQUEST: RequestMethod
REQUEST_METHOD_PAYWAY_CREATETOKENREQUEST: RequestMethod
REQUEST_METHOD_PAYWAY_SUBMITACHSALEREQUEST: RequestMethod
REQUEST_METHOD_BILLINGTREE_SUBMITCARDSALEREQUEST: RequestMethod
REQUEST_METHOD_EXPERIAN_CC_PAYMENT_REQUEST: RequestMethod
REQUEST_METHOD_EXPERIAN_CC_PAYMENTPLANREQUEST: RequestMethod
REQUEST_METHOD_EXPERIAN_BALANCEREQUEST: RequestMethod
REQUEST_METHOD_EXPERIAN_ACH_PAYMENT_REQUEST: RequestMethod
REQUEST_METHOD_EXPERIAN_ACH_PAYMENTPLANREQUEST: RequestMethod
REQUEST_METHOD_EXPERIAN_STELLA_CARD_ENTRY: RequestMethod
REQUEST_METHOD_EXPERIAN_STELLA_ECHECK: RequestMethod
REQUEST_METHOD_EXPERIAN_STELLA_CARD_DEVICE_TOKENIZATION: RequestMethod
REQUEST_METHOD_EXPERIAN_STELLA_TOKEN_PAYMENT: RequestMethod
REQUEST_METHOD_EXPERIAN_STELLA_ACH_TOKENIZATION: RequestMethod
REQUEST_METHOD_EXPERIAN_STELLA_ADD_USA_EPAY_TOKEN: RequestMethod
REQUEST_METHOD_EXPERIAN_STELLA_PAYMENT_PLANS: RequestMethod
REQUEST_METHOD_EXPERIAN_STELLA_AUTH: RequestMethod
REQUEST_METHOD_NEWSCYCLE_LOGIN: RequestMethod
REQUEST_METHOD_NEWSCYCLE_SEARCHPAGE: RequestMethod
REQUEST_METHOD_NEWSCYCLE_BILLINGINFO: RequestMethod
REQUEST_METHOD_NEWSCYCLE_SERVICEERRORINFO: RequestMethod
REQUEST_METHOD_NEWSCYCLE_SERVICEERRORTRANS: RequestMethod
REQUEST_METHOD_NEWSCYCLE_STOPINFO: RequestMethod
REQUEST_METHOD_NEWSCYCLE_STOPTRANS: RequestMethod
REQUEST_METHOD_NEWSCYCLE_RENEWINFO: RequestMethod
REQUEST_METHOD_NEWSCYCLE_AUTORENEWINFO: RequestMethod
REQUEST_METHOD_NEWSCYCLE_AUTOTRAN: RequestMethod
REQUEST_METHOD_NEWSCYCLE_PAYINFO: RequestMethod
REQUEST_METHOD_NEWSCYCLE_PAYTRAN: RequestMethod
REQUEST_METHOD_TRUSTCOMMERCE_CREDITSALE: RequestMethod
REQUEST_METHOD_TRUSTCOMMERCE_ACHSALE: RequestMethod
REQUEST_METHOD_VANTIV_CREDITSALE: RequestMethod
REQUEST_METHOD_VANTIV_ACHSALE: RequestMethod
REQUEST_METHOD_JOURNEY_LATEST: RequestMethod
REQUEST_METHOD_ATHENAHEALTH_GETPATIENTS: RequestMethod
REQUEST_METHOD_ATHENAHEALTH_GETPATIENTSWITHID: RequestMethod
REQUEST_METHOD_ATHENAHEALTH_CCPAYMENT: RequestMethod
REQUEST_METHOD_BRAINWORKS_GETCUSTOMERSBYPHONE: RequestMethod
REQUEST_METHOD_BRAINWORKS_GETSUSPENDS: RequestMethod
REQUEST_METHOD_BRAINWORKS_GETCUSTOMERBYCUSTIDV2: RequestMethod
REQUEST_METHOD_BRAINWORKS_GETCOMPLAINTS: RequestMethod
REQUEST_METHOD_BRAINWORKS_GETCODESORTYPES: RequestMethod
REQUEST_METHOD_BRAINWORKS_STOPSUSPENDS: RequestMethod
REQUEST_METHOD_BRAINWORKS_STARTSUSPENDS: RequestMethod
REQUEST_METHOD_BRAINWORKS_SENDCOMPLAINT: RequestMethod
REQUEST_METHOD_BRAINWORKS_GETCUSTOMERBYCUSTID: RequestMethod
REQUEST_METHOD_OSGCONNECT_CCPAYMENTS: RequestMethod
REQUEST_METHOD_OSGCONNECT_ACHPAYMENTS: RequestMethod
REQUEST_METHOD_OSGCONNECT_VALIDATEACCOUNTNO: RequestMethod
REQUEST_METHOD_NTVB_CREDIT_MISSED_DELIVERY: RequestMethod
REQUEST_METHOD_NTVB_CUSTOMER_SEARCH: RequestMethod
REQUEST_METHOD_NTVB_END_CALL: RequestMethod
REQUEST_METHOD_NTVB_INTEGRATION_DEFINITION: RequestMethod
REQUEST_METHOD_NTVB_MISSED_DELIVERY: RequestMethod
REQUEST_METHOD_NTVB_REMOVE_AUTORENEWAL: RequestMethod
REQUEST_METHOD_NTVB_RENEW_SUBSCRIPTION: RequestMethod
REQUEST_METHOD_NTVB_RENEWAL_OFFERS: RequestMethod
REQUEST_METHOD_NTVB_SET_AUTORENEWAL: RequestMethod
REQUEST_METHOD_NTVB_START_INCOMING_CALL: RequestMethod
REQUEST_METHOD_NTVB_START_OUTGOING_CALL: RequestMethod
REQUEST_METHOD_NTVB_SUBSCRIPTION_INFO: RequestMethod
REQUEST_METHOD_NTVB_VACATION_STOP: RequestMethod
REQUEST_METHOD_NTVB_AUTHTEST: RequestMethod
REQUEST_METHOD_ELAVON_CREDIT_CARD_SALE: RequestMethod
REQUEST_METHOD_ELAVON_ADD_RECURRING: RequestMethod
REQUEST_METHOD_ELAVON_DCC_RESPONSE: RequestMethod
REQUEST_METHOD_ELAVON_DELETE_RECURRING: RequestMethod
REQUEST_METHOD_ELAVON_UPDATE_RECURRING: RequestMethod
REQUEST_METHOD_ELAVON_HEALTH_CARE_CC_SALE: RequestMethod
REQUEST_METHOD_ELAVON_ADD_INSTALLMENT: RequestMethod
REQUEST_METHOD_ELAVON_UPDATE_INSTALLMENT: RequestMethod
REQUEST_METHOD_ELAVON_DELETE_INSTALLMENT: RequestMethod
REQUEST_METHOD_ELAVON_MCC_CREDIT_CARD_SALE: RequestMethod
REQUEST_METHOD_GLOBALPAYMENTS_CARDSALE: RequestMethod
REQUEST_METHOD_GLOBALPAYMENTS_GET_TRANSACTION_BY_ID: RequestMethod
REQUEST_METHOD_GLOBALPAYMENTS_LIST_TRANSACTIONS: RequestMethod
REQUEST_METHOD_GLOBALPAYMENTS_REFUND_SALE: RequestMethod
REQUEST_METHOD_GLOBALPAYMENTS_REVERSE_SALE_OR_REFUND: RequestMethod
REQUEST_METHOD_PAY_SCOUT_CREDIT_CARD_SALE: RequestMethod
REQUEST_METHOD_PAY_SCOUT_ECHECK_SALE: RequestMethod
REQUEST_METHOD_I2C_ECHO: RequestMethod
REQUEST_METHOD_I2C_BALANCE_INQUIRY: RequestMethod
REQUEST_METHOD_I2C_VERIFY_USER: RequestMethod
REQUEST_METHOD_I2C_SEARCH_CUSTOMER: RequestMethod
REQUEST_METHOD_I2C_MAKE_PAYMENT: RequestMethod
REQUEST_METHOD_I2C_GET_CARDHOLDER_PROFILE: RequestMethod
REQUEST_METHOD_I2C_GET_CARDHOLDER_STATEMENT: RequestMethod
REQUEST_METHOD_I2C_GET_CARDHOLDER_BALANCE: RequestMethod
REQUEST_METHOD_I2C_GET_CREDITPAYMENT_INFO: RequestMethod
REQUEST_METHOD_I2C_TRANSACTION_HISTORY: RequestMethod
REQUEST_METHOD_OPAYO_CCPAYMENTS: RequestMethod
REQUEST_METHOD_SHIFT4_CCPAYMENTS: RequestMethod
REQUEST_METHOD_POSCORP_ACCESSTOKEN: RequestMethod
REQUEST_METHOD_POSCORP_LOOKUP_GUARANTOR: RequestMethod
REQUEST_METHOD_POSCORP_UPDATE_PAYMENT_STATUS: RequestMethod
REQUEST_METHOD_PIANO_GET_USER: RequestMethod
REQUEST_METHOD_PIANO_UPDATE_USER: RequestMethod
TRANSACTION_TYPE_PAYMENT: TransactionType
TRANSACTION_TYPE_DATA_INQUIRY: TransactionType
TRANSACTION_TYPE_ACCOUNT_VERIFY: TransactionType
REQUEST_SOURCE_IVR: RequestSource
REQUEST_SOURCE_EMAIL: RequestSource
REQUEST_SOURCE_WEB: RequestSource
REQUEST_SOURCE_SMS: RequestSource
REQUEST_SOURCE_CHAT: RequestSource
REQUEST_SOURCE_LMS: RequestSource
TRANSACTION_RESULT_SUCCESS: TransactionResult
TRANSACTION_RESULT_FAILED: TransactionResult
VALUE_TYPE_UNKNOWN: ValueType
VALUE_TYPE_NUMBER: ValueType
VALUE_TYPE_BOOL: ValueType
VALUE_TYPE_MAP: ValueType
VALUE_TYPE_ARRAY: ValueType
VALUE_TYPE_INT: ValueType
VALUE_TYPE_STRING: ValueType
VALUE_TYPE_TIME: ValueType
VALUE_TYPE_COMPOSITE_VAL: ValueType
VISIBILITY_INVISIBLE: Visibility
VISIBILITY_UNRESTRICTED: Visibility
VISIBILITY_RUNTIME: Visibility
VISIBILITY_BY_METHOD: Visibility
VISIBILITY_PLUGIN: Visibility
COMPARE_OPERATION_EQ: CompareOperation
COMPARE_OPERATION_GT: CompareOperation
COMPARE_OPERATION_LT: CompareOperation
COMPARE_OPERATION_GE: CompareOperation
COMPARE_OPERATION_LE: CompareOperation
COMPARE_OPERATION_NE: CompareOperation
FFL_ANY: FlowFieldLoc
FFL_LINK: FlowFieldLoc
FFL_PLUGIN_INST: FlowFieldLoc
FFL_SUBMIT: FlowFieldLoc
VALIDATION_NONE: Validation
VALIDATION_CREDITCARD: Validation
VALIDATION_CVC: Validation
VALIDATION_MONTH_2_DIGIT: Validation
VALIDATION_YEAR_4_DIGIT: Validation
VALIDATION_LAST_4_SSN: Validation
VALIDATION_US_ZIP: Validation
VALIDATION_INTEGER: Validation
VALIDATION_FLOAT: Validation
VALIDATION_CURRENCY_USD: Validation
VALIDATION_DATE: Validation
VALIDATION_DOB: Validation
VALIDATION_BOOL: Validation
VALIDATION_REGEX: Validation
UNSPECIFIED: InvoiceDisplayType
AMOUNT_DUE: InvoiceDisplayType
SERVICE_DATE: InvoiceDisplayType
INVOICE_NUMBER: InvoiceDisplayType
ITEM_QUANTITY: InvoiceDisplayType
ITEM_NAME: InvoiceDisplayType
ITEM_DESCRIPTION: InvoiceDisplayType
ITEM_AMOUNT: InvoiceDisplayType
PAYOR_ACCOUNT_NUMBER: InvoiceDisplayType
PAYOR_FIRST_NAME: InvoiceDisplayType
PAYOR_LAST_NAME: InvoiceDisplayType
PAYOR_DATE_OF_BIRTH: InvoiceDisplayType
PAYOR_SSN_R4: InvoiceDisplayType
PAYOR_CELL_PHONE: InvoiceDisplayType
PAYOR_HOME_PHONE: InvoiceDisplayType
PAYOR_WORK_PHONE: InvoiceDisplayType
PAYOR_ZIP_CODE: InvoiceDisplayType
PATIENT_ACCOUNT_NUMBER: InvoiceDisplayType
PATIENT_FIRST_NAME: InvoiceDisplayType
PATIENT_LAST_NAME: InvoiceDisplayType
PATIENT_DATE_OF_BIRTH: InvoiceDisplayType
PATIENT_SSN_R4: InvoiceDisplayType
PATIENT_CELL_PHONE: InvoiceDisplayType
PATIENT_HOME_PHONE: InvoiceDisplayType
PATIENT_WORK_PHONE: InvoiceDisplayType
PATIENT_ZIP_CODE: InvoiceDisplayType
FIELD_SOURCE_NONE: FieldSource
FIELD_SOURCE_LINK: FieldSource
FIELD_SOURCE_VERIFICATION_DATA: FieldSource
FIELD_SOURCE_VERIFICATION_API: FieldSource
FIELD_SOURCE_INVOICE_DATA: FieldSource
FIELD_SOURCE_INVOICE_API: FieldSource
FIELD_SOURCE_PAYMENT_DATA: FieldSource
FIELD_SOURCE_PAYMENT_API: FieldSource
FIELD_SOURCE_PAYMENT_FORM: FieldSource
FLOW_TYPE_UNKNOWN: FlowType
FLOW_TYPE_INVOICE: FlowType
FLOW_TYPE_PAYMENT: FlowType
FLOW_TYPE_VERIFICATION: FlowType
FLOW_TYPE_EXECUTE: FlowType

class Invoices(_message.Message):
    __slots__ = ["top_level_fields", "invoices"]
    TOP_LEVEL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    INVOICES_FIELD_NUMBER: _ClassVar[int]
    top_level_fields: _containers.RepeatedCompositeFieldContainer[InvoiceField]
    invoices: _containers.RepeatedCompositeFieldContainer[Invoice]
    def __init__(self, top_level_fields: _Optional[_Iterable[_Union[InvoiceField, _Mapping]]] = ..., invoices: _Optional[_Iterable[_Union[Invoice, _Mapping]]] = ...) -> None: ...

class Invoice(_message.Message):
    __slots__ = ["top_level_fields", "items"]
    TOP_LEVEL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    top_level_fields: _containers.RepeatedCompositeFieldContainer[InvoiceField]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, top_level_fields: _Optional[_Iterable[_Union[InvoiceField, _Mapping]]] = ..., items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ["fields"]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[InvoiceField]
    def __init__(self, fields: _Optional[_Iterable[_Union[InvoiceField, _Mapping]]] = ...) -> None: ...

class InvoiceField(_message.Message):
    __slots__ = ["item_type", "name", "display_name", "value"]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    item_type: InvoiceDisplayType
    name: str
    display_name: str
    value: str
    def __init__(self, item_type: _Optional[_Union[InvoiceDisplayType, str]] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class InvoiceTemplate(_message.Message):
    __slots__ = ["account_fields", "invoice_descriptions"]
    ACCOUNT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    INVOICE_DESCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
    account_fields: _containers.RepeatedCompositeFieldContainer[FieldDefinition]
    invoice_descriptions: _containers.RepeatedCompositeFieldContainer[InvoiceDescription]
    def __init__(self, account_fields: _Optional[_Iterable[_Union[FieldDefinition, _Mapping]]] = ..., invoice_descriptions: _Optional[_Iterable[_Union[InvoiceDescription, _Mapping]]] = ...) -> None: ...

class InvoiceDescription(_message.Message):
    __slots__ = ["invoice_description_fields", "line_items"]
    INVOICE_DESCRIPTION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    invoice_description_fields: _containers.RepeatedCompositeFieldContainer[FieldDefinition]
    line_items: _containers.RepeatedCompositeFieldContainer[LineItemGroup]
    def __init__(self, invoice_description_fields: _Optional[_Iterable[_Union[FieldDefinition, _Mapping]]] = ..., line_items: _Optional[_Iterable[_Union[LineItemGroup, _Mapping]]] = ...) -> None: ...

class LineItemGroup(_message.Message):
    __slots__ = ["line_item_fields"]
    LINE_ITEM_FIELDS_FIELD_NUMBER: _ClassVar[int]
    line_item_fields: _containers.RepeatedCompositeFieldContainer[FieldDefinition]
    def __init__(self, line_item_fields: _Optional[_Iterable[_Union[FieldDefinition, _Mapping]]] = ...) -> None: ...

class ListOfStrings(_message.Message):
    __slots__ = ["values"]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...

class Flow(_message.Message):
    __slots__ = ["invoice_flow", "payment_flow", "verification_flow", "execute_flow"]
    INVOICE_FLOW_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FLOW_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FLOW_FIELD_NUMBER: _ClassVar[int]
    EXECUTE_FLOW_FIELD_NUMBER: _ClassVar[int]
    invoice_flow: InvoiceFlow
    payment_flow: PaymentFlow
    verification_flow: VerificationFlow
    execute_flow: ExecuteFlow
    def __init__(self, invoice_flow: _Optional[_Union[InvoiceFlow, _Mapping]] = ..., payment_flow: _Optional[_Union[PaymentFlow, _Mapping]] = ..., verification_flow: _Optional[_Union[VerificationFlow, _Mapping]] = ..., execute_flow: _Optional[_Union[ExecuteFlow, _Mapping]] = ...) -> None: ...

class InvoiceFlow(_message.Message):
    __slots__ = ["plugin_instance_id", "experian_query_balance", "authorize_net_link_data", "authorize_net_custom_http", "journey", "dynamic_journey", "invoice_template"]
    PLUGIN_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_QUERY_BALANCE_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZE_NET_LINK_DATA_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZE_NET_CUSTOM_HTTP_FIELD_NUMBER: _ClassVar[int]
    JOURNEY_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_JOURNEY_FIELD_NUMBER: _ClassVar[int]
    INVOICE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    plugin_instance_id: str
    experian_query_balance: InvoiceExperianQueryBalance
    authorize_net_link_data: InvoiceAuthorizeNetLinkData
    authorize_net_custom_http: InvoiceAuthorizeNetCustomHttp
    journey: InvoiceJourney
    dynamic_journey: InvoiceDynamicJourney
    invoice_template: InvoiceTemplate
    def __init__(self, plugin_instance_id: _Optional[str] = ..., experian_query_balance: _Optional[_Union[InvoiceExperianQueryBalance, _Mapping]] = ..., authorize_net_link_data: _Optional[_Union[InvoiceAuthorizeNetLinkData, _Mapping]] = ..., authorize_net_custom_http: _Optional[_Union[InvoiceAuthorizeNetCustomHttp, _Mapping]] = ..., journey: _Optional[_Union[InvoiceJourney, _Mapping]] = ..., dynamic_journey: _Optional[_Union[InvoiceDynamicJourney, _Mapping]] = ..., invoice_template: _Optional[_Union[InvoiceTemplate, _Mapping]] = ...) -> None: ...

class PaymentFlow(_message.Message):
    __slots__ = ["plugin_instance_id", "experian_cc", "experian_ach", "authorize_net_cc", "authorize_net_ach", "authorize_net_paypal", "authorize_net_apple_pay", "authorize_net_google_pay", "payway_submit_card_sale_request", "payway_submit_ach_alert_request", "payment_fields"]
    PLUGIN_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_CC_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_ACH_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZE_NET_CC_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZE_NET_ACH_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZE_NET_PAYPAL_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZE_NET_APPLE_PAY_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZE_NET_GOOGLE_PAY_FIELD_NUMBER: _ClassVar[int]
    PAYWAY_SUBMIT_CARD_SALE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PAYWAY_SUBMIT_ACH_ALERT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELDS_FIELD_NUMBER: _ClassVar[int]
    plugin_instance_id: str
    experian_cc: PaymentExperianCC
    experian_ach: PaymentExperianACH
    authorize_net_cc: PaymentAuthorizeNetCC
    authorize_net_ach: PaymentAuthorizeNetACH
    authorize_net_paypal: PaymentAuthorizeNetPaypal
    authorize_net_apple_pay: PaymentAuthorizeNetApplePay
    authorize_net_google_pay: PaymentAuthorizeNetGooglePay
    payway_submit_card_sale_request: PaymentPaywaySubmitCardSaleRequest
    payway_submit_ach_alert_request: PaymentPaywaySubmitACHAlertRequest
    payment_fields: _containers.RepeatedCompositeFieldContainer[FieldDefinition]
    def __init__(self, plugin_instance_id: _Optional[str] = ..., experian_cc: _Optional[_Union[PaymentExperianCC, _Mapping]] = ..., experian_ach: _Optional[_Union[PaymentExperianACH, _Mapping]] = ..., authorize_net_cc: _Optional[_Union[PaymentAuthorizeNetCC, _Mapping]] = ..., authorize_net_ach: _Optional[_Union[PaymentAuthorizeNetACH, _Mapping]] = ..., authorize_net_paypal: _Optional[_Union[PaymentAuthorizeNetPaypal, _Mapping]] = ..., authorize_net_apple_pay: _Optional[_Union[PaymentAuthorizeNetApplePay, _Mapping]] = ..., authorize_net_google_pay: _Optional[_Union[PaymentAuthorizeNetGooglePay, _Mapping]] = ..., payway_submit_card_sale_request: _Optional[_Union[PaymentPaywaySubmitCardSaleRequest, _Mapping]] = ..., payway_submit_ach_alert_request: _Optional[_Union[PaymentPaywaySubmitACHAlertRequest, _Mapping]] = ..., payment_fields: _Optional[_Iterable[_Union[FieldDefinition, _Mapping]]] = ...) -> None: ...

class VerificationFlow(_message.Message):
    __slots__ = ["plugin_instance_id", "experian_query_balance", "experian_link_data", "experian_zip_dob", "authorize_net_customer_profile", "authorize_net_link_data", "journey", "verification_fields"]
    PLUGIN_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_QUERY_BALANCE_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_LINK_DATA_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_ZIP_DOB_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZE_NET_CUSTOMER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZE_NET_LINK_DATA_FIELD_NUMBER: _ClassVar[int]
    JOURNEY_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_FIELDS_FIELD_NUMBER: _ClassVar[int]
    plugin_instance_id: str
    experian_query_balance: VerificationExperianQueryBalance
    experian_link_data: VerificationExperianLinkData
    experian_zip_dob: VerificationExperianZipDob
    authorize_net_customer_profile: VerificationAuthorizeNetCustomerProfile
    authorize_net_link_data: VerificationAuthorizeNetLinkData
    journey: VerificationJourney
    verification_fields: _containers.RepeatedCompositeFieldContainer[FieldDefinition]
    def __init__(self, plugin_instance_id: _Optional[str] = ..., experian_query_balance: _Optional[_Union[VerificationExperianQueryBalance, _Mapping]] = ..., experian_link_data: _Optional[_Union[VerificationExperianLinkData, _Mapping]] = ..., experian_zip_dob: _Optional[_Union[VerificationExperianZipDob, _Mapping]] = ..., authorize_net_customer_profile: _Optional[_Union[VerificationAuthorizeNetCustomerProfile, _Mapping]] = ..., authorize_net_link_data: _Optional[_Union[VerificationAuthorizeNetLinkData, _Mapping]] = ..., journey: _Optional[_Union[VerificationJourney, _Mapping]] = ..., verification_fields: _Optional[_Iterable[_Union[FieldDefinition, _Mapping]]] = ...) -> None: ...

class FieldDefinition(_message.Message):
    __slots__ = ["name", "alt_name", "display_name", "field_type", "validation_type", "formats", "invoice_type", "helper_text"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALT_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    FORMATS_FIELD_NUMBER: _ClassVar[int]
    INVOICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    HELPER_TEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    alt_name: str
    display_name: str
    field_type: ValueType
    validation_type: Validation
    formats: _containers.RepeatedScalarFieldContainer[str]
    invoice_type: InvoiceDisplayType
    helper_text: HelperText
    def __init__(self, name: _Optional[str] = ..., alt_name: _Optional[str] = ..., display_name: _Optional[str] = ..., field_type: _Optional[_Union[ValueType, str]] = ..., validation_type: _Optional[_Union[Validation, str]] = ..., formats: _Optional[_Iterable[str]] = ..., invoice_type: _Optional[_Union[InvoiceDisplayType, str]] = ..., helper_text: _Optional[_Union[HelperText, _Mapping]] = ...) -> None: ...

class HelperText(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class ExecuteFlow(_message.Message):
    __slots__ = ["plugin_instance_id", "braintree_credit_sale", "braintree_bank_sale", "relatient_get_patient_balance", "relatient_get_patient_cc_tokens", "relatient_post_patient_token", "relatient_post_patient_balance", "relatient_get_patient", "relatient_post_balance_by_id", "relatient_create_fortis_achtoken", "relatient_create_fortis_cctoken", "relatient_fortis_token_ach_debit_payment", "relatient_fortis_token_cc_payment", "cybersource_credit_payment", "cybersource_echeck_payment", "circpro_phone_lookup_with_bundle", "circpro_phone_lookup", "circpro_vacation_restart_inquiry", "circpro_complaint_inquiry", "circpro_account_inquiry", "circpro_account_inquiry_with_tax", "circpro_account_inquiry_with_tax_bundle", "circpro_complaint_codes", "circpro_complaint_update", "circpro_vacation_update", "circpro_restart_update", "circpro_law_immediate_payment", "circpro_law_update_data_with_pac", "circpro_law_get_customers", "authorizenet_charge_credit_card", "authorizenet_debit_bank_account", "authorizenet_create_customer_payment_profile", "authorizenet_paypal_transaction", "authorizenet_google_pay_transaction", "authorizenet_apple_pay_transaction", "authorizenet_pay_pal_auth_capture", "expitrans_cc_transaction", "expitrans_ach_transaction", "axiamedfusion_cc_transaction", "axiamedfusion_ach_transaction", "axiamedfusion_card_verify", "instamed_payment_sale", "instamed_void_payment", "usaepay_submit_cc_payments", "usaepay_submit_ach_payments", "usaepay_get_cc_token", "ezidebit_submit_cc_payments", "ezidebit_submit_ach_payments", "bambora_submit_cc_payments", "bambora_submit_ach_payments", "repay_store_card", "repay_payment_token", "repay_ach_payment_token", "axia_submit_sale_request_by_cc", "axia_submit_sale_request_by_check", "securetrading_send_payment", "payment_vision_submit_card_sale_request_by_cc", "payment_vision_submit_card_sale_request_by_ach", "interprose_lookup_account", "interprose_submit_card_sale_request_by_cc", "interprose_submit_card_sale_request_by_ach", "interprose_lookup_payment_id", "interprose_lookup_account_by_form_id", "dallasnews_search_by_phone", "dallasnews_search_by_zip_street", "dallasnews_search_by", "dallasnews_create_vacation", "dallasnews_get_vacation", "dallasnews_get_vacation_days_between", "dallasnews_get_vacation_with_cutoff", "dallasnews_delete_vacation", "dallasnews_add_complaint", "dallasnews_update_phone_number", "dallasnews_stop_account", "dallasnews_cc_payment_token", "dallasnews_ach_payment_token", "payway_submit_card_sale_request", "payway_create_token_request", "payway_submit_ach_sale_request", "billingtree_submit_card_sale_request", "experian_cc_payment_request", "experian_cc_payment_plan_request", "experian_balancerequest", "experian_ach_payment_request", "experian_ach_payment_plan_request", "experian_stella_card_entry", "experian_stella_echeck", "experian_stella_card_device_tokenization", "experian_stella_token_payment", "experian_stella_ach_tokenization", "experian_stella_add_usa_epay_token", "experian_stella_payment_plans", "experian_stella_auth", "newscycle_login", "newscycle_search_page", "newscycle_billing_info", "newscycle_service_error_info", "newscycle_service_error_trans", "newscycle_stop_info", "newscycle_stop_trans", "newscycle_renew_info", "newscycle_auto_renew_info", "newscycle_auto_tran", "newscycle_pay_info", "newscycle_pay_tran", "trustcommerce_credit_sale", "trustcommerce_ach_sale", "vantiv_credit_sale", "vantiv_ach_sale", "journey_latest", "athenahealth_get_patients", "athenahealth_get_patients_with_id", "athenahealth_cc_payment", "brainworks_get_customers_by_phone", "brainworks_get_suspends", "brainworks_get_customer_by_cust_id_v2", "brainworks_get_complaints", "brainworks_get_codes_or_types", "brainworks_stop_suspends", "brainworks_start_suspends", "brainworks_send_complaint", "brainworks_get_customer_by_cust_id", "osgconnect_cc_payments", "osgconnect_ach_payments", "osgconnect_validate_account_no", "ntvb_credit_missed_delivery", "ntvb_customer_search", "ntvb_end_call", "ntvb_integration_definition", "ntvb_missed_delivery", "ntvb_remove_autorenewal", "ntvb_renew_subscription", "ntvb_renewal_offers", "ntvb_set_autorenewal", "ntvb_start_incoming_call", "ntvb_start_outgoing_call", "ntvb_subscription_info", "ntvb_vacation_stop", "ntvb_authtest", "elavon_credit_card_sale", "elavon_add_recurring", "elavon_dcc_response", "elavon_delete_recurring", "elavon_update_recurring", "elavon_health_care_cc_sale", "elavon_add_installment", "elavon_update_installment", "elavon_delete_installment", "elavon_mcc_credit_card_sale", "globalPayments_card_sale", "globalPayments_get_transaction_by_id", "globalPayments_list_transactions", "globalPayments_refund_sale", "globalPayments_reverse_sale_or_refund", "payscout_credit_sale", "payscout_echeck_sale", "i2c_echo", "i2c_balance_inquiry", "i2c_verify_user", "i2c_search_customer", "i2c_make_payment", "i2c_get_cardholder_profile", "i2c_get_cardholder_statement", "i2c_get_cardholder_balance", "i2c_get_creditpayment_info", "i2c_transaction_history", "opayo_cc_payment", "shift4_cc_payment", "poscorp_accesstoken", "poscorp_lookup_guarantor", "poscorp_update_payment_status", "PIANO_GET_USER", "PIANO_UPDATE_USER"]
    PLUGIN_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    BRAINTREE_CREDIT_SALE_FIELD_NUMBER: _ClassVar[int]
    BRAINTREE_BANK_SALE_FIELD_NUMBER: _ClassVar[int]
    RELATIENT_GET_PATIENT_BALANCE_FIELD_NUMBER: _ClassVar[int]
    RELATIENT_GET_PATIENT_CC_TOKENS_FIELD_NUMBER: _ClassVar[int]
    RELATIENT_POST_PATIENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RELATIENT_POST_PATIENT_BALANCE_FIELD_NUMBER: _ClassVar[int]
    RELATIENT_GET_PATIENT_FIELD_NUMBER: _ClassVar[int]
    RELATIENT_POST_BALANCE_BY_ID_FIELD_NUMBER: _ClassVar[int]
    RELATIENT_CREATE_FORTIS_ACHTOKEN_FIELD_NUMBER: _ClassVar[int]
    RELATIENT_CREATE_FORTIS_CCTOKEN_FIELD_NUMBER: _ClassVar[int]
    RELATIENT_FORTIS_TOKEN_ACH_DEBIT_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    RELATIENT_FORTIS_TOKEN_CC_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    CYBERSOURCE_CREDIT_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    CYBERSOURCE_ECHECK_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_PHONE_LOOKUP_WITH_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_PHONE_LOOKUP_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_VACATION_RESTART_INQUIRY_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_COMPLAINT_INQUIRY_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_ACCOUNT_INQUIRY_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_ACCOUNT_INQUIRY_WITH_TAX_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_ACCOUNT_INQUIRY_WITH_TAX_BUNDLE_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_COMPLAINT_CODES_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_COMPLAINT_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_VACATION_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_RESTART_UPDATE_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_LAW_IMMEDIATE_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_LAW_UPDATE_DATA_WITH_PAC_FIELD_NUMBER: _ClassVar[int]
    CIRCPRO_LAW_GET_CUSTOMERS_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZENET_CHARGE_CREDIT_CARD_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZENET_DEBIT_BANK_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZENET_CREATE_CUSTOMER_PAYMENT_PROFILE_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZENET_PAYPAL_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZENET_GOOGLE_PAY_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZENET_APPLE_PAY_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    AUTHORIZENET_PAY_PAL_AUTH_CAPTURE_FIELD_NUMBER: _ClassVar[int]
    EXPITRANS_CC_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    EXPITRANS_ACH_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    AXIAMEDFUSION_CC_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    AXIAMEDFUSION_ACH_TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    AXIAMEDFUSION_CARD_VERIFY_FIELD_NUMBER: _ClassVar[int]
    INSTAMED_PAYMENT_SALE_FIELD_NUMBER: _ClassVar[int]
    INSTAMED_VOID_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    USAEPAY_SUBMIT_CC_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    USAEPAY_SUBMIT_ACH_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    USAEPAY_GET_CC_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EZIDEBIT_SUBMIT_CC_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    EZIDEBIT_SUBMIT_ACH_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    BAMBORA_SUBMIT_CC_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    BAMBORA_SUBMIT_ACH_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    REPAY_STORE_CARD_FIELD_NUMBER: _ClassVar[int]
    REPAY_PAYMENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REPAY_ACH_PAYMENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AXIA_SUBMIT_SALE_REQUEST_BY_CC_FIELD_NUMBER: _ClassVar[int]
    AXIA_SUBMIT_SALE_REQUEST_BY_CHECK_FIELD_NUMBER: _ClassVar[int]
    SECURETRADING_SEND_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_VISION_SUBMIT_CARD_SALE_REQUEST_BY_CC_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_VISION_SUBMIT_CARD_SALE_REQUEST_BY_ACH_FIELD_NUMBER: _ClassVar[int]
    INTERPROSE_LOOKUP_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    INTERPROSE_SUBMIT_CARD_SALE_REQUEST_BY_CC_FIELD_NUMBER: _ClassVar[int]
    INTERPROSE_SUBMIT_CARD_SALE_REQUEST_BY_ACH_FIELD_NUMBER: _ClassVar[int]
    INTERPROSE_LOOKUP_PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    INTERPROSE_LOOKUP_ACCOUNT_BY_FORM_ID_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_SEARCH_BY_PHONE_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_SEARCH_BY_ZIP_STREET_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_SEARCH_BY_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_CREATE_VACATION_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_GET_VACATION_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_GET_VACATION_DAYS_BETWEEN_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_GET_VACATION_WITH_CUTOFF_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_DELETE_VACATION_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_ADD_COMPLAINT_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_UPDATE_PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_STOP_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_CC_PAYMENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DALLASNEWS_ACH_PAYMENT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PAYWAY_SUBMIT_CARD_SALE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PAYWAY_CREATE_TOKEN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PAYWAY_SUBMIT_ACH_SALE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    BILLINGTREE_SUBMIT_CARD_SALE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_CC_PAYMENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_CC_PAYMENT_PLAN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_BALANCEREQUEST_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_ACH_PAYMENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_ACH_PAYMENT_PLAN_REQUEST_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_STELLA_CARD_ENTRY_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_STELLA_ECHECK_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_STELLA_CARD_DEVICE_TOKENIZATION_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_STELLA_TOKEN_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_STELLA_ACH_TOKENIZATION_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_STELLA_ADD_USA_EPAY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_STELLA_PAYMENT_PLANS_FIELD_NUMBER: _ClassVar[int]
    EXPERIAN_STELLA_AUTH_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_LOGIN_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_SEARCH_PAGE_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_BILLING_INFO_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_SERVICE_ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_SERVICE_ERROR_TRANS_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_STOP_INFO_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_STOP_TRANS_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_RENEW_INFO_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_AUTO_RENEW_INFO_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_AUTO_TRAN_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_PAY_INFO_FIELD_NUMBER: _ClassVar[int]
    NEWSCYCLE_PAY_TRAN_FIELD_NUMBER: _ClassVar[int]
    TRUSTCOMMERCE_CREDIT_SALE_FIELD_NUMBER: _ClassVar[int]
    TRUSTCOMMERCE_ACH_SALE_FIELD_NUMBER: _ClassVar[int]
    VANTIV_CREDIT_SALE_FIELD_NUMBER: _ClassVar[int]
    VANTIV_ACH_SALE_FIELD_NUMBER: _ClassVar[int]
    JOURNEY_LATEST_FIELD_NUMBER: _ClassVar[int]
    ATHENAHEALTH_GET_PATIENTS_FIELD_NUMBER: _ClassVar[int]
    ATHENAHEALTH_GET_PATIENTS_WITH_ID_FIELD_NUMBER: _ClassVar[int]
    ATHENAHEALTH_CC_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    BRAINWORKS_GET_CUSTOMERS_BY_PHONE_FIELD_NUMBER: _ClassVar[int]
    BRAINWORKS_GET_SUSPENDS_FIELD_NUMBER: _ClassVar[int]
    BRAINWORKS_GET_CUSTOMER_BY_CUST_ID_V2_FIELD_NUMBER: _ClassVar[int]
    BRAINWORKS_GET_COMPLAINTS_FIELD_NUMBER: _ClassVar[int]
    BRAINWORKS_GET_CODES_OR_TYPES_FIELD_NUMBER: _ClassVar[int]
    BRAINWORKS_STOP_SUSPENDS_FIELD_NUMBER: _ClassVar[int]
    BRAINWORKS_START_SUSPENDS_FIELD_NUMBER: _ClassVar[int]
    BRAINWORKS_SEND_COMPLAINT_FIELD_NUMBER: _ClassVar[int]
    BRAINWORKS_GET_CUSTOMER_BY_CUST_ID_FIELD_NUMBER: _ClassVar[int]
    OSGCONNECT_CC_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    OSGCONNECT_ACH_PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    OSGCONNECT_VALIDATE_ACCOUNT_NO_FIELD_NUMBER: _ClassVar[int]
    NTVB_CREDIT_MISSED_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    NTVB_CUSTOMER_SEARCH_FIELD_NUMBER: _ClassVar[int]
    NTVB_END_CALL_FIELD_NUMBER: _ClassVar[int]
    NTVB_INTEGRATION_DEFINITION_FIELD_NUMBER: _ClassVar[int]
    NTVB_MISSED_DELIVERY_FIELD_NUMBER: _ClassVar[int]
    NTVB_REMOVE_AUTORENEWAL_FIELD_NUMBER: _ClassVar[int]
    NTVB_RENEW_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
    NTVB_RENEWAL_OFFERS_FIELD_NUMBER: _ClassVar[int]
    NTVB_SET_AUTORENEWAL_FIELD_NUMBER: _ClassVar[int]
    NTVB_START_INCOMING_CALL_FIELD_NUMBER: _ClassVar[int]
    NTVB_START_OUTGOING_CALL_FIELD_NUMBER: _ClassVar[int]
    NTVB_SUBSCRIPTION_INFO_FIELD_NUMBER: _ClassVar[int]
    NTVB_VACATION_STOP_FIELD_NUMBER: _ClassVar[int]
    NTVB_AUTHTEST_FIELD_NUMBER: _ClassVar[int]
    ELAVON_CREDIT_CARD_SALE_FIELD_NUMBER: _ClassVar[int]
    ELAVON_ADD_RECURRING_FIELD_NUMBER: _ClassVar[int]
    ELAVON_DCC_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ELAVON_DELETE_RECURRING_FIELD_NUMBER: _ClassVar[int]
    ELAVON_UPDATE_RECURRING_FIELD_NUMBER: _ClassVar[int]
    ELAVON_HEALTH_CARE_CC_SALE_FIELD_NUMBER: _ClassVar[int]
    ELAVON_ADD_INSTALLMENT_FIELD_NUMBER: _ClassVar[int]
    ELAVON_UPDATE_INSTALLMENT_FIELD_NUMBER: _ClassVar[int]
    ELAVON_DELETE_INSTALLMENT_FIELD_NUMBER: _ClassVar[int]
    ELAVON_MCC_CREDIT_CARD_SALE_FIELD_NUMBER: _ClassVar[int]
    GLOBALPAYMENTS_CARD_SALE_FIELD_NUMBER: _ClassVar[int]
    GLOBALPAYMENTS_GET_TRANSACTION_BY_ID_FIELD_NUMBER: _ClassVar[int]
    GLOBALPAYMENTS_LIST_TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    GLOBALPAYMENTS_REFUND_SALE_FIELD_NUMBER: _ClassVar[int]
    GLOBALPAYMENTS_REVERSE_SALE_OR_REFUND_FIELD_NUMBER: _ClassVar[int]
    PAYSCOUT_CREDIT_SALE_FIELD_NUMBER: _ClassVar[int]
    PAYSCOUT_ECHECK_SALE_FIELD_NUMBER: _ClassVar[int]
    I2C_ECHO_FIELD_NUMBER: _ClassVar[int]
    I2C_BALANCE_INQUIRY_FIELD_NUMBER: _ClassVar[int]
    I2C_VERIFY_USER_FIELD_NUMBER: _ClassVar[int]
    I2C_SEARCH_CUSTOMER_FIELD_NUMBER: _ClassVar[int]
    I2C_MAKE_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    I2C_GET_CARDHOLDER_PROFILE_FIELD_NUMBER: _ClassVar[int]
    I2C_GET_CARDHOLDER_STATEMENT_FIELD_NUMBER: _ClassVar[int]
    I2C_GET_CARDHOLDER_BALANCE_FIELD_NUMBER: _ClassVar[int]
    I2C_GET_CREDITPAYMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    I2C_TRANSACTION_HISTORY_FIELD_NUMBER: _ClassVar[int]
    OPAYO_CC_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    SHIFT4_CC_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    POSCORP_ACCESSTOKEN_FIELD_NUMBER: _ClassVar[int]
    POSCORP_LOOKUP_GUARANTOR_FIELD_NUMBER: _ClassVar[int]
    POSCORP_UPDATE_PAYMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    PIANO_GET_USER_FIELD_NUMBER: _ClassVar[int]
    PIANO_UPDATE_USER_FIELD_NUMBER: _ClassVar[int]
    plugin_instance_id: str
    braintree_credit_sale: ExecuteBraintreeCreditSale
    braintree_bank_sale: ExecuteBraintreeBankSale
    relatient_get_patient_balance: ExecuteRelatientGetPatientBalance
    relatient_get_patient_cc_tokens: ExecuteRelatientGetPatientCcTokens
    relatient_post_patient_token: ExecuteRelatientPostPatientToken
    relatient_post_patient_balance: ExecuteRelatientPostPatientBalance
    relatient_get_patient: ExecuteRelatientGetPatient
    relatient_post_balance_by_id: ExecuteRelatientPostBalanceById
    relatient_create_fortis_achtoken: ExecuteRelatientCreateFortisAchtoken
    relatient_create_fortis_cctoken: ExecuteRelatientCreateFortisCctoken
    relatient_fortis_token_ach_debit_payment: ExecuteRelatientFortisTokenAchDebitPayment
    relatient_fortis_token_cc_payment: ExecuteRelatientFortisTokenCcPayment
    cybersource_credit_payment: ExecuteCybersourceCreditPayment
    cybersource_echeck_payment: ExecuteCybersourceEcheckPayment
    circpro_phone_lookup_with_bundle: ExecuteCircproPhoneLookupWithBundle
    circpro_phone_lookup: ExecuteCircproPhoneLookup
    circpro_vacation_restart_inquiry: ExecuteCircproVacationRestartInquiry
    circpro_complaint_inquiry: ExecuteCircproComplaintInquiry
    circpro_account_inquiry: ExecuteCircproAccountInquiry
    circpro_account_inquiry_with_tax: ExecuteCircproAccountInquiryWithTax
    circpro_account_inquiry_with_tax_bundle: ExecuteCircproAccountInquiryWithTaxBundle
    circpro_complaint_codes: ExecuteCircproComplaintCodes
    circpro_complaint_update: ExecuteCircproComplaintUpdate
    circpro_vacation_update: ExecuteCircproVacationUpdate
    circpro_restart_update: ExecuteCircproRestartUpdate
    circpro_law_immediate_payment: ExecuteCircproLawImmediatePayment
    circpro_law_update_data_with_pac: ExecuteCircproLawUpdateDataWithPac
    circpro_law_get_customers: ExecuteCircproLawGetCustomers
    authorizenet_charge_credit_card: ExecuteAuthorizenetChargeCreditCard
    authorizenet_debit_bank_account: ExecuteAuthorizenetDebitBankAccount
    authorizenet_create_customer_payment_profile: ExecuteAuthorizenetCreateCustomerPaymentProfile
    authorizenet_paypal_transaction: ExecuteAuthorizenetPaypalTransaction
    authorizenet_google_pay_transaction: ExecuteAuthorizenetGooglePayTransaction
    authorizenet_apple_pay_transaction: ExecuteAuthorizenetApplePayTransaction
    authorizenet_pay_pal_auth_capture: ExecuteAuthorizenetPayPalAuthCapture
    expitrans_cc_transaction: ExecuteExpitransCcTransaction
    expitrans_ach_transaction: ExecuteExpitransAchTransaction
    axiamedfusion_cc_transaction: ExecuteAxiamedfusionCcTransaction
    axiamedfusion_ach_transaction: ExecuteAxiamedfusionAchTransaction
    axiamedfusion_card_verify: ExecuteAxiamedfusionCardVerify
    instamed_payment_sale: ExecuteInstamedPaymentSale
    instamed_void_payment: ExecuteInstamedVoidPayment
    usaepay_submit_cc_payments: ExecuteUsaepaySubmitCcPayments
    usaepay_submit_ach_payments: ExecuteUsaepaySubmitAchPayments
    usaepay_get_cc_token: ExecuteUsaepayGetCcToken
    ezidebit_submit_cc_payments: ExecuteEzidebitSubmitCcPayments
    ezidebit_submit_ach_payments: ExecuteEzidebitSubmitAchPayments
    bambora_submit_cc_payments: ExecuteBamboraSubmitCcPayments
    bambora_submit_ach_payments: ExecuteBamboraSubmitAchPayments
    repay_store_card: ExecuteRepayStoreCard
    repay_payment_token: ExecuteRepayPaymentToken
    repay_ach_payment_token: ExecuteRepayAchPaymentToken
    axia_submit_sale_request_by_cc: ExecuteAxiaSubmitSaleRequestByCc
    axia_submit_sale_request_by_check: ExecuteAxiaSubmitSaleRequestByCheck
    securetrading_send_payment: ExecuteSecuretradingSendPayment
    payment_vision_submit_card_sale_request_by_cc: ExecutePaymentVisionSubmitCardSaleRequestByCc
    payment_vision_submit_card_sale_request_by_ach: ExecutePaymentVisionSubmitCardSaleRequestByAch
    interprose_lookup_account: ExecuteInterproseLookupAccount
    interprose_submit_card_sale_request_by_cc: ExecuteInterproseSubmitCardSaleRequestByCc
    interprose_submit_card_sale_request_by_ach: ExecuteInterproseSubmitCardSaleRequestByAch
    interprose_lookup_payment_id: ExecuteInterproseLookupPaymentId
    interprose_lookup_account_by_form_id: ExecuteInterproseLookupAccountByFormId
    dallasnews_search_by_phone: ExecuteDallasnewsSearchByPhone
    dallasnews_search_by_zip_street: ExecuteDallasnewsSearchByZipStreet
    dallasnews_search_by: ExecuteDallasnewsSearchBy
    dallasnews_create_vacation: ExecuteDallasnewsCreateVacation
    dallasnews_get_vacation: ExecuteDallasnewsGetVacation
    dallasnews_get_vacation_days_between: ExecuteDallasnewsGetVacationDaysBetween
    dallasnews_get_vacation_with_cutoff: ExecuteDallasnewsGetVacationWithCutoff
    dallasnews_delete_vacation: ExecuteDallasnewsDeleteVacation
    dallasnews_add_complaint: ExecuteDallasnewsAddComplaint
    dallasnews_update_phone_number: ExecuteDallasnewsUpdatePhoneNumber
    dallasnews_stop_account: ExecuteDallasnewsStopAccount
    dallasnews_cc_payment_token: ExecuteDallasnewsCcPaymentToken
    dallasnews_ach_payment_token: ExecuteDallasnewsAchPaymentToken
    payway_submit_card_sale_request: ExecutePaywaySubmitCardSaleRequest
    payway_create_token_request: ExecutePaywayCreateTokenRequest
    payway_submit_ach_sale_request: ExecutePaywaySubmitACHSaleRequest
    billingtree_submit_card_sale_request: ExecuteBillingtreeSubmitCardSaleRequest
    experian_cc_payment_request: ExecuteExperianCcPaymentRequest
    experian_cc_payment_plan_request: ExecuteExperianCcPaymentPlanRequest
    experian_balancerequest: ExecuteExperianBalancerequest
    experian_ach_payment_request: ExecuteExperianAchPaymentRequest
    experian_ach_payment_plan_request: ExecuteExperianAchPaymentPlanRequest
    experian_stella_card_entry: ExecuteExperianStellaCardEntry
    experian_stella_echeck: ExecuteExperianStellaECheck
    experian_stella_card_device_tokenization: ExecuteExperianStellaCardDeviceTokenization
    experian_stella_token_payment: ExecuteExperianStellaTokenPayment
    experian_stella_ach_tokenization: ExecuteExperianStellaAchTokenization
    experian_stella_add_usa_epay_token: ExecuteExperianStellaAddusaepaytoken
    experian_stella_payment_plans: ExecuteExperianStellaPaymentPlans
    experian_stella_auth: ExecuteExperianStellaAuth
    newscycle_login: ExecuteNewscycleLogin
    newscycle_search_page: ExecuteNewscycleSearchPage
    newscycle_billing_info: ExecuteNewscycleBillingInfo
    newscycle_service_error_info: ExecuteNewscycleServiceErrorInfo
    newscycle_service_error_trans: ExecuteNewscycleServiceErrorTrans
    newscycle_stop_info: ExecuteNewscycleStopInfo
    newscycle_stop_trans: ExecuteNewscycleStopTrans
    newscycle_renew_info: ExecuteNewscycleRenewInfo
    newscycle_auto_renew_info: ExecuteNewscycleAutoRenewInfo
    newscycle_auto_tran: ExecuteNewscycleAutoTran
    newscycle_pay_info: ExecuteNewscyclePayInfo
    newscycle_pay_tran: ExecuteNewscyclePayTran
    trustcommerce_credit_sale: ExecuteTrustcommerceCreditSale
    trustcommerce_ach_sale: ExecuteTrustcommerceAchSale
    vantiv_credit_sale: ExecuteVantivCreditSale
    vantiv_ach_sale: ExecuteVantivAchSale
    journey_latest: ExecuteJourneyLatest
    athenahealth_get_patients: ExecuteAthenahealthGetPatients
    athenahealth_get_patients_with_id: ExecuteAthenahealthGetPatientsWithId
    athenahealth_cc_payment: ExecuteAthenahealthCcPayment
    brainworks_get_customers_by_phone: ExecuteBrainworksGetCustomersByPhone
    brainworks_get_suspends: ExecuteBrainworksGetSuspends
    brainworks_get_customer_by_cust_id_v2: ExecuteBrainworksGetCustomerByCustIdV2
    brainworks_get_complaints: ExecuteBrainworksGetComplaints
    brainworks_get_codes_or_types: ExecuteBrainworksGetCodesOrTypes
    brainworks_stop_suspends: ExecuteBrainworksStopSuspends
    brainworks_start_suspends: ExecuteBrainworksStartSuspends
    brainworks_send_complaint: ExecuteBrainworksSendComplaint
    brainworks_get_customer_by_cust_id: ExecuteBrainworksGetCustomerByCustId
    osgconnect_cc_payments: ExecuteOsgconnectCcPayments
    osgconnect_ach_payments: ExecuteOsgconnectAchPayments
    osgconnect_validate_account_no: ExecuteOsgconnectValidateAccountNo
    ntvb_credit_missed_delivery: ExecuteNtvbCreditMissedDelivery
    ntvb_customer_search: ExecuteNtvbCustomerSearch
    ntvb_end_call: ExecuteNtvbEndCall
    ntvb_integration_definition: ExecuteNtvbIntegrationDefinition
    ntvb_missed_delivery: ExecuteNtvbMissedDelivery
    ntvb_remove_autorenewal: ExecuteNtvbRemoveAutorenewal
    ntvb_renew_subscription: ExecuteNtvbRenewSubscription
    ntvb_renewal_offers: ExecuteNtvbRenewalOffers
    ntvb_set_autorenewal: ExecuteNtvbSetAutorenewal
    ntvb_start_incoming_call: ExecuteNtvbStartIncomingCall
    ntvb_start_outgoing_call: ExecuteNtvbStartOutgoingCall
    ntvb_subscription_info: ExecuteNtvbSubscriptionInfo
    ntvb_vacation_stop: ExecuteNtvbVacationStop
    ntvb_authtest: ExecuteNtvbAuthtest
    elavon_credit_card_sale: ExecuteElavonCreditCardSale
    elavon_add_recurring: ExecuteElavonAddRecurring
    elavon_dcc_response: ExecuteElavonDccResponse
    elavon_delete_recurring: ExecuteElavonDeleteRecurring
    elavon_update_recurring: ExecuteElavonUpdateRecurring
    elavon_health_care_cc_sale: ExecuteElavonHealthCareCCSale
    elavon_add_installment: ExecuteElavonAddInstallment
    elavon_update_installment: ExecuteElavonUpdateInstallment
    elavon_delete_installment: ExecuteElavonDeleteInstallment
    elavon_mcc_credit_card_sale: ExecuteElavonMccCreditCardSale
    globalPayments_card_sale: ExecuteGlobalPaymentsCardSale
    globalPayments_get_transaction_by_id: ExecuteGlobalPaymentsGetTransactionByID
    globalPayments_list_transactions: ExecuteGlobalPaymentsListTransactions
    globalPayments_refund_sale: ExecuteGlobalPaymentsRefundSale
    globalPayments_reverse_sale_or_refund: ExecuteGlobalPaymentsReverseSaleOrRefund
    payscout_credit_sale: ExecutePayScoutCreditCardSale
    payscout_echeck_sale: ExecutePayScoutEcheckSale
    i2c_echo: ExecuteI2cEcho
    i2c_balance_inquiry: ExecuteI2cBalanceInquiry
    i2c_verify_user: ExecuteI2cVerifyUser
    i2c_search_customer: ExecuteI2cSearchCustomer
    i2c_make_payment: ExecuteI2cMakePayment
    i2c_get_cardholder_profile: ExecuteI2cGetCardholderProfile
    i2c_get_cardholder_statement: ExecuteI2cGetCardholderStatement
    i2c_get_cardholder_balance: ExecuteI2cGetCardholderBalance
    i2c_get_creditpayment_info: ExecuteI2cGetCreditPaymentInfo
    i2c_transaction_history: ExecuteI2cTransactionHistory
    opayo_cc_payment: ExecuteOpayoCcPayments
    shift4_cc_payment: ExecuteShift4CcPayments
    poscorp_accesstoken: ExecutePoscorpAccesstoken
    poscorp_lookup_guarantor: ExecutePoscorpLookupGuarantor
    poscorp_update_payment_status: ExecutePoscorpUpdatePaymentStatus
    PIANO_GET_USER: ExecutePianoGetUser
    PIANO_UPDATE_USER: ExecutePianoUpdateUser
    def __init__(self, plugin_instance_id: _Optional[str] = ..., braintree_credit_sale: _Optional[_Union[ExecuteBraintreeCreditSale, _Mapping]] = ..., braintree_bank_sale: _Optional[_Union[ExecuteBraintreeBankSale, _Mapping]] = ..., relatient_get_patient_balance: _Optional[_Union[ExecuteRelatientGetPatientBalance, _Mapping]] = ..., relatient_get_patient_cc_tokens: _Optional[_Union[ExecuteRelatientGetPatientCcTokens, _Mapping]] = ..., relatient_post_patient_token: _Optional[_Union[ExecuteRelatientPostPatientToken, _Mapping]] = ..., relatient_post_patient_balance: _Optional[_Union[ExecuteRelatientPostPatientBalance, _Mapping]] = ..., relatient_get_patient: _Optional[_Union[ExecuteRelatientGetPatient, _Mapping]] = ..., relatient_post_balance_by_id: _Optional[_Union[ExecuteRelatientPostBalanceById, _Mapping]] = ..., relatient_create_fortis_achtoken: _Optional[_Union[ExecuteRelatientCreateFortisAchtoken, _Mapping]] = ..., relatient_create_fortis_cctoken: _Optional[_Union[ExecuteRelatientCreateFortisCctoken, _Mapping]] = ..., relatient_fortis_token_ach_debit_payment: _Optional[_Union[ExecuteRelatientFortisTokenAchDebitPayment, _Mapping]] = ..., relatient_fortis_token_cc_payment: _Optional[_Union[ExecuteRelatientFortisTokenCcPayment, _Mapping]] = ..., cybersource_credit_payment: _Optional[_Union[ExecuteCybersourceCreditPayment, _Mapping]] = ..., cybersource_echeck_payment: _Optional[_Union[ExecuteCybersourceEcheckPayment, _Mapping]] = ..., circpro_phone_lookup_with_bundle: _Optional[_Union[ExecuteCircproPhoneLookupWithBundle, _Mapping]] = ..., circpro_phone_lookup: _Optional[_Union[ExecuteCircproPhoneLookup, _Mapping]] = ..., circpro_vacation_restart_inquiry: _Optional[_Union[ExecuteCircproVacationRestartInquiry, _Mapping]] = ..., circpro_complaint_inquiry: _Optional[_Union[ExecuteCircproComplaintInquiry, _Mapping]] = ..., circpro_account_inquiry: _Optional[_Union[ExecuteCircproAccountInquiry, _Mapping]] = ..., circpro_account_inquiry_with_tax: _Optional[_Union[ExecuteCircproAccountInquiryWithTax, _Mapping]] = ..., circpro_account_inquiry_with_tax_bundle: _Optional[_Union[ExecuteCircproAccountInquiryWithTaxBundle, _Mapping]] = ..., circpro_complaint_codes: _Optional[_Union[ExecuteCircproComplaintCodes, _Mapping]] = ..., circpro_complaint_update: _Optional[_Union[ExecuteCircproComplaintUpdate, _Mapping]] = ..., circpro_vacation_update: _Optional[_Union[ExecuteCircproVacationUpdate, _Mapping]] = ..., circpro_restart_update: _Optional[_Union[ExecuteCircproRestartUpdate, _Mapping]] = ..., circpro_law_immediate_payment: _Optional[_Union[ExecuteCircproLawImmediatePayment, _Mapping]] = ..., circpro_law_update_data_with_pac: _Optional[_Union[ExecuteCircproLawUpdateDataWithPac, _Mapping]] = ..., circpro_law_get_customers: _Optional[_Union[ExecuteCircproLawGetCustomers, _Mapping]] = ..., authorizenet_charge_credit_card: _Optional[_Union[ExecuteAuthorizenetChargeCreditCard, _Mapping]] = ..., authorizenet_debit_bank_account: _Optional[_Union[ExecuteAuthorizenetDebitBankAccount, _Mapping]] = ..., authorizenet_create_customer_payment_profile: _Optional[_Union[ExecuteAuthorizenetCreateCustomerPaymentProfile, _Mapping]] = ..., authorizenet_paypal_transaction: _Optional[_Union[ExecuteAuthorizenetPaypalTransaction, _Mapping]] = ..., authorizenet_google_pay_transaction: _Optional[_Union[ExecuteAuthorizenetGooglePayTransaction, _Mapping]] = ..., authorizenet_apple_pay_transaction: _Optional[_Union[ExecuteAuthorizenetApplePayTransaction, _Mapping]] = ..., authorizenet_pay_pal_auth_capture: _Optional[_Union[ExecuteAuthorizenetPayPalAuthCapture, _Mapping]] = ..., expitrans_cc_transaction: _Optional[_Union[ExecuteExpitransCcTransaction, _Mapping]] = ..., expitrans_ach_transaction: _Optional[_Union[ExecuteExpitransAchTransaction, _Mapping]] = ..., axiamedfusion_cc_transaction: _Optional[_Union[ExecuteAxiamedfusionCcTransaction, _Mapping]] = ..., axiamedfusion_ach_transaction: _Optional[_Union[ExecuteAxiamedfusionAchTransaction, _Mapping]] = ..., axiamedfusion_card_verify: _Optional[_Union[ExecuteAxiamedfusionCardVerify, _Mapping]] = ..., instamed_payment_sale: _Optional[_Union[ExecuteInstamedPaymentSale, _Mapping]] = ..., instamed_void_payment: _Optional[_Union[ExecuteInstamedVoidPayment, _Mapping]] = ..., usaepay_submit_cc_payments: _Optional[_Union[ExecuteUsaepaySubmitCcPayments, _Mapping]] = ..., usaepay_submit_ach_payments: _Optional[_Union[ExecuteUsaepaySubmitAchPayments, _Mapping]] = ..., usaepay_get_cc_token: _Optional[_Union[ExecuteUsaepayGetCcToken, _Mapping]] = ..., ezidebit_submit_cc_payments: _Optional[_Union[ExecuteEzidebitSubmitCcPayments, _Mapping]] = ..., ezidebit_submit_ach_payments: _Optional[_Union[ExecuteEzidebitSubmitAchPayments, _Mapping]] = ..., bambora_submit_cc_payments: _Optional[_Union[ExecuteBamboraSubmitCcPayments, _Mapping]] = ..., bambora_submit_ach_payments: _Optional[_Union[ExecuteBamboraSubmitAchPayments, _Mapping]] = ..., repay_store_card: _Optional[_Union[ExecuteRepayStoreCard, _Mapping]] = ..., repay_payment_token: _Optional[_Union[ExecuteRepayPaymentToken, _Mapping]] = ..., repay_ach_payment_token: _Optional[_Union[ExecuteRepayAchPaymentToken, _Mapping]] = ..., axia_submit_sale_request_by_cc: _Optional[_Union[ExecuteAxiaSubmitSaleRequestByCc, _Mapping]] = ..., axia_submit_sale_request_by_check: _Optional[_Union[ExecuteAxiaSubmitSaleRequestByCheck, _Mapping]] = ..., securetrading_send_payment: _Optional[_Union[ExecuteSecuretradingSendPayment, _Mapping]] = ..., payment_vision_submit_card_sale_request_by_cc: _Optional[_Union[ExecutePaymentVisionSubmitCardSaleRequestByCc, _Mapping]] = ..., payment_vision_submit_card_sale_request_by_ach: _Optional[_Union[ExecutePaymentVisionSubmitCardSaleRequestByAch, _Mapping]] = ..., interprose_lookup_account: _Optional[_Union[ExecuteInterproseLookupAccount, _Mapping]] = ..., interprose_submit_card_sale_request_by_cc: _Optional[_Union[ExecuteInterproseSubmitCardSaleRequestByCc, _Mapping]] = ..., interprose_submit_card_sale_request_by_ach: _Optional[_Union[ExecuteInterproseSubmitCardSaleRequestByAch, _Mapping]] = ..., interprose_lookup_payment_id: _Optional[_Union[ExecuteInterproseLookupPaymentId, _Mapping]] = ..., interprose_lookup_account_by_form_id: _Optional[_Union[ExecuteInterproseLookupAccountByFormId, _Mapping]] = ..., dallasnews_search_by_phone: _Optional[_Union[ExecuteDallasnewsSearchByPhone, _Mapping]] = ..., dallasnews_search_by_zip_street: _Optional[_Union[ExecuteDallasnewsSearchByZipStreet, _Mapping]] = ..., dallasnews_search_by: _Optional[_Union[ExecuteDallasnewsSearchBy, _Mapping]] = ..., dallasnews_create_vacation: _Optional[_Union[ExecuteDallasnewsCreateVacation, _Mapping]] = ..., dallasnews_get_vacation: _Optional[_Union[ExecuteDallasnewsGetVacation, _Mapping]] = ..., dallasnews_get_vacation_days_between: _Optional[_Union[ExecuteDallasnewsGetVacationDaysBetween, _Mapping]] = ..., dallasnews_get_vacation_with_cutoff: _Optional[_Union[ExecuteDallasnewsGetVacationWithCutoff, _Mapping]] = ..., dallasnews_delete_vacation: _Optional[_Union[ExecuteDallasnewsDeleteVacation, _Mapping]] = ..., dallasnews_add_complaint: _Optional[_Union[ExecuteDallasnewsAddComplaint, _Mapping]] = ..., dallasnews_update_phone_number: _Optional[_Union[ExecuteDallasnewsUpdatePhoneNumber, _Mapping]] = ..., dallasnews_stop_account: _Optional[_Union[ExecuteDallasnewsStopAccount, _Mapping]] = ..., dallasnews_cc_payment_token: _Optional[_Union[ExecuteDallasnewsCcPaymentToken, _Mapping]] = ..., dallasnews_ach_payment_token: _Optional[_Union[ExecuteDallasnewsAchPaymentToken, _Mapping]] = ..., payway_submit_card_sale_request: _Optional[_Union[ExecutePaywaySubmitCardSaleRequest, _Mapping]] = ..., payway_create_token_request: _Optional[_Union[ExecutePaywayCreateTokenRequest, _Mapping]] = ..., payway_submit_ach_sale_request: _Optional[_Union[ExecutePaywaySubmitACHSaleRequest, _Mapping]] = ..., billingtree_submit_card_sale_request: _Optional[_Union[ExecuteBillingtreeSubmitCardSaleRequest, _Mapping]] = ..., experian_cc_payment_request: _Optional[_Union[ExecuteExperianCcPaymentRequest, _Mapping]] = ..., experian_cc_payment_plan_request: _Optional[_Union[ExecuteExperianCcPaymentPlanRequest, _Mapping]] = ..., experian_balancerequest: _Optional[_Union[ExecuteExperianBalancerequest, _Mapping]] = ..., experian_ach_payment_request: _Optional[_Union[ExecuteExperianAchPaymentRequest, _Mapping]] = ..., experian_ach_payment_plan_request: _Optional[_Union[ExecuteExperianAchPaymentPlanRequest, _Mapping]] = ..., experian_stella_card_entry: _Optional[_Union[ExecuteExperianStellaCardEntry, _Mapping]] = ..., experian_stella_echeck: _Optional[_Union[ExecuteExperianStellaECheck, _Mapping]] = ..., experian_stella_card_device_tokenization: _Optional[_Union[ExecuteExperianStellaCardDeviceTokenization, _Mapping]] = ..., experian_stella_token_payment: _Optional[_Union[ExecuteExperianStellaTokenPayment, _Mapping]] = ..., experian_stella_ach_tokenization: _Optional[_Union[ExecuteExperianStellaAchTokenization, _Mapping]] = ..., experian_stella_add_usa_epay_token: _Optional[_Union[ExecuteExperianStellaAddusaepaytoken, _Mapping]] = ..., experian_stella_payment_plans: _Optional[_Union[ExecuteExperianStellaPaymentPlans, _Mapping]] = ..., experian_stella_auth: _Optional[_Union[ExecuteExperianStellaAuth, _Mapping]] = ..., newscycle_login: _Optional[_Union[ExecuteNewscycleLogin, _Mapping]] = ..., newscycle_search_page: _Optional[_Union[ExecuteNewscycleSearchPage, _Mapping]] = ..., newscycle_billing_info: _Optional[_Union[ExecuteNewscycleBillingInfo, _Mapping]] = ..., newscycle_service_error_info: _Optional[_Union[ExecuteNewscycleServiceErrorInfo, _Mapping]] = ..., newscycle_service_error_trans: _Optional[_Union[ExecuteNewscycleServiceErrorTrans, _Mapping]] = ..., newscycle_stop_info: _Optional[_Union[ExecuteNewscycleStopInfo, _Mapping]] = ..., newscycle_stop_trans: _Optional[_Union[ExecuteNewscycleStopTrans, _Mapping]] = ..., newscycle_renew_info: _Optional[_Union[ExecuteNewscycleRenewInfo, _Mapping]] = ..., newscycle_auto_renew_info: _Optional[_Union[ExecuteNewscycleAutoRenewInfo, _Mapping]] = ..., newscycle_auto_tran: _Optional[_Union[ExecuteNewscycleAutoTran, _Mapping]] = ..., newscycle_pay_info: _Optional[_Union[ExecuteNewscyclePayInfo, _Mapping]] = ..., newscycle_pay_tran: _Optional[_Union[ExecuteNewscyclePayTran, _Mapping]] = ..., trustcommerce_credit_sale: _Optional[_Union[ExecuteTrustcommerceCreditSale, _Mapping]] = ..., trustcommerce_ach_sale: _Optional[_Union[ExecuteTrustcommerceAchSale, _Mapping]] = ..., vantiv_credit_sale: _Optional[_Union[ExecuteVantivCreditSale, _Mapping]] = ..., vantiv_ach_sale: _Optional[_Union[ExecuteVantivAchSale, _Mapping]] = ..., journey_latest: _Optional[_Union[ExecuteJourneyLatest, _Mapping]] = ..., athenahealth_get_patients: _Optional[_Union[ExecuteAthenahealthGetPatients, _Mapping]] = ..., athenahealth_get_patients_with_id: _Optional[_Union[ExecuteAthenahealthGetPatientsWithId, _Mapping]] = ..., athenahealth_cc_payment: _Optional[_Union[ExecuteAthenahealthCcPayment, _Mapping]] = ..., brainworks_get_customers_by_phone: _Optional[_Union[ExecuteBrainworksGetCustomersByPhone, _Mapping]] = ..., brainworks_get_suspends: _Optional[_Union[ExecuteBrainworksGetSuspends, _Mapping]] = ..., brainworks_get_customer_by_cust_id_v2: _Optional[_Union[ExecuteBrainworksGetCustomerByCustIdV2, _Mapping]] = ..., brainworks_get_complaints: _Optional[_Union[ExecuteBrainworksGetComplaints, _Mapping]] = ..., brainworks_get_codes_or_types: _Optional[_Union[ExecuteBrainworksGetCodesOrTypes, _Mapping]] = ..., brainworks_stop_suspends: _Optional[_Union[ExecuteBrainworksStopSuspends, _Mapping]] = ..., brainworks_start_suspends: _Optional[_Union[ExecuteBrainworksStartSuspends, _Mapping]] = ..., brainworks_send_complaint: _Optional[_Union[ExecuteBrainworksSendComplaint, _Mapping]] = ..., brainworks_get_customer_by_cust_id: _Optional[_Union[ExecuteBrainworksGetCustomerByCustId, _Mapping]] = ..., osgconnect_cc_payments: _Optional[_Union[ExecuteOsgconnectCcPayments, _Mapping]] = ..., osgconnect_ach_payments: _Optional[_Union[ExecuteOsgconnectAchPayments, _Mapping]] = ..., osgconnect_validate_account_no: _Optional[_Union[ExecuteOsgconnectValidateAccountNo, _Mapping]] = ..., ntvb_credit_missed_delivery: _Optional[_Union[ExecuteNtvbCreditMissedDelivery, _Mapping]] = ..., ntvb_customer_search: _Optional[_Union[ExecuteNtvbCustomerSearch, _Mapping]] = ..., ntvb_end_call: _Optional[_Union[ExecuteNtvbEndCall, _Mapping]] = ..., ntvb_integration_definition: _Optional[_Union[ExecuteNtvbIntegrationDefinition, _Mapping]] = ..., ntvb_missed_delivery: _Optional[_Union[ExecuteNtvbMissedDelivery, _Mapping]] = ..., ntvb_remove_autorenewal: _Optional[_Union[ExecuteNtvbRemoveAutorenewal, _Mapping]] = ..., ntvb_renew_subscription: _Optional[_Union[ExecuteNtvbRenewSubscription, _Mapping]] = ..., ntvb_renewal_offers: _Optional[_Union[ExecuteNtvbRenewalOffers, _Mapping]] = ..., ntvb_set_autorenewal: _Optional[_Union[ExecuteNtvbSetAutorenewal, _Mapping]] = ..., ntvb_start_incoming_call: _Optional[_Union[ExecuteNtvbStartIncomingCall, _Mapping]] = ..., ntvb_start_outgoing_call: _Optional[_Union[ExecuteNtvbStartOutgoingCall, _Mapping]] = ..., ntvb_subscription_info: _Optional[_Union[ExecuteNtvbSubscriptionInfo, _Mapping]] = ..., ntvb_vacation_stop: _Optional[_Union[ExecuteNtvbVacationStop, _Mapping]] = ..., ntvb_authtest: _Optional[_Union[ExecuteNtvbAuthtest, _Mapping]] = ..., elavon_credit_card_sale: _Optional[_Union[ExecuteElavonCreditCardSale, _Mapping]] = ..., elavon_add_recurring: _Optional[_Union[ExecuteElavonAddRecurring, _Mapping]] = ..., elavon_dcc_response: _Optional[_Union[ExecuteElavonDccResponse, _Mapping]] = ..., elavon_delete_recurring: _Optional[_Union[ExecuteElavonDeleteRecurring, _Mapping]] = ..., elavon_update_recurring: _Optional[_Union[ExecuteElavonUpdateRecurring, _Mapping]] = ..., elavon_health_care_cc_sale: _Optional[_Union[ExecuteElavonHealthCareCCSale, _Mapping]] = ..., elavon_add_installment: _Optional[_Union[ExecuteElavonAddInstallment, _Mapping]] = ..., elavon_update_installment: _Optional[_Union[ExecuteElavonUpdateInstallment, _Mapping]] = ..., elavon_delete_installment: _Optional[_Union[ExecuteElavonDeleteInstallment, _Mapping]] = ..., elavon_mcc_credit_card_sale: _Optional[_Union[ExecuteElavonMccCreditCardSale, _Mapping]] = ..., globalPayments_card_sale: _Optional[_Union[ExecuteGlobalPaymentsCardSale, _Mapping]] = ..., globalPayments_get_transaction_by_id: _Optional[_Union[ExecuteGlobalPaymentsGetTransactionByID, _Mapping]] = ..., globalPayments_list_transactions: _Optional[_Union[ExecuteGlobalPaymentsListTransactions, _Mapping]] = ..., globalPayments_refund_sale: _Optional[_Union[ExecuteGlobalPaymentsRefundSale, _Mapping]] = ..., globalPayments_reverse_sale_or_refund: _Optional[_Union[ExecuteGlobalPaymentsReverseSaleOrRefund, _Mapping]] = ..., payscout_credit_sale: _Optional[_Union[ExecutePayScoutCreditCardSale, _Mapping]] = ..., payscout_echeck_sale: _Optional[_Union[ExecutePayScoutEcheckSale, _Mapping]] = ..., i2c_echo: _Optional[_Union[ExecuteI2cEcho, _Mapping]] = ..., i2c_balance_inquiry: _Optional[_Union[ExecuteI2cBalanceInquiry, _Mapping]] = ..., i2c_verify_user: _Optional[_Union[ExecuteI2cVerifyUser, _Mapping]] = ..., i2c_search_customer: _Optional[_Union[ExecuteI2cSearchCustomer, _Mapping]] = ..., i2c_make_payment: _Optional[_Union[ExecuteI2cMakePayment, _Mapping]] = ..., i2c_get_cardholder_profile: _Optional[_Union[ExecuteI2cGetCardholderProfile, _Mapping]] = ..., i2c_get_cardholder_statement: _Optional[_Union[ExecuteI2cGetCardholderStatement, _Mapping]] = ..., i2c_get_cardholder_balance: _Optional[_Union[ExecuteI2cGetCardholderBalance, _Mapping]] = ..., i2c_get_creditpayment_info: _Optional[_Union[ExecuteI2cGetCreditPaymentInfo, _Mapping]] = ..., i2c_transaction_history: _Optional[_Union[ExecuteI2cTransactionHistory, _Mapping]] = ..., opayo_cc_payment: _Optional[_Union[ExecuteOpayoCcPayments, _Mapping]] = ..., shift4_cc_payment: _Optional[_Union[ExecuteShift4CcPayments, _Mapping]] = ..., poscorp_accesstoken: _Optional[_Union[ExecutePoscorpAccesstoken, _Mapping]] = ..., poscorp_lookup_guarantor: _Optional[_Union[ExecutePoscorpLookupGuarantor, _Mapping]] = ..., poscorp_update_payment_status: _Optional[_Union[ExecutePoscorpUpdatePaymentStatus, _Mapping]] = ..., PIANO_GET_USER: _Optional[_Union[ExecutePianoGetUser, _Mapping]] = ..., PIANO_UPDATE_USER: _Optional[_Union[ExecutePianoUpdateUser, _Mapping]] = ...) -> None: ...

class InvoiceExperianQueryBalance(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InvoiceAuthorizeNetAuthorizedTransactionIdLookup(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InvoiceAuthorizeNetLinkData(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InvoiceAuthorizeNetCustomHttp(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InvoiceJourney(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class InvoiceDynamicJourney(_message.Message):
    __slots__ = ["match_fields", "total_field", "journey_fields"]
    class JourneyFieldsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ListOfStrings
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ListOfStrings, _Mapping]] = ...) -> None: ...
    MATCH_FIELDS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_FIELD_NUMBER: _ClassVar[int]
    JOURNEY_FIELDS_FIELD_NUMBER: _ClassVar[int]
    match_fields: _containers.RepeatedScalarFieldContainer[str]
    total_field: str
    journey_fields: _containers.MessageMap[str, ListOfStrings]
    def __init__(self, match_fields: _Optional[_Iterable[str]] = ..., total_field: _Optional[str] = ..., journey_fields: _Optional[_Mapping[str, ListOfStrings]] = ...) -> None: ...

class VerificationExperianQueryBalance(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VerificationExperianLinkData(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VerificationExperianZipDob(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VerificationAuthorizeNetCustomerProfile(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VerificationAuthorizeNetLinkData(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class VerificationJourney(_message.Message):
    __slots__ = ["date_of_birth_field", "last_name_field", "first_name_field", "zip_field", "last4_ssn"]
    DATE_OF_BIRTH_FIELD_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_FIELD_NUMBER: _ClassVar[int]
    LAST4_SSN_FIELD_NUMBER: _ClassVar[int]
    date_of_birth_field: str
    last_name_field: str
    first_name_field: str
    zip_field: str
    last4_ssn: str
    def __init__(self, date_of_birth_field: _Optional[str] = ..., last_name_field: _Optional[str] = ..., first_name_field: _Optional[str] = ..., zip_field: _Optional[str] = ..., last4_ssn: _Optional[str] = ...) -> None: ...

class PaymentExperianCC(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PaymentExperianACH(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PaymentAuthorizeNetCC(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PaymentAuthorizeNetACH(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PaymentAuthorizeNetPaypal(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PaymentAuthorizeNetApplePay(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PaymentAuthorizeNetGooglePay(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PaymentPaywaySubmitCardSaleRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PaymentPaywaySubmitACHAlertRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBraintreeCreditSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBraintreeBankSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRelatientGetPatientBalance(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRelatientGetPatientCcTokens(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRelatientPostPatientToken(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRelatientPostPatientBalance(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRelatientGetPatient(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRelatientPostBalanceById(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRelatientCreateFortisAchtoken(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRelatientCreateFortisCctoken(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRelatientFortisTokenAchDebitPayment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRelatientFortisTokenCcPayment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCybersourceCreditPayment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCybersourceEcheckPayment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproPhoneLookupWithBundle(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproPhoneLookup(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproVacationRestartInquiry(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproComplaintInquiry(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproAccountInquiry(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproAccountInquiryWithTax(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproAccountInquiryWithTaxBundle(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproComplaintCodes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproComplaintUpdate(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproVacationUpdate(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproRestartUpdate(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproLawImmediatePayment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproLawUpdateDataWithPac(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteCircproLawGetCustomers(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAuthorizenetChargeCreditCard(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAuthorizenetDebitBankAccount(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAuthorizenetCreateCustomerPaymentProfile(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAuthorizenetPaypalTransaction(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAuthorizenetGooglePayTransaction(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAuthorizenetApplePayTransaction(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAuthorizenetPayPalAuthCapture(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExpitransCcTransaction(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExpitransAchTransaction(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAxiamedfusionCcTransaction(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAxiamedfusionAchTransaction(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAxiamedfusionCardVerify(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteInstamedPaymentSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteInstamedVoidPayment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteUsaepaySubmitCcPayments(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteUsaepaySubmitAchPayments(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteUsaepayGetCcToken(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteEzidebitSubmitCcPayments(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteEzidebitSubmitAchPayments(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBamboraSubmitCcPayments(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBamboraSubmitAchPayments(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRepayStoreCard(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRepayPaymentToken(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteRepayAchPaymentToken(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAxiaSubmitSaleRequestByCc(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAxiaSubmitSaleRequestByCheck(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteSecuretradingSendPayment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePaymentVisionSubmitCardSaleRequestByCc(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePaymentVisionSubmitCardSaleRequestByAch(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteInterproseLookupAccount(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteInterproseSubmitCardSaleRequestByCc(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteInterproseSubmitCardSaleRequestByAch(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteInterproseLookupPaymentId(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteInterproseLookupAccountByFormId(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsSearchByPhone(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsSearchByZipStreet(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsSearchBy(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsCreateVacation(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsGetVacation(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsGetVacationDaysBetween(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsGetVacationWithCutoff(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsDeleteVacation(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsAddComplaint(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsUpdatePhoneNumber(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsStopAccount(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsCcPaymentToken(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteDallasnewsAchPaymentToken(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePaywaySubmitCardSaleRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePaywayCreateTokenRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePaywaySubmitACHSaleRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBillingtreeSubmitCardSaleRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianCcPaymentRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianCcPaymentPlanRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianBalancerequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianAchPaymentRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianAchPaymentPlanRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianStellaCardEntry(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianStellaECheck(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianStellaCardDeviceTokenization(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianStellaTokenPayment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianStellaAchTokenization(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianStellaAddusaepaytoken(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianStellaPaymentPlans(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteExperianStellaAuth(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscycleLogin(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscycleSearchPage(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscycleBillingInfo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscycleServiceErrorInfo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscycleServiceErrorTrans(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscycleStopInfo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscycleStopTrans(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscycleRenewInfo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscycleAutoRenewInfo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscycleAutoTran(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscyclePayInfo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNewscyclePayTran(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteTrustcommerceCreditSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteTrustcommerceAchSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteVantivCreditSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteVantivAchSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteJourneyLatest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAthenahealthGetPatients(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAthenahealthGetPatientsWithId(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteAthenahealthCcPayment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBrainworksGetCustomersByPhone(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBrainworksGetSuspends(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBrainworksGetCustomerByCustIdV2(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBrainworksGetComplaints(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBrainworksGetCodesOrTypes(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBrainworksStopSuspends(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBrainworksStartSuspends(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBrainworksSendComplaint(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteBrainworksGetCustomerByCustId(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteOsgconnectCcPayments(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteOsgconnectAchPayments(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteOsgconnectValidateAccountNo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbCreditMissedDelivery(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbCustomerSearch(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbEndCall(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbIntegrationDefinition(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbMissedDelivery(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbRemoveAutorenewal(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbRenewSubscription(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbRenewalOffers(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbSetAutorenewal(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbStartIncomingCall(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbStartOutgoingCall(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbSubscriptionInfo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbVacationStop(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteNtvbAuthtest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteElavonCreditCardSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteElavonAddRecurring(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteElavonDccResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteElavonUpdateRecurring(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteElavonDeleteRecurring(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteElavonMccCreditCardSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteElavonHealthCareCCSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteElavonAddInstallment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteElavonDeleteInstallment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteElavonUpdateInstallment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteGlobalPaymentsCardSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteGlobalPaymentsGetTransactionByID(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteGlobalPaymentsListTransactions(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteGlobalPaymentsRefundSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteGlobalPaymentsReverseSaleOrRefund(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePayScoutCreditCardSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePayScoutEcheckSale(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteI2cEcho(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteI2cBalanceInquiry(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteI2cVerifyUser(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteI2cSearchCustomer(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteI2cMakePayment(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteI2cGetCardholderProfile(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteI2cGetCardholderStatement(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteI2cGetCardholderBalance(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteI2cGetCreditPaymentInfo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteI2cTransactionHistory(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteOpayoCcPayments(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecuteShift4CcPayments(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePoscorpAccesstoken(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePoscorpLookupGuarantor(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePoscorpUpdatePaymentStatus(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePianoGetUser(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ExecutePianoUpdateUser(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...