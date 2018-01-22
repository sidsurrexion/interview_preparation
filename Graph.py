import sys
import heapq


class Queue(object):
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return not self.heap


class Stack(object):
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        p = self.data[-1]
        self.data = self.data[:-1]
        return p

    def peek(self):
        return self.data[-1]


class Vertex(object):
    def __init__(self, name):
        self.distance = -1
        self.parent = None
        self.adjacent_edges = []
        self.name = name
        self.seen = False
        self.cno = 0

    def get_distance(self):
        return self.distance


class Edge(object):
    def __init__(self, source, destination, weight):
        self.source = source
        self.weight = weight
        self.destination = destination

    def get_other_end(self, vertex):
        if self.source == vertex:
            return self.destination
        return self.source


class Graph(object):
    def __init__(self, number):
        self.size = number
        self.vertices = {}

    def add_edge(self, source, destination, weight):
        edge = Edge(self.vertices[source], self.vertices[destination], weight)
        self.vertices[source].adjacent_edges.append(edge)


def iterative_depth_first_search(graph):
    for vertex in graph.vertices.values():
        if not vertex.seen:
            depth_first_search(vertex)


def depth_first_search(vertex):
    vertex.seen = True
    for edge in vertex.adjacent_edges:
        destination = edge.get_other_end(vertex)
        if not destination.seen:
            destination.parent = vertex
            depth_first_search(destination)


def iterative_connected_components(graph):
    cno = 0
    for vertex in graph.vertices.values():
        if not vertex.seen:
            cno += 1
            connected_components(vertex, cno)


def connected_components(vertex, cno):
    vertex.seen = True
    vertex.cno = cno
    for edge in vertex.adjacent_edges:
        destination = edge.get_other_end(vertex)
        if not destination.seen:
            destination.parent = vertex
            connected_components(destination, cno)


def iterative_topological_sort(graph):
    stack = Stack()
    for vertex in graph.vertices.values():
        if not vertex.seen:
            topological_sort(vertex, stack)


def topological_sort(vertex, stack):
    vertex.seen = True
    for edge in vertex.adjacent_edges:
        destination = edge.get_other_end(vertex)
        if not destination.seen:
            destination.parent = vertex
            topological_sort(destination, stack)
    stack.push(vertex)


def breadth_first_search(graph):
    for vertex in graph.vertices.values():
        queue = Queue()
        if not vertex.seen:
            queue.push(vertex)
            while not queue.is_empty():
                vertex = queue.pop()
                vertex.seen = True
                for edge in vertex.adjacent_edges:
                    destination = edge.get_other_end(vertex)
                    if not destination.seen:
                        destination.parent = vertex
                        queue.push(destination)


def check_bipartite(graph):
    for vertex in graph.vertices.values():
        queue = Queue()
        queue.push(vertex)
        while not queue.is_empty():
            vertex = queue.pop()
            if vertex.distance == -1:
                vertex.distance = 1
            for edge in vertex.adjacent_edges:
                destination = edge.get_other_end(vertex)
                if destination.distance == vertex.distance:
                    return False
                if destination.distance == -1:
                    if vertex.distance == 1:
                        destination.distance = 2
                    else:
                        destination.distance = 1
                queue.push(destination)
    return True
