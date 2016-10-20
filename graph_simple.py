#Grahp theory... kurngnisberg 7 briges

#A dictionary to store node and edges of a graph
"""The keys of the dictionary are the nodes of our graph.the 
the corresponding values are the lists with the node, which
are connecting by an edge
"""
graph = {"a": ["c"],
        "b": ["c", "e"],
        "c": ["a","b","d","e"],
        "d": ["c"],
        "e": ["c", "b"],
        "f": []
    }
    
def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))
    return edges
print(generate_edges(graph))


def find_isolated_nodes(graph):
    """return a list of isolated nodes."""
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated;

print (find_isolated_nodes(graph))