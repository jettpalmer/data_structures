# Implements a linked list.
# CSC 202, Lab 2
# Given code, Summer '19


class List:
    """
    An ordered collection of elements
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The head of the backing linked list:
        self.head = None
        # The number of elements in this list:
        self.size = 0

    def __eq__(self, other):
        return (type(other) == List
                and self.head == other.head
                and self.size == other.size)

    def __repr__(self):
        return "List(%r, %d)" % (self.head, self.size)


class Node:
    """
    A single node in a linked list
    NOTE: Do not alter this class.
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

# Creating objects for function testing
# lst = List() # Create empty linked list
# lst.head = Node('a', 'b')
# lst.size = 1

def size(lst):
    """
    Calculate the size of a list.
    TODO: Implement this function. It must have O(1) complexity.

    :param lst: A List
    :return: The number of elements in the list
    """
    return lst.size

def get(lst, idx):
    """
    Get the element at an index.
    TODO: Implement this function. It must have O(n) complexity.

    :param lst: A List
    :param idx: An index at which to get an element
    :return: The element in the list at the index
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx >= lst.size: # If the index is out-of-bounds, raise an index error
        raise IndexError("Index is out-of-bounds")

    current = lst.head # Set the current Node to the List's head

    for i in range(idx): # Traverse forward from the head to the Node at the given index
        current = current.next # Set the current Node to the current Node's next

    return current.value # Return the current Node's value

def set(lst, idx, value):
    """
    Set the element at an index.
    TODO: Implement this function. It must have O(n) complexity.

    :param lst: A List
    :param idx: An index at which to set an element
    :param value: A value to which to set an element
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx >= lst.size: # If the index is out-of-bounds, raise an index error
        raise IndexError("Index is out-of-bounds")

    current = lst.head # Set the current Node to the List's head

    for i in range(idx): # Traverse forward from the head to the Node at the given index
        current = current.next # Set the current Node to the current Node's next

    current.value = value # Change the value of the current Node to the given value


def add(lst, idx, value):
    """
    Add an element at an index.
    TODO: Implement this function. It must have O(n) complexity.

    :param lst: A List
    :param idx: An index at which to add an element
    :param value: A value to add as an element
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx > lst.size: # If the index is out-of-bounds, raise an index error
        raise IndexError("Index is out-of-bounds")

    new_node = Node(value, None) # Initialize a new_node using the value provided

    if idx == 0: # If the index is 0 (to create a new head):
        new_node.next = lst.head # Set the new Node's next to the current List's head
        lst.head = new_node # Set the List's head to the new Node

    else: # Otherwise:

        current = lst.head # Set current Node to the List's head

        for i in range(idx - 1): # Traverse forward from the head to the Node BEFORE the given index
            current = current.next # Set the current Node to the current Node's next

        new_node.next = current.next # Set the new Node's next to the current Node's next
        current.next = new_node # Set the current Node's next to the new Node

    lst.size += 1 # Increment the List's size


def remove(lst, idx):
    """
    Remove the element at an index.
    TODO: Implement this function. It must have O(n) complexity.

    :param lst: A List
    :param idx: An index at which to remove an element
    :return: The removed element
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx >= lst.size: # If the index is out-of-bounds, raise an index error
        raise IndexError("Index is out-of-bounds")

    if idx == 0: # If the index is 0 (to remove the head):
        temp = lst.head.value
        lst.head = lst.head.next

    else:

        current = lst.head # Set current Node to the List's head

        for i in range(idx - 1): # Traverse forward from the head to the Node BEFORE the given index
            current = current.next # Set the current Node to the current Node's next

        temp = current.next.value
        current.next = current.next.next # Set the current Node's next to the current Node's next-next

    lst.size -= 1 # Decrement the List's size

    return temp