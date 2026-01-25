from src.domain.command.clientes.inserir_cliente_comando import InserirClienteComando

class ClienteMapper:
    @staticmethod
    def mapear_cliente_request_comando(request):
        return InserirClienteComando(
            nome=request.nome,
            telefone=request.telefone,
            data_criacao=request.data_criacao,
            data_atualizacao=request.data_atualizacao,
            situacao=request.situacao
        )