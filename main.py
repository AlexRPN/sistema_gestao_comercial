"""
Ponto de entrada da aplicação.
Aqui fazemos a injeção de dependências e iniciamos a interface gráfica.
"""
import customtkinter as ctk

from src.presentation.views.clientes.tela_cadastro_cliente import TelaCadastroCliente
from src.presentation.controllers.clientes.cliente_controller import ClienteController
from src.application.services.clientes.cliente_app_service import ClienteAppService
from src.infrastructure.repositories.cliente.cliente_repositorio import ClienteRepositorio
from src.domain.repositories.clientes.interface.cliente_repositorio_interface import ClienteRepositorioInterface
from src.domain.repositories.enderecos.interface.endereco_repositorio_interface import EnderecoRepositorioInterface
from src.infrastructure.repositories.endereco.endereco_repositorio import EnderecoRepositorio
from src.domain.services.clientes.interface.cliente_servico_interface import ClienteServicoInterface
from src.domain.services.clientes.cliente_servico import ClienteServico
from src.domain.services.enderecos.interface.endereco_servico_interface import EnderecoServicoInterface
from src.domain.services.enderecos.endereco_servico import EnderecoServico
from src.application.services.clientes.interface.cliente_app_service_interface import ClienteAppServiceInterface


# Configur aparência do CustomTkinter
ctk.set_appearance_mode("System")  # Modos: "System" (padrão), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (padrão), "dark-blue", "green"

class App:
    def __init__(self):
        # Cria a janela principal
        self.root = ctk.CTk()
        self.root.title("Sistema de Gestão Comercial")
        self.root.geometry("900x650")

        # Injeção de dependências (DI)
        self._configurar_dependencias()

        # Criar interface principal
        self._criar_interface_principal()

    def _configurar_dependencias(self):
        """
        Configura as dependências da aplicação usando interfaces.
        Inicializa repositórios, serviços de domínio, serviços de aplicação e controladores.
        """

        # Inicializa os repositórios (implementações concretas tipadas pelas interfaces)
        cliente_repository: ClienteRepositorioInterface = ClienteRepositorio()
        endereco_repository: EnderecoRepositorioInterface = EnderecoRepositorio()

        # Inicializa os serviços de domínio com os repositórios
        cliente_servico: ClienteServicoInterface = ClienteServico(cliente_repository)
        endereco_servico: EnderecoServicoInterface = EnderecoServico(endereco_repository)

        # Inicializa o serviço de aplicação com os serviços de domínio
        cliente_app_service: ClienteAppServiceInterface = ClienteAppService(cliente_servico, endereco_servico)

        # Inicializa o controlador com o serviço de aplicação
        self.cliente_controller = ClienteController(cliente_app_service)

    def _criar_interface_principal(self):
        """ Cria a interface principal com abas para diferentes funcionalidades. """
        # Título
        titulo = ctk.CTkLabel(
            self.root,
            text="Sistema de Gestão Comercial",
            font=('Arial', 26, 'bold')
        )
        titulo.pack(pady=20)

        # Tabview para navegação entre telas
        tabview = ctk.CTkTabview(self.root)
        tabview.pack(expand=True, fill="both", padx=20, pady=10)

        # Aba de Cadastro de Clientes
        tab_cadastro_clientes = tabview.add("Cadastro de Clientes")
        self.tela_cadastro = TelaCadastroCliente(
            tab_cadastro_clientes,
            self.cliente_controller
        )
        self.tela_cadastro.pack(expand=True, fill="both")

        # Aba de Listagem de Clientes
        # tab_listagem_clientes = tabview.add("Clientes Cadastrados")
        # self.tela_listagem = TelaListagemClientes(
        #     tab_listagem_clientes,
        #     self.cliente_controller
        # )
        # self.tela_listagem.pack(expand=True, fill="both")

    def run(self):
        """ Inicia o loop principal da aplicação. """
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()