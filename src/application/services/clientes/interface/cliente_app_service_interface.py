from src.application.dtos.clientes.request.cliente_request import ClienteRequest
from abc import ABC, abstractmethod

class ClienteAppServiceInterface(ABC):
    @abstractmethod
    def cadastrar_cliente(self, request: ClienteRequest):
        pass