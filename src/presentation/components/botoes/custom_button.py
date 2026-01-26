'''
Componente reutilizável: Botão Customizado
Este componente define um botão customizado que pode ser reutilizado em diferentes partes da aplicação.
'''
import customtkinter as ctk

class CustomButton(ctk.CTkButton):
    def __init__(self, container_pai, **configuracoes_adicionais):
        default_style = {
            "fg_color": "#007BFF",
            "hover_color": "#0056b3",
            "text_color": "#FFFFFF",
            "font": ("Arial", 12, "bold"),
            "corner_radius": 8,
            "height": 40
        }

        # Atualiza o estilo padrão com quaisquer argumentos fornecidos
        default_style.update(configuracoes_adicionais)
        super().__init__(container_pai, **default_style)