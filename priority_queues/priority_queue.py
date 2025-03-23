# Implements a priority queue.
# CSC 202, Lab 8
# Given code, Summer '19


class PriorityQueue:
    """
    A prioritized collection of elements
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array, placeholder at index 0:
        self.array = [None] * (self.capacity + 1)
        # The number of elements in this queue:
        self.size = 0

    def __eq__(self, other):
        if type(other) != PriorityQueue or self.size != other.size:
            return False

        for idx in range(1, self.size + 1):
            if self.array[idx] != other.array[idx]:
                return False

        return True

    def __repr__(self):
        return "PriorityQueue(%d, %r, %d)"\
               % (self.capacity, self.array, self.size)


def size(pqueue):
    """
    Calculate the size of a priority queue.
    TODO: Implement this function. It must have O(1) complexity.

    :param pqueue: A PriorityQueue
    :return: The number of elements in the priority queue
    """
    return pqueue.size

### For Testing Purposes ###

# pqueue = PriorityQueue()

###

def enqueue(pqueue, value):
    """
    Enqueue an element with some priority to a priority queue.
    TODO: Implement this function. It must have O(1) complexity.

    :param pqueue: A PriorityQueue
    :param value: A comparable value to be enqueued
    """
    if pqueue.size == pqueue.capacity:

        pqueue.capacity = pqueue.capacity * 2
        new_array = [None] * (pqueue.capacity + 1)

        for i in range(pqueue.size):
            new_array[i + 1] = pqueue.array[i + 1]

        pqueue.array = new_array

    i = pqueue.size + 1
    pqueue.array[i] = value

    while i > 1:

        if pqueue.array[i] > pqueue.array[i // 2]:
            temp = pqueue.array[i]
            pqueue.array[i] = pqueue.array[i // 2]
            pqueue.array[i // 2] = temp
            i = i // 2
        else:
            i = 0

    pqueue.size += 1

def dequeue(pqueue):
    """
    Dequeue the element of highest priority from a priority queue.
    TODO: Implement this function. It must have O(log n) complexity.

    :param pqueue: A PriorityQueue
    :return: The dequeued element
    :raise ValueError: If the priority queue is empty
    """
    if pqueue.size == 0:
        raise ValueError("Priority queue is empty.")

    i = 1

    highest_priority = pqueue.array[i]
    pqueue.array[i] = pqueue.array[pqueue.size]

    while 2 * i <= pqueue.size:

        left = 2 * i
        right = 2 * i + 1

        if right > pqueue.size or pqueue.array[left] > pqueue.array[right]:
            if pqueue.array[left] > pqueue.array[i]:
                temp = pqueue.array[i]
                pqueue.array[i] = pqueue.array[left]
                pqueue.array[left] = temp
                i = left
            else:
                break
        else:
            if pqueue.array[right] > pqueue.array[i]:
                temp = pqueue.array[i]
                pqueue.array[i] = pqueue.array[right]
                pqueue.array[right] = temp
                i = right
            else:
                break

    pqueue.size -= 1

    return highest_priority

### For Testing Purposes ###

# enqueue(pqueue, 'a')
# enqueue(pqueue, 'b')
# enqueue(pqueue, 'c')
# dequeue(pqueue)
# enqueue(pqueue, 0)
# enqueue(pqueue, 9)
# dequeue(pqueue)

# print(pqueue.array)

###

def peek(pqueue):
    """
    Peek at the element of highest priority in a queue.
    TODO: Implement this function. It must have O(1) complexity.

    :param pqueue: A PriorityQueue
    :return: The peeked element
    :raise ValueError: If the priority queue is empty
    """
    if pqueue.size == 0:
        raise ValueError("Priority queue is empty.")

    return pqueue.array[1]
