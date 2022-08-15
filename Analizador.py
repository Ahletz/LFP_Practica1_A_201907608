# encoding:utf-8

class Analisis:

    texto = None
    Contenido = []

    def __init__(self, ubicacion):

        print('COMENZANDO ANALISIS')

        self.ubicacion = ubicacion  # OBTENCION DE UBICACION DE DOCUMENTO

        contenido = open(self.ubicacion, encoding='utf-8')  # ABRIR ARCHIVO

        self.texto = contenido.read()  # OBTENER EL CONTENIDO DEL ARCHIVO

        self.Analizador() #LLAMADO DEL METODO PARA ANALIZAR EL CONTENIDO 

    def Analizador(self):

        txt = self.texto + '\n' 
        linea = ''


        #SEPARACION DEL TEXTO Y MANIPULACION EN LISTA
        for i in txt:

            if i != '\n':

                linea += i

            else:

                lista = linea.split(',')
                self.Contenido.append(lista)
                linea = ''


