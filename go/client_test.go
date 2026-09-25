package sdk

import (
	"context"
	"net"
	"testing"

	authpb "github.com/linksoft-dev/sdks/go/pb/apps/auth/v1"
	"google.golang.org/grpc"
	healthpb "google.golang.org/grpc/health/grpc_health_v1"
	"google.golang.org/grpc/metadata"
	"google.golang.org/grpc/test/bufconn"
)

// servidor registra a metadata de cada chamada e devolve o token renovado quando
// novoToken está preenchido, como o servidor faz na segunda metade da validade.
type servidor struct {
	authpb.UnimplementedAuthServiceServer
	healthpb.UnimplementedHealthServer
	recebida  []metadata.MD
	novoToken string
}

func (s *servidor) Login(_ context.Context, req *authpb.LoginRequest) (*authpb.LoginResponse, error) {
	return &authpb.LoginResponse{Token: "token-do-login", CurrentOrg: &authpb.OrgLoginModel{Id: "empresa-padrao"}}, nil
}

func (s *servidor) Check(ctx context.Context, _ *healthpb.HealthCheckRequest) (*healthpb.HealthCheckResponse, error) {
	md, _ := metadata.FromIncomingContext(ctx)
	s.recebida = append(s.recebida, md)
	if s.novoToken != "" {
		_ = grpc.SetTrailer(ctx, metadata.Pairs("x-new-token", s.novoToken))
	}
	return &healthpb.HealthCheckResponse{}, nil
}

func conecta(t *testing.T) (*Client, *servidor) {
	t.Helper()
	lis := bufconn.Listen(1 << 20)
	s := &servidor{}
	srv := grpc.NewServer()
	authpb.RegisterAuthServiceServer(srv, s)
	healthpb.RegisterHealthServer(srv, s)
	go srv.Serve(lis)
	t.Cleanup(srv.Stop)

	c, err := Dial("localhost:1", grpc.WithContextDialer(func(ctx context.Context, _ string) (net.Conn, error) {
		return lis.DialContext(ctx)
	}))
	if err != nil {
		t.Fatal(err)
	}
	t.Cleanup(func() { c.Close() })
	return c, s
}

func chama(t *testing.T, c *Client) {
	t.Helper()
	if _, err := healthpb.NewHealthClient(c.Conn()).Check(context.Background(), &healthpb.HealthCheckRequest{}); err != nil {
		t.Fatal(err)
	}
}

func valor(md metadata.MD, chave string) string {
	if v := md.Get(chave); len(v) > 0 {
		return v[0]
	}
	return ""
}

func TestLoginPassaAUsarOTokenEAEmpresaPadrao(t *testing.T) {
	c, s := conecta(t)

	if _, err := c.Login(context.Background(), "integracao@empresa.com", "senha", ""); err != nil {
		t.Fatal(err)
	}
	chama(t, c)

	if c.Org() != "empresa-padrao" {
		t.Fatalf("empresa = %q", c.Org())
	}
	md := s.recebida[0]
	if valor(md, "token") != "token-do-login" || valor(md, "org") != "empresa-padrao" {
		t.Fatalf("credencial enviada: %v", md)
	}
}

func TestLoginComEmpresaEscolhida(t *testing.T) {
	c, _ := conecta(t)

	if _, err := c.Login(context.Background(), "integracao@empresa.com", "senha", "outra-empresa"); err != nil {
		t.Fatal(err)
	}

	if c.Org() != "outra-empresa" {
		t.Fatalf("empresa = %q", c.Org())
	}
}

// O token renovado que volta no trailer passa a valer na chamada seguinte.
func TestTokenRenovadoPeloServidor(t *testing.T) {
	c, s := conecta(t)
	c.SetToken("token-antigo", "empresa-1")

	s.novoToken = "token-novo"
	chama(t, c)
	s.novoToken = ""
	chama(t, c)

	if got := valor(s.recebida[0], "token"); got != "token-antigo" {
		t.Fatalf("primeira chamada com %q", got)
	}
	if got := valor(s.recebida[1], "token"); got != "token-novo" {
		t.Fatalf("segunda chamada com %q", got)
	}
}

func TestConexaoOAuth(t *testing.T) {
	c, s := conecta(t)
	c.SetBearer("token-oauth", "empresa-2")

	chama(t, c)

	md := s.recebida[0]
	if valor(md, "authorization") != "Bearer token-oauth" || valor(md, "org") != "empresa-2" || valor(md, "token") != "" {
		t.Fatalf("credencial enviada: %v", md)
	}
}

func TestEnderecoLocalSemTLS(t *testing.T) {
	for endereco, esperado := range map[string]bool{
		"localhost:8080":      true,
		"127.0.0.1:8080":      true,
		"[::1]:8080":          true,
		"app.empresa.com:443": false,
	} {
		if local(endereco) != esperado {
			t.Errorf("local(%q) = %v", endereco, !esperado)
		}
	}
}
