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
    if graph['directed']:
        graph['directed'] = sc.new_map(size, 0.5)
    return graph

#funciones que ya están y funcionan
def num_edges(grafo):
    return grafo['edges']

def edges(grafo):
    lista_edges = lt.new_list()
    lista_de_listas = sc.value_set(grafo['vertices'])
    for lista in lista_de_listas['elements']:
        if grafo['directed']:
            #A a B es diferente B a A dirijido
                lt.add_list(lista_edges,lista)
        else:
            #"vertex_a": v_a, "vertex_b": v_b, "weight": weight
            #A a B es igual a B a A  
            for edgee in lista['elements']:
                if lt.size(lista_edges) < 1:
                    lt.add_last(lista_edges, edgee)
                else:
                    for edgee_2 in lista_edges['elements']:   
                        if edge.compare_edges_no_dirigido(edgee, edgee_2) != 0:
                            lt.add_last(lista_edges, edgee)        
    return lista_edges

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

def vertices(grafo):
    return sc.key_set(grafo['vertices'])

def contains_vertex(graph, vertex):
    return sc.get(graph['vertices'], vertex)

def get_edge(graph, vertex_a, vertex_b):
    lista_arco = sc.get(graph['vertices'],vertex_a)
    for arco in lista_arco['elements']:
        if edge.other(arco,vertex_a) == vertex_b:
            return arco

# Funciones por hacer - agregar!

def add_edge(graph, vertex_a, vertex_b, weight=0):
    arco_1 = edge.new_edge(vertex_a, vertex_b, weight)
    verticees = sc.get(graph["vertices"], vertex_a)
    if verticees == None:
        verticees = lt.new_list()
        sc.put(graph['vertices'],vertex_a,verticees)
    lt.add_last(verticees, arco_1)
    if graph["directed"] != False: #es decir, si es verdadero o existe el mapa
        in_degree = sc.get(graph["in_degree"], vertex_b)
        if in_degree == None:
            in_degree = lt.new_list()
            sc.put(graph['in_degree'],vertex_b, in_degree)
        lt.add_last(in_degree, arco_1)
    else:
        arco_2 = edge.new_edge(vertex_b, vertex_a, weight)
        verticees = sc.get(graph["vertices"], vertex_b)
        if verticees == None:
            verticees = lt.new_list()
            sc.put(graph['vertices'],vertex_b,verticees)
        lt.add_last(verticees, arco_2)
        #duda de esto
    graph['edges'] += 1
    return graph

def insert_vertex(graph, key_vertex, info_vertex):
    mapa_vertices_info = graph['information']
    sc.put(mapa_vertices_info, key_vertex, info_vertex)
    mapa_vertices_arcos = graph['vertices']
    lista_arco = lt.new_list()
    sc.put(mapa_vertices_arcos,key_vertex, lista_arco)
    if graph['directed'] != False:
        mapa_in_degree = graph['in_degree']
        lista_in_degree = lt.new_list()
        sc.put(mapa_in_degree,key_vertex,lista_in_degree)
    return graph



