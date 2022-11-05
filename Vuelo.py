class Vuelo :
    def __init__(self,travel_code,user_code,t_from,t_to,flight_type,price,time,distance,agency,date):
        self.travel_code = travel_code
        self.user_code = user_code
        self.t_from = t_from
        self.t_to  = t_to
        self.flight_type = flight_type
        self.price = price
        self.time = time
        self.distance = distance
        self.agency = agency
        self.date = date
    
    def __str__(self) -> str:
        return 'Desde : ' + str(self.t_from) + '\n' + \
                'Hacia: ' + str(self.t_to) + '\n' + \
                'Tipo de vuelo: ' + str(self.flight_type) + '\n' + \
                'Precio: ' + str(self.price) + '\n' + \
                'Tiempo: ' + str(self.time)+ '\n' + \
                'Distancia: ' + str(self.distance) + '\n' + \
                'Agencia: ' + str(self.distance) + '\n' + \
                'Fecha: ' + str(self.date)

    