from tkinter import ttk,Tk
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox as MessageBox

class ExitProgram:
    def __init__(self,window) :
        self.principal=window
        
    def closeProgram(self):
        self.comprobante=MessageBox.askquestion("Saliendo","¿Estás seguro que deseas salir del programa?")
        if self.comprobante=='yes':
            self.principal.destroy()