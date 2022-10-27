#El vertice en grafos tambien es conocido como el nodo
class Vertice:
    def __init__(self,i):
        # i -> Es el valor que tiene cada vertice
        self.id = i 
        # visitado -> Para saber si el nodo o vertice ya fue visitado o no 
        self.visitado = False
        # nivel -> Se utilizara para algunos algoritmos
        self.nivel = -1
        # neighbour -> Lista que esta conformada por vertices que estan realicioanadas a esta por una arista
        self.neighbour = []
        
    def add_neighbour(self, v):
        # v -> El vecino nuevo que vamos agregar a la lista de vecinos
        if not v in self.neighbour:# Primero debemos verificar si el nuevo vertice no esta en la lista de vecinos
           self.neighbour.append(v)# Agregando al vecino nuevo
    
    def show_neighbours(self):
        print(self.id,self.neighbour)
        
