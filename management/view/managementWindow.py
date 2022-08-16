from tkinter import ttk,Tk
from tkinter import *
from principal.controller.loadFile import Loadfile
from management.controller.addcourse import AgregarCurso
from management.controller.editcourse import EditarCurso


class ManagementCourses:
    
    def __init__(self,window) :
        self.principal=window
        self.newWindow= Toplevel()
        self.newWindow.title("Gestionar Cursos")
        self.newWindow.geometry("1420x730")


        #Boton de listar cursos
        self.list=Button(self.newWindow,text="Listar Cursos",
        command=lambda:self.enlistar(),
        width=22,
        height=3).grid(row=1,column=0)

        #Boton agregar cursos
        self.add=Button(self.newWindow,text="Agregar Curso",
        command= lambda:AgregarCurso(window),
        width=22,
        height=3).grid(row=2,column=0)

        #Boton editar curso
        self.edit=Button(self.newWindow,text="Editar Curso",
        command=lambda:EditarCurso(window),
        width=22,
        height=3).grid(row=3,column=0)

        #Boton eliminar curso
        self.delete=Button(self.newWindow,text="Eliminar Curso",
        width=22,
        height=3).grid(row=4,column=0)

        #Boton de Regresar (cerrar la ventana secundaria)
        self.close=Button(self.newWindow,text="Regresar",
        command=lambda:self.newWindow.destroy(),
        width=22
        ,height=3).grid(row=5,column=0)

        #Tabla TreeView donde se mostrarán los datos

        self.tree = ttk.Treeview(self.newWindow,height=16,columns=("0","1","2","3","4","5"))
        self.tree.heading('#0',text="Codigo",anchor=CENTER)
        self.tree.heading('#1',text="Nombre",anchor=CENTER)
        self.tree.heading('#2',text="Prerrequisitos",anchor=CENTER)
        self.tree.heading('#3',text="Obligatorio",anchor=CENTER)
        self.tree.heading('#4',text="Semestre",anchor=CENTER)
        self.tree.heading('#5',text="Créditos",anchor=CENTER)
        self.tree.heading('#6',text="Estado",anchor=CENTER)
        self.tree.grid(row=0,column=0)

        #Campos de texto
        self.codeEdit=Entry(self.newWindow).grid(row=1,column=1)
        self.codeDelete= Entry(self.newWindow).grid(row=2,column=1)
        

    def enlistar(self):
        filas=Loadfile.fileReader(self.principal)
        treeview=self.tree
        records= treeview.get_children()
        for element in records:
            treeview.delete(element)

        for row in filas:
            treeview.insert("",0,text=row["Codigo"],values=(row["Nombre"],
            row["Prerrequisito"],row["Obligatorio"],row["Semestre"],row["Creditos"],row["Estado"]
            ))


            



        
        





       
        
        
