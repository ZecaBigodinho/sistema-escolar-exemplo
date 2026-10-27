import customtkinter as ctk


class MainView(ctk.CTk):
    """Janela principal do Sistema Escolar."""

    def __init__(self):
        super().__init__()
        self.title("Sistema Escolar")
        self.geometry("900x600")
