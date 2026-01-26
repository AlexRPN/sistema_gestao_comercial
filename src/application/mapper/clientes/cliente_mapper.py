from src.domain.command.clientes.inserir_cliente_comando import InserirClienteComando
from datetime import datetime
from src.domain.utils.ativo_inativo_enum import Situacao

class ClienteMapper:
    @staticmethod
    def mapear_cliente_request_comando(request):
        return InserirClienteComando(
            nome=request.nome,
            telefone=request.telefone,
            email=request.email,
            data_criacao=datetime.now(),
            data_atualizacao=None,
            situacao=Situacao.ATIVO
        )