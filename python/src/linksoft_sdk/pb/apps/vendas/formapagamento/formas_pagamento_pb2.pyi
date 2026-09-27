import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethod(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "tipo_pagamento", "nome", "codigo", "padrao", "disponivel_checkout", "disponivel_venda", "usar_carteira_cashback", "lancar_contas_receber", "checkout_nome_tela", "adquirente_nome", "adquirente_cnpj", "adquirente_dias_recebimento_total", "tipo_moeda_baixa", "taxa_adm", "taxa_antecipacao", "taxa_valor_fixo", "juros", "valor_venda_maior_que", "parcelas", "integration", "antifraud_policy", "manual_review_policy", "caixa_id", "caixa_nome", "nao_movimenta_caixa", "nao_gera_comissao", "fields", "tabela_preco", "nao_verifica_limite_credito", "nao_emite_nfse_automatica")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    PADRAO_FIELD_NUMBER: _ClassVar[int]
    DISPONIVEL_CHECKOUT_FIELD_NUMBER: _ClassVar[int]
    DISPONIVEL_VENDA_FIELD_NUMBER: _ClassVar[int]
    USAR_CARTEIRA_CASHBACK_FIELD_NUMBER: _ClassVar[int]
    LANCAR_CONTAS_RECEBER_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_NOME_TELA_FIELD_NUMBER: _ClassVar[int]
    ADQUIRENTE_NOME_FIELD_NUMBER: _ClassVar[int]
    ADQUIRENTE_CNPJ_FIELD_NUMBER: _ClassVar[int]
    ADQUIRENTE_DIAS_RECEBIMENTO_TOTAL_FIELD_NUMBER: _ClassVar[int]
    TIPO_MOEDA_BAIXA_FIELD_NUMBER: _ClassVar[int]
    TAXA_ADM_FIELD_NUMBER: _ClassVar[int]
    TAXA_ANTECIPACAO_FIELD_NUMBER: _ClassVar[int]
    TAXA_VALOR_FIXO_FIELD_NUMBER: _ClassVar[int]
    JUROS_FIELD_NUMBER: _ClassVar[int]
    VALOR_VENDA_MAIOR_QUE_FIELD_NUMBER: _ClassVar[int]
    PARCELAS_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    ANTIFRAUD_POLICY_FIELD_NUMBER: _ClassVar[int]
    MANUAL_REVIEW_POLICY_FIELD_NUMBER: _ClassVar[int]
    CAIXA_ID_FIELD_NUMBER: _ClassVar[int]
    CAIXA_NOME_FIELD_NUMBER: _ClassVar[int]
    NAO_MOVIMENTA_CAIXA_FIELD_NUMBER: _ClassVar[int]
    NAO_GERA_COMISSAO_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    TABELA_PRECO_FIELD_NUMBER: _ClassVar[int]
    NAO_VERIFICA_LIMITE_CREDITO_FIELD_NUMBER: _ClassVar[int]
    NAO_EMITE_NFSE_AUTOMATICA_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    tipo_pagamento: str
    nome: str
    codigo: int
    padrao: bool
    disponivel_checkout: bool
    disponivel_venda: bool
    usar_carteira_cashback: bool
    lancar_contas_receber: bool
    checkout_nome_tela: str
    adquirente_nome: str
    adquirente_cnpj: str
    adquirente_dias_recebimento_total: int
    tipo_moeda_baixa: str
    taxa_adm: float
    taxa_antecipacao: float
    taxa_valor_fixo: float
    juros: float
    valor_venda_maior_que: float
    parcelas: _containers.RepeatedCompositeFieldContainer[Parcelas]
    integration: Integration
    antifraud_policy: FraudPolicy
    manual_review_policy: ManualReviewPolicy
    caixa_id: str
    caixa_nome: str
    nao_movimenta_caixa: bool
    nao_gera_comissao: bool
    fields: _metadata_pb2.BasicFields
    tabela_preco: str
    nao_verifica_limite_credito: bool
    nao_emite_nfse_automatica: bool
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., tipo_pagamento: _Optional[str] = ..., nome: _Optional[str] = ..., codigo: _Optional[int] = ..., padrao: _Optional[bool] = ..., disponivel_checkout: _Optional[bool] = ..., disponivel_venda: _Optional[bool] = ..., usar_carteira_cashback: _Optional[bool] = ..., lancar_contas_receber: _Optional[bool] = ..., checkout_nome_tela: _Optional[str] = ..., adquirente_nome: _Optional[str] = ..., adquirente_cnpj: _Optional[str] = ..., adquirente_dias_recebimento_total: _Optional[int] = ..., tipo_moeda_baixa: _Optional[str] = ..., taxa_adm: _Optional[float] = ..., taxa_antecipacao: _Optional[float] = ..., taxa_valor_fixo: _Optional[float] = ..., juros: _Optional[float] = ..., valor_venda_maior_que: _Optional[float] = ..., parcelas: _Optional[_Iterable[_Union[Parcelas, _Mapping]]] = ..., integration: _Optional[_Union[Integration, _Mapping]] = ..., antifraud_policy: _Optional[_Union[FraudPolicy, _Mapping]] = ..., manual_review_policy: _Optional[_Union[ManualReviewPolicy, _Mapping]] = ..., caixa_id: _Optional[str] = ..., caixa_nome: _Optional[str] = ..., nao_movimenta_caixa: _Optional[bool] = ..., nao_gera_comissao: _Optional[bool] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., tabela_preco: _Optional[str] = ..., nao_verifica_limite_credito: _Optional[bool] = ..., nao_emite_nfse_automatica: _Optional[bool] = ...) -> None: ...

