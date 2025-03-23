# Tests binary trees.
# CSC 202, Lab 6
# Given tests, Summer '22

import unittest
from queue import size as qsize, dequeue
from binary_tree import *


class TestBinaryTree(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing binary tree equality and representation"

        tree = BinaryTree()
        tree.root = Node(0, None, None)
        tree.size = 1

        self.assertEqual(tree, tree, msg)
        self.assertEqual(repr(tree), "BinaryTree(Node(0, None, None), 1)", msg)

    def test02_combine(self):
        msg = "Testing combining empty binary trees"

        tree = combine(0,
                BinaryTree(1),
                BinaryTree())

        self.assertEqual(size(tree), 2, msg)
        self.assertEqual(tree.root.value, 0, msg)
        self.assertEqual(tree.root.left.value, 1, msg)

    def test03_combine(self):
        msg = "Testing combining full binary trees"

        tree = combine(0,
                combine(1,
                 BinaryTree(3),
                 BinaryTree(4)),
                BinaryTree(2))

        self.assertEqual(size(tree), 5, msg)
        self.assertEqual(tree.root.value, 0, msg)
        self.assertEqual(tree.root.left.value, 1, msg)
        self.assertEqual(tree.root.right.value, 2, msg)
        self.assertEqual(tree.root.left.left.value, 3, msg)
        self.assertEqual(tree.root.left.right.value, 4, msg)

    def test04_postorder(self):
        msg = "Testing traversing binary trees in post-order"

        tree = combine(0,
                combine(1,
                 BinaryTree(3),
                 BinaryTree(4)),
                BinaryTree(2))
        traversal = postorder(tree)

        self.assertEqual(qsize(traversal), 5, msg)
        self.assertEqual(dequeue(traversal), 3, msg)
        self.assertEqual(dequeue(traversal), 4, msg)
        self.assertEqual(dequeue(traversal), 1, msg)
        self.assertEqual(dequeue(traversal), 2, msg)
        self.assertEqual(dequeue(traversal), 0, msg)

    def test05_preorder(self):
        msg = "Testing traversing binary trees in pre-order"

        tree = combine(0,
                combine(1,
                 BinaryTree(3),
                 BinaryTree(4)),
                BinaryTree(2))
        traversal = preorder(tree)

        self.assertEqual(qsize(traversal), 5, msg)
        self.assertEqual(dequeue(traversal), 0, msg)
        self.assertEqual(dequeue(traversal), 1, msg)
        self.assertEqual(dequeue(traversal), 3, msg)
        self.assertEqual(dequeue(traversal), 4, msg)
        self.assertEqual(dequeue(traversal), 2, msg)


    def test06_levelorder(self):
        msg = "Testing traversing binary trees in level-order"

        tree = combine(0,
                combine(1,
                 BinaryTree(3),
                 BinaryTree(4)),
                BinaryTree(2))
        traversal = levelorder(tree)

        self.assertEqual(qsize(traversal), 5, msg)
        self.assertEqual(dequeue(traversal), 0, msg)
        self.assertEqual(dequeue(traversal), 1, msg)
        self.assertEqual(dequeue(traversal), 2, msg)
        self.assertEqual(dequeue(traversal), 3, msg)
        self.assertEqual(dequeue(traversal), 4, msg)

    def test07_empty(self):
        msg = "Testing traversing binary trees that are empty"

        tree = BinaryTree()

        preorder_trav = preorder(tree)
        postorder_trav = postorder(tree)
        levelorder_trav = levelorder(tree)

        self.assertEqual(qsize(preorder_trav), 0, msg)
        self.assertEqual(qsize(postorder_trav), 0, msg)
        self.assertEqual(qsize(levelorder_trav), 0, msg)

if __name__ == "__main__":
    unittest.main()
