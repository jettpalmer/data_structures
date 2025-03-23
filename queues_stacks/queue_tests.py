# Tests queues.
# CSC 202, Lab 4
# Given tests, Summer '22

import unittest
from queue import *


class TestQueue(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing queue equality and representation"

        # NOTE: Your functions are not expected to maintain both a linked queue
        #       and an array queue. This test is doing so only for coverage.

        queue = Queue()
        queue.head = Node('a', None)
        queue.tail = queue.head
        queue.array = ['a', None, None, None]
        queue.front = 0
        queue.back = 0
        queue.size = 1

        self.assertEqual(queue, queue, msg)
        self.assertEqual(repr(queue),
         "Queue(Node('a', None), 4, ['a', None, None, None], 0, 0, 1)", msg)

        other = Queue()
        other.head = Node('a', None)
        other.tail = other.head
        other.array = ['b', None, None, None]
        other.front = 0
        other.back = 0
        other.size = 1

        self.assertNotEqual(queue, other, msg)
        self.assertNotEqual(queue, queue.array, msg)

    def test02_empty(self):
        msg = "Testing empty queues"

        queue = Queue()

        self.assertEqual(size(queue), 0, msg)

    def test03_enqueue(self):
        msg = "Testing enqeueueing to queues"

        queue = Queue()
        enqueue(queue, 'b')
        enqueue(queue, 'a')
        enqueue(queue, 'b')

        self.assertEqual(size(queue), 3, msg)
        self.assertEqual(peek(queue), 'b', msg)

    def test04_dequeue(self):
        msg = "Testing deqeueueing from queues"

        queue = Queue()
        enqueue(queue, 'b')
        enqueue(queue, 'a')
        enqueue(queue, 'b')
        dequeue(queue)
        enqueue(queue, 'c')

        self.assertEqual(size(queue), 3, msg)
        self.assertEqual(peek(queue), 'a', msg)

    def test05_dequeue(self):
        msg = "Testing queue size one in dequeue"

        queue = Queue()

        enqueue(queue, 'a')
        dequeue(queue)

        self.assertEqual(size(queue), 0, msg)

    def test06_dequeue(self):
        msg = "Testing value error in dequeue"

        queue = Queue()

        self.assertEqual(size(queue), 0, msg)
        with self.assertRaises(ValueError, msg=msg):
            dequeue(queue)

    def test07_peek(self):
        msg = "Testing value error in peek"

        queue = Queue()

        self.assertEqual(size(queue), 0, msg)
        with self.assertRaises(ValueError, msg=msg):
            peek(queue)

if __name__ == "__main__":
    unittest.main()
