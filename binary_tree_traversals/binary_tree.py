# Implements a binary tree.
# CSC 202, Lab 6
# Given code, Summer '22

from stack import *
from queue import *

class BinaryTree:
    """
    A binary tree
    NOTE: Do not alter this class.
    """

    def __init__(self, value = None):
        if value is None:
            # The root of this empty tree:
            self.root = None
            # The number of nodes in this tree:
            self.size = 0
        else:
            # The root of this singleton tree:
            self.root = Node(value, None, None)
            # The number of nodes in this tree:
            self.size = 1

    def __eq__(self, other):
        return (type(other) == BinaryTree
                and self.root == other.root
                and self.size == other.size)

    def __repr__(self):
        return "BinaryTree(%r, %d)" % (self.root, self.size)


class Node:
    """
    A single node in a binary tree
    NOTE: Do not alter this class.
    """

    def __init__(self, value, left, right):
        # The value contained in this node:
        self.value = value
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right

    def __eq__(self, other):
        return (type(other) == Node
                and self.value == other.value
                and self.left == other.left
                and self.right == other.right)

    def __repr__(self):
        return "Node(%r, %r, %r)" % (self.value, self.left, self.right)


def size(tree):
    """
    Calculate the size of a binary tree.
    TODO: Implement this function. It must have O(1) complexity.

    :param tree: A BinaryTree
    :return: The number of nodes in the binary tree
    """
    return tree.size


def combine(value, left, right):
    """
    Combine two binary trees into one.
    TODO: Implement this function. It must have O(1) complexity.

    :param value: A value to add within a new root
    :param left: A BinaryTree to use as a left subtree
    :param right: A BinaryTree to use as a right subtree
    :return: A new BinaryTree combining the left, right, and value
    """
    tree = BinaryTree(value)
    tree.root.left = left.root
    tree.root.right = right.root
    tree.size = size(left) + size(right) + 1

    return tree

### For testing purposes ###

tree = combine(0,
                combine(1,
                 BinaryTree(3),
                 BinaryTree(4)),
                BinaryTree(2))

###

def _traverse(node, queue = None):

    if queue is None:
        queue = Queue()

    if node is None:
        return queue

    else:
        _traverse(node.left, queue)
        _traverse(node.right, queue)
        # print(node.value)
        enqueue(queue, node.value)

    return queue

def postorder(tree):
    """
    Traverse a binary tree in post-order.
    TODO: Implement this function. It must have O(n) complexity.

    :param tree: A BinaryTree
    :return: A new Queue containing the tree's values in post-order
    """
    return _traverse(tree.root)

    # postorder(tree)

    # queue = Queue()
    #
    # if tree.root is None:
    #     return queue
    #
    # stack = Stack()
    # push(stack, tree.root)
    #
    # while size(stack) > 0:
    #     node = peek(stack)
    #     print(node.value)
    #
    #     if node.left is not None:
    #         push(stack, node.left)
    #
    #     if node.right is not None:
    #         push(stack, node.right)
    #
    #     enqueue(queue, node.value)
    #     temp = pop(stack)
    #
    # return queue

postorder(tree)

def preorder(tree):
    """
    Traverse a binary tree in pre-order.
    TODO: Implement this function. It must have O(n) complexity.

    :param tree: A BinaryTree
    :return: A new Queue containing the tree's values in pre-order
    """
    queue = Queue()

    if tree.root is None:
        return queue

    stack = Stack()
    push(stack, tree.root)

    while size(stack) > 0:
        node = pop(stack)
        # print(node.value)
        enqueue(queue, node.value)

        if node.right is not None:
            push(stack, node.right)

        if node.left is not None:
            push(stack, node.left)

    return queue

# preorder(tree)

def levelorder(tree):
    """
    Traverse a binary tree in level-order.
    TODO: Implement this function. It must have O(n) complexity.

    :param tree: A BinaryTree
    :return: A new Queue containing the tree's values in level-order
    """
    queue = Queue()
    output = Queue()

    if tree.root is None:
        return queue

    enqueue(queue, tree.root)

    while size(queue) > 0:
        node = dequeue(queue)
        # print(node.value)
        enqueue(output, node.value)

        if node.left is not None:
            enqueue(queue, node.left)

        if node.right is not None:
            enqueue(queue, node.right)

    return output

# levelorder(tree)
