# Implements a binary search tree.
# CSC 202, Lab 7
# Given code, Summer '19

# TODO: Import stack if necessary.
# import stack
from queue import *


class BinarySearchTree:
    """
    A binary search tree
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The root of this tree:
        self.root = None
        # The number of nodes in this tree:
        self.size = 0

    def __eq__(self, other):
        return (type(other) == BinarySearchTree
                and self.root == other.root
                and self.size == other.size)

    def __repr__(self):
        return "BinarySearchTree(%r, %d)" % (self.root, self.size)


class Node:
    """
    A single node in a binary search tree
    NOTE: Do not alter this class.
    """

    def __init__(self, key, value, left, right):
        # The key contained in this node:
        self.key = key
        # The value associated with the key:
        self.value = value
        # The left child of this node:
        self.left = left
        # The right child of this node:
        self.right = right

    def __eq__(self, other):
        return (type(other) == Node
                and self.value == other.value
                and self.key == other.key
                and self.left == other.left
                and self.right == other.right)

    def __repr__(self):
        return "Node(%r, %r, %r, %r)"\
               % (self.key, self.value, self.left, self.right)


def size(bst):
    """
    Calculate the size of a BST.
    TODO: Implement this function. It must have O(1) complexity.

    :param bst: A BinarySearchTree
    :return: The number of nodes in the BST
    """
    return bst.size

def _find(node, key):

    if node is None:
        return None

    elif key == node.key:
        return node

    elif key < node.key:
        return _find(node.left, key)

    else:
        return _find(node.right, key)


def find(bst, key):
    """
    Find the value associated with a key.
    TODO: Implement this function. It must have O(log n) complexity.

    :param bst: A BinarySearchTree
    :param key: A comparable key to be found
    :return: The value associated with the key
    :raise KeyError: If the key is not in the BST
    """
    result = _find(bst.root, key)

    if result is None:
        raise KeyError("The key is not in the BST.")

    else:
        return result.value

def _insert(bst, node, key, value = None):
    if node is None:
        new_node = Node(key, value, None, None)
        bst.size += 1
        return new_node

    elif key == node.key:
        node.value = value
        return node

    elif key < node.key:
        node.left = _insert(bst, node.left, key, value)
        return node

    else:
        node.right = _insert(bst, node.right, key, value)
        return node

def insert(bst, key, value):
    """
    Insert a key, overwriting any existing associated value.
    TODO: Implement this function. It must have O(log n) complexity.

    :param bst: A BinarySearchTree
    :param key: A comparable key to be inserted
    :param value: A value associated with the key
    """
    bst.root = _insert(bst, bst.root, key, value)

### For Testing Purposes

# bst = BinarySearchTree()
# insert(bst, 5, 'e')
# insert(bst, 4, 'd')
# insert(bst, 9, 'i')
#
# print(bst)

###

def _min(node):

    if node.left is None:
        return (node.key, node.value)

    else:
        return _min(node.left)

def _remove(bst, node, key):

    if key == node.key:
        if node.right is None:
            bst.size -= 1
            return node.left
        elif node.left is None:
            bst.size -= 1
            return node.right
        else:
            smallest = _min(node.right)
            node.right = _remove(bst, node.right, smallest[0])
            node.key = smallest[0]
            node.value = smallest[1]
            return node

    elif key < node.key:
        node.left = _remove(bst, node.left, key)
        return node
    else:
        node.right = _remove(bst, node.right, key)
        return node

def remove(bst, key):
    """
    Remove a key and its associated value.
    TODO: Implement this function. It must have O(log n) complexity.

    :param bst: A BinarySearchTree
    :param key: A comparable key to be removed
    :return: The value associated with the removed key
    :raise KeyError: If the key is not in the BST
    """
    value = find(bst, key)

    bst.root = _remove(bst, bst.root, key)
    return value

### For Testing Purposes

# remove(bst, 4)
# remove(bst, 5)
# print(bst)

###

def _traverse(node, queue = None):

    if queue is None:
        queue = Queue()

    if node is None:
        return queue

    else:
        _traverse(node.left, queue)
        enqueue(queue, (node.key, node.value))
        _traverse(node.right, queue)

    return queue

def inorder(bst):
    """
    Traverse a BST in sorted order.
    TODO: Implement this function. It must have O(n) complexity.

    :param bst: A BinarySearchTree
    :return: A new Queue containing the BST's key-value pairs in sorted order
    """
    return _traverse(bst.root)
