import datetime

from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Situacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SITUACAO_UNSPECIFIED: _ClassVar[Situacao]
    SITUACAO_ATIVO: _ClassVar[Situacao]
    SITUACAO_INATIVO: _ClassVar[Situacao]

class Destinatario(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DESTINATARIO_UNSPECIFIED: _ClassVar[Destinatario]
    DESTINATARIO_TODOS: _ClassVar[Destinatario]
    DESTINATARIO_VENDEDOR: _ClassVar[Destinatario]
SITUACAO_UNSPECIFIED: Situacao
SITUACAO_ATIVO: Situacao
SITUACAO_INATIVO: Situacao
DESTINATARIO_UNSPECIFIED: Destinatario
DESTINATARIO_TODOS: Destinatario
DESTINATARIO_VENDEDOR: Destinatario

class InactivityRule(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "name", "situacao", "dias", "filtro_cliente", "filtro_venda", "destinatario", "avisa_cliente")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    DIAS_FIELD_NUMBER: _ClassVar[int]
    FILTRO_CLIENTE_FIELD_NUMBER: _ClassVar[int]
    FILTRO_VENDA_FIELD_NUMBER: _ClassVar[int]
    DESTINATARIO_FIELD_NUMBER: _ClassVar[int]
    AVISA_CLIENTE_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    name: str
    situacao: Situacao
    dias: int
    filtro_cliente: _filter_pb2.Filter
    filtro_venda: _filter_pb2.Filter
    destinatario: Destinatario
    avisa_cliente: bool
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., name: _Optional[str] = ..., situacao: _Optional[_Union[Situacao, str]] = ..., dias: _Optional[int] = ..., filtro_cliente: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., filtro_venda: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., destinatario: _Optional[_Union[Destinatario, str]] = ..., avisa_cliente: _Optional[bool] = ...) -> None: ...
