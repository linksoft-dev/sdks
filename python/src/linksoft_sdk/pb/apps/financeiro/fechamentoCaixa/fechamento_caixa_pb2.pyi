import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FechamentoCaixa(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "numero", "situacao", "dataHoraInicial", "dataHoraFinal", "periodoAutomatico", "caixaId", "caixaNome", "usuarioCaixaId", "usuarioCaixaNome", "diferenca", "obs", "valores", "aprovador", "aprovadorId", "dataHoraAprovacao", "motivoRejeicao", "rejeitadoPor", "dataHoraRejeicao", "deviceId")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAINICIAL_FIELD_NUMBER: _ClassVar[int]
    DATAHORAFINAL_FIELD_NUMBER: _ClassVar[int]
    PERIODOAUTOMATICO_FIELD_NUMBER: _ClassVar[int]
    CAIXAID_FIELD_NUMBER: _ClassVar[int]
    CAIXANOME_FIELD_NUMBER: _ClassVar[int]
    USUARIOCAIXAID_FIELD_NUMBER: _ClassVar[int]
    USUARIOCAIXANOME_FIELD_NUMBER: _ClassVar[int]
    DIFERENCA_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    VALORES_FIELD_NUMBER: _ClassVar[int]
    APROVADOR_FIELD_NUMBER: _ClassVar[int]
    APROVADORID_FIELD_NUMBER: _ClassVar[int]
    DATAHORAAPROVACAO_FIELD_NUMBER: _ClassVar[int]
    MOTIVOREJEICAO_FIELD_NUMBER: _ClassVar[int]
    REJEITADOPOR_FIELD_NUMBER: _ClassVar[int]
    DATAHORAREJEICAO_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    numero: int
    situacao: str
    dataHoraInicial: _timestamp_pb2.Timestamp
    dataHoraFinal: _timestamp_pb2.Timestamp
    periodoAutomatico: bool
    caixaId: str
    caixaNome: str
    usuarioCaixaId: str
    usuarioCaixaNome: str
    diferenca: float
    obs: str
    valores: _containers.RepeatedCompositeFieldContainer[Apuracao]
    aprovador: str
    aprovadorId: str
    dataHoraAprovacao: _timestamp_pb2.Timestamp
    motivoRejeicao: str
    rejeitadoPor: str
    dataHoraRejeicao: _timestamp_pb2.Timestamp
    deviceId: str
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., numero: _Optional[int] = ..., situacao: _Optional[str] = ..., dataHoraInicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraFinal: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., periodoAutomatico: _Optional[bool] = ..., caixaId: _Optional[str] = ..., caixaNome: _Optional[str] = ..., usuarioCaixaId: _Optional[str] = ..., usuarioCaixaNome: _Optional[str] = ..., diferenca: _Optional[float] = ..., obs: _Optional[str] = ..., valores: _Optional[_Iterable[_Union[Apuracao, _Mapping]]] = ..., aprovador: _Optional[str] = ..., aprovadorId: _Optional[str] = ..., dataHoraAprovacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., motivoRejeicao: _Optional[str] = ..., rejeitadoPor: _Optional[str] = ..., dataHoraRejeicao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deviceId: _Optional[str] = ...) -> None: ...

class Apuracao(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "fechamentoCaixaId", "tipoPagamento", "valorInformado", "entrada", "saida", "valorApurado", "diferenca")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FECHAMENTOCAIXAID_FIELD_NUMBER: _ClassVar[int]
    TIPOPAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    VALORINFORMADO_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_FIELD_NUMBER: _ClassVar[int]
    SAIDA_FIELD_NUMBER: _ClassVar[int]
    VALORAPURADO_FIELD_NUMBER: _ClassVar[int]
    DIFERENCA_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    fechamentoCaixaId: str
    tipoPagamento: str
    valorInformado: float
    entrada: float
    saida: float
    valorApurado: float
    diferenca: float
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., fechamentoCaixaId: _Optional[str] = ..., tipoPagamento: _Optional[str] = ..., valorInformado: _Optional[float] = ..., entrada: _Optional[float] = ..., saida: _Optional[float] = ..., valorApurado: _Optional[float] = ..., diferenca: _Optional[float] = ...) -> None: ...

