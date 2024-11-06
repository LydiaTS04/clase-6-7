import networkx as nx

# """ para comentar varias lienas """

grafo=nx.Graph()
grafo.add_node(1)#añadir nodo, añadir varios add_nodes_from()
grafo.add_edge(1,2)#crear arista

#definir atributos al nodo o arista (si se quita no pasa nada)
grafo.add_node(1,time="5pm")
grafo.add_edge(1,2,weight=4.7)

#fabricar
import matplotlib.pyplot as plt
nx.draw(grafo,with_labels=True)
plt.show()


