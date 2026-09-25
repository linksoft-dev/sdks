import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.apps.vendas.pedido import pedido_pb2 as _pedido_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetUltimaOsPorNumeroSerieRequest(_message.Message):
    __slots__ = ("numeroSerie",)
    NUMEROSERIE_FIELD_NUMBER: _ClassVar[int]
    numeroSerie: str
    def __init__(self, numeroSerie: _Optional[str] = ...) -> None: ...

class GetUltimaOsPorNumeroSerieResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: _pedido_pb2.Pedido
    def __init__(self, pedido: _Optional[_Union[_pedido_pb2.Pedido, _Mapping]] = ...) -> None: ...

class HistoricoEquipamentoRequest(_message.Message):
    __slots__ = ("numeroSerie",)
    NUMEROSERIE_FIELD_NUMBER: _ClassVar[int]
    numeroSerie: str
    def __init__(self, numeroSerie: _Optional[str] = ...) -> None: ...

class HistoricoEquipamentoItem(_message.Message):
    __slots__ = ("id", "numero", "tipo", "situacao", "dataHoraRegistro", "dataHoraFechamento", "clienteNome", "valorTotal", "defeitoReclamado", "produtos", "servicos")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAREGISTRO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAFECHAMENTO_FIELD_NUMBER: _ClassVar[int]
    CLIENTENOME_FIELD_NUMBER: _ClassVar[int]
    VALORTOTAL_FIELD_NUMBER: _ClassVar[int]
    DEFEITORECLAMADO_FIELD_NUMBER: _ClassVar[int]
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    SERVICOS_FIELD_NUMBER: _ClassVar[int]
    id: str
    numero: int
    tipo: str
    situacao: str
    dataHoraRegistro: _timestamp_pb2.Timestamp
    dataHoraFechamento: _timestamp_pb2.Timestamp
    clienteNome: str
    valorTotal: float
    defeitoReclamado: str
    produtos: _containers.RepeatedScalarFieldContainer[str]
    servicos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., numero: _Optional[int] = ..., tipo: _Optional[str] = ..., situacao: _Optional[str] = ..., dataHoraRegistro: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraFechamento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., clienteNome: _Optional[str] = ..., valorTotal: _Optional[float] = ..., defeitoReclamado: _Optional[str] = ..., produtos: _Optional[_Iterable[str]] = ..., servicos: _Optional[_Iterable[str]] = ...) -> None: ...

class HistoricoEquipamentoResponse(_message.Message):
    __slots__ = ("itens",)
    ITENS_FIELD_NUMBER: _ClassVar[int]
    itens: _containers.RepeatedCompositeFieldContainer[HistoricoEquipamentoItem]
    def __init__(self, itens: _Optional[_Iterable[_Union[HistoricoEquipamentoItem, _Mapping]]] = ...) -> None: ...
