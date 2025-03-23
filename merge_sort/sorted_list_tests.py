# Tests sorted lists.
# CSC 202, Lab 5
# Given tests, Summer '19

import unittest
from sorted_list import *


class TestSortedList(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing sorted list equality and representation"

        lst = SortedList()
        lst.array = [0, None, None, None]
        lst.size = 1

        self.assertEqual(lst, lst, msg)
        self.assertEqual(repr(lst),
         "SortedList(4, [0, None, None, None], 1)", msg)

        other = SortedList()
        other.array = [1, None, None, None]
        other.size = 1

        self.assertNotEqual(lst, other, msg)
        self.assertNotEqual(lst, lst.array, msg)

    def test02_insert(self):
        msg = "Testing inserting into sorted lists"

        lst = SortedList()
        insert(lst, -3)
        insert(lst, 3)
        insert(lst, -1)

        self.assertEqual(size(lst), 3, msg)
        self.assertEqual(get(lst, 0), -3, msg)
        self.assertEqual(get(lst, 1), -1, msg)
        self.assertEqual(get(lst, 2), 3, msg)

    def test03_remove(self):
        msg = "Testing removing from sorted lists"

        lst = SortedList()
        insert(lst, -3)
        insert(lst, 3)
        remove(lst, find(lst, 3))
        insert(lst, -1)

        self.assertEqual(size(lst), 2, msg)
        self.assertEqual(get(lst, 0), -3, msg)
        self.assertEqual(get(lst, 1), -1, msg)

    def test04_create(self):
        msg = "Testing creating sorted lists"

        lst = create([0, 1, 2], 3)
        insert(lst, -3)
        remove(lst, find(lst, 1))
        insert(lst, 3)
        remove(lst, find(lst, 3))
        insert(lst, -1)

        self.assertEqual(size(lst), 4, msg)
        self.assertEqual(get(lst, 0), -3, msg)
        self.assertEqual(get(lst, 1), -1, msg)
        self.assertEqual(get(lst, 2), 0, msg)
        self.assertEqual(get(lst, 3), 2, msg)

    def test05_remove(self):
        msg = "Testing remove() when index is out of bounds"

        lst = SortedList()
        insert(lst, 'a')
        insert(lst, 'b')

        with self.assertRaises(IndexError, msg = msg):
            remove(lst,-1)

    def test06_find(self):
        msg = "Testing finding a number in the list"

        lst = SortedList()
        insert(lst, -3)
        insert(lst, 3)
        insert(lst, -1)

        self.assertEqual(find(lst, 3), 2, msg)

    def test07_find(self):
        msg = "Testing finding a number not in the list"

        lst = SortedList()
        insert(lst, -3)
        insert(lst, 3)
        insert(lst, -1)

        with self.assertRaises(ValueError, msg = msg):
            find(lst,4)

    def test08_get(self):
        msg = "Testing get() when index is out of bounds"

        lst = SortedList()
        insert(lst, 'a')
        insert(lst, 'b')

        with self.assertRaises(IndexError, msg = msg):
            get(lst, 2)

    def test09_find(self):
        msg = "Testing finding a number in the list when high = mid - 1"

        lst = SortedList()
        insert(lst, 1)
        insert(lst, 2)
        insert(lst, 3)
        insert(lst, 4)
        insert(lst, 5)

        self.assertEqual(find(lst, 2), 1, msg)

    def test10_create(self):
        msg = "Testing creating sorted lists again"

        lst = create([5, 4, 3, 1, 2, 3], 6)
        insert(lst, -1)
        remove(lst, find(lst, 1))
        insert(lst, -2)
        remove(lst, find(lst, 2))

        self.assertEqual(size(lst), 6, msg)

    def test11_create(self):
        msg = "Testing creating empty sorted lists"

        lst = create([], 0)
        insert(lst, 1)
        insert(lst, -1)
        remove(lst, 1)

        self.assertEqual(size(lst), 1, msg)
        self.assertEqual(get(lst, 0), -1, msg)
        self.assertEqual(find(lst, -1), 0, msg)

if __name__ == "__main__":
    unittest.main()
