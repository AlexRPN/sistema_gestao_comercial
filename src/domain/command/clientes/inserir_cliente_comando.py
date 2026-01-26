from datetime import datetime
from src.domain.utils.ativo_inativo_enum import Situacao

class InserirClienteComando:
    def __init__(self, nome: str, 
                       telefone: str,
                       email: str, 
                       data_criacao: datetime, 
                       data_atualizacao: datetime = None, 
                       situacao: Situacao = Situacao.ATIVO):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.data_criacao = data_criacao or datetime.now()
        self.data_atualizacao = data_atualizacao 
        self.situacao = situacao