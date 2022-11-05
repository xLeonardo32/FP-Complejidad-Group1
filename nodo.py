class Nodo:
   def __init__(self,element) -> None:
      self.__dato = element
   
   @property
   def dato(self):
      return self.__dato

   def __str__(self) -> str:
      return str(self.__dato)
   

   
   