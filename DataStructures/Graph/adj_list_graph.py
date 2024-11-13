from DataStructures.Map import map_separate_chaining as sc

def new_graph(size=19, directed=False):
    
    graph = {"vertices": sc.new_map(size, 0.5),
             "infromation": sc.new_map(size, 0.5),
             "in_degree": None,
             "edges": 0,
             "directed": directed,
             "type": "ADJ_LIST"}
    
    return graph