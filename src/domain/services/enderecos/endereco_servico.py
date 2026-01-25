from domain.command.enderecos.inserir_endereco_comando import InserirEnderecoComando
from domain.repositories.enderecos.interface.endereco_repositorio_interface import EnderecoRepositorioInterface
from domain.services.enderecos.interface.endereco_servico_interface import EnderecoServicoInterface
from tkinter import messagebox

class EnderecoServico(EnderecoServicoInterface):
    def __init__(self, endereco_repositorio: EnderecoRepositorioInterface):
        self.endereco_repositorio = endereco_repositorio

    def cadastrar_endereco(self, comando: InserirEnderecoComando):
        if comando.id_cliente is None:
            return messagebox.showerror("Erro", "O ID do cliente é obrigatório para cadastrar um endereço.")

        return self.endereco_repositorio.cadastrar_endereco(comando)