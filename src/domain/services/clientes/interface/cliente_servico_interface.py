from src.domain.command.clientes.inserir_cliente_comando import InserirClienteComando
from abc import ABC, abstractmethod

class ClienteServicoInterface(ABC):
    @abstractmethod
    def cadastrar_cliente(self, comando: InserirClienteComando):
        pass