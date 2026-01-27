from src.domain.services.clientes.interface.cliente_servico_interface import ClienteServicoInterface
from src.domain.services.enderecos.interface.endereco_servico_interface import EnderecoServicoInterface
from src.application.services.clientes.interface.cliente_app_service_interface import ClienteAppServiceInterface
from src.application.mapper.clientes.cliente_mapper import ClienteMapper
from src.application.mapper.enderecos.endereco_mapper import EnderecoMapper
from tkinter import messagebox

class ClienteAppService(ClienteAppServiceInterface):
    DADOS_CLIENTE_OBRIGATORIOS = "Dados do cliente são obrigatórios."
    DADOS_ENDERECO_OBRIGATORIOS = "Dados do endereço são obrigatórios."

    def __init__(self, 
                 cliente_servico: ClienteServicoInterface,
                 endereco_servico: EnderecoServicoInterface):
        self.cliente_servico = cliente_servico
        self.endereco_servico = endereco_servico

    def cadastrar_cliente(self, request):
        try:
            # Valida dados do cliente (excluindo o objeto endereco)
            if not any([request.nome, request.telefone, request.email]):
                return messagebox.showerror("Erro", self.DADOS_CLIENTE_OBRIGATORIOS)
            
            # Valida dados do endereço
            if not request.endereco or not any(vars(request.endereco).values()):
                return messagebox.showerror("Erro", self.DADOS_ENDERECO_OBRIGATORIOS)
            
            comando = ClienteMapper.mapear_cliente_request_comando(request)
            self.cliente_servico.cadastrar_cliente(comando)

            endereco_comando = EnderecoMapper.mapear_endereco_request_comando(request.endereco)
            endereco_comando.id_cliente = comando.id
            self.endereco_servico.cadastrar_endereco(endereco_comando)

            return {
                'sucesso': True,
                'mensagem': f'Cliente {comando.nome} cadastrado(a) com sucesso!',
            }

        except Exception as ex:
            messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {str(ex)}")
