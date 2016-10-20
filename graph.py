""" A Python class 
A simple Python graph class, demostrating the essential facts 
and functionalities of graphs.
"""

class Graph(object):
    def __init__(self, graph_dict = None):
        """initializes a graph object
            If no dictionary or Noe is given,
            and empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict =graph_dict
        
    def vertices(self):
        """ return the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ return the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ if the vertex "vertex" is not in 
            self.__graph_dict, a key "vertex" with 
            an empty list as value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
            
    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list,
            between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1]= [vertex2]