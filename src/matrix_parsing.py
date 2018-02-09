class Edge(object):
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def get_other_end(self, vertex):
        if self.source == vertex:
            return self.destination
        return self.source


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.seen = False
        self.neighbours = []


class Graph(object):
    def __init__(self, size):
        self.size = size
        self.vertex_mapper = {}

    def add_vertex(self, value, name):
        if name not in self.vertex_mapper:
            self.vertex_mapper[name] = Vertex(value)
        return name

    def add_edge(self, source, destination):
        edge = Edge(self.vertex_mapper[source], self.vertex_mapper[
            destination], 0)
        self.vertex_mapper[source].neighbours.append(edge)
        self.vertex_mapper[destination].neighbours.append(edge)


def has_value(matrix, row, column):
    try:
        return matrix[row][column], True
    except Exception as exception:
        str(exception)
        return -1, False


def update_graph(graph, row, column, matrix, current, curr_row, curr_col):
    value, flag = has_value(matrix, row, column)
    if flag:
        graph.add_vertex(current, int(str(curr_row) + str(curr_col)))
        graph.add_vertex(value, int(str(row) + str(column)))
        graph.add_edge(int(str(row) + str(column)),
                       int(str(curr_row) + str(curr_col)))


def matrix_parser(matrix):
    row = len(matrix)
    column = len(matrix[0])
    graph = Graph(row * column)
    for i in range(row):
        for j in range(column):
            update_graph(graph, i, j - 1, matrix, matrix[i][j], i, j)
            update_graph(graph, i, j + 1, matrix, matrix[i][j], i, j)
            update_graph(graph, i - 1, j, matrix, matrix[i][j], i, j)
            update_graph(graph, i + 1, j, matrix, matrix[i][j], i, j)
    return graph


def dfs(vertex, count):
    vertex.seen = True
    for edge in vertex.neighbours:
        other = edge.get_other_end(vertex)
        if not other.seen and other.name == 1:
            count += 1
            dfs(other, count)
    return count


mat = [[1, 1, 1, 1], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]
g = matrix_parser(mat)
print([dfs(vertex, 1) for vertex in g.vertex_mapper.values() if not
      vertex.seen and vertex.name == 1])
