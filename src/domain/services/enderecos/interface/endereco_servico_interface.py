from abc import ABC, abstractmethod
from src.domain.command.enderecos.inserir_endereco_comando import InserirEnderecoComando

class EnderecoServicoInterface(ABC):
    @abstractmethod
    def cadastrar_endereco(self, comando: InserirEnderecoComando):
        pass
