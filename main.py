from nodo import Nodo
from Vuelo import Vuelo
from arista import Arista
from grafo import Grafo
from programControler import ProgramControler
if __name__ == '__main__':
    """
    nodo1 = Nodo(Vuelo(0,0,'Recife (PE)','Florianopolis (SC)','firstClass',1434.38,1.76,676.53,'FlyingDrops','09/26/2019'))
    nodo2 = Nodo(Vuelo(0,0,'Florianopolis (SC)','Recife (PE)','firstClass',1292.29,1.76,676.53,'FlyingDrops','09/30/2019'))
    
    nodo3 = Nodo(Vuelo(1,0,'Brasilia (DF)','Florianopolis(SC)','firstClass',1487.52,1.66,637.56,'CloudFy','10/03/2019'))
    nodo4 = Nodo(Vuelo(1,0,'Florianopolis (SC)','Brasilia (DF)','firstClass',1127.36,1.66,637.56,'CloudFy','10/04/2019'))
    
    arista1 = Arista(nodo1,nodo2)
    arista2 = Arista(nodo3,nodo4)
    arista3 = Arista(nodo1,nodo4)
    #print(arista1)
    g = Grafo()
    g.agregar_arista(arista1)
    g.agregar_arista(arista2)
    g.agregar_arista(arista3)
    g.get_list_ady()
    
    g.print_list_ady()
    """   
    program = ProgramControler("VuelosDatos.csv")
    program.g.print_list_ady()
    #print(program.g.aristas)
    #Mejorar las impresiones de la lista de adyacencia
   # print(nodo1.dato) 
    