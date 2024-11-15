from DataStructures.List import array_list as lt
from DataStructures.Map import map_separate_chaining as sc
from DataStructures.Graph import edge

def new_graph(size=19, directed=False):
    
    graph = {"vertices": sc.new_map(size, 0.5), #llave son los vertices y el valor los arcos
             "information": sc.new_map(size, 0.5), #llave son los vertice y el información del vertice
             "in_degree": None, #solo se inicia en caso de ser un grafo dirigido
             "edges": 0, #iniciadon en 15
             "directed": directed, #de acuerdo a lo dado en parametro
             "type": "ADJ_LIST"}
    
    return graph

# Funciones por hacer

"""
def add_edge(graph, vertex_a vertex_b, weight):
    arco = edge.new_edge(vertex_a, vertex_b, weight)
	adyacentes = th.get(graph["adyacentes"], vertex_a)
	lt.add_last(adyacentes, arco)
 
	if graph["directed"]
		in_degree = th.get(graph["in_degree"], vertex_b)
		lt.add_last(graph["in_degree"], vertex_a)
	else:
		arco_2 = edge.new_edge(vertex_b, vertex_a. weight)
		adyacentes_2 = th.get(graph["adyacentes"], vertex_b)
    return graph
"""

def num_edges(grafo):
    return grafo['edges']

def edges(grafo):
    #lst = sc.value_set(grafo['vertices'])
    #en teoria cómo es una lista dentro de una lista, toca revisar bien
    return sc.value_set(grafo['vertices'])

def num_vertices(grafo):
    return sc.size(grafo['vertices'])

def degree(grafo, vertice):
    elemento = sc.get(grafo['vertices'], vertice)
    if elemento == None:
        return None
    else:
        return (lt.size(elemento))
    

def in_degree(grafo, vertice):
    if (grafo['directed']):
        grado = sc.get(grafo['in_degree'], vertice)
        return grado['value']
    else:
        return degree(grafo, vertice)