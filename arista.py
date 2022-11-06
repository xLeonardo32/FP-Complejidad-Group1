from nodo import Nodo
class Arista:
    def __init__(self,nodo1:Nodo,nodo2:Nodo) -> None:
        self.__par = [nodo1,nodo2]
    
    def es_dirigido(self) -> bool:
      return False
    
    def get_par(self) -> list:
      return self.__par
    
    def get_nodo1(self) -> Nodo:
      return self.get_par()[0]
  
    def get_nodo2(self) -> Nodo: 
      return self.get_par()[1]

 
    def __eq__(self, __o: object) -> bool:
      if self.get_par()[0] == __o.get_par()[0] and self.get_par()[1] == __o.get_par()[1]:
        return True
      return False

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



   
  