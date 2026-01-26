from datetime import datetime
from src.application.dtos.enderecos.request.endereco_request import EnderecoClienteRequest
from src.domain.utils.ativo_inativo_enum import Situacao

class ClienteRequest:
    def __init__(self, nome: str, 
                       telefone: str,
                       email: str,
                       endereco: EnderecoClienteRequest):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco