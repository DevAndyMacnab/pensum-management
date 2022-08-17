from tkinter import ttk,Tk
from tkinter import *

class EditarcursoView:
    def __init__(self,window) -> None:
        self.principal=window
        self.principal= Toplevel()
        self.principal.title("Editar el curso elegido")
        self.principal.geometry("300x500")


        #LABELS DE LA VENTANA
        Label(self.principal,text="Código").grid(row=0,column=0)
        Label(self.principal,text="Nombre").grid(row=1,column=0)
        Label(self.principal,text="Prerrequisito").grid(row=2,column=0)
        Label(self.principal,text="Semestre").grid(row=3,column=0)
        Label(self.principal,text="Opcionalidad").grid(row=4,column=0)
        Label(self.principal,text="Créditos").grid(row=5,column=0)
        Label(self.principal,text="Estado").grid(row=6,column=0)

        #ENTRY'S DE LA VENTANA PARA EDITAR LA INFORMACION

        self.codigo=Entry(self.principal).grid(row=0,column=1)
        self.nombre=Entry(self.principal).grid(row=1,column=1)
        self.pre=Entry(self.principal).grid(row=2,column=1)
        self.semestre=Entry(self.principal).grid(row=3,column=1)
        self.opcionalidad=Entry(self.principal).grid(row=4,column=1)
        self.creditos=Entry(self.principal).grid(row=5,column=1)
        self.estado=Entry(self.principal).grid(row=6,column=1)

        #BOTONES DE LA VENTANA
        self.addEvent=Button(self.principal,text="Editar",
        width=17,
        height=3).grid(row=8,column=0)

        self.regresar=Button(self.principal,text="Regresar",
        command=lambda:self.principal.destroy(),
        width=17,
        height=3).grid(row=8,column=1)