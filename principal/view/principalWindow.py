from tkinter import ttk,Tk
from tkinter import filedialog
from tkinter import *




class Principal:
    
    def __init__(self,window) :
        #Aqui damos parametros graficos a nuestra ventana principal(tamaño, titulo, etc)
        self.principal = window
        self.principal.title("PRINCIPAL WINDOW APP")
        self.principal.geometry("800x500")
        self.principal.configure(background="#C84D32",pady="4px",padx="4px")
        self.prueba= 2 + 2
        print(self.prueba)

        #Boton para cargar archivos
        self.loadButton= Button(self.principal,text="Open File",
            command=self.loadFiles,
            width=22,
            height=3)
        self.loadButton.grid(row= 2,column = 2)
        self.loadButton.pack()
        
        #Boton para gestionar cursos
        self.management=Button(self.principal,text="Gestionar Cursos",
        command=lambda:print("hola mundo"),
        width=22,
        height=3)
        
        self.management.pack()
    
    def loadFiles(self):
        self.archivo = filedialog.askopenfilename(
        title="Abrir", initialdir="C:/")
        print(self.archivo)
        return self.archivo
        
    
        




