"""Exemplo de integração pelo SDK: o sistema de uma loja consulta o catálogo, os
clientes e os últimos pedidos da empresa. Com GRAVAR=1 ele também cadastra um cliente
de exemplo (ou reaproveita o que já existe com o mesmo CPF) e lança um pedido para ele
com o primeiro produto do catálogo.

    API_ENDERECO=app.suaempresa.com.br:443 \\
    API_USUARIO=integracao@suaempresa.com.br \\
    API_SENHA='senha do usuário da integração' \\
    python exemplos/cliente.py

API_ORG escolhe a empresa quando o usuário tem acesso a mais de uma; sem ela vale a
empresa padrão do usuário.
"""

import os
import sys

import grpc

from linksoft_sdk import Client
from linksoft_sdk.pb.apps.estoque.produto import produto_pb2, produto_pb2_grpc
from linksoft_sdk.pb.apps.person import person_pb2, person_pb2_grpc
from linksoft_sdk.pb.apps.vendas.pedido import pedido_pb2, pedido_pb2_grpc
from linksoft_sdk.pb.filter import filter_pb2

# CPF válido reservado para o cliente de exemplo: rodar de novo reaproveita o cadastro.
CPF_DO_EXEMPLO = "11144477735"


def variavel(nome):
    valor = os.environ.get(nome)
    if not valor:
        sys.exit(f"Informe {nome}. Veja o comentário no início do arquivo.")
    return valor


def cliente_de_exemplo(pessoas):
    """Devolve o cliente do CPF de exemplo, cadastrando-o na primeira vez."""
    achados = pessoas.List(person_pb2.ListRequest(cpf_cnpjs=[CPF_DO_EXEMPLO]))
    if achados.person_list:
        return achados.person_list[0]
    criado = pessoas.Create(
        person_pb2.CreateRequest(
            person=person_pb2.Person(
                name="Cliente de exemplo da integração",
                cpf_cnpj=CPF_DO_EXEMPLO,
                tags=[person_pb2.PersonTag(value="customer")],
            )
        )
    )
    return criado.person


def lanca_pedido(pedidos, comprador, item):
    """Abre o pedido e inclui o item. O item vai por AddProduct, como na tela: é ele
    que traz nome, unidade e preço do cadastro e calcula os totais do pedido."""
    aberto = pedidos.Create(
        pedido_pb2.CreatePedidoRequest(
            pedido=pedido_pb2.Pedido(
                tipo="ped",
                pessoa=pedido_pb2.Pessoa(id=comprador.id, nome=comprador.name),
                obs="Pedido de exemplo lançado pela API",
            )
        )
    )
    pedidos.AddProduct(
        pedido_pb2.AddProductRequest(
            parentId=aberto.pedido.id,
            productId=item.id,
            product=pedido_pb2.Produto(produtoId=item.id, quantidade=2),
        )
    )
    return pedidos.Get(pedido_pb2.GetPedidoRequest(id=aberto.pedido.id)).pedido


def main():
    endereco = variavel("API_ENDERECO")
    usuario = variavel("API_USUARIO")
    senha = variavel("API_SENHA")

    with Client(endereco) as cliente:
        login = cliente.login(usuario, senha, os.environ.get("API_ORG"))
        print(f"Conectado como {login.name} na empresa {cliente.org}")

        produtos = produto_pb2_grpc.ProdutoServiceStub(cliente.channel)
        pessoas = person_pb2_grpc.PersonServiceStub(cliente.channel)
        pedidos = pedido_pb2_grpc.PedidoServiceStub(cliente.channel)

        catalogo = produtos.List(produto_pb2.ListProdutoRequest(page_size=5)).produtoList
        print("\nProdutos:")
        for p in catalogo:
            print(f"  {p.nome:<45} R$ {p.valorUnitario:>10.2f}")

        clientes = pessoas.List(person_pb2.ListRequest(tipo="customer", page_size=5)).person_list
        print("\nClientes:")
        for c in clientes:
            print(f"  {c.name:<45} {c.cpf_cnpj}")

        ultimos = pedidos.List(
            pedido_pb2.ListPedidoRequest(
                types=["ped"],
                filter=filter_pb2.Filter(
                    limit=5,
                    orderBy=[filter_pb2.OrderBy(field_name="createdAt", direction=filter_pb2.DESC)],
                ),
            )
        ).pedidoList
        print("\nÚltimos pedidos:")
        for p in ultimos:
            print(f"  nº {p.numero:<6} {p.pessoa.nome:<38} R$ {p.valorTotal:>10.2f}  {p.situacao}")

        if os.environ.get("GRAVAR") != "1":
            print("\nPara cadastrar um cliente e lançar um pedido de exemplo, rode de novo com GRAVAR=1.")
            return
        if not catalogo:
            print("\nCadastre ao menos um produto para lançar o pedido de exemplo.")
            return

        lancado = lanca_pedido(pedidos, cliente_de_exemplo(pessoas), catalogo[0])
        print(
            f"\nPedido nº {lancado.numero} lançado para {lancado.pessoa.nome}: "
            f"R$ {lancado.valorTotal:.2f} ({lancado.situacao})"
        )


if __name__ == "__main__":
    try:
        main()
    except grpc.RpcError as erro:
        sys.exit(f"Falha na chamada: {erro.code().name} - {erro.details()}")
