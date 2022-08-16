from tkinter import *


class Gestiones:


    def GestionarCurso(self):

       self.window = Tk()

       self.window.geometry('500x500+550+150')
       self.window.configure(background='orange')
       self.window.resizable(False,False)

       self.button()

       self.window.mainloop()

    
    def button(self):

        boton1 = Button(self.window,text='Listar Cursos',height=2,width=15).place(x=200,y=150)
        boton2 = Button(self.window,text='Agregar Curso',height=2,width=15).place(x=200,y=200)
        boton3 = Button(self.window,text='Editar Curso',height=2,width=15).place(x=200,y=250)
        boton4 = Button(self.window,text='Eliminar Curso',height=2,width=15).place(x=200,y=300)
        boton5 = Button(self.window,text='Salir',height=2,width=15,command=self.window.destroy).place(x=200,y=350)
        
   

        

    