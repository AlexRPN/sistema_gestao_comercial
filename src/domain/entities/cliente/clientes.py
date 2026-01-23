from datetime import datetime
from src.domain.utils.ativo_inativo_enum import Situacao

class Cliente:
    def __init__(self, id: int, 
                       nome: str, 
                       telefone: str, 
                       data_criacao: datetime, 
                       data_atualizacao: datetime, 
                       situacao: Situacao = Situacao.ATIVO):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.data_criacao = data_criacao or datetime.now()
        self.data_atualizacao = data_atualizacao 
        self.situacao = situacao
        
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

    def setSituacao(self, situacao: bool):
        self.situacao = situacao

        