from tkinter import Tk,ttk
from tkinter import *
from principal.view.principalWindow import Principal


if __name__=="__main__":
    #Ejecucion de ventana principal del programa
    wPrincipal=Tk()
    application=Principal(wPrincipal)
    wPrincipal.mainloop()

    




