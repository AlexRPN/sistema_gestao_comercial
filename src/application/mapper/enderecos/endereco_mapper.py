from src.domain.command.enderecos.inserir_endereco_comando import InserirEnderecoComando
from datetime import datetime
from src.domain.utils.ativo_inativo_enum import Situacao

class EnderecoMapper:
    @staticmethod
    def mapear_endereco_request_comando(request):
        return InserirEnderecoComando(
            id_cliente=None,  # Será definido após cadastrar o cliente
            numero=request.numero,
            logradouro=request.logradouro,
            complemento=request.complemento,
            cep=request.cep,
            bairro=request.bairro,
            cidade=request.cidade,
            estado=request.estado,
            data_criacao=datetime.now(),
            data_atualizacao=None,
            situacao=Situacao.ATIVO
        )