from datetime import datetime

from src.domain.utils.ativo_inativo_enum import Situacao


class EnderecoClienteRequest:
    def __init__(self, numero: int,
                       logradouro: str,
                       complemento: str,
                       cep: str,
                       bairro: str,
                       cidade: str,
                       estado: str):
        self.numero = numero
        self.logradouro = logradouro
        self.complemento = complemento
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado