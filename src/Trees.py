import random
import sys


class Node(object):
    def __init__(self, data):
        self.data = data
        self.size = 1
        self.left = None
        self.right = None

    def get_size(self):
        return self.size

    def get_left_size(self):
        if self.left is None:
            return 0
        return self.left.get_size()

    def get_data(self):
        return self.data

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        self.size += 1

    def find(self, data):
        if data == self.data:
            return self
        elif data < self.data:
            if self.left is None:
                return None
            else:
                return self.left.find(data)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(data)

    def get_random_node(self):
        if self.size == 1:
            return self
        size = random.randint(1, self.size)
        left_size = self.get_left_size()
        if size < left_size:
            return self.left.get_random_node()
        elif size == left_size:
            return self.left
        else:
            return self.right.get_random_node()


# Tree traversals
def visit(node):
    return node.data


def in_order_traversal(node):
    while node is not None:
        in_order_traversal(node.left)
        visit(node)
        in_order_traversal(node.right)


def pre_order_traversal(node):
    while node is not None:
        visit(node)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node):
    while node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        visit(node)
# Ends

# Minimal length for BST


def create_minimal_bst(data):
    return minimal_bst(data, 0, len(data) - 1)


def minimal_bst(data, minimum, maximum):
    if maximum < minimum:
        return None
    middle = (maximum + minimum) / 2
    node = Node(data[middle])
    node.left = minimal_bst(data, minimum, middle - 1)
    node.right = minimal_bst(data, middle + 1, maximum)
    return node
# Ends

# Validate balanced BST -> O(N log N)


def get_height(node):
    if node is None:
        return -1
    return max(get_height(node.left), get_height(node.right)) + 1


def validate_balanced_bst(node):
    if node is None:
        return True
    depth = abs(get_height(node.left) - get_height(node.right))
    if depth > 1:
        return False
    else:
        return validate_balanced_bst(node.left) and validate_balanced_bst(
            node.right)
# Ends


# Validate balanced BST (Alternate Version) -> O(N log N)


def balanced_bst(node):
    return check_balanced_alternate(node) != sys.maxsize * -1


def check_balanced_alternate(node):
    if node is None:
        return -1

    left_depth = check_balanced_alternate(node.left)
    if left_depth == sys.maxsize * -1:
        return sys.maxsize * -1

    right_depth = check_balanced_alternate(node.right)
    if right_depth == sys.maxsize * -1:
        return sys.maxsize * -1

    if abs(left_depth - right_depth) > 1:
        return sys.maxsize * -1
    return abs(left_depth - right_depth) + 1
# Ends

# In order successor


def get_left_node(node):
    if node is None:
        return None
    if node.left is not None:
        return node.left
    return node


def in_order_successor(node):
    if node is None:
        return None
    if node.right is not None:
        return get_left_node(node.right)
    parent = node.parent
    while parent is not None and parent.left != node:
        node = parent
        parent = node.parent
    return parent
# Ends


# Validate BST

def check_bst(node):
    return validate_bst(node, None, None)


def validate_bst(node, minimum, maximum):
    if node is None:
        return True
    if (minimum is not None and minimum >= node.data) or (
                    maximum is not None and node.data > maximum):
        return False
    if (not validate_bst(node.left, minimum, node.data)) or (not
                                                             validate_bst(
                                                                 node.right,
                                                                 node.data,
                                                                 maximum)):
        return False
    return True
# Ends

# Least common ancestor


def get_common_ancestor(first, second):
    depth_diff = get_depth(first) - get_depth(second)
    first_node = get_shallow_node(depth_diff, first, second)
    second_node = get_deep_node(depth_diff, first, second)
    second_node = get_diff_node(depth_diff, second_node)
    while first_node is not None or second_node is not None or first_node !=\
            second_node:
        first_node = first_node.parent
        second_node = second_node.parent
    return None if first_node is None or second_node is None else first_node


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
    if node is None:
        return None
    while depth > 0 and node is not None:
        node = node.parent
        depth -= 1
    return node
# Ends
