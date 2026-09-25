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

class Situacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SITUACAO_NAO_ESPECIFICADA: _ClassVar[Situacao]
    SITUACAO_PENDENTE: _ClassVar[Situacao]
    SITUACAO_FINALIZADA: _ClassVar[Situacao]
    SITUACAO_CANCELADA: _ClassVar[Situacao]
SITUACAO_NAO_ESPECIFICADA: Situacao
SITUACAO_PENDENTE: Situacao
SITUACAO_FINALIZADA: Situacao
SITUACAO_CANCELADA: Situacao

class Pessoa(_message.Message):
    __slots__ = ("id", "cpf_cnpj", "nome", "nome_2", "ie", "end_cep", "end_endereco", "end_numero", "end_bairro", "end_cidade", "end_cidade_cod", "end_uf", "end_complemento", "email", "telefone")
    ID_FIELD_NUMBER: _ClassVar[int]
    CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    NOME_2_FIELD_NUMBER: _ClassVar[int]
    IE_FIELD_NUMBER: _ClassVar[int]
    END_CEP_FIELD_NUMBER: _ClassVar[int]
    END_ENDERECO_FIELD_NUMBER: _ClassVar[int]
    END_NUMERO_FIELD_NUMBER: _ClassVar[int]
    END_BAIRRO_FIELD_NUMBER: _ClassVar[int]
    END_CIDADE_FIELD_NUMBER: _ClassVar[int]
    END_CIDADE_COD_FIELD_NUMBER: _ClassVar[int]
    END_UF_FIELD_NUMBER: _ClassVar[int]
    END_COMPLEMENTO_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    TELEFONE_FIELD_NUMBER: _ClassVar[int]
    id: str
    cpf_cnpj: str
    nome: str
    nome_2: str
    ie: str
    end_cep: str
    end_endereco: str
    end_numero: str
    end_bairro: str
    end_cidade: str
    end_cidade_cod: str
    end_uf: str
    end_complemento: str
    email: str
    telefone: str
    def __init__(self, id: _Optional[str] = ..., cpf_cnpj: _Optional[str] = ..., nome: _Optional[str] = ..., nome_2: _Optional[str] = ..., ie: _Optional[str] = ..., end_cep: _Optional[str] = ..., end_endereco: _Optional[str] = ..., end_numero: _Optional[str] = ..., end_bairro: _Optional[str] = ..., end_cidade: _Optional[str] = ..., end_cidade_cod: _Optional[str] = ..., end_uf: _Optional[str] = ..., end_complemento: _Optional[str] = ..., email: _Optional[str] = ..., telefone: _Optional[str] = ...) -> None: ...

