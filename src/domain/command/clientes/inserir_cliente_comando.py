from datetime import datetime
from src.domain.utils.ativo_inativo_enum import Situacao

class InserirClienteComando:
    def __init__(self, id: int, 
                       nome: str, 
                       telefone: str, 
                       data_criacao: datetime, 
                       data_atualizacao: datetime = None, 
                       situacao: Situacao = Situacao.ATIVO):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.data_criacao = data_criacao or datetime.now()
        self.data_atualizacao = data_atualizacao 
        self.situacao = situacao