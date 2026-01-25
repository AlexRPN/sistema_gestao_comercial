from datetime import datetime
from src.domain.utils.ativo_inativo_enum import Situacao
from src.domain.command.clientes.inserir_cliente_comando import InserirClienteComando

class Cliente:
    def __init__(self, comando: InserirClienteComando):
        self.id = comando.id
        self.nome = comando.nome
        self.telefone = comando.telefone
        self.data_criacao = comando.data_criacao or datetime.now()
        self.data_atualizacao = comando.data_atualizacao 
        self.situacao = comando.situacao
        
    def setSituacao(self, situacao: Situacao):
        if not isinstance(situacao, Situacao):
            raise ValueError("situacao deve ser uma instância de Situacao (enum).")
        self.situacao = situacao

    def setNome(self, nome: str):
        if not nome:
            raise ValueError("Nome não pode ser vazio.")
        self.nome = nome

    def setTelefone(self, telefone: str):
        if not telefone or len(telefone) < 11:
            raise ValueError("Telefone inválido.")
        self.telefone = telefone

    def setDataCriacao(self, data_criacao: datetime):
        self.data_criacao = data_criacao

    def setDataAtualizacao(self, data_atualizacao: datetime):
        self.data_atualizacao = data_atualizacao