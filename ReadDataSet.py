from abc import ABC, abstractmethod

class IReadCsv(ABC) :
    @abstractmethod
    def read(file : str) -> list:
        pass
    
    @abstractmethod
    def object_instance(datos : list) -> None:
        pass
    
    @abstractmethod
    def get_result()->list:
        pass
        

    