from domain.services.clientes.interface.cliente_servico_interface import ClienteServicoInterface
from domain.services.enderecos.interface.endereco_servico_interface import EnderecoServicoInterface
from src.application.services.clientes.interface.cliente_app_service_interface import ClienteAppServiceInterface
from src.application.mapper.clientes.cliente_mapper import ClienteMapper
from src.application.mapper.enderecos.endereco_mapper import EnderecoMapper
from tkinter import messagebox

class ClienteAppService(ClienteAppServiceInterface):
    def __init__(self, 
                 cliente_servico: ClienteServicoInterface,
                 endereco_servico: EnderecoServicoInterface):
        self.cliente_servico = cliente_servico
        self.endereco_servico = endereco_servico

    def cadastrar_cliente(self, request):
        try:
            comando = ClienteMapper.mapear_cliente_request_comando(request)
            cliente = self.cliente_servico.cadastrar_cliente(comando)
            if cliente is not None:
                endereco_comando = EnderecoMapper.mapear_endereco_request_comando(request.endereco)
                endereco_comando.id_cliente = cliente.id
                self.endereco_servico.cadastrar_endereco(endereco_comando)

            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

        except Exception as ex:
            messagebox.showerror("Erro", f"Falha ao cadastrar cliente: {str(ex)}")
