
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#CLASE GESTION DE CURSOS
class Gestiones:

    #VENTANA GESTION DE CURSOS
    def GestionarCurso(self, contenido):

       self.contenido = contenido #AQUI SE ENCUENTRA LA LISTA CON INFORMACION

       self.window = Tk()

       self.window.geometry('500x500+550+150')
       self.window.configure(background='LightCyan3')
       self.window.resizable(False,False)

       self.button()

       self.window.mainloop()

       return self.contenido

    #BOTONES PARA LA GESTION DE CURSOS
    def button(self):

        boton1 = Button(self.window,text='Listar Cursos',height=2,width=15,command=self.LLamado_Listar_Cursos).place(x=200,y=150)
        boton2 = Button(self.window,text='Agregar Curso',height=2,width=15,command=self.LLamado_Agregar_curso).place(x=200,y=200)
        boton3 = Button(self.window,text='Editar Curso',height=2,width=15,command=self.LLamado_Editar_cursos).place(x=200,y=250)
        boton4 = Button(self.window,text='Eliminar Curso',height=2,width=15,command=self.LLamado_eliminar_cursos).place(x=200,y=300)
        boton5 = Button(self.window,text='Salir',height=2,width=15,command=self.window.destroy).place(x=200,y=350)

    #METOD DE LLAMADO PARA LA VENTANA DE LA LISTA DE CURSOS
    def LLamado_Listar_Cursos(self):

        llamado = Listar_Cursos()

        llamado.lista_cursos(self.contenido)

    #METODO DE LLAMADO PARA LA VENTANA DE AGREGAR CURSOS
    def LLamado_Agregar_curso(self):

        llamado = Agregar_Curso()

        self.contenido = llamado.agregar_curso(self.contenido)

    #METODO DE LLAMADO PARA LA VENTANA DE EDITAR CURSOS
    def LLamado_Editar_cursos(self):

        llamado = Editar_Curso()
        self.contenido = llamado.editar_curso(self.contenido)

    #METODO DE LLAMADO PARA LA VENTANA DE ELIMINAR CURSOS
    def LLamado_eliminar_cursos(self):

        llamado = Eliminar_curso()
        self.contenido = llamado.Eliminar(self.contenido)
        

#CLASE LISTA DE CURSOS 
class Listar_Cursos:


    #METODO VENTANA DE LISTA DE CURSOS
    def lista_cursos(self, contenido) :

        self.contenido = contenido #AQUI SE OBTIENEN LOS DATOS PARA LA TABLA

        self.ventana_lista_cursos = Tk()
        self.ventana_lista_cursos.geometry('600x500+500+150')
        self.ventana_lista_cursos.configure(background='LightCyan3')
        self.ventana_lista_cursos.resizable(0,0)

        self.Tabla()
        self.Botones()
        

        self.ventana_lista_cursos.mainloop()

    #METODO BOTONES LISTA DE CURSOS
    def Botones(self):

        boton = Button(self.ventana_lista_cursos,text='Regresar',height=2,width=15,command=self.ventana_lista_cursos.destroy).place(x=350,y=400)


    #TABLA DINAMICA PARA LA LISTA DE LOS CURSOS
    def Tabla(self):

        #UTILIZACION DE TREEVIEW PARA CREAR LA TABLA 
        tb = ttk.Treeview(self.ventana_lista_cursos, columns=('col0','col1','col2','col3','col4','col5','col6'), show='headings')
        tb.place(x=10,y=20)

        #CREACION DE COLUMNAS CON PROPIEDADES
        #tb.column('#0',width=80)
        tb.column('col0',width=80,anchor=CENTER)
        tb.column('col1',width=80,anchor=CENTER)
        tb.column('col2',width=80,anchor=CENTER)
        tb.column('col3',width=80,anchor=CENTER)
        tb.column('col4',width=80,anchor=CENTER)
        tb.column('col5',width=80,anchor=CENTER)
        tb.column('col6',width=80,anchor=CENTER)

        #TITULO DE LAS COLUMNAS
        #tb.heading('#0',text='Código',anchor = CENTER)
        tb.heading('col0',text='Código',anchor = CENTER)
        tb.heading('col1',text='Nombre',anchor = CENTER)
        tb.heading('col2',text='Pre-Requisito',anchor = CENTER)
        tb.heading('col3',text='Opcionalidad',anchor = CENTER)
        tb.heading('col4',text='Semestre',anchor = CENTER)
        tb.heading('col5',text='Creditos',anchor = CENTER)
        tb.heading('col6',text='Estado',anchor = CENTER)

            #CICLO FOR PARA PODER CREAR CONTENIDO EN LA TABLA
        for i in self.contenido:

            tb.insert('',END, values=i)


        
        

