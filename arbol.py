import networkx as nx
import matplotlib.pyplot as plt



grafo1=nx.Graph()
grafo1.add_edge(1,2)#crear arista de 2 en 2
grafo1.add_edge(2,3)
grafo1.add_edge(3,1)

grafo2=nx.Graph()
grafo2.add_edge(4,5)#crear arista
grafo2.add_edge(5,6)
grafo2.add_edge(6,7)
grafo2.add_edge(7,5)

grafo3=nx.Graph()
grafo3.add_edges_from([(1,2),(2,3),(3,1),(5,6)])


if nx.is_connected(grafo1):
    print("el grafo 1 es conexo") #conexo = estan todos los nodos unidos
    if grafo1.number_of_edges()==(grafo1.number_of_nodes()-1):
        print("es un arbol")
    else:
        print("no es un arbol")
else:
    print("el grafo 1 no es conexo")#si no es conexo no es un arbol 


if nx.is_connected(grafo2):
    print("el grafo 2 es conexo") #conexo = estan todos los nodos unidos
    if grafo2.number_of_edges()==(grafo2.number_of_nodes()-1):
        print("es un arbol")
    else:
        print("no es un arbol")
else:
    print("el grafo 2 no es conexo")


if nx.is_connected(grafo3):
    print("el grafo 3 es conexo") #conexo = estan todos los nodos unidos
    if grafo3.number_of_edges()==(grafo3.number_of_nodes()-1):
        print("es un arbol")
    else:
        print("no es un arbol")
else:
    print("el grafo 3 no es conexo")

    
#fabricar
nx.draw(grafo1,with_labels=True)
plt.show()

nx.draw(grafo2,with_labels=True)
plt.show()

nx.draw(grafo3,with_labels=True)
plt.show()

print()

#otra manera
def arbol (graph):
    return nx.is_connected(graph) and graph.number_of_edges()==graph.number_of_nodes()-1

G1=nx.Graph()
G1.add_edges_from([(1,2),(1,3),(1,4),(1,5),(1,6)])

print(f"G1 es un arbol: {arbol(G1)}")

G2=nx.Graph()
G2.add_edges_from([(1,2),(1,3),(2,3),(1,4),(1,5),(1,6)])

print(f"G2 es un arbol: {arbol(G2)}")

#fabricar
nx.draw(G1,with_labels=True)
plt.show()

nx.draw(G2,with_labels=True)
plt.show()
