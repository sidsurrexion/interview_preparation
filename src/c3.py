import heapq

max_sum = 0


def find_square_root(number):
    return square_root_binary(number, int(number/2))


def square_root_binary(actual, number):
    first_middle = int(number/2)
    second_middle = number - first_middle
    if number < first_middle * first_middle < actual:
        square_root = first_middle
    else:
        square_root = square_root_binary(actual, first_middle)
    if number < second_middle * second_middle < actual:
        square_root = max(square_root, second_middle)
    else:
        square_root = max(square_root, square_root_binary(actual,
                                                          second_middle))
    return square_root


def string_matching_naive(text, pattern):
    for i in range(0, len(text) - len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            return i


def hash_formation(string):
    return sum([ord(i) for i in string])


def string_matching_ruban(text, pattern):
    if len(text) < len(pattern):
        return -1
    pattern_hash = hash_formation(pattern)
    text_hash = hash_formation(text[0:len(pattern)])
    if pattern_hash == text_hash and text[0:len(pattern)] == pattern:
        return 0
    for i in range(len(pattern), len(text)):
        text_hash -= ord(text[i-len(pattern)])
        text_hash += ord(text[i])
        if text_hash == pattern_hash and text[i-len(pattern):len(pattern)] \
                == pattern:
            return i-len(pattern)


def visit(list_string, string):
    return ''.join([string[i] for i in list_string if i != -1])


def naive_permute(list_string, string, index):
    if index == 0:
        print(visit(list_string, string))
    for k in range(len(list_string)):
        if list_string[k] == -1:
            list_string[k] = index - 1
            naive_permute(list_string, string, index - 1)
            list_string[k] = -1


def better_permute(list_string, string, index):
    if index == 0:
        print(visit(list_string, string))
    for k in range(index):
        list_string[k], list_string[index-1] = list_string[index-1], \
                                               list_string[k]
        better_permute(list_string, string, index - 1)
        list_string[k], list_string[index - 1] = list_string[index - 1], \
                                                 list_string[k]


def lc_subsequence_naive(first_string, second_string, first_length,
                         second_length):
    if first_length == 0 or second_length == 0:
        return 0
    if first_string[first_length - 1] == second_string[second_length - 1]:
        return lc_subsequence_naive(first_string, second_string,
                                    first_length - 1, second_length - 1)
    else:
        return max(lc_subsequence_naive(first_string, second_string,
                                        first_length - 1, second_length),
                   lc_subsequence_naive(first_string, second_string,
                                        first_length, second_length - 1))


def lc_subsequence_better(first_string, second_string):
    rows = len(first_string)
    col = len(second_string)
    l = [[0] * (col+1) for i in range(rows+1)]
    for i in range(rows):
        for j in range(col):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif l[i][j] == l[i-1][j-1]:
                l[i][j] = 1 + l[i-1][j-1]
            else:
                l[i][j] = max(l[i][j-1], l[i-1][j])
    return l[rows][col]


def lcs(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    l = [[0] * (n+1) for i in range(m)]
    result = 0
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif l[i][j] == l[i-1][j-1]:
                l[i][j] = 1 + l[i-1][j-1]
                result = max(result, l[i][j])
            else:
                l[i][j] = 0
    return result


def lis(seq):
    l = [1] * len(seq)
    for i in range(1, len(seq)):
        for j in range(i):
            if seq[i] < seq[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1
    maximum = 0
    for i in l:
        maximum = max(i, maximum)
    return maximum


def edit_distance(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    d = [[0] * (n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            elif d[i][j] == d[i-1][j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i-1][j], d[i][j-1], d[i-1][j-1])
    return d[m][n]


def max_single_profit(numbers):
    minimum = numbers[0]
    diff = 0
    for i in range(1, len(numbers)):
        if numbers[i] >= minimum:
            diff = max(diff, numbers[i] - minimum)
        else:
            minimum = numbers[i]
    return diff


def merge_lists(list_one, list_two):
    index_one = 0
    index_second = 0
    if len(list_one) == 0:
        return list_two
    if len(list_two) == 0:
        return list_one
    final_list = []
    while index_one < len(list_one) and index_second < len(list_two):
        if list_one[index_one] < list_two[index_second]:
            final_list.append(list_one[index_one])
            index_one += 1
        elif list_two[index_second] < list_one[index_one]:
            final_list.append(list_two[index_second])
            index_second += 1
        else:
            final_list.append(list_one[index_one])
            final_list.append(list_two[index_second])
            index_one += 1
            index_second += 1
    while index_one < len(list_one):
        final_list.append(list_one[index_one])
        index_one += 1
    while index_second < len(list_two):
        final_list.append(list_two[index_second])
        index_second += 1
    return final_list


def maximum_sum_subarray(numbers):
    max_current = numbers[0]
    max_global = numbers[0]
    for i in numbers:
        max_current = max(max_current, i + max_current)
        if max_current > max_global:
            max_global = max_current
    return max_global


class Edge(object):
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def get_other_end(self, vertex):
        if vertex == self.source:
            return self.destination
        return self.source


class Vertex(object):
    def __init__(self, name):
        self.seen = False
        self.parent = None
        self.name = name
        self.distance = -1
        self.neighbours = []


class Graph(object):
    def __init__(self, size):
        self.size = size
        self.vertex_holder = {}

    def add_vertex(self, name, value):
        if name not in self.vertex_holder:
            self.vertex_holder[name] = Vertex(value)
        return name

    def add_edge(self, source, destination, weight):
        edge = Edge(self.vertex_holder[source], self.vertex_holder[
            destination], weight)
        self.vertex_holder[source].neighbours.append(edge)
        self.vertex_holder[destination].neighbours.append(edge)


class Queue(object):
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        return self.heap[0]

    def is_empty(self):
        return bool(self.heap)


def dfs(graph):
    for vertex in graph.vertex_holder.values():
        if not vertex.seen:
            dfs_drill(vertex)


def bfs(graph):
    for vertex in graph.vertex_holder.values():
        if not vertex.seen:
            bfs_drill(vertex)


def bfs_drill(vertex):
    queue = Queue()
    queue.push(vertex)
    while not queue.is_empty():
        vertex = queue.pop()
        for edge in vertex.neighbours:
            source = edge.get_other_end(vertex)
            if not source.seen:
                source.parent = vertex
                queue.push(source)


def check_bipartite(source):
    queue = Queue()
    queue.push(source)
    while queue.is_empty():
        source = queue.pop()
        source.seen = True
        if source.distance == -1:
            source.distance = 1
        for edge in source.neighbours:
            vertex = edge.get_other_end(source)
            if not vertex.seen:
                if vertex.distance == 1:
                    source.distance = 2
                else:
                    source.distance = 1
            else:
                if vertex.distance == source.distance:
                    return False
            queue.push(vertex)
    return True


def dfs_drill(vertex):
    vertex.seen = True
    for neighbour in vertex.neighbours:
        destination = neighbour.get_other_end(vertex)
        if not destination.seen:
            destination.parent = vertex
            dfs_drill(destination)


class Tree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1

    def get_left_size(self):
        if self.left is None:
            return 0
        return self.left.get_left_size()

    def insert(self, data):
        if self.data <= data:
            if self.left is None:
                self.left = Tree(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Tree(data)
            else:
                self.right.insert(data)
        self.size += 1

    def find(self, data):
        if self.data == data:
            return self
        elif self.data < data:
            if self.left is None:
                return None
            return self.left.find(data)
        else:
            if self.right is None:
                return None
            return self.right.find(data)


def node_visit(node):
    return node.data


def inorder(node):
    while node is not None:
        inorder(node.left)
        node_visit(node)
        inorder(node.right)


def preorder(node):
    while node is not None:
        node_visit(node)
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    while node is not None:
        postorder(node.left)
        postorder(node.right)
        node_visit(node)


def minimal_bst(data, minimum, maximum):
    if minimum > maximum:
        return None
    middle = (minimum + maximum)/2
    node = Tree(data[middle])
    node.left = minimal_bst(data, minimum, middle - 1)
    node.right = minimal_bst(data, middle, maximum)
    return node


def get_height(node):
    if node is None:
        return -1
    return max(get_height(node.left), node.right) + 1


def validate_bst(node):
    if node is None:
        return True
    depth_diff = abs(get_height(node.left) - get_height(node.right))
    if depth_diff > 1:
        return False
    return validate_bst(node.left) and validate_bst(node.right)


def get_left_node(node):
    if node is None:
        return None
    if node.left is not None:
        return node.left
    return node


def get_inorder_node(node):
    if node is None:
        return None
    if node.right is not None:
        return get_left_node(node.right)
    parent = node.parent
    while parent is not None and node != parent.left:
        node = parent
        parent = node.parent
    return parent


def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1
    return depth


def get_shallow_node(depth, first, second):
    return second if depth > 0 else first


def get_deep_node(depth, first, second):
    return first if depth > 0 else second


def get_diff_node(depth, node):
    while depth > 0 or node is not None:
        node = node.parent
        depth -= 1
    return node


def get_common_ancestor(first, second):
    depth_diff = get_depth(first) - get_depth(second)
    first = get_shallow_node(depth_diff, first, second)
    second = get_deep_node(depth_diff, first, second)
    second = get_diff_node(depth_diff, second)
    while first is not None or second is not None or first != second:
        first = first.parent
        second = second.parent
    return None if first is None or second is None else first


def find_prime(number, is_prime):
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, number + 1):
        is_prime = True
    p = 2
    while p * p <= number:
        if is_prime[p]:
            for i in range(2*p, number+1, p):
                is_prime = False


def prime_sum(number):
    is_prime = []
    find_prime(number, is_prime)
    for i in range(number):
        if is_prime[i] and is_prime[number-i]:
            return i, number - i


def invert_tree(node):
    if node is None:
        return
    node.left, node.right = invert_tree(node.right), invert_tree(node.left)
    return node


def merge_trees(first, second):
    if first is None and second is None:
        return None
    if second is None:
        return first
    if first is None:
        return second
    node = Tree(first.data + second.data)
    node.left = merge_trees(first.left, second.left)
    node.right = merge_trees(first.right, second.right)
    return node


class TreeIterator(object):
    def __init__(self, node):
        self.last = node
        while self.last and self.last.right:
            self.last = self.last.right
        self.current = node
        self.iterator = self.iterate(node)

    def has_next(self):
        return self.current != self.last

    def next(self):
        return next(self.iterator)

    def iterate(self, node):
        if node is None:
            return None
        for tree in self.iterate(node.left):
            yield tree
        self.current = node
        yield self.current.data
        for tree in self.iterate(node.right):
            yield tree


def kth_smallest(node, count_l):
    if not node:
        return
    kth_smallest(node.left, count_l)
    count_l.append(node.data)
    kth_smallest(node.right, count_l)


def get_kth_smallest_element(node, k):
    if not node:
        return
    count = []
    kth_smallest(node, count)
    return count[k-1]


def calculate_max_sum(node):
    global max_sum
    max_path_sum(node, max_sum)
    return max_sum


def max_path_sum(node, maximum_sum):
    if not node:
        return
    left = max(0, max_path_sum(node.left, maximum_sum))
    right = max(0, max_path_sum(node.right, maximum_sum))
    maximum_sum = max(maximum_sum, left + right + node.data)
    return max(left, right) + node.data


def serialize(node, l_serialize):
    if not node:
        l_serialize.append("X,")
    l_serialize.append(node.data+",")
    serialize(node.left, l_serialize)
    serialize(node.right, l_serialize)


def deserialize(l_serialize):
    if l_serialize.popleft() == 'X':
        return
    node = Tree(l_serialize.popleft())
    node.left = deserialize(l_serialize)
    node.right = deserialize(l_serialize)
    return node


def is_symmetric(node_one, node_two):
    if node_one and node_two and node_one.left.data == node_two.right.data:
        return is_symmetric(node_one.left, node_two.right) and is_symmetric(
            node_one.right, node_two.left)
    return node_one == node_two


def remove_parenthesis(string, answer, previous_i, previous_j, chars):
    stack = 0
    for i in range(len(string)):
        if string[i] == '(':
            stack += 1
        else:
            stack -= 1
        if stack >= 0:
            continue
        for j in range(previous_j, i):
            if string[j] == ')' and (j == previous_j || string[j-1] !=
                                         chars[1]):
                remove_parenthesis(string[0:j-1] + string[j+1:len(string)],
                                   answer, i, j, chars)
    reverse_str = string[::-1]
    if chars[0] == '(':
        remove_parenthesis(reverse_str, answer, 0, 0, ('(', ')'))
    else:
        answer.append(reverse_str)
