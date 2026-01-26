'''
Componente reutilizável: Entry com Label
'''
import customtkinter as ctk

class LabeledEntry(ctk.CTkFrame):
    ''' Entry com label integrado '''
    def __init__(self, parent, label_text: str, **configuracoes_adicionais):
        super().__init__(parent, fg_color="transparent") # Inicializa a classe pai com fundo transparente

        # Cria o label
        self.label = ctk.CTkLabel(
            self,
            text=label_text,
            font=("Arial", 12),
            anchor="w"
        )
        self.label.pack(anchor="w", pady=(0, 5))

        self.entry = ctk.CTkEntry(
            self,
            font=("Arial", 12),
            height=35,
            corner_radius=8,
            **configuracoes_adicionais
        )
        self.entry.pack(fill="x")

    def get(self) -> str:
        ''' Retorna o texto do Entry '''
        return self.entry.get()
    
    def set(self, value: str):
        ''' Define o texto do Entry '''
        self.entry.delete(0, 'end')
        self.entry.insert(0, value)

    def clear(self):
        ''' Limpa o texto do Entry '''
        self.entry.delete(0, 'end')