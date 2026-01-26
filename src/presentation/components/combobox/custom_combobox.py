'''
Componente reutilizável: ComboBox Customizado
Este componente define um ComboBox customizado que pode ser reutilizado em diferentes partes da aplicação.
'''

import customtkinter as ctk

class CustomComboBox(ctk.CTkComboBox):
    def __init__(self, container_pai, **configuracoes_adicionais):
        default_style = {
            "width": 150,
            "height": 35,
            "font": ("Arial", 12),
            "corner_radius": 8,
            "dropdown_fg_color": "#2b2b2b",
            "dropdown_text_color": "#FFFFFF",
            "button_hover_color": "#3a3a3a"
        }

        # Atualiza o estilo padrão com quaisquer argumentos fornecidos
        default_style.update(configuracoes_adicionais)
        super().__init__(container_pai, **default_style) # Inicializa a classe pai com o estilo atualizado