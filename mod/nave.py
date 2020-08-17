'''
Funciones que hacen referencia a la navegación dentro de las carpetas y manejo de archivos.
    Aplicable a cualquier programa

    * Busca archivos (todos o por formato específico)
    * Recorre carpetas con la posibilidad de recorrer subcarpetas
    * Mueve archivos de lugar
    * Elimina archivos
    * Devuelve información sobre los archivos

CODIGOS DEL MÓDULO os    
    * Devuelve la carpeta actual del programa
        - carpeta_actual = os.getcwd()
    
    * Crea una carpeta, en éste caso, en la carpeta actual
        - os.mkdir("Nombre_de_Carpeta")
    
    * Devuelve True/False si en cuentra una carpeta buscada
        - os.path.isdir("Nombre_de_carpeta_buscada")
    
    * Devuelve información de un archivo en bytes
        - Tamaño: os.path.getsize("Archivo.exe")

    * Devuelve una LISTA con todos los archivos y carpetas
        - os.listdir("")
        - os.listdir("D:\\Programación\\Python\\Proyectos\\")
    
    * Elimina carpetas
    * Nota: Únicamente elimina carpetas que estén vacías (VER SHUTIL)
        - os.rmdir("Nombre_del_archivo")

    * Elimina archivos
        - os.unlink("Nombre_del_archivo")

CODIGOS DEL MÓDULO shutil
    * Copia archivos
        - shutil.copy("Ubicacion_completa_del_archivo","Ubicacion_destino")

    * Mueve archivos
        - shutil.move("Ubicacion_completa_del_archivo\\archivo.txt","Ubicacion_destino\\archivo.txt")
    * Al mismo tiempo, si le cambiamos el nombre al segundo parámetro lo renombramos
        - shutil.move("Ubicacion_completa_del_archivo\\archivo.txt","Ubicacion_destino\\archivo_modificado.txt")
    
    * Elimina carpetas con archivos
        - shutil.rmtree("Nombre_de_la_carpeta")
'''
import os
import shutil

# Busca archivos en la carpeta indicada, y subcarpetas si así se indica
    # Se devuelve una variable y 2 listas:
    # (1) Encontrada: variable que indica que el path que se le dió fue encontrado correctamente
    # (2) ListaCar: Lista que tiene todas las carpetas encontradas, siendo la posición 0, la misma carpeta que se usó para llamar a ésta función
    # (3) ListaArc: Lista que contiene todos los archivos encontrados, salvo que están todos juntos y donde a cada uno se le antepone un número para indicar a qué carpeta
        # pertencece dentro de la ListaCar. Entonces por ejemplo si se busca en una carpeta que dentro tiene 4 carpetas, la ListaCar contiene 5 posiciones (de 0 a 4), la 
        # carpeta raíz y las 4 carpetas encontradas, luego en la ListaArc si un archivo por ejemplo dice "4***Musica.mp3", quiere decir que ese tema está dentro de la quinta
        # posición que posee la ListaCar, o sea la última carpeta encontrada.
    # En la variable que llega por parámetro "SubCarpetas_VF" se indica con True/False si se quieren revisar las subcarpetas, y con los Tipo(n) se pueden indicar hasta 10 
    # formatos distintos de archivos, si no se pone nada devuelve todos los archivos encontrados, y si se pone por ejemplo "mp3" sólo devuelve los archivos mp3.
    # IMPORTANTE: Cabe aclarar que deben cargarse en orden los formatos, es decir, que primero hay que utilizar el parámetro Tipo0, luego Tipo1, y así sucesivamente ya que al encontrarse con un parámetro vacío ignora el resto, y también se debe ignorar el punto al indicar el formato: "mp3" = BIEN /// ".mp3" = MAL
