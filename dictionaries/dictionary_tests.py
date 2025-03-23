# Tests dictionaries.
# CSC 202, Lab 9
# Given tests, Summer '22

import unittest
from array_list import size as lsize, get as lget
from dictionary import *


class TestDictionary(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing dictionary equality and representation"

        # NOTE: A key's hash code is not predictable across multiple Python
        #       processes, and your tests generally should not assume any
        #       particular arrangement of nodes within the backing array.
        idx = hash('a') % 5

        dct = Dictionary()
        dct.array = [None, None, None, None, None]
        dct.array[idx] = Node('a', 1, None)
        dct.size = 1

        self.assertEqual(dct, dct, msg)
        self.assertEqual(repr(dct), "Dictionary(5, %r, 1)" % dct.array, msg)

        other = Dictionary()
        other.array = [None, None, None, None, None]
        other.array[idx] = Node('a', 2, None)
        other.size = 1

        self.assertNotEqual(dct, other, msg)
        self.assertNotEqual(dct.array[idx], other.array[idx], msg)
        self.assertNotEqual(dct, Dictionary(), msg)

    def test02_insert(self):
        msg = "Testing inserting into dictionaries"

        dct = Dictionary()
        insert(dct, 'a', 1)
        insert(dct, 'b', 3)
        insert(dct, 'f', 2)

        self.assertEqual(size(dct), 3, msg)
        self.assertEqual(get(dct, 'a'), 1, msg)
        self.assertEqual(get(dct, 'b'), 3, msg)
        self.assertEqual(get(dct, 'f'), 2, msg)

    def test03_remove(self):
        msg = "Testing removing from dictionaries"

        dct = Dictionary()
        insert(dct, 'a', 1)
        insert(dct, 'b', 3)
        insert(dct, 'f', 2)
        remove(dct, 'b')
        insert(dct, 'c', 2)

        self.assertEqual(size(dct), 3, msg)
        self.assertEqual(get(dct, 'a'), 1, msg)
        self.assertEqual(get(dct, 'c'), 2, msg)
        self.assertEqual(get(dct, 'f'), 2, msg)
        self.assertIsNone(get(dct, 'b'), msg)

    def test04_keys(self):
        msg = "Testing enumerating the keys in a dictionary"

        dct = Dictionary()
        insert(dct, 'a', 1)
        insert(dct, 'b', 3)
        insert(dct, 'f', 2)
        remove(dct, 'b')
        insert(dct, 'c', 2)
        lst = keys(dct)

        self.assertEqual(lsize(lst), 3, msg)
        self.assertIn('a', {lget(lst, 0), lget(lst, 1), lget(lst, 2)}, msg)
        self.assertIn('c', {lget(lst, 0), lget(lst, 1), lget(lst, 2)}, msg)
        self.assertIn('f', {lget(lst, 0), lget(lst, 1), lget(lst, 2)}, msg)

    def test05_get(self):
        msg = "Testing get when current node is none"

        dct = Dictionary()

        self.assertIsNone(get(dct, 'a'), msg)

    def test06_insert(self):
        msg = "Testing inserting into dictionaries requiring expansion"

        dct = Dictionary()
        insert(dct, 'a', 1)
        insert(dct, 'b', 3)
        insert(dct, 'f', 2)
        insert(dct, 'c', 3)
        insert(dct, 'd', 4)
        insert(dct, 'g', 6)

        self.assertEqual(size(dct), 6, msg)
        self.assertEqual(get(dct, 'a'), 1, msg)
        self.assertEqual(get(dct, 'b'), 3, msg)
        self.assertEqual(get(dct, 'f'), 2, msg)
        self.assertEqual(dct.capacity, 11, msg)

    def test07_remove(self):
        msg = "Testing remove when current node is none"

        dct = Dictionary()

        self.assertIsNone(remove(dct, 'a'), msg)

    def test08_remove(self):
        msg = "Testing removing from dictionaries with collisions"

        dct = Dictionary()
        insert(dct, 0, 1)
        insert(dct, 5, 2)
        insert(dct, 10, 3)
        remove(dct, 10)

        self.assertEqual(size(dct), 2, msg)
        self.assertEqual(get(dct, 0), 1, msg)
        self.assertEqual(get(dct, 5), 2, msg)

    def test09_remove(self):
        msg = "Testing removing the first item the dictionary"

        dct = Dictionary()
        insert(dct, 0, 1)
        insert(dct, 5, 2)
        insert(dct, 10, 3)

        self.assertEqual(size(dct), 3, msg)
        self.assertEqual(remove(dct, 0), 1, msg)

    def test10_get(self):
        msg = "Testing get when current node is none (2)"

        dct = Dictionary()

        insert(dct, 0, 1)
        insert(dct, 10, 2)

        self.assertEqual(get(dct, 0), 1, msg)
        self.assertEqual(get(dct, 10), 2, msg)
        self.assertIsNone(get(dct, 5), msg)

    def test11_remove(self):
        msg = "Testing removing and returning default (2)"

        dct = Dictionary()
        insert(dct, 0, 1)

        self.assertEqual(size(dct), 1, msg)
        self.assertIsNone(remove(dct, 5), msg)

    def test12_remove(self):
        msg = "Testing removing and returning default (3)"

        dct = Dictionary()
        insert(dct, 'a', 1)
        insert(dct, 'b', 2)
        insert(dct, 'c', 3)

        self.assertIsNone(remove(dct, 'd'), msg)
        self.assertEqual(size(dct), 3, msg)

    def test13_remove(self):
        msg = "Testing nonexistent keys and defaults"

        dct = Dictionary()
        insert(dct, 1, 4)
        insert(dct, 2, 5)
        insert(dct, 3, 6)

        self.assertEqual(remove(dct, -3, "hello"), "hello", msg)
        self.assertEqual(size(dct), 3, msg)


if __name__ == "__main__":
    unittest.main()
