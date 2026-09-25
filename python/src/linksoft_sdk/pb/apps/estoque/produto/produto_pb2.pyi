import datetime

from google.api import annotations_pb2 as _annotations_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.apps.estoque.movimento import movimentoestoque_pb2 as _movimentoestoque_pb2
from linksoft_sdk.pb.apps.estoque.produto import vehicle_pb2 as _vehicle_pb2
from linksoft_sdk.pb.exports import exports_pb2 as _exports_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EcommerceAvailability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ECOMMERCE_AVAILABILITY_CATEGORY: _ClassVar[EcommerceAvailability]
    ECOMMERCE_AVAILABILITY_YES: _ClassVar[EcommerceAvailability]
    ECOMMERCE_AVAILABILITY_NO: _ClassVar[EcommerceAvailability]

class NegativeStockRule(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NEGATIVE_STOCK_RULE_UNSPECIFIED: _ClassVar[NegativeStockRule]
    NEGATIVE_STOCK_RULE_ALLOW_NEGATIVE_MOVEMENT: _ClassVar[NegativeStockRule]
    NEGATIVE_STOCK_RULE_BLOCK_NEGATIVE_MOVEMENT: _ClassVar[NegativeStockRule]

class ProductMediaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCT_MEDIA_TYPE_UNSPECIFIED: _ClassVar[ProductMediaType]
    PRODUCT_MEDIA_TYPE_IMAGE: _ClassVar[ProductMediaType]
    PRODUCT_MEDIA_TYPE_VIDEO: _ClassVar[ProductMediaType]

class Rentabilidade(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RENTABILIDADE_DEFAULT: _ClassVar[Rentabilidade]
    RENTABILIDADE_ABAIXO_DO_CUSTO: _ClassVar[Rentabilidade]
    RENTABILIDADE_SEM_MARGEM: _ClassVar[Rentabilidade]
    RENTABILIDADE_SEM_CUSTO: _ClassVar[Rentabilidade]
    RENTABILIDADE_SEM_PRECO: _ClassVar[Rentabilidade]

class StockMovement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOCK_MOVEMENT_DEFAULT: _ClassVar[StockMovement]
    STOCK_MOVEMENT_HAS_MOVIMENT: _ClassVar[StockMovement]
    STOCK_MOVEMENT_HAS_NOT_MOVIMENT: _ClassVar[StockMovement]
    STOCK_MOVEMENT_IN_STOCK: _ClassVar[StockMovement]
    STOCK_MOVEMENT_OUT_OF_STOCK: _ClassVar[StockMovement]
    STOCK_MOVEMENT_HAS_NO_NF_ENTRADA: _ClassVar[StockMovement]
    STOCK_MOVEMENT_HAS_NF_ENTRADA: _ClassVar[StockMovement]
    STOCK_MOVEMENT_NEGATIVE: _ClassVar[StockMovement]
    STOCK_MOVEMENT_NOT_ZERO: _ClassVar[StockMovement]
ECOMMERCE_AVAILABILITY_CATEGORY: EcommerceAvailability
ECOMMERCE_AVAILABILITY_YES: EcommerceAvailability
ECOMMERCE_AVAILABILITY_NO: EcommerceAvailability
NEGATIVE_STOCK_RULE_UNSPECIFIED: NegativeStockRule
NEGATIVE_STOCK_RULE_ALLOW_NEGATIVE_MOVEMENT: NegativeStockRule
NEGATIVE_STOCK_RULE_BLOCK_NEGATIVE_MOVEMENT: NegativeStockRule
PRODUCT_MEDIA_TYPE_UNSPECIFIED: ProductMediaType
PRODUCT_MEDIA_TYPE_IMAGE: ProductMediaType
PRODUCT_MEDIA_TYPE_VIDEO: ProductMediaType
RENTABILIDADE_DEFAULT: Rentabilidade
RENTABILIDADE_ABAIXO_DO_CUSTO: Rentabilidade
RENTABILIDADE_SEM_MARGEM: Rentabilidade
RENTABILIDADE_SEM_CUSTO: Rentabilidade
RENTABILIDADE_SEM_PRECO: Rentabilidade
STOCK_MOVEMENT_DEFAULT: StockMovement
STOCK_MOVEMENT_HAS_MOVIMENT: StockMovement
STOCK_MOVEMENT_HAS_NOT_MOVIMENT: StockMovement
STOCK_MOVEMENT_IN_STOCK: StockMovement
STOCK_MOVEMENT_OUT_OF_STOCK: StockMovement
STOCK_MOVEMENT_HAS_NO_NF_ENTRADA: StockMovement
STOCK_MOVEMENT_HAS_NF_ENTRADA: StockMovement
STOCK_MOVEMENT_NEGATIVE: StockMovement
STOCK_MOVEMENT_NOT_ZERO: StockMovement

class ProdutoTag(_message.Message):
    __slots__ = ("value", "color")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    value: str
    color: str
    def __init__(self, value: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...

class Produto(_message.Message):
    __slots__ = ("fields", "id", "importadoEm", "situacao", "nome", "primary_media", "media", "un", "unTrib", "fatorConversaoUnidade", "isFracionavel", "descricao", "aplicacao", "codigoProduto", "codigoBarra", "codigoReferencia", "codes", "fabricanteId", "fabricanteNome", "tributacaoId", "tributacaoNome", "tributacaoRevendaId", "tributacaoRevendaNome", "fator_conversao_monofasico", "fator_conversao_proporcional", "categoriaId", "categoriaNome", "segmentoId", "segmentoNome", "ncm", "cest", "pesoBruto", "pesoLiquido", "valorUnitario", "precoVendaAprazo", "precoVendaAtacado", "historicoPreco", "precoComposicao", "quantidadeMinima", "quantidadeMaxima", "quantidadeMinimaVenda", "quantidadeVendaMultiplo", "quantidadeEmbalagem", "bloquearEstoqueNegativo", "negative_stok_rules", "diasGarantiaEmpresa", "diasGarantia", "descricaoAdicionalVenda", "composto", "composicao", "rendimento", "tags", "estoques", "estoquesList", "localizacoes", "consultaQuantidade", "quantidadeEstoqueTotal", "quantidadeImportar", "produtoEspecifico", "precoUltimaCompra", "custoManual", "precoCusto", "custoMedio", "custoIcms", "custoIpi", "custoFrete", "custoOutrasDespesas", "custoDiferencaAliquota", "margemLucro", "margem_icms", "margem_ipi", "margem_comissao", "custo_comissao", "margem_outras_despesas", "margem_custo", "margem_lucro_aprazo", "margem_desconto_atacado", "codigoAnp", "codigoAnpDescricao", "percentualGlp", "percentualGasNaturalNacional", "percentualGasNaturalImportado", "grade", "promocao", "ecommerce", "has_batch_control", "parent_product_id", "parent_product_name", "variation", "variations", "comissao", "impressoraId", "impressoraNome", "grupoProducao", "naoImprimirProducao", "insumo", "composicaoFixa", "dadosFiscais", "has_serial_control", "vehicle", "comodato", "createdAt", "updatedAt", "userId", "userName", "type", "description")
    class EstoquesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Estoque
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Estoque, _Mapping]] = ...) -> None: ...
    class Ecommerce(_message.Message):
        __slots__ = ("slug", "availability", "featured", "short_description", "full_description", "tags", "keywords", "meta_title", "meta_description", "display_order", "video_url", "highlights", "hide_price", "hide_price_message", "promotional_price")
        SLUG_FIELD_NUMBER: _ClassVar[int]
        AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
        FEATURED_FIELD_NUMBER: _ClassVar[int]
        SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        FULL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        KEYWORDS_FIELD_NUMBER: _ClassVar[int]
        META_TITLE_FIELD_NUMBER: _ClassVar[int]
        META_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_ORDER_FIELD_NUMBER: _ClassVar[int]
        VIDEO_URL_FIELD_NUMBER: _ClassVar[int]
        HIGHLIGHTS_FIELD_NUMBER: _ClassVar[int]
        HIDE_PRICE_FIELD_NUMBER: _ClassVar[int]
        HIDE_PRICE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PROMOTIONAL_PRICE_FIELD_NUMBER: _ClassVar[int]
        slug: str
        availability: EcommerceAvailability
        featured: bool
        short_description: str
        full_description: str
        tags: _containers.RepeatedScalarFieldContainer[str]
        keywords: _containers.RepeatedScalarFieldContainer[str]
        meta_title: str
        meta_description: str
        display_order: int
        video_url: str
        highlights: _containers.RepeatedCompositeFieldContainer[Produto.ProductHighlight]
        hide_price: bool
        hide_price_message: str
        promotional_price: float
        def __init__(self, slug: _Optional[str] = ..., availability: _Optional[_Union[EcommerceAvailability, str]] = ..., featured: _Optional[bool] = ..., short_description: _Optional[str] = ..., full_description: _Optional[str] = ..., tags: _Optional[_Iterable[str]] = ..., keywords: _Optional[_Iterable[str]] = ..., meta_title: _Optional[str] = ..., meta_description: _Optional[str] = ..., display_order: _Optional[int] = ..., video_url: _Optional[str] = ..., highlights: _Optional[_Iterable[_Union[Produto.ProductHighlight, _Mapping]]] = ..., hide_price: _Optional[bool] = ..., hide_price_message: _Optional[str] = ..., promotional_price: _Optional[float] = ...) -> None: ...
    class VariationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Produto.ProductVariation
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Produto.ProductVariation, _Mapping]] = ...) -> None: ...
    class DadosFiscais(_message.Message):
        __slots__ = ("icmsOrigem", "icmsReducaoBase", "ipiAliquota", "icmsStMargemValorAdicional", "icmsStAliquota", "icmsStReducaoBase")
        ICMSORIGEM_FIELD_NUMBER: _ClassVar[int]
        ICMSREDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
        IPIALIQUOTA_FIELD_NUMBER: _ClassVar[int]
        ICMSSTMARGEMVALORADICIONAL_FIELD_NUMBER: _ClassVar[int]
        ICMSSTALIQUOTA_FIELD_NUMBER: _ClassVar[int]
        ICMSSTREDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
        icmsOrigem: str
        icmsReducaoBase: float
        ipiAliquota: float
        icmsStMargemValorAdicional: float
        icmsStAliquota: float
        icmsStReducaoBase: float
        def __init__(self, icmsOrigem: _Optional[str] = ..., icmsReducaoBase: _Optional[float] = ..., ipiAliquota: _Optional[float] = ..., icmsStMargemValorAdicional: _Optional[float] = ..., icmsStAliquota: _Optional[float] = ..., icmsStReducaoBase: _Optional[float] = ...) -> None: ...
    class ProductVariationMeta(_message.Message):
        __slots__ = ("template_id", "template_name", "is_variation_child", "variation_key", "display_name", "attributes", "hidden_from_product_search", "sku", "code")
        class AttributesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
        TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
        IS_VARIATION_CHILD_FIELD_NUMBER: _ClassVar[int]
        VARIATION_KEY_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_FROM_PRODUCT_SEARCH_FIELD_NUMBER: _ClassVar[int]
        SKU_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        template_id: str
        template_name: str
        is_variation_child: bool
        variation_key: str
        display_name: str
        attributes: _containers.ScalarMap[str, str]
        hidden_from_product_search: bool
        sku: str
        code: str
        def __init__(self, template_id: _Optional[str] = ..., template_name: _Optional[str] = ..., is_variation_child: _Optional[bool] = ..., variation_key: _Optional[str] = ..., display_name: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., hidden_from_product_search: _Optional[bool] = ..., sku: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...
    class ProductVariation(_message.Message):
        __slots__ = ("id", "sku", "code", "attributes", "display_name", "quantity", "stock_quantities", "active", "valor_unitario", "preco_venda_aprazo", "preco_venda_atacado", "barcode")
        class AttributesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class StockQuantitiesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: float
            def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
        ID_FIELD_NUMBER: _ClassVar[int]
        SKU_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        STOCK_QUANTITIES_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
        PRECO_VENDA_APRAZO_FIELD_NUMBER: _ClassVar[int]
        PRECO_VENDA_ATACADO_FIELD_NUMBER: _ClassVar[int]
        BARCODE_FIELD_NUMBER: _ClassVar[int]
        id: str
        sku: str
        code: str
        attributes: _containers.ScalarMap[str, str]
        display_name: str
        quantity: float
        stock_quantities: _containers.ScalarMap[str, float]
        active: bool
        valor_unitario: float
        preco_venda_aprazo: float
        preco_venda_atacado: float
        barcode: str
        def __init__(self, id: _Optional[str] = ..., sku: _Optional[str] = ..., code: _Optional[str] = ..., attributes: _Optional[_Mapping[str, str]] = ..., display_name: _Optional[str] = ..., quantity: _Optional[float] = ..., stock_quantities: _Optional[_Mapping[str, float]] = ..., active: _Optional[bool] = ..., valor_unitario: _Optional[float] = ..., preco_venda_aprazo: _Optional[float] = ..., preco_venda_atacado: _Optional[float] = ..., barcode: _Optional[str] = ...) -> None: ...
    class ProductHighlight(_message.Message):
        __slots__ = ("icon", "title", "description")
        ICON_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        icon: str
        title: str
        description: str
        def __init__(self, icon: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMPORTADOEM_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_MEDIA_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    UNTRIB_FIELD_NUMBER: _ClassVar[int]
    FATORCONVERSAOUNIDADE_FIELD_NUMBER: _ClassVar[int]
    ISFRACIONAVEL_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    APLICACAO_FIELD_NUMBER: _ClassVar[int]
    CODIGOPRODUTO_FIELD_NUMBER: _ClassVar[int]
    CODIGOBARRA_FIELD_NUMBER: _ClassVar[int]
    CODIGOREFERENCIA_FIELD_NUMBER: _ClassVar[int]
    CODES_FIELD_NUMBER: _ClassVar[int]
    FABRICANTEID_FIELD_NUMBER: _ClassVar[int]
    FABRICANTENOME_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAOID_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAONOME_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAOREVENDAID_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAOREVENDANOME_FIELD_NUMBER: _ClassVar[int]
    FATOR_CONVERSAO_MONOFASICO_FIELD_NUMBER: _ClassVar[int]
    FATOR_CONVERSAO_PROPORCIONAL_FIELD_NUMBER: _ClassVar[int]
    CATEGORIAID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIANOME_FIELD_NUMBER: _ClassVar[int]
    SEGMENTOID_FIELD_NUMBER: _ClassVar[int]
    SEGMENTONOME_FIELD_NUMBER: _ClassVar[int]
    NCM_FIELD_NUMBER: _ClassVar[int]
    CEST_FIELD_NUMBER: _ClassVar[int]
    PESOBRUTO_FIELD_NUMBER: _ClassVar[int]
    PESOLIQUIDO_FIELD_NUMBER: _ClassVar[int]
    VALORUNITARIO_FIELD_NUMBER: _ClassVar[int]
    PRECOVENDAAPRAZO_FIELD_NUMBER: _ClassVar[int]
    PRECOVENDAATACADO_FIELD_NUMBER: _ClassVar[int]
    HISTORICOPRECO_FIELD_NUMBER: _ClassVar[int]
    PRECOCOMPOSICAO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEMINIMA_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEMAXIMA_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEMINIMAVENDA_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEVENDAMULTIPLO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEEMBALAGEM_FIELD_NUMBER: _ClassVar[int]
    BLOQUEARESTOQUENEGATIVO_FIELD_NUMBER: _ClassVar[int]
    NEGATIVE_STOK_RULES_FIELD_NUMBER: _ClassVar[int]
    DIASGARANTIAEMPRESA_FIELD_NUMBER: _ClassVar[int]
    DIASGARANTIA_FIELD_NUMBER: _ClassVar[int]
    DESCRICAOADICIONALVENDA_FIELD_NUMBER: _ClassVar[int]
    COMPOSTO_FIELD_NUMBER: _ClassVar[int]
    COMPOSICAO_FIELD_NUMBER: _ClassVar[int]
    RENDIMENTO_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    ESTOQUES_FIELD_NUMBER: _ClassVar[int]
    ESTOQUESLIST_FIELD_NUMBER: _ClassVar[int]
    LOCALIZACOES_FIELD_NUMBER: _ClassVar[int]
    CONSULTAQUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEESTOQUETOTAL_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEIMPORTAR_FIELD_NUMBER: _ClassVar[int]
    PRODUTOESPECIFICO_FIELD_NUMBER: _ClassVar[int]
    PRECOULTIMACOMPRA_FIELD_NUMBER: _ClassVar[int]
    CUSTOMANUAL_FIELD_NUMBER: _ClassVar[int]
    PRECOCUSTO_FIELD_NUMBER: _ClassVar[int]
    CUSTOMEDIO_FIELD_NUMBER: _ClassVar[int]
    CUSTOICMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOIPI_FIELD_NUMBER: _ClassVar[int]
    CUSTOFRETE_FIELD_NUMBER: _ClassVar[int]
    CUSTOOUTRASDESPESAS_FIELD_NUMBER: _ClassVar[int]
    CUSTODIFERENCAALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    MARGEMLUCRO_FIELD_NUMBER: _ClassVar[int]
    MARGEM_ICMS_FIELD_NUMBER: _ClassVar[int]
    MARGEM_IPI_FIELD_NUMBER: _ClassVar[int]
    MARGEM_COMISSAO_FIELD_NUMBER: _ClassVar[int]
    CUSTO_COMISSAO_FIELD_NUMBER: _ClassVar[int]
    MARGEM_OUTRAS_DESPESAS_FIELD_NUMBER: _ClassVar[int]
    MARGEM_CUSTO_FIELD_NUMBER: _ClassVar[int]
    MARGEM_LUCRO_APRAZO_FIELD_NUMBER: _ClassVar[int]
    MARGEM_DESCONTO_ATACADO_FIELD_NUMBER: _ClassVar[int]
    CODIGOANP_FIELD_NUMBER: _ClassVar[int]
    CODIGOANPDESCRICAO_FIELD_NUMBER: _ClassVar[int]
    PERCENTUALGLP_FIELD_NUMBER: _ClassVar[int]
    PERCENTUALGASNATURALNACIONAL_FIELD_NUMBER: _ClassVar[int]
    PERCENTUALGASNATURALIMPORTADO_FIELD_NUMBER: _ClassVar[int]
    GRADE_FIELD_NUMBER: _ClassVar[int]
    PROMOCAO_FIELD_NUMBER: _ClassVar[int]
    ECOMMERCE_FIELD_NUMBER: _ClassVar[int]
    HAS_BATCH_CONTROL_FIELD_NUMBER: _ClassVar[int]
    PARENT_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    VARIATION_FIELD_NUMBER: _ClassVar[int]
    VARIATIONS_FIELD_NUMBER: _ClassVar[int]
    COMISSAO_FIELD_NUMBER: _ClassVar[int]
    IMPRESSORAID_FIELD_NUMBER: _ClassVar[int]
    IMPRESSORANOME_FIELD_NUMBER: _ClassVar[int]
    GRUPOPRODUCAO_FIELD_NUMBER: _ClassVar[int]
    NAOIMPRIMIRPRODUCAO_FIELD_NUMBER: _ClassVar[int]
    INSUMO_FIELD_NUMBER: _ClassVar[int]
    COMPOSICAOFIXA_FIELD_NUMBER: _ClassVar[int]
    DADOSFISCAIS_FIELD_NUMBER: _ClassVar[int]
    HAS_SERIAL_CONTROL_FIELD_NUMBER: _ClassVar[int]
    VEHICLE_FIELD_NUMBER: _ClassVar[int]
    COMODATO_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    fields: _metadata_pb2.BasicFields
    id: str
    importadoEm: _timestamp_pb2.Timestamp
    situacao: str
    nome: str
    primary_media: ProductMedia
    media: _containers.RepeatedCompositeFieldContainer[ProductMedia]
    un: str
    unTrib: str
    fatorConversaoUnidade: float
    isFracionavel: bool
    descricao: str
    aplicacao: str
    codigoProduto: str
    codigoBarra: str
    codigoReferencia: str
    codes: _containers.RepeatedScalarFieldContainer[str]
    fabricanteId: str
    fabricanteNome: str
    tributacaoId: str
    tributacaoNome: str
    tributacaoRevendaId: str
    tributacaoRevendaNome: str
    fator_conversao_monofasico: float
    fator_conversao_proporcional: float
    categoriaId: str
    categoriaNome: str
    segmentoId: str
    segmentoNome: str
    ncm: str
    cest: str
    pesoBruto: float
    pesoLiquido: float
    valorUnitario: float
    precoVendaAprazo: float
    precoVendaAtacado: float
    historicoPreco: _containers.RepeatedCompositeFieldContainer[HistoricoPreco]
    precoComposicao: float
    quantidadeMinima: float
    quantidadeMaxima: float
    quantidadeMinimaVenda: float
    quantidadeVendaMultiplo: float
    quantidadeEmbalagem: int
    bloquearEstoqueNegativo: bool
    negative_stok_rules: NegativeStockRule
    diasGarantiaEmpresa: float
    diasGarantia: float
    descricaoAdicionalVenda: bool
    composto: bool
    composicao: _containers.RepeatedCompositeFieldContainer[Composicao]
    rendimento: float
    tags: _containers.RepeatedCompositeFieldContainer[ProdutoTag]
    estoques: _containers.MessageMap[str, Estoque]
    estoquesList: _containers.RepeatedCompositeFieldContainer[Estoque]
    localizacoes: _containers.RepeatedCompositeFieldContainer[ProdutoLocalizacao]
    consultaQuantidade: float
    quantidadeEstoqueTotal: float
    quantidadeImportar: float
    produtoEspecifico: str
    precoUltimaCompra: float
    custoManual: bool
    precoCusto: float
    custoMedio: float
    custoIcms: float
    custoIpi: float
    custoFrete: float
    custoOutrasDespesas: float
    custoDiferencaAliquota: float
    margemLucro: float
    margem_icms: float
    margem_ipi: float
    margem_comissao: float
    custo_comissao: float
    margem_outras_despesas: float
    margem_custo: float
    margem_lucro_aprazo: float
    margem_desconto_atacado: float
    codigoAnp: str
    codigoAnpDescricao: str
    percentualGlp: float
    percentualGasNaturalNacional: float
    percentualGasNaturalImportado: float
    grade: _containers.RepeatedCompositeFieldContainer[Grade]
    promocao: str
    ecommerce: Produto.Ecommerce
    has_batch_control: bool
    parent_product_id: str
    parent_product_name: str
    variation: Produto.ProductVariationMeta
    variations: _containers.MessageMap[str, Produto.ProductVariation]
    comissao: float
    impressoraId: str
    impressoraNome: str
    grupoProducao: str
    naoImprimirProducao: bool
    insumo: bool
    composicaoFixa: bool
    dadosFiscais: Produto.DadosFiscais
    has_serial_control: bool
    vehicle: _vehicle_pb2.VehicleData
    comodato: bool
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    type: str
    description: str
    def __init__(self, fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., id: _Optional[str] = ..., importadoEm: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., situacao: _Optional[str] = ..., nome: _Optional[str] = ..., primary_media: _Optional[_Union[ProductMedia, _Mapping]] = ..., media: _Optional[_Iterable[_Union[ProductMedia, _Mapping]]] = ..., un: _Optional[str] = ..., unTrib: _Optional[str] = ..., fatorConversaoUnidade: _Optional[float] = ..., isFracionavel: _Optional[bool] = ..., descricao: _Optional[str] = ..., aplicacao: _Optional[str] = ..., codigoProduto: _Optional[str] = ..., codigoBarra: _Optional[str] = ..., codigoReferencia: _Optional[str] = ..., codes: _Optional[_Iterable[str]] = ..., fabricanteId: _Optional[str] = ..., fabricanteNome: _Optional[str] = ..., tributacaoId: _Optional[str] = ..., tributacaoNome: _Optional[str] = ..., tributacaoRevendaId: _Optional[str] = ..., tributacaoRevendaNome: _Optional[str] = ..., fator_conversao_monofasico: _Optional[float] = ..., fator_conversao_proporcional: _Optional[float] = ..., categoriaId: _Optional[str] = ..., categoriaNome: _Optional[str] = ..., segmentoId: _Optional[str] = ..., segmentoNome: _Optional[str] = ..., ncm: _Optional[str] = ..., cest: _Optional[str] = ..., pesoBruto: _Optional[float] = ..., pesoLiquido: _Optional[float] = ..., valorUnitario: _Optional[float] = ..., precoVendaAprazo: _Optional[float] = ..., precoVendaAtacado: _Optional[float] = ..., historicoPreco: _Optional[_Iterable[_Union[HistoricoPreco, _Mapping]]] = ..., precoComposicao: _Optional[float] = ..., quantidadeMinima: _Optional[float] = ..., quantidadeMaxima: _Optional[float] = ..., quantidadeMinimaVenda: _Optional[float] = ..., quantidadeVendaMultiplo: _Optional[float] = ..., quantidadeEmbalagem: _Optional[int] = ..., bloquearEstoqueNegativo: _Optional[bool] = ..., negative_stok_rules: _Optional[_Union[NegativeStockRule, str]] = ..., diasGarantiaEmpresa: _Optional[float] = ..., diasGarantia: _Optional[float] = ..., descricaoAdicionalVenda: _Optional[bool] = ..., composto: _Optional[bool] = ..., composicao: _Optional[_Iterable[_Union[Composicao, _Mapping]]] = ..., rendimento: _Optional[float] = ..., tags: _Optional[_Iterable[_Union[ProdutoTag, _Mapping]]] = ..., estoques: _Optional[_Mapping[str, Estoque]] = ..., estoquesList: _Optional[_Iterable[_Union[Estoque, _Mapping]]] = ..., localizacoes: _Optional[_Iterable[_Union[ProdutoLocalizacao, _Mapping]]] = ..., consultaQuantidade: _Optional[float] = ..., quantidadeEstoqueTotal: _Optional[float] = ..., quantidadeImportar: _Optional[float] = ..., produtoEspecifico: _Optional[str] = ..., precoUltimaCompra: _Optional[float] = ..., custoManual: _Optional[bool] = ..., precoCusto: _Optional[float] = ..., custoMedio: _Optional[float] = ..., custoIcms: _Optional[float] = ..., custoIpi: _Optional[float] = ..., custoFrete: _Optional[float] = ..., custoOutrasDespesas: _Optional[float] = ..., custoDiferencaAliquota: _Optional[float] = ..., margemLucro: _Optional[float] = ..., margem_icms: _Optional[float] = ..., margem_ipi: _Optional[float] = ..., margem_comissao: _Optional[float] = ..., custo_comissao: _Optional[float] = ..., margem_outras_despesas: _Optional[float] = ..., margem_custo: _Optional[float] = ..., margem_lucro_aprazo: _Optional[float] = ..., margem_desconto_atacado: _Optional[float] = ..., codigoAnp: _Optional[str] = ..., codigoAnpDescricao: _Optional[str] = ..., percentualGlp: _Optional[float] = ..., percentualGasNaturalNacional: _Optional[float] = ..., percentualGasNaturalImportado: _Optional[float] = ..., grade: _Optional[_Iterable[_Union[Grade, _Mapping]]] = ..., promocao: _Optional[str] = ..., ecommerce: _Optional[_Union[Produto.Ecommerce, _Mapping]] = ..., has_batch_control: _Optional[bool] = ..., parent_product_id: _Optional[str] = ..., parent_product_name: _Optional[str] = ..., variation: _Optional[_Union[Produto.ProductVariationMeta, _Mapping]] = ..., variations: _Optional[_Mapping[str, Produto.ProductVariation]] = ..., comissao: _Optional[float] = ..., impressoraId: _Optional[str] = ..., impressoraNome: _Optional[str] = ..., grupoProducao: _Optional[str] = ..., naoImprimirProducao: _Optional[bool] = ..., insumo: _Optional[bool] = ..., composicaoFixa: _Optional[bool] = ..., dadosFiscais: _Optional[_Union[Produto.DadosFiscais, _Mapping]] = ..., has_serial_control: _Optional[bool] = ..., vehicle: _Optional[_Union[_vehicle_pb2.VehicleData, _Mapping]] = ..., comodato: _Optional[bool] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., type: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class ProductMedia(_message.Message):
    __slots__ = ("id", "created_at", "updated_at", "media_type", "url", "file_id", "display_name", "file_extension", "attribute_key", "attribute_value")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FILE_EXTENSION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_KEY_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_VALUE_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    media_type: ProductMediaType
    url: str
    file_id: str
    display_name: str
    file_extension: str
    attribute_key: str
    attribute_value: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., media_type: _Optional[_Union[ProductMediaType, str]] = ..., url: _Optional[str] = ..., file_id: _Optional[str] = ..., display_name: _Optional[str] = ..., file_extension: _Optional[str] = ..., attribute_key: _Optional[str] = ..., attribute_value: _Optional[str] = ...) -> None: ...

class HistoricoPreco(_message.Message):
    __slots__ = ("tipo_preco", "valor", "preco_anterior", "data", "userId", "userNome")
    TIPO_PRECO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    PRECO_ANTERIOR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNOME_FIELD_NUMBER: _ClassVar[int]
    tipo_preco: str
    valor: float
    preco_anterior: float
    data: _timestamp_pb2.Timestamp
    userId: str
    userNome: str
    def __init__(self, tipo_preco: _Optional[str] = ..., valor: _Optional[float] = ..., preco_anterior: _Optional[float] = ..., data: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userNome: _Optional[str] = ...) -> None: ...

class Composicao(_message.Message):
    __slots__ = ("id", "item_id", "tipo", "nome", "quantidade", "un", "valor_unitario", "total", "perda_percentual")
    ID_FIELD_NUMBER: _ClassVar[int]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    PERDA_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    id: str
    item_id: str
    tipo: str
    nome: str
    quantidade: float
    un: str
    valor_unitario: float
    total: float
    perda_percentual: float
    def __init__(self, id: _Optional[str] = ..., item_id: _Optional[str] = ..., tipo: _Optional[str] = ..., nome: _Optional[str] = ..., quantidade: _Optional[float] = ..., un: _Optional[str] = ..., valor_unitario: _Optional[float] = ..., total: _Optional[float] = ..., perda_percentual: _Optional[float] = ...) -> None: ...

class ProdutoLocalizacao(_message.Message):
    __slots__ = ("estoque_nome", "localizacao")
    ESTOQUE_NOME_FIELD_NUMBER: _ClassVar[int]
    LOCALIZACAO_FIELD_NUMBER: _ClassVar[int]
    estoque_nome: str
    localizacao: str
    def __init__(self, estoque_nome: _Optional[str] = ..., localizacao: _Optional[str] = ...) -> None: ...

class Estoque(_message.Message):
    __slots__ = ("estoque_id", "estoque_nome", "quantidade", "createdAt", "updatedAt", "id")
    ESTOQUE_ID_FIELD_NUMBER: _ClassVar[int]
    ESTOQUE_NOME_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    estoque_id: str
    estoque_nome: str
    quantidade: float
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    id: str
    def __init__(self, estoque_id: _Optional[str] = ..., estoque_nome: _Optional[str] = ..., quantidade: _Optional[float] = ..., createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...

class Grade(_message.Message):
    __slots__ = ("id", "color", "size", "qtd")
    ID_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    QTD_FIELD_NUMBER: _ClassVar[int]
    id: str
    color: str
    size: str
    qtd: float
    def __init__(self, id: _Optional[str] = ..., color: _Optional[str] = ..., size: _Optional[str] = ..., qtd: _Optional[float] = ...) -> None: ...

class CreateProdutoRequest(_message.Message):
    __slots__ = ("produto",)
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    produto: Produto
    def __init__(self, produto: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class CreateProdutoResponse(_message.Message):
    __slots__ = ("produto",)
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    produto: Produto
    def __init__(self, produto: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class UpdateProdutoRequest(_message.Message):
    __slots__ = ("id", "produto", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    produto: Produto
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., produto: _Optional[_Union[Produto, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateProdutoResponse(_message.Message):
    __slots__ = ("produto",)
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    produto: Produto
    def __init__(self, produto: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class DeleteProdutoRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteProdutoResponse(_message.Message):
    __slots__ = ("id", "avisos")
    ID_FIELD_NUMBER: _ClassVar[int]
    AVISOS_FIELD_NUMBER: _ClassVar[int]
    id: str
    avisos: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[str] = ..., avisos: _Optional[_Iterable[str]] = ...) -> None: ...

class GetProdutoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetProdutoResponse(_message.Message):
    __slots__ = ("produto",)
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    produto: Produto
    def __init__(self, produto: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class ListProdutoRequest(_message.Message):
    __slots__ = ("ids", "names", "eanCodes", "productCodes", "page_size", "page_token", "produto", "codigoReferencia", "categoriaNome", "categoriaId", "fabricanteNome", "fabricanteId", "temCategoria", "temFabricante", "createdAtGte", "createdAtLte", "updatedAtGte", "updatedAtLte", "precoCustoGte", "precoCustoLte", "precoVendaAvistaGte", "precoVendaAvistaLte", "precoVendaAprazoGte", "precoVendaAprazoLte", "quantidadeGte", "quantidadeLte", "codigoProduto", "codigoBarra", "unidade", "ignoreSituacaoPadrao", "situacao", "filter", "categoriaIds", "stock_movement", "rentabilidade", "parent_product_id", "include_variation_children", "exclude_insumos", "markup_gte", "markup_lte")
    IDS_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    EANCODES_FIELD_NUMBER: _ClassVar[int]
    PRODUCTCODES_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    CODIGOREFERENCIA_FIELD_NUMBER: _ClassVar[int]
    CATEGORIANOME_FIELD_NUMBER: _ClassVar[int]
    CATEGORIAID_FIELD_NUMBER: _ClassVar[int]
    FABRICANTENOME_FIELD_NUMBER: _ClassVar[int]
    FABRICANTEID_FIELD_NUMBER: _ClassVar[int]
    TEMCATEGORIA_FIELD_NUMBER: _ClassVar[int]
    TEMFABRICANTE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATGTE_FIELD_NUMBER: _ClassVar[int]
    CREATEDATLTE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDATGTE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDATLTE_FIELD_NUMBER: _ClassVar[int]
    PRECOCUSTOGTE_FIELD_NUMBER: _ClassVar[int]
    PRECOCUSTOLTE_FIELD_NUMBER: _ClassVar[int]
    PRECOVENDAAVISTAGTE_FIELD_NUMBER: _ClassVar[int]
    PRECOVENDAAVISTALTE_FIELD_NUMBER: _ClassVar[int]
    PRECOVENDAAPRAZOGTE_FIELD_NUMBER: _ClassVar[int]
    PRECOVENDAAPRAZOLTE_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEGTE_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADELTE_FIELD_NUMBER: _ClassVar[int]
    CODIGOPRODUTO_FIELD_NUMBER: _ClassVar[int]
    CODIGOBARRA_FIELD_NUMBER: _ClassVar[int]
    UNIDADE_FIELD_NUMBER: _ClassVar[int]
    IGNORESITUACAOPADRAO_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CATEGORIAIDS_FIELD_NUMBER: _ClassVar[int]
    STOCK_MOVEMENT_FIELD_NUMBER: _ClassVar[int]
    RENTABILIDADE_FIELD_NUMBER: _ClassVar[int]
    PARENT_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_VARIATION_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_INSUMOS_FIELD_NUMBER: _ClassVar[int]
    MARKUP_GTE_FIELD_NUMBER: _ClassVar[int]
    MARKUP_LTE_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    names: _containers.RepeatedScalarFieldContainer[str]
    eanCodes: _containers.RepeatedScalarFieldContainer[str]
    productCodes: _containers.RepeatedScalarFieldContainer[str]
    page_size: int
    page_token: str
    produto: _containers.RepeatedCompositeFieldContainer[Produto]
    codigoReferencia: str
    categoriaNome: str
    categoriaId: str
    fabricanteNome: str
    fabricanteId: str
    temCategoria: bool
    temFabricante: bool
    createdAtGte: _timestamp_pb2.Timestamp
    createdAtLte: _timestamp_pb2.Timestamp
    updatedAtGte: _timestamp_pb2.Timestamp
    updatedAtLte: _timestamp_pb2.Timestamp
    precoCustoGte: float
    precoCustoLte: float
    precoVendaAvistaGte: float
    precoVendaAvistaLte: float
    precoVendaAprazoGte: float
    precoVendaAprazoLte: float
    quantidadeGte: float
    quantidadeLte: float
    codigoProduto: _containers.RepeatedScalarFieldContainer[str]
    codigoBarra: _containers.RepeatedScalarFieldContainer[str]
    unidade: _containers.RepeatedScalarFieldContainer[str]
    ignoreSituacaoPadrao: bool
    situacao: str
    filter: _filter_pb2.Filter
    categoriaIds: _containers.RepeatedScalarFieldContainer[str]
    stock_movement: StockMovement
    rentabilidade: Rentabilidade
    parent_product_id: str
    include_variation_children: bool
    exclude_insumos: bool
    markup_gte: float
    markup_lte: float
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., names: _Optional[_Iterable[str]] = ..., eanCodes: _Optional[_Iterable[str]] = ..., productCodes: _Optional[_Iterable[str]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., produto: _Optional[_Iterable[_Union[Produto, _Mapping]]] = ..., codigoReferencia: _Optional[str] = ..., categoriaNome: _Optional[str] = ..., categoriaId: _Optional[str] = ..., fabricanteNome: _Optional[str] = ..., fabricanteId: _Optional[str] = ..., temCategoria: _Optional[bool] = ..., temFabricante: _Optional[bool] = ..., createdAtGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., createdAtLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAtGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAtLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., precoCustoGte: _Optional[float] = ..., precoCustoLte: _Optional[float] = ..., precoVendaAvistaGte: _Optional[float] = ..., precoVendaAvistaLte: _Optional[float] = ..., precoVendaAprazoGte: _Optional[float] = ..., precoVendaAprazoLte: _Optional[float] = ..., quantidadeGte: _Optional[float] = ..., quantidadeLte: _Optional[float] = ..., codigoProduto: _Optional[_Iterable[str]] = ..., codigoBarra: _Optional[_Iterable[str]] = ..., unidade: _Optional[_Iterable[str]] = ..., ignoreSituacaoPadrao: _Optional[bool] = ..., situacao: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., categoriaIds: _Optional[_Iterable[str]] = ..., stock_movement: _Optional[_Union[StockMovement, str]] = ..., rentabilidade: _Optional[_Union[Rentabilidade, str]] = ..., parent_product_id: _Optional[str] = ..., include_variation_children: _Optional[bool] = ..., exclude_insumos: _Optional[bool] = ..., markup_gte: _Optional[float] = ..., markup_lte: _Optional[float] = ...) -> None: ...

class ListProdutoResponse(_message.Message):
    __slots__ = ("produtoList", "next_page_token")
    PRODUTOLIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    produtoList: _containers.RepeatedCompositeFieldContainer[Produto]
    next_page_token: str
    def __init__(self, produtoList: _Optional[_Iterable[_Union[Produto, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class AddMovimentacaoEstoqueRequest(_message.Message):
    __slots__ = ("inputMovimento",)
    INPUTMOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    inputMovimento: _containers.RepeatedCompositeFieldContainer[InputMovimentoEstoque]
    def __init__(self, inputMovimento: _Optional[_Iterable[_Union[InputMovimentoEstoque, _Mapping]]] = ...) -> None: ...

class AddMovimentacaoEstoqueResponse(_message.Message):
    __slots__ = ("movimentoList",)
    MOVIMENTOLIST_FIELD_NUMBER: _ClassVar[int]
    movimentoList: _containers.RepeatedCompositeFieldContainer[_movimentoestoque_pb2.MovimentoEstoque]
    def __init__(self, movimentoList: _Optional[_Iterable[_Union[_movimentoestoque_pb2.MovimentoEstoque, _Mapping]]] = ...) -> None: ...

class GetMovimentacaoEstoqueRequest(_message.Message):
    __slots__ = ("produtoId", "tipoMovimento", "origem", "filter", "created_at_gte", "created_at_lte", "produtoIds")
    PRODUTOID_FIELD_NUMBER: _ClassVar[int]
    TIPOMOVIMENTO_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_GTE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_LTE_FIELD_NUMBER: _ClassVar[int]
    PRODUTOIDS_FIELD_NUMBER: _ClassVar[int]
    produtoId: str
    tipoMovimento: str
    origem: str
    filter: _filter_pb2.Filter
    created_at_gte: _timestamp_pb2.Timestamp
    created_at_lte: _timestamp_pb2.Timestamp
    produtoIds: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, produtoId: _Optional[str] = ..., tipoMovimento: _Optional[str] = ..., origem: _Optional[str] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., created_at_gte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., created_at_lte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., produtoIds: _Optional[_Iterable[str]] = ...) -> None: ...

class GetMovimentacaoEstoqueResponse(_message.Message):
    __slots__ = ("movimentoList",)
    MOVIMENTOLIST_FIELD_NUMBER: _ClassVar[int]
    movimentoList: _containers.RepeatedCompositeFieldContainer[_movimentoestoque_pb2.MovimentoEstoque]
    def __init__(self, movimentoList: _Optional[_Iterable[_Union[_movimentoestoque_pb2.MovimentoEstoque, _Mapping]]] = ...) -> None: ...

class GerarArquivoBalancaRequest(_message.Message):
    __slots__ = ("formato", "codigo_departamento", "tipo_venda", "dias_validade", "imprime_data_validade", "imprime_data_embalagem", "filter")
    FORMATO_FIELD_NUMBER: _ClassVar[int]
    CODIGO_DEPARTAMENTO_FIELD_NUMBER: _ClassVar[int]
    TIPO_VENDA_FIELD_NUMBER: _ClassVar[int]
    DIAS_VALIDADE_FIELD_NUMBER: _ClassVar[int]
    IMPRIME_DATA_VALIDADE_FIELD_NUMBER: _ClassVar[int]
    IMPRIME_DATA_EMBALAGEM_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    formato: str
    codigo_departamento: str
    tipo_venda: str
    dias_validade: int
    imprime_data_validade: bool
    imprime_data_embalagem: bool
    filter: _filter_pb2.Filter
    def __init__(self, formato: _Optional[str] = ..., codigo_departamento: _Optional[str] = ..., tipo_venda: _Optional[str] = ..., dias_validade: _Optional[int] = ..., imprime_data_validade: _Optional[bool] = ..., imprime_data_embalagem: _Optional[bool] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ...) -> None: ...

class GerarArquivoBalancaResponse(_message.Message):
    __slots__ = ("conteudoArquivo", "quantidadeProdutos")
    CONTEUDOARQUIVO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEPRODUTOS_FIELD_NUMBER: _ClassVar[int]
    conteudoArquivo: str
    quantidadeProdutos: int
    def __init__(self, conteudoArquivo: _Optional[str] = ..., quantidadeProdutos: _Optional[int] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("tipoRelatorio", "listProdutoRequest")
    TIPORELATORIO_FIELD_NUMBER: _ClassVar[int]
    LISTPRODUTOREQUEST_FIELD_NUMBER: _ClassVar[int]
    tipoRelatorio: str
    listProdutoRequest: ListProdutoRequest
    def __init__(self, tipoRelatorio: _Optional[str] = ..., listProdutoRequest: _Optional[_Union[ListProdutoRequest, _Mapping]] = ...) -> None: ...

class ReportResponse(_message.Message):
    __slots__ = ("response",)
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _report_pb2.Response
    def __init__(self, response: _Optional[_Union[_report_pb2.Response, _Mapping]] = ...) -> None: ...

class AjusteEstoque(_message.Message):
    __slots__ = ("produtoId", "quantidade", "variation_product_id")
    PRODUTOID_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    VARIATION_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    produtoId: str
    quantidade: float
    variation_product_id: str
    def __init__(self, produtoId: _Optional[str] = ..., quantidade: _Optional[float] = ..., variation_product_id: _Optional[str] = ...) -> None: ...

class AjustarEstoqueRequest(_message.Message):
    __slots__ = ("estoqueId", "pessoaId", "pessoaNome", "origemId", "origemNumero", "ajusteEstoque")
    ESTOQUEID_FIELD_NUMBER: _ClassVar[int]
    PESSOAID_FIELD_NUMBER: _ClassVar[int]
    PESSOANOME_FIELD_NUMBER: _ClassVar[int]
    ORIGEMID_FIELD_NUMBER: _ClassVar[int]
    ORIGEMNUMERO_FIELD_NUMBER: _ClassVar[int]
    AJUSTEESTOQUE_FIELD_NUMBER: _ClassVar[int]
    estoqueId: str
    pessoaId: str
    pessoaNome: str
    origemId: str
    origemNumero: str
    ajusteEstoque: _containers.RepeatedCompositeFieldContainer[AjusteEstoque]
    def __init__(self, estoqueId: _Optional[str] = ..., pessoaId: _Optional[str] = ..., pessoaNome: _Optional[str] = ..., origemId: _Optional[str] = ..., origemNumero: _Optional[str] = ..., ajusteEstoque: _Optional[_Iterable[_Union[AjusteEstoque, _Mapping]]] = ...) -> None: ...

class AjustarEstoqueResponse(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class ImportErrorGroup(_message.Message):
    __slots__ = ("errors",)
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    errors: _containers.RepeatedCompositeFieldContainer[ImportError]
    def __init__(self, errors: _Optional[_Iterable[_Union[ImportError, _Mapping]]] = ...) -> None: ...

class ImportError(_message.Message):
    __slots__ = ("product", "reason", "details")
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    product: str
    reason: str
    details: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, product: _Optional[str] = ..., reason: _Optional[str] = ..., details: _Optional[_Iterable[str]] = ...) -> None: ...

class AlteracaoCadastro(_message.Message):
    __slots__ = ("id", "nome")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ...) -> None: ...

class AlteracoesFiltro(_message.Message):
    __slots__ = ("ids", "fabricante", "categoria")
    IDS_FIELD_NUMBER: _ClassVar[int]
    FABRICANTE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    fabricante: AlteracaoCadastro
    categoria: AlteracaoCadastro
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., fabricante: _Optional[_Union[AlteracaoCadastro, _Mapping]] = ..., categoria: _Optional[_Union[AlteracaoCadastro, _Mapping]] = ...) -> None: ...

class AlteracoesConjuntasRequest(_message.Message):
    __slots__ = ("filtro", "fabricante", "categoria", "unidade", "fracionavel", "naoFracionavel", "situacao", "reprecificacao")
    FILTRO_FIELD_NUMBER: _ClassVar[int]
    FABRICANTE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    UNIDADE_FIELD_NUMBER: _ClassVar[int]
    FRACIONAVEL_FIELD_NUMBER: _ClassVar[int]
    NAOFRACIONAVEL_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    REPRECIFICACAO_FIELD_NUMBER: _ClassVar[int]
    filtro: AlteracoesFiltro
    fabricante: AlteracaoCadastro
    categoria: AlteracaoCadastro
    unidade: str
    fracionavel: bool
    naoFracionavel: bool
    situacao: str
    reprecificacao: ReprecificacaoConjunta
    def __init__(self, filtro: _Optional[_Union[AlteracoesFiltro, _Mapping]] = ..., fabricante: _Optional[_Union[AlteracaoCadastro, _Mapping]] = ..., categoria: _Optional[_Union[AlteracaoCadastro, _Mapping]] = ..., unidade: _Optional[str] = ..., fracionavel: _Optional[bool] = ..., naoFracionavel: _Optional[bool] = ..., situacao: _Optional[str] = ..., reprecificacao: _Optional[_Union[ReprecificacaoConjunta, _Mapping]] = ...) -> None: ...

class ReprecificacaoConjunta(_message.Message):
    __slots__ = ("recalcularPrecos", "margemLucro", "margemCusto", "margemComissao", "margemOutrasDespesas", "margemLucroAprazo", "margemDescontoAtacado", "margemSobreVenda", "reajusteCustoPercentual")
    RECALCULARPRECOS_FIELD_NUMBER: _ClassVar[int]
    MARGEMLUCRO_FIELD_NUMBER: _ClassVar[int]
    MARGEMCUSTO_FIELD_NUMBER: _ClassVar[int]
    MARGEMCOMISSAO_FIELD_NUMBER: _ClassVar[int]
    MARGEMOUTRASDESPESAS_FIELD_NUMBER: _ClassVar[int]
    MARGEMLUCROAPRAZO_FIELD_NUMBER: _ClassVar[int]
    MARGEMDESCONTOATACADO_FIELD_NUMBER: _ClassVar[int]
    MARGEMSOBREVENDA_FIELD_NUMBER: _ClassVar[int]
    REAJUSTECUSTOPERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    recalcularPrecos: bool
    margemLucro: float
    margemCusto: float
    margemComissao: float
    margemOutrasDespesas: float
    margemLucroAprazo: float
    margemDescontoAtacado: float
    margemSobreVenda: float
    reajusteCustoPercentual: float
    def __init__(self, recalcularPrecos: _Optional[bool] = ..., margemLucro: _Optional[float] = ..., margemCusto: _Optional[float] = ..., margemComissao: _Optional[float] = ..., margemOutrasDespesas: _Optional[float] = ..., margemLucroAprazo: _Optional[float] = ..., margemDescontoAtacado: _Optional[float] = ..., margemSobreVenda: _Optional[float] = ..., reajusteCustoPercentual: _Optional[float] = ...) -> None: ...

class AlteracoesConjuntasResponse(_message.Message):
    __slots__ = ("quantidadeAlterada", "status", "produtosSemCusto")
    QUANTIDADEALTERADA_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PRODUTOSSEMCUSTO_FIELD_NUMBER: _ClassVar[int]
    quantidadeAlterada: int
    status: str
    produtosSemCusto: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, quantidadeAlterada: _Optional[int] = ..., status: _Optional[str] = ..., produtosSemCusto: _Optional[_Iterable[str]] = ...) -> None: ...

class BatchInfo(_message.Message):
    __slots__ = ("id", "batch_number")
    ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_NUMBER_FIELD_NUMBER: _ClassVar[int]
    id: str
    batch_number: str
    def __init__(self, id: _Optional[str] = ..., batch_number: _Optional[str] = ...) -> None: ...

class SerialInfo(_message.Message):
    __slots__ = ("ids", "serial_numbers")
    IDS_FIELD_NUMBER: _ClassVar[int]
    SERIAL_NUMBERS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    serial_numbers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., serial_numbers: _Optional[_Iterable[str]] = ...) -> None: ...

class InputMovimentoEstoque(_message.Message):
    __slots__ = ("estoqueNome", "produtoId", "tipo", "quantidade", "valorUnitario", "origem", "origemId", "origemNumero", "obs", "pessoaId", "pessoaNome", "batch", "variation_product_id", "serial", "comodato", "atualiza_custo")
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
    BATCH_FIELD_NUMBER: _ClassVar[int]
    VARIATION_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    COMODATO_FIELD_NUMBER: _ClassVar[int]
    ATUALIZA_CUSTO_FIELD_NUMBER: _ClassVar[int]
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
    batch: BatchInfo
    variation_product_id: str
    serial: SerialInfo
    comodato: bool
    atualiza_custo: bool
    def __init__(self, estoqueNome: _Optional[str] = ..., produtoId: _Optional[str] = ..., tipo: _Optional[str] = ..., quantidade: _Optional[float] = ..., valorUnitario: _Optional[float] = ..., origem: _Optional[str] = ..., origemId: _Optional[str] = ..., origemNumero: _Optional[str] = ..., obs: _Optional[str] = ..., pessoaId: _Optional[str] = ..., pessoaNome: _Optional[str] = ..., batch: _Optional[_Union[BatchInfo, _Mapping]] = ..., variation_product_id: _Optional[str] = ..., serial: _Optional[_Union[SerialInfo, _Mapping]] = ..., comodato: _Optional[bool] = ..., atualiza_custo: _Optional[bool] = ...) -> None: ...

class AddMediaRequest(_message.Message):
    __slots__ = ("produto_id", "media")
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    produto_id: str
    media: ProductMedia
    def __init__(self, produto_id: _Optional[str] = ..., media: _Optional[_Union[ProductMedia, _Mapping]] = ...) -> None: ...

class AddMediaResponse(_message.Message):
    __slots__ = ("produto",)
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    produto: Produto
    def __init__(self, produto: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class UpdateMediaRequest(_message.Message):
    __slots__ = ("produto_id", "media_id", "media")
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    produto_id: str
    media_id: str
    media: ProductMedia
    def __init__(self, produto_id: _Optional[str] = ..., media_id: _Optional[str] = ..., media: _Optional[_Union[ProductMedia, _Mapping]] = ...) -> None: ...

class UpdateMediaResponse(_message.Message):
    __slots__ = ("produto",)
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    produto: Produto
    def __init__(self, produto: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class DeleteMediaRequest(_message.Message):
    __slots__ = ("produto_id", "media_id")
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    MEDIA_ID_FIELD_NUMBER: _ClassVar[int]
    produto_id: str
    media_id: str
    def __init__(self, produto_id: _Optional[str] = ..., media_id: _Optional[str] = ...) -> None: ...

class DeleteMediaResponse(_message.Message):
    __slots__ = ("produto",)
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    produto: Produto
    def __init__(self, produto: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class ImportProdutoRequest(_message.Message):
    __slots__ = ("produtos", "file_string", "file_name", "import_categoria", "import_fabricante", "update_if_exists", "validate_only", "overwrite_if_exists", "codigo_produto_externo")
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    FILE_STRING_FIELD_NUMBER: _ClassVar[int]
    FILE_NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_CATEGORIA_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FABRICANTE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_IF_EXISTS_FIELD_NUMBER: _ClassVar[int]
    CODIGO_PRODUTO_EXTERNO_FIELD_NUMBER: _ClassVar[int]
    produtos: _containers.RepeatedCompositeFieldContainer[Produto]
    file_string: str
    file_name: str
    import_categoria: bool
    import_fabricante: bool
    update_if_exists: bool
    validate_only: bool
    overwrite_if_exists: bool
    codigo_produto_externo: bool
    def __init__(self, produtos: _Optional[_Iterable[_Union[Produto, _Mapping]]] = ..., file_string: _Optional[str] = ..., file_name: _Optional[str] = ..., import_categoria: _Optional[bool] = ..., import_fabricante: _Optional[bool] = ..., update_if_exists: _Optional[bool] = ..., validate_only: _Optional[bool] = ..., overwrite_if_exists: _Optional[bool] = ..., codigo_produto_externo: _Optional[bool] = ...) -> None: ...

class ImportProdutoResponse(_message.Message):
    __slots__ = ("produtos", "result", "success", "failed", "total", "erros_by_category", "html_report")
    class ErrosByCategoryEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ImportErrorGroup
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ImportErrorGroup, _Mapping]] = ...) -> None: ...
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    FAILED_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    ERROS_BY_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    HTML_REPORT_FIELD_NUMBER: _ClassVar[int]
    produtos: _containers.RepeatedCompositeFieldContainer[Produto]
    result: str
    success: int
    failed: int
    total: int
    erros_by_category: _containers.MessageMap[str, ImportErrorGroup]
    html_report: str
    def __init__(self, produtos: _Optional[_Iterable[_Union[Produto, _Mapping]]] = ..., result: _Optional[str] = ..., success: _Optional[int] = ..., failed: _Optional[int] = ..., total: _Optional[int] = ..., erros_by_category: _Optional[_Mapping[str, ImportErrorGroup]] = ..., html_report: _Optional[str] = ...) -> None: ...

class GetProductsAdditionalDataRequest(_message.Message):
    __slots__ = ("product_ids",)
    PRODUCT_IDS_FIELD_NUMBER: _ClassVar[int]
    product_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, product_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class ProductAdditionalData(_message.Message):
    __slots__ = ("product_name", "category_id", "category_name", "manufacturer_id", "manufacturer_name")
    PRODUCT_NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_NAME_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_ID_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_NAME_FIELD_NUMBER: _ClassVar[int]
    product_name: str
    category_id: str
    category_name: str
    manufacturer_id: str
    manufacturer_name: str
    def __init__(self, product_name: _Optional[str] = ..., category_id: _Optional[str] = ..., category_name: _Optional[str] = ..., manufacturer_id: _Optional[str] = ..., manufacturer_name: _Optional[str] = ...) -> None: ...

class GetProductsAdditionalDataResponse(_message.Message):
    __slots__ = ("additional_data",)
    class AdditionalDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ProductAdditionalData
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ProductAdditionalData, _Mapping]] = ...) -> None: ...
    ADDITIONAL_DATA_FIELD_NUMBER: _ClassVar[int]
    additional_data: _containers.MessageMap[str, ProductAdditionalData]
    def __init__(self, additional_data: _Optional[_Mapping[str, ProductAdditionalData]] = ...) -> None: ...

class CorrecaoMovimentacaoRequest(_message.Message):
    __slots__ = ("produto_origem_id", "produto_origem_quantidade", "produto_destino_id", "produto_destino_quantidade", "estoque_origem_id", "estoque_destino_id", "movimentoList")
    PRODUTO_ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ORIGEM_QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_DESTINO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_DESTINO_QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    ESTOQUE_ORIGEM_ID_FIELD_NUMBER: _ClassVar[int]
    ESTOQUE_DESTINO_ID_FIELD_NUMBER: _ClassVar[int]
    MOVIMENTOLIST_FIELD_NUMBER: _ClassVar[int]
    produto_origem_id: str
    produto_origem_quantidade: float
    produto_destino_id: str
    produto_destino_quantidade: float
    estoque_origem_id: str
    estoque_destino_id: str
    movimentoList: _containers.RepeatedCompositeFieldContainer[_movimentoestoque_pb2.MovimentoEstoque]
    def __init__(self, produto_origem_id: _Optional[str] = ..., produto_origem_quantidade: _Optional[float] = ..., produto_destino_id: _Optional[str] = ..., produto_destino_quantidade: _Optional[float] = ..., estoque_origem_id: _Optional[str] = ..., estoque_destino_id: _Optional[str] = ..., movimentoList: _Optional[_Iterable[_Union[_movimentoestoque_pb2.MovimentoEstoque, _Mapping]]] = ...) -> None: ...

class CorrecaoMovimentacaoResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExportProductsRequest(_message.Message):
    __slots__ = ("format", "filter", "include_metadata")
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_METADATA_FIELD_NUMBER: _ClassVar[int]
    format: _exports_pb2.ExportFormat
    filter: _filter_pb2.Filter
    include_metadata: bool
    def __init__(self, format: _Optional[_Union[_exports_pb2.ExportFormat, str]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., include_metadata: _Optional[bool] = ...) -> None: ...

class ExportProductsResponse(_message.Message):
    __slots__ = ("export",)
    EXPORT_FIELD_NUMBER: _ClassVar[int]
    export: _exports_pb2.ExportResponse
    def __init__(self, export: _Optional[_Union[_exports_pb2.ExportResponse, _Mapping]] = ...) -> None: ...

class CloneProdutoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class CloneProdutoResponse(_message.Message):
    __slots__ = ("produto",)
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    produto: Produto
    def __init__(self, produto: _Optional[_Union[Produto, _Mapping]] = ...) -> None: ...

class GenerateSeoMetaRequest(_message.Message):
    __slots__ = ("id", "additional_instructions")
    ID_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_INSTRUCTIONS_FIELD_NUMBER: _ClassVar[int]
    id: str
    additional_instructions: str
    def __init__(self, id: _Optional[str] = ..., additional_instructions: _Optional[str] = ...) -> None: ...

class GenerateSeoMetaResponse(_message.Message):
    __slots__ = ("meta_title", "meta_description", "slug", "keywords")
    META_TITLE_FIELD_NUMBER: _ClassVar[int]
    META_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SLUG_FIELD_NUMBER: _ClassVar[int]
    KEYWORDS_FIELD_NUMBER: _ClassVar[int]
    meta_title: str
    meta_description: str
    slug: str
    keywords: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, meta_title: _Optional[str] = ..., meta_description: _Optional[str] = ..., slug: _Optional[str] = ..., keywords: _Optional[_Iterable[str]] = ...) -> None: ...

class GetEstoqueGrupoRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class EstoqueEmpresa(_message.Message):
    __slots__ = ("org_id", "org_nome", "estoques", "quantidade_total")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_NOME_FIELD_NUMBER: _ClassVar[int]
    ESTOQUES_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_TOTAL_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    org_nome: str
    estoques: _containers.RepeatedCompositeFieldContainer[Estoque]
    quantidade_total: float
    def __init__(self, org_id: _Optional[str] = ..., org_nome: _Optional[str] = ..., estoques: _Optional[_Iterable[_Union[Estoque, _Mapping]]] = ..., quantidade_total: _Optional[float] = ...) -> None: ...

class GetEstoqueGrupoResponse(_message.Message):
    __slots__ = ("empresas",)
    EMPRESAS_FIELD_NUMBER: _ClassVar[int]
    empresas: _containers.RepeatedCompositeFieldContainer[EstoqueEmpresa]
    def __init__(self, empresas: _Optional[_Iterable[_Union[EstoqueEmpresa, _Mapping]]] = ...) -> None: ...
