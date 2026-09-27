import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.message import message_pb2 as _message_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateRequest(_message.Message):
    __slots__ = ("deal",)
    DEAL_FIELD_NUMBER: _ClassVar[int]
    deal: _message_pb2.Message
    def __init__(self, deal: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("deal",)
    DEAL_FIELD_NUMBER: _ClassVar[int]
    deal: _message_pb2.Message
    def __init__(self, deal: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "deal", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    DEAL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    deal: _message_pb2.Message
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., deal: _Optional[_Union[_message_pb2.Message, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("deal",)
    DEAL_FIELD_NUMBER: _ClassVar[int]
    deal: _message_pb2.Message
    def __init__(self, deal: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

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
    __slots__ = ("deal",)
    DEAL_FIELD_NUMBER: _ClassVar[int]
    deal: _message_pb2.Message
    def __init__(self, deal: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class ListRequest(_message.Message):
    __slots__ = ("ids", "person_id", "pipeline_id", "stage_id", "outcome", "loss_reason_id", "close_forecast_gte", "close_forecast_lte", "filter", "campaign_id")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    LOSS_REASON_ID_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FORECAST_GTE_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FORECAST_LTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    person_id: str
    pipeline_id: str
    stage_id: str
    outcome: _message_pb2.DealOutcome
    loss_reason_id: str
    close_forecast_gte: _timestamp_pb2.Timestamp
    close_forecast_lte: _timestamp_pb2.Timestamp
    filter: _filter_pb2.Filter
    campaign_id: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., person_id: _Optional[str] = ..., pipeline_id: _Optional[str] = ..., stage_id: _Optional[str] = ..., outcome: _Optional[_Union[_message_pb2.DealOutcome, str]] = ..., loss_reason_id: _Optional[str] = ..., close_forecast_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., close_forecast_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., campaign_id: _Optional[str] = ...) -> None: ...

class ListResponse(_message.Message):
    __slots__ = ("deal_list",)
    DEAL_LIST_FIELD_NUMBER: _ClassVar[int]
    deal_list: _containers.RepeatedCompositeFieldContainer[_message_pb2.Message]
    def __init__(self, deal_list: _Optional[_Iterable[_Union[_message_pb2.Message, _Mapping]]] = ...) -> None: ...

class MoveStageRequest(_message.Message):
    __slots__ = ("id", "pipeline_id", "stage_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    pipeline_id: str
    stage_id: str
    def __init__(self, id: _Optional[str] = ..., pipeline_id: _Optional[str] = ..., stage_id: _Optional[str] = ...) -> None: ...

class MoveStageResponse(_message.Message):
    __slots__ = ("deal",)
    DEAL_FIELD_NUMBER: _ClassVar[int]
    deal: _message_pb2.Message
    def __init__(self, deal: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class CloseDealRequest(_message.Message):
    __slots__ = ("id", "outcome", "loss_reason_id", "close_notes", "close_date")
    ID_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    LOSS_REASON_ID_FIELD_NUMBER: _ClassVar[int]
    CLOSE_NOTES_FIELD_NUMBER: _ClassVar[int]
    CLOSE_DATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    outcome: _message_pb2.DealOutcome
    loss_reason_id: str
    close_notes: str
    close_date: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., outcome: _Optional[_Union[_message_pb2.DealOutcome, str]] = ..., loss_reason_id: _Optional[str] = ..., close_notes: _Optional[str] = ..., close_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CloseDealResponse(_message.Message):
    __slots__ = ("deal",)
    DEAL_FIELD_NUMBER: _ClassVar[int]
    deal: _message_pb2.Message
    def __init__(self, deal: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class ReopenDealRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ReopenDealResponse(_message.Message):
    __slots__ = ("deal",)
    DEAL_FIELD_NUMBER: _ClassVar[int]
    deal: _message_pb2.Message
    def __init__(self, deal: _Optional[_Union[_message_pb2.Message, _Mapping]] = ...) -> None: ...

class ConvertToOrderRequest(_message.Message):
    __slots__ = ("id", "tipo")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    id: str
    tipo: str
    def __init__(self, id: _Optional[str] = ..., tipo: _Optional[str] = ...) -> None: ...

class ConvertToOrderResponse(_message.Message):
    __slots__ = ("order_id", "order_number")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    order_number: int
    def __init__(self, order_id: _Optional[str] = ..., order_number: _Optional[int] = ...) -> None: ...

class AddInteractionRequest(_message.Message):
    __slots__ = ("deal_id", "content", "is_internal", "attachments")
    DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_INTERNAL_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENTS_FIELD_NUMBER: _ClassVar[int]
    deal_id: str
    content: str
    is_internal: bool
    attachments: _containers.RepeatedCompositeFieldContainer[_message_pb2.Attachment]
    def __init__(self, deal_id: _Optional[str] = ..., content: _Optional[str] = ..., is_internal: _Optional[bool] = ..., attachments: _Optional[_Iterable[_Union[_message_pb2.Attachment, _Mapping]]] = ...) -> None: ...

class AddInteractionResponse(_message.Message):
    __slots__ = ("interaction",)
    INTERACTION_FIELD_NUMBER: _ClassVar[int]
    interaction: _message_pb2.Interaction
    def __init__(self, interaction: _Optional[_Union[_message_pb2.Interaction, _Mapping]] = ...) -> None: ...

class ListInteractionsRequest(_message.Message):
    __slots__ = ("deal_id", "page_size", "page_token")
    DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    deal_id: str
    page_size: int
    page_token: str
    def __init__(self, deal_id: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListInteractionsResponse(_message.Message):
    __slots__ = ("interactions", "next_page_token")
    INTERACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    interactions: _containers.RepeatedCompositeFieldContainer[_message_pb2.Interaction]
    next_page_token: str
    def __init__(self, interactions: _Optional[_Iterable[_Union[_message_pb2.Interaction, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("list_request", "tipo_relatorio")
    LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TIPO_RELATORIO_FIELD_NUMBER: _ClassVar[int]
    list_request: ListRequest
    tipo_relatorio: str
    def __init__(self, list_request: _Optional[_Union[ListRequest, _Mapping]] = ..., tipo_relatorio: _Optional[str] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class AiSummarizeRequest(_message.Message):
    __slots__ = ("id", "additional_instructions", "ai_integration_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    AI_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    additional_instructions: str
    ai_integration_id: str
    def __init__(self, id: _Optional[str] = ..., additional_instructions: _Optional[str] = ..., ai_integration_id: _Optional[str] = ...) -> None: ...

class AiSummarizeResponse(_message.Message):
    __slots__ = ("summary", "temperature", "highlights", "risks")
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    HIGHLIGHTS_FIELD_NUMBER: _ClassVar[int]
    RISKS_FIELD_NUMBER: _ClassVar[int]
    summary: str
    temperature: str
    highlights: _containers.RepeatedScalarFieldContainer[str]
    risks: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, summary: _Optional[str] = ..., temperature: _Optional[str] = ..., highlights: _Optional[_Iterable[str]] = ..., risks: _Optional[_Iterable[str]] = ...) -> None: ...

class AiSuggestNextStepRequest(_message.Message):
    __slots__ = ("id", "additional_instructions", "ai_integration_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    AI_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    additional_instructions: str
    ai_integration_id: str
    def __init__(self, id: _Optional[str] = ..., additional_instructions: _Optional[str] = ..., ai_integration_id: _Optional[str] = ...) -> None: ...

class AiSuggestNextStepResponse(_message.Message):
    __slots__ = ("activity_type", "title", "due_in_days", "message_draft", "reasoning")
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DUE_IN_DAYS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_DRAFT_FIELD_NUMBER: _ClassVar[int]
    REASONING_FIELD_NUMBER: _ClassVar[int]
    activity_type: str
    title: str
    due_in_days: int
    message_draft: str
    reasoning: str
    def __init__(self, activity_type: _Optional[str] = ..., title: _Optional[str] = ..., due_in_days: _Optional[int] = ..., message_draft: _Optional[str] = ..., reasoning: _Optional[str] = ...) -> None: ...

class DashboardRequest(_message.Message):
    __slots__ = ("campaign_id",)
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    def __init__(self, campaign_id: _Optional[str] = ...) -> None: ...

class ResumoTotais(_message.Message):
    __slots__ = ("nome", "qtde", "total")
    NOME_FIELD_NUMBER: _ClassVar[int]
    QTDE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    nome: str
    qtde: int
    total: float
    def __init__(self, nome: _Optional[str] = ..., qtde: _Optional[int] = ..., total: _Optional[float] = ...) -> None: ...

class CampaignSummary(_message.Message):
    __slots__ = ("id", "name", "count", "amount", "won_count", "won_amount", "lost_count", "lost_amount", "open_count", "open_amount", "conversion_rate", "cost", "roi")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    WON_COUNT_FIELD_NUMBER: _ClassVar[int]
    WON_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LOST_COUNT_FIELD_NUMBER: _ClassVar[int]
    LOST_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    OPEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    OPEN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_RATE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    ROI_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    count: int
    amount: float
    won_count: int
    won_amount: float
    lost_count: int
    lost_amount: float
    open_count: int
    open_amount: float
    conversion_rate: float
    cost: float
    roi: float
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ..., amount: _Optional[float] = ..., won_count: _Optional[int] = ..., won_amount: _Optional[float] = ..., lost_count: _Optional[int] = ..., lost_amount: _Optional[float] = ..., open_count: _Optional[int] = ..., open_amount: _Optional[float] = ..., conversion_rate: _Optional[float] = ..., cost: _Optional[float] = ..., roi: _Optional[float] = ...) -> None: ...

class ResumoMesAno(_message.Message):
    __slots__ = ("ano_mes", "aberto", "ganho", "perdido", "responsaveis", "clientes", "pipelines", "etapas", "motivos_perda", "campaigns")
    ANO_MES_FIELD_NUMBER: _ClassVar[int]
    ABERTO_FIELD_NUMBER: _ClassVar[int]
    GANHO_FIELD_NUMBER: _ClassVar[int]
    PERDIDO_FIELD_NUMBER: _ClassVar[int]
    RESPONSAVEIS_FIELD_NUMBER: _ClassVar[int]
    CLIENTES_FIELD_NUMBER: _ClassVar[int]
    PIPELINES_FIELD_NUMBER: _ClassVar[int]
    ETAPAS_FIELD_NUMBER: _ClassVar[int]
    MOTIVOS_PERDA_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGNS_FIELD_NUMBER: _ClassVar[int]
    ano_mes: str
    aberto: ResumoTotais
    ganho: ResumoTotais
    perdido: ResumoTotais
    responsaveis: _containers.RepeatedCompositeFieldContainer[ResumoTotais]
    clientes: _containers.RepeatedCompositeFieldContainer[ResumoTotais]
    pipelines: _containers.RepeatedCompositeFieldContainer[ResumoTotais]
    etapas: _containers.RepeatedCompositeFieldContainer[ResumoTotais]
    motivos_perda: _containers.RepeatedCompositeFieldContainer[ResumoTotais]
    campaigns: _containers.RepeatedCompositeFieldContainer[CampaignSummary]
    def __init__(self, ano_mes: _Optional[str] = ..., aberto: _Optional[_Union[ResumoTotais, _Mapping]] = ..., ganho: _Optional[_Union[ResumoTotais, _Mapping]] = ..., perdido: _Optional[_Union[ResumoTotais, _Mapping]] = ..., responsaveis: _Optional[_Iterable[_Union[ResumoTotais, _Mapping]]] = ..., clientes: _Optional[_Iterable[_Union[ResumoTotais, _Mapping]]] = ..., pipelines: _Optional[_Iterable[_Union[ResumoTotais, _Mapping]]] = ..., etapas: _Optional[_Iterable[_Union[ResumoTotais, _Mapping]]] = ..., motivos_perda: _Optional[_Iterable[_Union[ResumoTotais, _Mapping]]] = ..., campaigns: _Optional[_Iterable[_Union[CampaignSummary, _Mapping]]] = ...) -> None: ...

class DashboardResponse(_message.Message):
    __slots__ = ("meses",)
    MESES_FIELD_NUMBER: _ClassVar[int]
    meses: _containers.RepeatedCompositeFieldContainer[ResumoMesAno]
    def __init__(self, meses: _Optional[_Iterable[_Union[ResumoMesAno, _Mapping]]] = ...) -> None: ...

class ForecastRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ForecastItem(_message.Message):
    __slots__ = ("ano_mes", "total", "ponderado", "qtde")
    ANO_MES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PONDERADO_FIELD_NUMBER: _ClassVar[int]
    QTDE_FIELD_NUMBER: _ClassVar[int]
    ano_mes: str
    total: float
    ponderado: float
    qtde: int
    def __init__(self, ano_mes: _Optional[str] = ..., total: _Optional[float] = ..., ponderado: _Optional[float] = ..., qtde: _Optional[int] = ...) -> None: ...

class ForecastDeal(_message.Message):
    __slots__ = ("id", "nome", "cliente", "valor", "ponderado", "probabilidade", "etapa", "previsao")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CLIENTE_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    PONDERADO_FIELD_NUMBER: _ClassVar[int]
    PROBABILIDADE_FIELD_NUMBER: _ClassVar[int]
    ETAPA_FIELD_NUMBER: _ClassVar[int]
    PREVISAO_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    cliente: str
    valor: float
    ponderado: float
    probabilidade: float
    etapa: str
    previsao: str
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., cliente: _Optional[str] = ..., valor: _Optional[float] = ..., ponderado: _Optional[float] = ..., probabilidade: _Optional[float] = ..., etapa: _Optional[str] = ..., previsao: _Optional[str] = ...) -> None: ...

class ForecastResponse(_message.Message):
    __slots__ = ("total_ponderado", "total_bruto", "qtde_deals", "por_mes", "top_deals")
    TOTAL_PONDERADO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BRUTO_FIELD_NUMBER: _ClassVar[int]
    QTDE_DEALS_FIELD_NUMBER: _ClassVar[int]
    POR_MES_FIELD_NUMBER: _ClassVar[int]
    TOP_DEALS_FIELD_NUMBER: _ClassVar[int]
    total_ponderado: float
    total_bruto: float
    qtde_deals: int
    por_mes: _containers.RepeatedCompositeFieldContainer[ForecastItem]
    top_deals: _containers.RepeatedCompositeFieldContainer[ForecastDeal]
    def __init__(self, total_ponderado: _Optional[float] = ..., total_bruto: _Optional[float] = ..., qtde_deals: _Optional[int] = ..., por_mes: _Optional[_Iterable[_Union[ForecastItem, _Mapping]]] = ..., top_deals: _Optional[_Iterable[_Union[ForecastDeal, _Mapping]]] = ...) -> None: ...

class AlertsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AlertItem(_message.Message):
    __slots__ = ("deal_id", "deal_name", "cliente", "tipo", "mensagem", "valor")
    DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    DEAL_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENTE_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    deal_id: str
    deal_name: str
    cliente: str
    tipo: str
    mensagem: str
    valor: float
    def __init__(self, deal_id: _Optional[str] = ..., deal_name: _Optional[str] = ..., cliente: _Optional[str] = ..., tipo: _Optional[str] = ..., mensagem: _Optional[str] = ..., valor: _Optional[float] = ...) -> None: ...

class AlertsResponse(_message.Message):
    __slots__ = ("alertas", "total_alertas")
    ALERTAS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ALERTAS_FIELD_NUMBER: _ClassVar[int]
    alertas: _containers.RepeatedCompositeFieldContainer[AlertItem]
    total_alertas: int
    def __init__(self, alertas: _Optional[_Iterable[_Union[AlertItem, _Mapping]]] = ..., total_alertas: _Optional[int] = ...) -> None: ...

class PipelineHealthRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AgingBucket(_message.Message):
    __slots__ = ("faixa", "qtde", "total", "min_dias", "max_dias")
    FAIXA_FIELD_NUMBER: _ClassVar[int]
    QTDE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    MIN_DIAS_FIELD_NUMBER: _ClassVar[int]
    MAX_DIAS_FIELD_NUMBER: _ClassVar[int]
    faixa: str
    qtde: int
    total: float
    min_dias: int
    max_dias: int
    def __init__(self, faixa: _Optional[str] = ..., qtde: _Optional[int] = ..., total: _Optional[float] = ..., min_dias: _Optional[int] = ..., max_dias: _Optional[int] = ...) -> None: ...

class StageTime(_message.Message):
    __slots__ = ("stage_id", "nome", "qtde", "dias_medios", "total", "probability", "weighted_amount", "order", "pipeline_id", "pipeline_name")
    STAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    QTDE_FIELD_NUMBER: _ClassVar[int]
    DIAS_MEDIOS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PROBABILITY_FIELD_NUMBER: _ClassVar[int]
    WEIGHTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ID_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_NAME_FIELD_NUMBER: _ClassVar[int]
    stage_id: str
    nome: str
    qtde: int
    dias_medios: float
    total: float
    probability: float
    weighted_amount: float
    order: int
    pipeline_id: str
    pipeline_name: str
    def __init__(self, stage_id: _Optional[str] = ..., nome: _Optional[str] = ..., qtde: _Optional[int] = ..., dias_medios: _Optional[float] = ..., total: _Optional[float] = ..., probability: _Optional[float] = ..., weighted_amount: _Optional[float] = ..., order: _Optional[int] = ..., pipeline_id: _Optional[str] = ..., pipeline_name: _Optional[str] = ...) -> None: ...

class PipelineHealthResponse(_message.Message):
    __slots__ = ("aging_buckets", "tempo_por_etapa", "cycle_time_dias", "ticket_medio", "qtde_ganhos_90d", "qtde_abertos", "valor_abertos", "weighted_amount_total")
    AGING_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    TEMPO_POR_ETAPA_FIELD_NUMBER: _ClassVar[int]
    CYCLE_TIME_DIAS_FIELD_NUMBER: _ClassVar[int]
    TICKET_MEDIO_FIELD_NUMBER: _ClassVar[int]
    QTDE_GANHOS_90D_FIELD_NUMBER: _ClassVar[int]
    QTDE_ABERTOS_FIELD_NUMBER: _ClassVar[int]
    VALOR_ABERTOS_FIELD_NUMBER: _ClassVar[int]
    WEIGHTED_AMOUNT_TOTAL_FIELD_NUMBER: _ClassVar[int]
    aging_buckets: _containers.RepeatedCompositeFieldContainer[AgingBucket]
    tempo_por_etapa: _containers.RepeatedCompositeFieldContainer[StageTime]
    cycle_time_dias: float
    ticket_medio: float
    qtde_ganhos_90d: int
    qtde_abertos: int
    valor_abertos: float
    weighted_amount_total: float
    def __init__(self, aging_buckets: _Optional[_Iterable[_Union[AgingBucket, _Mapping]]] = ..., tempo_por_etapa: _Optional[_Iterable[_Union[StageTime, _Mapping]]] = ..., cycle_time_dias: _Optional[float] = ..., ticket_medio: _Optional[float] = ..., qtde_ganhos_90d: _Optional[int] = ..., qtde_abertos: _Optional[int] = ..., valor_abertos: _Optional[float] = ..., weighted_amount_total: _Optional[float] = ...) -> None: ...
