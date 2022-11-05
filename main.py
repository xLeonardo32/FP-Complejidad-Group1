from nodo import Nodo
from Vuelo import Vuelo
from arista import Arista
from grafo import Grafo

if __name__ == '__main__':
    nodo1 = Nodo(Vuelo(0,0,'Recife (PE)','Florianopolis (SC)','firstClass',1434.38,1.76,676.53,'FlyingDrops','09/26/2019'))
    nodo2 = Nodo(Vuelo(0,0,'Florianopolis (SC)','Recife (PE)','firstClass',1292.29,1.76,676.53,'FlyingDrops','09/30/2019'))
    
    
    arista1 = Arista(nodo1,nodo2)
    arista2 = Arista(nodo1,nodo2)
    print(arista1)
    g = Grafo()
    g.agregar_arista(arista1)
    g.agregar_arista(arista2)
       
    
   # print(nodo1.dato) 
    