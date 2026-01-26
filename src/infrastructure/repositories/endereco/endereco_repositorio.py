from src.infrastructure.database.migrations.sistema_gestao_comercial_bd import SistemaGestaoComercialBD
from src.domain.repositories.enderecos.interface.endereco_repositorio_interface import EnderecoRepositorioInterface
from src.domain.command.enderecos.inserir_endereco_comando import InserirEnderecoComando
from tkinter import messagebox

class EnderecoRepositorio(EnderecoRepositorioInterface):
    def __init__(self):
        self.db = SistemaGestaoComercialBD()

    def cadastrar_endereco(self, comando: InserirEnderecoComando):
        query = '''
                    INSERT INTO endereco (
                        id_cliente, logradouro, numero, complemento, cep, bairro, cidade, estado, data_criacao, situacao
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                '''
        params = (comando.id_cliente, 
                  comando.logradouro, 
                  comando.numero, 
                  comando.complemento, 
                  comando.cep, 
                  comando.bairro, 
                  comando.cidade, 
                  comando.estado,
                  comando.data_criacao.strftime('%Y-%m-%d %H:%M:%S'),
                  comando.situacao.value)
        
        try:
            cursor = self.db.connection.cursor()
            cursor.execute(query, params)
            self.db.connection.commit()
            comando.id = cursor.lastrowid
            messagebox.showinfo("Sucesso", "Endereço cadastrado com sucesso.")

            return comando
        except Exception as ex:
            messagebox.showerror("Erro", f"Erro ao cadastrar endereço: {ex}")
            return None