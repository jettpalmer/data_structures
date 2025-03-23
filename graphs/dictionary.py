# Implements a dictionary.
# CSC 202, Lab 9
# Given code, Summer '22

import array_list as lst


class Dictionary:
    """
    A collection of key-value pairs
    NOTE: Do not alter this class.
    """

    def __init__(self):
        # The length of the backing array:
        self.capacity = 5
        # The backing array:
        self.array = [None] * self.capacity
        # The number of pairs in this dictionary:
        self.size = 0

    def __eq__(self, other):
        if type(other) != Dictionary or self.size != other.size:
            return False

        keylist = keys(self)
        for i in range(lst.size(keylist)):
            key = lst.get(keylist, i)
            if get(self, key) != get(other, key):
                return False

        return True

    def __repr__(self):
        return "Dictionary(%d, %r, %d)"\
               % (self.capacity, self.array, self.size)


class Node:
    """
    A single node in a linked list
    NOTE: Do not alter this class.
    """

    def __init__(self, key, value, next):
        # The key contained in this node:
        self.key = key
        # The value contained in this node:
        self.value = value
        # The next node in the linked list:
        self.next = next

    def __eq__(self, other):
        return (type(other) == Node
                and self.key == other.key
                and self.value == other.value
                and self.next == other.next)

    def __repr__(self):
        return "Node(%r, %r, %r)" % (self.key, self.value, self.next)

def size(dct):
    """
    Calculate the size of a dictionary.
    TODO: Implement this function. It must have O(1) complexity.

    :param dct: A Dictionary
    :return: The size of the dictionary
    """
    return dct.size


def get(dct, key, default = None):
    """
    Get the value to which a key is mapped.
    TODO: Implement this function. It must have O(1) complexity.

    :param dct: A Dictionary
    :param key: A hashable key whose value to get
    :param default: A default value
    :return: The value to which the key maps, the default if it does not exist
    """
    idx = hash(key) % dct.capacity

    # if dct.array[idx] is None:
    #     return default

    current_node = dct.array[idx]

    if current_node is None:
        return default

    else:
        while current_node.key != key:
            current_node = current_node.next

            if current_node is None:
                return default

        return current_node.value


def insert(dct, key, value):
    """
    Insert a key, overwriting any existing value, rehashing first if necessary.
    TODO: Implement this function. It must have O(1) complexity.

    :param dct: A Dictionary
    :param key: A hashable key to be inserted
    :param value: A value to which to map the key
    """
    if dct.size == dct.capacity:
        capacity = dct.capacity
        dct.capacity = capacity * 2 + 1
        new_array = [None] * dct.capacity

        for i in range(capacity):
            current_node = dct.array[i]

            while current_node is not None:
                new_idx = hash(current_node.key) % dct.capacity
                new_node = Node(current_node.key, current_node.value, new_array[new_idx])
                new_array[new_idx] = new_node

                current_node = current_node.next

        dct.array = new_array

    idx = hash(key) % dct.capacity

    if dct.array[idx] is None:
        new_node = Node(key, value, None)
        dct.array[idx] = new_node
        dct.size += 1

    else:
        current_node = dct.array[idx]
        while current_node.key != key:

            if current_node.next is None:
                new_node = Node(key, value, None)
                current_node.next = new_node
                dct.size += 1
            current_node = current_node.next

        current_node.value = value

### For Testing Purposes ##

dct = Dictionary()
insert(dct, 'a', 1)
insert(dct, 'b', 3)
insert(dct, 'f', 2)
# print(dct)

###

def remove(dct, key, default = None):
    """
    Remove a key and the value to which it maps.
    TODO: Implement this function. It must have O(1) complexity.

    :param dct: A Dictionary
    :param key: A hashable key to be removed
    :param default: A default value
    :return: The removed value, the default if the key does not exist
    """

    idx = hash(key) % dct.capacity

    if dct.array[idx] is None:
        # print('a')
        return default

    if dct.array[idx].key == key:
        removed = dct.array[idx]
        dct.array[idx] = dct.array[idx].next
        dct.size -= 1
        return removed.value

    current_node = dct.array[idx]

    if current_node.next is None:
        # print('b')
        return default

    else:
        while current_node.next.key != key:
            current_node = current_node.next

            # if current_node.next is None:
            #     print('cover')
            #     return default

        removed = current_node.next
        current_node.next = current_node.next.next

    dct.size -= 1

    return removed.value


def keys(dct):
    """
    Enumerate all of the keys in a dictionary.
    TODO: Implement this function. It must have O(n) complexity.

    :param dct: A dictionary
    :return: A new List of the dictionary's keys, in no particular order
    """
    keys = lst.List()
    j = 0

    for i in range(dct.capacity):

        current_node = dct.array[i]

        while current_node is not None:
            lst.add(keys, j, current_node.key)
            current_node = current_node.next
            j += 1

    return keys