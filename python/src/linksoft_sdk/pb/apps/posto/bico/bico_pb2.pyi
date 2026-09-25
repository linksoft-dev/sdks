import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Bico(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "numero", "modelo", "produto_id", "produto_nome", "num_tanque", "num_bomba", "tipo_preco", "preco", "fields", "preco_avista", "preco_aprazo")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    MODELO_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    NUM_TANQUE_FIELD_NUMBER: _ClassVar[int]
    NUM_BOMBA_FIELD_NUMBER: _ClassVar[int]
    TIPO_PRECO_FIELD_NUMBER: _ClassVar[int]
    PRECO_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    PRECO_AVISTA_FIELD_NUMBER: _ClassVar[int]
    PRECO_APRAZO_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    numero: int
    modelo: str
    produto_id: str
    produto_nome: str
    num_tanque: str
    num_bomba: str
    tipo_preco: str
    preco: float
    fields: _metadata_pb2.BasicFields
    preco_avista: float
    preco_aprazo: float
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., numero: _Optional[int] = ..., modelo: _Optional[str] = ..., produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ..., num_tanque: _Optional[str] = ..., num_bomba: _Optional[str] = ..., tipo_preco: _Optional[str] = ..., preco: _Optional[float] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., preco_avista: _Optional[float] = ..., preco_aprazo: _Optional[float] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("bico",)
    BICO_FIELD_NUMBER: _ClassVar[int]
    bico: Bico
    def __init__(self, bico: _Optional[_Union[Bico, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("bico",)
    BICO_FIELD_NUMBER: _ClassVar[int]
    bico: Bico
    def __init__(self, bico: _Optional[_Union[Bico, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "bico", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    BICO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    bico: Bico
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., bico: _Optional[_Union[Bico, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("bico",)
    BICO_FIELD_NUMBER: _ClassVar[int]
    bico: Bico
    def __init__(self, bico: _Optional[_Union[Bico, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("bico",)
    BICO_FIELD_NUMBER: _ClassVar[int]
    bico: Bico
    def __init__(self, bico: _Optional[_Union[Bico, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("bico_list", "next_page_token")
    BICO_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    bico_list: _containers.RepeatedCompositeFieldContainer[Bico]
    next_page_token: str
    def __init__(self, bico_list: _Optional[_Iterable[_Union[Bico, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
