from datetime import datetime
from src.domain.utils.ativo_inativo_enum import Situacao

class InserirEnderecoComando:
    def __init__(self, id_cliente: int,
                       numero: int,
                       logradouro: str,
                       complemento: str,
                       cep: str,
                       bairro: str,
                       cidade: str,
                       estado: str,
                       data_criacao: datetime,
                       data_atualizacao: datetime = None,
                       situacao: Situacao = Situacao.ATIVO):
        self.id_cliente = id_cliente
        self.numero = numero
        self.logradouro = logradouro
        self.complemento = complemento
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao
        self.situacao = situacao