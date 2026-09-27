import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from linksoft_sdk.pb.apps.vendas.rentcar.model import rentcar_model_pb2 as _rentcar_model_pb2
from linksoft_sdk.pb.apps.vendas.pedido import pedido_otica_pb2 as _pedido_otica_pb2
from linksoft_sdk.pb.apps.vendas.pedido import pedido_mesa_pb2 as _pedido_mesa_pb2
from linksoft_sdk.pb.apps.filemanager import filemanager_pb2 as _filemanager_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.imports import imports_pb2 as _imports_pb2
from linksoft_sdk.pb.exports import exports_pb2 as _exports_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RespostaCliente(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESPOSTA_CLIENTE_UNSPECIFIED: _ClassVar[RespostaCliente]
    RESPOSTA_CLIENTE_APROVADO: _ClassVar[RespostaCliente]
    RESPOSTA_CLIENTE_AJUSTE: _ClassVar[RespostaCliente]
    RESPOSTA_CLIENTE_CONVERSA: _ClassVar[RespostaCliente]
    RESPOSTA_CLIENTE_RECUSADO: _ClassVar[RespostaCliente]
    RESPOSTA_CLIENTE_MAIS_PRAZO: _ClassVar[RespostaCliente]

class ReportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPORT_TYPE_UNSPECIFIED: _ClassVar[ReportType]
    REPORT_TYPE_ORDER_SUMMARY: _ClassVar[ReportType]
    REPORT_TYPE_ORDER_SMALL_SUMMARY: _ClassVar[ReportType]
    REPORT_TYPE_PAYMENT_BY_ACQUIRER_SUMMARY: _ClassVar[ReportType]
    REPORT_TYPE_PAYMENT_BY_ACQUIRER_DETAIL: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_PAYMENT_METHOD_SUMMARY: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_PAYMENT_METHOD_DETAIL: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_DATE: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_PERSON: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_PRODUCT: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_SERVICE: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_CATEGORY: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_MANUFACTURER: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_SELLER_COMMISSION: _ClassVar[ReportType]
    REPORT_TYPE_SALES_SUMMARY: _ClassVar[ReportType]
    REPORT_TYPE_SALES_DETAIL: _ClassVar[ReportType]
    REPORT_TYPE_SALES_BY_PRODUCT: _ClassVar[ReportType]
    REPORT_TYPE_SALES_BY_SERVICE: _ClassVar[ReportType]
    REPORT_TYPE_SALES_BY_CATEGORY: _ClassVar[ReportType]
    REPORT_TYPE_SALES_FOR_DELIVERY: _ClassVar[ReportType]
    REPORT_TYPE_COMMISSION_BY_SELLER: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_SELLER: _ClassVar[ReportType]
    REPORT_TYPE_GROUP_BY_TECHNICAL_SERVICE: _ClassVar[ReportType]
    REPORT_TYPE_YEAR_MONTH: _ClassVar[ReportType]
    REPORT_TYPE_PROD_SERV_MOST_SOLD: _ClassVar[ReportType]
    REPORT_TYPE_PROD_MOST_PROFITABLE: _ClassVar[ReportType]
    REPORT_TYPE_SALES_BY_SELLER_UNIT_PRICE_DIFFERENCE: _ClassVar[ReportType]
    REPORT_TYPE_DASHBOARD_SALES_SUMMARY: _ClassVar[ReportType]
    REPORT_TYPE_DASHBOARD_SALES_TOP5: _ClassVar[ReportType]
    REPORT_TYPE_DASHBOARD_SALES_BY_REGION: _ClassVar[ReportType]
    REPORT_TYPE_DASHBOARD_SALES_KPI: _ClassVar[ReportType]
    REPORT_TYPE_ABC_CURVE_BY_PERSON: _ClassVar[ReportType]

class TipoMovimentacao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_UNSPECIFIED: _ClassVar[TipoMovimentacao]
    TIPO_ALL: _ClassVar[TipoMovimentacao]
    TIPO_PEDIDO: _ClassVar[TipoMovimentacao]
    TIPO_ORCAMENTO: _ClassVar[TipoMovimentacao]
    TIPO_OS: _ClassVar[TipoMovimentacao]
    TIPO_AUTHORIZATION: _ClassVar[TipoMovimentacao]
    TIPO_CART: _ClassVar[TipoMovimentacao]
    TIPO_CONTRACTSALES: _ClassVar[TipoMovimentacao]
    TIPO_CONTRACT: _ClassVar[TipoMovimentacao]
    TIPO_RENT_CAR: _ClassVar[TipoMovimentacao]

class RecurrenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RECURRENCE_TYPE_UNSPECIFIED: _ClassVar[RecurrenceType]
    DAILY: _ClassVar[RecurrenceType]
    WEEKLY: _ClassVar[RecurrenceType]
    MONTHLY: _ClassVar[RecurrenceType]
    YEARLY: _ClassVar[RecurrenceType]

class Origin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORIGIN_MARKETPLACE: _ClassVar[Origin]
    ORIGIN_ONLINE_STORE: _ClassVar[Origin]
    ORIGIN_EXTERNAL_SALESMAN: _ClassVar[Origin]
    ORIGIN_GENERAL: _ClassVar[Origin]

class TipoGarantia(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_GARANTIA_UNSPECIFIED: _ClassVar[TipoGarantia]
    TIPO_GARANTIA_EMPRESA: _ClassVar[TipoGarantia]
    TIPO_GARANTIA_FORNECEDOR: _ClassVar[TipoGarantia]

class CheckoutPaymentChargeMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHECKOUT_PAYMENT_CHARGE_MODE_UNSPECIFIED: _ClassVar[CheckoutPaymentChargeMode]
    CHECKOUT_PAYMENT_CHARGE_MODE_ONLINE: _ClassVar[CheckoutPaymentChargeMode]
    CHECKOUT_PAYMENT_CHARGE_MODE_OFFLINE: _ClassVar[CheckoutPaymentChargeMode]

class CheckoutPaymentContext(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHECKOUT_PAYMENT_CONTEXT_UNSPECIFIED: _ClassVar[CheckoutPaymentContext]
    CHECKOUT_PAYMENT_CONTEXT_ANY: _ClassVar[CheckoutPaymentContext]
    CHECKOUT_PAYMENT_CONTEXT_PICKUP: _ClassVar[CheckoutPaymentContext]
    CHECKOUT_PAYMENT_CONTEXT_DELIVERY: _ClassVar[CheckoutPaymentContext]

class ContractType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTRACT_TYPE_UNSPECIFIED: _ClassVar[ContractType]
    CONTRACT_TYPE_PRE_PAID: _ClassVar[ContractType]
    CONTRACT_TYPE_POST_PAID: _ClassVar[ContractType]

class ContractStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTRACT_STATUS_UNSPECIFIED: _ClassVar[ContractStatus]
    CONTRACT_STATUS_ACTIVE: _ClassVar[ContractStatus]
    CONTRACT_STATUS_INACTIVE: _ClassVar[ContractStatus]
    CONTRACT_STATUS_CANCELED: _ClassVar[ContractStatus]
    CONTRACT_STATUS_BLOCKED: _ClassVar[ContractStatus]
    CONTRACT_STATUS_TRIAL: _ClassVar[ContractStatus]
    CONTRACT_STATUS_SUSPENDED: _ClassVar[ContractStatus]
    CONTRACT_STATUS_TRIAL_EXPIRED: _ClassVar[ContractStatus]

class ServicoCategoria(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SERVICO_CATEGORIA_UNSPECIFIED: _ClassVar[ServicoCategoria]
    SERVICO_CATEGORIA_DESLOCAMENTO: _ClassVar[ServicoCategoria]
    SERVICO_CATEGORIA_TERCEIROS: _ClassVar[ServicoCategoria]
    SERVICO_CATEGORIA_OUTROS: _ClassVar[ServicoCategoria]

class DanfeFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DANFE_FORMAT_UNSPECIFIED: _ClassVar[DanfeFormat]
    DANFE_FORMAT_PDF: _ClassVar[DanfeFormat]
    DANFE_FORMAT_REPORT: _ClassVar[DanfeFormat]
    DANFE_FORMAT_HTML: _ClassVar[DanfeFormat]

class DeliveryMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DELIVERY_METHOD_UNSPECIFIED: _ClassVar[DeliveryMethod]
    DELIVERY_METHOD_STANDARD: _ClassVar[DeliveryMethod]
    DELIVERY_METHOD_EXPRESS: _ClassVar[DeliveryMethod]
    DELIVERY_METHOD_PICKUP: _ClassVar[DeliveryMethod]
    DELIVERY_METHOD_CORREIOS_PAC: _ClassVar[DeliveryMethod]
    DELIVERY_METHOD_CORREIOS_SEDEX: _ClassVar[DeliveryMethod]
    DELIVERY_METHOD_CORREIOS_SEDEX10: _ClassVar[DeliveryMethod]
    DELIVERY_METHOD_CUSTOM: _ClassVar[DeliveryMethod]

class BaseApuracao(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BASE_APURACAO_DOCUMENTO: _ClassVar[BaseApuracao]
    BASE_APURACAO_PAGAMENTO: _ClassVar[BaseApuracao]
RESPOSTA_CLIENTE_UNSPECIFIED: RespostaCliente
RESPOSTA_CLIENTE_APROVADO: RespostaCliente
RESPOSTA_CLIENTE_AJUSTE: RespostaCliente
RESPOSTA_CLIENTE_CONVERSA: RespostaCliente
RESPOSTA_CLIENTE_RECUSADO: RespostaCliente
RESPOSTA_CLIENTE_MAIS_PRAZO: RespostaCliente
REPORT_TYPE_UNSPECIFIED: ReportType
REPORT_TYPE_ORDER_SUMMARY: ReportType
REPORT_TYPE_ORDER_SMALL_SUMMARY: ReportType
REPORT_TYPE_PAYMENT_BY_ACQUIRER_SUMMARY: ReportType
REPORT_TYPE_PAYMENT_BY_ACQUIRER_DETAIL: ReportType
REPORT_TYPE_GROUP_BY_PAYMENT_METHOD_SUMMARY: ReportType
REPORT_TYPE_GROUP_BY_PAYMENT_METHOD_DETAIL: ReportType
REPORT_TYPE_GROUP_BY_DATE: ReportType
REPORT_TYPE_GROUP_BY_PERSON: ReportType
REPORT_TYPE_GROUP_BY_PRODUCT: ReportType
REPORT_TYPE_GROUP_BY_SERVICE: ReportType
REPORT_TYPE_GROUP_BY_CATEGORY: ReportType
REPORT_TYPE_GROUP_BY_MANUFACTURER: ReportType
REPORT_TYPE_GROUP_BY_SELLER_COMMISSION: ReportType
REPORT_TYPE_SALES_SUMMARY: ReportType
REPORT_TYPE_SALES_DETAIL: ReportType
REPORT_TYPE_SALES_BY_PRODUCT: ReportType
REPORT_TYPE_SALES_BY_SERVICE: ReportType
REPORT_TYPE_SALES_BY_CATEGORY: ReportType
REPORT_TYPE_SALES_FOR_DELIVERY: ReportType
REPORT_TYPE_COMMISSION_BY_SELLER: ReportType
REPORT_TYPE_GROUP_BY_SELLER: ReportType
REPORT_TYPE_GROUP_BY_TECHNICAL_SERVICE: ReportType
REPORT_TYPE_YEAR_MONTH: ReportType
REPORT_TYPE_PROD_SERV_MOST_SOLD: ReportType
REPORT_TYPE_PROD_MOST_PROFITABLE: ReportType
REPORT_TYPE_SALES_BY_SELLER_UNIT_PRICE_DIFFERENCE: ReportType
REPORT_TYPE_DASHBOARD_SALES_SUMMARY: ReportType
REPORT_TYPE_DASHBOARD_SALES_TOP5: ReportType
REPORT_TYPE_DASHBOARD_SALES_BY_REGION: ReportType
REPORT_TYPE_DASHBOARD_SALES_KPI: ReportType
REPORT_TYPE_ABC_CURVE_BY_PERSON: ReportType
TIPO_UNSPECIFIED: TipoMovimentacao
TIPO_ALL: TipoMovimentacao
TIPO_PEDIDO: TipoMovimentacao
TIPO_ORCAMENTO: TipoMovimentacao
TIPO_OS: TipoMovimentacao
TIPO_AUTHORIZATION: TipoMovimentacao
TIPO_CART: TipoMovimentacao
TIPO_CONTRACTSALES: TipoMovimentacao
TIPO_CONTRACT: TipoMovimentacao
TIPO_RENT_CAR: TipoMovimentacao
RECURRENCE_TYPE_UNSPECIFIED: RecurrenceType
DAILY: RecurrenceType
WEEKLY: RecurrenceType
MONTHLY: RecurrenceType
YEARLY: RecurrenceType
ORIGIN_MARKETPLACE: Origin
ORIGIN_ONLINE_STORE: Origin
ORIGIN_EXTERNAL_SALESMAN: Origin
ORIGIN_GENERAL: Origin
TIPO_GARANTIA_UNSPECIFIED: TipoGarantia
TIPO_GARANTIA_EMPRESA: TipoGarantia
TIPO_GARANTIA_FORNECEDOR: TipoGarantia
CHECKOUT_PAYMENT_CHARGE_MODE_UNSPECIFIED: CheckoutPaymentChargeMode
CHECKOUT_PAYMENT_CHARGE_MODE_ONLINE: CheckoutPaymentChargeMode
CHECKOUT_PAYMENT_CHARGE_MODE_OFFLINE: CheckoutPaymentChargeMode
CHECKOUT_PAYMENT_CONTEXT_UNSPECIFIED: CheckoutPaymentContext
CHECKOUT_PAYMENT_CONTEXT_ANY: CheckoutPaymentContext
CHECKOUT_PAYMENT_CONTEXT_PICKUP: CheckoutPaymentContext
CHECKOUT_PAYMENT_CONTEXT_DELIVERY: CheckoutPaymentContext
CONTRACT_TYPE_UNSPECIFIED: ContractType
CONTRACT_TYPE_PRE_PAID: ContractType
CONTRACT_TYPE_POST_PAID: ContractType
CONTRACT_STATUS_UNSPECIFIED: ContractStatus
CONTRACT_STATUS_ACTIVE: ContractStatus
CONTRACT_STATUS_INACTIVE: ContractStatus
CONTRACT_STATUS_CANCELED: ContractStatus
CONTRACT_STATUS_BLOCKED: ContractStatus
CONTRACT_STATUS_TRIAL: ContractStatus
CONTRACT_STATUS_SUSPENDED: ContractStatus
CONTRACT_STATUS_TRIAL_EXPIRED: ContractStatus
SERVICO_CATEGORIA_UNSPECIFIED: ServicoCategoria
SERVICO_CATEGORIA_DESLOCAMENTO: ServicoCategoria
SERVICO_CATEGORIA_TERCEIROS: ServicoCategoria
SERVICO_CATEGORIA_OUTROS: ServicoCategoria
DANFE_FORMAT_UNSPECIFIED: DanfeFormat
DANFE_FORMAT_PDF: DanfeFormat
DANFE_FORMAT_REPORT: DanfeFormat
DANFE_FORMAT_HTML: DanfeFormat
DELIVERY_METHOD_UNSPECIFIED: DeliveryMethod
DELIVERY_METHOD_STANDARD: DeliveryMethod
DELIVERY_METHOD_EXPRESS: DeliveryMethod
DELIVERY_METHOD_PICKUP: DeliveryMethod
DELIVERY_METHOD_CORREIOS_PAC: DeliveryMethod
DELIVERY_METHOD_CORREIOS_SEDEX: DeliveryMethod
DELIVERY_METHOD_CORREIOS_SEDEX10: DeliveryMethod
DELIVERY_METHOD_CUSTOM: DeliveryMethod
BASE_APURACAO_DOCUMENTO: BaseApuracao
BASE_APURACAO_PAGAMENTO: BaseApuracao

class GetQuickProdutosRequest(_message.Message):
    __slots__ = ("dias", "limit")
    DIAS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    dias: int
    limit: int
    def __init__(self, dias: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class QuickProduto(_message.Message):
    __slots__ = ("produtoId", "nome", "codigo", "un", "valorUnitario", "categoriaId", "categoriaNome", "imagemUrl")
    PRODUTOID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    VALORUNITARIO_FIELD_NUMBER: _ClassVar[int]
    CATEGORIAID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIANOME_FIELD_NUMBER: _ClassVar[int]
    IMAGEMURL_FIELD_NUMBER: _ClassVar[int]
    produtoId: str
    nome: str
    codigo: str
    un: str
    valorUnitario: float
    categoriaId: str
    categoriaNome: str
    imagemUrl: str
    def __init__(self, produtoId: _Optional[str] = ..., nome: _Optional[str] = ..., codigo: _Optional[str] = ..., un: _Optional[str] = ..., valorUnitario: _Optional[float] = ..., categoriaId: _Optional[str] = ..., categoriaNome: _Optional[str] = ..., imagemUrl: _Optional[str] = ...) -> None: ...

class GetQuickProdutosResponse(_message.Message):
    __slots__ = ("maisVendidos", "recentes")
    MAISVENDIDOS_FIELD_NUMBER: _ClassVar[int]
    RECENTES_FIELD_NUMBER: _ClassVar[int]
    maisVendidos: _containers.RepeatedCompositeFieldContainer[QuickProduto]
    recentes: _containers.RepeatedCompositeFieldContainer[QuickProduto]
    def __init__(self, maisVendidos: _Optional[_Iterable[_Union[QuickProduto, _Mapping]]] = ..., recentes: _Optional[_Iterable[_Union[QuickProduto, _Mapping]]] = ...) -> None: ...

class EnviarProducaoRequest(_message.Message):
    __slots__ = ("pedidoId", "reimprimir", "itemIds")
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    REIMPRIMIR_FIELD_NUMBER: _ClassVar[int]
    ITEMIDS_FIELD_NUMBER: _ClassVar[int]
    pedidoId: str
    reimprimir: bool
    itemIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, pedidoId: _Optional[str] = ..., reimprimir: _Optional[bool] = ..., itemIds: _Optional[_Iterable[str]] = ...) -> None: ...

class ImpressoraProducao(_message.Message):
    __slots__ = ("id", "nome", "tipoConexao", "host", "porta", "modelo", "grupo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    TIPOCONEXAO_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PORTA_FIELD_NUMBER: _ClassVar[int]
    MODELO_FIELD_NUMBER: _ClassVar[int]
    GRUPO_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    tipoConexao: str
    host: str
    porta: int
    modelo: int
    grupo: str
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., tipoConexao: _Optional[str] = ..., host: _Optional[str] = ..., porta: _Optional[int] = ..., modelo: _Optional[int] = ..., grupo: _Optional[str] = ...) -> None: ...

class ProducaoItem(_message.Message):
    __slots__ = ("itemId", "nome", "quantidade", "un", "obs")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    itemId: str
    nome: str
    quantidade: float
    un: str
    obs: str
    def __init__(self, itemId: _Optional[str] = ..., nome: _Optional[str] = ..., quantidade: _Optional[float] = ..., un: _Optional[str] = ..., obs: _Optional[str] = ...) -> None: ...

class ProducaoJob(_message.Message):
    __slots__ = ("impressora", "mesaCartao", "setor", "dataHora", "itens")
    IMPRESSORA_FIELD_NUMBER: _ClassVar[int]
    MESACARTAO_FIELD_NUMBER: _ClassVar[int]
    SETOR_FIELD_NUMBER: _ClassVar[int]
    DATAHORA_FIELD_NUMBER: _ClassVar[int]
    ITENS_FIELD_NUMBER: _ClassVar[int]
    impressora: ImpressoraProducao
    mesaCartao: str
    setor: str
    dataHora: str
    itens: _containers.RepeatedCompositeFieldContainer[ProducaoItem]
    def __init__(self, impressora: _Optional[_Union[ImpressoraProducao, _Mapping]] = ..., mesaCartao: _Optional[str] = ..., setor: _Optional[str] = ..., dataHora: _Optional[str] = ..., itens: _Optional[_Iterable[_Union[ProducaoItem, _Mapping]]] = ...) -> None: ...

class EnviarProducaoResponse(_message.Message):
    __slots__ = ("jobs",)
    JOBS_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[ProducaoJob]
    def __init__(self, jobs: _Optional[_Iterable[_Union[ProducaoJob, _Mapping]]] = ...) -> None: ...

class ConfirmacaoImpressaoItem(_message.Message):
    __slots__ = ("itemId", "impresso", "erro")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    IMPRESSO_FIELD_NUMBER: _ClassVar[int]
    ERRO_FIELD_NUMBER: _ClassVar[int]
    itemId: str
    impresso: bool
    erro: str
    def __init__(self, itemId: _Optional[str] = ..., impresso: _Optional[bool] = ..., erro: _Optional[str] = ...) -> None: ...

class ConfirmarImpressaoProducaoRequest(_message.Message):
    __slots__ = ("pedidoId", "itens")
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    ITENS_FIELD_NUMBER: _ClassVar[int]
    pedidoId: str
    itens: _containers.RepeatedCompositeFieldContainer[ConfirmacaoImpressaoItem]
    def __init__(self, pedidoId: _Optional[str] = ..., itens: _Optional[_Iterable[_Union[ConfirmacaoImpressaoItem, _Mapping]]] = ...) -> None: ...

class ConfirmarImpressaoProducaoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MarcarItemEntregueRequest(_message.Message):
    __slots__ = ("pedidoId", "itemIds", "entregue")
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    ITEMIDS_FIELD_NUMBER: _ClassVar[int]
    ENTREGUE_FIELD_NUMBER: _ClassVar[int]
    pedidoId: str
    itemIds: _containers.RepeatedScalarFieldContainer[str]
    entregue: bool
    def __init__(self, pedidoId: _Optional[str] = ..., itemIds: _Optional[_Iterable[str]] = ..., entregue: _Optional[bool] = ...) -> None: ...

class MarcarItemEntregueResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CreatePedidoRequest(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class CreatePedidoResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class UpdatePedidoRequest(_message.Message):
    __slots__ = ("id", "pedido", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    pedido: Pedido
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., pedido: _Optional[_Union[Pedido, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdatePedidoResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class DeletePedidoRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeletePedidoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListPedidoRequest(_message.Message):
    __slots__ = ("ids", "nome", "pedido", "merged", "seller_only", "seller_id", "generated_nfe", "generated_nfce", "nfe_id", "nfce_id", "nfse_id", "person_id", "contract_number", "types", "status", "products_id", "payment_method_id", "due_date_gte", "due_date_lte", "created_at_gte", "created_at_lte", "closeDateGte", "closeDateLte", "deliveryDateGte", "deliveryDateLte", "recurrenceDateGte", "recurrenceDateLte", "dataHoraRegistroGte", "dataHoraRegistroLte", "totalGte", "totalLte", "payment_id", "filter", "currency", "categoryId", "recurrence_type", "recurrence_increment", "contract_type", "source", "source_id")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    MERGED_FIELD_NUMBER: _ClassVar[int]
    SELLER_ONLY_FIELD_NUMBER: _ClassVar[int]
    SELLER_ID_FIELD_NUMBER: _ClassVar[int]
    GENERATED_NFE_FIELD_NUMBER: _ClassVar[int]
    GENERATED_NFCE_FIELD_NUMBER: _ClassVar[int]
    NFE_ID_FIELD_NUMBER: _ClassVar[int]
    NFCE_ID_FIELD_NUMBER: _ClassVar[int]
    NFSE_ID_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRODUCTS_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_GTE_FIELD_NUMBER: _ClassVar[int]
    DUE_DATE_LTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    CLOSEDATEGTE_FIELD_NUMBER: _ClassVar[int]
    CLOSEDATELTE_FIELD_NUMBER: _ClassVar[int]
    DELIVERYDATEGTE_FIELD_NUMBER: _ClassVar[int]
    DELIVERYDATELTE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCEDATEGTE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCEDATELTE_FIELD_NUMBER: _ClassVar[int]
    DATAHORAREGISTROGTE_FIELD_NUMBER: _ClassVar[int]
    DATAHORAREGISTROLTE_FIELD_NUMBER: _ClassVar[int]
    TOTALGTE_FIELD_NUMBER: _ClassVar[int]
    TOTALLTE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CATEGORYID_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    nome: str
    pedido: Pedido
    merged: _metadata_pb2.Boolean
    seller_only: _metadata_pb2.Boolean
    seller_id: str
    generated_nfe: _metadata_pb2.Boolean
    generated_nfce: _metadata_pb2.Boolean
    nfe_id: str
    nfce_id: str
    nfse_id: str
    person_id: str
    contract_number: str
    types: _containers.RepeatedScalarFieldContainer[str]
    status: _containers.RepeatedScalarFieldContainer[str]
    products_id: _containers.RepeatedScalarFieldContainer[str]
    payment_method_id: _containers.RepeatedScalarFieldContainer[str]
    due_date_gte: _timestamp_pb2.Timestamp
    due_date_lte: _timestamp_pb2.Timestamp
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    closeDateGte: _timestamp_pb2.Timestamp
    closeDateLte: _timestamp_pb2.Timestamp
    deliveryDateGte: _timestamp_pb2.Timestamp
    deliveryDateLte: _timestamp_pb2.Timestamp
    recurrenceDateGte: _timestamp_pb2.Timestamp
    recurrenceDateLte: _timestamp_pb2.Timestamp
    dataHoraRegistroGte: _timestamp_pb2.Timestamp
    dataHoraRegistroLte: _timestamp_pb2.Timestamp
    totalGte: float
    totalLte: float
    payment_id: str
    filter: _filter_pb2.Filter
    currency: _containers.RepeatedScalarFieldContainer[str]
    categoryId: str
    recurrence_type: str
    recurrence_increment: int
    contract_type: str
    source: str
    source_id: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., nome: _Optional[str] = ..., pedido: _Optional[_Union[Pedido, _Mapping]] = ..., merged: _Optional[_Union[_metadata_pb2.Boolean, str]] = ..., seller_only: _Optional[_Union[_metadata_pb2.Boolean, str]] = ..., seller_id: _Optional[str] = ..., generated_nfe: _Optional[_Union[_metadata_pb2.Boolean, str]] = ..., generated_nfce: _Optional[_Union[_metadata_pb2.Boolean, str]] = ..., nfe_id: _Optional[str] = ..., nfce_id: _Optional[str] = ..., nfse_id: _Optional[str] = ..., person_id: _Optional[str] = ..., contract_number: _Optional[str] = ..., types: _Optional[_Iterable[str]] = ..., status: _Optional[_Iterable[str]] = ..., products_id: _Optional[_Iterable[str]] = ..., payment_method_id: _Optional[_Iterable[str]] = ..., due_date_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., due_date_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., closeDateGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., closeDateLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deliveryDateGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., deliveryDateLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., recurrenceDateGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., recurrenceDateLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraRegistroGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraRegistroLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., totalGte: _Optional[float] = ..., totalLte: _Optional[float] = ..., payment_id: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., currency: _Optional[_Iterable[str]] = ..., categoryId: _Optional[str] = ..., recurrence_type: _Optional[str] = ..., recurrence_increment: _Optional[int] = ..., contract_type: _Optional[str] = ..., source: _Optional[str] = ..., source_id: _Optional[str] = ...) -> None: ...

class CancelPedidoRequest(_message.Message):
    __slots__ = ("id", "reason")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class CancelPedidoResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class ClonePedidoRequest(_message.Message):
    __slots__ = ("id", "reason", "use_current_prices")
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    USE_CURRENT_PRICES_FIELD_NUMBER: _ClassVar[int]
    id: str
    reason: str
    use_current_prices: bool
    def __init__(self, id: _Optional[str] = ..., reason: _Optional[str] = ..., use_current_prices: _Optional[bool] = ...) -> None: ...

class ClonePedidoResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class ConfirmOrderReceiptRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ConfirmOrderReceiptResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class AddFilesRequest(_message.Message):
    __slots__ = ("id", "files", "skip_upload")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    SKIP_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    id: str
    files: _containers.RepeatedCompositeFieldContainer[_filemanager_pb2.File]
    skip_upload: bool
    def __init__(self, id: _Optional[str] = ..., files: _Optional[_Iterable[_Union[_filemanager_pb2.File, _Mapping]]] = ..., skip_upload: _Optional[bool] = ...) -> None: ...

class AddFilesResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class RemoveFilesRequest(_message.Message):
    __slots__ = ("id", "file_ids", "paths")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILE_IDS_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    id: str
    file_ids: _containers.RepeatedScalarFieldContainer[str]
    paths: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., file_ids: _Optional[_Iterable[str]] = ..., paths: _Optional[_Iterable[str]] = ...) -> None: ...

class RemoveFilesResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class SetFileApprovalRequest(_message.Message):
    __slots__ = ("id", "file_id", "status", "note")
    ID_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    id: str
    file_id: str
    status: _filemanager_pb2.FileApprovalStatus
    note: str
    def __init__(self, id: _Optional[str] = ..., file_id: _Optional[str] = ..., status: _Optional[_Union[_filemanager_pb2.FileApprovalStatus, str]] = ..., note: _Optional[str] = ...) -> None: ...

class SetFileApprovalResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class ExportOrdersRequest(_message.Message):
    __slots__ = ("format", "filter", "type", "include_metadata")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    format: _exports_pb2.ExportFormat
    filter: _filter_pb2.Filter
    type: str
    include_metadata: bool
    def __init__(self, format: _Optional[_Union[_exports_pb2.ExportFormat, str]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., type: _Optional[str] = ..., include_metadata: _Optional[bool] = ...) -> None: ...

class ExportOrdersResponse(_message.Message):
    __slots__ = ("export",)
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    export: _exports_pb2.ExportResponse
    def __init__(self, export: _Optional[_Union[_exports_pb2.ExportResponse, _Mapping]] = ...) -> None: ...

class SendReviewEmailRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SendReviewEmailResponse(_message.Message):
    __slots__ = ("sent_count",)
    SENT_COUNT_FIELD_NUMBER: _ClassVar[int]
    sent_count: int
    def __init__(self, sent_count: _Optional[int] = ...) -> None: ...

class GetPedidoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetPedidoResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class GenerateFromOrcamentoRequest(_message.Message):
    __slots__ = ("id", "type", "itens_serial")
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ITENS_SERIAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    type: TipoMovimentacao
    itens_serial: _containers.RepeatedCompositeFieldContainer[OrcamentoItemSerial]
    def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[TipoMovimentacao, str]] = ..., itens_serial: _Optional[_Iterable[_Union[OrcamentoItemSerial, _Mapping]]] = ...) -> None: ...

class OrcamentoItemSerial(_message.Message):
    __slots__ = ("orcamento_produto_id", "serial")
    ORCAMENTO_PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    orcamento_produto_id: str
    serial: SerialInfo
    def __init__(self, orcamento_produto_id: _Optional[str] = ..., serial: _Optional[_Union[SerialInfo, _Mapping]] = ...) -> None: ...

class GenerateFromOrcamentoResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class ListPedidoResponse(_message.Message):
    __slots__ = ("pedidoList",)
    PEDIDOLIST_FIELD_NUMBER: _ClassVar[int]
    pedidoList: _containers.RepeatedCompositeFieldContainer[Pedido]
    def __init__(self, pedidoList: _Optional[_Iterable[_Union[Pedido, _Mapping]]] = ...) -> None: ...

class AddProductRequest(_message.Message):
    __slots__ = ("parentId", "type", "productId", "product")
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    parentId: str
    type: TipoMovimentacao
    productId: str
    product: Produto
    def __init__(self, parentId: _Optional[str] = ..., type: _Optional[_Union[TipoMovimentacao, str]] = ..., productId: _Optional[str] = ..., product: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class AddProductResponse(_message.Message):
    __slots__ = ("pedido", "product")
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    product: Produto
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ..., product: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class UpdateProductRequest(_message.Message):
    __slots__ = ("parentId", "productId", "product")
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    parentId: str
    productId: str
    product: Produto
    def __init__(self, parentId: _Optional[str] = ..., productId: _Optional[str] = ..., product: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class UpdateProductResponse(_message.Message):
    __slots__ = ("pedido", "product")
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    product: Produto
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ..., product: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class DeleteProductRequest(_message.Message):
    __slots__ = ("parentId", "productId")
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    PRODUCTID_FIELD_NUMBER: _ClassVar[int]
    parentId: str
    productId: str
    def __init__(self, parentId: _Optional[str] = ..., productId: _Optional[str] = ...) -> None: ...

class DeleteProductResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class AddServiceRequest(_message.Message):
    __slots__ = ("parentId", "type", "serviceId", "service")
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVICEID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    parentId: str
    type: TipoMovimentacao
    serviceId: str
    service: Servico
    def __init__(self, parentId: _Optional[str] = ..., type: _Optional[_Union[TipoMovimentacao, str]] = ..., serviceId: _Optional[str] = ..., service: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class AddServiceResponse(_message.Message):
    __slots__ = ("pedido", "service")
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    service: Servico
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ..., service: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class UpdateServiceRequest(_message.Message):
    __slots__ = ("parentId", "serviceId", "service")
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    SERVICEID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    parentId: str
    serviceId: str
    service: Servico
    def __init__(self, parentId: _Optional[str] = ..., serviceId: _Optional[str] = ..., service: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class UpdateServiceResponse(_message.Message):
    __slots__ = ("pedido", "service")
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    service: Servico
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ..., service: _Optional[_Union[Servico, _Mapping]] = ...) -> None: ...

class DeleteServiceRequest(_message.Message):
    __slots__ = ("parentId", "serviceId", "quantity")
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    SERVICEID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    parentId: str
    serviceId: str
    quantity: float
    def __init__(self, parentId: _Optional[str] = ..., serviceId: _Optional[str] = ..., quantity: _Optional[float] = ...) -> None: ...

class DeleteServiceResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class AddPaymentRequest(_message.Message):
    __slots__ = ("parentId", "payments", "skip_financial_postings", "parent_ids")
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    SKIP_FINANCIAL_POSTINGS_FIELD_NUMBER: _ClassVar[int]
    PARENT_IDS_FIELD_NUMBER: _ClassVar[int]
    parentId: str
    payments: _containers.RepeatedCompositeFieldContainer[Pagamento]
    skip_financial_postings: bool
    parent_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, parentId: _Optional[str] = ..., payments: _Optional[_Iterable[_Union[Pagamento, _Mapping]]] = ..., skip_financial_postings: _Optional[bool] = ..., parent_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class AddPaymentResponse(_message.Message):
    __slots__ = ("pedido", "pagamento", "pedidos", "troco")
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    PEDIDOS_FIELD_NUMBER: _ClassVar[int]
    TROCO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    pagamento: Pagamento
    pedidos: _containers.RepeatedCompositeFieldContainer[Pedido]
    troco: float
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ..., pagamento: _Optional[_Union[Pagamento, _Mapping]] = ..., pedidos: _Optional[_Iterable[_Union[Pedido, _Mapping]]] = ..., troco: _Optional[float] = ...) -> None: ...

class DeletePaymentRequest(_message.Message):
    __slots__ = ("parentId", "paymentId")
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTID_FIELD_NUMBER: _ClassVar[int]
    parentId: str
    paymentId: str
    def __init__(self, parentId: _Optional[str] = ..., paymentId: _Optional[str] = ...) -> None: ...

class DeletePaymentResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class CancelPaymentRequest(_message.Message):
    __slots__ = ("parentId", "paymentId", "paymentOnlineId", "reason", "cancelOrder")
    PARENTID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTID_FIELD_NUMBER: _ClassVar[int]
    PAYMENTONLINEID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CANCELORDER_FIELD_NUMBER: _ClassVar[int]
    parentId: str
    paymentId: str
    paymentOnlineId: str
    reason: str
    cancelOrder: bool
    def __init__(self, parentId: _Optional[str] = ..., paymentId: _Optional[str] = ..., paymentOnlineId: _Optional[str] = ..., reason: _Optional[str] = ..., cancelOrder: _Optional[bool] = ...) -> None: ...

class CancelPaymentResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class EffectuatePaymentsRequest(_message.Message):
    __slots__ = ("parent_id",)
    PARENT_ID_FIELD_NUMBER: _ClassVar[int]
    parent_id: str
    def __init__(self, parent_id: _Optional[str] = ...) -> None: ...

class EffectuatePaymentsResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class SendByEmailRequest(_message.Message):
    __slots__ = ("pedidoId", "destEmail", "email_integration_id", "whatsapp_numero", "whatsapp_nome_destinatario", "whatsapp_integration_id", "message_template_id")
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    DESTEMAIL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NUMERO_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NOME_DESTINATARIO_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    pedidoId: str
    destEmail: str
    email_integration_id: str
    whatsapp_numero: str
    whatsapp_nome_destinatario: str
    whatsapp_integration_id: str
    message_template_id: str
    def __init__(self, pedidoId: _Optional[str] = ..., destEmail: _Optional[str] = ..., email_integration_id: _Optional[str] = ..., whatsapp_numero: _Optional[str] = ..., whatsapp_nome_destinatario: _Optional[str] = ..., whatsapp_integration_id: _Optional[str] = ..., message_template_id: _Optional[str] = ...) -> None: ...

class SendByEmailResponse(_message.Message):
    __slots__ = ("result", "whatsapp_web_message", "public_download_link")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_WEB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    result: str
    whatsapp_web_message: str
    public_download_link: str
    def __init__(self, result: _Optional[str] = ..., whatsapp_web_message: _Optional[str] = ..., public_download_link: _Optional[str] = ...) -> None: ...

class SendReminderRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SendReminderResponse(_message.Message):
    __slots__ = ("event", "falhas")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    FALHAS_FIELD_NUMBER: _ClassVar[int]
    event: _pedido_mesa_pb2.PedidoEvent
    falhas: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, event: _Optional[_Union[_pedido_mesa_pb2.PedidoEvent, _Mapping]] = ..., falhas: _Optional[_Iterable[str]] = ...) -> None: ...

class DownloadPdfPublicoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DownloadPdfPublicoResponse(_message.Message):
    __slots__ = ("filename", "pdf_base64")
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    PDF_BASE64_FIELD_NUMBER: _ClassVar[int]
    filename: str
    pdf_base64: str
    def __init__(self, filename: _Optional[str] = ..., pdf_base64: _Optional[str] = ...) -> None: ...

class AplicaTabelaPrecoRequest(_message.Message):
    __slots__ = ("pedidoId", "tabelaPreco")
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    TABELAPRECO_FIELD_NUMBER: _ClassVar[int]
    pedidoId: str
    tabelaPreco: str
    def __init__(self, pedidoId: _Optional[str] = ..., tabelaPreco: _Optional[str] = ...) -> None: ...

class AplicaTabelaPrecoResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class RecalcularComissaoRequest(_message.Message):
    __slots__ = ("ids", "sobrescrever_manuais", "incluir_fechados")
    IDS_FIELD_NUMBER: _ClassVar[int]
    SOBRESCREVER_MANUAIS_FIELD_NUMBER: _ClassVar[int]
    INCLUIR_FECHADOS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    sobrescrever_manuais: bool
    incluir_fechados: bool
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., sobrescrever_manuais: _Optional[bool] = ..., incluir_fechados: _Optional[bool] = ...) -> None: ...

class RecalcularComissaoResponse(_message.Message):
    __slots__ = ("pedidos", "recalculados", "ignorados")
    PEDIDOS_FIELD_NUMBER: _ClassVar[int]
    RECALCULADOS_FIELD_NUMBER: _ClassVar[int]
    IGNORADOS_FIELD_NUMBER: _ClassVar[int]
    pedidos: _containers.RepeatedCompositeFieldContainer[Pedido]
    recalculados: int
    ignorados: int
    def __init__(self, pedidos: _Optional[_Iterable[_Union[Pedido, _Mapping]]] = ..., recalculados: _Optional[int] = ..., ignorados: _Optional[int] = ...) -> None: ...

class Billing(_message.Message):
    __slots__ = ("enabled", "billing_plan_id", "billing_plan_name", "next_billing_date", "billings_count", "last_billing_date", "send_whatsapp", "whatsapp_integration_id", "ignore_billing_plan")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    NEXT_BILLING_DATE_FIELD_NUMBER: _ClassVar[int]
    BILLINGS_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_BILLING_DATE_FIELD_NUMBER: _ClassVar[int]
    SEND_WHATSAPP_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    IGNORE_BILLING_PLAN_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    billing_plan_id: str
    billing_plan_name: str
    next_billing_date: _timestamp_pb2.Timestamp
    billings_count: int
    last_billing_date: _timestamp_pb2.Timestamp
    send_whatsapp: bool
    whatsapp_integration_id: str
    ignore_billing_plan: bool
    def __init__(self, enabled: _Optional[bool] = ..., billing_plan_id: _Optional[str] = ..., billing_plan_name: _Optional[str] = ..., next_billing_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., billings_count: _Optional[int] = ..., last_billing_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., send_whatsapp: _Optional[bool] = ..., whatsapp_integration_id: _Optional[str] = ..., ignore_billing_plan: _Optional[bool] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("list_request", "reportType", "tipoRelatorio", "sendByEmail")
    LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    REPORTTYPE_FIELD_NUMBER: _ClassVar[int]
    TIPORELATORIO_FIELD_NUMBER: _ClassVar[int]
    SENDBYEMAIL_FIELD_NUMBER: _ClassVar[int]
    list_request: ListPedidoRequest
    reportType: ReportType
    tipoRelatorio: str
    sendByEmail: str
    def __init__(self, list_request: _Optional[_Union[ListPedidoRequest, _Mapping]] = ..., reportType: _Optional[_Union[ReportType, str]] = ..., tipoRelatorio: _Optional[str] = ..., sendByEmail: _Optional[str] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class OriginInfo(_message.Message):
    __slots__ = ("name", "id", "reference_number", "origin_type")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    reference_number: str
    origin_type: Origin
    def __init__(self, name: _Optional[str] = ..., id: _Optional[str] = ..., reference_number: _Optional[str] = ..., origin_type: _Optional[_Union[Origin, str]] = ...) -> None: ...

class OrderTag(_message.Message):
    __slots__ = ("value", "color")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    value: str
    color: str
    def __init__(self, value: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class OrderAcompanhamento(_message.Message):
    __slots__ = ("id", "code", "name", "color")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    code: str
    name: str
    color: str
    def __init__(self, id: _Optional[str] = ..., code: _Optional[str] = ..., name: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class SetAcompanhamentoRequest(_message.Message):
    __slots__ = ("id", "acompanhamento_id", "code")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACOMPANHAMENTO_ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    acompanhamento_id: str
    code: str
    def __init__(self, id: _Optional[str] = ..., acompanhamento_id: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class SetAcompanhamentoResponse(_message.Message):
    __slots__ = ("acompanhamento",)
    ACOMPANHAMENTO_FIELD_NUMBER: _ClassVar[int]
    acompanhamento: OrderAcompanhamento
    def __init__(self, acompanhamento: _Optional[_Union[OrderAcompanhamento, _Mapping]] = ...) -> None: ...

class Pedido(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "account_id", "fields", "origem", "origemId", "tipo", "situacao", "tags", "tipoMoeda", "tipoMoedaCotacao", "tabelaPreco", "importadoEm", "pessoa", "vendedor", "numero", "dataHoraRegistro", "dataHoraFechamento", "previsaoEntrega", "previsaoEntregaDescricao", "dataHoraInicio", "dataHoraEntrega", "tempoDecorrido", "descontoValor", "acrescimoValor", "valorSubtotal", "valorTotalServico", "valorTotalProduto", "valorTotal", "valorTotalPago", "cashbackValor", "comissaoValor", "nfeNumero", "nfeUrlDanfe", "nfeChave", "nfeSerie", "nfeId", "nfeSituacao", "nfe_forma_emissao", "nfeDataHoraEmissao", "nfceNumero", "nfceUrlDanfe", "nfceUrlXml", "nfceSerie", "nfceChave", "nfceId", "nfceSituacao", "nfce_forma_emissao", "nfceDataHoraEmissao", "nfseUrlDanfe", "nfseChave", "nfseNumero", "nfseSituacao", "obs", "cancelamentoMotivo", "cancelamentoUsuarioId", "cancelamentoUsuarioNome", "cancelamentoDataHora", "produtos", "servicos", "pagamentos", "transactions_online", "mesclagemId", "pedidosVinculados", "descontoAplicado", "descontoAplicadosCaption", "cashbackAplicado", "cashbackAplicadosCaption", "licenciamento", "consiguinacao", "importado", "os", "otica", "partnership", "cuponsSorteios", "convertedBy", "rentCar", "contract", "files", "confirmation_receipt", "origin", "billing", "delivery", "checkout_payment_selection", "dfe", "consumption_control", "events", "diasGarantia", "dataFimGarantia", "warranty", "recorrencias", "devolucao_id", "devolucao_numero", "webhooks", "external_reference", "acompanhamento", "cupomAplicado", "org_id", "org_nome", "divida", "validade", "validadeDescricao", "qr_code_documento", "pedido_compra", "agenda_event_id", "lembrete_cliente", "resposta_cliente", "posto_veiculo_id", "posto_placa", "posto_km", "posto_motorista_nome")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    ORIGEMID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    TIPOMOEDA_FIELD_NUMBER: _ClassVar[int]
    TIPOMOEDACOTACAO_FIELD_NUMBER: _ClassVar[int]
    TABELAPRECO_FIELD_NUMBER: _ClassVar[int]
    IMPORTADOEM_FIELD_NUMBER: _ClassVar[int]
    PESSOA_FIELD_NUMBER: _ClassVar[int]
    VENDEDOR_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAREGISTRO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAFECHAMENTO_FIELD_NUMBER: _ClassVar[int]
    PREVISAOENTREGA_FIELD_NUMBER: _ClassVar[int]
    PREVISAOENTREGADESCRICAO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAINICIO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAENTREGA_FIELD_NUMBER: _ClassVar[int]
    TEMPODECORRIDO_FIELD_NUMBER: _ClassVar[int]
    DESCONTOVALOR_FIELD_NUMBER: _ClassVar[int]
    ACRESCIMOVALOR_FIELD_NUMBER: _ClassVar[int]
    VALORSUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    VALORTOTALSERVICO_FIELD_NUMBER: _ClassVar[int]
    VALORTOTALPRODUTO_FIELD_NUMBER: _ClassVar[int]
    VALORTOTAL_FIELD_NUMBER: _ClassVar[int]
    VALORTOTALPAGO_FIELD_NUMBER: _ClassVar[int]
    CASHBACKVALOR_FIELD_NUMBER: _ClassVar[int]
    COMISSAOVALOR_FIELD_NUMBER: _ClassVar[int]
    NFENUMERO_FIELD_NUMBER: _ClassVar[int]
    NFEURLDANFE_FIELD_NUMBER: _ClassVar[int]
    NFECHAVE_FIELD_NUMBER: _ClassVar[int]
    NFESERIE_FIELD_NUMBER: _ClassVar[int]
    NFEID_FIELD_NUMBER: _ClassVar[int]
    NFESITUACAO_FIELD_NUMBER: _ClassVar[int]
    NFE_FORMA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    NFEDATAHORAEMISSAO_FIELD_NUMBER: _ClassVar[int]
    NFCENUMERO_FIELD_NUMBER: _ClassVar[int]
    NFCEURLDANFE_FIELD_NUMBER: _ClassVar[int]
    NFCEURLXML_FIELD_NUMBER: _ClassVar[int]
    NFCESERIE_FIELD_NUMBER: _ClassVar[int]
    NFCECHAVE_FIELD_NUMBER: _ClassVar[int]
    NFCEID_FIELD_NUMBER: _ClassVar[int]
    NFCESITUACAO_FIELD_NUMBER: _ClassVar[int]
    NFCE_FORMA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    NFCEDATAHORAEMISSAO_FIELD_NUMBER: _ClassVar[int]
    NFSEURLDANFE_FIELD_NUMBER: _ClassVar[int]
    NFSECHAVE_FIELD_NUMBER: _ClassVar[int]
    NFSENUMERO_FIELD_NUMBER: _ClassVar[int]
    NFSESITUACAO_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTOMOTIVO_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTOUSUARIOID_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTOUSUARIONOME_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTODATAHORA_FIELD_NUMBER: _ClassVar[int]
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    SERVICOS_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTOS_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    MESCLAGEMID_FIELD_NUMBER: _ClassVar[int]
    PEDIDOSVINCULADOS_FIELD_NUMBER: _ClassVar[int]
    DESCONTOAPLICADO_FIELD_NUMBER: _ClassVar[int]
    DESCONTOAPLICADOSCAPTION_FIELD_NUMBER: _ClassVar[int]
    CASHBACKAPLICADO_FIELD_NUMBER: _ClassVar[int]
    CASHBACKAPLICADOSCAPTION_FIELD_NUMBER: _ClassVar[int]
    LICENCIAMENTO_FIELD_NUMBER: _ClassVar[int]
    CONSIGUINACAO_FIELD_NUMBER: _ClassVar[int]
    IMPORTADO_FIELD_NUMBER: _ClassVar[int]
    OS_FIELD_NUMBER: _ClassVar[int]
    OTICA_FIELD_NUMBER: _ClassVar[int]
    PARTNERSHIP_FIELD_NUMBER: _ClassVar[int]
    CUPONSSORTEIOS_FIELD_NUMBER: _ClassVar[int]
    CONVERTEDBY_FIELD_NUMBER: _ClassVar[int]
    RENTCAR_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    FILES_FIELD_NUMBER: _ClassVar[int]
    CONFIRMATION_RECEIPT_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    BILLING_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_PAYMENT_SELECTION_FIELD_NUMBER: _ClassVar[int]
    DFE_FIELD_NUMBER: _ClassVar[int]
    CONSUMPTION_CONTROL_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    DIASGARANTIA_FIELD_NUMBER: _ClassVar[int]
    DATAFIMGARANTIA_FIELD_NUMBER: _ClassVar[int]
    WARRANTY_FIELD_NUMBER: _ClassVar[int]
    RECORRENCIAS_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_ID_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_NUMERO_FIELD_NUMBER: _ClassVar[int]
    WEBHOOKS_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    ACOMPANHAMENTO_FIELD_NUMBER: _ClassVar[int]
    CUPOMAPLICADO_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_NOME_FIELD_NUMBER: _ClassVar[int]
    DIVIDA_FIELD_NUMBER: _ClassVar[int]
    VALIDADE_FIELD_NUMBER: _ClassVar[int]
    VALIDADEDESCRICAO_FIELD_NUMBER: _ClassVar[int]
    QR_CODE_DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_COMPRA_FIELD_NUMBER: _ClassVar[int]
    AGENDA_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    LEMBRETE_CLIENTE_FIELD_NUMBER: _ClassVar[int]
    RESPOSTA_CLIENTE_FIELD_NUMBER: _ClassVar[int]
    POSTO_VEICULO_ID_FIELD_NUMBER: _ClassVar[int]
    POSTO_PLACA_FIELD_NUMBER: _ClassVar[int]
    POSTO_KM_FIELD_NUMBER: _ClassVar[int]
    POSTO_MOTORISTA_NOME_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    account_id: str
    fields: _metadata_pb2.BasicFields
    origem: str
    origemId: str
    tipo: str
    situacao: str
    tags: _containers.RepeatedCompositeFieldContainer[OrderTag]
    tipoMoeda: str
    tipoMoedaCotacao: float
    tabelaPreco: str
    importadoEm: _timestamp_pb2.Timestamp
    pessoa: Pessoa
    vendedor: Pessoa
    numero: int
    dataHoraRegistro: _timestamp_pb2.Timestamp
    dataHoraFechamento: _timestamp_pb2.Timestamp
    previsaoEntrega: _timestamp_pb2.Timestamp
    previsaoEntregaDescricao: str
    dataHoraInicio: _timestamp_pb2.Timestamp
    dataHoraEntrega: _timestamp_pb2.Timestamp
    tempoDecorrido: str
    descontoValor: float
    acrescimoValor: float
    valorSubtotal: float
    valorTotalServico: float
    valorTotalProduto: float
    valorTotal: float
    valorTotalPago: float
    cashbackValor: float
    comissaoValor: float
    nfeNumero: int
    nfeUrlDanfe: str
    nfeChave: str
    nfeSerie: int
    nfeId: str
    nfeSituacao: str
    nfe_forma_emissao: str
    nfeDataHoraEmissao: _timestamp_pb2.Timestamp
    nfceNumero: int
    nfceUrlDanfe: str
    nfceUrlXml: str
    nfceSerie: int
    nfceChave: str
    nfceId: str
    nfceSituacao: str
    nfce_forma_emissao: str
    nfceDataHoraEmissao: _timestamp_pb2.Timestamp
    nfseUrlDanfe: str
    nfseChave: str
    nfseNumero: str
    nfseSituacao: str
    obs: str
    cancelamentoMotivo: str
    cancelamentoUsuarioId: str
    cancelamentoUsuarioNome: str
    cancelamentoDataHora: _timestamp_pb2.Timestamp
    produtos: _containers.RepeatedCompositeFieldContainer[Produto]
    servicos: _containers.RepeatedCompositeFieldContainer[Servico]
    pagamentos: _containers.RepeatedCompositeFieldContainer[Pagamento]
    transactions_online: TransactionsOnline
    mesclagemId: str
    pedidosVinculados: _containers.RepeatedCompositeFieldContainer[PedidoVinculado]
    descontoAplicado: DescontoAplicadosModel
    descontoAplicadosCaption: str
    cashbackAplicado: CashbackAplicadosModel
    cashbackAplicadosCaption: str
    licenciamento: LicenciamentoModel
    consiguinacao: bool
    importado: bool
    os: OrdemServico
    otica: _pedido_otica_pb2.Otica
    partnership: Partnership
    cuponsSorteios: _containers.RepeatedCompositeFieldContainer[CuponsSorteio]
    convertedBy: str
    rentCar: _rentcar_model_pb2.Reservation
    contract: Contract
    files: _containers.RepeatedCompositeFieldContainer[_filemanager_pb2.File]
    confirmation_receipt: ConfirmationOrderReceipt
    origin: OriginInfo
    billing: Billing
    delivery: DeliveryInfo
    checkout_payment_selection: CheckoutPaymentSelection
    dfe: Dfe
    consumption_control: _pedido_mesa_pb2.ConsumptionControl
    events: _containers.RepeatedCompositeFieldContainer[_pedido_mesa_pb2.PedidoEvent]
    diasGarantia: float
    dataFimGarantia: _timestamp_pb2.Timestamp
    warranty: Warranty
    recorrencias: _containers.RepeatedCompositeFieldContainer[Pedido]
    devolucao_id: str
    devolucao_numero: int
    webhooks: _containers.RepeatedCompositeFieldContainer[PedidoWebhook]
    external_reference: str
    acompanhamento: OrderAcompanhamento
    cupomAplicado: CupomAplicadoModel
    org_id: str
    org_nome: str
    divida: float
    validade: _timestamp_pb2.Timestamp
    validadeDescricao: str
    qr_code_documento: QrCodeDocumento
    pedido_compra: str
    agenda_event_id: str
    lembrete_cliente: bool
    resposta_cliente: RespostaCliente
    posto_veiculo_id: str
    posto_placa: str
    posto_km: float
    posto_motorista_nome: str
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., account_id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., origem: _Optional[str] = ..., origemId: _Optional[str] = ..., tipo: _Optional[str] = ..., situacao: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[OrderTag, _Mapping]]] = ..., tipoMoeda: _Optional[str] = ..., tipoMoedaCotacao: _Optional[float] = ..., tabelaPreco: _Optional[str] = ..., importadoEm: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., pessoa: _Optional[_Union[Pessoa, _Mapping]] = ..., vendedor: _Optional[_Union[Pessoa, _Mapping]] = ..., numero: _Optional[int] = ..., dataHoraRegistro: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraFechamento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., previsaoEntrega: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., previsaoEntregaDescricao: _Optional[str] = ..., dataHoraInicio: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraEntrega: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tempoDecorrido: _Optional[str] = ..., descontoValor: _Optional[float] = ..., acrescimoValor: _Optional[float] = ..., valorSubtotal: _Optional[float] = ..., valorTotalServico: _Optional[float] = ..., valorTotalProduto: _Optional[float] = ..., valorTotal: _Optional[float] = ..., valorTotalPago: _Optional[float] = ..., cashbackValor: _Optional[float] = ..., comissaoValor: _Optional[float] = ..., nfeNumero: _Optional[int] = ..., nfeUrlDanfe: _Optional[str] = ..., nfeChave: _Optional[str] = ..., nfeSerie: _Optional[int] = ..., nfeId: _Optional[str] = ..., nfeSituacao: _Optional[str] = ..., nfe_forma_emissao: _Optional[str] = ..., nfeDataHoraEmissao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., nfceNumero: _Optional[int] = ..., nfceUrlDanfe: _Optional[str] = ..., nfceUrlXml: _Optional[str] = ..., nfceSerie: _Optional[int] = ..., nfceChave: _Optional[str] = ..., nfceId: _Optional[str] = ..., nfceSituacao: _Optional[str] = ..., nfce_forma_emissao: _Optional[str] = ..., nfceDataHoraEmissao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., nfseUrlDanfe: _Optional[str] = ..., nfseChave: _Optional[str] = ..., nfseNumero: _Optional[str] = ..., nfseSituacao: _Optional[str] = ..., obs: _Optional[str] = ..., cancelamentoMotivo: _Optional[str] = ..., cancelamentoUsuarioId: _Optional[str] = ..., cancelamentoUsuarioNome: _Optional[str] = ..., cancelamentoDataHora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., produtos: _Optional[_Iterable[_Union[Produto, _Mapping]]] = ..., servicos: _Optional[_Iterable[_Union[Servico, _Mapping]]] = ..., pagamentos: _Optional[_Iterable[_Union[Pagamento, _Mapping]]] = ..., transactions_online: _Optional[_Union[TransactionsOnline, _Mapping]] = ..., mesclagemId: _Optional[str] = ..., pedidosVinculados: _Optional[_Iterable[_Union[PedidoVinculado, _Mapping]]] = ..., descontoAplicado: _Optional[_Union[DescontoAplicadosModel, _Mapping]] = ..., descontoAplicadosCaption: _Optional[str] = ..., cashbackAplicado: _Optional[_Union[CashbackAplicadosModel, _Mapping]] = ..., cashbackAplicadosCaption: _Optional[str] = ..., licenciamento: _Optional[_Union[LicenciamentoModel, _Mapping]] = ..., consiguinacao: _Optional[bool] = ..., importado: _Optional[bool] = ..., os: _Optional[_Union[OrdemServico, _Mapping]] = ..., otica: _Optional[_Union[_pedido_otica_pb2.Otica, _Mapping]] = ..., partnership: _Optional[_Union[Partnership, _Mapping]] = ..., cuponsSorteios: _Optional[_Iterable[_Union[CuponsSorteio, _Mapping]]] = ..., convertedBy: _Optional[str] = ..., rentCar: _Optional[_Union[_rentcar_model_pb2.Reservation, _Mapping]] = ..., contract: _Optional[_Union[Contract, _Mapping]] = ..., files: _Optional[_Iterable[_Union[_filemanager_pb2.File, _Mapping]]] = ..., confirmation_receipt: _Optional[_Union[ConfirmationOrderReceipt, _Mapping]] = ..., origin: _Optional[_Union[OriginInfo, _Mapping]] = ..., billing: _Optional[_Union[Billing, _Mapping]] = ..., delivery: _Optional[_Union[DeliveryInfo, _Mapping]] = ..., checkout_payment_selection: _Optional[_Union[CheckoutPaymentSelection, _Mapping]] = ..., dfe: _Optional[_Union[Dfe, _Mapping]] = ..., consumption_control: _Optional[_Union[_pedido_mesa_pb2.ConsumptionControl, _Mapping]] = ..., events: _Optional[_Iterable[_Union[_pedido_mesa_pb2.PedidoEvent, _Mapping]]] = ..., diasGarantia: _Optional[float] = ..., dataFimGarantia: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., warranty: _Optional[_Union[Warranty, _Mapping]] = ..., recorrencias: _Optional[_Iterable[_Union[Pedido, _Mapping]]] = ..., devolucao_id: _Optional[str] = ..., devolucao_numero: _Optional[int] = ..., webhooks: _Optional[_Iterable[_Union[PedidoWebhook, _Mapping]]] = ..., external_reference: _Optional[str] = ..., acompanhamento: _Optional[_Union[OrderAcompanhamento, _Mapping]] = ..., cupomAplicado: _Optional[_Union[CupomAplicadoModel, _Mapping]] = ..., org_id: _Optional[str] = ..., org_nome: _Optional[str] = ..., divida: _Optional[float] = ..., validade: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., validadeDescricao: _Optional[str] = ..., qr_code_documento: _Optional[_Union[QrCodeDocumento, _Mapping]] = ..., pedido_compra: _Optional[str] = ..., agenda_event_id: _Optional[str] = ..., lembrete_cliente: _Optional[bool] = ..., resposta_cliente: _Optional[_Union[RespostaCliente, str]] = ..., posto_veiculo_id: _Optional[str] = ..., posto_placa: _Optional[str] = ..., posto_km: _Optional[float] = ..., posto_motorista_nome: _Optional[str] = ...) -> None: ...

class QrCodeDocumento(_message.Message):
    __slots__ = ("ativo", "dias_validade")
    ATIVO_FIELD_NUMBER: _ClassVar[int]
    DIAS_VALIDADE_FIELD_NUMBER: _ClassVar[int]
    ativo: bool
    dias_validade: int
    def __init__(self, ativo: _Optional[bool] = ..., dias_validade: _Optional[int] = ...) -> None: ...

class PedidoWebhook(_message.Message):
    __slots__ = ("id", "url", "events", "secret", "last_attempt_at", "last_status", "last_error", "attempts")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    LAST_ATTEMPT_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_FIELD_NUMBER: _ClassVar[int]
    ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    events: _containers.RepeatedScalarFieldContainer[str]
    secret: str
    last_attempt_at: _timestamp_pb2.Timestamp
    last_status: str
    last_error: str
    attempts: int
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., events: _Optional[_Iterable[str]] = ..., secret: _Optional[str] = ..., last_attempt_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_status: _Optional[str] = ..., last_error: _Optional[str] = ..., attempts: _Optional[int] = ...) -> None: ...

class Warranty(_message.Message):
    __slots__ = ("active_until", "items_count", "value")
    ACTIVE_UNTIL_FIELD_NUMBER: _ClassVar[int]
    ITEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    active_until: _timestamp_pb2.Timestamp
    items_count: int
    value: float
    def __init__(self, active_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., items_count: _Optional[int] = ..., value: _Optional[float] = ...) -> None: ...

class OnlineTransactionLink(_message.Message):
    __slots__ = ("id", "url", "description", "payment_methods", "max_installments", "preferred_due_date", "payment_link_expiration_date")
    ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTALLMENTS_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_LINK_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    id: str
    url: str
    description: str
    payment_methods: _containers.RepeatedCompositeFieldContainer[PaymentMethod]
    max_installments: int
    preferred_due_date: _timestamp_pb2.Timestamp
    payment_link_expiration_date: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., url: _Optional[str] = ..., description: _Optional[str] = ..., payment_methods: _Optional[_Iterable[_Union[PaymentMethod, _Mapping]]] = ..., max_installments: _Optional[int] = ..., preferred_due_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payment_link_expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class TransactionsOnline(_message.Message):
    __slots__ = ("checkout_url", "max_installments", "preferred_due_date", "payment_link_expiration_date", "payment_methods", "links")
    CHECKOUT_URL_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTALLMENTS_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_LINK_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    checkout_url: str
    max_installments: int
    preferred_due_date: _timestamp_pb2.Timestamp
    payment_link_expiration_date: _timestamp_pb2.Timestamp
    payment_methods: _containers.RepeatedCompositeFieldContainer[PaymentMethod]
    links: _containers.RepeatedCompositeFieldContainer[OnlineTransactionLink]
    def __init__(self, checkout_url: _Optional[str] = ..., max_installments: _Optional[int] = ..., preferred_due_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payment_link_expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., payment_methods: _Optional[_Iterable[_Union[PaymentMethod, _Mapping]]] = ..., links: _Optional[_Iterable[_Union[OnlineTransactionLink, _Mapping]]] = ...) -> None: ...

class PaymentMethod(_message.Message):
    __slots__ = ("payment_method_id", "payment_method_name")
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    payment_method_id: str
    payment_method_name: str
    def __init__(self, payment_method_id: _Optional[str] = ..., payment_method_name: _Optional[str] = ...) -> None: ...

class CheckoutPaymentSelection(_message.Message):
    __slots__ = ("payment_method_id", "payment_method_name", "payment_type", "charge_mode", "context", "selected_at", "note")
    PAYMENT_METHOD_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHARGE_MODE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SELECTED_AT_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    payment_method_id: str
    payment_method_name: str
    payment_type: str
    charge_mode: CheckoutPaymentChargeMode
    context: CheckoutPaymentContext
    selected_at: _timestamp_pb2.Timestamp
    note: str
    def __init__(self, payment_method_id: _Optional[str] = ..., payment_method_name: _Optional[str] = ..., payment_type: _Optional[str] = ..., charge_mode: _Optional[_Union[CheckoutPaymentChargeMode, str]] = ..., context: _Optional[_Union[CheckoutPaymentContext, str]] = ..., selected_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., note: _Optional[str] = ...) -> None: ...

class OrdemServico(_message.Message):
    __slots__ = ("situacao", "numeroSerie", "chassi", "km", "tipoObjetoId", "tipoObjetoNome", "marcaId", "marcaNome", "modelo", "defeitoReclamado", "acessorios", "parecerTecnico", "responsavelTecnicoId", "responsavelTecnicoNome", "observacoes_internas", "garantidor_id", "garantidor_nome", "garantidor_senha", "nf_venda_numero", "certificado_garantia_numero", "data_compra", "revendedor", "nf_entrada_numero", "nf_entrada_valor", "nf_entrada_emissor_id", "nf_entrada_emissor_nome", "os_terceiros_numero", "os_fabricante_numero", "os_terceiros_emissor_id", "os_terceiros_emissor_nome")
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    NUMEROSERIE_FIELD_NUMBER: _ClassVar[int]
    CHASSI_FIELD_NUMBER: _ClassVar[int]
    KM_FIELD_NUMBER: _ClassVar[int]
    TIPOOBJETOID_FIELD_NUMBER: _ClassVar[int]
    TIPOOBJETONOME_FIELD_NUMBER: _ClassVar[int]
    MARCAID_FIELD_NUMBER: _ClassVar[int]
    MARCANOME_FIELD_NUMBER: _ClassVar[int]
    MODELO_FIELD_NUMBER: _ClassVar[int]
    DEFEITORECLAMADO_FIELD_NUMBER: _ClassVar[int]
    ACESSORIOS_FIELD_NUMBER: _ClassVar[int]
    PARECERTECNICO_FIELD_NUMBER: _ClassVar[int]
    RESPONSAVELTECNICOID_FIELD_NUMBER: _ClassVar[int]
    RESPONSAVELTECNICONOME_FIELD_NUMBER: _ClassVar[int]
    OBSERVACOES_INTERNAS_FIELD_NUMBER: _ClassVar[int]
    GARANTIDOR_ID_FIELD_NUMBER: _ClassVar[int]
    GARANTIDOR_NOME_FIELD_NUMBER: _ClassVar[int]
    GARANTIDOR_SENHA_FIELD_NUMBER: _ClassVar[int]
    NF_VENDA_NUMERO_FIELD_NUMBER: _ClassVar[int]
    CERTIFICADO_GARANTIA_NUMERO_FIELD_NUMBER: _ClassVar[int]
    DATA_COMPRA_FIELD_NUMBER: _ClassVar[int]
    REVENDEDOR_FIELD_NUMBER: _ClassVar[int]
    NF_ENTRADA_NUMERO_FIELD_NUMBER: _ClassVar[int]
    NF_ENTRADA_VALOR_FIELD_NUMBER: _ClassVar[int]
    NF_ENTRADA_EMISSOR_ID_FIELD_NUMBER: _ClassVar[int]
    NF_ENTRADA_EMISSOR_NOME_FIELD_NUMBER: _ClassVar[int]
    OS_TERCEIROS_NUMERO_FIELD_NUMBER: _ClassVar[int]
    OS_FABRICANTE_NUMERO_FIELD_NUMBER: _ClassVar[int]
    OS_TERCEIROS_EMISSOR_ID_FIELD_NUMBER: _ClassVar[int]
    OS_TERCEIROS_EMISSOR_NOME_FIELD_NUMBER: _ClassVar[int]
    situacao: str
    numeroSerie: str
    chassi: str
    km: str
    tipoObjetoId: str
    tipoObjetoNome: str
    marcaId: str
    marcaNome: str
    modelo: str
    defeitoReclamado: str
    acessorios: str
    parecerTecnico: str
    responsavelTecnicoId: str
    responsavelTecnicoNome: str
    observacoes_internas: str
    garantidor_id: str
    garantidor_nome: str
    garantidor_senha: str
    nf_venda_numero: str
    certificado_garantia_numero: str
    data_compra: _timestamp_pb2.Timestamp
    revendedor: str
    nf_entrada_numero: str
    nf_entrada_valor: float
    nf_entrada_emissor_id: str
    nf_entrada_emissor_nome: str
    os_terceiros_numero: str
    os_fabricante_numero: str
    os_terceiros_emissor_id: str
    os_terceiros_emissor_nome: str
    def __init__(self, situacao: _Optional[str] = ..., numeroSerie: _Optional[str] = ..., chassi: _Optional[str] = ..., km: _Optional[str] = ..., tipoObjetoId: _Optional[str] = ..., tipoObjetoNome: _Optional[str] = ..., marcaId: _Optional[str] = ..., marcaNome: _Optional[str] = ..., modelo: _Optional[str] = ..., defeitoReclamado: _Optional[str] = ..., acessorios: _Optional[str] = ..., parecerTecnico: _Optional[str] = ..., responsavelTecnicoId: _Optional[str] = ..., responsavelTecnicoNome: _Optional[str] = ..., observacoes_internas: _Optional[str] = ..., garantidor_id: _Optional[str] = ..., garantidor_nome: _Optional[str] = ..., garantidor_senha: _Optional[str] = ..., nf_venda_numero: _Optional[str] = ..., certificado_garantia_numero: _Optional[str] = ..., data_compra: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., revendedor: _Optional[str] = ..., nf_entrada_numero: _Optional[str] = ..., nf_entrada_valor: _Optional[float] = ..., nf_entrada_emissor_id: _Optional[str] = ..., nf_entrada_emissor_nome: _Optional[str] = ..., os_terceiros_numero: _Optional[str] = ..., os_fabricante_numero: _Optional[str] = ..., os_terceiros_emissor_id: _Optional[str] = ..., os_terceiros_emissor_nome: _Optional[str] = ...) -> None: ...

class Contract(_message.Message):
    __slots__ = ("number", "type", "recurrence_type", "recurrence_increment", "recurrence_due_date", "status", "block_reason", "last_access", "recurrence_created_id", "recurrence_created_number", "start_date", "courtesy", "renewal_number", "grace_period_days", "auto_renew_disabled", "status_reason", "released_at", "trial_days", "previous_due_date", "released_until", "trial_ends_at", "full_period_total")
    class LastAccess(_message.Message):
        __slots__ = ("last_date", "user_name")
        LAST_DATE_FIELD_NUMBER: _ClassVar[int]
        USER_NAME_FIELD_NUMBER: _ClassVar[int]
        last_date: _timestamp_pb2.Timestamp
        user_name: str
        def __init__(self, last_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_name: _Optional[str] = ...) -> None: ...
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    BLOCK_REASON_FIELD_NUMBER: _ClassVar[int]
    LAST_ACCESS_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_CREATED_ID_FIELD_NUMBER: _ClassVar[int]
    RECURRENCE_CREATED_NUMBER_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    COURTESY_FIELD_NUMBER: _ClassVar[int]
    RENEWAL_NUMBER_FIELD_NUMBER: _ClassVar[int]
    GRACE_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    AUTO_RENEW_DISABLED_FIELD_NUMBER: _ClassVar[int]
    STATUS_REASON_FIELD_NUMBER: _ClassVar[int]
    RELEASED_AT_FIELD_NUMBER: _ClassVar[int]
    TRIAL_DAYS_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_DUE_DATE_FIELD_NUMBER: _ClassVar[int]
    RELEASED_UNTIL_FIELD_NUMBER: _ClassVar[int]
    TRIAL_ENDS_AT_FIELD_NUMBER: _ClassVar[int]
    FULL_PERIOD_TOTAL_FIELD_NUMBER: _ClassVar[int]
    number: str
    type: ContractType
    recurrence_type: RecurrenceType
    recurrence_increment: int
    recurrence_due_date: _timestamp_pb2.Timestamp
    status: ContractStatus
    block_reason: str
    last_access: Contract.LastAccess
    recurrence_created_id: str
    recurrence_created_number: str
    start_date: _timestamp_pb2.Timestamp
    courtesy: bool
    renewal_number: int
    grace_period_days: int
    auto_renew_disabled: bool
    status_reason: str
    released_at: _timestamp_pb2.Timestamp
    trial_days: int
    previous_due_date: _timestamp_pb2.Timestamp
    released_until: _timestamp_pb2.Timestamp
    trial_ends_at: _timestamp_pb2.Timestamp
    full_period_total: float
    def __init__(self, number: _Optional[str] = ..., type: _Optional[_Union[ContractType, str]] = ..., recurrence_type: _Optional[_Union[RecurrenceType, str]] = ..., recurrence_increment: _Optional[int] = ..., recurrence_due_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[_Union[ContractStatus, str]] = ..., block_reason: _Optional[str] = ..., last_access: _Optional[_Union[Contract.LastAccess, _Mapping]] = ..., recurrence_created_id: _Optional[str] = ..., recurrence_created_number: _Optional[str] = ..., start_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., courtesy: _Optional[bool] = ..., renewal_number: _Optional[int] = ..., grace_period_days: _Optional[int] = ..., auto_renew_disabled: _Optional[bool] = ..., status_reason: _Optional[str] = ..., released_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., trial_days: _Optional[int] = ..., previous_due_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., released_until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., trial_ends_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., full_period_total: _Optional[float] = ...) -> None: ...

class BatchInfo(_message.Message):
    __slots__ = ("id", "batch_number", "expiration_date", "manufacturing_date", "quantity")
    ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURING_DATE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    batch_number: str
    expiration_date: _timestamp_pb2.Timestamp
    manufacturing_date: _timestamp_pb2.Timestamp
    quantity: int
    def __init__(self, id: _Optional[str] = ..., batch_number: _Optional[str] = ..., expiration_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., manufacturing_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., quantity: _Optional[int] = ...) -> None: ...

class SerialInfo(_message.Message):
    __slots__ = ("ids", "serial_numbers")
    IDS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    serial_numbers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., serial_numbers: _Optional[_Iterable[str]] = ...) -> None: ...

class Produto(_message.Message):
    __slots__ = ("id", "createdAt", "updatedAt", "userId", "userName", "tipo", "nome", "descricao", "produtoId", "pedidoId", "pedidoProdutoId", "codigo", "un", "codigoAnp", "codigoAnpDescricao", "postoNumBico", "postoNumBomba", "postoNumTanque", "postoEncerranteInicial", "postoEncerranteFinal", "postoAbastecimentoIds", "postoFrentistaId", "postoFrentistaNome", "ncm", "obs", "vendedorId", "vendedorNome", "comissaoValor", "comissaoPercentual", "comprimento", "largura", "medida", "profundidade", "quantidade", "tabelaPreco", "valorUnitario", "diferencaValorVenda", "valorUnitarioOriginal", "custoUnitario", "lucroBrutoUnitario", "lucroLiquidoUnitario", "descontoValor", "descontoAplicado", "acrescimoValor", "valorSubtotal", "valorTotal", "ValorCompra", "descontoRateado", "pesoUnitario", "composto", "compostoString", "composicao", "color", "size", "referencia", "batch", "review_date", "variation_product_id", "serial", "diasGarantia", "dataFimGarantia", "comissao_manual", "tipoGarantia", "comodato", "valor_reposicao", "stock_decrease_applied", "skip_stock_decrease", "producao", "imagemUrl", "precoPromocionalAplicado", "numero_item", "observacao", "pedido_compra_item")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    PRODUTOID_FIELD_NUMBER: _ClassVar[int]
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    PEDIDOPRODUTOID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    CODIGOANP_FIELD_NUMBER: _ClassVar[int]
    CODIGOANPDESCRICAO_FIELD_NUMBER: _ClassVar[int]
    POSTONUMBICO_FIELD_NUMBER: _ClassVar[int]
    POSTONUMBOMBA_FIELD_NUMBER: _ClassVar[int]
    POSTONUMTANQUE_FIELD_NUMBER: _ClassVar[int]
    POSTOENCERRANTEINICIAL_FIELD_NUMBER: _ClassVar[int]
    POSTOENCERRANTEFINAL_FIELD_NUMBER: _ClassVar[int]
    POSTOABASTECIMENTOIDS_FIELD_NUMBER: _ClassVar[int]
    POSTOFRENTISTAID_FIELD_NUMBER: _ClassVar[int]
    POSTOFRENTISTANOME_FIELD_NUMBER: _ClassVar[int]
    NCM_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    VENDEDORID_FIELD_NUMBER: _ClassVar[int]
    VENDEDORNOME_FIELD_NUMBER: _ClassVar[int]
    COMISSAOVALOR_FIELD_NUMBER: _ClassVar[int]
    COMISSAOPERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    COMPRIMENTO_FIELD_NUMBER: _ClassVar[int]
    LARGURA_FIELD_NUMBER: _ClassVar[int]
    MEDIDA_FIELD_NUMBER: _ClassVar[int]
    PROFUNDIDADE_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    TABELAPRECO_FIELD_NUMBER: _ClassVar[int]
    VALORUNITARIO_FIELD_NUMBER: _ClassVar[int]
    DIFERENCAVALORVENDA_FIELD_NUMBER: _ClassVar[int]
    VALORUNITARIOORIGINAL_FIELD_NUMBER: _ClassVar[int]
    CUSTOUNITARIO_FIELD_NUMBER: _ClassVar[int]
    LUCROBRUTOUNITARIO_FIELD_NUMBER: _ClassVar[int]
    LUCROLIQUIDOUNITARIO_FIELD_NUMBER: _ClassVar[int]
    DESCONTOVALOR_FIELD_NUMBER: _ClassVar[int]
    DESCONTOAPLICADO_FIELD_NUMBER: _ClassVar[int]
    ACRESCIMOVALOR_FIELD_NUMBER: _ClassVar[int]
    VALORSUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    VALORTOTAL_FIELD_NUMBER: _ClassVar[int]
    VALORCOMPRA_FIELD_NUMBER: _ClassVar[int]
    DESCONTORATEADO_FIELD_NUMBER: _ClassVar[int]
    PESOUNITARIO_FIELD_NUMBER: _ClassVar[int]
    COMPOSTO_FIELD_NUMBER: _ClassVar[int]
    COMPOSTOSTRING_FIELD_NUMBER: _ClassVar[int]
    COMPOSICAO_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    REFERENCIA_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    REVIEW_DATE_FIELD_NUMBER: _ClassVar[int]
    VARIATION_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    DIASGARANTIA_FIELD_NUMBER: _ClassVar[int]
    DATAFIMGARANTIA_FIELD_NUMBER: _ClassVar[int]
    COMISSAO_MANUAL_FIELD_NUMBER: _ClassVar[int]
    TIPOGARANTIA_FIELD_NUMBER: _ClassVar[int]
    COMODATO_FIELD_NUMBER: _ClassVar[int]
    VALOR_REPOSICAO_FIELD_NUMBER: _ClassVar[int]
    STOCK_DECREASE_APPLIED_FIELD_NUMBER: _ClassVar[int]
    SKIP_STOCK_DECREASE_FIELD_NUMBER: _ClassVar[int]
    PRODUCAO_FIELD_NUMBER: _ClassVar[int]
    IMAGEMURL_FIELD_NUMBER: _ClassVar[int]
    PRECOPROMOCIONALAPLICADO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_ITEM_FIELD_NUMBER: _ClassVar[int]
    OBSERVACAO_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_COMPRA_ITEM_FIELD_NUMBER: _ClassVar[int]
    id: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    tipo: str
    nome: str
    descricao: str
    produtoId: str
    pedidoId: str
    pedidoProdutoId: str
    codigo: str
    un: str
    codigoAnp: str
    codigoAnpDescricao: str
    postoNumBico: str
    postoNumBomba: str
    postoNumTanque: str
    postoEncerranteInicial: float
    postoEncerranteFinal: float
    postoAbastecimentoIds: _containers.RepeatedScalarFieldContainer[str]
    postoFrentistaId: str
    postoFrentistaNome: str
    ncm: str
    obs: str
    vendedorId: str
    vendedorNome: str
    comissaoValor: float
    comissaoPercentual: float
    comprimento: float
    largura: float
    medida: float
    profundidade: float
    quantidade: float
    tabelaPreco: str
    valorUnitario: float
    diferencaValorVenda: float
    valorUnitarioOriginal: float
    custoUnitario: float
    lucroBrutoUnitario: float
    lucroLiquidoUnitario: float
    descontoValor: float
    descontoAplicado: DescontoAplicadosModel
    acrescimoValor: float
    valorSubtotal: float
    valorTotal: float
    ValorCompra: float
    descontoRateado: float
    pesoUnitario: float
    composto: bool
    compostoString: str
    composicao: _containers.RepeatedCompositeFieldContainer[Produto]
    color: str
    size: str
    referencia: str
    batch: BatchInfo
    review_date: _timestamp_pb2.Timestamp
    variation_product_id: str
    serial: SerialInfo
    diasGarantia: float
    dataFimGarantia: _timestamp_pb2.Timestamp
    comissao_manual: bool
    tipoGarantia: TipoGarantia
    comodato: bool
    valor_reposicao: float
    stock_decrease_applied: bool
    skip_stock_decrease: bool
    producao: ItemProducao
    imagemUrl: str
    precoPromocionalAplicado: bool
    numero_item: int
    observacao: str
    pedido_compra_item: int
    def __init__(self, id: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., tipo: _Optional[str] = ..., nome: _Optional[str] = ..., descricao: _Optional[str] = ..., produtoId: _Optional[str] = ..., pedidoId: _Optional[str] = ..., pedidoProdutoId: _Optional[str] = ..., codigo: _Optional[str] = ..., un: _Optional[str] = ..., codigoAnp: _Optional[str] = ..., codigoAnpDescricao: _Optional[str] = ..., postoNumBico: _Optional[str] = ..., postoNumBomba: _Optional[str] = ..., postoNumTanque: _Optional[str] = ..., postoEncerranteInicial: _Optional[float] = ..., postoEncerranteFinal: _Optional[float] = ..., postoAbastecimentoIds: _Optional[_Iterable[str]] = ..., postoFrentistaId: _Optional[str] = ..., postoFrentistaNome: _Optional[str] = ..., ncm: _Optional[str] = ..., obs: _Optional[str] = ..., vendedorId: _Optional[str] = ..., vendedorNome: _Optional[str] = ..., comissaoValor: _Optional[float] = ..., comissaoPercentual: _Optional[float] = ..., comprimento: _Optional[float] = ..., largura: _Optional[float] = ..., medida: _Optional[float] = ..., profundidade: _Optional[float] = ..., quantidade: _Optional[float] = ..., tabelaPreco: _Optional[str] = ..., valorUnitario: _Optional[float] = ..., diferencaValorVenda: _Optional[float] = ..., valorUnitarioOriginal: _Optional[float] = ..., custoUnitario: _Optional[float] = ..., lucroBrutoUnitario: _Optional[float] = ..., lucroLiquidoUnitario: _Optional[float] = ..., descontoValor: _Optional[float] = ..., descontoAplicado: _Optional[_Union[DescontoAplicadosModel, _Mapping]] = ..., acrescimoValor: _Optional[float] = ..., valorSubtotal: _Optional[float] = ..., valorTotal: _Optional[float] = ..., ValorCompra: _Optional[float] = ..., descontoRateado: _Optional[float] = ..., pesoUnitario: _Optional[float] = ..., composto: _Optional[bool] = ..., compostoString: _Optional[str] = ..., composicao: _Optional[_Iterable[_Union[Produto, _Mapping]]] = ..., color: _Optional[str] = ..., size: _Optional[str] = ..., referencia: _Optional[str] = ..., batch: _Optional[_Union[BatchInfo, _Mapping]] = ..., review_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., variation_product_id: _Optional[str] = ..., serial: _Optional[_Union[SerialInfo, _Mapping]] = ..., diasGarantia: _Optional[float] = ..., dataFimGarantia: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., comissao_manual: _Optional[bool] = ..., tipoGarantia: _Optional[_Union[TipoGarantia, str]] = ..., comodato: _Optional[bool] = ..., valor_reposicao: _Optional[float] = ..., stock_decrease_applied: _Optional[bool] = ..., skip_stock_decrease: _Optional[bool] = ..., producao: _Optional[_Union[ItemProducao, _Mapping]] = ..., imagemUrl: _Optional[str] = ..., precoPromocionalAplicado: _Optional[bool] = ..., numero_item: _Optional[int] = ..., observacao: _Optional[str] = ..., pedido_compra_item: _Optional[int] = ...) -> None: ...

class ItemProducao(_message.Message):
    __slots__ = ("enviado", "dataHoraEnvio", "impressoraId", "impressoraNome", "impresso", "dataHoraImpressao", "erroImpressao", "entregue", "dataHoraEntrega")
    ENVIADO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAENVIO_FIELD_NUMBER: _ClassVar[int]
    IMPRESSORAID_FIELD_NUMBER: _ClassVar[int]
    IMPRESSORANOME_FIELD_NUMBER: _ClassVar[int]
    IMPRESSO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAIMPRESSAO_FIELD_NUMBER: _ClassVar[int]
    ERROIMPRESSAO_FIELD_NUMBER: _ClassVar[int]
    ENTREGUE_FIELD_NUMBER: _ClassVar[int]
    DATAHORAENTREGA_FIELD_NUMBER: _ClassVar[int]
    enviado: bool
    dataHoraEnvio: _timestamp_pb2.Timestamp
    impressoraId: str
    impressoraNome: str
    impresso: bool
    dataHoraImpressao: _timestamp_pb2.Timestamp
    erroImpressao: str
    entregue: bool
    dataHoraEntrega: _timestamp_pb2.Timestamp
    def __init__(self, enviado: _Optional[bool] = ..., dataHoraEnvio: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., impressoraId: _Optional[str] = ..., impressoraNome: _Optional[str] = ..., impresso: _Optional[bool] = ..., dataHoraImpressao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., erroImpressao: _Optional[str] = ..., entregue: _Optional[bool] = ..., dataHoraEntrega: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Servico(_message.Message):
    __slots__ = ("id", "createdAt", "updatedAt", "userId", "userName", "pedidoId", "servicoId", "servicoNome", "codigo", "un", "obs", "tecnicoId", "tecnicoNome", "comissaoValor", "comissaoPercentual", "repasseValor", "quantidade", "valorUnitario", "custo", "lucroBruto", "lucroLiquido", "descontoValor", "descontoAplicado", "descontoRateado", "acrescimoValor", "subtotal", "total", "compostoId", "is_recurring", "composto", "composicao", "diasGarantia", "dataFimGarantia", "comissao_manual", "categoria", "hora_inicio", "hora_fim", "numero_item", "observacao")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    SERVICOID_FIELD_NUMBER: _ClassVar[int]
    SERVICONOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    TECNICOID_FIELD_NUMBER: _ClassVar[int]
    TECNICONOME_FIELD_NUMBER: _ClassVar[int]
    COMISSAOVALOR_FIELD_NUMBER: _ClassVar[int]
    COMISSAOPERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    REPASSEVALOR_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    VALORUNITARIO_FIELD_NUMBER: _ClassVar[int]
    CUSTO_FIELD_NUMBER: _ClassVar[int]
    LUCROBRUTO_FIELD_NUMBER: _ClassVar[int]
    LUCROLIQUIDO_FIELD_NUMBER: _ClassVar[int]
    DESCONTOVALOR_FIELD_NUMBER: _ClassVar[int]
    DESCONTOAPLICADO_FIELD_NUMBER: _ClassVar[int]
    DESCONTORATEADO_FIELD_NUMBER: _ClassVar[int]
    ACRESCIMOVALOR_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    COMPOSTOID_FIELD_NUMBER: _ClassVar[int]
    IS_RECURRING_FIELD_NUMBER: _ClassVar[int]
    COMPOSTO_FIELD_NUMBER: _ClassVar[int]
    COMPOSICAO_FIELD_NUMBER: _ClassVar[int]
    DIASGARANTIA_FIELD_NUMBER: _ClassVar[int]
    DATAFIMGARANTIA_FIELD_NUMBER: _ClassVar[int]
    COMISSAO_MANUAL_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    HORA_INICIO_FIELD_NUMBER: _ClassVar[int]
    HORA_FIM_FIELD_NUMBER: _ClassVar[int]
    NUMERO_ITEM_FIELD_NUMBER: _ClassVar[int]
    OBSERVACAO_FIELD_NUMBER: _ClassVar[int]
    id: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    pedidoId: str
    servicoId: str
    servicoNome: str
    codigo: str
    un: str
    obs: str
    tecnicoId: str
    tecnicoNome: str
    comissaoValor: float
    comissaoPercentual: float
    repasseValor: float
    quantidade: float
    valorUnitario: float
    custo: float
    lucroBruto: float
    lucroLiquido: float
    descontoValor: float
    descontoAplicado: DescontoAplicadosModel
    descontoRateado: float
    acrescimoValor: float
    subtotal: float
    total: float
    compostoId: str
    is_recurring: bool
    composto: bool
    composicao: _containers.RepeatedCompositeFieldContainer[ComposicaoServico]
    diasGarantia: float
    dataFimGarantia: _timestamp_pb2.Timestamp
    comissao_manual: bool
    categoria: ServicoCategoria
    hora_inicio: _timestamp_pb2.Timestamp
    hora_fim: _timestamp_pb2.Timestamp
    numero_item: int
    observacao: str
    def __init__(self, id: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., pedidoId: _Optional[str] = ..., servicoId: _Optional[str] = ..., servicoNome: _Optional[str] = ..., codigo: _Optional[str] = ..., un: _Optional[str] = ..., obs: _Optional[str] = ..., tecnicoId: _Optional[str] = ..., tecnicoNome: _Optional[str] = ..., comissaoValor: _Optional[float] = ..., comissaoPercentual: _Optional[float] = ..., repasseValor: _Optional[float] = ..., quantidade: _Optional[float] = ..., valorUnitario: _Optional[float] = ..., custo: _Optional[float] = ..., lucroBruto: _Optional[float] = ..., lucroLiquido: _Optional[float] = ..., descontoValor: _Optional[float] = ..., descontoAplicado: _Optional[_Union[DescontoAplicadosModel, _Mapping]] = ..., descontoRateado: _Optional[float] = ..., acrescimoValor: _Optional[float] = ..., subtotal: _Optional[float] = ..., total: _Optional[float] = ..., compostoId: _Optional[str] = ..., is_recurring: _Optional[bool] = ..., composto: _Optional[bool] = ..., composicao: _Optional[_Iterable[_Union[ComposicaoServico, _Mapping]]] = ..., diasGarantia: _Optional[float] = ..., dataFimGarantia: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., comissao_manual: _Optional[bool] = ..., categoria: _Optional[_Union[ServicoCategoria, str]] = ..., hora_inicio: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., hora_fim: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., numero_item: _Optional[int] = ..., observacao: _Optional[str] = ...) -> None: ...

class ComposicaoServico(_message.Message):
    __slots__ = ("id", "item_id", "tipo", "nome", "quantidade", "un", "valor_unitario", "total", "codigo")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    id: str
    item_id: str
    tipo: str
    nome: str
    quantidade: float
    un: str
    valor_unitario: float
    total: float
    codigo: str
    def __init__(self, id: _Optional[str] = ..., item_id: _Optional[str] = ..., tipo: _Optional[str] = ..., nome: _Optional[str] = ..., quantidade: _Optional[float] = ..., un: _Optional[str] = ..., valor_unitario: _Optional[float] = ..., total: _Optional[float] = ..., codigo: _Optional[str] = ...) -> None: ...

class Pagamento(_message.Message):
    __slots__ = ("id", "createdAt", "updatedAt", "userId", "userName", "situacao", "userUpdateId", "userUpdateNome", "formaPagamentoId", "formaPagamentoNome", "pagamentoOnlineId", "tipoPagamento", "usarCarteiraCashback", "avista", "valorPago", "valorLiquido", "cartaCreditoId", "cartaoComprovante", "cartaoCodigoAutorizacao", "cartaoRedeAdquirente", "cartaoRedeAdquirenteCnpj", "cartaoNomeCartaoAdministradora", "moedaTipoRecebimento", "moedaCotacao", "valorTipoMoeda", "adquirenteValorReceber", "adquirenteTaxaValor", "adquirenteTaxaPercentual", "adquirenteTaxaFixaValor", "caixaNome", "caixaId", "numeroParcelas", "parcelas", "dataHoraCancelamento", "motivoCancelamento", "transactionNumber", "transactionId", "origin")
    class paymentOrigin(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PAYMENT_ORIGIN_UNSPECIFIED: _ClassVar[Pagamento.paymentOrigin]
        PAYMENT_ORIGIN_ONLINE: _ClassVar[Pagamento.paymentOrigin]
        PAYMENT_ORIGIN_OFFLINE: _ClassVar[Pagamento.paymentOrigin]
    PAYMENT_ORIGIN_UNSPECIFIED: Pagamento.paymentOrigin
    PAYMENT_ORIGIN_ONLINE: Pagamento.paymentOrigin
    PAYMENT_ORIGIN_OFFLINE: Pagamento.paymentOrigin
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    USERUPDATEID_FIELD_NUMBER: _ClassVar[int]
    USERUPDATENOME_FIELD_NUMBER: _ClassVar[int]
    FORMAPAGAMENTOID_FIELD_NUMBER: _ClassVar[int]
    FORMAPAGAMENTONOME_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTOONLINEID_FIELD_NUMBER: _ClassVar[int]
    TIPOPAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    USARCARTEIRACASHBACK_FIELD_NUMBER: _ClassVar[int]
    AVISTA_FIELD_NUMBER: _ClassVar[int]
    VALORPAGO_FIELD_NUMBER: _ClassVar[int]
    VALORLIQUIDO_FIELD_NUMBER: _ClassVar[int]
    CARTACREDITOID_FIELD_NUMBER: _ClassVar[int]
    CARTAOCOMPROVANTE_FIELD_NUMBER: _ClassVar[int]
    CARTAOCODIGOAUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    CARTAOREDEADQUIRENTE_FIELD_NUMBER: _ClassVar[int]
    CARTAOREDEADQUIRENTECNPJ_FIELD_NUMBER: _ClassVar[int]
    CARTAONOMECARTAOADMINISTRADORA_FIELD_NUMBER: _ClassVar[int]
    MOEDATIPORECEBIMENTO_FIELD_NUMBER: _ClassVar[int]
    MOEDACOTACAO_FIELD_NUMBER: _ClassVar[int]
    VALORTIPOMOEDA_FIELD_NUMBER: _ClassVar[int]
    ADQUIRENTEVALORRECEBER_FIELD_NUMBER: _ClassVar[int]
    ADQUIRENTETAXAVALOR_FIELD_NUMBER: _ClassVar[int]
    ADQUIRENTETAXAPERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    ADQUIRENTETAXAFIXAVALOR_FIELD_NUMBER: _ClassVar[int]
    CAIXANOME_FIELD_NUMBER: _ClassVar[int]
    CAIXAID_FIELD_NUMBER: _ClassVar[int]
    NUMEROPARCELAS_FIELD_NUMBER: _ClassVar[int]
    PARCELAS_FIELD_NUMBER: _ClassVar[int]
    DATAHORACANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    MOTIVOCANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONNUMBER_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
    ORIGIN_FIELD_NUMBER: _ClassVar[int]
    id: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    situacao: str
    userUpdateId: str
    userUpdateNome: str
    formaPagamentoId: str
    formaPagamentoNome: str
    pagamentoOnlineId: str
    tipoPagamento: str
    usarCarteiraCashback: bool
    avista: bool
    valorPago: float
    valorLiquido: float
    cartaCreditoId: str
    cartaoComprovante: str
    cartaoCodigoAutorizacao: str
    cartaoRedeAdquirente: str
    cartaoRedeAdquirenteCnpj: str
    cartaoNomeCartaoAdministradora: str
    moedaTipoRecebimento: str
    moedaCotacao: float
    valorTipoMoeda: float
    adquirenteValorReceber: float
    adquirenteTaxaValor: float
    adquirenteTaxaPercentual: float
    adquirenteTaxaFixaValor: float
    caixaNome: str
    caixaId: str
    numeroParcelas: int
    parcelas: _containers.RepeatedCompositeFieldContainer[Parcelas]
    dataHoraCancelamento: _timestamp_pb2.Timestamp
    motivoCancelamento: str
    transactionNumber: str
    transactionId: str
    origin: Pagamento.paymentOrigin
    def __init__(self, id: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., situacao: _Optional[str] = ..., userUpdateId: _Optional[str] = ..., userUpdateNome: _Optional[str] = ..., formaPagamentoId: _Optional[str] = ..., formaPagamentoNome: _Optional[str] = ..., pagamentoOnlineId: _Optional[str] = ..., tipoPagamento: _Optional[str] = ..., usarCarteiraCashback: _Optional[bool] = ..., avista: _Optional[bool] = ..., valorPago: _Optional[float] = ..., valorLiquido: _Optional[float] = ..., cartaCreditoId: _Optional[str] = ..., cartaoComprovante: _Optional[str] = ..., cartaoCodigoAutorizacao: _Optional[str] = ..., cartaoRedeAdquirente: _Optional[str] = ..., cartaoRedeAdquirenteCnpj: _Optional[str] = ..., cartaoNomeCartaoAdministradora: _Optional[str] = ..., moedaTipoRecebimento: _Optional[str] = ..., moedaCotacao: _Optional[float] = ..., valorTipoMoeda: _Optional[float] = ..., adquirenteValorReceber: _Optional[float] = ..., adquirenteTaxaValor: _Optional[float] = ..., adquirenteTaxaPercentual: _Optional[float] = ..., adquirenteTaxaFixaValor: _Optional[float] = ..., caixaNome: _Optional[str] = ..., caixaId: _Optional[str] = ..., numeroParcelas: _Optional[int] = ..., parcelas: _Optional[_Iterable[_Union[Parcelas, _Mapping]]] = ..., dataHoraCancelamento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., motivoCancelamento: _Optional[str] = ..., transactionNumber: _Optional[str] = ..., transactionId: _Optional[str] = ..., origin: _Optional[_Union[Pagamento.paymentOrigin, str]] = ...) -> None: ...

class Parcelas(_message.Message):
    __slots__ = ("id", "parcela", "valor", "valorTipoMoeda", "taxaAdm", "taxaAdmValor", "taxaValorFixo", "taxaAntecipacao", "taxaAntecipacaoValor", "adquirenteValorReceber", "vencimento", "pedidoPagamento")
    ID_FIELD_NUMBER: _ClassVar[int]
    PARCELA_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    VALORTIPOMOEDA_FIELD_NUMBER: _ClassVar[int]
    TAXAADM_FIELD_NUMBER: _ClassVar[int]
    TAXAADMVALOR_FIELD_NUMBER: _ClassVar[int]
    TAXAVALORFIXO_FIELD_NUMBER: _ClassVar[int]
    TAXAANTECIPACAO_FIELD_NUMBER: _ClassVar[int]
    TAXAANTECIPACAOVALOR_FIELD_NUMBER: _ClassVar[int]
    ADQUIRENTEVALORRECEBER_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    PEDIDOPAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    parcela: str
    valor: float
    valorTipoMoeda: float
    taxaAdm: float
    taxaAdmValor: float
    taxaValorFixo: float
    taxaAntecipacao: float
    taxaAntecipacaoValor: float
    adquirenteValorReceber: float
    vencimento: _timestamp_pb2.Timestamp
    pedidoPagamento: Pagamento
    def __init__(self, id: _Optional[str] = ..., parcela: _Optional[str] = ..., valor: _Optional[float] = ..., valorTipoMoeda: _Optional[float] = ..., taxaAdm: _Optional[float] = ..., taxaAdmValor: _Optional[float] = ..., taxaValorFixo: _Optional[float] = ..., taxaAntecipacao: _Optional[float] = ..., taxaAntecipacaoValor: _Optional[float] = ..., adquirenteValorReceber: _Optional[float] = ..., vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., pedidoPagamento: _Optional[_Union[Pagamento, _Mapping]] = ...) -> None: ...

class Pessoa(_message.Message):
    __slots__ = ("id", "revenda", "cpfCnpj", "ie", "nome", "nome2", "usuarioId", "usuarioNome", "comissao", "endId", "endNome", "endCep", "endEndereco", "endNumero", "endBairro", "endCidade", "endCidadeCodigo", "endUf", "endComplemento", "telefone", "email", "dataNascimento", "genero", "desconto_maximo")
    ID_FIELD_NUMBER: _ClassVar[int]
    REVENDA_FIELD_NUMBER: _ClassVar[int]
    CPFCNPJ_FIELD_NUMBER: _ClassVar[int]
    IE_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    NOME2_FIELD_NUMBER: _ClassVar[int]
    USUARIOID_FIELD_NUMBER: _ClassVar[int]
    USUARIONOME_FIELD_NUMBER: _ClassVar[int]
    COMISSAO_FIELD_NUMBER: _ClassVar[int]
    ENDID_FIELD_NUMBER: _ClassVar[int]
    ENDNOME_FIELD_NUMBER: _ClassVar[int]
    ENDCEP_FIELD_NUMBER: _ClassVar[int]
    ENDENDERECO_FIELD_NUMBER: _ClassVar[int]
    ENDNUMERO_FIELD_NUMBER: _ClassVar[int]
    ENDBAIRRO_FIELD_NUMBER: _ClassVar[int]
    ENDCIDADE_FIELD_NUMBER: _ClassVar[int]
    ENDCIDADECODIGO_FIELD_NUMBER: _ClassVar[int]
    ENDUF_FIELD_NUMBER: _ClassVar[int]
    ENDCOMPLEMENTO_FIELD_NUMBER: _ClassVar[int]
    TELEFONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DATANASCIMENTO_FIELD_NUMBER: _ClassVar[int]
    GENERO_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_MAXIMO_FIELD_NUMBER: _ClassVar[int]
    id: str
    revenda: bool
    cpfCnpj: str
    ie: str
    nome: str
    nome2: str
    usuarioId: str
    usuarioNome: str
    comissao: float
    endId: str
    endNome: str
    endCep: str
    endEndereco: str
    endNumero: str
    endBairro: str
    endCidade: str
    endCidadeCodigo: str
    endUf: str
    endComplemento: str
    telefone: str
    email: str
    dataNascimento: str
    genero: str
    desconto_maximo: float
    def __init__(self, id: _Optional[str] = ..., revenda: _Optional[bool] = ..., cpfCnpj: _Optional[str] = ..., ie: _Optional[str] = ..., nome: _Optional[str] = ..., nome2: _Optional[str] = ..., usuarioId: _Optional[str] = ..., usuarioNome: _Optional[str] = ..., comissao: _Optional[float] = ..., endId: _Optional[str] = ..., endNome: _Optional[str] = ..., endCep: _Optional[str] = ..., endEndereco: _Optional[str] = ..., endNumero: _Optional[str] = ..., endBairro: _Optional[str] = ..., endCidade: _Optional[str] = ..., endCidadeCodigo: _Optional[str] = ..., endUf: _Optional[str] = ..., endComplemento: _Optional[str] = ..., telefone: _Optional[str] = ..., email: _Optional[str] = ..., dataNascimento: _Optional[str] = ..., genero: _Optional[str] = ..., desconto_maximo: _Optional[float] = ...) -> None: ...

class Dfe(_message.Message):
    __slots__ = ("nfe", "nfce", "nfse")
    NFE_FIELD_NUMBER: _ClassVar[int]
    NFCE_FIELD_NUMBER: _ClassVar[int]
    NFSE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    nfce: Nfce
    nfse: Nfse
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ..., nfce: _Optional[_Union[Nfce, _Mapping]] = ..., nfse: _Optional[_Union[Nfse, _Mapping]] = ...) -> None: ...

class Nfe(_message.Message):
    __slots__ = ("id", "tipo", "situacao", "chave", "url_danfe", "serie", "numero", "forma_emissao", "dataHoraEmissao")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    URL_DANFE_FIELD_NUMBER: _ClassVar[int]
    SERIE_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    FORMA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAEMISSAO_FIELD_NUMBER: _ClassVar[int]
    id: str
    tipo: str
    situacao: str
    chave: str
    url_danfe: str
    serie: int
    numero: int
    forma_emissao: str
    dataHoraEmissao: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., tipo: _Optional[str] = ..., situacao: _Optional[str] = ..., chave: _Optional[str] = ..., url_danfe: _Optional[str] = ..., serie: _Optional[int] = ..., numero: _Optional[int] = ..., forma_emissao: _Optional[str] = ..., dataHoraEmissao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Nfce(_message.Message):
    __slots__ = ("nfce_numero", "nfce_url_danfe", "nfce_url_xml", "nfce_serie", "nfce_chave", "nfce_id", "nfce_situacao", "nfce_forma_emissao")
    NFCE_NUMERO_FIELD_NUMBER: _ClassVar[int]
    NFCE_URL_DANFE_FIELD_NUMBER: _ClassVar[int]
    NFCE_URL_XML_FIELD_NUMBER: _ClassVar[int]
    NFCE_SERIE_FIELD_NUMBER: _ClassVar[int]
    NFCE_CHAVE_FIELD_NUMBER: _ClassVar[int]
    NFCE_ID_FIELD_NUMBER: _ClassVar[int]
    NFCE_SITUACAO_FIELD_NUMBER: _ClassVar[int]
    NFCE_FORMA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    nfce_numero: int
    nfce_url_danfe: str
    nfce_url_xml: str
    nfce_serie: int
    nfce_chave: str
    nfce_id: str
    nfce_situacao: str
    nfce_forma_emissao: str
    def __init__(self, nfce_numero: _Optional[int] = ..., nfce_url_danfe: _Optional[str] = ..., nfce_url_xml: _Optional[str] = ..., nfce_serie: _Optional[int] = ..., nfce_chave: _Optional[str] = ..., nfce_id: _Optional[str] = ..., nfce_situacao: _Optional[str] = ..., nfce_forma_emissao: _Optional[str] = ...) -> None: ...

class Nfse(_message.Message):
    __slots__ = ("id", "situacao", "numero", "chave", "codigo_verificacao", "url_danfse", "nfse_auto_emite")
    ID_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    CODIGO_VERIFICACAO_FIELD_NUMBER: _ClassVar[int]
    URL_DANFSE_FIELD_NUMBER: _ClassVar[int]
    NFSE_AUTO_EMITE_FIELD_NUMBER: _ClassVar[int]
    id: str
    situacao: str
    numero: str
    chave: str
    codigo_verificacao: str
    url_danfse: str
    nfse_auto_emite: bool
    def __init__(self, id: _Optional[str] = ..., situacao: _Optional[str] = ..., numero: _Optional[str] = ..., chave: _Optional[str] = ..., codigo_verificacao: _Optional[str] = ..., url_danfse: _Optional[str] = ..., nfse_auto_emite: _Optional[bool] = ...) -> None: ...

class LicenciamentoModel(_message.Message):
    __slots__ = ("tipoContrato", "numeroSerie", "codigoAutorizacao", "motivoBloqueio", "ultimoAcesso")
    class UltimoAcesso(_message.Message):
        __slots__ = ("lastDate", "userName")
        LASTDATE_FIELD_NUMBER: _ClassVar[int]
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        lastDate: _timestamp_pb2.Timestamp
        userName: str
        def __init__(self, lastDate: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userName: _Optional[str] = ...) -> None: ...
    TIPOCONTRATO_FIELD_NUMBER: _ClassVar[int]
    NUMEROSERIE_FIELD_NUMBER: _ClassVar[int]
    CODIGOAUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    MOTIVOBLOQUEIO_FIELD_NUMBER: _ClassVar[int]
    ULTIMOACESSO_FIELD_NUMBER: _ClassVar[int]
    tipoContrato: str
    numeroSerie: str
    codigoAutorizacao: str
    motivoBloqueio: str
    ultimoAcesso: LicenciamentoModel.UltimoAcesso
    def __init__(self, tipoContrato: _Optional[str] = ..., numeroSerie: _Optional[str] = ..., codigoAutorizacao: _Optional[str] = ..., motivoBloqueio: _Optional[str] = ..., ultimoAcesso: _Optional[_Union[LicenciamentoModel.UltimoAcesso, _Mapping]] = ...) -> None: ...

class PedidoVinculado(_message.Message):
    __slots__ = ("id", "pedidoId", "numero", "total", "tipo", "clienteNome", "clienteCpfCnpj", "origemNumero", "data")
    ID_FIELD_NUMBER: _ClassVar[int]
    PEDIDOID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    CLIENTENOME_FIELD_NUMBER: _ClassVar[int]
    CLIENTECPFCNPJ_FIELD_NUMBER: _ClassVar[int]
    ORIGEMNUMERO_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    id: str
    pedidoId: str
    numero: int
    total: float
    tipo: str
    clienteNome: str
    clienteCpfCnpj: str
    origemNumero: str
    data: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[str] = ..., pedidoId: _Optional[str] = ..., numero: _Optional[int] = ..., total: _Optional[float] = ..., tipo: _Optional[str] = ..., clienteNome: _Optional[str] = ..., clienteCpfCnpj: _Optional[str] = ..., origemNumero: _Optional[str] = ..., data: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DescontoAplicadosModel(_message.Message):
    __slots__ = ("id", "createdAt", "updatedAt", "userId", "userName", "descontoId", "descontoNome", "valor", "itens")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DESCONTOID_FIELD_NUMBER: _ClassVar[int]
    DESCONTONOME_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    ITENS_FIELD_NUMBER: _ClassVar[int]
    id: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    descontoId: str
    descontoNome: str
    valor: float
    itens: _containers.RepeatedCompositeFieldContainer[DescontoItemAplicado]
    def __init__(self, id: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., descontoId: _Optional[str] = ..., descontoNome: _Optional[str] = ..., valor: _Optional[float] = ..., itens: _Optional[_Iterable[_Union[DescontoItemAplicado, _Mapping]]] = ...) -> None: ...

class CupomAplicadoModel(_message.Message):
    __slots__ = ("cupomId", "codigo", "valor", "cumulativo", "aplicadoEm", "itens")
    CUPOMID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVO_FIELD_NUMBER: _ClassVar[int]
    APLICADOEM_FIELD_NUMBER: _ClassVar[int]
    ITENS_FIELD_NUMBER: _ClassVar[int]
    cupomId: str
    codigo: str
    valor: float
    cumulativo: bool
    aplicadoEm: _timestamp_pb2.Timestamp
    itens: _containers.RepeatedCompositeFieldContainer[DescontoItemAplicado]
    def __init__(self, cupomId: _Optional[str] = ..., codigo: _Optional[str] = ..., valor: _Optional[float] = ..., cumulativo: _Optional[bool] = ..., aplicadoEm: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., itens: _Optional[_Iterable[_Union[DescontoItemAplicado, _Mapping]]] = ...) -> None: ...

class DescontoItemAplicado(_message.Message):
    __slots__ = ("itemId", "servico", "valor")
    ITEMID_FIELD_NUMBER: _ClassVar[int]
    SERVICO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    itemId: str
    servico: bool
    valor: float
    def __init__(self, itemId: _Optional[str] = ..., servico: _Optional[bool] = ..., valor: _Optional[float] = ...) -> None: ...

class CashbackAplicadosModel(_message.Message):
    __slots__ = ("id", "createdAt", "updatedAt", "userId", "userName", "cashbackId", "cashbackNome", "valor")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    CASHBACKID_FIELD_NUMBER: _ClassVar[int]
    CASHBACKNOME_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    id: str
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    cashbackId: str
    cashbackNome: str
    valor: float
    def __init__(self, id: _Optional[str] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., cashbackId: _Optional[str] = ..., cashbackNome: _Optional[str] = ..., valor: _Optional[float] = ...) -> None: ...

class Partnership(_message.Message):
    __slots__ = ("partnership_id", "partnership_name", "titular_id", "titular_name", "dependent_id", "dependent_name")
    PARTNERSHIP_ID_FIELD_NUMBER: _ClassVar[int]
    PARTNERSHIP_NAME_FIELD_NUMBER: _ClassVar[int]
    TITULAR_ID_FIELD_NUMBER: _ClassVar[int]
    TITULAR_NAME_FIELD_NUMBER: _ClassVar[int]
    DEPENDENT_ID_FIELD_NUMBER: _ClassVar[int]
    DEPENDENT_NAME_FIELD_NUMBER: _ClassVar[int]
    partnership_id: str
    partnership_name: str
    titular_id: str
    titular_name: str
    dependent_id: str
    dependent_name: str
    def __init__(self, partnership_id: _Optional[str] = ..., partnership_name: _Optional[str] = ..., titular_id: _Optional[str] = ..., titular_name: _Optional[str] = ..., dependent_id: _Optional[str] = ..., dependent_name: _Optional[str] = ...) -> None: ...

class ConfirmationOrderReceipt(_message.Message):
    __slots__ = ("date_time", "user_id", "user_name", "url")
    DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    date_time: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    url: str
    def __init__(self, date_time: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class CuponsSorteio(_message.Message):
    __slots__ = ("id", "cupomId")
    ID_FIELD_NUMBER: _ClassVar[int]
    CUPOMID_FIELD_NUMBER: _ClassVar[int]
    id: str
    cupomId: str
    def __init__(self, id: _Optional[str] = ..., cupomId: _Optional[str] = ...) -> None: ...

class DfeDanfeRequest(_message.Message):
    __slots__ = ("id", "tipo", "format")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    id: str
    tipo: str
    format: DanfeFormat
    def __init__(self, id: _Optional[str] = ..., tipo: _Optional[str] = ..., format: _Optional[_Union[DanfeFormat, str]] = ...) -> None: ...

class DfeDanfeResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class ImportRequest(_message.Message):
    __slots__ = ("data", "file_name", "orders", "validate_only", "import_pedido", "update_if_exists", "import_cliente", "import_vendedor", "import_produto", "import_servico", "import_formas_pagamento", "import_conta", "mapping_id", "overwrite_existing_fields")
    DATA_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    IMPORT_PEDIDO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    IMPORT_CLIENTE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_VENDEDOR_FIELD_NUMBER: _ClassVar[int]
    IMPORT_PRODUTO_FIELD_NUMBER: _ClassVar[int]
    IMPORT_SERVICO_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FORMAS_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    IMPORT_CONTA_FIELD_NUMBER: _ClassVar[int]
    MAPPING_ID_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_EXISTING_FIELDS_FIELD_NUMBER: _ClassVar[int]
    data: str
    file_name: str
    orders: _containers.RepeatedCompositeFieldContainer[Pedido]
    validate_only: bool
    import_pedido: bool
    update_if_exists: bool
    import_cliente: bool
    import_vendedor: bool
    import_produto: bool
    import_servico: bool
    import_formas_pagamento: bool
    import_conta: bool
    mapping_id: str
    overwrite_existing_fields: bool
    def __init__(self, data: _Optional[str] = ..., file_name: _Optional[str] = ..., orders: _Optional[_Iterable[_Union[Pedido, _Mapping]]] = ..., validate_only: _Optional[bool] = ..., import_pedido: _Optional[bool] = ..., update_if_exists: _Optional[bool] = ..., import_cliente: _Optional[bool] = ..., import_vendedor: _Optional[bool] = ..., import_produto: _Optional[bool] = ..., import_servico: _Optional[bool] = ..., import_formas_pagamento: _Optional[bool] = ..., import_conta: _Optional[bool] = ..., mapping_id: _Optional[str] = ..., overwrite_existing_fields: _Optional[bool] = ...) -> None: ...

class ImportResponse(_message.Message):
    __slots__ = ("report",)
    REPORT_FIELD_NUMBER: _ClassVar[int]
    report: _imports_pb2.ImportResponse
    def __init__(self, report: _Optional[_Union[_imports_pb2.ImportResponse, _Mapping]] = ...) -> None: ...

class SendPaymentLinkRequest(_message.Message):
    __slots__ = ("ids", "pedidos", "email", "channel", "email_integration_id", "billing_plan_id", "billing_plan_name", "whatsapp_integration_id", "whatsapp_template_name", "whatsapp_template_language", "message_template_id")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PEDIDOS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    BILLING_PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_TEMPLATE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    pedidos: _containers.RepeatedCompositeFieldContainer[Pedido]
    email: str
    channel: str
    email_integration_id: str
    billing_plan_id: str
    billing_plan_name: str
    whatsapp_integration_id: str
    whatsapp_template_name: str
    whatsapp_template_language: str
    message_template_id: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., pedidos: _Optional[_Iterable[_Union[Pedido, _Mapping]]] = ..., email: _Optional[str] = ..., channel: _Optional[str] = ..., email_integration_id: _Optional[str] = ..., billing_plan_id: _Optional[str] = ..., billing_plan_name: _Optional[str] = ..., whatsapp_integration_id: _Optional[str] = ..., whatsapp_template_name: _Optional[str] = ..., whatsapp_template_language: _Optional[str] = ..., message_template_id: _Optional[str] = ...) -> None: ...

class SendPaymentLinkResponse(_message.Message):
    __slots__ = ("pedidos", "whatsapp_web")
    PEDIDOS_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_WEB_FIELD_NUMBER: _ClassVar[int]
    pedidos: _containers.RepeatedCompositeFieldContainer[Pedido]
    whatsapp_web: _containers.RepeatedCompositeFieldContainer[WhatsappWebEnvio]
    def __init__(self, pedidos: _Optional[_Iterable[_Union[Pedido, _Mapping]]] = ..., whatsapp_web: _Optional[_Iterable[_Union[WhatsappWebEnvio, _Mapping]]] = ...) -> None: ...

class WhatsappWebEnvio(_message.Message):
    __slots__ = ("numero", "mensagem")
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    numero: str
    mensagem: str
    def __init__(self, numero: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class MesclaPedidosRequest(_message.Message):
    __slots__ = ("tipo", "ids", "pessoaId", "vendedorId")
    TIPO_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    PESSOAID_FIELD_NUMBER: _ClassVar[int]
    VENDEDORID_FIELD_NUMBER: _ClassVar[int]
    tipo: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    pessoaId: str
    vendedorId: str
    def __init__(self, tipo: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ..., pessoaId: _Optional[str] = ..., vendedorId: _Optional[str] = ...) -> None: ...

class MesclaPedidosResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class AddPedidoVinculadoRequest(_message.Message):
    __slots__ = ("id", "pedido_vinculado")
    ID_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_VINCULADO_FIELD_NUMBER: _ClassVar[int]
    id: str
    pedido_vinculado: PedidoVinculado
    def __init__(self, id: _Optional[str] = ..., pedido_vinculado: _Optional[_Union[PedidoVinculado, _Mapping]] = ...) -> None: ...

class AddPedidoVinculadoResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class DeletePedidoVinculadoRequest(_message.Message):
    __slots__ = ("id", "pedidoVinculadoId")
    ID_FIELD_NUMBER: _ClassVar[int]
    PEDIDOVINCULADOID_FIELD_NUMBER: _ClassVar[int]
    id: str
    pedidoVinculadoId: str
    def __init__(self, id: _Optional[str] = ..., pedidoVinculadoId: _Optional[str] = ...) -> None: ...

class DeletePedidoVinculadoResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class EnviaNFeRequest(_message.Message):
    __slots__ = ("ids", "tipo", "pessoaId", "apenas_gerar")
    IDS_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    PESSOAID_FIELD_NUMBER: _ClassVar[int]
    APENAS_GERAR_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    tipo: str
    pessoaId: str
    apenas_gerar: bool
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., tipo: _Optional[str] = ..., pessoaId: _Optional[str] = ..., apenas_gerar: _Optional[bool] = ...) -> None: ...

class EnviaNFeResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class SincronizaNFeRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SincronizaNFeResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class SincronizaPessoaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class SincronizaPessoaResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class VinculoNfManualRequest(_message.Message):
    __slots__ = ("id", "nfeId", "nfeTipo")
    ID_FIELD_NUMBER: _ClassVar[int]
    NFEID_FIELD_NUMBER: _ClassVar[int]
    NFETIPO_FIELD_NUMBER: _ClassVar[int]
    id: str
    nfeId: str
    nfeTipo: str
    def __init__(self, id: _Optional[str] = ..., nfeId: _Optional[str] = ..., nfeTipo: _Optional[str] = ...) -> None: ...

class VinculoNfManualResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class PrintPedidoRequest(_message.Message):
    __slots__ = ("ids", "modelo", "mostra_composicao", "mostra_medidas", "incluir_imagens")
    IDS_FIELD_NUMBER: _ClassVar[int]
    MODELO_FIELD_NUMBER: _ClassVar[int]
    MOSTRA_COMPOSICAO_FIELD_NUMBER: _ClassVar[int]
    MOSTRA_MEDIDAS_FIELD_NUMBER: _ClassVar[int]
    INCLUIR_IMAGENS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    modelo: str
    mostra_composicao: bool
    mostra_medidas: bool
    incluir_imagens: bool
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., modelo: _Optional[str] = ..., mostra_composicao: _Optional[bool] = ..., mostra_medidas: _Optional[bool] = ..., incluir_imagens: _Optional[bool] = ...) -> None: ...

class PrintPedidoResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class CorrecaoMovimentacaoRequest(_message.Message):
    __slots__ = ("ids", "produto_origem_id", "produto_origem_nome", "produto_destino_id", "produto_destino_nome")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ORIGEM_NOME_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_DESTINO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_DESTINO_NOME_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    produto_origem_id: str
    produto_origem_nome: str
    produto_destino_id: str
    produto_destino_nome: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., produto_origem_id: _Optional[str] = ..., produto_origem_nome: _Optional[str] = ..., produto_destino_id: _Optional[str] = ..., produto_destino_nome: _Optional[str] = ...) -> None: ...

class CorrecaoMovimentacaoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeliveryInfo(_message.Message):
    __slots__ = ("delivery_method", "delivery_zone_id", "delivery_zone_name", "shipping_fee", "estimated_days", "estimated_delivery_date", "tracking_code", "tracking_url", "carrier_name", "carrier_service", "delivery_instructions", "status_history", "address", "pickup_location_id", "pickup_location_name", "pickup_scheduled_date")
    DELIVERY_METHOD_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_ZONE_ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_ZONE_NAME_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_FEE_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DAYS_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_DELIVERY_DATE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_CODE_FIELD_NUMBER: _ClassVar[int]
    TRACKING_URL_FIELD_NUMBER: _ClassVar[int]
    CARRIER_NAME_FIELD_NUMBER: _ClassVar[int]
    CARRIER_SERVICE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    STATUS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PICKUP_LOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    PICKUP_LOCATION_NAME_FIELD_NUMBER: _ClassVar[int]
    PICKUP_SCHEDULED_DATE_FIELD_NUMBER: _ClassVar[int]
    delivery_method: DeliveryMethod
    delivery_zone_id: str
    delivery_zone_name: str
    shipping_fee: float
    estimated_days: int
    estimated_delivery_date: _timestamp_pb2.Timestamp
    tracking_code: str
    tracking_url: str
    carrier_name: str
    carrier_service: str
    delivery_instructions: str
    status_history: _containers.RepeatedCompositeFieldContainer[DeliveryStatusHistory]
    address: DeliveryAddress
    pickup_location_id: str
    pickup_location_name: str
    pickup_scheduled_date: _timestamp_pb2.Timestamp
    def __init__(self, delivery_method: _Optional[_Union[DeliveryMethod, str]] = ..., delivery_zone_id: _Optional[str] = ..., delivery_zone_name: _Optional[str] = ..., shipping_fee: _Optional[float] = ..., estimated_days: _Optional[int] = ..., estimated_delivery_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tracking_code: _Optional[str] = ..., tracking_url: _Optional[str] = ..., carrier_name: _Optional[str] = ..., carrier_service: _Optional[str] = ..., delivery_instructions: _Optional[str] = ..., status_history: _Optional[_Iterable[_Union[DeliveryStatusHistory, _Mapping]]] = ..., address: _Optional[_Union[DeliveryAddress, _Mapping]] = ..., pickup_location_id: _Optional[str] = ..., pickup_location_name: _Optional[str] = ..., pickup_scheduled_date: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class DeliveryStatusHistory(_message.Message):
    __slots__ = ("status", "description", "timestamp", "location")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    status: str
    description: str
    timestamp: _timestamp_pb2.Timestamp
    location: str
    def __init__(self, status: _Optional[str] = ..., description: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., location: _Optional[str] = ...) -> None: ...

class DeliveryAddress(_message.Message):
    __slots__ = ("recipient_name", "cep", "street", "number", "complement", "neighborhood", "city", "city_code", "state", "phone", "reference")
    RECIPIENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CEP_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    COMPLEMENT_FIELD_NUMBER: _ClassVar[int]
    NEIGHBORHOOD_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    CITY_CODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    recipient_name: str
    cep: str
    street: str
    number: str
    complement: str
    neighborhood: str
    city: str
    city_code: str
    state: str
    phone: str
    reference: str
    def __init__(self, recipient_name: _Optional[str] = ..., cep: _Optional[str] = ..., street: _Optional[str] = ..., number: _Optional[str] = ..., complement: _Optional[str] = ..., neighborhood: _Optional[str] = ..., city: _Optional[str] = ..., city_code: _Optional[str] = ..., state: _Optional[str] = ..., phone: _Optional[str] = ..., reference: _Optional[str] = ...) -> None: ...

class ReorderItemsRequest(_message.Message):
    __slots__ = ("id", "produto_ids", "servico_ids")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_IDS_FIELD_NUMBER: _ClassVar[int]
    SERVICO_IDS_FIELD_NUMBER: _ClassVar[int]
    id: str
    produto_ids: _containers.RepeatedScalarFieldContainer[str]
    servico_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., produto_ids: _Optional[_Iterable[str]] = ..., servico_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ReorderItemsResponse(_message.Message):
    __slots__ = ("pedido",)
    PEDIDO_FIELD_NUMBER: _ClassVar[int]
    pedido: Pedido
    def __init__(self, pedido: _Optional[_Union[Pedido, _Mapping]] = ...) -> None: ...

class FaixaResumoVendas(_message.Message):
    __slots__ = ("chave", "inicio", "fim")
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    INICIO_FIELD_NUMBER: _ClassVar[int]
    FIM_FIELD_NUMBER: _ClassVar[int]
    chave: str
    inicio: _timestamp_pb2.Timestamp
    fim: _timestamp_pb2.Timestamp
    def __init__(self, chave: _Optional[str] = ..., inicio: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., fim: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class ResumoVendasPorVendedorRequest(_message.Message):
    __slots__ = ("seller_ids", "faixas", "types", "base")
    SELLER_IDS_FIELD_NUMBER: _ClassVar[int]
    FAIXAS_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    BASE_FIELD_NUMBER: _ClassVar[int]
    seller_ids: _containers.RepeatedScalarFieldContainer[str]
    faixas: _containers.RepeatedCompositeFieldContainer[FaixaResumoVendas]
    types: _containers.RepeatedScalarFieldContainer[str]
    base: BaseApuracao
    def __init__(self, seller_ids: _Optional[_Iterable[str]] = ..., faixas: _Optional[_Iterable[_Union[FaixaResumoVendas, _Mapping]]] = ..., types: _Optional[_Iterable[str]] = ..., base: _Optional[_Union[BaseApuracao, str]] = ...) -> None: ...

class TotalVendasVendedor(_message.Message):
    __slots__ = ("seller_id", "chave", "valor", "quantidade")
    SELLER_ID_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    seller_id: str
    chave: str
    valor: float
    quantidade: int
    def __init__(self, seller_id: _Optional[str] = ..., chave: _Optional[str] = ..., valor: _Optional[float] = ..., quantidade: _Optional[int] = ...) -> None: ...

class ResumoVendasPorVendedorResponse(_message.Message):
    __slots__ = ("totais",)
    TOTAIS_FIELD_NUMBER: _ClassVar[int]
    totais: _containers.RepeatedCompositeFieldContainer[TotalVendasVendedor]
    def __init__(self, totais: _Optional[_Iterable[_Union[TotalVendasVendedor, _Mapping]]] = ...) -> None: ...
