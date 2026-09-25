import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_TYPE_UNSPECIFIED: _ClassVar[ReportType]
    REPORT_TYPE_DRE: _ClassVar[ReportType]
    REPORT_TYPE_ACCOUNTS_AND_CASH: _ClassVar[ReportType]

class Regime(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REGIME_COMPETENCIA: _ClassVar[Regime]
    REGIME_CAIXA: _ClassVar[Regime]

class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPE_UNSPECIFIED: _ClassVar[Type]
    TYPE_REVENUE: _ClassVar[Type]
    TYPE_EXPENSE: _ClassVar[Type]
REPORT_TYPE_UNSPECIFIED: ReportType
REPORT_TYPE_DRE: ReportType
REPORT_TYPE_ACCOUNTS_AND_CASH: ReportType
REGIME_COMPETENCIA: Regime
REGIME_CAIXA: Regime
TYPE_UNSPECIFIED: Type
TYPE_REVENUE: Type
TYPE_EXPENSE: Type

class ReportRequest(_message.Message):
    __slots__ = ("filter", "report_type", "chart_of_account_id", "meta_lucro", "org_ids")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    REPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHART_OF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    META_LUCRO_FIELD_NUMBER: _ClassVar[int]
    ORG_IDS_FIELD_NUMBER: _ClassVar[int]
    filter: _filter_pb2.Filter
    report_type: ReportType
    chart_of_account_id: str
    meta_lucro: float
    org_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., report_type: _Optional[_Union[ReportType, str]] = ..., chart_of_account_id: _Optional[str] = ..., meta_lucro: _Optional[float] = ..., org_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response", "dre", "entries", "empresas")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    DRE_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    EMPRESAS_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    dre: Dre
    entries: _containers.RepeatedCompositeFieldContainer[Entry]
    empresas: _containers.RepeatedCompositeFieldContainer[DreEmpresa]
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ..., dre: _Optional[_Union[Dre, _Mapping]] = ..., entries: _Optional[_Iterable[_Union[Entry, _Mapping]]] = ..., empresas: _Optional[_Iterable[_Union[DreEmpresa, _Mapping]]] = ...) -> None: ...

class DreEmpresa(_message.Message):
    __slots__ = ("org_id", "org_nome", "dre")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_NOME_FIELD_NUMBER: _ClassVar[int]
    DRE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    org_nome: str
    dre: Dre
    def __init__(self, org_id: _Optional[str] = ..., org_nome: _Optional[str] = ..., dre: _Optional[_Union[Dre, _Mapping]] = ...) -> None: ...

class Dre(_message.Message):
    __slots__ = ("date_initial", "date_final", "regime", "currency_type", "items", "warnings", "analise")
    DATE_INITIAL_FIELD_NUMBER: _ClassVar[int]
    DATE_FINAL_FIELD_NUMBER: _ClassVar[int]
    REGIME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ANALISE_FIELD_NUMBER: _ClassVar[int]
    date_initial: _timestamp_pb2.Timestamp
    date_final: _timestamp_pb2.Timestamp
    regime: Regime
    currency_type: str
    items: _containers.RepeatedCompositeFieldContainer[Item]
    warnings: _containers.RepeatedScalarFieldContainer[str]
    analise: AnaliseGerencial
    def __init__(self, date_initial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., date_final: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., regime: _Optional[_Union[Regime, str]] = ..., currency_type: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., warnings: _Optional[_Iterable[str]] = ..., analise: _Optional[_Union[AnaliseGerencial, _Mapping]] = ...) -> None: ...

class AnaliseGerencial(_message.Message):
    __slots__ = ("receita", "custosVariaveis", "margemContribuicao", "margemContribuicaoPercentual", "custosFixos", "pontoEquilibrio", "margemSeguranca", "naoClassificado", "metaLucro", "pontoEquilibrioMeta")
    RECEITA_FIELD_NUMBER: _ClassVar[int]
    CUSTOSVARIAVEIS_FIELD_NUMBER: _ClassVar[int]
    MARGEMCONTRIBUICAO_FIELD_NUMBER: _ClassVar[int]
    MARGEMCONTRIBUICAOPERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    CUSTOSFIXOS_FIELD_NUMBER: _ClassVar[int]
    PONTOEQUILIBRIO_FIELD_NUMBER: _ClassVar[int]
    MARGEMSEGURANCA_FIELD_NUMBER: _ClassVar[int]
    NAOCLASSIFICADO_FIELD_NUMBER: _ClassVar[int]
    METALUCRO_FIELD_NUMBER: _ClassVar[int]
    PONTOEQUILIBRIOMETA_FIELD_NUMBER: _ClassVar[int]
    receita: float
    custosVariaveis: float
    margemContribuicao: float
    margemContribuicaoPercentual: float
    custosFixos: float
    pontoEquilibrio: float
    margemSeguranca: float
    naoClassificado: float
    metaLucro: float
    pontoEquilibrioMeta: float
    def __init__(self, receita: _Optional[float] = ..., custosVariaveis: _Optional[float] = ..., margemContribuicao: _Optional[float] = ..., margemContribuicaoPercentual: _Optional[float] = ..., custosFixos: _Optional[float] = ..., pontoEquilibrio: _Optional[float] = ..., margemSeguranca: _Optional[float] = ..., naoClassificado: _Optional[float] = ..., metaLucro: _Optional[float] = ..., pontoEquilibrioMeta: _Optional[float] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("id", "chart_of_account_id", "chart_of_account_name", "chart_of_account_code", "type", "budgeted", "realized", "level", "parent_id", "total", "count")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHART_OF_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    CHART_OF_ACCOUNT_NAME_FIELD_NUMBER: _ClassVar[int]
    CHART_OF_ACCOUNT_CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BUDGETED_FIELD_NUMBER: _ClassVar[int]
    REALIZED_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    id: str
    chart_of_account_id: str
    chart_of_account_name: str
    chart_of_account_code: str
    type: Type
    budgeted: float
    realized: float
    level: int
    parent_id: str
    total: bool
    count: int
    def __init__(self, id: _Optional[str] = ..., chart_of_account_id: _Optional[str] = ..., chart_of_account_name: _Optional[str] = ..., chart_of_account_code: _Optional[str] = ..., type: _Optional[_Union[Type, str]] = ..., budgeted: _Optional[float] = ..., realized: _Optional[float] = ..., level: _Optional[int] = ..., parent_id: _Optional[str] = ..., total: _Optional[bool] = ..., count: _Optional[int] = ...) -> None: ...

class Entry(_message.Message):
    __slots__ = ("date", "description", "person_name", "document", "source", "source_id", "value")
    DATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PERSON_NAME_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    date: _timestamp_pb2.Timestamp
    description: str
    person_name: str
    document: str
    source: str
    source_id: str
    value: float
    def __init__(self, date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., description: _Optional[str] = ..., person_name: _Optional[str] = ..., document: _Optional[str] = ..., source: _Optional[str] = ..., source_id: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
