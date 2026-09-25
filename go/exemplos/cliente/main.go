// Exemplo de integração pelo SDK: o sistema de uma loja consulta o catálogo, os
// clientes e os últimos pedidos da empresa. Com GRAVAR=1 ele também cadastra um
// cliente de exemplo (ou reaproveita o que já existe com o mesmo CPF) e lança um
// pedido para ele com o primeiro produto do catálogo.
//
//	API_ENDERECO=app.suaempresa.com.br:443 \
//	API_USUARIO=integracao@suaempresa.com.br \
//	API_SENHA='senha do usuário da integração' \
//	go run ./exemplos/cliente
//
// API_ORG escolhe a empresa quando o usuário tem acesso a mais de uma; sem ela vale
// a empresa padrão do usuário.
package main

import (
	"context"
	"fmt"
	"os"
	"time"

	sdk "github.com/linksoft-dev/sdks/go"
	"github.com/linksoft-dev/sdks/go/pb/apps/estoque/produto"
	"github.com/linksoft-dev/sdks/go/pb/apps/person"
	"github.com/linksoft-dev/sdks/go/pb/apps/vendas/pedido"
	"github.com/linksoft-dev/sdks/go/pb/filter"
)

// CPF válido reservado para o cliente de exemplo: rodar de novo reaproveita o cadastro.
const cpfDoExemplo = "11144477735"

func main() {
	endereco := variavel("API_ENDERECO")
	usuario := variavel("API_USUARIO")
	senha := variavel("API_SENHA")

	ctx, cancel := context.WithTimeout(context.Background(), time.Minute)
	defer cancel()

	cliente, err := sdk.Dial(endereco)
	confere(err, "conectar")
	defer cliente.Close()

	login, err := cliente.Login(ctx, usuario, senha, os.Getenv("API_ORG"))
	confere(err, "entrar")
	fmt.Printf("Conectado como %s na empresa %s\n", login.GetName(), cliente.Org())

	produtos := produto.NewProdutoServiceClient(cliente.Conn())
	pessoas := person.NewPersonServiceClient(cliente.Conn())
	pedidos := pedido.NewPedidoServiceClient(cliente.Conn())

	catalogo, err := produtos.List(ctx, &produto.ListProdutoRequest{PageSize: 5})
	confere(err, "listar produtos")
	fmt.Println("\nProdutos:")
	for _, p := range catalogo.GetProdutoList() {
		fmt.Printf("  %-45s R$ %10.2f\n", p.GetNome(), p.GetValorUnitario())
	}

	clientes, err := pessoas.List(ctx, &person.ListRequest{Tipo: "customer", PageSize: 5})
	confere(err, "listar clientes")
	fmt.Println("\nClientes:")
	for _, c := range clientes.GetPersonList() {
		fmt.Printf("  %-45s %s\n", c.GetName(), c.GetCpfCnpj())
	}

	ultimos, err := pedidos.List(ctx, &pedido.ListPedidoRequest{
		Types: []string{"ped"},
		Filter: &filter.Filter{
			Limit:   5,
			OrderBy: []*filter.OrderBy{{FieldName: "createdAt", Direction: filter.Direction_DESC}},
		},
	})
	confere(err, "listar pedidos")
	fmt.Println("\nÚltimos pedidos:")
	for _, p := range ultimos.GetPedidoList() {
		fmt.Printf("  nº %-6d %-38s R$ %10.2f  %s\n", p.GetNumero(), p.GetPessoa().GetNome(), p.GetValorTotal(), p.GetSituacao())
	}

	if os.Getenv("GRAVAR") != "1" {
		fmt.Println("\nPara cadastrar um cliente e lançar um pedido de exemplo, rode de novo com GRAVAR=1.")
		return
	}
	if len(catalogo.GetProdutoList()) == 0 {
		fmt.Println("\nCadastre ao menos um produto para lançar o pedido de exemplo.")
		return
	}

	comprador := clienteDeExemplo(ctx, pessoas)
	lancado := lancaPedido(ctx, pedidos, comprador, catalogo.GetProdutoList()[0])
	fmt.Printf("\nPedido nº %d lançado para %s: R$ %.2f (%s)\n",
		lancado.GetNumero(), lancado.GetPessoa().GetNome(), lancado.GetValorTotal(), lancado.GetSituacao())
}

// clienteDeExemplo devolve o cliente do CPF de exemplo, cadastrando-o na primeira vez.
func clienteDeExemplo(ctx context.Context, pessoas person.PersonServiceClient) *person.Person {
	achados, err := pessoas.List(ctx, &person.ListRequest{CpfCnpjs: []string{cpfDoExemplo}})
	confere(err, "procurar o cliente de exemplo")
	if len(achados.GetPersonList()) > 0 {
		return achados.GetPersonList()[0]
	}
	criado, err := pessoas.Create(ctx, &person.CreateRequest{Person: &person.Person{
		Name:    "Cliente de exemplo da integração",
		CpfCnpj: cpfDoExemplo,
		Tags:    []*person.PersonTag{{Value: "customer"}},
	}})
	confere(err, "cadastrar o cliente de exemplo")
	return criado.GetPerson()
}

// lancaPedido abre o pedido e inclui o item. O item vai por AddProduct, como na tela:
// é ele que traz nome, unidade e preço do cadastro e calcula os totais do pedido.
func lancaPedido(ctx context.Context, pedidos pedido.PedidoServiceClient, comprador *person.Person, item *produto.Produto) *pedido.Pedido {
	aberto, err := pedidos.Create(ctx, &pedido.CreatePedidoRequest{Pedido: &pedido.Pedido{
		Tipo:   "ped",
		Pessoa: &pedido.Pessoa{Id: comprador.GetId(), Nome: comprador.GetName()},
		Obs:    "Pedido de exemplo lançado pela API",
	}})
	confere(err, "abrir o pedido")

	_, err = pedidos.AddProduct(ctx, &pedido.AddProductRequest{
		ParentId:  aberto.GetPedido().GetId(),
		ProductId: item.GetId(),
		Product:   &pedido.Produto{ProdutoId: item.GetId(), Quantidade: 2},
	})
	confere(err, "incluir o item")

	lancado, err := pedidos.Get(ctx, &pedido.GetPedidoRequest{Id: aberto.GetPedido().GetId()})
	confere(err, "ler o pedido")
	return lancado.GetPedido()
}

func variavel(nome string) string {
	valor := os.Getenv(nome)
	if valor == "" {
		fmt.Fprintf(os.Stderr, "Informe %s. Veja o comentário no início do arquivo.\n", nome)
		os.Exit(2)
	}
	return valor
}

func confere(err error, etapa string) {
	if err != nil {
		fmt.Fprintf(os.Stderr, "Falha ao %s: %v\n", etapa, err)
		os.Exit(1)
	}
}
