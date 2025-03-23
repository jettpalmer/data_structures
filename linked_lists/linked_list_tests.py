# Tests linked lists.
# CSC 202, Lab 2
# Given tests, Summer '19

import unittest
from linked_list import *


class TestList(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing list equality and representation"

        lst = List()
        lst.head = Node('a', None)
        lst.size = 1

        self.assertEqual(lst, lst, msg)
        self.assertEqual(repr(lst), "List(Node('a', None), 1)", msg)

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

    def test05_error(self):
        msg = "Testing raising error on get"

        lst = List()
        with self.assertRaises(IndexError, msg = msg):
            get(lst,0)

    def test06_error(self):
        msg = "Testing raising error on add"

        lst = List()
        with self.assertRaises(IndexError, msg = msg):
            add(lst,-1, 'a')

    def test07_error(self):
        msg = "Testing raising error on remove"

        lst = List()
        with self.assertRaises(IndexError, msg = msg):
            remove(lst, -1)

    def test08_error(self):
        msg = "Testing raising error on set"

        lst = List()
        with self.assertRaises(IndexError, msg = msg):
            set(lst,-1, 'a')

    def test09_set(self):
        msg = "Testing set"

        lst = List()
        add(lst, 0, 'a')
        add(lst, 1, 'b')

        set(lst, 1, 'c')

        self.assertEqual(size(lst), 2, msg)
        self.assertEqual(get(lst, 0), 'a', msg)
        self.assertEqual(get(lst, 1), 'c', msg)

    def test10_set(self):
        msg = "Testing add, entering for loop"

        lst = List()
        add(lst, 0, 'a')
        add(lst, 1, 'b')
        add(lst, 2, 'c')

        self.assertEqual(size(lst), 3, msg)
        self.assertEqual(get(lst, 0), 'a', msg)
        self.assertEqual(get(lst, 1), 'b', msg)
        self.assertEqual(get(lst, 2), 'c', msg)

    def test11_remove(self):
        msg = "Testing removing from lists when idx is 0"

        lst = List()
        add(lst, 0, 'b')
        add(lst, 1, 'c')
        remove(lst, 0)

        self.assertEqual(size(lst), 1, msg)
        self.assertEqual(get(lst, 0), 'c', msg)


    def test12_remove(self):
        msg = "Testing removing from list when idx >0"

        lst = List()
        add(lst, 0, 'a')
        add(lst, 1, 'b')
        add(lst, 2, 'c')
        remove(lst, 2)

        self.assertEqual(size(lst), 2, msg)
        self.assertEqual(get(lst, 0), 'a', msg)
        self.assertEqual(get(lst, 1), 'b', msg)

    def test13_remove(self):
        msg = "More testing removing from lists"

        lst = List()
        add(lst, 0, 'b')
        add(lst, 1, 'c')
        add(lst, 2, 'a')

        self.assertEqual(size(lst), 3, msg)
        self.assertEqual(remove(lst, 2), 'a', msg)

if __name__ == "__main__":
    unittest.main()