class FraudIntegration(_message.Message):
    __slots__ = ("id", "name", "provider", "environment")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    provider: str
    environment: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., provider: _Optional[str] = ..., environment: _Optional[str] = ...) -> None: ...

class AntifraudCriteria(_message.Message):
    __slots__ = ("payment_types", "min_amount", "max_amount", "min_installments", "max_installments", "checkout_only", "require_device_id")
    PAYMENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_INSTALLMENTS_FIELD_NUMBER: _ClassVar[int]
    MAX_INSTALLMENTS_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_ONLY_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
    payment_types: _containers.RepeatedScalarFieldContainer[str]
    min_amount: float
    max_amount: float
    min_installments: int
    max_installments: int
    checkout_only: bool
    require_device_id: bool
    def __init__(self, payment_types: _Optional[_Iterable[str]] = ..., min_amount: _Optional[float] = ..., max_amount: _Optional[float] = ..., min_installments: _Optional[int] = ..., max_installments: _Optional[int] = ..., checkout_only: _Optional[bool] = ..., require_device_id: _Optional[bool] = ...) -> None: ...

class FraudPolicy(_message.Message):
    __slots__ = ("enabled", "hold_payment_while_pending", "integration", "criteria")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    HOLD_PAYMENT_WHILE_PENDING_FIELD_NUMBER: _ClassVar[int]
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    CRITERIA_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    hold_payment_while_pending: bool
    integration: FraudIntegration
    criteria: AntifraudCriteria
    def __init__(self, enabled: _Optional[bool] = ..., hold_payment_while_pending: _Optional[bool] = ..., integration: _Optional[_Union[FraudIntegration, _Mapping]] = ..., criteria: _Optional[_Union[AntifraudCriteria, _Mapping]] = ...) -> None: ...

class ManualReviewPolicy(_message.Message):
    __slots__ = ("enabled", "required_after_antifraud", "hold_payment_while_pending", "min_amount", "min_installments", "reason_hint")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_AFTER_ANTIFRAUD_FIELD_NUMBER: _ClassVar[int]
    HOLD_PAYMENT_WHILE_PENDING_FIELD_NUMBER: _ClassVar[int]
    MIN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_INSTALLMENTS_FIELD_NUMBER: _ClassVar[int]
    REASON_HINT_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    required_after_antifraud: bool
    hold_payment_while_pending: bool
    min_amount: float
    min_installments: int
    reason_hint: str
    def __init__(self, enabled: _Optional[bool] = ..., required_after_antifraud: _Optional[bool] = ..., hold_payment_while_pending: _Optional[bool] = ..., min_amount: _Optional[float] = ..., min_installments: _Optional[int] = ..., reason_hint: _Optional[str] = ...) -> None: ...

class Integration(_message.Message):
    __slots__ = ("id", "name", "gateway", "gateway_ambiente", "gateway_nome_fatura_cartao", "gateway_dias_validade", "gateway_validade_pos_vencimento_p", "gateway_webhook_url", "gateway_pix")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_AMBIENTE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_NOME_FATURA_CARTAO_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_DIAS_VALIDADE_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_VALIDADE_POS_VENCIMENTO_P_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_WEBHOOK_URL_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_PIX_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    gateway: str
    gateway_ambiente: str
    gateway_nome_fatura_cartao: str
    gateway_dias_validade: int
    gateway_validade_pos_vencimento_p: bool
    gateway_webhook_url: str
    gateway_pix: GatewayPix
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., gateway: _Optional[str] = ..., gateway_ambiente: _Optional[str] = ..., gateway_nome_fatura_cartao: _Optional[str] = ..., gateway_dias_validade: _Optional[int] = ..., gateway_validade_pos_vencimento_p: _Optional[bool] = ..., gateway_webhook_url: _Optional[str] = ..., gateway_pix: _Optional[_Union[GatewayPix, _Mapping]] = ...) -> None: ...

