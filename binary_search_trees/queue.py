# Implements a queue.
# CSC 202, Lab 4
# Given code, Summer '22


class Queue:
    """
    A FIFO collection of elements
    NOTE: Do not alter this class. Some of its attributes may not be necessary,
          depending on your chosen implementation.
    """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The tail of the backing linked list:
        self.tail = None
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The index of the front of the queue:
        self.front = -1
        # The index of the back of the queue:
        self.back = -1
        # The number of elements in this list:
        self.size = 0

    def __eq__(self, other):
        if type(other) != Queue or self.head != other.head\
           or self.tail != other.tail or self.front != other.front\
           or self.back != other.back or self.size != other.size:
            return False

        for offset in range(self.size):
            self_idx = (self.front + offset) % self.capacity
            other_idx = (other.front + offset) % other.capacity
            if self.array[self_idx] != other.array[other_idx]:
                return False

        return True

    def __repr__(self):
        return "Queue(%r, %d, %r, %d, %d, %d)"\
               % (self.head, self.capacity, self.array,
                  self.front, self.back, self.size)


class Node:
    """
    A single node in a linked list
    NOTE: Do not alter this class. It may not be necessary, depending on your
          chosen implementation.
    """

    def __init__(self, value, next):
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next

    def __eq__(self, other):
        return (type(other) == Node
                and self.value == other.value
                and self.next == other.next)

    def __repr__(self):
        return "Node(%r, %r)" % (self.value, self.next)


def size(queue):
    """
    Calculate the size of a queue.
    TODO: Implement this function. It must have O(1) complexity.

    :param queue: A Queue
    :return: The number of elements in the queue
    """
    return queue.size


def enqueue(queue, value):
    """
    Enqueue an element to the back of a queue.
    TODO: Implement this function. It must have O(1) complexity.

    :param queue: A Queue
    :param value: A value to be enqueued
    """
    new_node = Node(value, queue.tail)

    if queue.size == 0:
        queue.head = new_node
    else:
        queue.tail.next = new_node

    queue.tail = new_node
    queue.size += 1


def dequeue(queue):
    """
    Dequeue an element from the front of a queue.
    TODO: Implement this function. It must have O(1) complexity.

    :param queue: A Queue
    :return: The dequeued element
    :raise ValueError: If the queue is empty
    """
    if queue.size == 0:
        raise ValueError("Cannot dequeue from an empty queue.")

    temp = queue.head.value

    if queue.size == 1:
        queue.head = None
        queue.tail = None
    else:
        queue.head = queue.head.next

    queue.size -= 1

    return temp

def peek(queue):
    """
    Peek at the element at the front of a queue.
    TODO: Implement this function. It must have O(1) complexity.

    :param queue: A Queue
    :return: The peeked element
    :raise ValueError: If the queue is empty
    """
    if queue.size == 0:
        raise ValueError("Cannot peek at an empty queue.")

    return queue.head.value
