import customtkinter as ctk


class MainView(ctk.CTk):
    """Janela principal do Sistema Escolar."""

    def __init__(self):
        super().__init__()
        self.title("Sistema Escolar — Turma 2º B")
        self.geometry("1000x650")
        self.minsize(800, 500)
