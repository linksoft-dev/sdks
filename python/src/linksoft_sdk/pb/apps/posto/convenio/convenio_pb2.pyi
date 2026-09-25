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

class Fechamento(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FECHAMENTO_MENSAL: _ClassVar[Fechamento]
    FECHAMENTO_QUINZENAL: _ClassVar[Fechamento]
    FECHAMENTO_SEMANAL: _ClassVar[Fechamento]
FECHAMENTO_MENSAL: Fechamento
FECHAMENTO_QUINZENAL: Fechamento
FECHAMENTO_SEMANAL: Fechamento

class Convenio(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "pessoa_id", "pessoa_nome", "ativo", "fechamento", "dia_fechamento", "prazo_vencimento_dias", "forma_pagamento_id", "forma_pagamento_nome", "emite_nfe", "exige_km", "exige_motorista", "bloqueia_atraso_dias", "obs")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    ATIVO_FIELD_NUMBER: _ClassVar[int]
    FECHAMENTO_FIELD_NUMBER: _ClassVar[int]
    DIA_FECHAMENTO_FIELD_NUMBER: _ClassVar[int]
    PRAZO_VENCIMENTO_DIAS_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    FORMA_PAGAMENTO_NOME_FIELD_NUMBER: _ClassVar[int]
    EMITE_NFE_FIELD_NUMBER: _ClassVar[int]
    EXIGE_KM_FIELD_NUMBER: _ClassVar[int]
    EXIGE_MOTORISTA_FIELD_NUMBER: _ClassVar[int]
    BLOQUEIA_ATRASO_DIAS_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    pessoa_id: str
    pessoa_nome: str
    ativo: bool
    fechamento: Fechamento
    dia_fechamento: int
    prazo_vencimento_dias: int
    forma_pagamento_id: str
    forma_pagamento_nome: str
    emite_nfe: bool
    exige_km: bool
    exige_motorista: bool
    bloqueia_atraso_dias: int
    obs: str
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., pessoa_id: _Optional[str] = ..., pessoa_nome: _Optional[str] = ..., ativo: _Optional[bool] = ..., fechamento: _Optional[_Union[Fechamento, str]] = ..., dia_fechamento: _Optional[int] = ..., prazo_vencimento_dias: _Optional[int] = ..., forma_pagamento_id: _Optional[str] = ..., forma_pagamento_nome: _Optional[str] = ..., emite_nfe: _Optional[bool] = ..., exige_km: _Optional[bool] = ..., exige_motorista: _Optional[bool] = ..., bloqueia_atraso_dias: _Optional[int] = ..., obs: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("convenio",)
    CONVENIO_FIELD_NUMBER: _ClassVar[int]
    convenio: Convenio
    def __init__(self, convenio: _Optional[_Union[Convenio, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("convenio",)
    CONVENIO_FIELD_NUMBER: _ClassVar[int]
    convenio: Convenio
    def __init__(self, convenio: _Optional[_Union[Convenio, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "convenio", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    CONVENIO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    convenio: Convenio
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., convenio: _Optional[_Union[Convenio, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("convenio",)
    CONVENIO_FIELD_NUMBER: _ClassVar[int]
    convenio: Convenio
    def __init__(self, convenio: _Optional[_Union[Convenio, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("convenio",)
    CONVENIO_FIELD_NUMBER: _ClassVar[int]
    convenio: Convenio
    def __init__(self, convenio: _Optional[_Union[Convenio, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("convenio_list", "next_page_token")
    CONVENIO_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    convenio_list: _containers.RepeatedCompositeFieldContainer[Convenio]
    next_page_token: str
    def __init__(self, convenio_list: _Optional[_Iterable[_Union[Convenio, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class FaturaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FaturaResponse(_message.Message):
    __slots__ = ("conta_id", "titulos", "valor")
    CONTA_ID_FIELD_NUMBER: _ClassVar[int]
    TITULOS_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    conta_id: str
    titulos: int
    valor: float
    def __init__(self, conta_id: _Optional[str] = ..., titulos: _Optional[int] = ..., valor: _Optional[float] = ...) -> None: ...