class GatewayPix(_message.Message):
    __slots__ = ("segundos_validos", "chave_pix", "certificado_pix", "cobranca_presencial")
    SEGUNDOS_VALIDOS_FIELD_NUMBER: _ClassVar[int]
    CHAVE_PIX_FIELD_NUMBER: _ClassVar[int]
    CERTIFICADO_PIX_FIELD_NUMBER: _ClassVar[int]
    COBRANCA_PRESENCIAL_FIELD_NUMBER: _ClassVar[int]
    segundos_validos: int
    chave_pix: str
    certificado_pix: CertificadoPix
    cobranca_presencial: bool
    def __init__(self, segundos_validos: _Optional[int] = ..., chave_pix: _Optional[str] = ..., certificado_pix: _Optional[_Union[CertificadoPix, _Mapping]] = ..., cobranca_presencial: _Optional[bool] = ...) -> None: ...

class CertificadoPix(_message.Message):
    __slots__ = ("arquivo_nome", "validade", "conteudo_upload", "download_link")
    ARQUIVO_NOME_FIELD_NUMBER: _ClassVar[int]
    VALIDADE_FIELD_NUMBER: _ClassVar[int]
    CONTEUDO_UPLOAD_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    arquivo_nome: str
    validade: str
    conteudo_upload: str
    download_link: str
    def __init__(self, arquivo_nome: _Optional[str] = ..., validade: _Optional[str] = ..., conteudo_upload: _Optional[str] = ..., download_link: _Optional[str] = ...) -> None: ...

class Parcelas(_message.Message):
    __slots__ = ("id", "numero_parcela", "dias", "juros", "taxa")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_PARCELA_FIELD_NUMBER: _ClassVar[int]
    DIAS_FIELD_NUMBER: _ClassVar[int]
    JUROS_FIELD_NUMBER: _ClassVar[int]
    TAXA_FIELD_NUMBER: _ClassVar[int]
    id: str
    numero_parcela: int
    dias: int
    juros: float
    taxa: float
    def __init__(self, id: _Optional[str] = ..., numero_parcela: _Optional[int] = ..., dias: _Optional[int] = ..., juros: _Optional[float] = ..., taxa: _Optional[float] = ...) -> None: ...

class CreatePaymentMethodRequest(_message.Message):
    __slots__ = ("payment_method",)
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class CreatePaymentMethodResponse(_message.Message):
    __slots__ = ("payment_method",)
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class UpdatePaymentMethodRequest(_message.Message):
    __slots__ = ("id", "payment_method", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    payment_method: PaymentMethod
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdatePaymentMethodResponse(_message.Message):
    __slots__ = ("payment_method",)
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class DeletePaymentMethodRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeletePaymentMethodResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetPaymentMethodRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetPaymentMethodResponse(_message.Message):
    __slots__ = ("payment_method",)
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...

class ListPaymentMethodRequest(_message.Message):
    __slots__ = ("ids", "codigo", "disponivel_venda", "checkout_available", "page_size", "page_token", "filter")
    IDS_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    DISPONIVEL_VENDA_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    codigo: str
    disponivel_venda: bool
    checkout_available: bool
    page_size: int
    page_token: str
    filter: _filter_pb2.Filter
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., codigo: _Optional[str] = ..., disponivel_venda: _Optional[bool] = ..., checkout_available: _Optional[bool] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class ListPaymentMethodResponse(_message.Message):
    __slots__ = ("payment_method_list", "next_page_token")
    PAYMENT_METHOD_LIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    payment_method_list: _containers.RepeatedCompositeFieldContainer[PaymentMethod]
    next_page_token: str
    def __init__(self, payment_method_list: _Optional[_Iterable[_Union[PaymentMethod, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class ImportPaymentMethodRequest(_message.Message):
    __slots__ = ("payment_methods", "update_if_exists")
    PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    payment_methods: _containers.RepeatedCompositeFieldContainer[PaymentMethod]
    update_if_exists: bool
    def __init__(self, payment_methods: _Optional[_Iterable[_Union[PaymentMethod, _Mapping]]] = ..., update_if_exists: _Optional[bool] = ...) -> None: ...

class ImportPaymentMethodResponse(_message.Message):
    __slots__ = ("payment_methods", "imported_count", "updated_count", "error_count", "errors")
    PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    IMPORTED_COUNT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    payment_methods: _containers.RepeatedCompositeFieldContainer[PaymentMethod]
    imported_count: int
    updated_count: int
    error_count: int
    errors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, payment_methods: _Optional[_Iterable[_Union[PaymentMethod, _Mapping]]] = ..., imported_count: _Optional[int] = ..., updated_count: _Optional[int] = ..., error_count: _Optional[int] = ..., errors: _Optional[_Iterable[str]] = ...) -> None: ...

class ClonePaymentMethodRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ClonePaymentMethodResponse(_message.Message):
    __slots__ = ("payment_method",)
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    payment_method: PaymentMethod
    def __init__(self, payment_method: _Optional[_Union[PaymentMethod, _Mapping]] = ...) -> None: ...
