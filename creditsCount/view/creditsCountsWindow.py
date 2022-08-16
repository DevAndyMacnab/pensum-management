from tkinter import ttk,Tk
from tkinter import *
from turtle import title

class CreditsWindow:
    def __init__(self,window) -> None:
        self.principal= window
        self.newWindow= Toplevel()
        self.newWindow.title("Conteo de Créditos")
        self.newWindow.geometry("600x770")
        self.newWindow.resizable(False,False)

        #Labels con los datos iniciales , no alterados durante la ejecucion de la ventana
        self.aprobados=Label(self.newWindow,text="Créditos Aprobados: XX").grid()
        self.cursando= Label(self.newWindow,text="Créditos Cursando: XX").grid()
        self.pendientes= Label(self.newWindow,text="Créditos Pendientes").grid()

        #Seccion de creditos obligatorios hasta el semestre N
        Label(self.newWindow,text="Créditos obligatorios hasta semestre N:")
        Label(self.newWindow,text="Semestre").grid()
        Label(self.newWindow,text="Créditos del semestre:").grid()
        Label(self.newWindow,text="Semestre:").grid()

        #Botones utilizados dentro de la ventana
        self.buttonsemestreN=Button(self.newWindow,text="Contar hasta N",
        width=22,
        height=3).grid()
        
        self.buttonSemestre=Button(self.newWindow,text="Contar",
        width=22
        ,height=3).grid()

        self.regresar=Button(self.newWindow,text="Regresar",
        command=lambda:self.newWindow.destroy(),
        width=22,
        height=3).grid()

        #Entry utilizados dentro de la ventana
        self.entryN= Entry(self.newWindow).grid(row=6,column=1)
        self.entrySemestre=Entry(self.newWindow).grid(row=7,column=1)
        self.entryCreditos=Entry(self.newWindow).grid(row=8,column=1)
        self.entrySemestre2=Entry(self.newWindow).grid(row=9,column=1)


