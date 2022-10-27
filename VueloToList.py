from ReadDataSet import IReadCsv
from Vuelo import Vuelo

class VueloToList(IReadCsv):
    def __init__(self) -> None:
        self.lista = []
    
    def object_instance(self,it:int,datos: list) -> None:
        if it % 2 == 0:
            code = datos[0] + 'i' #Se acoplara la fecha, crear una clase fecha 
        else:
            code = datos[0] + 'v'

        t_from = datos[2] #Mejorar en una clase aparte
        t_to = datos[3]
        flight_type = datos[4]
        price = datos[5]
        time = datos[6]
        distance = datos[7]
        agency = datos[8]
        date = datos[9]
        self.lista.append(Vuelo(code,t_from,t_to,flight_type,price,time,distance,agency,date))

    def read(self,file: str) -> list:
        try :
            archivo = open(file)
            lineas = archivo.readlines()

            it = 0
            for linea in lineas:
                aux = linea.replace('\n','')
                if len(aux.split(',')) == 10: #Mejorar el if
                    self.object_instance(it,aux)
                else:
                    continue
                it = it + 1
        except FileNotFoundError:
            print('No se encontro el archivo')
        
        finally:
            archivo.close()
    
    def get_result(self) -> list:
        return self.lista




