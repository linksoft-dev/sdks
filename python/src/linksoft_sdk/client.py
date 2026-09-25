"""Conexão, login e credenciais das chamadas gRPC."""

import threading
from typing import Optional

import grpc

from linksoft_sdk.pb.apps.auth.v1 import auth_pb2, auth_pb2_grpc

_LOCAIS = ("localhost", "127.0.0.1", "[::1]", "::1")


class Client:
    """Conexão com o servidor e a credencial usada nas chamadas.

    address é host:porta, por exemplo "app.sigeflex.com:443" ou o endereço próprio da
    revenda. Endereço local (localhost, 127.0.0.1) conecta sem TLS, para testar contra
    um servidor de desenvolvimento.
    """

    def __init__(self, address: str):
        host = address.rsplit(":", 1)[0]
        if host in _LOCAIS:
            canal = grpc.insecure_channel(address)
        else:
            canal = grpc.secure_channel(address, grpc.ssl_channel_credentials())
        self._credencial = _Credencial()
        self._bruto = canal
        self.channel = grpc.intercept_channel(canal, self._credencial)

    def login(self, username: str, password: str, org: Optional[str] = None):
        """Entra com o usuário da integração e passa a usar o token devolvido.

        org escolhe a empresa; sem ela vale a empresa padrão do usuário.
        """
        resposta = auth_pb2_grpc.AuthServiceStub(self.channel).Login(
            auth_pb2.LoginRequest(username=username, password=password, org_id=org or "")
        )
        self.set_token(resposta.token, org or resposta.current_org.id)
        return resposta

    def set_token(self, token: str, org: str) -> None:
        """Usa um token de login já obtido e a empresa das próximas chamadas."""
        self._credencial.define(token=token, bearer="", org=org)

    def set_bearer(self, bearer: str, org: str) -> None:
        """Usa o token de uma conexão OAuth2 e a empresa das próximas chamadas."""
        self._credencial.define(token="", bearer=bearer, org=org)

    @property
    def org(self) -> str:
        """Empresa em que as chamadas operam."""
        return self._credencial.org

    def close(self) -> None:
        self._bruto.close()

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


class _Credencial(grpc.UnaryUnaryClientInterceptor):
    """Põe a credencial e a empresa em cada chamada.

    O servidor renova o token de login na segunda metade da validade e devolve o novo
    no trailer x-new-token.
    """

    def __init__(self):
        self._trava = threading.Lock()
        self.token = self.bearer = self.org = ""

    def define(self, token: str, bearer: str, org: str) -> None:
        with self._trava:
            self.token, self.bearer, self.org = token, bearer, org

    def intercept_unary_unary(self, continuation, detalhes, requisicao):
        with self._trava:
            token, bearer, org = self.token, self.bearer, self.org
        metadata = list(detalhes.metadata or [])
        if token:
            metadata.append(("token", token))
        elif bearer:
            metadata.append(("authorization", "Bearer " + bearer))
        if org:
            metadata.append(("org", org))

        resultado = continuation(_Detalhes(detalhes, metadata), requisicao)
        for chave, valor in resultado.trailing_metadata() or ():
            if chave == "x-new-token" and valor:
                with self._trava:
                    if self.token == token:
                        self.token = valor
        return resultado


class _Detalhes(grpc.ClientCallDetails):
    def __init__(self, base, metadata):
        self.method = base.method
        self.timeout = base.timeout
        self.metadata = metadata
        self.credentials = base.credentials
        self.wait_for_ready = base.wait_for_ready
        self.compression = base.compression
