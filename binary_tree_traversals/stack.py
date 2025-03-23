# Implements a stack.
# CSC 202, Lab 4
# Given code, Summer '22


class Stack:
    """
    A LIFO collection of elements
    NOTE: Do not alter this class. Some of its attributes may not be necessary,
          depending on your chosen implementation.
    """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this stack:
        self.size = 0

    def __eq__(self, other):
        if type(other) != Stack or self.head != other.head\
           or self.size != other.size:
            return False

        for idx in range(self.size):
            if self.array[idx] != other.array[idx]:
                return False

        return True

    def __repr__(self):
        return "Stack(%r, %d, %r, %d)"\
               % (self.head, self.capacity, self.array, self.size)


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


def size(stack):
    """
    Calculate the size of a stack.
    TODO: Implement this function. It must have O(1) complexity.

    :param stack: A Stack
    :return: The number of elements in the stack
    """
    return stack.size


def push(stack, value):
    """
    Push an element onto the top of a stack.
    TODO: Implement this function. It must have O(1) complexity.

    :param stack: A Stack
    :param value: A value to be pushed
    """
    new_node = Node(value, stack.head)
    stack.head = new_node

    stack.size += 1


def pop(stack):
    """
    Pop an element off the top of a stack.
    TODO: Implement this function. It must have O(1) complexity.

    :param stack: A Stack
    :return: The popped element
    :raise ValueError: If the stack is empty
    """
    if stack.size == 0:
        raise ValueError("Cannot pop from an empty stack.")

    temp = stack.head.value
    stack.head = stack.head.next

    stack.size -= 1

    return temp

def peek(stack):
    """
    Peek at the element on top of a stack.
    TODO: Implement this function. It must have O(1) complexity.

    :param stack: A Stack
    :return: The peeked element
    :raise ValueError: If the stack is empty
    """
    if stack.size == 0:
        raise ValueError("Cannot peek at an empty stack.")

    return stack.head.value
