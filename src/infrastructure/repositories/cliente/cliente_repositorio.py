from infrastructure.database.migrations.sistema_gestao_comercial_bd import SistemaGestaoComercialBD
from domain.repositories.clientes.interface.cliente_repositorio_interface import ClienteRepositorioInterface
from src.domain.command.clientes.inserir_cliente_comando import InserirClienteComando
from tkinter import messagebox

class ClienteRepositorio(ClienteRepositorioInterface):
    def __init__(self):
        self.db = SistemaGestaoComercialBD()

    def cadastrar_cliente(self, comando: InserirClienteComando):
        query = ''' INSERT INTO cliente (
                        nome, telefone) 
                    VALUES (?, ?)
                ''', (comando.nome, 
                      comando.telefone)
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            self.db.connection.commit()
            comando.id = cursor.lastrowid
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso.")

            return comando
        except Exception as ex:
            messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {ex}")
            return None