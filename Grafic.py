
from tkinter import *
from tkinter import filedialog

from Analizador import *
from VentasAux import *


class Ventana:

    direccion =''
    

    def __init__(self):

        print('INICIANDO PROGRAMA...')

    
    #METODO DE INICIACION VENTANA PRINCIPAL
    def Window(self):

        self.ventana = Tk()
        self.ventana.geometry('500x500+550+150')
        self.ventana.configure(background='LightCyan3')
        self.ventana.resizable(False,False)

     
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



         boton1 = Button(text='Abrir Archivo',command=self.AbrirArchivo,height=2,width=15).place(x=200,y=150)
         boton2 = Button(text='Gestionar Cursos',command=self.AbrirGestion,height=2,width=15).place(x=200,y=200)
         boton3 = Button(text='Conteo de Creditos',command=self.AbrirConteo,height=2,width=15).place(x=200,y=250)
         boton4 = Button(text='Salir',command=self.ventana.destroy,height=2,width=15).place(x=200,y=300)
         



    #METODO PARA LA SELECCION DE ARCHIVO 
    def AbrirArchivo(self):

        archivo = filedialog.askopenfilename(title="Abrir",initialdir="C:/", filetypes=(('Archivos CSV','*.csv'),('Archivos LFP','*.lfp')))
        self.direccion = archivo
        self.Analisis = Analisis(self.direccion)
        self.Contenido = Analisis.Contenido
       # print(self.Contenido)

    #metodod para llamar ventana de gestion de cursos 
    def AbrirGestion(self):

       gestiones = Gestiones()

       self.Contenido = gestiones.GestionarCurso(self.Contenido)

    def AbrirConteo(self):

        conteo = Conteo_Creditos()
        conteo.Conteo(self.Contenido)








        


    
        

        
        


