# Linksoft SDKs

SDKs oficiais da Linksoft para múltiplas linguagens de programação.

[![Release](https://img.shields.io/github/v/release/linksoft-dev/sdks)](https://github.com/linksoft-dev/sdks/releases)
[![License](https://img.shields.io/github/license/linksoft-dev/sdks)](LICENSE)

## 📦 SDKs Disponíveis

| Linguagem | Pacote | Instalação | Documentação |
|-----------|--------|------------|--------------|
| 🐍 **Python** | [`linksoft-sdk`](https://pypi.org/project/linksoft-sdk/) | `pip install linksoft-sdk` | [README](python/README.md) |
| 🔷 **C#** | [`Linksoft.Sdk`](https://www.nuget.org/packages/Linksoft.Sdk/) | `dotnet add package Linksoft.Sdk` | [README](csharp/README.md) |
| 🎯 **Dart** | [`linksoft_sdk`](https://pub.dev/packages/linksoft_sdk) | `dart pub add linksoft_sdk` | [README](dart/README.md) |
| ☕ **Java** | [`linksoft-sdk`](https://central.sonatype.com/artifact/dev.linksoft/linksoft-sdk) | Maven/Gradle | [README](java/README.md) |
| 🏗️ **Kotlin** | [`linksoft-kotlin-sdk`](https://central.sonatype.com/artifact/dev.linksoft/linksoft-kotlin-sdk) | Maven/Gradle | [README](kotlin/README.md) |
| 🐹 **Go** | `github.com/linksoft-dev/sdks/go` | `go get github.com/linksoft-dev/sdks/go` | [README](go/README.md) |

## 🚀 Início Rápido

### Python
```bash
pip install linksoft-sdk
```

```python
from linksoft_sdk import LinksoftClient

client = LinksoftClient.with_defaults("sua-api-key")
```

### C#
```bash
dotnet add package Linksoft.Sdk
```

```csharp
using Linksoft.Sdk;

var client = new LinksoftClient("sua-api-key");
```

### Dart/Flutter
```bash
dart pub add linksoft_sdk
```

```dart
import 'package:linksoft_sdk/linksoft_sdk.dart';

final client = LinksoftClient.withDefaults("sua-api-key");
```

### Java
```xml
<dependency>
    <groupId>dev.linksoft</groupId>
    <artifactId>linksoft-sdk</artifactId>
    <version>LATEST</version>
</dependency>
```

```java
import dev.linksoft.sdk.LinksoftClient;

LinksoftClient client = LinksoftClient.withDefaults("sua-api-key");
```

### Kotlin
```kotlin
implementation("dev.linksoft:linksoft-kotlin-sdk:LATEST")
```

```kotlin
import dev.linksoft.sdk.LinksoftClient

val client = LinksoftClient.withDefaults("sua-api-key")
```

### Go
```bash
go get github.com/linksoft-dev/sdks/go
```

```go
import "github.com/linksoft-dev/sdks/go"

client := linksoft.NewClient("sua-api-key")
```

## 📚 Documentação

Cada SDK possui sua própria documentação detalhada:

- **[Python SDK](python/README.md)** - Suporte async/await, FastAPI, Django
- **[C# SDK](csharp/README.md)** - .NET 6+, ASP.NET Core, Dependency Injection
- **[Dart SDK](dart/README.md)** - Flutter, Dart puro, async/sync
- **[Java SDK](java/README.md)** - Java 17+, Spring Boot, Maven/Gradle
- **[Kotlin SDK](kotlin/README.md)** - Coroutines, interoperabilidade Java
- **[Go SDK](go/README.md)** - Context, channels, concorrência

## 🔧 Configuração

Todos os SDKs suportam configuração similar:

```bash
# Variáveis de ambiente
export LINKSOFT_API_KEY="sua-api-key"
export LINKSOFT_HOST="api.linksoft.com.br"
export LINKSOFT_PORT="443"
export LINKSOFT_USE_TLS="true"
```

## 🏗️ Arquitetura

Os SDKs são gerados automaticamente a partir dos arquivos Protocol Buffers (protobuf) da Linksoft, garantindo:

- **Consistência** entre todas as linguagens
- **Type Safety** com tipos fortemente tipados
- **Atualizações automáticas** quando novos serviços são adicionados
- **Compatibilidade** com gRPC e HTTP/REST

## 🔄 Atualizações

Os SDKs são atualizados automaticamente quando:

1. Novos serviços são adicionados aos protobuf
2. Uma nova versão é lançada
3. Correções de bugs são aplicadas

As atualizações são publicadas simultaneamente em todos os repositórios centrais.

## 🛠️ Desenvolvimento

### Estrutura do Projeto

```
sdks/
├── go/           # Go SDK
├── csharp/       # C# SDK  
├── dart/         # Dart SDK
├── java/         # Java SDK
├── kotlin/       # Kotlin SDK
├── python/       # Python SDK
├── buf.gen.yaml  # Configuração Buf
└── Makefile      # Comandos de build
```

### Comandos de Build

```bash
# Gerar todos os SDKs
make generate-all

# Gerar SDK específico
make generate-go
make generate-python
make generate-csharp
# etc...

# Testar todos os SDKs
make test-all

# Limpar arquivos gerados
make clean-all
```

## 📋 Requisitos

- **Buf CLI** para geração de protobuf
- **Go 1.21+** para SDK Go
- **Python 3.8+** para SDK Python
- **.NET 6+** para SDK C#
- **Dart 3.0+** para SDK Dart
- **Java 17+** para SDK Java
- **Kotlin 1.8+** para SDK Kotlin

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🆘 Suporte

- **Documentação**: https://docs.linksoft.com.br
- **Issues**: https://github.com/linksoft-dev/sdks/issues
- **Email**: suporte@linksoft.com.br
- **Website**: https://linksoft.com.br

## 🏷️ Versões

| Versão | Data | Mudanças |
|--------|------|----------|
| 1.0.0 | 2025-01-XX | Lançamento inicial |

---

**Linksoft** - Construindo software de qualidade desde 2020. 