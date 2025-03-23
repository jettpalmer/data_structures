# Tests binary search trees.
# CSC 202, Lab 7
# Given tests, Summer '19

import unittest
from queue import size as qsize, dequeue
from bst import *


class TestBinarySearchTree(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing BST equality and representation"

        bst = BinarySearchTree()
        bst.root = Node(1, 'a', None, None)
        bst.size = 1

        self.assertEqual(bst, bst, msg)
        self.assertEqual(repr(bst),
         "BinarySearchTree(Node(1, 'a', None, None), 1)", msg)

    def test02_insert(self):
        msg = "Testing inserting into BSTs"

        bst = BinarySearchTree()
        insert(bst, 5, 'e')
        insert(bst, 4, 'd')
        insert(bst, 9, 'i')

        self.assertEqual(size(bst), 3, msg)
        self.assertEqual(find(bst, 4), 'd', msg)
        self.assertEqual(find(bst, 5), 'e', msg)
        self.assertEqual(find(bst, 9), 'i', msg)

    def test03_remove(self):
        msg = "Testing removing from BSTs"

        bst = BinarySearchTree()
        insert(bst, 5, 'e')
        insert(bst, 4, 'd')
        insert(bst, 9, 'i')
        insert(bst, 2, 'b')
        insert(bst, 8, 'h')
        remove(bst, 4)
        remove(bst, 5)
        insert(bst, 5, 'e')
        insert(bst, 0, '`')

        self.assertEqual(size(bst), 5, msg)
        self.assertEqual(find(bst, 0), '`', msg)
        self.assertEqual(find(bst, 2), 'b', msg)
        self.assertEqual(find(bst, 5), 'e', msg)
        self.assertEqual(find(bst, 8), 'h', msg)
        self.assertEqual(find(bst, 9), 'i', msg)

    def test04_inorder(self):
        msg = "Testing traversing BSTs in sorted order"

        bst = BinarySearchTree()
        insert(bst, 5, 'e')
        insert(bst, 4, 'd')
        insert(bst, 9, 'i')
        traversal = inorder(bst)

        self.assertEqual(qsize(traversal), 3, msg)
        self.assertEqual(dequeue(traversal), (4, 'd'), msg)
        self.assertEqual(dequeue(traversal), (5, 'e'), msg)
        self.assertEqual(dequeue(traversal), (9, 'i'), msg)

    def test05_find(self):
        msg = "Testing inserting then finding a value error"

        bst = BinarySearchTree()
        insert(bst, 5, 'e')

        with self.assertRaises(KeyError, msg=msg):
            find(bst, 1)

    def test06_find(self):
        msg = "Testing inserting then finding a value error"

        bst = BinarySearchTree()
        insert(bst, 5, 'e')

        with self.assertRaises(KeyError, msg=msg):
            find(bst, 1)

    def test07_remove(self):
        msg = "Testing remove with a value error"

        bst = BinarySearchTree()
        insert(bst, 5, 'e')
        insert(bst, 4, 'd')
        insert(bst, 9, 'i')

        with self.assertRaises(KeyError, msg=msg):
            remove(bst, 8)

    def test08_insert(self):
        msg = "Testing inserting when key equals the node key"

        bst = BinarySearchTree()
        insert(bst, 5, 'e')
        insert(bst, 5, 'd')

        self.assertEqual(size(bst), 1, msg)
        self.assertEqual(find(bst, 5), "d", msg)

    def test09_remove(self):
        msg = "Testing removing a left child"

        bst = BinarySearchTree()
        insert(bst, 5, 'e')
        insert(bst, 4, 'c')
        remove(bst, 4)

        # self.assertEqual(remove(bst, 4), 'c', msg)
        self.assertEqual(size(bst), 1, msg)

    def test10_remove(self):
        msg = "Testing removing a left child"

        bst = BinarySearchTree()
        insert(bst, 5, 'e')
        insert(bst, 6, 'c')
        remove(bst, 6)

        self.assertEqual(size(bst), 1, msg)

    def test11_remove(self):
        msg = "Testing removing a left child"

        bst = BinarySearchTree()
        insert(bst, 5, 'e')
        insert(bst, 6, 'c')
        remove(bst, 5)

        self.assertEqual(size(bst), 1, msg)

if __name__ == "__main__":
    unittest.main()
