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

class ProdutoPermitido(_message.Message):
    __slots__ = ("produto_id", "produto_nome")
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    produto_id: str
    produto_nome: str
    def __init__(self, produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ...) -> None: ...

class Motorista(_message.Message):
    __slots__ = ("nome", "cpf")
    NOME_FIELD_NUMBER: _ClassVar[int]
    CPF_FIELD_NUMBER: _ClassVar[int]
    nome: str
    cpf: str
    def __init__(self, nome: _Optional[str] = ..., cpf: _Optional[str] = ...) -> None: ...

class Veiculo(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "pessoa_id", "pessoa_nome", "placa", "modelo", "combustiveis", "limite_litros_abastecimento", "limite_valor_abastecimento", "limite_litros_dia", "limite_litros_mes", "motoristas", "ultimo_km", "ativo", "obs", "tag")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    PESSOA_NOME_FIELD_NUMBER: _ClassVar[int]
    PLACA_FIELD_NUMBER: _ClassVar[int]
    MODELO_FIELD_NUMBER: _ClassVar[int]
    COMBUSTIVEIS_FIELD_NUMBER: _ClassVar[int]
    LIMITE_LITROS_ABASTECIMENTO_FIELD_NUMBER: _ClassVar[int]
    LIMITE_VALOR_ABASTECIMENTO_FIELD_NUMBER: _ClassVar[int]
    LIMITE_LITROS_DIA_FIELD_NUMBER: _ClassVar[int]
    LIMITE_LITROS_MES_FIELD_NUMBER: _ClassVar[int]
    MOTORISTAS_FIELD_NUMBER: _ClassVar[int]
    ULTIMO_KM_FIELD_NUMBER: _ClassVar[int]
    ATIVO_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    pessoa_id: str
    pessoa_nome: str
    placa: str
    modelo: str
    combustiveis: _containers.RepeatedCompositeFieldContainer[ProdutoPermitido]
    limite_litros_abastecimento: float
    limite_valor_abastecimento: float
    limite_litros_dia: float
    limite_litros_mes: float
    motoristas: _containers.RepeatedCompositeFieldContainer[Motorista]
    ultimo_km: float
    ativo: bool
    obs: str
    tag: str
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., pessoa_id: _Optional[str] = ..., pessoa_nome: _Optional[str] = ..., placa: _Optional[str] = ..., modelo: _Optional[str] = ..., combustiveis: _Optional[_Iterable[_Union[ProdutoPermitido, _Mapping]]] = ..., limite_litros_abastecimento: _Optional[float] = ..., limite_valor_abastecimento: _Optional[float] = ..., limite_litros_dia: _Optional[float] = ..., limite_litros_mes: _Optional[float] = ..., motoristas: _Optional[_Iterable[_Union[Motorista, _Mapping]]] = ..., ultimo_km: _Optional[float] = ..., ativo: _Optional[bool] = ..., obs: _Optional[str] = ..., tag: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("veiculo",)
    VEICULO_FIELD_NUMBER: _ClassVar[int]
    veiculo: Veiculo
    def __init__(self, veiculo: _Optional[_Union[Veiculo, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("veiculo",)
    VEICULO_FIELD_NUMBER: _ClassVar[int]
    veiculo: Veiculo
    def __init__(self, veiculo: _Optional[_Union[Veiculo, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "veiculo", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    VEICULO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    veiculo: Veiculo
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., veiculo: _Optional[_Union[Veiculo, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("veiculo",)
    VEICULO_FIELD_NUMBER: _ClassVar[int]
    veiculo: Veiculo
    def __init__(self, veiculo: _Optional[_Union[Veiculo, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("veiculo",)
    VEICULO_FIELD_NUMBER: _ClassVar[int]
    veiculo: Veiculo
    def __init__(self, veiculo: _Optional[_Union[Veiculo, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("veiculo_list", "next_page_token")
    VEICULO_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    veiculo_list: _containers.RepeatedCompositeFieldContainer[Veiculo]
    next_page_token: str
    def __init__(self, veiculo_list: _Optional[_Iterable[_Union[Veiculo, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AutorizaRequest(_message.Message):
    __slots__ = ("pedido_id",)
    PEDIDO_ID_FIELD_NUMBER: _ClassVar[int]
    pedido_id: str
    def __init__(self, pedido_id: _Optional[str] = ...) -> None: ...

class AutorizaResponse(_message.Message):
    __slots__ = ("veiculo", "litros_dia", "litros_mes")
    VEICULO_FIELD_NUMBER: _ClassVar[int]
    LITROS_DIA_FIELD_NUMBER: _ClassVar[int]
    LITROS_MES_FIELD_NUMBER: _ClassVar[int]
    veiculo: Veiculo
    litros_dia: float
    litros_mes: float
    def __init__(self, veiculo: _Optional[_Union[Veiculo, _Mapping]] = ..., litros_dia: _Optional[float] = ..., litros_mes: _Optional[float] = ...) -> None: ...

class TagsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TagVeiculo(_message.Message):
    __slots__ = ("tag", "placa", "cliente", "limite_litros", "nivel_preco")
    TAG_FIELD_NUMBER: _ClassVar[int]
    PLACA_FIELD_NUMBER: _ClassVar[int]
    CLIENTE_FIELD_NUMBER: _ClassVar[int]
    LIMITE_LITROS_FIELD_NUMBER: _ClassVar[int]
    NIVEL_PRECO_FIELD_NUMBER: _ClassVar[int]
    tag: str
    placa: str
    cliente: str
    limite_litros: float
    nivel_preco: int
    def __init__(self, tag: _Optional[str] = ..., placa: _Optional[str] = ..., cliente: _Optional[str] = ..., limite_litros: _Optional[float] = ..., nivel_preco: _Optional[int] = ...) -> None: ...

class TagsResponse(_message.Message):
    __slots__ = ("tags",)
    TAGS_FIELD_NUMBER: _ClassVar[int]
    tags: _containers.RepeatedCompositeFieldContainer[TagVeiculo]
    def __init__(self, tags: _Optional[_Iterable[_Union[TagVeiculo, _Mapping]]] = ...) -> None: ...
