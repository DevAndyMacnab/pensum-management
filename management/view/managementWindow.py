from tkinter import ttk,Tk
from tkinter import *
class ManagementCourses:
    
    def __init__(self,window) :
        self.principal=window
        self.newWindow= Toplevel()
        
        self.newWindow.title("Gestionar Cursos")
        self.newWindow.geometry("1280x720")
        self.newWindow.resizable(False,False)
        


        #Boton de listar cursos
        self.list=Button(self.newWindow,text="Listar Cursos",
        width=22,
        height=3).grid()

        #Boton agregar cursos
        self.add=Button(self.newWindow,text="Agregar Curso",
        width=22,
        height=3).grid()

        #Boton editar curso
        self.edit=Button(self.newWindow,text="Editar Curso",
        width=22,
        height=3).grid()

        #Boton eliminar curso
        self.delete=Button(self.newWindow,text="Eliminar Curso",
        width=22,
        height=3).grid()

        #Regresar (cerrar la ventana secundaria)
        self.close=Button(self.newWindow,text="Regresar",
        command=lambda:self.newWindow.destroy(),
        width=22
        ,height=3).grid()




       
        
        
