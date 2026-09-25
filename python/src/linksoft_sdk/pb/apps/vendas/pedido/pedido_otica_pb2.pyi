from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Otica(_message.Message):
    __slots__ = ("tipoLenteId", "tipoLenteNome", "tipoLente2Id", "tipoLente2Nome", "tipoMaterialId", "tipoMaterialNome", "tipoMaterial2Id", "tipoMaterial2Nome", "tipoTratamentoId", "tipoTratamentoNome", "tipoTratamento2Id", "tipoTratamento2Nome", "longeDir", "pertoDir", "longeEsq", "pertoEsq", "acuidadeVisual", "vencimentoLente", "fornecedorId", "fornecedorNome", "armacaoCor", "armacaoCor2", "armacaoTamanho", "armacaoTamanho2", "armacaoAltura", "armacaoAltura2", "armacaoTipoId", "armacaoTipoNome", "armacaoTipo2Id", "armacaoTipo2Nome")
    TIPOLENTEID_FIELD_NUMBER: _ClassVar[int]
    TIPOLENTENOME_FIELD_NUMBER: _ClassVar[int]
    TIPOLENTE2ID_FIELD_NUMBER: _ClassVar[int]
    TIPOLENTE2NOME_FIELD_NUMBER: _ClassVar[int]
    TIPOMATERIALID_FIELD_NUMBER: _ClassVar[int]
    TIPOMATERIALNOME_FIELD_NUMBER: _ClassVar[int]
    TIPOMATERIAL2ID_FIELD_NUMBER: _ClassVar[int]
    TIPOMATERIAL2NOME_FIELD_NUMBER: _ClassVar[int]
    TIPOTRATAMENTOID_FIELD_NUMBER: _ClassVar[int]
    TIPOTRATAMENTONOME_FIELD_NUMBER: _ClassVar[int]
    TIPOTRATAMENTO2ID_FIELD_NUMBER: _ClassVar[int]
    TIPOTRATAMENTO2NOME_FIELD_NUMBER: _ClassVar[int]
    LONGEDIR_FIELD_NUMBER: _ClassVar[int]
    PERTODIR_FIELD_NUMBER: _ClassVar[int]
    LONGEESQ_FIELD_NUMBER: _ClassVar[int]
    PERTOESQ_FIELD_NUMBER: _ClassVar[int]
    ACUIDADEVISUAL_FIELD_NUMBER: _ClassVar[int]
    VENCIMENTOLENTE_FIELD_NUMBER: _ClassVar[int]
    FORNECEDORID_FIELD_NUMBER: _ClassVar[int]
    FORNECEDORNOME_FIELD_NUMBER: _ClassVar[int]
    ARMACAOCOR_FIELD_NUMBER: _ClassVar[int]
    ARMACAOCOR2_FIELD_NUMBER: _ClassVar[int]
    ARMACAOTAMANHO_FIELD_NUMBER: _ClassVar[int]
    ARMACAOTAMANHO2_FIELD_NUMBER: _ClassVar[int]
    ARMACAOALTURA_FIELD_NUMBER: _ClassVar[int]
    ARMACAOALTURA2_FIELD_NUMBER: _ClassVar[int]
    ARMACAOTIPOID_FIELD_NUMBER: _ClassVar[int]
    ARMACAOTIPONOME_FIELD_NUMBER: _ClassVar[int]
    ARMACAOTIPO2ID_FIELD_NUMBER: _ClassVar[int]
    ARMACAOTIPO2NOME_FIELD_NUMBER: _ClassVar[int]
    tipoLenteId: str
    tipoLenteNome: str
    tipoLente2Id: str
    tipoLente2Nome: str
    tipoMaterialId: str
    tipoMaterialNome: str
    tipoMaterial2Id: str
    tipoMaterial2Nome: str
    tipoTratamentoId: str
    tipoTratamentoNome: str
    tipoTratamento2Id: str
    tipoTratamento2Nome: str
    longeDir: DadosLente
    pertoDir: DadosLente
    longeEsq: DadosLente
    pertoEsq: DadosLente
    acuidadeVisual: AcuidadeVisual
    vencimentoLente: str
    fornecedorId: str
    fornecedorNome: str
    armacaoCor: str
    armacaoCor2: str
    armacaoTamanho: int
    armacaoTamanho2: int
    armacaoAltura: float
    armacaoAltura2: float
    armacaoTipoId: str
    armacaoTipoNome: str
    armacaoTipo2Id: str
    armacaoTipo2Nome: str
    def __init__(self, tipoLenteId: _Optional[str] = ..., tipoLenteNome: _Optional[str] = ..., tipoLente2Id: _Optional[str] = ..., tipoLente2Nome: _Optional[str] = ..., tipoMaterialId: _Optional[str] = ..., tipoMaterialNome: _Optional[str] = ..., tipoMaterial2Id: _Optional[str] = ..., tipoMaterial2Nome: _Optional[str] = ..., tipoTratamentoId: _Optional[str] = ..., tipoTratamentoNome: _Optional[str] = ..., tipoTratamento2Id: _Optional[str] = ..., tipoTratamento2Nome: _Optional[str] = ..., longeDir: _Optional[_Union[DadosLente, _Mapping]] = ..., pertoDir: _Optional[_Union[DadosLente, _Mapping]] = ..., longeEsq: _Optional[_Union[DadosLente, _Mapping]] = ..., pertoEsq: _Optional[_Union[DadosLente, _Mapping]] = ..., acuidadeVisual: _Optional[_Union[AcuidadeVisual, _Mapping]] = ..., vencimentoLente: _Optional[str] = ..., fornecedorId: _Optional[str] = ..., fornecedorNome: _Optional[str] = ..., armacaoCor: _Optional[str] = ..., armacaoCor2: _Optional[str] = ..., armacaoTamanho: _Optional[int] = ..., armacaoTamanho2: _Optional[int] = ..., armacaoAltura: _Optional[float] = ..., armacaoAltura2: _Optional[float] = ..., armacaoTipoId: _Optional[str] = ..., armacaoTipoNome: _Optional[str] = ..., armacaoTipo2Id: _Optional[str] = ..., armacaoTipo2Nome: _Optional[str] = ...) -> None: ...

