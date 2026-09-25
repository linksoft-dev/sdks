import datetime

from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Inventario(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "nome", "nfce", "nfe", "pedido", "data_inicio", "data_fim", "total_custo", "total_atacado", "total", "total_aprazo", "produtos")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    NFCE_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    DATA_INICIO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIM_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CUSTO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ATACADO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_APRAZO_FIELD_NUMBER: _ClassVar[int]
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    nome: str
    nfce: bool
    nfe: bool
    pedido: bool
    data_inicio: _timestamp_pb2.Timestamp
    data_fim: _timestamp_pb2.Timestamp
    total_custo: float
    total_atacado: float
    total: float
    total_aprazo: float
    produtos: _containers.RepeatedCompositeFieldContainer[InventarioProduto]
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., nome: _Optional[str] = ..., nfce: _Optional[bool] = ..., nfe: _Optional[bool] = ..., pedido: _Optional[bool] = ..., data_inicio: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_fim: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_custo: _Optional[float] = ..., total_atacado: _Optional[float] = ..., total: _Optional[float] = ..., total_aprazo: _Optional[float] = ..., produtos: _Optional[_Iterable[_Union[InventarioProduto, _Mapping]]] = ...) -> None: ...

class InventarioProduto(_message.Message):
    __slots__ = ("id", "produto_id", "produto_nome", "codigo", "un", "quantidade", "preco_custo", "preco_venda_atacado", "valor_unitario", "preco_venda_aprazo", "total_custo", "total_atacado", "total", "total_aprazo")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    PRECO_CUSTO_FIELD_NUMBER: _ClassVar[int]
    PRECO_VENDA_ATACADO_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    PRECO_VENDA_APRAZO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CUSTO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ATACADO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_APRAZO_FIELD_NUMBER: _ClassVar[int]
    id: str
    produto_id: str
    produto_nome: str
    codigo: str
    un: str
    quantidade: float
    preco_custo: float
    preco_venda_atacado: float
    valor_unitario: float
    preco_venda_aprazo: float
    total_custo: float
    total_atacado: float
    total: float
    total_aprazo: float
    def __init__(self, id: _Optional[str] = ..., produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ..., codigo: _Optional[str] = ..., un: _Optional[str] = ..., quantidade: _Optional[float] = ..., preco_custo: _Optional[float] = ..., preco_venda_atacado: _Optional[float] = ..., valor_unitario: _Optional[float] = ..., preco_venda_aprazo: _Optional[float] = ..., total_custo: _Optional[float] = ..., total_atacado: _Optional[float] = ..., total: _Optional[float] = ..., total_aprazo: _Optional[float] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("inventario",)
    INVENTARIO_FIELD_NUMBER: _ClassVar[int]
    inventario: Inventario
    def __init__(self, inventario: _Optional[_Union[Inventario, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("inventario",)
    INVENTARIO_FIELD_NUMBER: _ClassVar[int]
    inventario: Inventario
    def __init__(self, inventario: _Optional[_Union[Inventario, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "inventario", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    INVENTARIO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    inventario: Inventario
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., inventario: _Optional[_Union[Inventario, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("inventario",)
    INVENTARIO_FIELD_NUMBER: _ClassVar[int]
    inventario: Inventario
    def __init__(self, inventario: _Optional[_Union[Inventario, _Mapping]] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetResponse(_message.Message):
    __slots__ = ("inventario",)
    INVENTARIO_FIELD_NUMBER: _ClassVar[int]
    inventario: Inventario
    def __init__(self, inventario: _Optional[_Union[Inventario, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
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

class ListResponse(_message.Message):
    __slots__ = ("inventario_list", "next_page_token")
    INVENTARIO_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    inventario_list: _containers.RepeatedCompositeFieldContainer[Inventario]
    next_page_token: str
    def __init__(self, inventario_list: _Optional[_Iterable[_Union[Inventario, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GerarRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GerarResponse(_message.Message):
    __slots__ = ("inventario",)
    INVENTARIO_FIELD_NUMBER: _ClassVar[int]
    inventario: Inventario
    def __init__(self, inventario: _Optional[_Union[Inventario, _Mapping]] = ...) -> None: ...

class ImprimirRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ImprimirResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class EnviaPorEmailRequest(_message.Message):
    __slots__ = ("id", "email", "format", "subject", "recipient_name", "integration_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    email: str
    format: _report_pb2.ReportFormat
    subject: str
    recipient_name: str
    integration_id: str
    def __init__(self, id: _Optional[str] = ..., email: _Optional[str] = ..., format: _Optional[_Union[_report_pb2.ReportFormat, str]] = ..., subject: _Optional[str] = ..., recipient_name: _Optional[str] = ..., integration_id: _Optional[str] = ...) -> None: ...

class EnviaPorEmailResponse(_message.Message):
    __slots__ = ("inventario",)
    INVENTARIO_FIELD_NUMBER: _ClassVar[int]
    inventario: Inventario
    def __init__(self, inventario: _Optional[_Union[Inventario, _Mapping]] = ...) -> None: ...
