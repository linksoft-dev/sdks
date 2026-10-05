import datetime

from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from linksoft_sdk.pb.plugins.validate import validate_pb2 as _validate_pb2
from linksoft_sdk.pb.plugins.service import service_pb2 as _service_pb2
from linksoft_sdk.pb.filter import filter_pb2 as _filter_pb2
from linksoft_sdk.pb.common.metadata import metadata_pb2 as _metadata_pb2
from linksoft_sdk.pb.apps.dfe.emitente import emitente_pb2 as _emitente_pb2
from linksoft_sdk.pb.apps.report import report_pb2 as _report_pb2
from linksoft_sdk.pb.apps.dfe.nfe import impostos_pb2 as _impostos_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tipo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIPO_UNSPECIFIED: _ClassVar[Tipo]
    TIPO_NFE: _ClassVar[Tipo]
    TIPO_NFCE: _ClassVar[Tipo]
    TIPO_NFE_ENTRADA: _ClassVar[Tipo]
    TIPO_DFE_ALL: _ClassVar[Tipo]

class DanfeTipo(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DANFE_TIPO_UNSPECIFIED: _ClassVar[DanfeTipo]
    DANFE_TIPO_PDF: _ClassVar[DanfeTipo]
    DANFE_TIPO_HTML: _ClassVar[DanfeTipo]
    DANFE_TIPO_REPORT: _ClassVar[DanfeTipo]
TIPO_UNSPECIFIED: Tipo
TIPO_NFE: Tipo
TIPO_NFCE: Tipo
TIPO_NFE_ENTRADA: Tipo
TIPO_DFE_ALL: Tipo
DANFE_TIPO_UNSPECIFIED: DanfeTipo
DANFE_TIPO_PDF: DanfeTipo
DANFE_TIPO_HTML: DanfeTipo
DANFE_TIPO_REPORT: DanfeTipo

class CreateNfeRequest(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class CreateNfeResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class UpdateNfeRequest(_message.Message):
    __slots__ = ("id", "nfe", "update_mask")
    ID_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    id: str
    nfe: Nfe
    update_mask: _metadata_pb2.FieldMask
    def __init__(self, id: _Optional[str] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ..., update_mask: _Optional[_Union[_metadata_pb2.FieldMask, _Mapping]] = ...) -> None: ...

class UpdateNfeResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class DeleteNfeRequest(_message.Message):
    __slots__ = ("id", "hard")
    ID_FIELD_NUMBER: _ClassVar[int]
    HARD_FIELD_NUMBER: _ClassVar[int]
    id: str
    hard: bool
    def __init__(self, id: _Optional[str] = ..., hard: _Optional[bool] = ...) -> None: ...

class DeleteNfeResponse(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetNfeRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetNfeResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class ListNfeRequest(_message.Message):
    __slots__ = ("ids", "chaves", "situacoes", "in_nfe_origens", "formaEmissao", "dataHoraEmissaoGte", "dataHoraEmissaoLte", "entradaDataHoraAceiteRejeicaoGte", "entradaDataHoraAceiteRejeicaoLte", "filter", "tipos", "page_size", "page_token", "tipoOperacao", "ignorarNotaReimpressao", "produtoId", "pessoaId", "totalNotaGte", "totalNotaLte", "totalIcmsGte", "totalIcmsLte", "totalIpiGte", "totalIpiLte", "totalPisGte", "totalPisLte", "totalCofinsGte", "totalCofinsLte", "cfops", "cstsIcms", "cstsIpi", "cstsPis", "cstsCofins")
    IDS_FIELD_NUMBER: _ClassVar[int]
    CHAVES_FIELD_NUMBER: _ClassVar[int]
    SITUACOES_FIELD_NUMBER: _ClassVar[int]
    IN_NFE_ORIGENS_FIELD_NUMBER: _ClassVar[int]
    FORMAEMISSAO_FIELD_NUMBER: _ClassVar[int]
    DATAHORAEMISSAOGTE_FIELD_NUMBER: _ClassVar[int]
    DATAHORAEMISSAOLTE_FIELD_NUMBER: _ClassVar[int]
    ENTRADADATAHORAACEITEREJEICAOGTE_FIELD_NUMBER: _ClassVar[int]
    ENTRADADATAHORAACEITEREJEICAOLTE_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    TIPOS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TIPOOPERACAO_FIELD_NUMBER: _ClassVar[int]
    IGNORARNOTAREIMPRESSAO_FIELD_NUMBER: _ClassVar[int]
    PRODUTOID_FIELD_NUMBER: _ClassVar[int]
    PESSOAID_FIELD_NUMBER: _ClassVar[int]
    TOTALNOTAGTE_FIELD_NUMBER: _ClassVar[int]
    TOTALNOTALTE_FIELD_NUMBER: _ClassVar[int]
    TOTALICMSGTE_FIELD_NUMBER: _ClassVar[int]
    TOTALICMSLTE_FIELD_NUMBER: _ClassVar[int]
    TOTALIPIGTE_FIELD_NUMBER: _ClassVar[int]
    TOTALIPILTE_FIELD_NUMBER: _ClassVar[int]
    TOTALPISGTE_FIELD_NUMBER: _ClassVar[int]
    TOTALPISLTE_FIELD_NUMBER: _ClassVar[int]
    TOTALCOFINSGTE_FIELD_NUMBER: _ClassVar[int]
    TOTALCOFINSLTE_FIELD_NUMBER: _ClassVar[int]
    CFOPS_FIELD_NUMBER: _ClassVar[int]
    CSTSICMS_FIELD_NUMBER: _ClassVar[int]
    CSTSIPI_FIELD_NUMBER: _ClassVar[int]
    CSTSPIS_FIELD_NUMBER: _ClassVar[int]
    CSTSCOFINS_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    chaves: _containers.RepeatedScalarFieldContainer[str]
    situacoes: _containers.RepeatedScalarFieldContainer[str]
    in_nfe_origens: _containers.RepeatedScalarFieldContainer[str]
    formaEmissao: str
    dataHoraEmissaoGte: _timestamp_pb2.Timestamp
    dataHoraEmissaoLte: _timestamp_pb2.Timestamp
    entradaDataHoraAceiteRejeicaoGte: _timestamp_pb2.Timestamp
    entradaDataHoraAceiteRejeicaoLte: _timestamp_pb2.Timestamp
    filter: _filter_pb2.Filter
    tipos: _containers.RepeatedScalarFieldContainer[Tipo]
    page_size: int
    page_token: str
    tipoOperacao: str
    ignorarNotaReimpressao: bool
    produtoId: str
    pessoaId: str
    totalNotaGte: float
    totalNotaLte: float
    totalIcmsGte: float
    totalIcmsLte: float
    totalIpiGte: float
    totalIpiLte: float
    totalPisGte: float
    totalPisLte: float
    totalCofinsGte: float
    totalCofinsLte: float
    cfops: _containers.RepeatedScalarFieldContainer[str]
    cstsIcms: _containers.RepeatedScalarFieldContainer[str]
    cstsIpi: _containers.RepeatedScalarFieldContainer[str]
    cstsPis: _containers.RepeatedScalarFieldContainer[str]
    cstsCofins: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., chaves: _Optional[_Iterable[str]] = ..., situacoes: _Optional[_Iterable[str]] = ..., in_nfe_origens: _Optional[_Iterable[str]] = ..., formaEmissao: _Optional[str] = ..., dataHoraEmissaoGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraEmissaoLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., entradaDataHoraAceiteRejeicaoGte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., entradaDataHoraAceiteRejeicaoLte: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., filter: _Optional[_Union[_filter_pb2.Filter, _Mapping]] = ..., tipos: _Optional[_Iterable[_Union[Tipo, str]]] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., tipoOperacao: _Optional[str] = ..., ignorarNotaReimpressao: _Optional[bool] = ..., produtoId: _Optional[str] = ..., pessoaId: _Optional[str] = ..., totalNotaGte: _Optional[float] = ..., totalNotaLte: _Optional[float] = ..., totalIcmsGte: _Optional[float] = ..., totalIcmsLte: _Optional[float] = ..., totalIpiGte: _Optional[float] = ..., totalIpiLte: _Optional[float] = ..., totalPisGte: _Optional[float] = ..., totalPisLte: _Optional[float] = ..., totalCofinsGte: _Optional[float] = ..., totalCofinsLte: _Optional[float] = ..., cfops: _Optional[_Iterable[str]] = ..., cstsIcms: _Optional[_Iterable[str]] = ..., cstsIpi: _Optional[_Iterable[str]] = ..., cstsPis: _Optional[_Iterable[str]] = ..., cstsCofins: _Optional[_Iterable[str]] = ...) -> None: ...

class ListNfeResponse(_message.Message):
    __slots__ = ("nfeList", "next_page_token")
    NFELIST_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    nfeList: _containers.RepeatedCompositeFieldContainer[Nfe]
    next_page_token: str
    def __init__(self, nfeList: _Optional[_Iterable[_Union[Nfe, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class Nfe(_message.Message):
    __slots__ = ("created_at", "updated_at", "user_id", "user_name", "id", "fields", "account_id", "situacao", "emitente", "pessoa", "tipo", "tipo_ambiente", "tipo_operacao", "finalidade_emissao", "natureza_operacao", "entrada_cadastra_produto_nao_vinculado", "entrada_aplica_calculo_venda_custo", "entrada_motivo_rejeicao", "entrada_data_hora_aceite_rejeicao", "entrada_alteracao_preco", "numero", "serie", "chave", "nfe_origem", "nfe_origens", "id_devolucao", "url_danfe", "protocolo", "data_hora_autorizacao", "data_hora_emissao", "data_hora_saida", "obs", "qrcode", "importada", "protocolo_cancelamento", "motivo_cancelamento", "data_hora_cancelamento", "cancelamento_usuario_id", "cancelamento_usuario_nome", "historico", "forma_emissao", "forma_emissao_descricao", "sequencia_evento", "contingencia_data_hora", "contingencia_motivo", "contingencia_nfe_numero_vinculada", "contingencia_nfe_serie_vinculada", "contingencia_processada_em", "xml_autorizacao", "xml_cancelamento", "xml_cancelamento_evento", "rejeicoes", "total_icms_credito", "icms_credito_aliquota", "transp_mod_frete", "transporte", "transp_id", "transp_cpf_cnpj", "transp_nome", "transp_ie", "transp_endereco", "transp_municipio", "transp_uf", "transp_veic_placa", "transp_veic_uf", "transp_veic_rntc", "transp_quantidade", "transp_especie", "transp_marca", "transp_numeracao_volumes", "transp_peso_liquido", "transp_peso_bruto", "valor_seguro", "total_seguro", "valor_frete", "total_frete", "valor_outras_despesas", "total_outras_despesas", "desconto_valor", "desconto_percentual", "subtotal_produtos", "total_desconto_produtos", "subtotal", "total", "total_pago", "total_tributos", "ibs_cbs_habilitado", "impostos", "valor_icms", "valor_icms_bc", "valor_icms_desoneracao", "valor_icms_st", "valor_icms_st_bc", "valor_ipi", "valor_pis", "valor_cofins", "valor_icms_intere_fcp", "valor_icms_intere_destino", "valor_icms_intere_origem", "totais", "produtos", "pagamentos", "duplicatas", "volumes", "referencias", "eventos", "entrada_data_hora_consulta_sefaz", "tipo_nota_debito", "tipo_nota_credito", "pag_antecipado_refs", "idempotency_key", "entrada_ia_vinculo_executado")
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    EMITENTE_FIELD_NUMBER: _ClassVar[int]
    PESSOA_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    TIPO_AMBIENTE_FIELD_NUMBER: _ClassVar[int]
    TIPO_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    FINALIDADE_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    NATUREZA_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_CADASTRA_PRODUTO_NAO_VINCULADO_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_APLICA_CALCULO_VENDA_CUSTO_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_MOTIVO_REJEICAO_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_DATA_HORA_ACEITE_REJEICAO_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_ALTERACAO_PRECO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    SERIE_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    NFE_ORIGEM_FIELD_NUMBER: _ClassVar[int]
    NFE_ORIGENS_FIELD_NUMBER: _ClassVar[int]
    ID_DEVOLUCAO_FIELD_NUMBER: _ClassVar[int]
    URL_DANFE_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_AUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_SAIDA_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    QRCODE_FIELD_NUMBER: _ClassVar[int]
    IMPORTADA_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_USUARIO_ID_FIELD_NUMBER: _ClassVar[int]
    CANCELAMENTO_USUARIO_NOME_FIELD_NUMBER: _ClassVar[int]
    HISTORICO_FIELD_NUMBER: _ClassVar[int]
    FORMA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    FORMA_EMISSAO_DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    SEQUENCIA_EVENTO_FIELD_NUMBER: _ClassVar[int]
    CONTINGENCIA_DATA_HORA_FIELD_NUMBER: _ClassVar[int]
    CONTINGENCIA_MOTIVO_FIELD_NUMBER: _ClassVar[int]
    CONTINGENCIA_NFE_NUMERO_VINCULADA_FIELD_NUMBER: _ClassVar[int]
    CONTINGENCIA_NFE_SERIE_VINCULADA_FIELD_NUMBER: _ClassVar[int]
    CONTINGENCIA_PROCESSADA_EM_FIELD_NUMBER: _ClassVar[int]
    XML_AUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    XML_CANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    XML_CANCELAMENTO_EVENTO_FIELD_NUMBER: _ClassVar[int]
    REJEICOES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_ICMS_CREDITO_FIELD_NUMBER: _ClassVar[int]
    ICMS_CREDITO_ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    TRANSP_MOD_FRETE_FIELD_NUMBER: _ClassVar[int]
    TRANSPORTE_FIELD_NUMBER: _ClassVar[int]
    TRANSP_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSP_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    TRANSP_NOME_FIELD_NUMBER: _ClassVar[int]
    TRANSP_IE_FIELD_NUMBER: _ClassVar[int]
    TRANSP_ENDERECO_FIELD_NUMBER: _ClassVar[int]
    TRANSP_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    TRANSP_UF_FIELD_NUMBER: _ClassVar[int]
    TRANSP_VEIC_PLACA_FIELD_NUMBER: _ClassVar[int]
    TRANSP_VEIC_UF_FIELD_NUMBER: _ClassVar[int]
    TRANSP_VEIC_RNTC_FIELD_NUMBER: _ClassVar[int]
    TRANSP_QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    TRANSP_ESPECIE_FIELD_NUMBER: _ClassVar[int]
    TRANSP_MARCA_FIELD_NUMBER: _ClassVar[int]
    TRANSP_NUMERACAO_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    TRANSP_PESO_LIQUIDO_FIELD_NUMBER: _ClassVar[int]
    TRANSP_PESO_BRUTO_FIELD_NUMBER: _ClassVar[int]
    VALOR_SEGURO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SEGURO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FRETE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FRETE_FIELD_NUMBER: _ClassVar[int]
    VALOR_OUTRAS_DESPESAS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_OUTRAS_DESPESAS_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_VALOR_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DESCONTO_PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PAGO_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TRIBUTOS_FIELD_NUMBER: _ClassVar[int]
    IBS_CBS_HABILITADO_FIELD_NUMBER: _ClassVar[int]
    IMPOSTOS_FIELD_NUMBER: _ClassVar[int]
    VALOR_ICMS_FIELD_NUMBER: _ClassVar[int]
    VALOR_ICMS_BC_FIELD_NUMBER: _ClassVar[int]
    VALOR_ICMS_DESONERACAO_FIELD_NUMBER: _ClassVar[int]
    VALOR_ICMS_ST_FIELD_NUMBER: _ClassVar[int]
    VALOR_ICMS_ST_BC_FIELD_NUMBER: _ClassVar[int]
    VALOR_IPI_FIELD_NUMBER: _ClassVar[int]
    VALOR_PIS_FIELD_NUMBER: _ClassVar[int]
    VALOR_COFINS_FIELD_NUMBER: _ClassVar[int]
    VALOR_ICMS_INTERE_FCP_FIELD_NUMBER: _ClassVar[int]
    VALOR_ICMS_INTERE_DESTINO_FIELD_NUMBER: _ClassVar[int]
    VALOR_ICMS_INTERE_ORIGEM_FIELD_NUMBER: _ClassVar[int]
    TOTAIS_FIELD_NUMBER: _ClassVar[int]
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTOS_FIELD_NUMBER: _ClassVar[int]
    DUPLICATAS_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    REFERENCIAS_FIELD_NUMBER: _ClassVar[int]
    EVENTOS_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_DATA_HORA_CONSULTA_SEFAZ_FIELD_NUMBER: _ClassVar[int]
    TIPO_NOTA_DEBITO_FIELD_NUMBER: _ClassVar[int]
    TIPO_NOTA_CREDITO_FIELD_NUMBER: _ClassVar[int]
    PAG_ANTECIPADO_REFS_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_IA_VINCULO_EXECUTADO_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    id: str
    fields: _metadata_pb2.BasicFields
    account_id: str
    situacao: str
    emitente: _emitente_pb2.Emitente
    pessoa: Pessoa
    tipo: str
    tipo_ambiente: str
    tipo_operacao: str
    finalidade_emissao: str
    natureza_operacao: str
    entrada_cadastra_produto_nao_vinculado: str
    entrada_aplica_calculo_venda_custo: bool
    entrada_motivo_rejeicao: str
    entrada_data_hora_aceite_rejeicao: _timestamp_pb2.Timestamp
    entrada_alteracao_preco: bool
    numero: int
    serie: int
    chave: str
    nfe_origem: str
    nfe_origens: _containers.RepeatedScalarFieldContainer[str]
    id_devolucao: str
    url_danfe: str
    protocolo: str
    data_hora_autorizacao: _timestamp_pb2.Timestamp
    data_hora_emissao: _timestamp_pb2.Timestamp
    data_hora_saida: _timestamp_pb2.Timestamp
    obs: str
    qrcode: str
    importada: bool
    protocolo_cancelamento: str
    motivo_cancelamento: str
    data_hora_cancelamento: _timestamp_pb2.Timestamp
    cancelamento_usuario_id: str
    cancelamento_usuario_nome: str
    historico: str
    forma_emissao: str
    forma_emissao_descricao: str
    sequencia_evento: int
    contingencia_data_hora: _timestamp_pb2.Timestamp
    contingencia_motivo: str
    contingencia_nfe_numero_vinculada: int
    contingencia_nfe_serie_vinculada: int
    contingencia_processada_em: _timestamp_pb2.Timestamp
    xml_autorizacao: str
    xml_cancelamento: str
    xml_cancelamento_evento: str
    rejeicoes: _containers.RepeatedCompositeFieldContainer[Rejeicao]
    total_icms_credito: float
    icms_credito_aliquota: float
    transp_mod_frete: str
    transporte: TranspDados
    transp_id: str
    transp_cpf_cnpj: str
    transp_nome: str
    transp_ie: str
    transp_endereco: str
    transp_municipio: str
    transp_uf: str
    transp_veic_placa: str
    transp_veic_uf: str
    transp_veic_rntc: str
    transp_quantidade: int
    transp_especie: str
    transp_marca: str
    transp_numeracao_volumes: str
    transp_peso_liquido: float
    transp_peso_bruto: float
    valor_seguro: float
    total_seguro: float
    valor_frete: float
    total_frete: float
    valor_outras_despesas: float
    total_outras_despesas: float
    desconto_valor: float
    desconto_percentual: float
    subtotal_produtos: float
    total_desconto_produtos: float
    subtotal: float
    total: float
    total_pago: float
    total_tributos: float
    ibs_cbs_habilitado: bool
    impostos: Impostos
    valor_icms: float
    valor_icms_bc: float
    valor_icms_desoneracao: float
    valor_icms_st: float
    valor_icms_st_bc: float
    valor_ipi: float
    valor_pis: float
    valor_cofins: float
    valor_icms_intere_fcp: float
    valor_icms_intere_destino: float
    valor_icms_intere_origem: float
    totais: _impostos_pb2.Totais
    produtos: _containers.RepeatedCompositeFieldContainer[ItemModel]
    pagamentos: _containers.RepeatedCompositeFieldContainer[PagamentoModel]
    duplicatas: _containers.RepeatedCompositeFieldContainer[DuplicataModel]
    volumes: _containers.RepeatedCompositeFieldContainer[VolumesModel]
    referencias: _containers.RepeatedCompositeFieldContainer[ReferenciaModel]
    eventos: _containers.RepeatedCompositeFieldContainer[Evento]
    entrada_data_hora_consulta_sefaz: _timestamp_pb2.Timestamp
    tipo_nota_debito: str
    tipo_nota_credito: str
    pag_antecipado_refs: _containers.RepeatedScalarFieldContainer[str]
    idempotency_key: str
    entrada_ia_vinculo_executado: bool
    def __init__(self, created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., id: _Optional[str] = ..., fields: _Optional[_Union[_metadata_pb2.BasicFields, _Mapping]] = ..., account_id: _Optional[str] = ..., situacao: _Optional[str] = ..., emitente: _Optional[_Union[_emitente_pb2.Emitente, _Mapping]] = ..., pessoa: _Optional[_Union[Pessoa, _Mapping]] = ..., tipo: _Optional[str] = ..., tipo_ambiente: _Optional[str] = ..., tipo_operacao: _Optional[str] = ..., finalidade_emissao: _Optional[str] = ..., natureza_operacao: _Optional[str] = ..., entrada_cadastra_produto_nao_vinculado: _Optional[str] = ..., entrada_aplica_calculo_venda_custo: _Optional[bool] = ..., entrada_motivo_rejeicao: _Optional[str] = ..., entrada_data_hora_aceite_rejeicao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., entrada_alteracao_preco: _Optional[bool] = ..., numero: _Optional[int] = ..., serie: _Optional[int] = ..., chave: _Optional[str] = ..., nfe_origem: _Optional[str] = ..., nfe_origens: _Optional[_Iterable[str]] = ..., id_devolucao: _Optional[str] = ..., url_danfe: _Optional[str] = ..., protocolo: _Optional[str] = ..., data_hora_autorizacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_emissao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_saida: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., obs: _Optional[str] = ..., qrcode: _Optional[str] = ..., importada: _Optional[bool] = ..., protocolo_cancelamento: _Optional[str] = ..., motivo_cancelamento: _Optional[str] = ..., data_hora_cancelamento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cancelamento_usuario_id: _Optional[str] = ..., cancelamento_usuario_nome: _Optional[str] = ..., historico: _Optional[str] = ..., forma_emissao: _Optional[str] = ..., forma_emissao_descricao: _Optional[str] = ..., sequencia_evento: _Optional[int] = ..., contingencia_data_hora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., contingencia_motivo: _Optional[str] = ..., contingencia_nfe_numero_vinculada: _Optional[int] = ..., contingencia_nfe_serie_vinculada: _Optional[int] = ..., contingencia_processada_em: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., xml_autorizacao: _Optional[str] = ..., xml_cancelamento: _Optional[str] = ..., xml_cancelamento_evento: _Optional[str] = ..., rejeicoes: _Optional[_Iterable[_Union[Rejeicao, _Mapping]]] = ..., total_icms_credito: _Optional[float] = ..., icms_credito_aliquota: _Optional[float] = ..., transp_mod_frete: _Optional[str] = ..., transporte: _Optional[_Union[TranspDados, _Mapping]] = ..., transp_id: _Optional[str] = ..., transp_cpf_cnpj: _Optional[str] = ..., transp_nome: _Optional[str] = ..., transp_ie: _Optional[str] = ..., transp_endereco: _Optional[str] = ..., transp_municipio: _Optional[str] = ..., transp_uf: _Optional[str] = ..., transp_veic_placa: _Optional[str] = ..., transp_veic_uf: _Optional[str] = ..., transp_veic_rntc: _Optional[str] = ..., transp_quantidade: _Optional[int] = ..., transp_especie: _Optional[str] = ..., transp_marca: _Optional[str] = ..., transp_numeracao_volumes: _Optional[str] = ..., transp_peso_liquido: _Optional[float] = ..., transp_peso_bruto: _Optional[float] = ..., valor_seguro: _Optional[float] = ..., total_seguro: _Optional[float] = ..., valor_frete: _Optional[float] = ..., total_frete: _Optional[float] = ..., valor_outras_despesas: _Optional[float] = ..., total_outras_despesas: _Optional[float] = ..., desconto_valor: _Optional[float] = ..., desconto_percentual: _Optional[float] = ..., subtotal_produtos: _Optional[float] = ..., total_desconto_produtos: _Optional[float] = ..., subtotal: _Optional[float] = ..., total: _Optional[float] = ..., total_pago: _Optional[float] = ..., total_tributos: _Optional[float] = ..., ibs_cbs_habilitado: _Optional[bool] = ..., impostos: _Optional[_Union[Impostos, _Mapping]] = ..., valor_icms: _Optional[float] = ..., valor_icms_bc: _Optional[float] = ..., valor_icms_desoneracao: _Optional[float] = ..., valor_icms_st: _Optional[float] = ..., valor_icms_st_bc: _Optional[float] = ..., valor_ipi: _Optional[float] = ..., valor_pis: _Optional[float] = ..., valor_cofins: _Optional[float] = ..., valor_icms_intere_fcp: _Optional[float] = ..., valor_icms_intere_destino: _Optional[float] = ..., valor_icms_intere_origem: _Optional[float] = ..., totais: _Optional[_Union[_impostos_pb2.Totais, _Mapping]] = ..., produtos: _Optional[_Iterable[_Union[ItemModel, _Mapping]]] = ..., pagamentos: _Optional[_Iterable[_Union[PagamentoModel, _Mapping]]] = ..., duplicatas: _Optional[_Iterable[_Union[DuplicataModel, _Mapping]]] = ..., volumes: _Optional[_Iterable[_Union[VolumesModel, _Mapping]]] = ..., referencias: _Optional[_Iterable[_Union[ReferenciaModel, _Mapping]]] = ..., eventos: _Optional[_Iterable[_Union[Evento, _Mapping]]] = ..., entrada_data_hora_consulta_sefaz: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tipo_nota_debito: _Optional[str] = ..., tipo_nota_credito: _Optional[str] = ..., pag_antecipado_refs: _Optional[_Iterable[str]] = ..., idempotency_key: _Optional[str] = ..., entrada_ia_vinculo_executado: _Optional[bool] = ...) -> None: ...

class Pessoa(_message.Message):
    __slots__ = ("id", "nome", "nome2", "cpfCnpj", "ie", "contribuinte", "revenda", "isentoIe", "endCep", "endEndereco", "endNumero", "endBairro", "endCidade", "endCidadeCod", "endUf", "endComplemento", "telefone", "email", "enviarNfePorEmail")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOME_FIELD_NUMBER: _ClassVar[int]
    NOME2_FIELD_NUMBER: _ClassVar[int]
    CPFCNPJ_FIELD_NUMBER: _ClassVar[int]
    IE_FIELD_NUMBER: _ClassVar[int]
    CONTRIBUINTE_FIELD_NUMBER: _ClassVar[int]
    REVENDA_FIELD_NUMBER: _ClassVar[int]
    ISENTOIE_FIELD_NUMBER: _ClassVar[int]
    ENDCEP_FIELD_NUMBER: _ClassVar[int]
    ENDENDERECO_FIELD_NUMBER: _ClassVar[int]
    ENDNUMERO_FIELD_NUMBER: _ClassVar[int]
    ENDBAIRRO_FIELD_NUMBER: _ClassVar[int]
    ENDCIDADE_FIELD_NUMBER: _ClassVar[int]
    ENDCIDADECOD_FIELD_NUMBER: _ClassVar[int]
    ENDUF_FIELD_NUMBER: _ClassVar[int]
    ENDCOMPLEMENTO_FIELD_NUMBER: _ClassVar[int]
    TELEFONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ENVIARNFEPOREMAIL_FIELD_NUMBER: _ClassVar[int]
    id: str
    nome: str
    nome2: str
    cpfCnpj: str
    ie: str
    contribuinte: bool
    revenda: bool
    isentoIe: bool
    endCep: str
    endEndereco: str
    endNumero: str
    endBairro: str
    endCidade: str
    endCidadeCod: str
    endUf: str
    endComplemento: str
    telefone: str
    email: str
    enviarNfePorEmail: bool
    def __init__(self, id: _Optional[str] = ..., nome: _Optional[str] = ..., nome2: _Optional[str] = ..., cpfCnpj: _Optional[str] = ..., ie: _Optional[str] = ..., contribuinte: _Optional[bool] = ..., revenda: _Optional[bool] = ..., isentoIe: _Optional[bool] = ..., endCep: _Optional[str] = ..., endEndereco: _Optional[str] = ..., endNumero: _Optional[str] = ..., endBairro: _Optional[str] = ..., endCidade: _Optional[str] = ..., endCidadeCod: _Optional[str] = ..., endUf: _Optional[str] = ..., endComplemento: _Optional[str] = ..., telefone: _Optional[str] = ..., email: _Optional[str] = ..., enviarNfePorEmail: _Optional[bool] = ...) -> None: ...

class Rejeicao(_message.Message):
    __slots__ = ("id", "dataHora", "dataHoraSituacaoDoc", "cstat", "mensagem")
    ID_FIELD_NUMBER: _ClassVar[int]
    DATAHORA_FIELD_NUMBER: _ClassVar[int]
    DATAHORASITUACAODOC_FIELD_NUMBER: _ClassVar[int]
    CSTAT_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    id: str
    dataHora: _timestamp_pb2.Timestamp
    dataHoraSituacaoDoc: _timestamp_pb2.Timestamp
    cstat: str
    mensagem: str
    def __init__(self, id: _Optional[str] = ..., dataHora: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataHoraSituacaoDoc: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., cstat: _Optional[str] = ..., mensagem: _Optional[str] = ...) -> None: ...

class TranspDados(_message.Message):
    __slots__ = ("transpId", "transpCpfCnpj", "transpNome", "transpIe", "transpEndereco", "transpMunicipio", "transpUf", "transpVeicPlaca", "transpVeicUf", "transpVeicRntc", "transpQuantidade", "transpEspecie", "transpMarca", "transpNumeracaoVolumes", "transpPesoLiquido", "transpPesoBruto")
    TRANSPID_FIELD_NUMBER: _ClassVar[int]
    TRANSPCPFCNPJ_FIELD_NUMBER: _ClassVar[int]
    TRANSPNOME_FIELD_NUMBER: _ClassVar[int]
    TRANSPIE_FIELD_NUMBER: _ClassVar[int]
    TRANSPENDERECO_FIELD_NUMBER: _ClassVar[int]
    TRANSPMUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    TRANSPUF_FIELD_NUMBER: _ClassVar[int]
    TRANSPVEICPLACA_FIELD_NUMBER: _ClassVar[int]
    TRANSPVEICUF_FIELD_NUMBER: _ClassVar[int]
    TRANSPVEICRNTC_FIELD_NUMBER: _ClassVar[int]
    TRANSPQUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    TRANSPESPECIE_FIELD_NUMBER: _ClassVar[int]
    TRANSPMARCA_FIELD_NUMBER: _ClassVar[int]
    TRANSPNUMERACAOVOLUMES_FIELD_NUMBER: _ClassVar[int]
    TRANSPPESOLIQUIDO_FIELD_NUMBER: _ClassVar[int]
    TRANSPPESOBRUTO_FIELD_NUMBER: _ClassVar[int]
    transpId: str
    transpCpfCnpj: str
    transpNome: str
    transpIe: str
    transpEndereco: str
    transpMunicipio: str
    transpUf: str
    transpVeicPlaca: str
    transpVeicUf: str
    transpVeicRntc: str
    transpQuantidade: int
    transpEspecie: str
    transpMarca: str
    transpNumeracaoVolumes: str
    transpPesoLiquido: float
    transpPesoBruto: float
    def __init__(self, transpId: _Optional[str] = ..., transpCpfCnpj: _Optional[str] = ..., transpNome: _Optional[str] = ..., transpIe: _Optional[str] = ..., transpEndereco: _Optional[str] = ..., transpMunicipio: _Optional[str] = ..., transpUf: _Optional[str] = ..., transpVeicPlaca: _Optional[str] = ..., transpVeicUf: _Optional[str] = ..., transpVeicRntc: _Optional[str] = ..., transpQuantidade: _Optional[int] = ..., transpEspecie: _Optional[str] = ..., transpMarca: _Optional[str] = ..., transpNumeracaoVolumes: _Optional[str] = ..., transpPesoLiquido: _Optional[float] = ..., transpPesoBruto: _Optional[float] = ...) -> None: ...

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

class ItemModel(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "produto_id", "produto_nome", "produto_nome_nfe", "entrada_vinculado_por", "entrada_alteracao_preco", "tributacao_id", "categoria_id", "obs", "codigo", "codigo_ean", "quantidade", "fatorConversaoUnidadeTrib", "quantidadeTrib", "conversaoFator", "valor_unitario", "valorUnitarioTrib", "total", "subtotal", "un", "unTrib", "desconto_valor", "desconto_percentual", "desconto_rateado", "frete_manual", "valor_frete", "peso_bruto", "peso_liquido", "seguro_manual", "valor_seguro", "outras_despesas_manual", "valor_outras_despesas", "posto", "cfop", "ncm", "codigo_cest", "impostos", "natureza_operacao", "entrada_natureza_definida_por", "margemComissao", "vendaMargemCusto", "vendaPrecoAvistaAnterior", "vendaPrecoAprazoAnterior", "vendaPrecoAtacadoAnterior", "custo", "custoUnitario", "custoIcmsAliquota", "custoIcms", "custoIpiAliquota", "custoIpi", "custoFrete", "custoComissao", "custoOutrasDespesas", "diferencaAliquotaValor", "margemLucro", "vendaMargemAprazo", "vendaMargemAtacado", "vendaPrecoAvista", "vendaPrecoAprazo", "vendaPrecoAtacado", "batch", "margem_outras_despesas", "custo_despesas_operacionais", "variation_product_id", "skip_stock_decrease", "referencia_id", "referencia_n_item", "conversao_un", "entrada_cadastra_produto", "pedido_compra", "pedido_compra_item", "categoria_nome", "codigo_ean_trib", "un_trib_nfe", "quantidade_trib_nfe")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_NFE_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_VINCULADO_POR_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_ALTERACAO_PRECO_FIELD_NUMBER: _ClassVar[int]
    TRIBUTACAO_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_ID_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    CODIGO_EAN_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    FATORCONVERSAOUNIDADETRIB_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADETRIB_FIELD_NUMBER: _ClassVar[int]
    CONVERSAOFATOR_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    VALORUNITARIOTRIB_FIELD_NUMBER: _ClassVar[int]
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    SUBTOTAL_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    UNTRIB_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_VALOR_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_RATEADO_FIELD_NUMBER: _ClassVar[int]
    FRETE_MANUAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_FRETE_FIELD_NUMBER: _ClassVar[int]
    PESO_BRUTO_FIELD_NUMBER: _ClassVar[int]
    PESO_LIQUIDO_FIELD_NUMBER: _ClassVar[int]
    SEGURO_MANUAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_SEGURO_FIELD_NUMBER: _ClassVar[int]
    OUTRAS_DESPESAS_MANUAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_OUTRAS_DESPESAS_FIELD_NUMBER: _ClassVar[int]
    POSTO_FIELD_NUMBER: _ClassVar[int]
    CFOP_FIELD_NUMBER: _ClassVar[int]
    NCM_FIELD_NUMBER: _ClassVar[int]
    CODIGO_CEST_FIELD_NUMBER: _ClassVar[int]
    IMPOSTOS_FIELD_NUMBER: _ClassVar[int]
    NATUREZA_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_NATUREZA_DEFINIDA_POR_FIELD_NUMBER: _ClassVar[int]
    MARGEMCOMISSAO_FIELD_NUMBER: _ClassVar[int]
    VENDAMARGEMCUSTO_FIELD_NUMBER: _ClassVar[int]
    VENDAPRECOAVISTAANTERIOR_FIELD_NUMBER: _ClassVar[int]
    VENDAPRECOAPRAZOANTERIOR_FIELD_NUMBER: _ClassVar[int]
    VENDAPRECOATACADOANTERIOR_FIELD_NUMBER: _ClassVar[int]
    CUSTO_FIELD_NUMBER: _ClassVar[int]
    CUSTOUNITARIO_FIELD_NUMBER: _ClassVar[int]
    CUSTOICMSALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    CUSTOICMS_FIELD_NUMBER: _ClassVar[int]
    CUSTOIPIALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    CUSTOIPI_FIELD_NUMBER: _ClassVar[int]
    CUSTOFRETE_FIELD_NUMBER: _ClassVar[int]
    CUSTOCOMISSAO_FIELD_NUMBER: _ClassVar[int]
    CUSTOOUTRASDESPESAS_FIELD_NUMBER: _ClassVar[int]
    DIFERENCAALIQUOTAVALOR_FIELD_NUMBER: _ClassVar[int]
    MARGEMLUCRO_FIELD_NUMBER: _ClassVar[int]
    VENDAMARGEMAPRAZO_FIELD_NUMBER: _ClassVar[int]
    VENDAMARGEMATACADO_FIELD_NUMBER: _ClassVar[int]
    VENDAPRECOAVISTA_FIELD_NUMBER: _ClassVar[int]
    VENDAPRECOAPRAZO_FIELD_NUMBER: _ClassVar[int]
    VENDAPRECOATACADO_FIELD_NUMBER: _ClassVar[int]
    BATCH_FIELD_NUMBER: _ClassVar[int]
    MARGEM_OUTRAS_DESPESAS_FIELD_NUMBER: _ClassVar[int]
    CUSTO_DESPESAS_OPERACIONAIS_FIELD_NUMBER: _ClassVar[int]
    VARIATION_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_STOCK_DECREASE_FIELD_NUMBER: _ClassVar[int]
    REFERENCIA_ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCIA_N_ITEM_FIELD_NUMBER: _ClassVar[int]
    CONVERSAO_UN_FIELD_NUMBER: _ClassVar[int]
    ENTRADA_CADASTRA_PRODUTO_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_COMPRA_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_COMPRA_ITEM_FIELD_NUMBER: _ClassVar[int]
    CATEGORIA_NOME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_EAN_TRIB_FIELD_NUMBER: _ClassVar[int]
    UN_TRIB_NFE_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_TRIB_NFE_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    produto_id: str
    produto_nome: str
    produto_nome_nfe: str
    entrada_vinculado_por: str
    entrada_alteracao_preco: bool
    tributacao_id: str
    categoria_id: str
    obs: str
    codigo: str
    codigo_ean: str
    quantidade: float
    fatorConversaoUnidadeTrib: float
    quantidadeTrib: float
    conversaoFator: float
    valor_unitario: float
    valorUnitarioTrib: float
    total: float
    subtotal: float
    un: str
    unTrib: str
    desconto_valor: float
    desconto_percentual: float
    desconto_rateado: float
    frete_manual: bool
    valor_frete: float
    peso_bruto: float
    peso_liquido: float
    seguro_manual: bool
    valor_seguro: float
    outras_despesas_manual: bool
    valor_outras_despesas: float
    posto: PostoDados
    cfop: str
    ncm: str
    codigo_cest: str
    impostos: Impostos
    natureza_operacao: str
    entrada_natureza_definida_por: str
    margemComissao: float
    vendaMargemCusto: float
    vendaPrecoAvistaAnterior: float
    vendaPrecoAprazoAnterior: float
    vendaPrecoAtacadoAnterior: float
    custo: float
    custoUnitario: float
    custoIcmsAliquota: float
    custoIcms: float
    custoIpiAliquota: float
    custoIpi: float
    custoFrete: float
    custoComissao: float
    custoOutrasDespesas: float
    diferencaAliquotaValor: float
    margemLucro: float
    vendaMargemAprazo: float
    vendaMargemAtacado: float
    vendaPrecoAvista: float
    vendaPrecoAprazo: float
    vendaPrecoAtacado: float
    batch: BatchInfo
    margem_outras_despesas: float
    custo_despesas_operacionais: float
    variation_product_id: str
    skip_stock_decrease: bool
    referencia_id: str
    referencia_n_item: int
    conversao_un: str
    entrada_cadastra_produto: bool
    pedido_compra: str
    pedido_compra_item: int
    categoria_nome: str
    codigo_ean_trib: str
    un_trib_nfe: str
    quantidade_trib_nfe: float
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., produto_id: _Optional[str] = ..., produto_nome: _Optional[str] = ..., produto_nome_nfe: _Optional[str] = ..., entrada_vinculado_por: _Optional[str] = ..., entrada_alteracao_preco: _Optional[bool] = ..., tributacao_id: _Optional[str] = ..., categoria_id: _Optional[str] = ..., obs: _Optional[str] = ..., codigo: _Optional[str] = ..., codigo_ean: _Optional[str] = ..., quantidade: _Optional[float] = ..., fatorConversaoUnidadeTrib: _Optional[float] = ..., quantidadeTrib: _Optional[float] = ..., conversaoFator: _Optional[float] = ..., valor_unitario: _Optional[float] = ..., valorUnitarioTrib: _Optional[float] = ..., total: _Optional[float] = ..., subtotal: _Optional[float] = ..., un: _Optional[str] = ..., unTrib: _Optional[str] = ..., desconto_valor: _Optional[float] = ..., desconto_percentual: _Optional[float] = ..., desconto_rateado: _Optional[float] = ..., frete_manual: _Optional[bool] = ..., valor_frete: _Optional[float] = ..., peso_bruto: _Optional[float] = ..., peso_liquido: _Optional[float] = ..., seguro_manual: _Optional[bool] = ..., valor_seguro: _Optional[float] = ..., outras_despesas_manual: _Optional[bool] = ..., valor_outras_despesas: _Optional[float] = ..., posto: _Optional[_Union[PostoDados, _Mapping]] = ..., cfop: _Optional[str] = ..., ncm: _Optional[str] = ..., codigo_cest: _Optional[str] = ..., impostos: _Optional[_Union[Impostos, _Mapping]] = ..., natureza_operacao: _Optional[str] = ..., entrada_natureza_definida_por: _Optional[str] = ..., margemComissao: _Optional[float] = ..., vendaMargemCusto: _Optional[float] = ..., vendaPrecoAvistaAnterior: _Optional[float] = ..., vendaPrecoAprazoAnterior: _Optional[float] = ..., vendaPrecoAtacadoAnterior: _Optional[float] = ..., custo: _Optional[float] = ..., custoUnitario: _Optional[float] = ..., custoIcmsAliquota: _Optional[float] = ..., custoIcms: _Optional[float] = ..., custoIpiAliquota: _Optional[float] = ..., custoIpi: _Optional[float] = ..., custoFrete: _Optional[float] = ..., custoComissao: _Optional[float] = ..., custoOutrasDespesas: _Optional[float] = ..., diferencaAliquotaValor: _Optional[float] = ..., margemLucro: _Optional[float] = ..., vendaMargemAprazo: _Optional[float] = ..., vendaMargemAtacado: _Optional[float] = ..., vendaPrecoAvista: _Optional[float] = ..., vendaPrecoAprazo: _Optional[float] = ..., vendaPrecoAtacado: _Optional[float] = ..., batch: _Optional[_Union[BatchInfo, _Mapping]] = ..., margem_outras_despesas: _Optional[float] = ..., custo_despesas_operacionais: _Optional[float] = ..., variation_product_id: _Optional[str] = ..., skip_stock_decrease: _Optional[bool] = ..., referencia_id: _Optional[str] = ..., referencia_n_item: _Optional[int] = ..., conversao_un: _Optional[str] = ..., entrada_cadastra_produto: _Optional[bool] = ..., pedido_compra: _Optional[str] = ..., pedido_compra_item: _Optional[int] = ..., categoria_nome: _Optional[str] = ..., codigo_ean_trib: _Optional[str] = ..., un_trib_nfe: _Optional[str] = ..., quantidade_trib_nfe: _Optional[float] = ...) -> None: ...

class PostoDados(_message.Message):
    __slots__ = ("codigoAnp", "codigoAnpDescricao", "bico", "bomba", "tanque", "percentualGlp", "percentualGasNaturalNacional", "percentualGasNaturalImportado", "valorPartida", "encerranteInicial", "encerranteFinal", "percentualMistBio")
    CODIGOANP_FIELD_NUMBER: _ClassVar[int]
    CODIGOANPDESCRICAO_FIELD_NUMBER: _ClassVar[int]
    BICO_FIELD_NUMBER: _ClassVar[int]
    BOMBA_FIELD_NUMBER: _ClassVar[int]
    TANQUE_FIELD_NUMBER: _ClassVar[int]
    PERCENTUALGLP_FIELD_NUMBER: _ClassVar[int]
    PERCENTUALGASNATURALNACIONAL_FIELD_NUMBER: _ClassVar[int]
    PERCENTUALGASNATURALIMPORTADO_FIELD_NUMBER: _ClassVar[int]
    VALORPARTIDA_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTEINICIAL_FIELD_NUMBER: _ClassVar[int]
    ENCERRANTEFINAL_FIELD_NUMBER: _ClassVar[int]
    PERCENTUALMISTBIO_FIELD_NUMBER: _ClassVar[int]
    codigoAnp: str
    codigoAnpDescricao: str
    bico: str
    bomba: str
    tanque: str
    percentualGlp: float
    percentualGasNaturalNacional: float
    percentualGasNaturalImportado: float
    valorPartida: float
    encerranteInicial: float
    encerranteFinal: float
    percentualMistBio: float
    def __init__(self, codigoAnp: _Optional[str] = ..., codigoAnpDescricao: _Optional[str] = ..., bico: _Optional[str] = ..., bomba: _Optional[str] = ..., tanque: _Optional[str] = ..., percentualGlp: _Optional[float] = ..., percentualGasNaturalNacional: _Optional[float] = ..., percentualGasNaturalImportado: _Optional[float] = ..., valorPartida: _Optional[float] = ..., encerranteInicial: _Optional[float] = ..., encerranteFinal: _Optional[float] = ..., percentualMistBio: _Optional[float] = ...) -> None: ...

class PagamentoModel(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "formaPagamentoCodigo", "formaPagamentoNome", "formaPagamentoId", "numeroParcelas", "valor", "valorTroco", "cartaoCodigoAutorizacao", "cartaoBandeira", "cartaoCnpjAdministradora", "comprovanteTef")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    FORMAPAGAMENTOCODIGO_FIELD_NUMBER: _ClassVar[int]
    FORMAPAGAMENTONOME_FIELD_NUMBER: _ClassVar[int]
    FORMAPAGAMENTOID_FIELD_NUMBER: _ClassVar[int]
    NUMEROPARCELAS_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    VALORTROCO_FIELD_NUMBER: _ClassVar[int]
    CARTAOCODIGOAUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    CARTAOBANDEIRA_FIELD_NUMBER: _ClassVar[int]
    CARTAOCNPJADMINISTRADORA_FIELD_NUMBER: _ClassVar[int]
    COMPROVANTETEF_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    formaPagamentoCodigo: str
    formaPagamentoNome: str
    formaPagamentoId: str
    numeroParcelas: str
    valor: float
    valorTroco: float
    cartaoCodigoAutorizacao: str
    cartaoBandeira: str
    cartaoCnpjAdministradora: str
    comprovanteTef: str
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., formaPagamentoCodigo: _Optional[str] = ..., formaPagamentoNome: _Optional[str] = ..., formaPagamentoId: _Optional[str] = ..., numeroParcelas: _Optional[str] = ..., valor: _Optional[float] = ..., valorTroco: _Optional[float] = ..., cartaoCodigoAutorizacao: _Optional[str] = ..., cartaoBandeira: _Optional[str] = ..., cartaoCnpjAdministradora: _Optional[str] = ..., comprovanteTef: _Optional[str] = ...) -> None: ...

class DuplicataModel(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "numero", "valor", "vencimento", "contaPagarId")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    CONTAPAGARID_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    numero: str
    valor: float
    vencimento: _timestamp_pb2.Timestamp
    contaPagarId: str
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., numero: _Optional[str] = ..., valor: _Optional[float] = ..., vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., contaPagarId: _Optional[str] = ...) -> None: ...

class Evento(_message.Message):
    __slots__ = ("id", "created_at", "user_id", "user_name", "codigo", "descricao", "protocolo", "data_hora_evento", "c_stat", "mensagem", "xml_envio", "xml_retorno")
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_NAME_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    DESCRICAO_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_EVENTO_FIELD_NUMBER: _ClassVar[int]
    C_STAT_FIELD_NUMBER: _ClassVar[int]
    MENSAGEM_FIELD_NUMBER: _ClassVar[int]
    XML_ENVIO_FIELD_NUMBER: _ClassVar[int]
    XML_RETORNO_FIELD_NUMBER: _ClassVar[int]
    id: str
    created_at: _timestamp_pb2.Timestamp
    user_id: str
    user_name: str
    codigo: str
    descricao: str
    protocolo: str
    data_hora_evento: _timestamp_pb2.Timestamp
    c_stat: str
    mensagem: str
    xml_envio: str
    xml_retorno: str
    def __init__(self, id: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., user_id: _Optional[str] = ..., user_name: _Optional[str] = ..., codigo: _Optional[str] = ..., descricao: _Optional[str] = ..., protocolo: _Optional[str] = ..., data_hora_evento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., c_stat: _Optional[str] = ..., mensagem: _Optional[str] = ..., xml_envio: _Optional[str] = ..., xml_retorno: _Optional[str] = ...) -> None: ...

class VolumesModel(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "quantidade", "especie", "marca", "numeracaoVolumes", "pesoLiquido", "pesoBruto", "geradoPeloPesoDaNota")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    ESPECIE_FIELD_NUMBER: _ClassVar[int]
    MARCA_FIELD_NUMBER: _ClassVar[int]
    NUMERACAOVOLUMES_FIELD_NUMBER: _ClassVar[int]
    PESOLIQUIDO_FIELD_NUMBER: _ClassVar[int]
    PESOBRUTO_FIELD_NUMBER: _ClassVar[int]
    GERADOPELOPESODANOTA_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    quantidade: int
    especie: str
    marca: str
    numeracaoVolumes: str
    pesoLiquido: float
    pesoBruto: float
    geradoPeloPesoDaNota: bool
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., quantidade: _Optional[int] = ..., especie: _Optional[str] = ..., marca: _Optional[str] = ..., numeracaoVolumes: _Optional[str] = ..., pesoLiquido: _Optional[float] = ..., pesoBruto: _Optional[float] = ..., geradoPeloPesoDaNota: _Optional[bool] = ...) -> None: ...

class ReferenciaModel(_message.Message):
    __slots__ = ("createdAt", "updatedAt", "userId", "userName", "id", "chave")
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    createdAt: _timestamp_pb2.Timestamp
    updatedAt: _timestamp_pb2.Timestamp
    userId: str
    userName: str
    id: str
    chave: str
    def __init__(self, createdAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updatedAt: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., userId: _Optional[str] = ..., userName: _Optional[str] = ..., id: _Optional[str] = ..., chave: _Optional[str] = ...) -> None: ...

class Impostos(_message.Message):
    __slots__ = ("icms", "ipi", "pis", "cofins", "ibsCbs", "aliquotasNacionais")
    ICMS_FIELD_NUMBER: _ClassVar[int]
    IPI_FIELD_NUMBER: _ClassVar[int]
    PIS_FIELD_NUMBER: _ClassVar[int]
    COFINS_FIELD_NUMBER: _ClassVar[int]
    IS_FIELD_NUMBER: _ClassVar[int]
    IBSCBS_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTASNACIONAIS_FIELD_NUMBER: _ClassVar[int]
    icms: ImpostoIcms
    ipi: ImpostoIpi
    pis: ImpostoPis
    cofins: ImpostoCofins
    ibsCbs: _impostos_pb2.ImpostoIbsCbs
    aliquotasNacionais: AliquotasNacionais
    def __init__(self, icms: _Optional[_Union[ImpostoIcms, _Mapping]] = ..., ipi: _Optional[_Union[ImpostoIpi, _Mapping]] = ..., pis: _Optional[_Union[ImpostoPis, _Mapping]] = ..., cofins: _Optional[_Union[ImpostoCofins, _Mapping]] = ..., ibsCbs: _Optional[_Union[_impostos_pb2.ImpostoIbsCbs, _Mapping]] = ..., aliquotasNacionais: _Optional[_Union[AliquotasNacionais, _Mapping]] = ..., **kwargs) -> None: ...

class ImpostoIcms(_message.Message):
    __slots__ = ("cst", "aliquota", "origem", "calculo_manual_bc", "base_valor", "desoneracao", "valor", "aliquota_monofasica", "valor_monofasico", "mva", "mod_bc", "credito_percentual", "creditoValor", "reducaoBase", "reducaoValor", "stRetido", "stAliquota", "stBaseValor", "stValor", "stReducaoBase", "stModBc", "ufdestBc", "ufdestAliquota", "ufdestValor", "ufdestRemetenteValor", "ufdestFcpAliquota", "ufdestFcpValor", "ufdestInterestadualAliquota", "ufdestInterestadualPartilha", "valorIcmsIntereFcp", "valorIcmsIntereDestino", "valorIcmsIntereOrigem")
    CST_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    ORIGEM_FIELD_NUMBER: _ClassVar[int]
    CALCULO_MANUAL_BC_FIELD_NUMBER: _ClassVar[int]
    BASE_VALOR_FIELD_NUMBER: _ClassVar[int]
    DESONERACAO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_MONOFASICA_FIELD_NUMBER: _ClassVar[int]
    VALOR_MONOFASICO_FIELD_NUMBER: _ClassVar[int]
    MVA_FIELD_NUMBER: _ClassVar[int]
    MOD_BC_FIELD_NUMBER: _ClassVar[int]
    CREDITO_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    CREDITOVALOR_FIELD_NUMBER: _ClassVar[int]
    REDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
    REDUCAOVALOR_FIELD_NUMBER: _ClassVar[int]
    STRETIDO_FIELD_NUMBER: _ClassVar[int]
    STALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    STBASEVALOR_FIELD_NUMBER: _ClassVar[int]
    STVALOR_FIELD_NUMBER: _ClassVar[int]
    STREDUCAOBASE_FIELD_NUMBER: _ClassVar[int]
    STMODBC_FIELD_NUMBER: _ClassVar[int]
    UFDESTBC_FIELD_NUMBER: _ClassVar[int]
    UFDESTALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    UFDESTVALOR_FIELD_NUMBER: _ClassVar[int]
    UFDESTREMETENTEVALOR_FIELD_NUMBER: _ClassVar[int]
    UFDESTFCPALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    UFDESTFCPVALOR_FIELD_NUMBER: _ClassVar[int]
    UFDESTINTERESTADUALALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    UFDESTINTERESTADUALPARTILHA_FIELD_NUMBER: _ClassVar[int]
    VALORICMSINTEREFCP_FIELD_NUMBER: _ClassVar[int]
    VALORICMSINTEREDESTINO_FIELD_NUMBER: _ClassVar[int]
    VALORICMSINTEREORIGEM_FIELD_NUMBER: _ClassVar[int]
    cst: str
    aliquota: float
    origem: str
    calculo_manual_bc: bool
    base_valor: float
    desoneracao: float
    valor: float
    aliquota_monofasica: float
    valor_monofasico: float
    mva: float
    mod_bc: str
    credito_percentual: float
    creditoValor: float
    reducaoBase: float
    reducaoValor: float
    stRetido: bool
    stAliquota: float
    stBaseValor: float
    stValor: float
    stReducaoBase: float
    stModBc: str
    ufdestBc: float
    ufdestAliquota: float
    ufdestValor: float
    ufdestRemetenteValor: float
    ufdestFcpAliquota: float
    ufdestFcpValor: float
    ufdestInterestadualAliquota: float
    ufdestInterestadualPartilha: float
    valorIcmsIntereFcp: float
    valorIcmsIntereDestino: float
    valorIcmsIntereOrigem: float
    def __init__(self, cst: _Optional[str] = ..., aliquota: _Optional[float] = ..., origem: _Optional[str] = ..., calculo_manual_bc: _Optional[bool] = ..., base_valor: _Optional[float] = ..., desoneracao: _Optional[float] = ..., valor: _Optional[float] = ..., aliquota_monofasica: _Optional[float] = ..., valor_monofasico: _Optional[float] = ..., mva: _Optional[float] = ..., mod_bc: _Optional[str] = ..., credito_percentual: _Optional[float] = ..., creditoValor: _Optional[float] = ..., reducaoBase: _Optional[float] = ..., reducaoValor: _Optional[float] = ..., stRetido: _Optional[bool] = ..., stAliquota: _Optional[float] = ..., stBaseValor: _Optional[float] = ..., stValor: _Optional[float] = ..., stReducaoBase: _Optional[float] = ..., stModBc: _Optional[str] = ..., ufdestBc: _Optional[float] = ..., ufdestAliquota: _Optional[float] = ..., ufdestValor: _Optional[float] = ..., ufdestRemetenteValor: _Optional[float] = ..., ufdestFcpAliquota: _Optional[float] = ..., ufdestFcpValor: _Optional[float] = ..., ufdestInterestadualAliquota: _Optional[float] = ..., ufdestInterestadualPartilha: _Optional[float] = ..., valorIcmsIntereFcp: _Optional[float] = ..., valorIcmsIntereDestino: _Optional[float] = ..., valorIcmsIntereOrigem: _Optional[float] = ...) -> None: ...

class ImpostoIpi(_message.Message):
    __slots__ = ("cst", "aliquota", "base_valor", "valor", "codigo_enquadramento")
    CST_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    BASE_VALOR_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    CODIGO_ENQUADRAMENTO_FIELD_NUMBER: _ClassVar[int]
    cst: str
    aliquota: float
    base_valor: float
    valor: float
    codigo_enquadramento: str
    def __init__(self, cst: _Optional[str] = ..., aliquota: _Optional[float] = ..., base_valor: _Optional[float] = ..., valor: _Optional[float] = ..., codigo_enquadramento: _Optional[str] = ...) -> None: ...

class ImpostoPis(_message.Message):
    __slots__ = ("cst", "aliquota", "calculo_manual_bc", "base_valor", "valor", "st_aliquota", "st_base_valor", "st_valor")
    CST_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    CALCULO_MANUAL_BC_FIELD_NUMBER: _ClassVar[int]
    BASE_VALOR_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    ST_ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    ST_BASE_VALOR_FIELD_NUMBER: _ClassVar[int]
    ST_VALOR_FIELD_NUMBER: _ClassVar[int]
    cst: str
    aliquota: float
    calculo_manual_bc: bool
    base_valor: float
    valor: float
    st_aliquota: float
    st_base_valor: float
    st_valor: float
    def __init__(self, cst: _Optional[str] = ..., aliquota: _Optional[float] = ..., calculo_manual_bc: _Optional[bool] = ..., base_valor: _Optional[float] = ..., valor: _Optional[float] = ..., st_aliquota: _Optional[float] = ..., st_base_valor: _Optional[float] = ..., st_valor: _Optional[float] = ...) -> None: ...

class ImpostoCofins(_message.Message):
    __slots__ = ("cst", "aliquota", "calculo_manual_bc", "base_valor", "valor", "st_aliquota", "st_base_valor", "st_valor")
    CST_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    CALCULO_MANUAL_BC_FIELD_NUMBER: _ClassVar[int]
    BASE_VALOR_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    ST_ALIQUOTA_FIELD_NUMBER: _ClassVar[int]
    ST_BASE_VALOR_FIELD_NUMBER: _ClassVar[int]
    ST_VALOR_FIELD_NUMBER: _ClassVar[int]
    cst: str
    aliquota: float
    calculo_manual_bc: bool
    base_valor: float
    valor: float
    st_aliquota: float
    st_base_valor: float
    st_valor: float
    def __init__(self, cst: _Optional[str] = ..., aliquota: _Optional[float] = ..., calculo_manual_bc: _Optional[bool] = ..., base_valor: _Optional[float] = ..., valor: _Optional[float] = ..., st_aliquota: _Optional[float] = ..., st_base_valor: _Optional[float] = ..., st_valor: _Optional[float] = ...) -> None: ...

class AliquotasNacionais(_message.Message):
    __slots__ = ("aliquota_federal", "aliquota_estadual", "aliquota_municipal", "tributo_federal", "tributo_estadual", "tributo_municipal")
    ALIQUOTA_FEDERAL_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_ESTADUAL_FIELD_NUMBER: _ClassVar[int]
    ALIQUOTA_MUNICIPAL_FIELD_NUMBER: _ClassVar[int]
    TRIBUTO_FEDERAL_FIELD_NUMBER: _ClassVar[int]
    TRIBUTO_ESTADUAL_FIELD_NUMBER: _ClassVar[int]
    TRIBUTO_MUNICIPAL_FIELD_NUMBER: _ClassVar[int]
    aliquota_federal: float
    aliquota_estadual: float
    aliquota_municipal: float
    tributo_federal: float
    tributo_estadual: float
    tributo_municipal: float
    def __init__(self, aliquota_federal: _Optional[float] = ..., aliquota_estadual: _Optional[float] = ..., aliquota_municipal: _Optional[float] = ..., tributo_federal: _Optional[float] = ..., tributo_estadual: _Optional[float] = ..., tributo_municipal: _Optional[float] = ...) -> None: ...

class ItemDevolucao(_message.Message):
    __slots__ = ("id", "codigo", "produtoNomeNfe", "valorUnitario", "quantidade", "quantidadeDevolver", "un")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    PRODUTONOMENFE_FIELD_NUMBER: _ClassVar[int]
    VALORUNITARIO_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADEDEVOLVER_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    id: str
    codigo: str
    produtoNomeNfe: str
    valorUnitario: float
    quantidade: float
    quantidadeDevolver: float
    un: str
    def __init__(self, id: _Optional[str] = ..., codigo: _Optional[str] = ..., produtoNomeNfe: _Optional[str] = ..., valorUnitario: _Optional[float] = ..., quantidade: _Optional[float] = ..., quantidadeDevolver: _Optional[float] = ..., un: _Optional[str] = ...) -> None: ...

class EmitirNfeRequest(_message.Message):
    __slots__ = ("id", "nota", "idempotency_key")
    ID_FIELD_NUMBER: _ClassVar[int]
    NOTA_FIELD_NUMBER: _ClassVar[int]
    IDEMPOTENCY_KEY_FIELD_NUMBER: _ClassVar[int]
    id: str
    nota: NfeEmissao
    idempotency_key: str
    def __init__(self, id: _Optional[str] = ..., nota: _Optional[_Union[NfeEmissao, _Mapping]] = ..., idempotency_key: _Optional[str] = ...) -> None: ...

class NfeEmissao(_message.Message):
    __slots__ = ("tipo_operacao", "finalidade_emissao", "natureza_operacao", "tipo_ambiente", "serie", "data_hora_saida", "obs", "pessoa", "desconto_valor", "desconto_percentual", "valor_frete", "valor_seguro", "valor_outras_despesas", "transp_mod_frete", "transp_id", "transp_cpf_cnpj", "transp_nome", "transp_ie", "transp_endereco", "transp_municipio", "transp_uf", "transp_veic_placa", "transp_veic_uf", "transp_veic_rntc", "volumes", "produtos", "pagamentos", "duplicatas", "referencias", "tipo_nota_debito", "tipo_nota_credito", "pag_antecipado_refs")
    TIPO_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    FINALIDADE_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    NATUREZA_OPERACAO_FIELD_NUMBER: _ClassVar[int]
    TIPO_AMBIENTE_FIELD_NUMBER: _ClassVar[int]
    SERIE_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_SAIDA_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    PESSOA_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_VALOR_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_PERCENTUAL_FIELD_NUMBER: _ClassVar[int]
    VALOR_FRETE_FIELD_NUMBER: _ClassVar[int]
    VALOR_SEGURO_FIELD_NUMBER: _ClassVar[int]
    VALOR_OUTRAS_DESPESAS_FIELD_NUMBER: _ClassVar[int]
    TRANSP_MOD_FRETE_FIELD_NUMBER: _ClassVar[int]
    TRANSP_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSP_CPF_CNPJ_FIELD_NUMBER: _ClassVar[int]
    TRANSP_NOME_FIELD_NUMBER: _ClassVar[int]
    TRANSP_IE_FIELD_NUMBER: _ClassVar[int]
    TRANSP_ENDERECO_FIELD_NUMBER: _ClassVar[int]
    TRANSP_MUNICIPIO_FIELD_NUMBER: _ClassVar[int]
    TRANSP_UF_FIELD_NUMBER: _ClassVar[int]
    TRANSP_VEIC_PLACA_FIELD_NUMBER: _ClassVar[int]
    TRANSP_VEIC_UF_FIELD_NUMBER: _ClassVar[int]
    TRANSP_VEIC_RNTC_FIELD_NUMBER: _ClassVar[int]
    VOLUMES_FIELD_NUMBER: _ClassVar[int]
    PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTOS_FIELD_NUMBER: _ClassVar[int]
    DUPLICATAS_FIELD_NUMBER: _ClassVar[int]
    REFERENCIAS_FIELD_NUMBER: _ClassVar[int]
    TIPO_NOTA_DEBITO_FIELD_NUMBER: _ClassVar[int]
    TIPO_NOTA_CREDITO_FIELD_NUMBER: _ClassVar[int]
    PAG_ANTECIPADO_REFS_FIELD_NUMBER: _ClassVar[int]
    tipo_operacao: str
    finalidade_emissao: str
    natureza_operacao: str
    tipo_ambiente: str
    serie: int
    data_hora_saida: _timestamp_pb2.Timestamp
    obs: str
    pessoa: Pessoa
    desconto_valor: float
    desconto_percentual: float
    valor_frete: float
    valor_seguro: float
    valor_outras_despesas: float
    transp_mod_frete: str
    transp_id: str
    transp_cpf_cnpj: str
    transp_nome: str
    transp_ie: str
    transp_endereco: str
    transp_municipio: str
    transp_uf: str
    transp_veic_placa: str
    transp_veic_uf: str
    transp_veic_rntc: str
    volumes: _containers.RepeatedCompositeFieldContainer[NfeEmissaoVolume]
    produtos: _containers.RepeatedCompositeFieldContainer[NfeEmissaoItem]
    pagamentos: _containers.RepeatedCompositeFieldContainer[NfeEmissaoPagamento]
    duplicatas: _containers.RepeatedCompositeFieldContainer[NfeEmissaoDuplicata]
    referencias: _containers.RepeatedCompositeFieldContainer[NfeEmissaoReferencia]
    tipo_nota_debito: str
    tipo_nota_credito: str
    pag_antecipado_refs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tipo_operacao: _Optional[str] = ..., finalidade_emissao: _Optional[str] = ..., natureza_operacao: _Optional[str] = ..., tipo_ambiente: _Optional[str] = ..., serie: _Optional[int] = ..., data_hora_saida: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., obs: _Optional[str] = ..., pessoa: _Optional[_Union[Pessoa, _Mapping]] = ..., desconto_valor: _Optional[float] = ..., desconto_percentual: _Optional[float] = ..., valor_frete: _Optional[float] = ..., valor_seguro: _Optional[float] = ..., valor_outras_despesas: _Optional[float] = ..., transp_mod_frete: _Optional[str] = ..., transp_id: _Optional[str] = ..., transp_cpf_cnpj: _Optional[str] = ..., transp_nome: _Optional[str] = ..., transp_ie: _Optional[str] = ..., transp_endereco: _Optional[str] = ..., transp_municipio: _Optional[str] = ..., transp_uf: _Optional[str] = ..., transp_veic_placa: _Optional[str] = ..., transp_veic_uf: _Optional[str] = ..., transp_veic_rntc: _Optional[str] = ..., volumes: _Optional[_Iterable[_Union[NfeEmissaoVolume, _Mapping]]] = ..., produtos: _Optional[_Iterable[_Union[NfeEmissaoItem, _Mapping]]] = ..., pagamentos: _Optional[_Iterable[_Union[NfeEmissaoPagamento, _Mapping]]] = ..., duplicatas: _Optional[_Iterable[_Union[NfeEmissaoDuplicata, _Mapping]]] = ..., referencias: _Optional[_Iterable[_Union[NfeEmissaoReferencia, _Mapping]]] = ..., tipo_nota_debito: _Optional[str] = ..., tipo_nota_credito: _Optional[str] = ..., pag_antecipado_refs: _Optional[_Iterable[str]] = ...) -> None: ...

class NfeEmissaoItem(_message.Message):
    __slots__ = ("produto_id", "codigo", "codigo_ean", "produto_nome", "produto_nome_nfe", "variation_product_id", "quantidade", "valor_unitario", "desconto_valor", "un", "ncm", "cfop", "obs", "posto", "skip_stock_decrease", "pedido_compra", "pedido_compra_item")
    PRODUTO_ID_FIELD_NUMBER: _ClassVar[int]
    CODIGO_FIELD_NUMBER: _ClassVar[int]
    CODIGO_EAN_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_NOME_NFE_FIELD_NUMBER: _ClassVar[int]
    VARIATION_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    VALOR_UNITARIO_FIELD_NUMBER: _ClassVar[int]
    DESCONTO_VALOR_FIELD_NUMBER: _ClassVar[int]
    UN_FIELD_NUMBER: _ClassVar[int]
    NCM_FIELD_NUMBER: _ClassVar[int]
    CFOP_FIELD_NUMBER: _ClassVar[int]
    OBS_FIELD_NUMBER: _ClassVar[int]
    POSTO_FIELD_NUMBER: _ClassVar[int]
    SKIP_STOCK_DECREASE_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_COMPRA_FIELD_NUMBER: _ClassVar[int]
    PEDIDO_COMPRA_ITEM_FIELD_NUMBER: _ClassVar[int]
    produto_id: str
    codigo: str
    codigo_ean: str
    produto_nome: str
    produto_nome_nfe: str
    variation_product_id: str
    quantidade: float
    valor_unitario: float
    desconto_valor: float
    un: str
    ncm: str
    cfop: str
    obs: str
    posto: PostoDados
    skip_stock_decrease: bool
    pedido_compra: str
    pedido_compra_item: int
    def __init__(self, produto_id: _Optional[str] = ..., codigo: _Optional[str] = ..., codigo_ean: _Optional[str] = ..., produto_nome: _Optional[str] = ..., produto_nome_nfe: _Optional[str] = ..., variation_product_id: _Optional[str] = ..., quantidade: _Optional[float] = ..., valor_unitario: _Optional[float] = ..., desconto_valor: _Optional[float] = ..., un: _Optional[str] = ..., ncm: _Optional[str] = ..., cfop: _Optional[str] = ..., obs: _Optional[str] = ..., posto: _Optional[_Union[PostoDados, _Mapping]] = ..., skip_stock_decrease: _Optional[bool] = ..., pedido_compra: _Optional[str] = ..., pedido_compra_item: _Optional[int] = ...) -> None: ...

class NfeEmissaoPagamento(_message.Message):
    __slots__ = ("formaPagamentoId", "formaPagamentoCodigo", "formaPagamentoNome", "numeroParcelas", "valor", "valorTroco", "cartaoCodigoAutorizacao", "cartaoBandeira", "cartaoCnpjAdministradora", "comprovanteTef")
    FORMAPAGAMENTOID_FIELD_NUMBER: _ClassVar[int]
    FORMAPAGAMENTOCODIGO_FIELD_NUMBER: _ClassVar[int]
    FORMAPAGAMENTONOME_FIELD_NUMBER: _ClassVar[int]
    NUMEROPARCELAS_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    VALORTROCO_FIELD_NUMBER: _ClassVar[int]
    CARTAOCODIGOAUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    CARTAOBANDEIRA_FIELD_NUMBER: _ClassVar[int]
    CARTAOCNPJADMINISTRADORA_FIELD_NUMBER: _ClassVar[int]
    COMPROVANTETEF_FIELD_NUMBER: _ClassVar[int]
    formaPagamentoId: str
    formaPagamentoCodigo: str
    formaPagamentoNome: str
    numeroParcelas: str
    valor: float
    valorTroco: float
    cartaoCodigoAutorizacao: str
    cartaoBandeira: str
    cartaoCnpjAdministradora: str
    comprovanteTef: str
    def __init__(self, formaPagamentoId: _Optional[str] = ..., formaPagamentoCodigo: _Optional[str] = ..., formaPagamentoNome: _Optional[str] = ..., numeroParcelas: _Optional[str] = ..., valor: _Optional[float] = ..., valorTroco: _Optional[float] = ..., cartaoCodigoAutorizacao: _Optional[str] = ..., cartaoBandeira: _Optional[str] = ..., cartaoCnpjAdministradora: _Optional[str] = ..., comprovanteTef: _Optional[str] = ...) -> None: ...

class NfeEmissaoDuplicata(_message.Message):
    __slots__ = ("numero", "valor", "vencimento")
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    VALOR_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTO_FIELD_NUMBER: _ClassVar[int]
    numero: str
    valor: float
    vencimento: _timestamp_pb2.Timestamp
    def __init__(self, numero: _Optional[str] = ..., valor: _Optional[float] = ..., vencimento: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class NfeEmissaoVolume(_message.Message):
    __slots__ = ("quantidade", "especie", "marca", "numeracaoVolumes", "pesoLiquido", "pesoBruto")
    QUANTIDADE_FIELD_NUMBER: _ClassVar[int]
    ESPECIE_FIELD_NUMBER: _ClassVar[int]
    MARCA_FIELD_NUMBER: _ClassVar[int]
    NUMERACAOVOLUMES_FIELD_NUMBER: _ClassVar[int]
    PESOLIQUIDO_FIELD_NUMBER: _ClassVar[int]
    PESOBRUTO_FIELD_NUMBER: _ClassVar[int]
    quantidade: int
    especie: str
    marca: str
    numeracaoVolumes: str
    pesoLiquido: float
    pesoBruto: float
    def __init__(self, quantidade: _Optional[int] = ..., especie: _Optional[str] = ..., marca: _Optional[str] = ..., numeracaoVolumes: _Optional[str] = ..., pesoLiquido: _Optional[float] = ..., pesoBruto: _Optional[float] = ...) -> None: ...

class NfeEmissaoReferencia(_message.Message):
    __slots__ = ("chave",)
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    chave: str
    def __init__(self, chave: _Optional[str] = ...) -> None: ...

class EmitirNfeResponse(_message.Message):
    __slots__ = ("id", "chave", "numero", "serie", "situacao", "forma_emissao", "protocolo", "motivo", "data_hora_emissao", "data_hora_autorizacao", "url_danfe", "url_xml")
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    SERIE_FIELD_NUMBER: _ClassVar[int]
    SITUACAO_FIELD_NUMBER: _ClassVar[int]
    FORMA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    PROTOCOLO_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_EMISSAO_FIELD_NUMBER: _ClassVar[int]
    DATA_HORA_AUTORIZACAO_FIELD_NUMBER: _ClassVar[int]
    URL_DANFE_FIELD_NUMBER: _ClassVar[int]
    URL_XML_FIELD_NUMBER: _ClassVar[int]
    id: str
    chave: str
    numero: int
    serie: int
    situacao: str
    forma_emissao: str
    protocolo: str
    motivo: str
    data_hora_emissao: _timestamp_pb2.Timestamp
    data_hora_autorizacao: _timestamp_pb2.Timestamp
    url_danfe: str
    url_xml: str
    def __init__(self, id: _Optional[str] = ..., chave: _Optional[str] = ..., numero: _Optional[int] = ..., serie: _Optional[int] = ..., situacao: _Optional[str] = ..., forma_emissao: _Optional[str] = ..., protocolo: _Optional[str] = ..., motivo: _Optional[str] = ..., data_hora_emissao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., data_hora_autorizacao: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., url_danfe: _Optional[str] = ..., url_xml: _Optional[str] = ...) -> None: ...

class ConsultaProtocoloByChaveRequest(_message.Message):
    __slots__ = ("id", "tipo", "numero", "chave")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    tipo: Tipo
    numero: int
    chave: str
    def __init__(self, id: _Optional[str] = ..., tipo: _Optional[_Union[Tipo, str]] = ..., numero: _Optional[int] = ..., chave: _Optional[str] = ...) -> None: ...

class ConsultaProtocoloByChaveResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class CancelarNfeRequest(_message.Message):
    __slots__ = ("id", "motivoCancelamento")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVOCANCELAMENTO_FIELD_NUMBER: _ClassVar[int]
    id: str
    motivoCancelamento: str
    def __init__(self, id: _Optional[str] = ..., motivoCancelamento: _Optional[str] = ...) -> None: ...

class CancelarNfeResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class GerarDevolucaoNfeRequest(_message.Message):
    __slots__ = ("ids", "itens_a_devolver", "force", "destinatario_id", "devolucao_id")
    IDS_FIELD_NUMBER: _ClassVar[int]
    ITENS_A_DEVOLVER_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATARIO_ID_FIELD_NUMBER: _ClassVar[int]
    DEVOLUCAO_ID_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    itens_a_devolver: _containers.RepeatedCompositeFieldContainer[ItemDevolucao]
    force: bool
    destinatario_id: str
    devolucao_id: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., itens_a_devolver: _Optional[_Iterable[_Union[ItemDevolucao, _Mapping]]] = ..., force: _Optional[bool] = ..., destinatario_id: _Optional[str] = ..., devolucao_id: _Optional[str] = ...) -> None: ...

class GerarDevolucaoNfeResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class CancelaOuGeraDevolucaoRequest(_message.Message):
    __slots__ = ("id", "motivo")
    ID_FIELD_NUMBER: _ClassVar[int]
    MOTIVO_FIELD_NUMBER: _ClassVar[int]
    id: str
    motivo: str
    def __init__(self, id: _Optional[str] = ..., motivo: _Optional[str] = ...) -> None: ...

class CancelaOuGeraDevolucaoResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class AddProdutoRequest(_message.Message):
    __slots__ = ("nfeId", "produto")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    produto: ItemModel
    def __init__(self, nfeId: _Optional[str] = ..., produto: _Optional[_Union[ItemModel, _Mapping]] = ...) -> None: ...

class AddProdutoResponse(_message.Message):
    __slots__ = ("nfe", "produto")
    NFE_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    produto: ItemModel
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ..., produto: _Optional[_Union[ItemModel, _Mapping]] = ...) -> None: ...

