import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CashType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CASH_TYPE_UNSPECIFIED: _ClassVar[CashType]
    CASH_TYPE_CAIXA: _ClassVar[CashType]
    CASH_TYPE_CASH: _ClassVar[CashType]
    CASH_TYPE_CREDIT_CARD: _ClassVar[CashType]
    CASH_TYPE_DEBIT_CARD: _ClassVar[CashType]
    CASH_TYPE_BANK_TRANSFER: _ClassVar[CashType]
    CASH_TYPE_OTHER: _ClassVar[CashType]
CASH_TYPE_UNSPECIFIED: CashType
CASH_TYPE_CAIXA: CashType
CASH_TYPE_CASH: CashType
CASH_TYPE_CREDIT_CARD: CashType
CASH_TYPE_DEBIT_CARD: CashType
CASH_TYPE_BANK_TRANSFER: CashType
CASH_TYPE_OTHER: CashType

class Caixa(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "nome", "type", "logo", "tipo_moeda", "bank_account", "card", "monthly_budget", "monthly_budgets", "fields")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    TIPO_MOEDA_FIELD_NUMBER: _ClassVar[int]
    BANK_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CARD_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_BUDGET_FIELD_NUMBER: _ClassVar[int]
    MONTHLY_BUDGETS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    nome: str
    type: CashType
    logo: str
    tipo_moeda: str
    bank_account: BankAccount
    card: Card
    monthly_budget: float
    monthly_budgets: _containers.RepeatedCompositeFieldContainer[MonthlyBudgetOverride]
    fields: _metadata_pb2.BasicFields
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., nome: _Optional[str] = ..., type: _Optional[_Union[CashType, str]] = ..., logo: _Optional[str] = ..., tipo_moeda: _Optional[str] = ..., bank_account: _Optional[_Union[BankAccount, _Mapping]] = ..., card: _Optional[_Union[Card, _Mapping]] = ..., monthly_budget: _Optional[float] = ..., monthly_budgets: _Optional[_Iterable[_Union[MonthlyBudgetOverride, _Mapping]]] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...

class BankAccount(_message.Message):
    __slots__ = ("id", "bank_name", "agency", "account")
    ID_FIELD_NUMBER: _ClassVar[int]
    BANK_NAME_FIELD_NUMBER: _ClassVar[int]
    AGENCY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    bank_name: str
    agency: str
    account: str
    def __init__(self, id: _Optional[str] = ..., bank_name: _Optional[str] = ..., agency: _Optional[str] = ..., account: _Optional[str] = ...) -> None: ...

class Card(_message.Message):
    __slots__ = ("id", "card_name", "card_number", "card_brand", "card_expiration_date", "card_cvv", "card_token")
    ID_FIELD_NUMBER: _ClassVar[int]
    CARD_NAME_FIELD_NUMBER: _ClassVar[int]
    CARD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    CARD_BRAND_FIELD_NUMBER: _ClassVar[int]
    CARD_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    CARD_CVV_FIELD_NUMBER: _ClassVar[int]
    CARD_TOKEN_FIELD_NUMBER: _ClassVar[int]
    id: str
    card_name: str
    card_number: str
    card_brand: str
    card_expiration_date: str
    card_cvv: str
    card_token: str
    def __init__(self, id: _Optional[str] = ..., card_name: _Optional[str] = ..., card_number: _Optional[str] = ..., card_brand: _Optional[str] = ..., card_expiration_date: _Optional[str] = ..., card_cvv: _Optional[str] = ..., card_token: _Optional[str] = ...) -> None: ...

class MonthlyBudgetOverride(_message.Message):
    __slots__ = ("month", "budget")
    MONTH_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    month: str
    budget: float
    def __init__(self, month: _Optional[str] = ..., budget: _Optional[float] = ...) -> None: ...

class CreateCaixaRequest(_message.Message):
    __slots__ = ("caixa",)
    CAIXA_FIELD_NUMBER: _ClassVar[int]
    caixa: Caixa
    def __init__(self, caixa: _Optional[_Union[Caixa, _Mapping]] = ...) -> None: ...

class CreateCaixaResponse(_message.Message):
    __slots__ = ("caixa",)
    CAIXA_FIELD_NUMBER: _ClassVar[int]
    caixa: Caixa
    def __init__(self, caixa: _Optional[_Union[Caixa, _Mapping]] = ...) -> None: ...

class UpdateCaixaRequest(_message.Message):
    __slots__ = ("id", "caixa", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CAIXA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    caixa: Caixa
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., caixa: _Optional[_Union[Caixa, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateCaixaResponse(_message.Message):
    __slots__ = ("caixa",)
    CAIXA_FIELD_NUMBER: _ClassVar[int]
    caixa: Caixa
    def __init__(self, caixa: _Optional[_Union[Caixa, _Mapping]] = ...) -> None: ...

class DeleteCaixaRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteCaixaResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCaixaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetCaixaResponse(_message.Message):
    __slots__ = ("caixa",)
    CAIXA_FIELD_NUMBER: _ClassVar[int]
    caixa: Caixa
    def __init__(self, caixa: _Optional[_Union[Caixa, _Mapping]] = ...) -> None: ...

class ListCaixaRequest(_message.Message):
    __slots__ = ("ids", "page_size", "page_token", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListCaixaResponse(_message.Message):
    __slots__ = ("caixaList", "next_page_token")
    CAIXALIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    caixaList: _containers.RepeatedCompositeFieldContainer[Caixa]
    next_page_token: str
    def __init__(self, caixaList: _Optional[_Iterable[_Union[Caixa, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
