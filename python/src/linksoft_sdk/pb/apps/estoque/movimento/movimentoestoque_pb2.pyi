import datetime

from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MovimentoEstoque(_message.Message):
    __slots__ = ("createdAt", "id", "fields", "userId", "userName", "estoqueNome", "produtoId", "tipo", "quantidade", "valorUnitario", "origem", "origemId", "origemNumero", "obs", "pessoaId", "pessoaNome", "produtoNome", "qAnterior", "qAtual", "variation_id", "variation_sku", "variation_display_name")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ESTOQUENOME_FIELD_NUMBER: _ClassVar[int]
    PRODUTOID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    VALORUNITARIO_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    ORIGEMID_FIELD_NUMBER: _ClassVar[int]
    ORIGEMNUMERO_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    PESSOAID_FIELD_NUMBER: _ClassVar[int]
    PESSOANOME_FIELD_NUMBER: _ClassVar[int]
    PRODUTONOME_FIELD_NUMBER: _ClassVar[int]
    QANTERIOR_FIELD_NUMBER: _ClassVar[int]
    QATUAL_FIELD_NUMBER: _ClassVar[int]
    VARIATION_ID_FIELD_NUMBER: _ClassVar[int]
    VARIATION_SKU_FIELD_NUMBER: _ClassVar[int]
    VARIATION_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    id: str
    fields: _metadata_pb2.BasicFields
    userId: str
    userName: str
    estoqueNome: str
    produtoId: str
    tipo: str
    quantidade: float
    valorUnitario: float
    origem: str
    origemId: str
    origemNumero: str
    obs: str
    pessoaId: str
    pessoaNome: str
    produtoNome: str
    qAnterior: float
    qAtual: float
    variation_id: str
    variation_sku: str
    variation_display_name: str
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., estoqueNome: _Optional[str] = ..., produtoId: _Optional[str] = ..., tipo: _Optional[str] = ..., quantidade: _Optional[float] = ..., valorUnitario: _Optional[float] = ..., origem: _Optional[str] = ..., origemId: _Optional[str] = ..., origemNumero: _Optional[str] = ..., obs: _Optional[str] = ..., pessoaId: _Optional[str] = ..., pessoaNome: _Optional[str] = ..., produtoNome: _Optional[str] = ..., qAnterior: _Optional[float] = ..., qAtual: _Optional[float] = ..., variation_id: _Optional[str] = ..., variation_sku: _Optional[str] = ..., variation_display_name: _Optional[str] = ...) -> None: ...
