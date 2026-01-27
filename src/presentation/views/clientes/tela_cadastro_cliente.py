"""
View: Tela de Cadastro de Cliente
Interface gráfica para o cadastro de novos clientes no sistema.
"""

import customtkinter as ctk
from tkinter import messagebox
from src.application.dtos.clientes.request.cliente_request import ClienteRequest
from src.application.dtos.enderecos.request.endereco_request import EnderecoClienteRequest
from src.presentation.controllers.clientes.cliente_controller import ClienteController
from src.presentation.components.botoes.custom_button import CustomButton
from src.presentation.components.campo_entrada.custom_entry import LabeledEntry

class TelaCadastroCliente(ctk.CTkFrame):
    def __init__(self, parent, cliente_controller: ClienteController):
        super().__init__(parent, fg_color="transparent")
        self.cliente_controller = cliente_controller
        self.criar_interface()

    def criar_interface(self):
        """ Cria todos os widgets da tela de cadastro de cliente. """
        # Título fixo
        titulo = ctk.CTkLabel(
            self, 
            text="Cadastro de Cliente", 
            font=('Arial', 24, 'bold')
        )
        titulo.pack(pady=20)

        # Frame com barra de rolagem
        frame_scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        frame_scroll.pack(expand=True, fill="both", padx=40, pady=(0, 20))

        # Configurar grid para 2 colunas
        frame_scroll.grid_columnconfigure(0, weight=1)
        frame_scroll.grid_columnconfigure(1, weight=1)

        # Seção: Dados do Cliente
        label_secao_cliente = ctk.CTkLabel(
            frame_scroll,
            text="Dados do Cliente",
            font=('Arial', 18, 'bold')
        )
        label_secao_cliente.grid(row=0, column=0, columnspan=2, pady=(10, 15), sticky="w")

        # Campo Nome (ocupa 2 colunas)
        self.entrada_nome = LabeledEntry(frame_scroll, "Nome:")
        self.entrada_nome.grid(row=1, column=0, columnspan=2, padx=5, pady=8, sticky="ew")

        # Campo Telefone
        self.entrada_telefone = LabeledEntry(frame_scroll, "Telefone:")
        self.entrada_telefone.grid(row=2, column=0, padx=5, pady=8, sticky="ew")

        # Campo Email
        self.entrada_email = LabeledEntry(frame_scroll, "Email:")
        self.entrada_email.grid(row=2, column=1, padx=5, pady=8, sticky="ew")

        # Espaço vazio para layout
        ctk.CTkLabel(frame_scroll, text="").grid(row=2, column=1)

        # Seção: Endereço
        label_secao_endereco = ctk.CTkLabel(
            frame_scroll,
            text="Endereço",
            font=('Arial', 18, 'bold')
        )
        label_secao_endereco.grid(row=3, column=0, columnspan=2, pady=(20, 15), sticky="w")

        # Campo Logradouro (ocupa 2 colunas)
        self.entrada_logradouro = LabeledEntry(frame_scroll, "Logradouro:")
        self.entrada_logradouro.grid(row=4, column=0, columnspan=2, padx=5, pady=8, sticky="ew")

        # Campo Número e Complemento
        self.entrada_numero = LabeledEntry(frame_scroll, "Número:")
        self.entrada_numero.grid(row=5, column=0, padx=5, pady=8, sticky="ew")

        self.entrada_complemento = LabeledEntry(frame_scroll, "Complemento:")
        self.entrada_complemento.grid(row=5, column=1, padx=5, pady=8, sticky="ew")

        # Campo CEP e Bairro
        self.entrada_cep = LabeledEntry(frame_scroll, "CEP:")
        self.entrada_cep.grid(row=6, column=0, padx=5, pady=8, sticky="ew")

        self.entrada_bairro = LabeledEntry(frame_scroll, "Bairro:")
        self.entrada_bairro.grid(row=6, column=1, padx=5, pady=8, sticky="ew")

        # Campo Cidade e Estado
        self.entrada_cidade = LabeledEntry(frame_scroll, "Cidade:")
        self.entrada_cidade.grid(row=7, column=0, padx=5, pady=8, sticky="ew")

        self.entrada_estado = LabeledEntry(frame_scroll, "Estado:")
        self.entrada_estado.grid(row=7, column=1, padx=5, pady=8, sticky="ew")

        # Frame dos botões (fora do scroll)
        frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        frame_botoes.pack(pady=20)

        # Botão Cadastrar
        botao_cadastrar = CustomButton(
            frame_botoes, 
            text="Cadastrar", 
            command=self._cadastrar_cliente,
            width=150
        )
        botao_cadastrar.pack(side="left", padx=10)

        # Botão Limpar
        botao_limpar = CustomButton(
            frame_botoes, 
            text="Limpar", 
            fg_color="#6c757d",
            hover_color="#5a6268",
            command=self.limpar_campos,
            width=150
        )
        botao_limpar.pack(side="left", padx=10)

        # Define o foco inicial para o campo Nome
        self.entrada_nome.entry.focus()

    def _cadastrar_cliente(self):
        """ Coleta os dados dos campos e chama o controller para cadastrar o cliente. """
        nome = self.entrada_nome.get()
        telefone = self.entrada_telefone.get()
        email = self.entrada_email.get()
        numero = self.entrada_numero.get()
        logradouro = self.entrada_logradouro.get()
        complemento = self.entrada_complemento.get()
        cep = self.entrada_cep.get()
        bairro = self.entrada_bairro.get()
        cidade = self.entrada_cidade.get()
        estado = self.entrada_estado.get()

        cliente_request: ClienteRequest = ClienteRequest(
            nome=nome,
            telefone=telefone,
            email=email,
            endereco=EnderecoClienteRequest(
                numero=numero,
                logradouro=logradouro,
                complemento=complemento,
                cep=cep,
                bairro=bairro,
                cidade=cidade,
                estado=estado
            )
        )
        resultado = self.cliente_controller.cadastrar_cliente(cliente_request)

        if resultado['sucesso']:
            messagebox.showinfo("Sucesso", resultado['mensagem'])
            self.limpar_campos()
        else:
            messagebox.showerror("Erro", resultado['mensagem_erro'])

    def limpar_campos(self):
        """ Limpa todos os campos de entrada da tela. """
        self.entrada_nome.clear()
        self.entrada_telefone.clear()
        self.entrada_email.clear()
        self.entrada_numero.clear()
        self.entrada_logradouro.clear()
        self.entrada_complemento.clear()
        self.entrada_cep.clear()
        self.entrada_bairro.clear()
        self.entrada_cidade.clear()
        self.entrada_estado.clear()
        self.entrada_nome.focus() # Define o foco inicial para o campo Nome