"""Conecta um programa à API gRPC do sistema.

Os clientes de cada serviço ficam nos módulos gerados em linksoft_sdk.pb; este pacote
cuida da conexão, do login e das credenciais que toda chamada leva.
"""

from .client import Client

__all__ = ["Client"]
