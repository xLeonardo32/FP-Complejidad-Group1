# Esta clase lo que hace es hacer toda la grafica del grafo
import vertice as vtc

class Grafica:
    def __init__(self):
        self.vertices = {} # Creando un diccionario
        
    def add_vertice(self,v):
        # Para agregar un vertice en el diccionario sera:
        # Clave : Valor del vertice
        # Valor : Objeto vertice 
        if not v in self.vertices:
           self.vertices[v] = vtc.Vertice(v)

    def add_arista(self,a,b):
    # a y b son los dos nodos o vertices
    # Primero debemos saber si a y b ya estan en nuestro diccionario
        if a in self.vertices and b in self.vertices:
            self.vertices[a].add_neighbour(b)
            self.vertices[b].add_neighbour(a)
    
    def show(self):
        for v in self.vertices:
            self.vertices[v].show_neighbours()
        
        
#Funcion main 
if __name__ == "__main__":
    g = Grafica()
    nodos = [1,2,3,4,5,6]
    
    #Creando los nos con la lista nodos
    for v in nodos:
        g.add_vertice(v)
    
    #Creando las aristas
    aristas = [4,5,6,3]
    
    for i in range(0,len(aristas),2):
        g.add_arista(aristas[i],aristas[i+1])
    
    g.show()
