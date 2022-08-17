from tkinter import ttk,Tk
from tkinter import *
from tkinter import messagebox as MessageBox
from principal.controller.loadFile import Loadfile



class AddcourseView:
    def __init__(self,window) :
        self.newWindow= window
        self.principal= Toplevel()
        self.principal.title("Agregar un nuevo curso")
        self.principal.geometry("300x500")
        self.newList=[]

        #LABELS DE LA VENTANA
        Label(self.principal,text="Código").grid(row=0,column=0)
        Label(self.principal,text="Nombre").grid(row=1,column=0)
        Label(self.principal,text="Prerrequisito").grid(row=2,column=0)
        Label(self.principal,text="Semestre").grid(row=3,column=0)
        Label(self.principal,text="Opcionalidad").grid(row=4,column=0)
        Label(self.principal,text="Créditos").grid(row=5,column=0)
        Label(self.principal,text="Estado").grid(row=6,column=0)

        #ENTRY'S DE LA VENTANA PARA AGREGAR CURSO
        self.codigo=Entry(self.principal)
        self.codigo.grid(row=0,column=1)
        
        self.nombre=Entry(self.principal)
        self.nombre.grid(row=1,column=1)

        self.pre=Entry(self.principal)
        self.pre.grid(row=2,column=1)

        self.semestre=Entry(self.principal)
        self.semestre.grid(row=3,column=1)

        self.opcionalidad=Entry(self.principal)
        self.opcionalidad.grid(row=4,column=1)

        self.creditos=Entry(self.principal)
        self.creditos.grid(row=5,column=1)

        self.estado=Entry(self.principal)
        self.estado.grid(row=6,column=1)


        #BOTONES DE LA VENTANA
        
        self.addEvent=Button(self.principal,text="Agregar",
        command=lambda:self.convertToList(),
        width=17,
        height=3).grid(row=8,column=0)


        self.regresar=Button(self.principal,text="Regresar",
        command=lambda:self.principal.destroy(),
        width=17,
        height=3).grid(row=8,column=1)

    def convertToList(self):
        self.newList.append({

                "Codigo": self.codigo.get(),
                "Nombre": self.nombre.get(),
                "Prerrequisito": self.pre.get(),
                "Obligatorio": self.opcionalidad.get(),
                "Semestre": self.semestre.get(),
                "Creditos": self.creditos.get(),
                "Estado": self.estado.get()    
            })
        return self.newList


