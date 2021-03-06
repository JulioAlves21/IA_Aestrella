from calendar import c
import networkx as nx
import matplotlib.pyplot as plt

nodos = []
aristas = []

class Nodo():
    def __init__(self,nombre,c,h,f,p):
        self.nombre = nombre
        self.c = c
        self.f= f
        self.h = h
        self.p = p

def getNodo(nombre):
    for nodo in nodos:
        if nodo.nombre == nombre:
            nodo_enc = nodo
    return nodo_enc

class Arista():
    def __init__(self,inicial,final,costo):
        self.inicial = inicial
        self.final = final
        self.costo = costo

# https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.add_edge.html?highlight=add_edge#networkx.DiGraph.add_edge
# Note: The nodes u and v will be automatically added if they are not already in the graph.
def agregar_arista(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)

    # Si el grafo no es dirigido
    if not di:
        # Agrego otra arista en sentido contrario
        G.add_edge(v, u, weight=w)


if __name__ == '__main__':
    # Instantiate the DiGraph
    G = nx.DiGraph()

    # Add node/edge pairs
    """     agregar_arista(G, "A", "B", 5)
    agregar_arista(G, "A", "D", 4)
    agregar_arista(G, "A", "E", 2)
    agregar_arista(G, "B", "C", 1, False)
    agregar_arista(G, "B", "E")
    agregar_arista(G, "C", "D", 3, False)
    agregar_arista(G, "C", "F", 5)
    agregar_arista(G, "D", "E", 3)
    agregar_arista(G, "D", "F", 4)
    agregar_arista(G, "E", "F", 8) """
    
    print("Ingrese Valores de los Nodos \nCtrl + C PARA SALIR")
    cont = 1
    try:
        while True:
            nombre = input('Ingrese Nombre del Nodo ' + str(cont)+': ')
            h = input('Ingrese el valor de h ' + str(cont)+': ')
            cont += 1
            nodos.append(Nodo(nombre,None,h,None,None))
    except KeyboardInterrupt:
        pass
    
    print("Ingrese Valores de los Aristas \nCtrl + C PARA SALIR")
    try:
        while True:
            inicio = input('Ingrese Nodo Inicial arista ' + str(cont)+': ')
            fin = input('Ingrese Nodo Final arista ' + str(cont)+': ')
            costo = input('Ingrese costo del Nodo arista ' + str(cont)+': ')
            cont += 1
            agregar_arista(G, inicio, fin, costo)
            aristas.append(Arista(getNodo(inicio),fin,costo))
    except KeyboardInterrupt:
        pass
    for n in  nodos:
        print(n.nombre)
    for a in  aristas:
        print(a.inicial.nombre)
    

    # Draw the networks
    pos = nx.layout.planar_layout(G)
    nx.draw_networkx(G, pos)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("TRABAJO PRACTICO FINAL IA 1")
    plt.show()
