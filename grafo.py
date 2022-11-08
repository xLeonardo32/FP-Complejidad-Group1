from arista import Arista
from nodo import Nodo

class Grafo:
    def __init__(self) -> None:
        self.__aristas = []
        self.__listady = dict() #Lista de adyacencia
        
        
    def agregar_arista(self,arista:Arista):
        if arista not in self.__aristas:
            self.__aristas.append(arista)
        else:
            print('No se agrego porque son aristas iguales')
    
    def eliminar_arista(self,arista:Arista):
        self.__aristas.remove(arista)

    def get_list_ady(self):
        for arista in self.__aristas:
            if arista.es_dirigido():
                pass
            else:
                #Se agregar dos veces porque son aristas bidireccionales
                self.agregar_ady(arista.get_nodo1(),arista.get_nodo2())
                self.agregar_ady(arista.get_nodo2(),arista.get_nodo1())
        
        return self.__listady  
                
            
    def agregar_ady(self,nodo1:Nodo,nodo2:Nodo):
        if nodo1 in self.__listady:
            self.__listady[nodo1].append([nodo2])
        else:
            self.__listady[nodo1] = [[nodo2]]
    
    def print_list_ady(self):
        print('Entro')
        self.__listady.clear()
        self.get_list_ady()
        
        for key in self.__listady.keys():
            print(key.dato,'--->',end="")
            for value in self.__listady[key]:
                print(value[0])
            
                 
            
               
    def __str__(self) -> str:
        return str([str(arista) for arista in self.__aristas])
    
    