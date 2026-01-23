from infrastructure.database.migrations.sistema_gestao_comercial_bd import SistemaGestaoComercialBD
from domain.repositories.enderecos.interface.endereco_repositorio_interface import EnderecoRepositorioInterface
from tkinter import messagebox

class EnderecoRepositorio(EnderecoRepositorioInterface):
    def __init__(self):
        self.db = SistemaGestaoComercialBD()

    def cadastrar_endereco(self, endereco):
        query = ''' INSERT INTO endereco (id_cliente, logradouro, numero, complemento, cep, bairro, cidade, estado) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
        (endereco.cliente.id, endereco.logradouro, endereco.numero, endereco.complemento, endereco.cep, endereco.bairro, endereco.cidade, endereco.estado)

        try:
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            self.db.connection.commit()
            endereco.id = cursor.lastrowid
            messagebox.showinfo("Sucesso", "Endereço cadastrado com sucesso.")

            return endereco
        except Exception as ex:
            messagebox.showerror("Erro", f"Erro ao cadastrar endereço: {ex}")
            return None