class EntradasAvulsa(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "numero", "pessoa", "data_hora_entrada", "situacao", "motivo_cancelamento", "data_hora_cancelamento", "cancelamento_usuario_id", "cancelamento_usuario_nome", "obs", "total", "produtos")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    PESSOA_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_ENTRADA_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_USUARIO_ID_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_USUARIO_NOME_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    numero: int
    pessoa: Pessoa
    data_hora_entrada: _timestamp_pb2.Timestamp
    situacao: Situacao
    motivo_cancelamento: str
    data_hora_cancelamento: _timestamp_pb2.Timestamp
    cancelamento_usuario_id: str
    cancelamento_usuario_nome: str
    obs: str
    total: float
    produtos: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., numero: _Optional[int] = ..., pessoa: _Optional[_Union[Pessoa, _Mapping]] = ..., data_hora_entrada: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., situacao: _Optional[_Union[Situacao, str]] = ..., motivo_cancelamento: _Optional[str] = ..., data_hora_cancelamento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cancelamento_usuario_id: _Optional[str] = ..., cancelamento_usuario_nome: _Optional[str] = ..., obs: _Optional[str] = ..., total: _Optional[float] = ..., produtos: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "produto_id", "produto_nome", "un", "servico_nome", "servico_id", "obs", "valor_unitario", "quantidade", "total", "variation_product_id")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    SERVICO_NOME_FIELD_NUMBER: _ClassVar[int]
    SERVICO_ID_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    VARIATION_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    produto_id: str
    produto_nome: str
    un: str
    servico_nome: str
    servico_id: str
    obs: str
    valor_unitario: float
    quantidade: float
    total: float
    variation_product_id: str
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ..., un: _Optional[str] = ..., servico_nome: _Optional[str] = ..., servico_id: _Optional[str] = ..., obs: _Optional[str] = ..., valor_unitario: _Optional[float] = ..., quantidade: _Optional[float] = ..., total: _Optional[float] = ..., variation_product_id: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("entradas_avulsa",)
    ENTRADAS_AVULSA_FIELD_NUMBER: _ClassVar[int]
    entradas_avulsa: EntradasAvulsa
    def __init__(self, entradas_avulsa: _Optional[_Union[EntradasAvulsa, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("entradas_avulsa",)
    ENTRADAS_AVULSA_FIELD_NUMBER: _ClassVar[int]
    entradas_avulsa: EntradasAvulsa
    def __init__(self, entradas_avulsa: _Optional[_Union[EntradasAvulsa, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "entradas_avulsa", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    ENTRADAS_AVULSA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    entradas_avulsa: EntradasAvulsa
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., entradas_avulsa: _Optional[_Union[EntradasAvulsa, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("entradas_avulsa",)
    ENTRADAS_AVULSA_FIELD_NUMBER: _ClassVar[int]
    entradas_avulsa: EntradasAvulsa
    def __init__(self, entradas_avulsa: _Optional[_Union[EntradasAvulsa, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("entradas_avulsa",)
    ENTRADAS_AVULSA_FIELD_NUMBER: _ClassVar[int]
    entradas_avulsa: EntradasAvulsa
    def __init__(self, entradas_avulsa: _Optional[_Union[EntradasAvulsa, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "page_size", "page_token", "filter", "created_at_gte", "created_at_lte", "data_hora_cancelamento_gte", "data_hora_cancelamento_lte", "total_gte", "total_lte", "pessoa_id", "situacao", "situacao_in", "produto_id_contem")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_CANCELAMENTO_GTE_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_CANCELAMENTO_LTE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GTE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LTE_FIELD_NUMBER: _ClassVar[int]
    PESSOA_ID_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_IN_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_CONTEM_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    data_hora_cancelamento_gte: _timestamp_pb2.Timestamp
    data_hora_cancelamento_lte: _timestamp_pb2.Timestamp
    total_gte: float
    total_lte: float
    pessoa_id: str
    situacao: Situacao
    situacao_in: _containers.RepeatedScalarFieldContainer[str]
    produto_id_contem: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_cancelamento_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_cancelamento_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., total_gte: _Optional[float] = ..., total_lte: _Optional[float] = ..., pessoa_id: _Optional[str] = ..., situacao: _Optional[_Union[Situacao, str]] = ..., situacao_in: _Optional[_Iterable[str]] = ..., produto_id_contem: _Optional[str] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("entradas_avulsa_list", "next_page_token")
    ENTRADAS_AVULSA_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entradas_avulsa_list: _containers.RepeatedCompositeFieldContainer[EntradasAvulsa]
    next_page_token: str
    def __init__(self, entradas_avulsa_list: _Optional[_Iterable[_Union[EntradasAvulsa, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AddProdutoRequest(_message.Message):
    __slots__ = ("entrada_id", "item")
    ENTRADA_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    entrada_id: str
    item: Item
    def __init__(self, entrada_id: _Optional[str] = ..., item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class AddProdutoResponse(_message.Message):
    __slots__ = ("entradas_avulsa",)
    ENTRADAS_AVULSA_FIELD_NUMBER: _ClassVar[int]
    entradas_avulsa: EntradasAvulsa
    def __init__(self, entradas_avulsa: _Optional[_Union[EntradasAvulsa, _Mapping]] = ...) -> None: ...

class UpdateProdutoRequest(_message.Message):
    __slots__ = ("entrada_id", "item_id", "item")
    ENTRADA_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    entrada_id: str
    item_id: str
    item: Item
    def __init__(self, entrada_id: _Optional[str] = ..., item_id: _Optional[str] = ..., item: _Optional[_Union[Item, _Mapping]] = ...) -> None: ...

class UpdateProdutoResponse(_message.Message):
    __slots__ = ("entradas_avulsa",)
    ENTRADAS_AVULSA_FIELD_NUMBER: _ClassVar[int]
    entradas_avulsa: EntradasAvulsa
    def __init__(self, entradas_avulsa: _Optional[_Union[EntradasAvulsa, _Mapping]] = ...) -> None: ...

class DeleteProdutoRequest(_message.Message):
    __slots__ = ("entrada_id", "item_id")
    ENTRADA_ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    entrada_id: str
    item_id: str
    def __init__(self, entrada_id: _Optional[str] = ..., item_id: _Optional[str] = ...) -> None: ...

class DeleteProdutoResponse(_message.Message):
    __slots__ = ("entradas_avulsa",)
    ENTRADAS_AVULSA_FIELD_NUMBER: _ClassVar[int]
    entradas_avulsa: EntradasAvulsa
    def __init__(self, entradas_avulsa: _Optional[_Union[EntradasAvulsa, _Mapping]] = ...) -> None: ...

class FinalizaRequest(_message.Message):
    __slots__ = ("entrada_id",)
    ENTRADA_ID_FIELD_NUMBER: _ClassVar[int]
    entrada_id: str
    def __init__(self, entrada_id: _Optional[str] = ...) -> None: ...

class FinalizaResponse(_message.Message):
    __slots__ = ("entradas_avulsa",)
    ENTRADAS_AVULSA_FIELD_NUMBER: _ClassVar[int]
    entradas_avulsa: EntradasAvulsa
    def __init__(self, entradas_avulsa: _Optional[_Union[EntradasAvulsa, _Mapping]] = ...) -> None: ...

class CancelaRequest(_message.Message):
    __slots__ = ("entrada_id", "motivo")
    ENTRADA_ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    entrada_id: str
    motivo: str
    def __init__(self, entrada_id: _Optional[str] = ..., motivo: _Optional[str] = ...) -> None: ...

class CancelaResponse(_message.Message):
    __slots__ = ("entradas_avulsa",)
    ENTRADAS_AVULSA_FIELD_NUMBER: _ClassVar[int]
    entradas_avulsa: EntradasAvulsa
    def __init__(self, entradas_avulsa: _Optional[_Union[EntradasAvulsa, _Mapping]] = ...) -> None: ...
