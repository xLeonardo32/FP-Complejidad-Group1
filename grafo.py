from arista import Arista
from nodo import Nodo

class Grafo:
    def __init__(self) -> None:
        self.__aristas = []
    
    def agregar_arista(self,arista:Arista):
        if arista not in self.__aristas:
            self.__aristas.append(arista)
        
    
    def __str__(self) -> str:
        return str([str(arista) for arista in self.__aristas])
    
    