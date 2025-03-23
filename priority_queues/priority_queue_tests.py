# Tests priority queues.
# CSC 202, Lab 8
# Given tests, Summer '19

import unittest
from priority_queue import *


class TestPriorityQueue(unittest.TestCase):
    def test01_methods(self):
        msg = "Testing priority queue equality and representation"

        pqueue = PriorityQueue()
        pqueue.array[1] = 0
        pqueue.size = 1

        self.assertEqual(pqueue, pqueue, msg)
        self.assertEqual(repr(pqueue),
         "PriorityQueue(4, [None, 0, None, None, None], 1)", msg)

        other = PriorityQueue()
        other.array[1] = 1
        other.size = 1

        self.assertNotEqual(pqueue, other, msg)
        self.assertNotEqual(pqueue, pqueue.array, msg)

    def test02_empty(self):
        msg = "Testing empty priority queues"

        pqueue = PriorityQueue()

        self.assertEqual(size(pqueue), 0, msg)

    def test03_enqueue(self):
        msg = "Testing enqueueing to priority queues"

        pqueue = PriorityQueue()
        enqueue(pqueue, 5)
        enqueue(pqueue, 2)
        enqueue(pqueue, 7)

        self.assertEqual(size(pqueue), 3, msg)
        self.assertEqual(peek(pqueue), 7, msg)

    def test04_dequeue(self):
        msg = "Testing dequeueing from priority queues"

        pqueue = PriorityQueue()
        enqueue(pqueue, 5)
        enqueue(pqueue, 2)
        enqueue(pqueue, 7)
        dequeue(pqueue)
        enqueue(pqueue, 8)

        self.assertEqual(size(pqueue), 3, msg)
        self.assertEqual(peek(pqueue), 8, msg)

    def test05_dequeue(self):
        msg = "Testing dequeueing and peeking with an empty priority queue"

        pqueue = PriorityQueue()

        self.assertEqual(size(pqueue), 0, msg)
        with self.assertRaises(ValueError, msg = msg):
            dequeue(pqueue)
        with self.assertRaises(ValueError, msg = msg):
            peek(pqueue)

    def test06_enqueue(self):
        msg = "Testing enqueueing many items to priority queues"

        pqueue = PriorityQueue()
        enqueue(pqueue, 5)
        enqueue(pqueue, 2)
        enqueue(pqueue, 8)
        enqueue(pqueue, 0)
        enqueue(pqueue, 9)

        self.assertEqual(size(pqueue), 5, msg)
        self.assertEqual(peek(pqueue), 9, msg)

    def test07_enqueue(self):
        msg = "Testing enqueueing when item enqueued belongs at leaf"

        pqueue = PriorityQueue()
        enqueue(pqueue, 5)
        enqueue(pqueue, 2)

        self.assertEqual(size(pqueue), 2, msg)
        self.assertEqual(peek(pqueue), 5, msg)

    def test08_dequeue(self):
        msg = "Testing dequeueing from priority queues"

        pqueue = PriorityQueue()
        enqueue(pqueue, 5)
        dequeue(pqueue)
        enqueue(pqueue, 20)
        enqueue(pqueue, 7)
        enqueue(pqueue, 6)
        dequeue(pqueue)
        enqueue(pqueue, 9)

        self.assertEqual(size(pqueue), 3, msg)
        self.assertEqual(peek(pqueue), 9, msg)

    def test09_dequeue(self):
        msg = "Testing dequeueing from priority queues"

        pqueue = PriorityQueue()

        enqueue(pqueue, 8)
        enqueue(pqueue, 10)
        dequeue(pqueue)
        enqueue(pqueue, 9)
        dequeue(pqueue)
        enqueue(pqueue, 13)
        enqueue(pqueue, 6)
        dequeue(pqueue)
        enqueue(pqueue, 3)
        dequeue(pqueue)

        self.assertEqual(size(pqueue), 2, msg)
        self.assertEqual(peek(pqueue), 6, msg)

    def test10_dequeue(self):
        msg = "Testing dequeueing from priority queues"

        pqueue = PriorityQueue()

        enqueue(pqueue, 9)
        enqueue(pqueue, 8)
        enqueue(pqueue, 10)
        enqueue(pqueue, 11)
        dequeue(pqueue)

        self.assertEqual(size(pqueue), 3, msg)
        self.assertEqual(peek(pqueue), 10, msg)

    def test11_dequeue(self):
        msg = "Testing dequeueing from priority queues"

        pqueue = PriorityQueue()

        enqueue(pqueue, 5)
        enqueue(pqueue, 2)
        enqueue(pqueue, 7)
        enqueue(pqueue, 8)
        enqueue(pqueue, 3)
        enqueue(pqueue, 19)
        dequeue(pqueue)

        self.assertEqual(size(pqueue), 5, msg)
        self.assertEqual(peek(pqueue), 8, msg)

    def test12_dequeue(self):
        msg = "Testing dequeueing from priority queues"

        pqueue = PriorityQueue()

        enqueue(pqueue, 5)
        enqueue(pqueue, 2)
        enqueue(pqueue, 7)
        enqueue(pqueue, 8)
        enqueue(pqueue, 3)
        enqueue(pqueue, 19)
        dequeue(pqueue)

        self.assertEqual(size(pqueue), 5, msg)
        self.assertEqual(peek(pqueue), 8, msg)

    def test13_dequeue(self):
        msg = "Testing dequeueing from priority queues"

        pqueue = PriorityQueue()

        enqueue(pqueue, 1)
        enqueue(pqueue, 1)
        enqueue(pqueue, 1)
        enqueue(pqueue, 1)
        dequeue(pqueue)
        dequeue(pqueue)

        self.assertEqual(size(pqueue), 2, msg)
        self.assertEqual(peek(pqueue), 1, msg)

if __name__ == "__main__":
    unittest.main()
