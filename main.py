from tkinter import Tk,ttk
from principal.view.principalWindow import Principal


if __name__=="__main__":
    #
    wPrincipal=Tk()

    #Recibe los parametros de diseño de la clase Principal 
    application=Principal(wPrincipal)

    #Aqui se inicializa mi ventana principal
    wPrincipal.mainloop()

    




