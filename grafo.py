from arista import Arista
from nodo import Nodo
from Vuelo import Vuelo

class Grafo:
    def __init__(self) -> None:
        self.__aristas = []
        self.__listady = dict() #Lista de adyacencia
        
    @property
    def aristas(self):
        return self.__aristas
    
    def print_aristas(self):
        for arista in self.aristas:
            print(arista)

    def print_vuelos(self):
        for arista in self.aristas:
            print(arista, arista.print_vuelos())
             
    def agregar_arista(self,arista:Arista,vuelo:Vuelo):
        if arista not in self.__aristas:
            #print(arista)
            arista.agregar_vuelo(vuelo)
            self.__aristas.append(arista)
        else:
            self.aristas[self.aristas.index(arista)].agregar_vuelo(vuelo)
            #arista.agregar_vuelo(vuelo)
            #print(arista)
            #print('No se agrego porque son aristas iguales')
    
    def eliminar_arista(self,arista:Arista):
        self.__aristas.remove(arista)

    def get_list_ady(self):
        for arista in self.__aristas:
            if arista.es_dirigido():
                pass
            else:
                #Se agregar dos veces porque son aristas bidireccionales
                self.agregar_ady(arista.get_nodo1(),arista.get_nodo2())
                #self.agregar_ady(arista.get_nodo2(),arista.get_nodo1())
        
        return self.__listady  
                
            
    def agregar_ady(self,nodo1:Nodo,nodo2:Nodo):
        if nodo1 in self.__listady:
            #print('Si esta')
            self.__listady[nodo1].append([nodo2])
        else:
            self.__listady[nodo1] = [[nodo2]]
    
    def print_list_ady(self):
        self.__listady.clear()
        self.get_list_ady()
        
        for key in self.__listady.keys():
            print(key.dato,'--->',end="")
            for value in self.__listady[key]:
                print(value[0])
            
                 
            
               
    def __str__(self) -> str:
        return str([str(arista) for arista in self.__aristas])
    
    