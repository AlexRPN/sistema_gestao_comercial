from domain.command.enderecos.inserir_endereco_comando import InserirEnderecoComando

class EnderecoMapper:
    @staticmethod
    def mapear_endereco_request_comando(request):
        return InserirEnderecoComando(
            id_cliente=request.id_cliente,
            numero=request.numero,
            logradouro=request.logradouro,
            complemento=request.complemento,
            cep=request.cep,
            bairro=request.bairro,
            cidade=request.cidade,
            estado=request.estado,
            data_criacao=request.data_criacao,
            data_atualizacao=request.data_atualizacao,
            situacao=request.situacao
        )