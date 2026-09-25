# SDK Go

```bash
go get github.com/linksoft-dev/sdks/go@latest
```

```go
cliente, err := sdk.Dial("app.suaempresa.com.br:443")
if err != nil { ... }
defer cliente.Close()

if _, err := cliente.Login(ctx, usuario, senha, ""); err != nil { ... }

produtos := produto.NewProdutoServiceClient(cliente.Conn())
resp, err := produtos.List(ctx, &produto.ListProdutoRequest{PageSize: 10})
```

Os clientes de cada serviço ficam em `pb/`, na mesma estrutura de pastas dos contratos
(ex.: `pb/apps/vendas/pedido`). O exemplo completo está em `exemplos/cliente`.
