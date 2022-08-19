from tkinter import ttk
from tkinter import *
from tkinter import filedialog as filedialog
from tkinter import messagebox as MessageBox
from principal.model.fileData import FileLoad
import csv

class Loadfile():
    
    def __init__(self,window):
        self.principal=window
        self.archivo=" "
        self.cursos=[]

    #Funcion que mostrará la ventana para seleccionar un archivo csv
    def fileSelect(self):
        self.archivo=filedialog.askopenfilename(
            title="Abrir",
            initialdir="C:/Escritorio"
        )
        print(self.archivo)
        return self.archivo

    #Funcion que leerá el archivo ingresado
    def fileReader(self):
        separador=","
        try:
            with open(self.archivo)as csvfile:
             self.cursos = []
             for linea in csvfile:
                    linea = linea.rstrip('\n')
                    columnas = linea.split(separador)
                    code = columnas[0]
                    nombreCurso = columnas[1]
                    prerrequisito = columnas[2] 
                    obligatorio = columnas[3]
                    semestreNo = columnas[4]
                    creditos = columnas[5]
                    estado = columnas[6]
                    self.cursos.append({
                        "Codigo": int(code),
                        "Nombre": nombreCurso,
                        "Prerrequisito": prerrequisito,
                        "Obligatorio": obligatorio,
                        "Semestre": int(semestreNo),
                        "Creditos": creditos,
                        "Estado": estado
                    })
             return self.cursos
               
                
        #Excepciones en caso el usuario no cargue correctamente el archivo
        except AttributeError:
            MessageBox.showerror("FALLO EN LA EJECUCION",
            "Debes cargar un archivo csv primero para poder ser leído")
        except FileNotFoundError:
            MessageBox.showerror("FALLO EN LA EJECUCION",
            "Debes cargar un archivo csv primero para poder ser leído")
    def diccionario(self):
        return self.cursos


        
        

    