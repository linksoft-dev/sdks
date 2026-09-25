// Package sdk conecta um programa à API gRPC do sistema. Os clientes de cada serviço
// ficam nos pacotes gerados em pb/; este pacote cuida da conexão, do login e das
// credenciais que toda chamada leva.
package sdk

import (
	"context"
	"crypto/tls"
	"net"
	"sync"

	authpb "github.com/linksoft-dev/sdks/go/pb/apps/auth/v1"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials"
	"google.golang.org/grpc/credentials/insecure"
	"google.golang.org/grpc/metadata"
)

// Client é a conexão com o servidor e a credencial usada nas chamadas.
type Client struct {
	conn *grpc.ClientConn

	mu     sync.RWMutex
	token  string
	bearer string
	org    string
}

// Dial abre a conexão. address é host:porta, por exemplo "app.sigeflex.com:443" ou o
// endereço próprio da revenda. Endereço local (localhost, 127.0.0.1) conecta sem TLS,
// para testar contra um servidor de desenvolvimento.
func Dial(address string, opts ...grpc.DialOption) (*Client, error) {
	c := &Client{}
	transporte := credentials.NewTLS(&tls.Config{})
	if local(address) {
		transporte = insecure.NewCredentials()
	}
	opts = append([]grpc.DialOption{
		grpc.WithTransportCredentials(transporte),
		grpc.WithChainUnaryInterceptor(c.intercept),
	}, opts...)
	conn, err := grpc.NewClient(address, opts...)
	if err != nil {
		return nil, err
	}
	c.conn = conn
	return c, nil
}

// Conn é a conexão para criar os clientes gerados, ex.: produtopb.NewProdutoServiceClient(c.Conn()).
func (c *Client) Conn() *grpc.ClientConn { return c.conn }

// Close encerra a conexão.
func (c *Client) Close() error { return c.conn.Close() }

// Login entra com o usuário da integração e passa a usar o token devolvido. org
// escolhe a empresa; vazio usa a empresa padrão do usuário.
func (c *Client) Login(ctx context.Context, username, password, org string) (*authpb.LoginResponse, error) {
	resp, err := authpb.NewAuthServiceClient(c.conn).Login(ctx, &authpb.LoginRequest{
		Username: username,
		Password: password,
		OrgId:    org,
	})
	if err != nil {
		return nil, err
	}
	if org == "" {
		org = resp.GetCurrentOrg().GetId()
	}
	c.SetToken(resp.GetToken(), org)
	return resp, nil
}

// SetToken usa um token de login já obtido e a empresa das próximas chamadas.
func (c *Client) SetToken(token, org string) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.token, c.bearer, c.org = token, "", org
}

// SetBearer usa o token de uma conexão OAuth2 e a empresa das próximas chamadas.
func (c *Client) SetBearer(bearer, org string) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.token, c.bearer, c.org = "", bearer, org
}

// Org é a empresa em que as chamadas operam.
func (c *Client) Org() string {
	c.mu.RLock()
	defer c.mu.RUnlock()
	return c.org
}

// intercept põe a credencial e a empresa em cada chamada. O servidor renova o token
// de login na segunda metade da validade e devolve o novo no trailer x-new-token.
func (c *Client) intercept(ctx context.Context, method string, req, reply any, cc *grpc.ClientConn, invoker grpc.UnaryInvoker, opts ...grpc.CallOption) error {
	c.mu.RLock()
	token, bearer, org := c.token, c.bearer, c.org
	c.mu.RUnlock()
	switch {
	case token != "":
		ctx = metadata.AppendToOutgoingContext(ctx, "token", token)
	case bearer != "":
		ctx = metadata.AppendToOutgoingContext(ctx, "authorization", "Bearer "+bearer)
	}
	if org != "" {
		ctx = metadata.AppendToOutgoingContext(ctx, "org", org)
	}

	var trailer metadata.MD
	err := invoker(ctx, method, req, reply, cc, append(opts, grpc.Trailer(&trailer))...)
	if novo := trailer.Get("x-new-token"); len(novo) > 0 && novo[0] != "" {
		c.mu.Lock()
		if c.token == token {
			c.token = novo[0]
		}
		c.mu.Unlock()
	}
	return err
}

func local(address string) bool {
	host, _, err := net.SplitHostPort(address)
	if err != nil {
		host = address
	}
	return host == "localhost" || host == "127.0.0.1" || host == "::1"
}
