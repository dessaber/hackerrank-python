import sys


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def check_bst(root, min_value, max_value):
    if root is None:
        return True

    return min_value < root.data < max_value and \
        check_bst(root.left, min_value, root.data) and \
        check_bst(root.right, root.data, max_value)


if __name__ == "__main__":
    root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
    print(check_bst(root, -sys.maxsize, sys.maxsize))
