# Implements a simple, undirected, unweighted graph.
# CSC 202, Lab 10
# Given code, Summer '24

import queue as que
import array_list as lst
import dictionary as dct
from dictionary import Dictionary


class Graph:
    """ A collection of vertices and edges """

    def __init__(self):
        # The backing adjacency matrix:
        self.matrix = dct.Dictionary()
        # The number of edges in this graph:
        self.size = 0

    def __eq__(self, other):
        return (type(other) == Graph
                and self.matrix == other.matrix
                and self.size == other.size)

    def __repr__(self):
        return "Graph(%r, %d)" % (self.matrix, self.size)


def order(graph):
    """
    Calculate the order of a graph.
    TODO: Implement this function. It must have O(1) complexity.

    :param graph: A Graph
    :return: The number of vertices in the graph
    """

    return graph.matrix.size


def size(graph):
    """
    Calculate the size of a graph.
    TODO: Implement this function. It must have O(1) complexity.

    :param graph: A Graph
    :return: The number of edges in the graph
    """
    return graph.size


def add_vertex(graph, vertex):
    """
    Add a vertex to a graph.
    TODO: Implement this function. It must have O(1) complexity.

    :param graph: A Graph
    :param vertex: An identifier of a vertex to be added
    :raise KeyError: If the vertex is already in the graph
    """
    if dct.get(graph.matrix, vertex) is not None: # If the vertex is already in the graph
        raise KeyError("The vertex is already in the graph.") # Raise a KeyError

    new_dct = dct.Dictionary() # Create a new empty dictionary
    dct.insert(graph.matrix, vertex, new_dct) # Insert the given vertex into the matrix, mapped to that dictionary


def add_edge(graph, vertex_u, vertex_v):
    """
    Add an edge, if one does not exist, to connect two vertices in a graph.
    TODO: Implement this function. It must have O(1) complexity.

    :param graph: A Graph
    :param vertex_u: An identifier of a vertex to be connected
    :param vertex_v: An identifier of a vertex to be connected
    :raise KeyError: If either vertex is not in the graph
    """
    if dct.get(graph.matrix, vertex_u) is None or dct.get(graph.matrix, vertex_v) is None: # If either vertex is not in the graph:
        raise KeyError("At least one vertex is not in the graph.") # Raise a KeyError

    dct_u = dct.get(graph.matrix, vertex_u) # Get vertex_u's dictionary from the matrix

    if dct.get(dct_u, vertex_v) is None:
        dct.insert(dct_u, vertex_v, 1) # Insert vertex_v into vertex_u's dictionary, mapped to 1

        dct_v = dct.get(graph.matrix, vertex_v) # Get vertex_v's dictionary from the matrix
        dct.insert(dct_v, vertex_u, 1) # Insert vertex_u into vertex_v's dictionary, mapped to 1

        graph.size += 1 # Increment the size of the graph

def remove_vertex(graph, vertex):
    """
    Remove a vertex from a graph.
    TODO: Implement this function. It may have up to O(n) complexity.

    :param graph: A Graph
    :param vertex: An identifier of a vertex to be removed
    :raise KeyError: If the vertex is not in the graph
    """
    if dct.get(graph.matrix, vertex) is None: # If the vertex is not in the graph:
        raise KeyError("The vertex is not in the graph.") # Raise a KeyError

    vertex_dct = dct.get(graph.matrix, vertex) # Get the given vertex's dictionary from the matrix
    neighbors = dct.keys(vertex_dct) # Get the neighbors of the given vertex

    for i in range(lst.size(neighbors)):
        neighbor = lst.get(neighbors, i) # Get the vertex's i'th neighbor
        remove_edge(graph, vertex, neighbor) # Remove the edge between the vertex and the i'th element

    dct.remove(graph.matrix, vertex) # Remove the given vertex from the matrix


def remove_edge(graph, vertex_u, vertex_v):
    """
    Remove an edge, if one exists, to disconnect two vertices in a graph.
    TODO: Implement this function. It must have O(1) complexity.

    :param graph: A Graph
    :param vertex_u: An identifier of a vertex to be connected
    :param vertex_v: An identifier of a vertex to be connected
    :raise KeyError: If either vertex is not in the graph
    """
    if dct.get(graph.matrix, vertex_u) is None or dct.get(graph.matrix, vertex_v) is None: # If either vertex is not in the graph:
        raise KeyError("At least one vertex is not in the graph.") # Raise a KeyError

    dct_u = dct.get(graph.matrix, vertex_u) # Get vertex_u's dictionary from the matrix

    if dct.get(dct_u, vertex_v) is not None:
        dct.remove(dct_u, vertex_v) # Remove vertex_v from vertex_u's dictionary

        dct_v = dct.get(graph.matrix, vertex_v) # Get vertex_v's dictionary from the matrix
        dct.remove(dct_v, vertex_u) # Remove vertex_u from vertex_v's dictionary

        graph.size -= 1 # Decrement the size of the graph

def path(graph, vertex_u, vertex_v):
    """
    Find the shortest path between two vertices.
    TODO: Implement this function. It may have up to O(n^2) complexity.

    :param graph: A Graph
    :param vertex_u: An identifier of a vertex at which to start
    :param vertex_v: An identifier of a vertex at which to end
    :return: A new List of vertices forming a path between the vertices
    :raise KeyError: If either vertex is not in the graph
    :raise ValueError: If there is no path between the vertices in the graph
    """
    if dct.get(graph.matrix, vertex_u) is None or dct.get(graph.matrix, vertex_v) is None: # If either vertex is not in the graph:
        raise KeyError("At least one vertex is not in the graph.") # Raise a KeyError

    vertices = que.Queue() # Create a new, empty queue (of vertices to be explored)
    que.enqueue(vertices, vertex_u) # Enqueue vertex_u

    pred = dct.Dictionary() # Create a new, empty dictionary (of predecessors along the path)
    dct.insert(pred, vertex_u, vertex_u) # Insert vertex_u into the predecessor's dictionary, mapped to itself

    while que.size(vertices) > 0:
        vertex = que.dequeue(vertices) # Dequeue a current vertex from the queue
        vertex_dct = dct.get(graph.matrix, vertex) # Get the current vertex's dictionary from the matrix
        neighbors = dct.keys(vertex_dct)  # Get the neighbors of the given vertex

        if vertex == vertex_v:
            path = lst.List()

            while vertex != vertex_u:
                lst.add(path, 0, vertex) # Insert the current vertex in the path
                vertex = dct.get(pred, vertex) # Shift to the current vertex's predecessor

            lst.add(path, 0, vertex_u)
            return path


        for i in range(lst.size(neighbors)):
            neighbor = lst.get(neighbors, i) # Get the current i'th neighbor

            if dct.get(pred, neighbor) is None: # If the i'th element is not in the predecessor's dictionary:
                que.enqueue(vertices, neighbor) # Enqueue the i'th element in vertices
                dct.insert(pred, neighbor, vertex) # Insert the i'th element into the predecessor's dictionary

    raise ValueError("There is no path between the vertices in the graph.") # Can only reach this line if the queue is empty and never found vertex_v
