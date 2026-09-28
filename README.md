# SDKs da API

Clientes gRPC da API do sistema, gerados dos mesmos contratos que o servidor usa. Cada
SDK traz os serviços abertos a integrações — os mesmos da [referência REST](https://docs.sigeflex.com/api) —
e um cliente pronto para conectar, entrar e manter a credencial das chamadas.

| Linguagem | Instalação |
|-----------|------------|
| Go (1.24+) | `go get github.com/linksoft-dev/sdks/go@latest` |
| Python (3.9+) | `pip install "git+https://github.com/linksoft-dev/sdks.git#subdirectory=python"` |

## Antes de começar

- A empresa precisa do **módulo API** contratado. Sem ele as chamadas voltam com
  `FAILED_PRECONDITION`.
- Crie um usuário só para a integração, num grupo com as permissões do que ela vai
  fazer. A integração enxerga exatamente o que esse usuário enxerga.
- O endereço é o mesmo que você usa para acessar o sistema, na porta 443.

## Exemplo

Os dois SDKs trazem o mesmo exemplo: o sistema de uma loja consulta produtos, clientes e
os últimos pedidos; com `GRAVAR=1` cadastra um cliente de exemplo e lança um pedido.

```bash
export API_ENDERECO=app.suaempresa.com.br:443
export API_USUARIO=integracao@suaempresa.com.br
export API_SENHA='senha do usuário da integração'

cd go && go run ./exemplos/cliente
cd python && python exemplos/cliente.py
```

`API_ORG` escolhe a empresa quando o usuário tem acesso a mais de uma.

## Credenciais

- **Usuário e senha**: `Login` devolve um token de sessão; o cliente passa a enviá-lo
  com a empresa em toda chamada e troca pelo token renovado quando o servidor devolve
  um novo.
- **Conexão OAuth2**: com o token de um aplicativo autorizado pelo usuário, use
  `SetBearer` (Go) ou `set_bearer` (Python).

## Testar sem programar

- **Postman ou Apidog, por REST**: importe a
  [coleção com todas as rotas](https://docs.sigeflex.com/openapi/api.postman_collection.json)
  e preencha `usuario` e `senha` nas variáveis dela; o login é automático.

Guia completo, com a lista de áreas e a referência de cada rota:
https://docs.sigeflex.com/manual-usuario/integracoes/api