def Dev_archivo_lista(Carpeta, SubCarpetas_VF, Tipo0 = "", Tipo1 = "", Tipo2 = "", Tipo3 = "", Tipo4 = "", Tipo5 = "", Tipo6 = "", Tipo7 = "", Tipo8 = "", Tipo9 = ""):
    # Bandera que indica si se encontró la carpeta que vino por parámetro
    Encontrada = False
    # Creamos las listas donde se van a guardar los nombres de carpetas y archivos
    ListaCar = []
    ListaArc = []
    # Este if es sólo verdadero si la carpeta raíz existe
    if os.path.isdir(Carpeta):
        Encontrada = True
        # Cargamos los valores de la lista en la posición actual
        ListaAuxC, ListaAuxA = Dev_Carpetas_Archivos(Carpeta)
        ListaCar.append(Carpeta)
        for pos in ListaAuxC:
            ListaCar.append(Carpeta + "/" + pos)
        for pos in ListaAuxA:
            ListaArc.append("0***" + pos)
        # Si el parámetro "SubCarpetas_VF" es True: Revisamos las subcarpetas, sino no
        if SubCarpetas_VF == True:
            # Si hay carpetas, las analizamos
            Largo = len(ListaCar)
            if Largo > 1:
                cont = 1
                Camino = ""
                Revisar = True
                while Revisar == True:
                    ListaAuxC = []
                    ListaAuxA = []
                    Camino = ListaCar[cont]
                    ListaAuxC, ListaAuxA = Dev_Carpetas_Archivos(Camino)
                    for i in ListaAuxC:
                        ListaCar.append(Camino + "/" + i)
                    for i in ListaAuxA:
                        ListaArc.append(str(cont) + "***" + i)
                    Largo = len(ListaCar)
                    cont += 1
                    if cont == Largo:
                        Revisar = False
        # Una vez que tenemos todos los archivos y carpetas correctos, analizamos sus formatos si es que se han indicado, se aceptan hasta 10 formatos distintos
        if Tipo0 != "" or Tipo1 != "" or Tipo2 != "" or Tipo3 != "" or Tipo4 != "" or Tipo5 != "" or Tipo6 != "" or Tipo7 != "" or Tipo8 != "" or Tipo9 != "":
            # Lista que cargará los archivos que coincidan con la extensión y luego reasignará los valores de la ListaArc
            ListaAuxA = []
            # Contador para recorrer todas las posiciones
            cont = 0
            tope = len(ListaArc)
            # Bucle que recorre todos los archivos y sólo carga en "ListaAuxA" aquellos que contengan las extenciones indicadas por parámetro
            while cont < tope:
                NombreArchivo = ListaArc[cont]
                Extension = Dev_Extencion(NombreArchivo)
                if Tipo0 != "":
                    if Extension == Tipo0:
                        ListaAuxA.append(NombreArchivo)
                    else:
                        if Extension == Tipo1:
                            ListaAuxA.append(NombreArchivo)
                        else:
                            if Tipo2 != "":
                                if Extension == Tipo2:
                                    ListaAuxA.append(NombreArchivo)
                                else:
                                    if Tipo3 != "":
                                        if Extension == Tipo3:
                                            ListaAuxA.append(NombreArchivo)
                                        else:
                                            if Tipo4 != "":
                                                if Extension == Tipo4:
                                                    ListaAuxA.append(NombreArchivo)
                                                else:
                                                    if Tipo5 != "":
                                                        if Extension == Tipo5:
                                                            ListaAuxA.append(NombreArchivo)
                                                        else:
                                                            if Tipo6 != "":
                                                                if Extension == Tipo6:
                                                                    ListaAuxA.append(NombreArchivo)
                                                                else:
                                                                    if Tipo7 != "":
                                                                        if Extension == Tipo7:
                                                                            ListaAuxA.append(NombreArchivo)
                                                                        else:
                                                                            if Tipo8 != "":
                                                                                if Extension == Tipo8:
                                                                                    ListaAuxA.append(NombreArchivo)
                                                                                else:
                                                                                    if Tipo9 != "":
                                                                                        if Extension == Tipo9:
                                                                                            ListaAuxA.append(NombreArchivo)
                cont += 1
            ListaArc = ListaAuxA
    return Encontrada, ListaCar, ListaArc

'''########################################################################################################################################
###########################################################################################################################################
                                FUNCIONES AUXILIARES (Internas utilizadas para ayuda de éste módulo)                                    '''

# Recibe un string y devuelve la extención en formato string sin el punto, ej: "mp3"
    # Recorre desde atrás hasta que encuentra un punto, y devuelve los caracteres recorridos
def Dev_Extencion(Texto):
    Largo = len(Texto)
    cont = 0
    while cont < Largo:
        cont += 1
        pos = 0 - cont
        if Texto[pos] == ".":
            return Texto[pos + 1:]

# Es una función auxiliar. Busca según el path indicado por parámetro y devuelve una lista de carpetas y archivos encontrados.
# Nota: La existencia de la carpeta debe controlarse antes de que se llame a ésta función.
def Dev_Carpetas_Archivos(Carpeta):
    # Creamos las listas donde se van a guardar los nombres de carpetas y archivos
    ListaCar = []
    ListaArc = []
    # Guardamos todos los archivos encontrados en una lista
    Lista2 = os.listdir(Carpeta)
    # Recorremos la lista para separar las carpetas de los archivos y ya quedan las listar cargadas
    Largo = len(Lista2)
    cont = 0
    while cont < Largo:
        if os.path.isdir(Carpeta + "/" + Lista2[cont]):
            ListaCar.append(Lista2[cont])
        else:
            ListaArc.append(Lista2[cont])
        cont += 1
    return ListaCar, ListaArc