#CLASE PARA AGREGAR UN CRUSO
class Agregar_Curso:

    #METODO  VENTANA AGREGAR CURSO
    def agregar_curso(self, contenido):

        self.contenido = contenido

        self.ventana_agregar = Tk()
        self.ventana_agregar.geometry('500x500+550+150')
        self.ventana_agregar.configure(background='LightCyan3')
        self.ventana_agregar.resizable(0,0)

        self.Etiquetas()
        self.Textbox()
        self.Botones()

        self.ventana_agregar.mainloop()


        return self.contenido

    #LABELS DE VENTANA
    def Etiquetas(self):

        etiqueta1 = Label(self.ventana_agregar,text='Código',background='LightCyan3').place(x=100,y=50)
        etiqueta2 = Label(self.ventana_agregar,text='Nombre',background='LightCyan3').place(x=100,y=100)
        etiqueta3 = Label(self.ventana_agregar,text='Pre-Requisito',background='LightCyan3').place(x=100,y=150)
        etiqueta4 = Label(self.ventana_agregar,text='Semestre',background='LightCyan3').place(x=100,y=200)
        etiqueta5 = Label(self.ventana_agregar,text='Opcionalidad',background='LightCyan3').place(x=100,y=250)
        etiqueta6 = Label(self.ventana_agregar,text='creditos',background='LightCyan3').place(x=100,y=300)
        etiqueta7 = Label(self.ventana_agregar,text='Estado',background='LightCyan3').place(x=100,y=350)

    #CAJAS DE TEXTO DE LA VENTANA
    def Textbox(self):
        
        caja1 = StringVar()
        caja2 = StringVar()
        caja3 = StringVar()
        caja4 = StringVar()
        caja5 = StringVar()
        caja6 = StringVar()
        caja7 = StringVar()


        self.Caja1 = Entry(self.ventana_agregar,textvariable= caja1)
        self.Caja1.place(x=250,y=50)
        self.Caja2 = Entry(self.ventana_agregar,textvariable= caja2)
        self.Caja2.place(x=250,y=100)
        self.Caja3 = Entry(self.ventana_agregar,textvariable= caja3)
        self.Caja3.place(x=250,y=150)
        self.Caja4 = Entry(self.ventana_agregar,textvariable= caja4)
        self.Caja4.place(x=250,y=200)
        self.Caja5 = Entry(self.ventana_agregar,textvariable= caja5)
        self.Caja5.place(x=250,y=250)
        self.Caja6 = Entry(self.ventana_agregar,textvariable= caja6)
        self.Caja6.place(x=250,y=300)
        self.Caja7 = Entry(self.ventana_agregar,textvariable= caja7)
        self.Caja7.place(x=250,y=350)

        
    #METODO PARA AGREGAR BOTONES
    def Botones(self):

        boton1 = Button(self.ventana_agregar,text='Agregar',height=2,width=15,command=self.agregar).place(x=100,y=400)
        boton2 = Button(self.ventana_agregar,text='Regresar',height=2,width=15, command=self.ventana_agregar.destroy).place(x=300,y=400)

    def agregar(self):

        nuevo = []
        codigo = self.Caja1.get()
        nombre = self.Caja2.get()
        prerequisitos = self.Caja3.get()
        semestre = self.Caja4.get()
        opcionalidad = self.Caja5.get()
        creditos = self.Caja6.get()
        estado = self.Caja7.get()

        nuevo.append(codigo)
        nuevo.append(nombre)
        nuevo.append(prerequisitos)
        nuevo.append(opcionalidad)
        nuevo.append(semestre)
        nuevo.append(creditos)
        nuevo.append(estado)

        if codigo.isnumeric() and semestre.isnumeric() and creditos.isnumeric() and (opcionalidad =='1' or opcionalidad=='0') and (estado == '1' or estado =='0' or estado =='-1'):

            self.contenido.append(nuevo)
            print(nuevo)
            messagebox.showinfo(message="CURSO AGREGADO")

        else:

            messagebox.askretrycancel(message='LOS DATOS QUE INGRESO NO SON CORRECTOS', title='Error')

        


