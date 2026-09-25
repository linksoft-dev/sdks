import datetime

from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.vendas.pedido import pedido_pb2 as _pedido_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransactionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSACTION_STATUS_UNSPECIFIED: _ClassVar[TransactionStatus]
    TRANSACTION_STATUS_AUTHORIZED: _ClassVar[TransactionStatus]
    TRANSACTION_STATUS_PENDING: _ClassVar[TransactionStatus]
    TRANSACTION_STATUS_FAIL: _ClassVar[TransactionStatus]
    TRANSACTION_STATUS_CANCELLED: _ClassVar[TransactionStatus]
    TRANSACTION_STATUS_REFUNDED: _ClassVar[TransactionStatus]
    TRANSACTION_STATUS_PENDING_ANTIFRAUD: _ClassVar[TransactionStatus]
    TRANSACTION_STATUS_PENDING_MANUAL_REVIEW: _ClassVar[TransactionStatus]

class TransactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRANSACTION_TYPE_UNSPECIFIED: _ClassVar[TransactionType]
    TRANSACTION_TYPE_CARD: _ClassVar[TransactionType]
    TRANSACTION_TYPE_BOLETO: _ClassVar[TransactionType]
    TRANSACTION_TYPE_PIX: _ClassVar[TransactionType]

class Gateway(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GATEWAY_UNSPECIFIED: _ClassVar[Gateway]
    GATEWAY_PAGHIPER: _ClassVar[Gateway]
    GATEWAY_PAGARME: _ClassVar[Gateway]
    GATEWAY_MERCADOPAGO: _ClassVar[Gateway]
    GATEWAY_BRAZILPAYS: _ClassVar[Gateway]
    GATEWAY_GERENCIANET: _ClassVar[Gateway]
    GATEWAY_CIELO: _ClassVar[Gateway]
    GATEWAY_SICREDI: _ClassVar[Gateway]
    GATEWAY_STRIPE: _ClassVar[Gateway]
    GATEWAY_ASAAS: _ClassVar[Gateway]
    GATEWAY_BB: _ClassVar[Gateway]
    GATEWAY_BANCO_CORA: _ClassVar[Gateway]
    GATEWAY_BRADESCO: _ClassVar[Gateway]
    GATEWAY_C6BANK: _ClassVar[Gateway]
    GATEWAY_TRANSFEERA: _ClassVar[Gateway]
    GATEWAY_SICOOB: _ClassVar[Gateway]
    GATEWAY_INTER: _ClassVar[Gateway]
    GATEWAY_REDE: _ClassVar[Gateway]

class ReportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_TYPE_UNSPECIFIED: _ClassVar[ReportType]
    REPORT_TYPE_LIST: _ClassVar[ReportType]

class Currency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURRENCY_UNSPECIFIED: _ClassVar[Currency]
    CURRENCY_BRL: _ClassVar[Currency]
    CURRENCY_USD: _ClassVar[Currency]
    CURRENCY_EUR: _ClassVar[Currency]
    CURRENCY_GBP: _ClassVar[Currency]

class SyncTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYNC_TRIGGER_UNSPECIFIED: _ClassVar[SyncTrigger]
    SYNC_TRIGGER_MANUAL: _ClassVar[SyncTrigger]
    SYNC_TRIGGER_WEBHOOK: _ClassVar[SyncTrigger]
    SYNC_TRIGGER_SYSTEM: _ClassVar[SyncTrigger]
    SYNC_TRIGGER_ANTIFRAUD: _ClassVar[SyncTrigger]
    SYNC_TRIGGER_MANUAL_REVIEW: _ClassVar[SyncTrigger]

class FraudDecisionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FRAUD_DECISION_STATUS_UNSPECIFIED: _ClassVar[FraudDecisionStatus]
    FRAUD_DECISION_STATUS_APPROVED: _ClassVar[FraudDecisionStatus]
    FRAUD_DECISION_STATUS_DENIED: _ClassVar[FraudDecisionStatus]
    FRAUD_DECISION_STATUS_REVIEW: _ClassVar[FraudDecisionStatus]
    FRAUD_DECISION_STATUS_PENDING: _ClassVar[FraudDecisionStatus]
    FRAUD_DECISION_STATUS_ERROR: _ClassVar[FraudDecisionStatus]

class ManualReviewStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MANUAL_REVIEW_STATUS_UNSPECIFIED: _ClassVar[ManualReviewStatus]
    MANUAL_REVIEW_STATUS_PENDING: _ClassVar[ManualReviewStatus]
    MANUAL_REVIEW_STATUS_APPROVED: _ClassVar[ManualReviewStatus]
    MANUAL_REVIEW_STATUS_DENIED: _ClassVar[ManualReviewStatus]
TRANSACTION_STATUS_UNSPECIFIED: TransactionStatus
TRANSACTION_STATUS_AUTHORIZED: TransactionStatus
TRANSACTION_STATUS_PENDING: TransactionStatus
TRANSACTION_STATUS_FAIL: TransactionStatus
TRANSACTION_STATUS_CANCELLED: TransactionStatus
TRANSACTION_STATUS_REFUNDED: TransactionStatus
TRANSACTION_STATUS_PENDING_ANTIFRAUD: TransactionStatus
TRANSACTION_STATUS_PENDING_MANUAL_REVIEW: TransactionStatus
TRANSACTION_TYPE_UNSPECIFIED: TransactionType
TRANSACTION_TYPE_CARD: TransactionType
TRANSACTION_TYPE_BOLETO: TransactionType
TRANSACTION_TYPE_PIX: TransactionType
GATEWAY_UNSPECIFIED: Gateway
GATEWAY_PAGHIPER: Gateway
GATEWAY_PAGARME: Gateway
GATEWAY_MERCADOPAGO: Gateway
GATEWAY_BRAZILPAYS: Gateway
GATEWAY_GERENCIANET: Gateway
GATEWAY_CIELO: Gateway
GATEWAY_SICREDI: Gateway
GATEWAY_STRIPE: Gateway
GATEWAY_ASAAS: Gateway
GATEWAY_BB: Gateway
GATEWAY_BANCO_CORA: Gateway
GATEWAY_BRADESCO: Gateway
GATEWAY_C6BANK: Gateway
GATEWAY_TRANSFEERA: Gateway
GATEWAY_SICOOB: Gateway
GATEWAY_INTER: Gateway
GATEWAY_REDE: Gateway
REPORT_TYPE_UNSPECIFIED: ReportType
REPORT_TYPE_LIST: ReportType
CURRENCY_UNSPECIFIED: Currency
CURRENCY_BRL: Currency
CURRENCY_USD: Currency
CURRENCY_EUR: Currency
CURRENCY_GBP: Currency
SYNC_TRIGGER_UNSPECIFIED: SyncTrigger
SYNC_TRIGGER_MANUAL: SyncTrigger
SYNC_TRIGGER_WEBHOOK: SyncTrigger
SYNC_TRIGGER_SYSTEM: SyncTrigger
SYNC_TRIGGER_ANTIFRAUD: SyncTrigger
SYNC_TRIGGER_MANUAL_REVIEW: SyncTrigger
FRAUD_DECISION_STATUS_UNSPECIFIED: FraudDecisionStatus
FRAUD_DECISION_STATUS_APPROVED: FraudDecisionStatus
FRAUD_DECISION_STATUS_DENIED: FraudDecisionStatus
FRAUD_DECISION_STATUS_REVIEW: FraudDecisionStatus
FRAUD_DECISION_STATUS_PENDING: FraudDecisionStatus
FRAUD_DECISION_STATUS_ERROR: FraudDecisionStatus
MANUAL_REVIEW_STATUS_UNSPECIFIED: ManualReviewStatus
MANUAL_REVIEW_STATUS_PENDING: ManualReviewStatus
MANUAL_REVIEW_STATUS_APPROVED: ManualReviewStatus
MANUAL_REVIEW_STATUS_DENIED: ManualReviewStatus

class Transaction(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "user_id", "user_name", "status", "number", "payment_type", "payment_method_id", "payment_method_name", "payment_gateway", "transaction_id", "autorization_code", "nsu", "gateway_code", "tid", "return_code", "transaction_return", "origin_description", "origin_id", "origin_number", "due_date", "url", "confirmation_date_time", "gateway_response_date_time", "gateway_response_time", "currency", "currency_rate", "boleto_details", "card_details", "pix_details", "cancel_details", "value", "installments", "history", "timeout", "contact", "fraud_analysis", "manual_review", "test_environment")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    AUTORIZATION_CODE_FIELD_NUMBER: _ClassVar[int]
    NSU_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_CODE_FIELD_NUMBER: _ClassVar[int]
    TID_FIELD_NUMBER: _ClassVar[int]
    RETURN_CODE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_RETURN_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_RESPONSE_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_RATE_FIELD_NUMBER: _ClassVar[int]
    BOLETO_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CARD_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PIX_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CANCEL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    INSTALLMENTS_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    FRAUD_ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    MANUAL_REVIEW_FIELD_NUMBER: _ClassVar[int]
    TEST_ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    status: TransactionStatus
    number: int
    payment_type: TransactionType
    payment_method_id: str
    payment_method_name: str
    payment_gateway: Gateway
    transaction_id: str
    autorization_code: str
    nsu: str
    gateway_code: str
    tid: str
    return_code: str
    transaction_return: str
    origin_description: str
    origin_id: str
    origin_number: str
    due_date: _timestamp_pb2.Timestamp
    url: str
    confirmation_date_time: _timestamp_pb2.Timestamp
    gateway_response_date_time: _timestamp_pb2.Timestamp
    gateway_response_time: float
    currency: Currency
    currency_rate: float
    boleto_details: BoletoDetails
    card_details: CardDetails
    pix_details: PixDetails
    cancel_details: CancelDetails
    value: float
    installments: int
    history: _containers.RepeatedCompositeFieldContainer[TransactionHistory]
    timeout: bool
    contact: Contact
    fraud_analysis: FraudAnalysis
    manual_review: ManualReview
    test_environment: bool
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., status: _Optional[_Union[TransactionStatus, str]] = ..., number: _Optional[int] = ..., payment_type: _Optional[_Union[TransactionType, str]] = ..., payment_method_id: _Optional[str] = ..., payment_method_name: _Optional[str] = ..., payment_gateway: _Optional[_Union[Gateway, str]] = ..., transaction_id: _Optional[str] = ..., autorization_code: _Optional[str] = ..., nsu: _Optional[str] = ..., gateway_code: _Optional[str] = ..., tid: _Optional[str] = ..., return_code: _Optional[str] = ..., transaction_return: _Optional[str] = ..., origin_description: _Optional[str] = ..., origin_id: _Optional[str] = ..., origin_number: _Optional[str] = ..., due_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., url: _Optional[str] = ..., confirmation_date_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., gateway_response_date_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., gateway_response_time: _Optional[float] = ..., currency: _Optional[_Union[Currency, str]] = ..., currency_rate: _Optional[float] = ..., boleto_details: _Optional[_Union[BoletoDetails, _Mapping]] = ..., card_details: _Optional[_Union[CardDetails, _Mapping]] = ..., pix_details: _Optional[_Union[PixDetails, _Mapping]] = ..., cancel_details: _Optional[_Union[CancelDetails, _Mapping]] = ..., value: _Optional[float] = ..., installments: _Optional[int] = ..., history: _Optional[_Iterable[_Union[TransactionHistory, _Mapping]]] = ..., timeout: _Optional[bool] = ..., contact: _Optional[_Union[Contact, _Mapping]] = ..., fraud_analysis: _Optional[_Union[FraudAnalysis, _Mapping]] = ..., manual_review: _Optional[_Union[ManualReview, _Mapping]] = ..., test_environment: _Optional[bool] = ...) -> None: ...

