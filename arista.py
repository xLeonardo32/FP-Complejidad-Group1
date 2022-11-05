from nodo import Nodo
class Arista:
    def __init__(self,nodo1:Nodo,nodo2:Nodo) -> None:
        self.__par = [nodo1,nodo2]
    
    def es_dirigido(self) -> bool:
      return False
    
    def get_par(self) -> list:
      return self.__par
    
    def __str__(self) -> str:
      return f'Nodo: {self.get_par()[0]} -> Nodo: {self.get_par()[1]}'
    
class AristaNoDirigida(Arista):
  def __init__(self, nodo1: Nodo, nodo2: Nodo) -> None:
     super().__init__(nodo1, nodo2)
  
  def es_dirigido(self) -> bool:
     return False
  
  def get_nodo1(self) -> Nodo:
    return self.get_par()[0]
  
  def get_nodo2(self) -> Nodo: 
    return self.get_par()[1]

  def __str__(self) -> str:
     return super().__str__()



   
  