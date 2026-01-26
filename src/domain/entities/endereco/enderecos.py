from src.domain.entities.cliente.clientes import Cliente
from src.domain.command.enderecos.inserir_endereco_comando import InserirEnderecoComando
from datetime import datetime
from src.domain.utils.ativo_inativo_enum import Situacao

class Enderecos:
    def __init__(self, InserirEnderecoComando: InserirEnderecoComando):
        self.id = InserirEnderecoComando.id
        self.id_cliente = InserirEnderecoComando.id_cliente
        self.numero = InserirEnderecoComando.numero
        self.logradouro = InserirEnderecoComando.logradouro
        self.complemento = InserirEnderecoComando.complemento
        self.cep = InserirEnderecoComando.cep
        self.bairro = InserirEnderecoComando.bairro
        self.cidade = InserirEnderecoComando.cidade
        self.estado = InserirEnderecoComando.estado
        self.data_criacao = InserirEnderecoComando.data_criacao or datetime.now()
        self.data_atualizacao = InserirEnderecoComando.data_atualizacao 
        self.situacao = InserirEnderecoComando.situacao

    def setSituacao(self, situacao: Situacao):
        self.situacao = situacao

    def setIdCliente(self, id_cliente: int):
        self.id_cliente = id_cliente

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