class AcuidadeVisual(_message.Message):
    __slots__ = ("sc", "cc")
    SC_FIELD_NUMBER: _ClassVar[int]
    CC_FIELD_NUMBER: _ClassVar[int]
    sc: Sc
    cc: Cc
    def __init__(self, sc: _Optional[_Union[Sc, _Mapping]] = ..., cc: _Optional[_Union[Cc, _Mapping]] = ...) -> None: ...

class Sc(_message.Message):
    __slots__ = ("olhoDireito", "olhoEsquerdo", "ambosOlhos")
    OLHODIREITO_FIELD_NUMBER: _ClassVar[int]
    OLHOESQUERDO_FIELD_NUMBER: _ClassVar[int]
    AMBOSOLHOS_FIELD_NUMBER: _ClassVar[int]
    olhoDireito: Acuidade
    olhoEsquerdo: Acuidade
    ambosOlhos: Acuidade
    def __init__(self, olhoDireito: _Optional[_Union[Acuidade, _Mapping]] = ..., olhoEsquerdo: _Optional[_Union[Acuidade, _Mapping]] = ..., ambosOlhos: _Optional[_Union[Acuidade, _Mapping]] = ...) -> None: ...

class Cc(_message.Message):
    __slots__ = ("olhoDireito", "olhoEsquerdo", "ambosOlhos")
    OLHODIREITO_FIELD_NUMBER: _ClassVar[int]
    OLHOESQUERDO_FIELD_NUMBER: _ClassVar[int]
    AMBOSOLHOS_FIELD_NUMBER: _ClassVar[int]
    olhoDireito: Acuidade
    olhoEsquerdo: Acuidade
    ambosOlhos: Acuidade
    def __init__(self, olhoDireito: _Optional[_Union[Acuidade, _Mapping]] = ..., olhoEsquerdo: _Optional[_Union[Acuidade, _Mapping]] = ..., ambosOlhos: _Optional[_Union[Acuidade, _Mapping]] = ...) -> None: ...

class Acuidade(_message.Message):
    __slots__ = ("longe", "perto")
    LONGE_FIELD_NUMBER: _ClassVar[int]
    PERTO_FIELD_NUMBER: _ClassVar[int]
    longe: str
    perto: str
    def __init__(self, longe: _Optional[str] = ..., perto: _Optional[str] = ...) -> None: ...

class DadosLente(_message.Message):
    __slots__ = ("esf", "cil", "eixo", "dnp", "dp", "co", "pl", "adicao")
    ESF_FIELD_NUMBER: _ClassVar[int]
    CIL_FIELD_NUMBER: _ClassVar[int]
    EIXO_FIELD_NUMBER: _ClassVar[int]
    DNP_FIELD_NUMBER: _ClassVar[int]
    DP_FIELD_NUMBER: _ClassVar[int]
    CO_FIELD_NUMBER: _ClassVar[int]
    PL_FIELD_NUMBER: _ClassVar[int]
    ADICAO_FIELD_NUMBER: _ClassVar[int]
    esf: float
    cil: float
    eixo: float
    dnp: float
    dp: float
    co: float
    pl: float
    adicao: float
    def __init__(self, esf: _Optional[float] = ..., cil: _Optional[float] = ..., eixo: _Optional[float] = ..., dnp: _Optional[float] = ..., dp: _Optional[float] = ..., co: _Optional[float] = ..., pl: _Optional[float] = ..., adicao: _Optional[float] = ...) -> None: ...
