from tkinter import ttk,Tk
from tkinter import *
from tkinter import messagebox as MessageBox
#Importando los modulos del proyecto ubicados en otros archivos

from management.view.managementWindow import ManagementCourses
from creditsCount.view.creditsCountsWindow import CreditsWindow
from principal.controller.loadFile import Loadfile
from principal.controller.exit import ExitProgram


class Principal:
    
    def __init__(self,window) :
        self.closeFunction=ExitProgram(window)
        #Aqui damos parametros graficos a nuestra ventana principal(tamaño, titulo, etc)
       
        self.principal = window
        self.principal.title("PRINCIPAL WINDOW APP")
        self.principal.geometry("350x400")
        self.principal.configure(pady="4px",padx="4px")
        self.principal.resizable(False,False)

        #Boton para cargar archivos
        self.loadButton= Button(self.principal,text="Abrir Archivo",
            command=lambda:Loadfile.fileSelect(window),
            width=22,
            height=3)
        self.loadButton.grid()
        
        #Boton para gestionar cursos
        self.management=Button(self.principal,text="Gestionar Cursos",
        command=lambda:ManagementCourses(window),
        width=22,
        height=3) 
        self.management.grid()


        #Boton para salir del programa
        self.exit= Button(self.principal,text="Salir",
        command=self.closeFunction.closeProgram,
        width=22,
        height=3)
        self.exit.grid()


        #Label con la informacion solicitada
        self.labelCurso=Label(self.principal,text="Nombre del Curso: Lab. Lenguajes Formales y de Programación").grid()
        self.labelEstudiantes=Label(self.principal,text="Andy Roberto Jimenez Macnab").grid()
        self.labelCarne=Label(self.principal,text="20211490").grid()
        





    

    
    


        
        
    
        




