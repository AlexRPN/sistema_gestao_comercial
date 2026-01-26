import sqlite3
from tkinter import messagebox

class SistemaGestaoComercialBD:
    def __init__(self):
        self.connection = sqlite3.connect('data/gestao_comercial.db')
        self.cursor = self.connection.cursor()
        # create_tables() deve ser chamado manualmente quando necessário

    def create_tables(self):
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS cliente (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            telefone TEXT NOT NULL,
                            email TEXT NOT NULL,
                            data_criacao TEXT NOT NULL,
                            data_atualizacao TEXT,
                            situacao boolean NOT NULL DEFAULT 1) ''')
        
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS endereco (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id_cliente INTEGER NOT NULL,
                            logradouro TEXT NOT NULL,
                            numero TEXT NOT NULL,
                            complemento TEXT,
                            bairro TEXT NOT NULL,
                            cidade TEXT NOT NULL,
                            estado TEXT NOT NULL,
                            cep TEXT NOT NULL,
                            data_criacao TEXT NOT NULL,
                            data_atualizacao TEXT,
                            situacao boolean NOT NULL DEFAULT 1,
                            FOREIGN KEY (id_cliente) REFERENCES cliente(id)) ''')
        
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS categoria (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            descricao TEXT NOT NULL)''')
        
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS produto (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id_categoria INTEGER NOT NULL,
                            descricao TEXT NOT NULL,
                            preco REAL NOT NULL,
                            quantidade INTEGER NOT NULL,
                            tamanho TEXT,
                            imagem TEXT,
                            data_criacao TEXT NOT NULL,
                            data_atualizacao TEXT,
                            situacao boolean NOT NULL DEFAULT 1,
                            FOREIGN KEY (id_categoria) REFERENCES categoria(id))''')
        
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS pedido (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id_cliente INTEGER NOT NULL,
                            valor_total REAL NOT NULL,
                            tipo_pagamento TEXT NOT NULL,
                            data_pedido TEXT NOT NULL,
                            status_pedido TEXT NOT NULL,
                            data_atualizacao TEXT,
                            motivo_cancelamento TEXT,
                            FOREIGN KEY (id_cliente) REFERENCES cliente(id))''')
        
        self.cursor.execute(''' CREATE TABLE IF NOT EXISTS pedido_produto (
                            id_pedido INTEGER NOT NULL,
                            id_produto INTEGER NOT NULL,
                            quantidade INTEGER NOT NULL,
                            preco_unitario REAL NOT NULL,
                            FOREIGN KEY (id_pedido) REFERENCES pedido(id),
                            FOREIGN KEY (id_produto) REFERENCES produto(id))''')
        
        self.connection.commit()
        messagebox.showinfo("Sucesso", "Banco de dados e tabelas criados com sucesso!")
