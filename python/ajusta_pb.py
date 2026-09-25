"""Ajusta o código gerado dos protos para morar dentro do pacote linksoft_sdk.

O gerador escreve imports absolutos a partir da raiz dos protos ("from apps.x import
y_pb2"). Dentro de um pacote instalado eles precisam do prefixo linksoft_sdk.pb, senão
"apps", "common" e "filter" viram pacotes de primeiro nível e colidem com os do
programa de quem usa o SDK. Os protos do Google saem dos pacotes protobuf e
googleapis-common-protos.
"""
import pathlib
import re
import shutil
import sys

PREFIXO = "linksoft_sdk.pb"


def ajusta(raiz: pathlib.Path) -> None:
    shutil.rmtree(raiz / "google", ignore_errors=True)
    proprios = sorted(p.name for p in raiz.iterdir() if p.is_dir())
    nomes = "|".join(re.escape(n) for n in proprios)
    importa = re.compile(rf"^(from|import) ({nomes})([. ])", re.M)
    modulo = re.compile(rf"(BuildTopDescriptorsAndMessages\(DESCRIPTOR, ')({nomes})\.")

    for arquivo in list(raiz.rglob("*.py")) + list(raiz.rglob("*.pyi")):
        texto = arquivo.read_text(encoding="utf-8")
        novo = importa.sub(rf"\1 {PREFIXO}.\2\3", texto)
        novo = modulo.sub(rf"\1{PREFIXO}.\2.", novo)
        if novo != texto:
            arquivo.write_text(novo, encoding="utf-8")

    for pasta in [raiz, *[p for p in raiz.rglob("*") if p.is_dir()]]:
        (pasta / "__init__.py").touch()


if __name__ == "__main__":
    ajusta(pathlib.Path(sys.argv[1]))
