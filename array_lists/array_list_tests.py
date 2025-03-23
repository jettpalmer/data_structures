# Tests array lists.
# CSC 202, Lab 3
# Given tests, Summer '19

import unittest
from array_list import *


class TestList(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing list equality and representation"

        lst = List()
        lst.array = ['a', None, None, None]
        lst.size = 1

        self.assertEqual(lst, lst, msg)
        self.assertEqual(repr(lst), "List(4, ['a', None, None, None], 1)", msg)

        other = List()
        other.array = ['b', None, None, None]
        other.size = 1

        self.assertNotEqual(lst, other, msg)
        self.assertNotEqual(lst, lst.array, msg)

    def test02_empty(self):
        msg = "Testing empty lists"

        lst = List()

        self.assertEqual(size(lst), 0, msg)

    def test03_add(self):
        msg = "Testing adding to lists"

        lst = List()
        add(lst, 0, 'a')
        add(lst, 1, 'b')

        self.assertEqual(size(lst), 2, msg)
        self.assertEqual(get(lst, 0), 'a', msg)
        self.assertEqual(get(lst, 1), 'b', msg)

    def test04_remove(self):
        msg = "Testing removing from lists"

        lst = List()
        add(lst, 0, 'b')
        add(lst, 1, 'c')
        add(lst, 1, 'a')
        remove(lst, 1)
        add(lst, 0, 'a')

        self.assertEqual(size(lst), 3, msg)
        self.assertEqual(get(lst, 0), 'a', msg)
        self.assertEqual(get(lst, 1), 'b', msg)
        self.assertEqual(get(lst, 2), 'c', msg)

    def test05_add(self):
        msg = "Testing add() when index is out of bounds"

        lst = List()
        add(lst, 0, 'a')
        add(lst, 1, 'b')

        with self.assertRaises(IndexError, msg = msg):
            add(lst,-1, 'a')

    def test06_get(self):
        msg = "Testing get() when index is out of bounds"

        lst = List()
        add(lst, 0, 'a')
        add(lst, 1, 'b')

        with self.assertRaises(IndexError, msg = msg):
            get(lst,-1)

    def test07_set(self):
        msg = "Testing set() when index is out of bounds"

        lst = List()
        add(lst, 0, 'a')
        add(lst, 1, 'b')

        with self.assertRaises(IndexError, msg = msg):
            set(lst,-1, 'a')

    def test08_remove(self):
        msg = "Testing remove() when index is out of bounds"

        lst = List()
        add(lst, 0, 'a')
        add(lst, 1, 'b')

        with self.assertRaises(IndexError, msg = msg):
            remove(lst,-1)

    def test09_add(self):
        msg = "Testing adding to an array that is at capacity"

        lst = List()
        add(lst, 0, 'a')
        add(lst, 1, 'b')
        add(lst, 2, 'c')
        add(lst, 3, 'd')
        add(lst, 4, 'e')

        self.assertEqual(size(lst), 5, msg)
        # self.assertEqual(get(lst, 0), 'a', msg)
        # self.assertEqual(get(lst, 1), 'b', msg)
        # self.assertEqual(get(lst, 2), 'c', msg)

    def test10_remove(self):
        msg = "Testing removing from lists"

        lst = List()
        add(lst, 0, 'a')
        add(lst, 1, 'b')
        add(lst, 2, 'c')

        self.assertEqual(size(lst), 3, msg)
        self.assertEqual(get(lst, 0), 'a', msg)
        self.assertEqual(get(lst, 1), 'b', msg)
        self.assertEqual(remove(lst, 1), 'b', msg)

if __name__ == "__main__":
    unittest.main()
