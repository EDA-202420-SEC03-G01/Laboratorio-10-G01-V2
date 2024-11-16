from DataStructures.Map import map_separate_chaining as sc
from DataStructures.List import array_list as al
from DataStructures.Graph import edge as edge

def new_graph(size=19, directed=False):
    
    graph = {"vertices": sc.new_map(size, 0.5),
             "infromation": sc.new_map(size, 0.5),
             "in_degree": None,
             "edges": 0,
             "directed": directed,
             "type": "ADJ_LIST"}
    
    if directed:
        graph["in_degree"] = sc.new_map(size, 0.5)
    
    return graph

def insert_vertex (my_graph, key_vertex, info_vertex):
    
    sc.put(my_graph["information"], key_vertex, info_vertex)
    
def add_edge (my_graph, vertex_a, vertex_b, weight=0):
    
    lista_arcos_adjacentes_a = sc.get(my_graph["vertices"], vertex_a)
    lista_arcos_in_degree_b = sc.get(my_graph["in_degree"], vertex_b)
    
    for arco in lista_arcos_adjacentes_a:
        if al.get_element(lista_arcos_in_degree_b, arco) != None:
            arco_entre_a_y_b = arco
            arco_entre_a_y_b_presente = True
        else:
            arco_entre_a_y_b_presente = False
            
    
    if sc.contains(my_graph["information"], vertex_a) == False or sc.contains(my_graph["information"], vertex_b) == False:
        return my_graph
    
    elif (sc.contains(my_graph["information"], vertex_a) == True) and sc.contains(my_graph["information"], vertex_b) == True and arco_entre_a_y_b_presente == True:
        
        arco_entre_a_y_b["weight"] = weight
    
    else:
        nuevo_arco = edge.new_edge(vertex_a, vertex_b, weight)
        adyacentes = sc.get(my_graph["vertices"], vertex_a)
        al.add_last(adyacentes, nuevo_arco)
        
        if my_graph["directed"]:
         in_degree = sc.get(my_graph["in_degree"], vertex_b)
         al.add_last(in_degree, vertex_a)
         
        else:
            
         adyacentes_2 = sc.get(my_graph["adyacentes"], vertex_b)
         nuevo_arco_2 = edge.new_edge(vertex_b, vertex_a. weight)
         al.add_last(adyacentes_2, nuevo_arco_2)
            
    return my_graph