class Editar_Curso:
    
    #METODO  VENTANA AGREGAR CURSO
    def editar_curso(self, contenido):
        
        self.contenido = contenido

        self.ventana_editar = Tk()
        self.ventana_editar.geometry('500x500+550+150')
        self.ventana_editar.configure(background='LightCyan3')
        self.ventana_editar.resizable(0,0)

        self.Etiquetas()
        self.Textbox()
        self.Botones()

        self.ventana_editar.mainloop()

        return self.contenido

    #LABELS DE VENTANA
    def Etiquetas(self):

        etiqueta1 = Label(self.ventana_editar,text='Código',background='LightCyan3').place(x=100,y=50)
        etiqueta2 = Label(self.ventana_editar,text='Nombre',background='LightCyan3').place(x=100,y=100)
        etiqueta3 = Label(self.ventana_editar,text='Pre-Requisito',background='LightCyan3').place(x=100,y=150)
        etiqueta4 = Label(self.ventana_editar,text='Semestre',background='LightCyan3').place(x=100,y=200)
        etiqueta5 = Label(self.ventana_editar,text='Opcionalidad',background='LightCyan3').place(x=100,y=250)
        etiqueta6 = Label(self.ventana_editar,text='creditos',background='LightCyan3').place(x=100,y=300)
        etiqueta7 = Label(self.ventana_editar,text='Estado',background='LightCyan3').place(x=100,y=350)

    #CAJAS DE TEXTO DE LA VENTANA
    def Textbox(self):
        
        caja1 = StringVar()
        caja2 = StringVar()
        caja3 = StringVar()
        caja4 = StringVar()
        caja5 = StringVar()
        caja6 = StringVar()
        caja7 = StringVar()


        self.Caja1 = Entry(self.ventana_editar,textvariable= caja1)
        self.Caja1.place(x=250,y=50)
        self.Caja2 = Entry(self.ventana_editar,textvariable= caja2)
        self.Caja2.place(x=250,y=100)
        self.Caja3 = Entry(self.ventana_editar,textvariable= caja3)
        self.Caja3.place(x=250,y=150)
        self.Caja4 = Entry(self.ventana_editar,textvariable= caja4)
        self.Caja4.place(x=250,y=200)
        self.Caja5 = Entry(self.ventana_editar,textvariable= caja5)
        self.Caja5.place(x=250,y=250)
        self.Caja6 = Entry(self.ventana_editar,textvariable= caja6)
        self.Caja6.place(x=250,y=300)
        self.Caja7 = Entry(self.ventana_editar,textvariable= caja7)
        self.Caja7.place(x=250,y=350)

    
    #METODO PARA AGREGAR BOTONES
    def Botones(self):

        boton1 = Button(self.ventana_editar,text='Editar',height=2,width=15,command=self.editar).place(x=100,y=400)
        boton2 = Button(self.ventana_editar,text='Regresar',height=2,width=15, command=self.ventana_editar.destroy).place(x=300,y=400)


    def editar(self):

        nuevo = []
        codigo = self.Caja1.get()
        nombre = self.Caja2.get()
        prerequisitos = self.Caja3.get()
        semestre = self.Caja4.get()
        opcionalidad = self.Caja5.get()
        creditos = self.Caja6.get()
        estado = self.Caja7.get()

        nuevo.append(codigo)
        nuevo.append(nombre)
        nuevo.append(prerequisitos)
        nuevo.append(opcionalidad)
        nuevo.append(semestre)
        nuevo.append(creditos)
        nuevo.append(estado)

        if codigo.isnumeric() and semestre.isnumeric() and creditos.isnumeric() and (opcionalidad =='1' or opcionalidad=='0') and (estado == '1' or estado =='0' or estado =='-1'):

            repetido = BooleanVar()
            ubicacion = IntVar()
            r = 0
            
            for i in self.contenido:
                
                if i[0] == codigo:

                    repetido = True

                    ubicacion = r
                else:

                    r+=1
            
            if repetido == True:

                self.contenido[ubicacion][0] = codigo
                self.contenido[ubicacion][1] = nombre
                self.contenido[ubicacion][2] = prerequisitos
                self.contenido[ubicacion][3] = semestre
                self.contenido[ubicacion][4] = opcionalidad
                self.contenido[ubicacion][5] = creditos
                self.contenido[ubicacion][6] = estado
                messagebox.showinfo(message="CURSO EDITADO!")

            else:

                messagebox.showinfo(message="CURSO NO ENCONTRADO PARA EDITAR")

            

        else:

            messagebox.askretrycancel(message='LOS DATOS QUE INGRESO NO SON CORRECTOS', title='Error')


