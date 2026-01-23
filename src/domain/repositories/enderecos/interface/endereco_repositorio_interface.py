from abc import ABC, abstractmethod

class EnderecoRepositorioInterface(ABC):
    @abstractmethod
    def cadastrar_endereco(self, endereco):
        pass