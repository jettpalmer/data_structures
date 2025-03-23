# Implements a sorted list.
# CSC 202, Lab 5
# Given code, Summer '19


class SortedList:
    """
    A sorted collection of elements
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 4
        # The backing array:
        self.array = [None] * self.capacity
        # The number of elements in this sorted list:
        self.size = 0

    def __eq__(self, other):
        if type(other) != SortedList or self.size != other.size:
            return False

        for idx in range(self.size):
            if self.array[idx] != other.array[idx]:
                return False

        return True

    def __repr__(self):
        return "SortedList(%d, %r, %d)"\
               % (self.capacity, self.array, self.size)


def size(lst):
    """
    Calculate the size of a sorted list.
    TODO: Implement this function. It must have O(1) complexity.

    :param lst: A SortedList
    :return: The number of elements in the sorted list
    """
    return lst.size


def get(lst, idx):
    """
    Get the element at an index.
    TODO: Implement this function. It must have O(1) complexity.

    :param lst: A SortedList
    :param idx: An index at which to get an element
    :return: The element in the sorted list at the index
    :raise IndexError: If the index is out-of-bounds
    """
    if idx < 0 or idx >= lst.size: # If the index is out-of-bounds, raise an index error
        raise IndexError("Index is out-of-bounds")

    return lst.array[idx]


def insert(lst, value):
    """
    Insert an element in sorted order, doubling capacity first if necessary.
    TODO: Implement this function. It must have O(n) complexity.

    :param lst: A SortedList
    :param value: A comparable value to insert as an element
    """
    if lst.size == lst.capacity: # If the existing list has reached capacity

        lst.capacity = lst.capacity * 2 # Update the list's capacity to 2X the original
        new_lst = SortedList() # Initialize a new sorted list
        new_lst.array = [None] * lst.capacity # Create a new array (containing Nones)

        for i in range(lst.size):
            new_lst.array[i] = lst.array[i] # Copy each item from the previous array into the new array

        lst.array = new_lst.array # Set the old array to the new array

    i = lst.size

    while ((i - 1) >= 0) and (lst.array[i - 1] > value): # While:
        # 1. i - 1 is greater than or equal to zero AND
        # 2. The element at i - 1 is greater than the value

        lst.array[i] = lst.array[i - 1] # Shift the values over to make space for 'value'
        i -= 1 # Decrement i

    lst.array[i] = value # Add the new value to the list
    lst.size += 1


def remove(lst, idx):
    """
    Remove the element at an index.
    TODO: Implement this function. It must have O(n) complexity.

    :param lst: A SortedList
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

def find(lst, value):
    """
    Find the index of an element.
    TODO: Implement this function. It must have O(log n) complexity.

    :param lst: A SortedList
    :param value: A comparable value to find as an element
    :return: The index of an element equal to the value
    :raise ValueError: If no element is equal to the value
    """
    low_idx = 0
    high_idx = lst.size - 1

    while low_idx <= high_idx:
        mid_idx = (high_idx + low_idx) // 2

        if lst.array[mid_idx] == value:
            return mid_idx
        elif lst.array[mid_idx] < value:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1

    raise ValueError("The value is not in the list.")

#####

def _merge(array_a, size_a, array_b, size_b):

    new_array = [None] * (size_a + size_b)
    i = 0
    j = 0
    k = 0

    while i < size_a or j < size_b:
        if i >= size_a:
            new_array[k] = array_b[j]
            j += 1
            k += 1
        elif j >= size_b:
            new_array[k] = array_a[i]
            i += 1
            k += 1
        elif array_b[j] < array_a[i]:
            new_array[k] = array_b[j]
            j += 1
            k += 1
        else:
            new_array[k] = array_a[i]
            i += 1
            k += 1

    return new_array

#####

def _sort(array, low_idx, high_idx):

    if low_idx == high_idx:
        new_array = [None] * 1
        new_array[0] = array[low_idx]
        return new_array

    else:
        mid_idx = (high_idx + low_idx) // 2
        left = _sort(array, low_idx, mid_idx)
        right = _sort(array, mid_idx + 1, high_idx)
        return _merge(left, (mid_idx - low_idx) + 1, right, (high_idx - mid_idx))

#####

def create(array, size):
    """
    Create a new sorted list from an array.
    TODO: Implement this function. It must have O(n log n) complexity.

    :param array: An unsorted array of comparable values
    :param size: A length of a given array
    :return: A new SortedList containing the array's values in sorted order
    """

    sorted_list = SortedList()

    if size == 0:
        return sorted_list

    sorted_list.size = size
    sorted_list.capacity = size

    sorted_array = _sort(array, 0, size - 1)
    sorted_list.array = sorted_array

    return sorted_list

