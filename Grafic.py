from distutils.cmd import Command
from tkinter import *
from tkinter import filedialog


class Ventana:

    direccion =''

    def __init__(self):

        print('INICIANDO PROGRAMA...')

    
    #METODO DE INICIACION VENTANA PRINCIPAL
    def Window(self):

        self.ventana = Tk()
        self.ventana.geometry('500x500')
        self.ventana.configure(background='LightCyan3')

        self.Etiquetas()
        self.Botones()

        self.ventana.mainloop()
        

    #DATOS DEL ESTUDIANTE MEDIANTE LABELS
    def Etiquetas(self):

        label1 = Label(text='LENGUAJES FORMALES Y DE PROGRAMACION',background='LightCyan3').place(x=5,y=5)
        label2 = Label(text='LUDWING ALEXANDER LOPEZ ORTIZ',background='LightCyan3').place(x=5,y=20)
        label3 = Label(text='201907608',background='LightCyan3').place(x=5,y=35)


    #BOTONES DE LA PANTALLA PRINCIPAL
    def Botones(self):



         boton1 = Button(text='Abrir Archivo',command=self.AbrirArchivo,height=2,width=15).place(x=100,y=100)
         boton2 = Button(text='Gestionar Cursos',command=self.AbrirArchivo,height=2,width=15).place(x=100,y=150)
         boton3 = Button(text='Conteo de Creditos',command=self.AbrirArchivo,height=2,width=15).place(x=100,y=200)
         boton4 = Button(text='Salir',command=self.ventana.destroy,height=2,width=15).place(x=100,y=250)
         



    #METODO PARA LA SELECCION DE ARCHIVO 
    def AbrirArchivo(self):
        archivo = filedialog.askopenfilename(title="Abrir",initialdir="C:/")
        self.direccion = archivo

        
        


