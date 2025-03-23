# Implements an array list.
# CSC 202, Lab 3
# Given code, Summer '19


class List:
    """
    An ordered collection of elements
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this list:
        self.size = 0

    def __eq__(self, other):
        if type(other) != List or self.size != other.size:
            return False

        for idx in range(self.size):
            if self.array[idx] != other.array[idx]:
                return False

        return True

    def __repr__(self):
        return "List(%d, %r, %d)" % (self.capacity, self.array, self.size)


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
    TODO: Implement this function. It must have O(1) complexity.

    :param lst: A List
    :param idx: An index at which to get an element
    :return: The element in the list at the index
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx >= lst.size: # If the index is out-of-bounds, raise an index error
        raise IndexError("Index is out-of-bounds")

    return lst.array[idx]


def set(lst, idx, value):
    """
    Set the element at an index.
    TODO: Implement this function. It must have O(1) complexity.

    :param lst: A List
    :param idx: An index at which to set an element
    :param value: A value to which to set an element
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx >= lst.size: # If the index is out-of-bounds, raise an index error
        raise IndexError("Index is out-of-bounds")

    lst.array[idx] = value

def add(lst, idx, value):
    """
    Add an element at an index, doubling capacity first if necessary.
    TODO: Implement this function. It must have O(n) complexity.

    :param lst: A List
    :param idx: An index at which to add an element
    :param value: A value to add as an element
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx > lst.size: # If the index is out-of-bounds, raise an index error
        raise IndexError("Index is out-of-bounds")

    if lst.size == lst.capacity: # If the existing list has reached capacity

        lst.capacity = lst.capacity * 2 # Update the list's capacity to 2X the original
        new_lst = List() # Initialize a new list
        new_lst.array = [None] * lst.capacity # Create a new array (containing Nones)

        for i in range(lst.size):
            new_lst.array[i] = lst.array[i] # Copy each item from the previous array into the new array

        lst.array = new_lst.array # Set the old array to the new array

    for i in range(lst.size, idx, -1): # Shift all values in the list down one index to make space for the new value
        lst.array[i] = lst.array[i - 1]

    lst.array[idx] = value
    lst.size += 1

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

    temp = lst.array[idx]

    for i in range(idx, lst.size - 1): # Shift all values in the list up one index to fill in space when removing a value
        lst.array[i] = lst.array[i + 1]

    lst.size -= 1
    return temp