class UpdateProdutoRequest(_message.Message):
    __slots__ = ("nfeId", "id", "produto")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    id: str
    produto: ItemModel
    def __init__(self, nfeId: _Optional[str] = ..., id: _Optional[str] = ..., produto: _Optional[_Union[ItemModel, _Mapping]] = ...) -> None: ...

class UpdateProdutoResponse(_message.Message):
    __slots__ = ("produto", "nfe")
    PRODUTO_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    produto: ItemModel
    nfe: Nfe
    def __init__(self, produto: _Optional[_Union[ItemModel, _Mapping]] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class DeleteProdutoRequest(_message.Message):
    __slots__ = ("nfeId", "id")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    id: str
    def __init__(self, nfeId: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteProdutoResponse(_message.Message):
    __slots__ = ("result", "nfe")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    result: str
    nfe: Nfe
    def __init__(self, result: _Optional[str] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class AddPagamentoRequest(_message.Message):
    __slots__ = ("nfeId", "pagamentos")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTOS_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    pagamentos: _containers.RepeatedCompositeFieldContainer[PagamentoModel]
    def __init__(self, nfeId: _Optional[str] = ..., pagamentos: _Optional[_Iterable[_Union[PagamentoModel, _Mapping]]] = ...) -> None: ...

class AddPagamentoResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class UpdatePagamentoRequest(_message.Message):
    __slots__ = ("nfeId", "id", "pagamento")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    id: str
    pagamento: PagamentoModel
    def __init__(self, nfeId: _Optional[str] = ..., id: _Optional[str] = ..., pagamento: _Optional[_Union[PagamentoModel, _Mapping]] = ...) -> None: ...

class UpdatePagamentoResponse(_message.Message):
    __slots__ = ("pagamento", "nfe")
    PAGAMENTO_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    pagamento: PagamentoModel
    nfe: Nfe
    def __init__(self, pagamento: _Optional[_Union[PagamentoModel, _Mapping]] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class DeletePagamentoRequest(_message.Message):
    __slots__ = ("nfeId", "id")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    id: str
    def __init__(self, nfeId: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeletePagamentoResponse(_message.Message):
    __slots__ = ("result", "nfe")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    result: str
    nfe: Nfe
    def __init__(self, result: _Optional[str] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class AddReferenciaRequest(_message.Message):
    __slots__ = ("nfeId", "referencia")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    REFERENCIA_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    referencia: ReferenciaModel
    def __init__(self, nfeId: _Optional[str] = ..., referencia: _Optional[_Union[ReferenciaModel, _Mapping]] = ...) -> None: ...

class AddReferenciaResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class UpdateReferenciaRequest(_message.Message):
    __slots__ = ("nfeId", "id", "referencia")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REFERENCIA_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    id: str
    referencia: ReferenciaModel
    def __init__(self, nfeId: _Optional[str] = ..., id: _Optional[str] = ..., referencia: _Optional[_Union[ReferenciaModel, _Mapping]] = ...) -> None: ...

class UpdateReferenciaResponse(_message.Message):
    __slots__ = ("referencia", "nfe")
    REFERENCIA_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    referencia: ReferenciaModel
    nfe: Nfe
    def __init__(self, referencia: _Optional[_Union[ReferenciaModel, _Mapping]] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class DeleteReferenciaRequest(_message.Message):
    __slots__ = ("nfeId", "id")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    id: str
    def __init__(self, nfeId: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteReferenciaResponse(_message.Message):
    __slots__ = ("result", "nfe")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    result: str
    nfe: Nfe
    def __init__(self, result: _Optional[str] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class AddDuplicataRequest(_message.Message):
    __slots__ = ("nfeId", "duplicata")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    DUPLICATA_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    duplicata: DuplicataModel
    def __init__(self, nfeId: _Optional[str] = ..., duplicata: _Optional[_Union[DuplicataModel, _Mapping]] = ...) -> None: ...

class AddDuplicataResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class UpdateDuplicataRequest(_message.Message):
    __slots__ = ("nfeId", "id", "duplicata")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DUPLICATA_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    id: str
    duplicata: DuplicataModel
    def __init__(self, nfeId: _Optional[str] = ..., id: _Optional[str] = ..., duplicata: _Optional[_Union[DuplicataModel, _Mapping]] = ...) -> None: ...

class UpdateDuplicataResponse(_message.Message):
    __slots__ = ("duplicata", "nfe")
    DUPLICATA_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    duplicata: DuplicataModel
    nfe: Nfe
    def __init__(self, duplicata: _Optional[_Union[DuplicataModel, _Mapping]] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class DeleteDuplicataRequest(_message.Message):
    __slots__ = ("nfeId", "id")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    id: str
    def __init__(self, nfeId: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteDuplicataResponse(_message.Message):
    __slots__ = ("result", "nfe")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    result: str
    nfe: Nfe
    def __init__(self, result: _Optional[str] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class AddVolumeRequest(_message.Message):
    __slots__ = ("nfeId", "volume")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    volume: VolumesModel
    def __init__(self, nfeId: _Optional[str] = ..., volume: _Optional[_Union[VolumesModel, _Mapping]] = ...) -> None: ...

class AddVolumeResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class UpdateVolumeRequest(_message.Message):
    __slots__ = ("nfeId", "id", "volume")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    id: str
    volume: VolumesModel
    def __init__(self, nfeId: _Optional[str] = ..., id: _Optional[str] = ..., volume: _Optional[_Union[VolumesModel, _Mapping]] = ...) -> None: ...

class UpdateVolumeResponse(_message.Message):
    __slots__ = ("volume", "nfe")
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    volume: VolumesModel
    nfe: Nfe
    def __init__(self, volume: _Optional[_Union[VolumesModel, _Mapping]] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class DeleteVolumeRequest(_message.Message):
    __slots__ = ("nfeId", "id")
    NFEID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    nfeId: str
    id: str
    def __init__(self, nfeId: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteVolumeResponse(_message.Message):
    __slots__ = ("result", "nfe")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    result: str
    nfe: Nfe
    def __init__(self, result: _Optional[str] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class DuplicaRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DuplicaResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class DanfeRequest(_message.Message):
    __slots__ = ("ids", "danfe_tipo")
    IDS_FIELD_NUMBER: _ClassVar[int]
    DANFE_TIPO_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    danfe_tipo: DanfeTipo
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., danfe_tipo: _Optional[_Union[DanfeTipo, str]] = ...) -> None: ...

class DanfeResponse(_message.Message):
    __slots__ = ("danfe_tipo", "danfeResponseList")
    class DanfeResponseList(_message.Message):
        __slots__ = ("numero", "serie", "chave", "danfe_data", "danfe_template", "filename")
        NUMERO_FIELD_NUMBER: _ClassVar[int]
        SERIE_FIELD_NUMBER: _ClassVar[int]
        CHAVE_FIELD_NUMBER: _ClassVar[int]
        DANFE_DATA_FIELD_NUMBER: _ClassVar[int]
        DANFE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        numero: int
        serie: int
        chave: str
        danfe_data: str
        danfe_template: str
        filename: str
        def __init__(self, numero: _Optional[int] = ..., serie: _Optional[int] = ..., chave: _Optional[str] = ..., danfe_data: _Optional[str] = ..., danfe_template: _Optional[str] = ..., filename: _Optional[str] = ...) -> None: ...
    DANFE_TIPO_FIELD_NUMBER: _ClassVar[int]
    DANFERESPONSELIST_FIELD_NUMBER: _ClassVar[int]
    danfe_tipo: DanfeTipo
    danfeResponseList: _containers.RepeatedCompositeFieldContainer[DanfeResponse.DanfeResponseList]
    def __init__(self, danfe_tipo: _Optional[_Union[DanfeTipo, str]] = ..., danfeResponseList: _Optional[_Iterable[_Union[DanfeResponse.DanfeResponseList, _Mapping]]] = ...) -> None: ...

class NfeImportaXmlRequest(_message.Message):
    __slots__ = ("file", "extensao", "nome_arquivo", "importa_cliente", "importa_transportador", "importa_produtos", "gera_pedidos")
    FILE_FIELD_NUMBER: _ClassVar[int]
    EXTENSAO_FIELD_NUMBER: _ClassVar[int]
    NOME_ARQUIVO_FIELD_NUMBER: _ClassVar[int]
    IMPORTA_CLIENTE_FIELD_NUMBER: _ClassVar[int]
    IMPORTA_TRANSPORTADOR_FIELD_NUMBER: _ClassVar[int]
    IMPORTA_PRODUTOS_FIELD_NUMBER: _ClassVar[int]
    GERA_PEDIDOS_FIELD_NUMBER: _ClassVar[int]
    file: bytes
    extensao: str
    nome_arquivo: str
    importa_cliente: bool
    importa_transportador: bool
    importa_produtos: bool
    gera_pedidos: bool
    def __init__(self, file: _Optional[bytes] = ..., extensao: _Optional[str] = ..., nome_arquivo: _Optional[str] = ..., importa_cliente: _Optional[bool] = ..., importa_transportador: _Optional[bool] = ..., importa_produtos: _Optional[bool] = ..., gera_pedidos: _Optional[bool] = ...) -> None: ...

class NfeImportaXmlResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: _containers.RepeatedCompositeFieldContainer[Nfe]
    def __init__(self, nfe: _Optional[_Iterable[_Union[Nfe, _Mapping]]] = ...) -> None: ...

class NfeEnviaXmlRequest(_message.Message):
    __slots__ = ("email", "ids", "tipo_documento", "whatsapp_numero", "whatsapp_nome_destinatario", "whatsapp_integration_id", "email_integration_id", "whatsapp_template_name", "whatsapp_template_language", "message_template_id")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    TIPO_DOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NUMERO_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_NOME_DESTINATARIO_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    WHATSAPP_TEMPLATE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    tipo_documento: str
    whatsapp_numero: str
    whatsapp_nome_destinatario: str
    whatsapp_integration_id: str
    email_integration_id: str
    whatsapp_template_name: str
    whatsapp_template_language: str
    message_template_id: str
    def __init__(self, email: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ..., tipo_documento: _Optional[str] = ..., whatsapp_numero: _Optional[str] = ..., whatsapp_nome_destinatario: _Optional[str] = ..., whatsapp_integration_id: _Optional[str] = ..., email_integration_id: _Optional[str] = ..., whatsapp_template_name: _Optional[str] = ..., whatsapp_template_language: _Optional[str] = ..., message_template_id: _Optional[str] = ...) -> None: ...

class NfeEnviaXmlResponse(_message.Message):
    __slots__ = ("whatsapp_web_message", "public_download_link")
    WHATSAPP_WEB_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_DOWNLOAD_LINK_FIELD_NUMBER: _ClassVar[int]
    whatsapp_web_message: str
    public_download_link: str
    def __init__(self, whatsapp_web_message: _Optional[str] = ..., public_download_link: _Optional[str] = ...) -> None: ...

class EnviaXmlsPeriodoRequest(_message.Message):
    __slots__ = ("email", "dataInicial", "dataFinal", "tipoDocumento")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    DATAINICIAL_FIELD_NUMBER: _ClassVar[int]
    DATAFINAL_FIELD_NUMBER: _ClassVar[int]
    TIPODOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    email: str
    dataInicial: _timestamp_pb2.Timestamp
    dataFinal: _timestamp_pb2.Timestamp
    tipoDocumento: str
    def __init__(self, email: _Optional[str] = ..., dataInicial: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., dataFinal: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., tipoDocumento: _Optional[str] = ...) -> None: ...

class EnviaXmlsPeriodoResponse(_message.Message):
    __slots__ = ("status", "qtdeNfe", "qtdeNfce", "qtdeNfeEntrada", "qtdeInutilizacao", "qtdeNfse")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    QTDENFE_FIELD_NUMBER: _ClassVar[int]
    QTDENFCE_FIELD_NUMBER: _ClassVar[int]
    QTDENFEENTRADA_FIELD_NUMBER: _ClassVar[int]
    QTDEINUTILIZACAO_FIELD_NUMBER: _ClassVar[int]
    QTDENFSE_FIELD_NUMBER: _ClassVar[int]
    status: str
    qtdeNfe: int
    qtdeNfce: int
    qtdeNfeEntrada: int
    qtdeInutilizacao: int
    qtdeNfse: int
    def __init__(self, status: _Optional[str] = ..., qtdeNfe: _Optional[int] = ..., qtdeNfce: _Optional[int] = ..., qtdeNfeEntrada: _Optional[int] = ..., qtdeInutilizacao: _Optional[int] = ..., qtdeNfse: _Optional[int] = ...) -> None: ...

class GerarNFeReimpressaoRequest(_message.Message):
    __slots__ = ("ids", "pessoaCpfCnpj")
    IDS_FIELD_NUMBER: _ClassVar[int]
    PESSOACPFCNPJ_FIELD_NUMBER: _ClassVar[int]
    ids: _containers.RepeatedScalarFieldContainer[str]
    pessoaCpfCnpj: str
    def __init__(self, ids: _Optional[_Iterable[str]] = ..., pessoaCpfCnpj: _Optional[str] = ...) -> None: ...

class GerarNFeReimpressaoResponse(_message.Message):
    __slots__ = ("status", "nfe")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    NFE_FIELD_NUMBER: _ClassVar[int]
    status: str
    nfe: Nfe
    def __init__(self, status: _Optional[str] = ..., nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class NfeRecuperaProtocoloRequest(_message.Message):
    __slots__ = ("id", "tipoDocumento", "numero", "chave")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIPODOCUMENTO_FIELD_NUMBER: _ClassVar[int]
    NUMERO_FIELD_NUMBER: _ClassVar[int]
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    id: str
    tipoDocumento: str
    numero: int
    chave: str
    def __init__(self, id: _Optional[str] = ..., tipoDocumento: _Optional[str] = ..., numero: _Optional[int] = ..., chave: _Optional[str] = ...) -> None: ...

class NfeRecuperaProtocoloResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class GetDownloadLinkXmlRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetDownloadLinkXmlResponse(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class GetWsStatusRequest(_message.Message):
    __slots__ = ("tipo",)
    TIPO_FIELD_NUMBER: _ClassVar[int]
    tipo: str
    def __init__(self, tipo: _Optional[str] = ...) -> None: ...

class GetWsStatusResponse(_message.Message):
    __slots__ = ("online",)
    ONLINE_FIELD_NUMBER: _ClassVar[int]
    online: bool
    def __init__(self, online: _Optional[bool] = ...) -> None: ...

class NfeImportacaoChaveRequest(_message.Message):
    __slots__ = ("chave",)
    CHAVE_FIELD_NUMBER: _ClassVar[int]
    chave: str
    def __init__(self, chave: _Optional[str] = ...) -> None: ...

class NfeImportacaoChaveResponse(_message.Message):
    __slots__ = ("nfe",)
    NFE_FIELD_NUMBER: _ClassVar[int]
    nfe: Nfe
    def __init__(self, nfe: _Optional[_Union[Nfe, _Mapping]] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("tipoRelatorio", "list_request", "mail")
    TIPORELATORIO_FIELD_NUMBER: _ClassVar[int]
    LIST_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MAIL_FIELD_NUMBER: _ClassVar[int]
    tipoRelatorio: str
    list_request: ListNfeRequest
    mail: str
    def __init__(self, tipoRelatorio: _Optional[str] = ..., list_request: _Optional[_Union[ListNfeRequest, _Mapping]] = ..., mail: _Optional[str] = ...) -> None: ...

class ReportResponse(_message.Message):
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

class ExplainRejectionRequest(_message.Message):
    __slots__ = ("id", "ai_integration_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    AI_INTEGRATION_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    ai_integration_id: str
    def __init__(self, id: _Optional[str] = ..., ai_integration_id: _Optional[str] = ...) -> None: ...

class ExplainRejectionResponse(_message.Message):
    __slots__ = ("cstat", "original_message", "explanation", "recommended_actions", "severity")
    CSTAT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    RECOMMENDED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    cstat: str
    original_message: str
    explanation: str
    recommended_actions: _containers.RepeatedScalarFieldContainer[str]
    severity: str
    def __init__(self, cstat: _Optional[str] = ..., original_message: _Optional[str] = ..., explanation: _Optional[str] = ..., recommended_actions: _Optional[_Iterable[str]] = ..., severity: _Optional[str] = ...) -> None: ...
