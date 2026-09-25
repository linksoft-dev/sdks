import unittest
from concurrent import futures

import grpc

from linksoft_sdk import Client
from linksoft_sdk.pb.apps.auth.v1 import auth_pb2, auth_pb2_grpc

ECO = "/teste.Eco/Chama"


class _Servidor(auth_pb2_grpc.AuthServiceServicer):
    """Registra a metadata de cada chamada e devolve o token renovado quando
    novo_token está preenchido, como o servidor faz na segunda metade da validade."""

    def __init__(self):
        self.recebida = []
        self.novo_token = ""

    def Login(self, requisicao, contexto):
        return auth_pb2.LoginResponse(
            token="token-do-login", current_org=auth_pb2.orgLoginModel(id="empresa-padrao")
        )

    def eco(self, requisicao, contexto):
        self.recebida.append(dict(contexto.invocation_metadata()))
        if self.novo_token:
            contexto.set_trailing_metadata((("x-new-token", self.novo_token),))
        return requisicao


class ClienteTest(unittest.TestCase):
    def setUp(self):
        self.servidor = _Servidor()
        self.grpc = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        auth_pb2_grpc.add_AuthServiceServicer_to_server(self.servidor, self.grpc)
        self.grpc.add_generic_rpc_handlers(
            (grpc.method_handlers_generic_handler("teste.Eco", {"Chama": grpc.unary_unary_rpc_method_handler(self.servidor.eco)}),)
        )
        porta = self.grpc.add_insecure_port("localhost:0")
        self.grpc.start()
        self.cliente = Client(f"localhost:{porta}")

    def tearDown(self):
        self.cliente.close()
        self.grpc.stop(None)

    def chama(self):
        return self.cliente.channel.unary_unary(ECO)(b"ok")

    def test_login_passa_a_usar_o_token_e_a_empresa_padrao(self):
        self.cliente.login("integracao@empresa.com", "senha")
        self.chama()

        self.assertEqual(self.cliente.org, "empresa-padrao")
        self.assertEqual(self.servidor.recebida[0]["token"], "token-do-login")
        self.assertEqual(self.servidor.recebida[0]["org"], "empresa-padrao")

    def test_login_com_empresa_escolhida(self):
        self.cliente.login("integracao@empresa.com", "senha", org="outra-empresa")

        self.assertEqual(self.cliente.org, "outra-empresa")

    def test_token_renovado_pelo_servidor(self):
        self.cliente.set_token("token-antigo", "empresa-1")

        self.servidor.novo_token = "token-novo"
        self.chama()
        self.servidor.novo_token = ""
        self.chama()

        self.assertEqual(self.servidor.recebida[0]["token"], "token-antigo")
        self.assertEqual(self.servidor.recebida[1]["token"], "token-novo")

    def test_conexao_oauth(self):
        self.cliente.set_bearer("token-oauth", "empresa-2")
        self.chama()

        recebida = self.servidor.recebida[0]
        self.assertEqual(recebida["authorization"], "Bearer token-oauth")
        self.assertEqual(recebida["org"], "empresa-2")
        self.assertNotIn("token", recebida)


if __name__ == "__main__":
    unittest.main()
