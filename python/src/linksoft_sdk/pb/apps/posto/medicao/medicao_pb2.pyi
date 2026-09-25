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

class Origem(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORIGEM_UNSPECIFIED: _ClassVar[Origem]
    ORIGEM_MANUAL: _ClassVar[Origem]
    ORIGEM_AUTOMATICA: _ClassVar[Origem]
ORIGEM_UNSPECIFIED: Origem
ORIGEM_MANUAL: Origem
ORIGEM_AUTOMATICA: Origem

class Medicao(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "tanque_id", "tanque_numero", "produto_id", "produto_nome", "data_hora", "volume", "agua", "temperatura", "nivel", "origem", "obs")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    TANQUE_ID_FIELD_NUMBER: _ClassVar[int]
    TANQUE_NUMERO_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    AGUA_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURA_FIELD_NUMBER: _ClassVar[int]
    NIVEL_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    tanque_id: str
    tanque_numero: int
    produto_id: str
    produto_nome: str
    data_hora: _timestamp_pb2.Timestamp
    volume: float
    agua: float
    temperatura: float
    nivel: float
    origem: Origem
    obs: str
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., tanque_id: _Optional[str] = ..., tanque_numero: _Optional[int] = ..., produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ..., data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., volume: _Optional[float] = ..., agua: _Optional[float] = ..., temperatura: _Optional[float] = ..., nivel: _Optional[float] = ..., origem: _Optional[_Union[Origem, str]] = ..., obs: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("medicao",)
    MEDICAO_FIELD_NUMBER: _ClassVar[int]
    medicao: Medicao
    def __init__(self, medicao: _Optional[_Union[Medicao, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("medicao",)
    MEDICAO_FIELD_NUMBER: _ClassVar[int]
    medicao: Medicao
    def __init__(self, medicao: _Optional[_Union[Medicao, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "medicao", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    MEDICAO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    medicao: Medicao
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., medicao: _Optional[_Union[Medicao, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("medicao",)
    MEDICAO_FIELD_NUMBER: _ClassVar[int]
    medicao: Medicao
    def __init__(self, medicao: _Optional[_Union[Medicao, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("medicao",)
    MEDICAO_FIELD_NUMBER: _ClassVar[int]
    medicao: Medicao
    def __init__(self, medicao: _Optional[_Union[Medicao, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("medicao_list", "next_page_token")
    MEDICAO_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    medicao_list: _containers.RepeatedCompositeFieldContainer[Medicao]
    next_page_token: str
    def __init__(self, medicao_list: _Optional[_Iterable[_Union[Medicao, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class LeituraTanque(_message.Message):
    __slots__ = ("tanque_numero", "volume", "agua", "temperatura", "nivel", "data_hora")
    TANQUE_NUMERO_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    AGUA_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURA_FIELD_NUMBER: _ClassVar[int]
    NIVEL_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    tanque_numero: int
    volume: float
    agua: float
    temperatura: float
    nivel: float
    data_hora: _timestamp_pb2.Timestamp
    def __init__(self, tanque_numero: _Optional[int] = ..., volume: _Optional[float] = ..., agua: _Optional[float] = ..., temperatura: _Optional[float] = ..., nivel: _Optional[float] = ..., data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class RecebeRequest(_message.Message):
    __slots__ = ("leituras",)
    LEITURAS_FIELD_NUMBER: _ClassVar[int]
    leituras: _containers.RepeatedCompositeFieldContainer[LeituraTanque]
    def __init__(self, leituras: _Optional[_Iterable[_Union[LeituraTanque, _Mapping]]] = ...) -> None: ...

class RecebeResponse(_message.Message):
    __slots__ = ("tanques_sem_cadastro",)
    TANQUES_SEM_CADASTRO_FIELD_NUMBER: _ClassVar[int]
    tanques_sem_cadastro: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, tanques_sem_cadastro: _Optional[_Iterable[int]] = ...) -> None: ...
