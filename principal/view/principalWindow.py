from tkinter import filedialog, ttk,Tk
from tkinter import *

class Principal:

    def __init__(self,window) :
        #Aqui damos parametros graficos a nuestra ventana principal(tamaño, titulo, etc)
        self.principal = window
        self.principal.title("PRINCIPAL WINDOW APP")
        self.principal.geometry("800x500")
        self.principal.configure(background="#C84D32",pady="4px",padx="4px")


        #Boton para cargar archivos
        self.loadButton= Button(self.principal,text="Open File",command=self.loadFile,width=22,height=3)
        self.loadButton.grid(row= 2,column = 4)
        self.loadButton.pack()
        
        
           
    
    #Funcion para cargar archivos CSV al programa
    def loadFile(self):
        self.archivo = filedialog.askopenfilename(title="Abrir", initialdir="C:/") 
        print(self.archivo)


if __name__ == '__principalWindow__':
    window = Tk()
    application = Principal(window)
    #Funcion para que se ejecute la ventana principal en bucle
    window.mainloop()
