from infrastructure.database.migrations.sistema_gestao_comercial_bd import SistemaGestaoComercialBD
from domain.repositories.clientes.interface.cliente_repositorio_interface import ClienteRepositorioInterface
from tkinter import messagebox

class ClienteRepositorio(ClienteRepositorioInterface):
    def __init__(self):
        self.db = SistemaGestaoComercialBD()

    def cadastrar_cliente(self, cliente):
        query = ''' INSERT INTO cliente (nome, telefone) 
                VALUES (?, ?)''', (cliente.nome, cliente.telefone)
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            self.db.connection.commit()
            cliente.id = cursor.lastrowid
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso.")

            return cliente
        except Exception as ex:
            messagebox.showerror("Erro", f"Erro ao cadastrar cliente: {ex}")
            return None