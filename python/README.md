# SDK Python

```bash
pip install "git+https://github.com/linksoft-dev/sdks.git#subdirectory=python"
```

```python
from linksoft_sdk import Client
from linksoft_sdk.pb.apps.estoque.produto import produto_pb2, produto_pb2_grpc

with Client("app.suaempresa.com.br:443") as cliente:
    cliente.login(usuario, senha)
    produtos = produto_pb2_grpc.ProdutoServiceStub(cliente.channel)
    resposta = produtos.List(produto_pb2.ListProdutoRequest(page_size=10))
```

Os módulos de cada serviço ficam em `linksoft_sdk.pb`, na mesma estrutura de pastas dos
contratos (ex.: `linksoft_sdk.pb.apps.vendas.pedido`). O exemplo completo está em
`exemplos/cliente.py`.
