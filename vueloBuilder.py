from Vuelo import Vuelo
from abc import ABC
class VueloBuilder(ABC):
    @staticmethod
    def of_list(value: list()):
        travel_code,user_code,from_v,to_v,flight_type,price,time,distance,agency,date = value
        return Vuelo(int(travel_code),int(user_code),from_v,to_v,flight_type,float(price),time,float(distance),agency,date)
    
    
    