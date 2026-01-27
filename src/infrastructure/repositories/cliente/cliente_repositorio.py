from src.infrastructure.database.migrations.sistema_gestao_comercial_bd import SistemaGestaoComercialBD
from src.domain.repositories.clientes.interface.cliente_repositorio_interface import ClienteRepositorioInterface
from src.domain.command.clientes.inserir_cliente_comando import InserirClienteComando
from tkinter import messagebox

class ClienteRepositorio(ClienteRepositorioInterface):
    def __init__(self):
        self.db = SistemaGestaoComercialBD()

    def cadastrar_cliente(self, comando: InserirClienteComando):
        query = ''' INSERT INTO cliente (
                        nome, telefone, email, data_criacao, situacao) 
                    VALUES (?, ?, ?, ?, ?)
                '''
        params = (comando.nome, comando.telefone, comando.email, comando.data_criacao.strftime('%Y-%m-%d %H:%M:%S'), comando.situacao.value)
        
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(query, params)
            self.db.connection.commit()
            comando.id = cursor.lastrowid
            
            return comando
        except Exception as ex:
            messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {ex}")
            return None