from domain.entities.cliente.clientes import Cliente
from datetime import datetime
from src.domain.utils.ativo_inativo_enum import Situacao

class Enderecos:
    def __init__(self, id: int,
                       cliente: Cliente,
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
        self.id = id
        self.cliente = cliente
        self.numero = numero
        self.logradouro = logradouro
        self.complemento = complemento
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao or datetime.now()
        self.situacao = situacao

    def setSituacao(self, situacao: Situacao):
        self.situacao = situacao

    def setCliente(self, cliente: Cliente):
        self.cliente = cliente

    def setNumero(self, numero: int):
        self.numero = numero

    def setLogradouro(self, logradouro: str):
        self.logradouro = logradouro

    def setComplemento(self, complemento: str):
        self.complemento = complemento

    def setCep(self, cep: str):
        if not cep or len(cep) != 8:
            raise ValueError("CEP inválido.")
        self.cep = cep

    def setBairro(self, bairro: str):
        self.bairro = bairro

    def setCidade(self, cidade: str):
        self.cidade = cidade

    def setEstado(self, estado: str):
        self.estado = estado

    def setDataCriacao(self, data_criacao: datetime):
        self.data_criacao = data_criacao

    def setDataAtualizacao(self, data_atualizacao: datetime):
        self.data_atualizacao = data_atualizacao