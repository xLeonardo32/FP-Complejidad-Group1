class Nodo:
   def __init__(self,element = None) -> None:
      self.__dato = element
   
   @property
   def dato(self):
      return self.__dato
   def __eq__(self, __o: object) -> bool:
      if self.__dato == __o.dato:
         return True
      return False
   
   def __str__(self) -> str:
      return str(self.__dato)
   
   def __hash__(self) -> int:
      return hash(self.dato)

   
   