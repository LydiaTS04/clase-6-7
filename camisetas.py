import networkx as nx
import matplotlib.pyplot as plt


ponderacion={"sostenible":5}

def calcular_peso(n1,n2):#que pseo tiene cada realcion
    peso=0 #comparar cuantos atributos coinciden
    for atributo in n1[1].items():
        #print(atributo)
        for atributo2 in n2[1].items():
            if atributo == atributo2:
                if atributo[0] in ponderacion:
                    peso += ponderacion[atributo[0]]
                else:
                    peso +=1

    return peso

G=nx.Graph()

categorias = {
    "Camisetas rojas": {"productos":"camisetas", "color":"rojo", "tipo":"casual", "material": "algodon", "sontenible":True},
    "Pantalones azules": {"productos": "pantalones", "color":"azul", "tipo":"oversize","material":"denium", "sostenible":False},
    "camiseta gris": {"productos": "camisetas", "color": "gris", "tipo": "casual", "material": "algodon", "sostenible": True},
    "Camiseta deporte": {"productos": "camisetas", "color":"gris", "tipo": "deporte", "material": "nylon", "sostenible": False}}

# **atributos desempaqueta automaticamente el diccionario y pasa sus elementos como argumentos de palabra clave a la funcion
for categorias, atributos in categorias.items(): #categorias es camiseta roja, pantalones axules, ... y atributos el calor, tipo...
    G.add_node(categorias, **atributos)#añado nodos

#añadir aristas entre nodos
for nodo in G.nodes.items():
    print(nodo)
    for nodo2 in G.nodes.items():
        if nodo2==nodo:
            pass #no hace nada, salta la linea
        else: #para calcualr el peso
            peso=calcular_peso(nodo,nodo2)
            print(f"Enlace de {nodo[0]} a {nodo2[0]} con peso {peso}")
            G.add_edge(nodo[0], nodo2[0], weight=peso)



# Dibuja el grafo
pos = nx.spring_layout(G)  # Posiciones para los nodos
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_color='black')

# Extraer los pesos de las aristas
weights = nx.get_edge_attributes(G, 'weight')

# Dibuja los pesos sobre las aristas
edge_labels = {(nodo1, nodo2): peso for (nodo1, nodo2), peso in weights.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
plt.title("Grafo de Categorías con Pesos en las Aristas")
plt.show()