class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.distance = -1
        self.parent = None
        self.seen = False
        self.adjacency_list = []
        self.reverse_adjacency_list = []


class Edge(object):
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def get_other_end(self, vertex):
        if vertex == self.source:
            return self.destination
        return self.source


class Graph(object):
    def __init__(self, size):
        self.size = size
        self.vertices = {}

    def add_vertex(self, vertex_name):
        self.vertices[vertex_name] = Vertex(vertex_name)

    def add_directed_edge(self, source, destination, weight):
        edge = Edge(source, destination, weight)
        self.vertices[source].adjacency_list.append(edge)
        self.vertices[destination].reverse_adjacency_list.append(edge)


def depth_first_search(vertex):
    vertex.seen = True
    for edge in vertex.adjacency_list:
        target = edge.get_other_end(vertex)
        if target.seen:
            return True
        depth_first_search(target)
    return False


def is_graph_cyclic(graph):
    for vertex in graph.vertices.items():
        if not vertex.seen:
            if depth_first_search(vertex):
                return True
    return False


def has_route(source, destination):
    source.seen = True
    for edge in source.adjacency_list:
        child = edge.get_other_end(source)
        if not child.seen:
            if child == destination:
                return True
            has_route(child, destination)
    return False
