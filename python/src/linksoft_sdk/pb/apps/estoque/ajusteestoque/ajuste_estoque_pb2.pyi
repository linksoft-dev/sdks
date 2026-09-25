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

class Produto(_message.Message):
    __slots__ = ("id", "produtoId", "nome", "codigo", "un", "obs", "quantidade", "ajusteExecutado", "userId", "userName", "createdAt", "updatedAt", "variationProductId")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTOID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    AJUSTEEXECUTADO_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    VARIATIONPRODUCTID_FIELD_NUMBER: _ClassVar[int]
    id: str
    produtoId: str
    nome: str
    codigo: str
    un: str
    obs: str
    quantidade: float
    ajusteExecutado: bool
    userId: str
    userName: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    variationProductId: str
    def __init__(self, id: _Optional[str] = ..., produtoId: _Optional[str] = ..., nome: _Optional[str] = ..., codigo: _Optional[str] = ..., un: _Optional[str] = ..., obs: _Optional[str] = ..., quantidade: _Optional[float] = ..., ajusteExecutado: _Optional[bool] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., variationProductId: _Optional[str] = ...) -> None: ...

class Categoria(_message.Message):
    __slots__ = ("id", "categoriaId", "categoriaNome", "createdAt", "updatedAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIAID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIANOME_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    categoriaId: str
    categoriaNome: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., categoriaId: _Optional[str] = ..., categoriaNome: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class AjusteEstoque(_message.Message):
    __slots__ = ("id", "numero", "situacao", "dataHoraFinalizacao", "estoqueId", "estoqueNome", "obs", "produtos", "categorias", "userId", "userName", "zerarEstoque", "createdAt", "updatedAt")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAFINALIZACAO_FIELD_NUMBER: _ClassVar[int]
    ESTOQUEID_FIELD_NUMBER: _ClassVar[int]
    ESTOQUENOME_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIAS_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ZERARESTOQUE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    numero: int
    situacao: str
    dataHoraFinalizacao: _timestamp_pb2.Timestamp
    estoqueId: str
    estoqueNome: str
    obs: str
    produtos: _containers.RepeatedCompositeFieldContainer[Produto]
    categorias: _containers.RepeatedCompositeFieldContainer[Categoria]
    userId: str
    userName: str
    zerarEstoque: bool
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., numero: _Optional[int] = ..., situacao: _Optional[str] = ..., dataHoraFinalizacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., estoqueId: _Optional[str] = ..., estoqueNome: _Optional[str] = ..., obs: _Optional[str] = ..., produtos: _Optional[_Iterable[_Union[Produto, _Mapping]]] = ..., categorias: _Optional[_Iterable[_Union[Categoria, _Mapping]]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., zerarEstoque: _Optional[bool] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAjusteEstoqueRequest(_message.Message):
    __slots__ = ("ajusteEstoque",)
    AJUSTEESTOQUE_FIELD_NUMBER: _ClassVar[int]
    ajusteEstoque: AjusteEstoque
    def __init__(self, ajusteEstoque: _Optional[_Union[AjusteEstoque, _Mapping]] = ...) -> None: ...

class CreateAjusteEstoqueResponse(_message.Message):
    __slots__ = ("ajusteEstoque",)
    AJUSTEESTOQUE_FIELD_NUMBER: _ClassVar[int]
    ajusteEstoque: AjusteEstoque
    def __init__(self, ajusteEstoque: _Optional[_Union[AjusteEstoque, _Mapping]] = ...) -> None: ...

class UpdateAjusteEstoqueRequest(_message.Message):
    __slots__ = ("id", "ajusteEstoque", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    AJUSTEESTOQUE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    ajusteEstoque: AjusteEstoque
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., ajusteEstoque: _Optional[_Union[AjusteEstoque, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateAjusteEstoqueResponse(_message.Message):
    __slots__ = ("ajusteEstoque",)
    AJUSTEESTOQUE_FIELD_NUMBER: _ClassVar[int]
    ajusteEstoque: AjusteEstoque
    def __init__(self, ajusteEstoque: _Optional[_Union[AjusteEstoque, _Mapping]] = ...) -> None: ...

class DeleteAjusteEstoqueRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteAjusteEstoqueResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetAjusteEstoqueRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetAjusteEstoqueResponse(_message.Message):
    __slots__ = ("ajusteEstoque",)
    AJUSTEESTOQUE_FIELD_NUMBER: _ClassVar[int]
    ajusteEstoque: AjusteEstoque
    def __init__(self, ajusteEstoque: _Optional[_Union[AjusteEstoque, _Mapping]] = ...) -> None: ...

class ListAjusteEstoqueRequest(_message.Message):
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

class ListAjusteEstoqueResponse(_message.Message):
    __slots__ = ("ajusteEstoqueList", "next_page_token")
    AJUSTEESTOQUELIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ajusteEstoqueList: _containers.RepeatedCompositeFieldContainer[AjusteEstoque]
    next_page_token: str
    def __init__(self, ajusteEstoqueList: _Optional[_Iterable[_Union[AjusteEstoque, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AjusteEstoqueResponse(_message.Message):
    __slots__ = ("ajusteEstoque",)
    AJUSTEESTOQUE_FIELD_NUMBER: _ClassVar[int]
    ajusteEstoque: AjusteEstoque
    def __init__(self, ajusteEstoque: _Optional[_Union[AjusteEstoque, _Mapping]] = ...) -> None: ...

class AddProdutoRequest(_message.Message):
    __slots__ = ("ajusteId", "produto")
    AJUSTEID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    ajusteId: str
    produto: Produto
    def __init__(self, ajusteId: _Optional[str] = ..., produto: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class UpdateProdutoRequest(_message.Message):
    __slots__ = ("ajusteId", "itemId", "produto")
    AJUSTEID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    ajusteId: str
    itemId: str
    produto: Produto
    def __init__(self, ajusteId: _Optional[str] = ..., itemId: _Optional[str] = ..., produto: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class DeleteProdutoRequest(_message.Message):
    __slots__ = ("ajusteId", "itemId")
    AJUSTEID_FIELD_NUMBER: _ClassVar[int]
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    ajusteId: str
    itemId: str
    def __init__(self, ajusteId: _Optional[str] = ..., itemId: _Optional[str] = ...) -> None: ...

class AddCategoriaRequest(_message.Message):
    __slots__ = ("ajusteId", "categoria")
    AJUSTEID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    ajusteId: str
    categoria: Categoria
    def __init__(self, ajusteId: _Optional[str] = ..., categoria: _Optional[_Union[Categoria, _Mapping]] = ...) -> None: ...

class FinalizaAjusteRequest(_message.Message):
    __slots__ = ("ajusteId",)
    AJUSTEID_FIELD_NUMBER: _ClassVar[int]
    ajusteId: str
    def __init__(self, ajusteId: _Optional[str] = ...) -> None: ...
