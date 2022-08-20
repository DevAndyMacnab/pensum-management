from tkinter import ttk,Tk
from tkinter import *

from principal.controller.loadFile import Loadfile


class CreditsWindow:
    def __init__(self,window,diccionario) :
        self.diccionario=diccionario
        print(self.diccionario)
        self.principal= window
        self.newWindow= Toplevel()
        self.newWindow.title("Conteo de Créditos")
        self.newWindow.geometry("630x400")

        

        #Labels con los datos iniciales , no alterados durante la ejecucion de la ventana
        self.aprobados=Label(self.newWindow,text="Créditos Aprobados: XX")
        self.aprobados.grid(row=0,column=0)
        self.cursando= Label(self.newWindow,text="Créditos Cursando: XX")
        self.cursando.grid(row=1,column=0)
        self.pendientes= Label(self.newWindow,text="Créditos Pendientes")
        self.pendientes.grid(row=2,column=0)

        self.semestreAprobados=Label(self.newWindow,text="Creditos Aprobados del semestre: ")
        self.semestreAprobados.grid(row=8,column=2)

        self.semestreAsignados= Label(self.newWindow,text="Creditos asignados del semestre: ")
        self.semestreAsignados.grid(row=9,column=2)

        self.semestrePendientes= Label(self.newWindow,text="Creditos pendientes del semestre: ")
        self.semestrePendientes.grid(row=10,column=2)


        #Seccion de creditos obligatorios hasta el semestre N
        self.hastaSemestreN=Label(self.newWindow,text="Créditos obligatorios hasta semestre N:")
        self.hastaSemestreN.grid(row=3,column=0)
        Label(self.newWindow,text="Semestre").grid(row=4,column=0)
        Label(self.newWindow,text="Créditos del semestre:").grid(row=5,column=0)
        Label(self.newWindow,text="Semestre:").grid(row=6,column=0)




        #Botones utilizados dentro de la ventana
        self.buttonsemestreN=Button(self.newWindow,text="Contar N",
        width=10,
        height=2,
        command=self.creditosHastaN
        ,padx=5)
        self.buttonsemestreN.grid(row=4,column=3)
        
        self.buttonSemestre=Button(self.newWindow,text="Contar",
        command=self.creditosDeSemestre,
        width=10
        ,height=2,
        padx=12,
        pady=4)
        self.buttonSemestre.grid(row=6,column=3)

        self.regresar=Button(self.newWindow,text="Regresar",
        command=lambda:self.newWindow.destroy(),
        width=10,
        height=2,
        pady=4).grid(row=9,column=0)

        self.actualizar=Button(self.newWindow,text="Actualizar",
        command=lambda:[self.creditosAprobados(),
        self.creditosCursando(),self.creditosPendientes()],
        width=10,
        height=2
        ,padx=12,
        pady=4)
        self.actualizar.grid(row=8,column=0)

        #Entry utilizados dentro de la ventana

        self.entrySemestre=Entry(self.newWindow)
        self.entrySemestre.grid(row=4,column=1)


        self.entrySemestre2=Entry(self.newWindow)
        self.entrySemestre2.grid(row=6,column=1)



    def entrada(self,diccionario):
        self.dicio=diccionario

        
        return self.diccionario

    def creditosAprobados(self):
        self.dicc=self.diccionario
        sumaCreditos=0
        for recorrido in self.dicc:
            if recorrido["Estado"]=='0':
                sumaCreditos=sumaCreditos + recorrido["Creditos"]

        self.aprobados["text"]="Créditos Aprobados: " , sumaCreditos 
        

    def creditosCursando(self):
        sumaCreditos=0
        for recorrido in self.diccionario:
            if recorrido["Estado"]=='1':
                sumaCreditos=sumaCreditos + recorrido["Creditos"]

        self.cursando["text"]="Créditos cursando: ", sumaCreditos
    
    def creditosPendientes(self):
        sumaCreditos=0
        for recorrido in self.diccionario:
            if recorrido["Estado"]=='-1':
                sumaCreditos= sumaCreditos + recorrido["Creditos"]

        self.pendientes["text"]="Creditos pendiente: ", sumaCreditos

    def creditosHastaN(self):
        sumaCreditos=0
        self.buscador=int(self.entrySemestre.get())
        for recorrido in self.diccionario:
            if recorrido["Semestre"]< self.buscador+1:
                if recorrido["Estado"]=='1':
                    sumaCreditos= sumaCreditos + recorrido["Creditos"]
            else:
                break

        self.hastaSemestreN["text"]="Créditos obligatorios hasta semestre N:" , sumaCreditos

    def creditosDeSemestre(self):
        sumaAprobados=0
        sumaAsignados=0
        sumaPendientes=0
        self.buscador=int(self.entrySemestre2.get())
        print(self.buscador)
        for recorrido in self.diccionario:
            if recorrido["Semestre"]== self.buscador:
                if recorrido["Estado"]=='0':
                    sumaAprobados= sumaAprobados + recorrido["Creditos"]
                elif recorrido["Estado"]=='1':
                    sumaAsignados= sumaAsignados + recorrido["Creditos"]
                elif recorrido["Estado"]=='-1':
                    sumaPendientes= sumaPendientes + recorrido["Creditos"]
        self.semestreAprobados["text"]= "Creditos Aprobados del semestre: ", sumaAprobados
        self.semestreAsignados["text"]="Creditos asignados del semestre: ", sumaAsignados
        self.semestrePendientes["text"]="Creditos pendientes del semestre", sumaPendientes

       


        



