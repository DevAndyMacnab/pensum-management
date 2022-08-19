from tkinter import ttk,Tk
from tkinter import *
from principal.controller.loadFile import Loadfile
from management.view.addCourseview import AddcourseView
from management.view.editCourseview import EditarcursoView


class ManagementCourses:

    
    def __init__(self,window) :
        self.principal=window
        self.newWindow= Toplevel()
        self.newWindow.title("Gestionar Cursos")
        self.newWindow.geometry("1550x700")
        self.diccionario=[]


        #Boton de listar cursos
        self.list=Button(self.newWindow,text="Listar Cursos",
        command=lambda:self.enlistar(),
        width=22,
        height=3,
        state="normal")
        self.list.grid(row=0,column=0)

        #Boton agregar cursos
        self.add=Button(self.newWindow,text="Agregar Curso",
        command= self.agregarCurso,
        width=22,
        height=3).grid(row=1,column=0)

        #Boton editar curso
        self.edit=Button(self.newWindow,text="Editar Curso",
        command=self.editarCurso,
        width=22,
        height=3).grid(row=2,column=0)        

        #Boton eliminar curso
        self.delete=Button(self.newWindow,text="Eliminar Curso",
        command=self.eliminarCurso,
        width=22,
        height=3).grid(row=3,column=0)

        #Boton de Regresar (cerrar la ventana secundaria)
        self.close=Button(self.newWindow,text="Regresar",
        command=lambda:self.newWindow.destroy(),
        width=22
        ,height=3).grid(row=4,column=0)


        #Tabla TreeView donde se mostrarán los datoS
        self.tree = ttk.Treeview(self.newWindow,height=16,
        columns=("0","1","2","3","4","5"))
        self.tree.heading('#0',text="Codigo",anchor=CENTER)
        self.tree.heading('#1',text="Nombre",anchor=CENTER)
        self.tree.heading('#2',text="Prerrequisitos",anchor=CENTER)
        self.tree.heading('#3',text="Obligatorio",anchor=CENTER)
        self.tree.heading('#4',text="Semestre",anchor=CENTER)
        self.tree.heading('#5',text="Créditos",anchor=CENTER)
        self.tree.heading('#6',text="Estado",anchor=CENTER)
        self.tree.grid(row=6,column=0,padx=5,pady=5,columnspan=2,rowspan=2,sticky='nsew')

        #Campos de texto
        self.codeEdit=Entry(self.newWindow)
        self.codeEdit.insert(0,"Editar")
        self.codeEdit.grid(row=3,column=1)

        self.codeDelete= Entry(self.newWindow)
        self.codeDelete.insert(0,"Eliminar")
        self.codeDelete.grid(row=4,column=1)


        #ENTRY'S DE LA VENTANA PARA AGREGAR CURSO
        self.codigo=Entry(self.newWindow)
        self.codigo.insert(0,"Codigo")
        self.codigo.grid(row=0,column=2)
        
        self.nombre=Entry(self.newWindow)
        self.nombre.insert(0,"Nombre")
        self.nombre.grid(row=1,column=2)

        self.pre=Entry(self.newWindow)
        self.pre.insert(0,"Prerrequisito")
        self.pre.grid(row=2,column=2)

        self.semestre=Entry(self.newWindow)
        self.semestre.insert(0,"Semestre")
        self.semestre.grid(row=3,column=2)

        self.opcionalidad=Entry(self.newWindow)
        self.opcionalidad.insert(0,"Opcionalidad")
        self.opcionalidad.grid(row=4,column=2)

        self.creditos=Entry(self.newWindow)
        self.creditos.insert(0,"Créditos")
        self.creditos.grid(row=5,column=2)

        self.estado=Entry(self.newWindow)
        self.estado.insert(0,"Estado")
        self.estado.grid(row=6,column=2)
        

    #FUNCION QUE APLICA LA LISTA AL TREEVIEW
    def enlistar(self):
        self.filas=Loadfile.fileReader(self.principal)

        treeview=self.tree
        records= treeview.get_children()
        for element in records:
            treeview.delete(element)

        for row in self.filas:
            treeview.insert("",0,text=row["Codigo"],values=(row["Nombre"],
            row["Prerrequisito"],row["Obligatorio"],row["Semestre"],row["Creditos"],row["Estado"]
            ))
        self.list["state"]="disabled"
        
        return self.filas

    def agregarCurso(self):
        self.newList=[]
        self.listacompleta=[]
        self.newList.append({

                "Codigo": int(self.codigo.get()),
                "Nombre": self.nombre.get(),
                "Prerrequisito": self.pre.get(),
                "Obligatorio": self.opcionalidad.get(),
                "Semestre": self.semestre.get(),
                "Creditos": self.creditos.get(),
                "Estado": self.estado.get()    
            })
        
        self.filas.extend(self.newList)


        treeview=self.tree
        records= treeview.get_children()
        for element in records:
            treeview.delete(element)

        for row in self.filas:
            treeview.insert("",0,text=row["Codigo"],values=(row["Nombre"],
            row["Prerrequisito"],row["Obligatorio"],row["Semestre"],row["Creditos"],row["Estado"]
            ))
        self.list["state"]="disabled"
        return self.filas

    
    def eliminarCurso(self):
        self.conteo=0
        self.buscador=int(self.codeDelete.get())
        for self.cursos in self.filas:

            if self.cursos["Codigo"]==self.buscador:
                print(self.cursos)
                self.filas.pop(self.conteo)
            else:
                self.conteo=self.conteo+1
        treeview=self.tree
        records= treeview.get_children()
        for element in records:
            treeview.delete(element)

        for row in self.filas:
            treeview.insert("",0,text=row["Codigo"],values=(row["Nombre"],
            row["Prerrequisito"],row["Obligatorio"],row["Semestre"],row["Creditos"],row["Estado"]
            ))
        self.list["state"]="disabled"
        return self.filas



    def editarCurso(self):
        contador=0
        self.search=int(self.codeEdit.get())
        for cursos in self.filas:
            if cursos["Codigo"]==self.search:
                self.filas.pop(contador)
                print(cursos)
                self.filas.append({
                    "Codigo":int(self.codigo.get()),
                    "Nombre": self.nombre.get(),
                    "Prerrequisito": self.pre.get(),
                    "Obligatorio": self.opcionalidad.get(),
                    "Semestre": self.semestre.get(),
                    "Creditos": self.creditos.get(),
                    "Estado": self.estado.get()
                })
            else:
                contador=contador+1
        treeview=self.tree
        records= treeview.get_children()
        for element in records:
            treeview.delete(element)

        for row in self.filas:
            treeview.insert("",0,text=row["Codigo"],values=(row["Nombre"],
            row["Prerrequisito"],row["Obligatorio"],row["Semestre"],row["Creditos"],row["Estado"]
            ))
        self.list["state"]="disabled"
        return self.filas
        

        
                



        
