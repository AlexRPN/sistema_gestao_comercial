from datetime import datetime
from application.dtos.enderecos.request.endereco_request import EnderecoClienteRequest
from src.domain.utils.ativo_inativo_enum import Situacao

class ClienteRequest:
    def __init__(self, id: int, 
                       nome: str, 
                       telefone: str, 
                       data_criacao: datetime, 
                       data_atualizacao: datetime, 
                       situacao: Situacao,
                       endereco: EnderecoClienteRequest):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.data_criacao = data_criacao
        self.data_atualizacao = data_atualizacao 
        self.situacao = situacao
        self.endereco = endereco