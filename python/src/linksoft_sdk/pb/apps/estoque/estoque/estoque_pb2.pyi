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

class EstoqueSituacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ESTOQUE_SITUACAO_ATIVO: _ClassVar[EstoqueSituacao]
    ESTOQUE_SITUACAO_INATIVO: _ClassVar[EstoqueSituacao]
ESTOQUE_SITUACAO_ATIVO: EstoqueSituacao
ESTOQUE_SITUACAO_INATIVO: EstoqueSituacao

class Estoque(_message.Message):
    __slots__ = ("fields", "id", "nome", "descricao", "situacao", "created_at", "updated_at", "user_id", "user_name")
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    fields: _metadata_pb2.BasicFields
    id: str
    nome: str
    descricao: str
    situacao: EstoqueSituacao
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    def __init__(self, fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., id: _Optional[str] = ..., nome: _Optional[str] = ..., descricao: _Optional[str] = ..., situacao: _Optional[_Union[EstoqueSituacao, str]] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ...) -> None: ...

class CreateEstoqueRequest(_message.Message):
    __slots__ = ("estoque",)
    ESTOQUE_FIELD_NUMBER: _ClassVar[int]
    estoque: Estoque
    def __init__(self, estoque: _Optional[_Union[Estoque, _Mapping]] = ...) -> None: ...

class CreateEstoqueResponse(_message.Message):
    __slots__ = ("estoque",)
    ESTOQUE_FIELD_NUMBER: _ClassVar[int]
    estoque: Estoque
    def __init__(self, estoque: _Optional[_Union[Estoque, _Mapping]] = ...) -> None: ...

class UpdateEstoqueRequest(_message.Message):
    __slots__ = ("id", "estoque", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    ESTOQUE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    estoque: Estoque
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., estoque: _Optional[_Union[Estoque, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateEstoqueResponse(_message.Message):
    __slots__ = ("estoque",)
    ESTOQUE_FIELD_NUMBER: _ClassVar[int]
    estoque: Estoque
    def __init__(self, estoque: _Optional[_Union[Estoque, _Mapping]] = ...) -> None: ...

class DeleteEstoqueRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteEstoqueResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetEstoqueRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetEstoqueResponse(_message.Message):
    __slots__ = ("estoque",)
    ESTOQUE_FIELD_NUMBER: _ClassVar[int]
    estoque: Estoque
    def __init__(self, estoque: _Optional[_Union[Estoque, _Mapping]] = ...) -> None: ...

class ListEstoqueRequest(_message.Message):
    __slots__ = ("ids", "nome", "situacao", "ignore_situacao", "filter", "page_size", "page_token")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    IGNORE_SITUACAO_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    nome: str
    situacao: EstoqueSituacao
    ignore_situacao: bool
    filter: _filter_pb2.Filter
    page_size: int
    page_token: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., nome: _Optional[str] = ..., situacao: _Optional[_Union[EstoqueSituacao, str]] = ..., ignore_situacao: _Optional[bool] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListEstoqueResponse(_message.Message):
    __slots__ = ("estoque_list", "next_page_token")
    ESTOQUE_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    estoque_list: _containers.RepeatedCompositeFieldContainer[Estoque]
    next_page_token: str
    def __init__(self, estoque_list: _Optional[_Iterable[_Union[Estoque, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
