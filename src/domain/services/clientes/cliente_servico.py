from src.domain.repositories.clientes.interface.cliente_repositorio_interface import ClienteRepositorioInterface
from src.domain.services.clientes.interface.cliente_servico_interface import ClienteServicoInterface
from src.domain.command.clientes.inserir_cliente_comando import InserirClienteComando
from tkinter import messagebox

class ClienteServico(ClienteServicoInterface):
    CAMPOS_OBRIGATORIOS = "Existem campos obrigatórios não preenchidos. Verifique os dados e tente novamente."
    # Injeção de dependência do repositório de clientes
    def __init__(self, cliente_repositorio: ClienteRepositorioInterface):
        self.cliente_repositorio = cliente_repositorio

    def cadastrar_cliente(self, comando: InserirClienteComando):
        # Validação se o cliente já existe no sistema
                
        return self.cliente_repositorio.cadastrar_cliente(comando)
        