class CreateFechamentoCaixaRequest(_message.Message):
    __slots__ = ("fechamentoCaixa",)
    FECHAMENTOCAIXA_FIELD_NUMBER: _ClassVar[int]
    fechamentoCaixa: FechamentoCaixa
    def __init__(self, fechamentoCaixa: _Optional[_Union[FechamentoCaixa, _Mapping]] = ...) -> None: ...

class CreateFechamentoCaixaResponse(_message.Message):
    __slots__ = ("fechamentoCaixa",)
    FECHAMENTOCAIXA_FIELD_NUMBER: _ClassVar[int]
    fechamentoCaixa: FechamentoCaixa
    def __init__(self, fechamentoCaixa: _Optional[_Union[FechamentoCaixa, _Mapping]] = ...) -> None: ...

class UpdateFechamentoCaixaRequest(_message.Message):
    __slots__ = ("id", "fechamentoCaixa", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    FECHAMENTOCAIXA_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    fechamentoCaixa: FechamentoCaixa
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., fechamentoCaixa: _Optional[_Union[FechamentoCaixa, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateFechamentoCaixaResponse(_message.Message):
    __slots__ = ("fechamentoCaixa",)
    FECHAMENTOCAIXA_FIELD_NUMBER: _ClassVar[int]
    fechamentoCaixa: FechamentoCaixa
    def __init__(self, fechamentoCaixa: _Optional[_Union[FechamentoCaixa, _Mapping]] = ...) -> None: ...

class DeleteFechamentoCaixaRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteFechamentoCaixaResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetFechamentoCaixaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetFechamentoCaixaResponse(_message.Message):
    __slots__ = ("fechamentoCaixa",)
    FECHAMENTOCAIXA_FIELD_NUMBER: _ClassVar[int]
    fechamentoCaixa: FechamentoCaixa
    def __init__(self, fechamentoCaixa: _Optional[_Union[FechamentoCaixa, _Mapping]] = ...) -> None: ...

class ListFechamentoCaixaRequest(_message.Message):
    __slots__ = ("ids", "dataHoraInicialGte", "dataHoraInicialLte", "dataHoraFinalGte", "dataHoraFinalLte", "caixaId", "usuarioCaixaId", "situacao", "page_size", "page_token", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    DATAHORAINICIALGTE_FIELD_NUMBER: _ClassVar[int]
    DATAHORAINICIALLTE_FIELD_NUMBER: _ClassVar[int]
    DATAHORAFINALGTE_FIELD_NUMBER: _ClassVar[int]
    DATAHORAFINALLTE_FIELD_NUMBER: _ClassVar[int]
    CAIXAID_FIELD_NUMBER: _ClassVar[int]
    USUARIOCAIXAID_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    dataHoraInicialGte: _timestamp_pb2.Timestamp
    dataHoraInicialLte: _timestamp_pb2.Timestamp
    dataHoraFinalGte: _timestamp_pb2.Timestamp
    dataHoraFinalLte: _timestamp_pb2.Timestamp
    caixaId: str
    usuarioCaixaId: str
    situacao: str
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., dataHoraInicialGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraInicialLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraFinalGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraFinalLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., caixaId: _Optional[str] = ..., usuarioCaixaId: _Optional[str] = ..., situacao: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ReportFechamentoCaixaRequest(_message.Message):
    __slots__ = ("tipo_relatorio", "listFechamentoCaixaRequest")
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    LISTFECHAMENTOCAIXAREQUEST_FIELD_NUMBER: _ClassVar[int]
    tipo_relatorio: str
    listFechamentoCaixaRequest: ListFechamentoCaixaRequest
    def __init__(self, tipo_relatorio: _Optional[str] = ..., listFechamentoCaixaRequest: _Optional[_Union[ListFechamentoCaixaRequest, _Mapping]] = ...) -> None: ...

class ReportFechamentoCaixaResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class ListFechamentoCaixaResponse(_message.Message):
    __slots__ = ("fechamentoCaixaList", "next_page_token")
    FECHAMENTOCAIXALIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    fechamentoCaixaList: _containers.RepeatedCompositeFieldContainer[FechamentoCaixa]
    next_page_token: str
    def __init__(self, fechamentoCaixaList: _Optional[_Iterable[_Union[FechamentoCaixa, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AceitaFechamentoRequest(_message.Message):
    __slots__ = ("id", "realizarSangria", "caixaDestinoId", "caixaDestinoNome")
    ID_FIELD_NUMBER: _ClassVar[int]
    REALIZARSANGRIA_FIELD_NUMBER: _ClassVar[int]
    CAIXADESTINOID_FIELD_NUMBER: _ClassVar[int]
    CAIXADESTINONOME_FIELD_NUMBER: _ClassVar[int]
    id: str
    realizarSangria: bool
    caixaDestinoId: str
    caixaDestinoNome: str
    def __init__(self, id: _Optional[str] = ..., realizarSangria: _Optional[bool] = ..., caixaDestinoId: _Optional[str] = ..., caixaDestinoNome: _Optional[str] = ...) -> None: ...

class AceitaFechamentoResponse(_message.Message):
    __slots__ = ("fechamentoCaixa",)
    FECHAMENTOCAIXA_FIELD_NUMBER: _ClassVar[int]
    fechamentoCaixa: FechamentoCaixa
    def __init__(self, fechamentoCaixa: _Optional[_Union[FechamentoCaixa, _Mapping]] = ...) -> None: ...

class RejeitaFechamentoRequest(_message.Message):
    __slots__ = ("id", "motivo")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    id: str
    motivo: str
    def __init__(self, id: _Optional[str] = ..., motivo: _Optional[str] = ...) -> None: ...

class RejeitaFechamentoResponse(_message.Message):
    __slots__ = ("fechamentoCaixa",)
    FECHAMENTOCAIXA_FIELD_NUMBER: _ClassVar[int]
    fechamentoCaixa: FechamentoCaixa
    def __init__(self, fechamentoCaixa: _Optional[_Union[FechamentoCaixa, _Mapping]] = ...) -> None: ...

class FechamentoCaixaRapidoRequest(_message.Message):
    __slots__ = ("dinheiro", "pix", "cartao_credito", "cartao_debito", "duplicata", "cheque")
    DINHEIRO_FIELD_NUMBER: _ClassVar[int]
    PIX_FIELD_NUMBER: _ClassVar[int]
    CARTAO_CREDITO_FIELD_NUMBER: _ClassVar[int]
    CARTAO_DEBITO_FIELD_NUMBER: _ClassVar[int]
    DUPLICATA_FIELD_NUMBER: _ClassVar[int]
    CHEQUE_FIELD_NUMBER: _ClassVar[int]
    dinheiro: float
    pix: float
    cartao_credito: float
    cartao_debito: float
    duplicata: float
    cheque: float
    def __init__(self, dinheiro: _Optional[float] = ..., pix: _Optional[float] = ..., cartao_credito: _Optional[float] = ..., cartao_debito: _Optional[float] = ..., duplicata: _Optional[float] = ..., cheque: _Optional[float] = ...) -> None: ...

class FechamentoCaixaRapidoResponse(_message.Message):
    __slots__ = ("fechamentoCaixa", "success", "message")
    FECHAMENTOCAIXA_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    fechamentoCaixa: FechamentoCaixa
    success: bool
    message: str
    def __init__(self, fechamentoCaixa: _Optional[_Union[FechamentoCaixa, _Mapping]] = ..., success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...

class UpdateApuracaoRequest(_message.Message):
    __slots__ = ("fechamentoCaixaId", "id", "apuracao", "update_mask")
    FECHAMENTOCAIXAID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    APURACAO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    fechamentoCaixaId: str
    id: str
    apuracao: Apuracao
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, fechamentoCaixaId: _Optional[str] = ..., id: _Optional[str] = ..., apuracao: _Optional[_Union[Apuracao, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateApuracaoResponse(_message.Message):
    __slots__ = ("apuracao",)
    APURACAO_FIELD_NUMBER: _ClassVar[int]
    apuracao: Apuracao
    def __init__(self, apuracao: _Optional[_Union[Apuracao, _Mapping]] = ...) -> None: ...

class FechamentoCaixaImprimirRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FechamentoCaixaImprimirResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class FechamentoCaixaValeDiferencaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class FechamentoCaixaValeDiferencaResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...
