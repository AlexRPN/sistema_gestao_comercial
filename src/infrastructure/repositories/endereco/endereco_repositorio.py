from infrastructure.database.migrations.sistema_gestao_comercial_bd import SistemaGestaoComercialBD
from domain.repositories.enderecos.interface.endereco_repositorio_interface import EnderecoRepositorioInterface
from src.domain.command.enderecos.inserir_endereco_comando import InserirEnderecoComando
from tkinter import messagebox

class EnderecoRepositorio(EnderecoRepositorioInterface):
    def __init__(self):
        self.db = SistemaGestaoComercialBD()

    def cadastrar_endereco(self, comando: InserirEnderecoComando):
        query = '''
                    INSERT INTO endereco (
                        id_cliente, logradouro, numero, complemento, cep, bairro, cidade, estado
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (comando.id_cliente, 
                      comando.logradouro, 
                      comando.numero, 
                      comando.complemento, 
                      comando.cep, 
                      comando.bairro, 
                      comando.cidade, 
                      comando.estado)
        
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(query)
            self.db.connection.commit()
            comando.id = cursor.lastrowid
            messagebox.showinfo("Sucesso", "Endereço cadastrado com sucesso.")

            return comando
        except Exception as ex:
            messagebox.showerror("Erro", f"Erro ao cadastrar endereço: {ex}")
            return None