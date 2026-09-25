import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetSummaryRequest(_message.Message):
    __slots__ = ("to",)
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: _timestamp_pb2.Timestamp
    def __init__(self, to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class GetSummaryResponse(_message.Message):
    __slots__ = ("period", "kpis", "resumos", "status_mensal", "impostos", "cfops", "resumo_por_finalidade")
    PERIOD_FIELD_NUMBER: _ClassVar[int]
    KPIS_FIELD_NUMBER: _ClassVar[int]
    RESUMOS_FIELD_NUMBER: _ClassVar[int]
    STATUS_MENSAL_FIELD_NUMBER: _ClassVar[int]
    IMPOSTOS_FIELD_NUMBER: _ClassVar[int]
    CFOPS_FIELD_NUMBER: _ClassVar[int]
    RESUMO_POR_FINALIDADE_FIELD_NUMBER: _ClassVar[int]
    period: Period
    kpis: Kpis
    resumos: Resumos
    status_mensal: _containers.RepeatedCompositeFieldContainer[StatusMensalItem]
    impostos: _containers.RepeatedCompositeFieldContainer[ImpostosItem]
    cfops: _containers.RepeatedCompositeFieldContainer[CfopItem]
    resumo_por_finalidade: _containers.RepeatedCompositeFieldContainer[ResumoPorFinalidadeItem]
    def __init__(self, period: _Optional[_Union[Period, _Mapping]] = ..., kpis: _Optional[_Union[Kpis, _Mapping]] = ..., resumos: _Optional[_Union[Resumos, _Mapping]] = ..., status_mensal: _Optional[_Iterable[_Union[StatusMensalItem, _Mapping]]] = ..., impostos: _Optional[_Iterable[_Union[ImpostosItem, _Mapping]]] = ..., cfops: _Optional[_Iterable[_Union[CfopItem, _Mapping]]] = ..., resumo_por_finalidade: _Optional[_Iterable[_Union[ResumoPorFinalidadeItem, _Mapping]]] = ...) -> None: ...

class ResumoPorFinalidadeItem(_message.Message):
    __slots__ = ("tipo_documento", "finalidade_codigo", "quantidade", "valor")
    TIPO_DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    FINALIDADE_CODIGO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    tipo_documento: str
    finalidade_codigo: str
    quantidade: int
    valor: float
    def __init__(self, tipo_documento: _Optional[str] = ..., finalidade_codigo: _Optional[str] = ..., quantidade: _Optional[int] = ..., valor: _Optional[float] = ...) -> None: ...

class Period(_message.Message):
    __slots__ = ("to", "prev_from", "prev_to")
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    PREV_FROM_FIELD_NUMBER: _ClassVar[int]
    PREV_TO_FIELD_NUMBER: _ClassVar[int]
    to: _timestamp_pb2.Timestamp
    prev_from: _timestamp_pb2.Timestamp
    prev_to: _timestamp_pb2.Timestamp
    def __init__(self, to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., prev_from: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., prev_to: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., **kwargs) -> None: ...

class KpiValue(_message.Message):
    __slots__ = ("value", "previous", "variation", "has_variation")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    VARIATION_FIELD_NUMBER: _ClassVar[int]
    HAS_VARIATION_FIELD_NUMBER: _ClassVar[int]
    value: float
    previous: float
    variation: float
    has_variation: bool
    def __init__(self, value: _Optional[float] = ..., previous: _Optional[float] = ..., variation: _Optional[float] = ..., has_variation: _Optional[bool] = ...) -> None: ...

class Kpis(_message.Message):
    __slots__ = ("valor_total_emitido", "qtd_notas_emitidas", "ticket_medio", "notas_canceladas", "valor_canceladas")
    VALOR_TOTAL_EMITIDO_FIELD_NUMBER: _ClassVar[int]
    QTD_NOTAS_EMITIDAS_FIELD_NUMBER: _ClassVar[int]
    TICKET_MEDIO_FIELD_NUMBER: _ClassVar[int]
    NOTAS_CANCELADAS_FIELD_NUMBER: _ClassVar[int]
    VALOR_CANCELADAS_FIELD_NUMBER: _ClassVar[int]
    valor_total_emitido: KpiValue
    qtd_notas_emitidas: KpiValue
    ticket_medio: KpiValue
    notas_canceladas: KpiValue
    valor_canceladas: KpiValue
    def __init__(self, valor_total_emitido: _Optional[_Union[KpiValue, _Mapping]] = ..., qtd_notas_emitidas: _Optional[_Union[KpiValue, _Mapping]] = ..., ticket_medio: _Optional[_Union[KpiValue, _Mapping]] = ..., notas_canceladas: _Optional[_Union[KpiValue, _Mapping]] = ..., valor_canceladas: _Optional[_Union[KpiValue, _Mapping]] = ...) -> None: ...

class ResumoItem(_message.Message):
    __slots__ = ("valor", "quantidade")
    VALOR_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    valor: float
    quantidade: int
    def __init__(self, valor: _Optional[float] = ..., quantidade: _Optional[int] = ...) -> None: ...

class Resumos(_message.Message):
    __slots__ = ("nfe", "nfce", "entrada", "nfse", "mdfe", "inutilizacoes")
    NFE_FIELD_NUMBER: _ClassVar[int]
    NFCE_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_FIELD_NUMBER: _ClassVar[int]
    NFSE_FIELD_NUMBER: _ClassVar[int]
    MDFE_FIELD_NUMBER: _ClassVar[int]
    INUTILIZACOES_FIELD_NUMBER: _ClassVar[int]
    nfe: ResumoItem
    nfce: ResumoItem
    entrada: ResumoItem
    nfse: ResumoItem
    mdfe: ResumoItem
    inutilizacoes: int
    def __init__(self, nfe: _Optional[_Union[ResumoItem, _Mapping]] = ..., nfce: _Optional[_Union[ResumoItem, _Mapping]] = ..., entrada: _Optional[_Union[ResumoItem, _Mapping]] = ..., nfse: _Optional[_Union[ResumoItem, _Mapping]] = ..., mdfe: _Optional[_Union[ResumoItem, _Mapping]] = ..., inutilizacoes: _Optional[int] = ...) -> None: ...

class StatusMensalItem(_message.Message):
    __slots__ = ("mes", "nfe_autorizada", "nfe_pendente", "nfe_cancelada", "nfe_autorizada_valor", "nfe_pendente_valor", "nfe_cancelada_valor", "nfce_autorizada", "nfce_pendente", "nfce_cancelada", "nfce_autorizada_valor", "nfce_pendente_valor", "nfce_cancelada_valor")
    MES_FIELD_NUMBER: _ClassVar[int]
    NFE_AUTORIZADA_FIELD_NUMBER: _ClassVar[int]
    NFE_PENDENTE_FIELD_NUMBER: _ClassVar[int]
    NFE_CANCELADA_FIELD_NUMBER: _ClassVar[int]
    NFE_AUTORIZADA_VALOR_FIELD_NUMBER: _ClassVar[int]
    NFE_PENDENTE_VALOR_FIELD_NUMBER: _ClassVar[int]
    NFE_CANCELADA_VALOR_FIELD_NUMBER: _ClassVar[int]
    NFCE_AUTORIZADA_FIELD_NUMBER: _ClassVar[int]
    NFCE_PENDENTE_FIELD_NUMBER: _ClassVar[int]
    NFCE_CANCELADA_FIELD_NUMBER: _ClassVar[int]
    NFCE_AUTORIZADA_VALOR_FIELD_NUMBER: _ClassVar[int]
    NFCE_PENDENTE_VALOR_FIELD_NUMBER: _ClassVar[int]
    NFCE_CANCELADA_VALOR_FIELD_NUMBER: _ClassVar[int]
    mes: str
    nfe_autorizada: int
    nfe_pendente: int
    nfe_cancelada: int
    nfe_autorizada_valor: float
    nfe_pendente_valor: float
    nfe_cancelada_valor: float
    nfce_autorizada: int
    nfce_pendente: int
    nfce_cancelada: int
    nfce_autorizada_valor: float
    nfce_pendente_valor: float
    nfce_cancelada_valor: float
    def __init__(self, mes: _Optional[str] = ..., nfe_autorizada: _Optional[int] = ..., nfe_pendente: _Optional[int] = ..., nfe_cancelada: _Optional[int] = ..., nfe_autorizada_valor: _Optional[float] = ..., nfe_pendente_valor: _Optional[float] = ..., nfe_cancelada_valor: _Optional[float] = ..., nfce_autorizada: _Optional[int] = ..., nfce_pendente: _Optional[int] = ..., nfce_cancelada: _Optional[int] = ..., nfce_autorizada_valor: _Optional[float] = ..., nfce_pendente_valor: _Optional[float] = ..., nfce_cancelada_valor: _Optional[float] = ...) -> None: ...

class ImpostosItem(_message.Message):
    __slots__ = ("mes", "icms", "pis", "cofins")
    MES_FIELD_NUMBER: _ClassVar[int]
    ICMS_FIELD_NUMBER: _ClassVar[int]
    PIS_FIELD_NUMBER: _ClassVar[int]
    COFINS_FIELD_NUMBER: _ClassVar[int]
    mes: str
    icms: float
    pis: float
    cofins: float
    def __init__(self, mes: _Optional[str] = ..., icms: _Optional[float] = ..., pis: _Optional[float] = ..., cofins: _Optional[float] = ...) -> None: ...

class CfopBucket(_message.Message):
    __slots__ = ("qtd", "valor", "total")
    QTD_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    qtd: int
    valor: float
    total: float
    def __init__(self, qtd: _Optional[int] = ..., valor: _Optional[float] = ..., total: _Optional[float] = ...) -> None: ...

class CfopItem(_message.Message):
    __slots__ = ("cfop", "descricao", "nfe", "nfce", "entrada", "total_geral")
    CFOP_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    NFCE_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_FIELD_NUMBER: _ClassVar[int]
    TOTAL_GERAL_FIELD_NUMBER: _ClassVar[int]
    cfop: str
    descricao: str
    nfe: CfopBucket
    nfce: CfopBucket
    entrada: CfopBucket
    total_geral: float
    def __init__(self, cfop: _Optional[str] = ..., descricao: _Optional[str] = ..., nfe: _Optional[_Union[CfopBucket, _Mapping]] = ..., nfce: _Optional[_Union[CfopBucket, _Mapping]] = ..., entrada: _Optional[_Union[CfopBucket, _Mapping]] = ..., total_geral: _Optional[float] = ...) -> None: ...
