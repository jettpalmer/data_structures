# Tests linear searching.
# CSC 202, Lab 1
# Given tests, Summer '22

import unittest
import linear_search as ls

class TestLinearSearch(unittest.TestCase):
    def test01_iterative(self):
        self.assertEqual(ls.iterative_search([1, 2, 3], 2), 1)

    def test02_iterative(self):
        self.assertIsNone(ls.iterative_search([1, 2, 3], 4))

    def test01_recursive(self):
        msg = "Testing recursively searching an empty list"
        self.assertIsNone(ls.recursive_search([], 1), msg)

    def test02_recursive(self):
        msg = "Testing recursively searching a singleton list"
        self.assertEqual(ls.recursive_search([1], 1), 0, msg)

    def test03_recursive(self):
        msg = "Testing recursively searching for an existent element"
        self.assertEqual(ls.recursive_search([1, 2, 3], 2), 1, msg)

    def test04_recursive(self):
        msg = "Testing recursively searching for a nonexistent element"
        self.assertIsNone(ls.recursive_search([1, 2, 3], 4), msg)

    def test05_recursive(self):
        msg = "Testing recursively searching a larger list"
        self.assertEqual(ls.recursive_search(list(range(20)), 19), 19, msg)


if __name__ == "__main__":
    unittest.main()
