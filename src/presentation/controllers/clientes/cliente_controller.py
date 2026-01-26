'''
Controller: Cliente
Conecta a view com a camada de aplicação para operações relacionadas a clientes.
'''

from src.application.dtos.clientes.request.cliente_request import ClienteRequest
from src.application.services.clientes.interface.cliente_app_service_interface import ClienteAppServiceInterface


class ClienteController:
    def __init__(self, cliente_app: ClienteAppServiceInterface):
        self.cliente_app = cliente_app

    def cadastrar_cliente(self, request: ClienteRequest):
        return self.cliente_app.cadastrar_cliente(request)