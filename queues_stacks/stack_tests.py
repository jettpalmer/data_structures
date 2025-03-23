# Tests stacks.
# CSC 202, Lab 4
# Given tests, Summer '22

import unittest
from stack import *


class TestStack(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing stack equality and representation"

        # NOTE: Your functions are not expected to maintain both a linked stack
        #       and an array stack. This test is doing so only for coverage.

        stack = Stack()
        stack.head = Node('a', None)
        stack.array = ['a', None, None, None]
        stack.size = 1

        self.assertEqual(stack, stack, msg)
        self.assertEqual(repr(stack),
         "Stack(Node('a', None), 4, ['a', None, None, None], 1)", msg)

        other = Stack()
        other.head = Node('a', None)
        other.array = ['b', None, None, None]
        other.size = 1

        self.assertNotEqual(stack, other, msg)
        self.assertNotEqual(stack, stack.array, msg)

    def test02_empty(self):
        msg = "Testing empty stacks"

        stack = Stack()

        self.assertEqual(size(stack), 0, msg)

    def test03_push(self):
        msg = "Testing pushing to stacks"

        stack = Stack()
        push(stack, 'a')
        push(stack, 'c')

        self.assertEqual(size(stack), 2, msg)
        self.assertEqual(peek(stack), 'c', msg)

    def test04_pop(self):
        msg = "Testing popping from stacks"

        stack = Stack()
        push(stack, 'a')
        push(stack, 'c')
        pop(stack)
        push(stack, 'b')
        push(stack, 'c')

        self.assertEqual(size(stack), 3, msg)
        self.assertEqual(peek(stack), 'c', msg)

    def test05_pop(self):
        msg = "Testing value error in pop"

        stack = Stack()

        self.assertEqual(size(stack), 0, msg)
        with self.assertRaises(ValueError, msg=msg):
            pop(stack)

    def test06_pop(self):
        msg = "Testing value error in peek"

        stack = Stack()

        self.assertEqual(size(stack), 0, msg)
        with self.assertRaises(ValueError, msg=msg):
            peek(stack)

if __name__ == "__main__":
    unittest.main()
