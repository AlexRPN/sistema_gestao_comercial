from abc import ABC, abstractmethod

class ClienteRepositorioInterface(ABC):
    @abstractmethod
    def cadastrar_cliente(self, cliente):
        pass