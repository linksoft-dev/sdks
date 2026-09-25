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

class Natureza(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NATUREZA_UNSPECIFIED: _ClassVar[Natureza]
    NATUREZA_VARIAVEL: _ClassVar[Natureza]
    NATUREZA_FIXA: _ClassVar[Natureza]
NATUREZA_UNSPECIFIED: Natureza
NATUREZA_VARIAVEL: Natureza
NATUREZA_FIXA: Natureza

class PlanoConta(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "codigo", "nome", "tipo", "sistema", "parentId", "descricao", "monthlyBudget", "monthlyBudgets", "natureza", "fields")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    SISTEMA_FIELD_NUMBER: _ClassVar[int]
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    MONTHLYBUDGET_FIELD_NUMBER: _ClassVar[int]
    MONTHLYBUDGETS_FIELD_NUMBER: _ClassVar[int]
    NATUREZA_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    codigo: str
    nome: str
    tipo: str
    sistema: bool
    parentId: str
    descricao: str
    monthlyBudget: float
    monthlyBudgets: _containers.RepeatedCompositeFieldContainer[MonthlyBudgetOverride]
    natureza: Natureza
    fields: _metadata_pb2.BasicFields
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., codigo: _Optional[str] = ..., nome: _Optional[str] = ..., tipo: _Optional[str] = ..., sistema: _Optional[bool] = ..., parentId: _Optional[str] = ..., descricao: _Optional[str] = ..., monthlyBudget: _Optional[float] = ..., monthlyBudgets: _Optional[_Iterable[_Union[MonthlyBudgetOverride, _Mapping]]] = ..., natureza: _Optional[_Union[Natureza, str]] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...

class MonthlyBudgetOverride(_message.Message):
    __slots__ = ("month", "budget")
    MONTH_FIELD_NUMBER: _ClassVar[int]
    BUDGET_FIELD_NUMBER: _ClassVar[int]
    month: str
    budget: float
    def __init__(self, month: _Optional[str] = ..., budget: _Optional[float] = ...) -> None: ...

class CreatePlanoContaRequest(_message.Message):
    __slots__ = ("planoConta",)
    PLANOCONTA_FIELD_NUMBER: _ClassVar[int]
    planoConta: PlanoConta
    def __init__(self, planoConta: _Optional[_Union[PlanoConta, _Mapping]] = ...) -> None: ...

class CreatePlanoContaResponse(_message.Message):
    __slots__ = ("planoConta",)
    PLANOCONTA_FIELD_NUMBER: _ClassVar[int]
    planoConta: PlanoConta
    def __init__(self, planoConta: _Optional[_Union[PlanoConta, _Mapping]] = ...) -> None: ...

class UpdatePlanoContaRequest(_message.Message):
    __slots__ = ("id", "planoConta", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    PLANOCONTA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    planoConta: PlanoConta
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., planoConta: _Optional[_Union[PlanoConta, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdatePlanoContaResponse(_message.Message):
    __slots__ = ("planoConta",)
    PLANOCONTA_FIELD_NUMBER: _ClassVar[int]
    planoConta: PlanoConta
    def __init__(self, planoConta: _Optional[_Union[PlanoConta, _Mapping]] = ...) -> None: ...

class DeletePlanoContaRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeletePlanoContaResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetPlanoContaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetPlanoContaResponse(_message.Message):
    __slots__ = ("planoConta",)
    PLANOCONTA_FIELD_NUMBER: _ClassVar[int]
    planoConta: PlanoConta
    def __init__(self, planoConta: _Optional[_Union[PlanoConta, _Mapping]] = ...) -> None: ...

class ListPlanoContaRequest(_message.Message):
    __slots__ = ("ids", "planoConta", "page_size", "page_token", "filter", "tipo")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PLANOCONTA_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    planoConta: PlanoConta
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    tipo: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., planoConta: _Optional[_Union[PlanoConta, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., tipo: _Optional[str] = ...) -> None: ...

class ListPlanoContaResponse(_message.Message):
    __slots__ = ("planoContaList", "next_page_token")
    PLANOCONTALIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    planoContaList: _containers.RepeatedCompositeFieldContainer[PlanoConta]
    next_page_token: str
    def __init__(self, planoContaList: _Optional[_Iterable[_Union[PlanoConta, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