class TransactionHistory(_message.Message):
    __slots__ = ("id", "user_id", "user_name", "status", "date_time", "response_time", "description", "sync_trigger")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SYNC_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    user_name: str
    status: TransactionStatus
    date_time: _timestamp_pb2.Timestamp
    response_time: float
    description: str
    sync_trigger: SyncTrigger
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., status: _Optional[_Union[TransactionStatus, str]] = ..., date_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., response_time: _Optional[float] = ..., description: _Optional[str] = ..., sync_trigger: _Optional[_Union[SyncTrigger, str]] = ...) -> None: ...

class FraudAnalysis(_message.Message):
    __slots__ = ("integration_id", "integration_name", "provider", "status", "score", "recommendation", "transaction_reference", "reason", "raw_response", "requested_at", "responded_at")
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDATION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RAW_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AT_FIELD_NUMBER: _ClassVar[int]
    RESPONDED_AT_FIELD_NUMBER: _ClassVar[int]
    integration_id: str
    integration_name: str
    provider: str
    status: FraudDecisionStatus
    score: str
    recommendation: str
    transaction_reference: str
    reason: str
    raw_response: str
    requested_at: _timestamp_pb2.Timestamp
    responded_at: _timestamp_pb2.Timestamp
    def __init__(self, integration_id: _Optional[str] = ..., integration_name: _Optional[str] = ..., provider: _Optional[str] = ..., status: _Optional[_Union[FraudDecisionStatus, str]] = ..., score: _Optional[str] = ..., recommendation: _Optional[str] = ..., transaction_reference: _Optional[str] = ..., reason: _Optional[str] = ..., raw_response: _Optional[str] = ..., requested_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., responded_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ManualReview(_message.Message):
    __slots__ = ("required", "status", "reviewed_by_user_id", "reviewed_by_user_name", "reviewed_at", "reason")
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    REVIEWED_BY_USER_ID_FIELD_NUMBER: _ClassVar[int]
    REVIEWED_BY_USER_NAME_FIELD_NUMBER: _ClassVar[int]
    REVIEWED_AT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    required: bool
    status: ManualReviewStatus
    reviewed_by_user_id: str
    reviewed_by_user_name: str
    reviewed_at: _timestamp_pb2.Timestamp
    reason: str
    def __init__(self, required: _Optional[bool] = ..., status: _Optional[_Union[ManualReviewStatus, str]] = ..., reviewed_by_user_id: _Optional[str] = ..., reviewed_by_user_name: _Optional[str] = ..., reviewed_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelDetails(_message.Message):
    __slots__ = ("code", "user_id", "user_name", "reason", "date_time")
    CODE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    code: str
    user_id: str
    user_name: str
    reason: str
    date_time: _timestamp_pb2.Timestamp
    def __init__(self, code: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., reason: _Optional[str] = ..., date_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class BoletoDetails(_message.Message):
    __slots__ = ("our_number", "document_number", "instruction", "bank", "agency", "account", "account_type", "account_digit", "account_name")
    OUR_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    BANK_FIELD_NUMBER: _ClassVar[int]
    AGENCY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_DIGIT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    our_number: str
    document_number: str
    instruction: str
    bank: str
    agency: str
    account: str
    account_type: str
    account_digit: str
    account_name: str
    def __init__(self, our_number: _Optional[str] = ..., document_number: _Optional[str] = ..., instruction: _Optional[str] = ..., bank: _Optional[str] = ..., agency: _Optional[str] = ..., account: _Optional[str] = ..., account_type: _Optional[str] = ..., account_digit: _Optional[str] = ..., account_name: _Optional[str] = ...) -> None: ...

class CardDetails(_message.Message):
    __slots__ = ("name_on_bill", "name", "expiration", "last4_digits", "number", "cvc", "year", "month", "brand", "token")
    NAME_ON_BILL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_FIELD_NUMBER: _ClassVar[int]
    LAST4_DIGITS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    CVC_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    name_on_bill: str
    name: str
    expiration: str
    last4_digits: str
    number: str
    cvc: str
    year: str
    month: str
    brand: str
    token: str
    def __init__(self, name_on_bill: _Optional[str] = ..., name: _Optional[str] = ..., expiration: _Optional[str] = ..., last4_digits: _Optional[str] = ..., number: _Optional[str] = ..., cvc: _Optional[str] = ..., year: _Optional[str] = ..., month: _Optional[str] = ..., brand: _Optional[str] = ..., token: _Optional[str] = ...) -> None: ...

class PixDetails(_message.Message):
    __slots__ = ("qr_code_base64", "qr_code_string", "id", "url")
    QR_CODE_BASE64_FIELD_NUMBER: _ClassVar[int]
    QR_CODE_STRING_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    qr_code_base64: str
    qr_code_string: str
    id: str
    url: str
    def __init__(self, qr_code_base64: _Optional[str] = ..., qr_code_string: _Optional[str] = ..., id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class Contact(_message.Message):
    __slots__ = ("id", "document_number", "name", "user_id", "user_name", "address_name", "zip_code", "address", "number", "district", "city", "city_code", "state", "phone", "email", "birth_date", "gender", "address_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_NAME_FIELD_NUMBER: _ClassVar[int]
    ZIP_CODE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    DISTRICT_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    CITY_CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    document_number: str
    name: str
    user_id: str
    user_name: str
    address_name: str
    zip_code: str
    address: str
    number: str
    district: str
    city: str
    city_code: str
    state: str
    phone: str
    email: str
    birth_date: str
    gender: str
    address_id: str
    def __init__(self, id: _Optional[str] = ..., document_number: _Optional[str] = ..., name: _Optional[str] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., address_name: _Optional[str] = ..., zip_code: _Optional[str] = ..., address: _Optional[str] = ..., number: _Optional[str] = ..., district: _Optional[str] = ..., city: _Optional[str] = ..., city_code: _Optional[str] = ..., state: _Optional[str] = ..., phone: _Optional[str] = ..., email: _Optional[str] = ..., birth_date: _Optional[str] = ..., gender: _Optional[str] = ..., address_id: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: Transaction
    def __init__(self, transaction: _Optional[_Union[Transaction, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: Transaction
    def __init__(self, transaction: _Optional[_Union[Transaction, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "transaction", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    transaction: Transaction
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., transaction: _Optional[_Union[Transaction, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: Transaction
    def __init__(self, transaction: _Optional[_Union[Transaction, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: Transaction
    def __init__(self, transaction: _Optional[_Union[Transaction, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "status", "payment_type", "origin_id", "origin_number", "origin_description", "transaction_id", "payment_gateway", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    status: TransactionStatus
    payment_type: TransactionType
    origin_id: str
    origin_number: str
    origin_description: str
    transaction_id: str
    payment_gateway: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., status: _Optional[_Union[TransactionStatus, str]] = ..., payment_type: _Optional[_Union[TransactionType, str]] = ..., origin_id: _Optional[str] = ..., origin_number: _Optional[str] = ..., origin_description: _Optional[str] = ..., transaction_id: _Optional[str] = ..., payment_gateway: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("transaction_list",)
    TRANSACTION_LIST_FIELD_NUMBER: _ClassVar[int]
    transaction_list: _containers.RepeatedCompositeFieldContainer[Transaction]
    def __init__(self, transaction_list: _Optional[_Iterable[_Union[Transaction, _Mapping]]] = ...) -> None: ...

class CancelRequest(_message.Message):
    __slots__ = ("id", "origin_id", "transaction_id", "reason", "cancel_order_payment")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CANCEL_ORDER_PAYMENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    origin_id: str
    transaction_id: str
    reason: str
    cancel_order_payment: bool
    def __init__(self, id: _Optional[str] = ..., origin_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., reason: _Optional[str] = ..., cancel_order_payment: _Optional[bool] = ...) -> None: ...

class CancelResponse(_message.Message):
    __slots__ = ("status", "message", "order")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    status: TransactionStatus
    message: str
    order: _pedido_pb2.Pedido
    def __init__(self, status: _Optional[_Union[TransactionStatus, str]] = ..., message: _Optional[str] = ..., order: _Optional[_Union[_pedido_pb2.Pedido, _Mapping]] = ...) -> None: ...

class SyncRequest(_message.Message):
    __slots__ = ("id", "origin_id", "transaction_id", "additional_details", "sync_trigger")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    SYNC_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    id: str
    origin_id: str
    transaction_id: str
    additional_details: str
    sync_trigger: SyncTrigger
    def __init__(self, id: _Optional[str] = ..., origin_id: _Optional[str] = ..., transaction_id: _Optional[str] = ..., additional_details: _Optional[str] = ..., sync_trigger: _Optional[_Union[SyncTrigger, str]] = ...) -> None: ...

class SyncResponse(_message.Message):
    __slots__ = ("status", "message")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    status: TransactionStatus
    message: str
    def __init__(self, status: _Optional[_Union[TransactionStatus, str]] = ..., message: _Optional[str] = ...) -> None: ...

class ApproveManualReviewRequest(_message.Message):
    __slots__ = ("id", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class ApproveManualReviewResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: Transaction
    def __init__(self, transaction: _Optional[_Union[Transaction, _Mapping]] = ...) -> None: ...

class RejectManualReviewRequest(_message.Message):
    __slots__ = ("id", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class RejectManualReviewResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: Transaction
    def __init__(self, transaction: _Optional[_Union[Transaction, _Mapping]] = ...) -> None: ...

class SimulatePaymentRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SimulatePaymentResponse(_message.Message):
    __slots__ = ("transaction",)
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    transaction: Transaction
    def __init__(self, transaction: _Optional[_Union[Transaction, _Mapping]] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("list_request", "report_type", "tipo_relatorio", "send_by_email")
    LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    SEND_BY_EMAIL_FIELD_NUMBER: _ClassVar[int]
    list_request: ListRequest
    report_type: ReportType
    tipo_relatorio: str
    send_by_email: str
    def __init__(self, list_request: _Optional[_Union[ListRequest, _Mapping]] = ..., report_type: _Optional[_Union[ReportType, str]] = ..., tipo_relatorio: _Optional[str] = ..., send_by_email: _Optional[str] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...
