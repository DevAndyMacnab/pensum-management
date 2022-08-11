from tkinter import ttk,Tk
from tkinter import *

class CreditsWindow:
    def __init__(self,window) -> None:
        self.principal= window
        self.newWindow= Toplevel()
        self.newWindow.title("Conteo de Créditos")
        self.newWindow.geometry("600x850")
        self.newWindow.resizable(False,False)

        Label(text="")