#CLASE ELIMINAR CURSOSO 
class Eliminar_curso:

    #METODO VENTANA PARA ELIMINAR CURSOS
    def Eliminar(self,contenido):

        self.contenido = contenido

        self.ventana_eliminar = Tk()
        self.ventana_eliminar.geometry('500x500+550+150')
        self.ventana_eliminar.configure(background='LightCyan3')
        self.ventana_eliminar.resizable(0,0)

        self.componentes()

        self.ventana_eliminar.mainloop()


        return self.contenido


    #COMPONENETES VENTANA ELIMINAR CURSOS
    def componentes(self):

        #ETIQUETAS DE TEXTO
        etiqueta = Label(self.ventana_eliminar,text='Código del Curso',background='LightCyan3').place(x=200,y=100)

        #CAJA DE TEXTO CON SU RESPECTIVA VARIABLE
        caja1 = StringVar()
        self.Caja1 = Entry(self.ventana_eliminar,textvariable=caja1)
        self.Caja1.place(x=200,y=150)

        #BOTONES
        boton1 = Button(self.ventana_eliminar,text='Eliminar',height=2,width=15,command=self.Eliminacion).place(x=100,y=400)
        boton2 = Button(self.ventana_eliminar,text='Regresar',height=2,width=15,command=self.ventana_eliminar.destroy).place(x=300,y=400)

    def Eliminacion(self):

        codigo = self.Caja1.get()

        Encontrado = BooleanVar()
        ubicacion = IntVar()

        cont = 0

        for i in self.contenido:

            if i[0] == codigo:

                Encontrado = True

                ubicacion = cont
            else:

                cont +=1
        
        if Encontrado == True:

            self.contenido.pop(ubicacion)
            messagebox.showinfo(message="CURSO ELIMINADO")

        else:

            messagebox.showinfo(message="CURSO NO ENCONTRADO PARA ELIMINAR")






#CLASE PARA LA VENTANA DE CONTEO DE CREDITOS 
class Conteo_Creditos:

    def Conteo(self, contenido):

        self.conenido = contenido

        self.Conteo = Tk()
        self.Conteo.geometry('500x500+550+150')
        self.Conteo.configure(background='LightCyan3')
        self.Conteo.resizable(0,0)

        self.componenetes()

        self.Conteo.mainloop()

    def componenetes(self):

        #ETIQUETAS DE TEXTO
        etiqueta1 = Label(self.Conteo,text='Creditos Aprobados',background='LightCyan3').place(x=100,y=100)
        etiqueta2 = Label(self.Conteo,text='Creditos Cursados',background='LightCyan3').place(x=100,y=150)
        etiqueta3 = Label(self.Conteo,text='Creditos Pendientes',background='LightCyan3').place(x=100,y=200)
        etiqueta4 = Label(self.Conteo,text='Creditos obligatorios hasta el semestre:',background='LightCyan3').place(x=100,y=250)
        etiqueta5 = Label(self.Conteo,text='Semestre',background='LightCyan3').place(x=200,y=300)
        etiqueta6 = Label(self.Conteo,text='Creditos del semestre',background='LightCyan3').place(x=100,y=350)
        etiqueta7 = Label(self.Conteo,text='Semestre',background='LightCyan3').place(x=200,y=400)

        #CAJA DE TEXTO CON SU RESPECTIVA VARIABLE
        caja1 = StringVar()
        Caja1 = Entry(self.Conteo,textvariable=caja1,width=5).place(x=330,y=250)
        caja2 = StringVar()
        Caja2 = Entry(self.Conteo,textvariable=caja2,width=5).place(x=250,y=350)

        caja3 = StringVar()
        Caja3 = Entry(self.Conteo,textvariable=caja3,width=5,state='disabled').place(x=220,y=100)
        caja4 = StringVar()
        Caja4 = Entry(self.Conteo,textvariable=caja4,width=5,state='disabled').place(x=220,y=150)
        caja5 = StringVar()
        Caja5 = Entry(self.Conteo,textvariable=caja5,width=5,state='disabled').place(x=220,y=200)

        caja6 = StringVar()
        Caja6 = Entry(self.Conteo,textvariable=caja6,width=2,state='disabled').place(x=260,y=300)
        caja7 = StringVar()
        Caja7 = Entry(self.Conteo,textvariable=caja7,width=2,state='disabled').place(x=260,y=400)

        #BOTONES
        boton1 = Button(self.Conteo,text='Contar',height=1,width=5).place(x=300,y=300)
        boton2 = Button(self.Conteo,text='Contar',height=1,width=5).place(x=300,y=400)

        boton3 = Button(self.Conteo,text='↑',height=1,width=1).place(x=280,y=290)
        boton4 = Button(self.Conteo,text='↓',height=1,width=1).place(x=280,y=315)

        boton5 = Button(self.Conteo,text='↑',height=1,width=1).place(x=280,y=390)
        boton6 = Button(self.Conteo,text='↓',height=1,width=1).place(x=280,y=415)

        boton7 = Button(self.Conteo,text='Regresar',height=2,width=15,command=self.Conteo.destroy).place(x=350,y=450)











        
   

        

    