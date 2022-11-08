from vueloBuilder import VueloBuilder
from arista import AristaBuilder
from grafo import Grafo
from nodo import Nodo
import csv
class ProgramControler:
    def __init__(self,datos:str) -> None:
        self.g = Grafo() #Instansiacion del grafo
        self.leer_datos(datos)
        

    def leer_datos(self,datos:str)-> None:
        with open(datos) as datos:
            csv_reader = csv.reader(datos)
            line_read = 0
            nodo1 = Nodo()
            nodo2 = Nodo()
            #Mejorar el if
            for row in csv_reader:
                if line_read % 2 == 0 and line_read >= 2:
                    nodo1 = Nodo(VueloBuilder.of_list(row))
                    line_read = line_read + 1
                    continue
                elif line_read % 2 != 0 and line_read >=2:
                    #Agregar datos en el grafo 
                    #Validar si el travel code es igual
                    nodo2 = Nodo(VueloBuilder.of_list(row))
                    self.g.agregar_arista(AristaBuilder.create(nodo1,nodo2))
                    
                line_read = line_read + 1 

    
    