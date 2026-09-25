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

class GrupoPessoaStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GRUPO_PESSOA_STATUS_UNSPECIFIED: _ClassVar[GrupoPessoaStatus]
    GRUPO_PESSOA_STATUS_ACTIVE: _ClassVar[GrupoPessoaStatus]
    GRUPO_PESSOA_STATUS_INACTIVE: _ClassVar[GrupoPessoaStatus]
    GRUPO_PESSOA_STATUS_BLOCKED: _ClassVar[GrupoPessoaStatus]
GRUPO_PESSOA_STATUS_UNSPECIFIED: GrupoPessoaStatus
GRUPO_PESSOA_STATUS_ACTIVE: GrupoPessoaStatus
GRUPO_PESSOA_STATUS_INACTIVE: GrupoPessoaStatus
GRUPO_PESSOA_STATUS_BLOCKED: GrupoPessoaStatus

class GrupoPessoa(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "status", "nome", "obs", "fields")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    status: GrupoPessoaStatus
    nome: str
    obs: str
    fields: _metadata_pb2.BasicFields
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., status: _Optional[_Union[GrupoPessoaStatus, str]] = ..., nome: _Optional[str] = ..., obs: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("grupo_pessoa",)
    GRUPO_PESSOA_FIELD_NUMBER: _ClassVar[int]
    grupo_pessoa: GrupoPessoa
    def __init__(self, grupo_pessoa: _Optional[_Union[GrupoPessoa, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("grupo_pessoa",)
    GRUPO_PESSOA_FIELD_NUMBER: _ClassVar[int]
    grupo_pessoa: GrupoPessoa
    def __init__(self, grupo_pessoa: _Optional[_Union[GrupoPessoa, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "grupo_pessoa", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    GRUPO_PESSOA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    grupo_pessoa: GrupoPessoa
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., grupo_pessoa: _Optional[_Union[GrupoPessoa, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("grupo_pessoa",)
    GRUPO_PESSOA_FIELD_NUMBER: _ClassVar[int]
    grupo_pessoa: GrupoPessoa
    def __init__(self, grupo_pessoa: _Optional[_Union[GrupoPessoa, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("grupo_pessoa",)
    GRUPO_PESSOA_FIELD_NUMBER: _ClassVar[int]
    grupo_pessoa: GrupoPessoa
    def __init__(self, grupo_pessoa: _Optional[_Union[GrupoPessoa, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("grupo_pessoa_list", "next_page_token")
    GRUPO_PESSOA_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    grupo_pessoa_list: _containers.RepeatedCompositeFieldContainer[GrupoPessoa]
    next_page_token: str
    def __init__(self, grupo_pessoa_list: _Optional[_Iterable[_Union[GrupoPessoa, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...
